"""Steam 数据抓取：磁盘缓存 + 按域名限速 + 重试。

所有请求结果都缓存到 cache/，重跑不会重复请求。
"""
import hashlib
import json
import time
from pathlib import Path
from urllib.parse import urlparse

import requests

ROOT = Path(__file__).resolve().parent
CACHE = ROOT / "cache"
CACHE.mkdir(exist_ok=True)

_session = requests.Session()
_session.headers.update({
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) steam-cn-review-research",
    "Accept-Language": "en-US,en;q=0.9",
})
_last_hit = {}


def _throttle(host, min_interval):
    wait = _last_hit.get(host, 0) + min_interval - time.time()
    if wait > 0:
        time.sleep(wait)
    _last_hit[host] = time.time()


def _cache_path(url, params):
    key = hashlib.sha1((url + "?" + json.dumps(params or {}, sort_keys=True)).encode()).hexdigest()
    return CACHE / f"{key}.json"


def get(url, params=None, *, as_json=True, min_interval=1.0, tries=7, use_cache=True):
    path = _cache_path(url, params)
    if use_cache and path.exists():
        payload = json.loads(path.read_text())
        return payload["body"]
    host = urlparse(url).netloc
    delay, err = 5, None
    for _ in range(tries):
        _throttle(host, min_interval)
        try:
            r = _session.get(url, params=params, timeout=45)
        except requests.RequestException as e:
            err = repr(e)
        else:
            if r.status_code == 200:
                body = r.json() if as_json else r.text
                path.write_text(json.dumps({"url": r.url, "body": body}, ensure_ascii=False))
                return body
            err = f"HTTP {r.status_code}"
            if r.status_code not in (429, 500, 502, 503, 504):
                break
        time.sleep(delay)
        delay = min(delay * 2, 120)
    raise RuntimeError(f"GET failed: {url} {params} -> {err}")


# ---------- 榜单 ----------

def top_release_pages():
    """官方月度新品榜（store.steampowered.com/charts/topnewreleases）。"""
    return get("https://api.steampowered.com/ISteamChartsService/GetTopReleasesPages/v1/")


# ---------- 商店元数据（批量） ----------

def get_items(appids, country="US", language="english"):
    items = []
    for i in range(0, len(appids), 40):
        chunk = [int(a) for a in appids[i:i + 40]]
        req = {
            "ids": [{"appid": a} for a in chunk],
            "context": {"language": language, "country_code": country, "steam_realm": 1},
            "data_request": {
                "include_basic_info": True,
                "include_release": True,
                "include_reviews": True,
                "include_supported_languages": True,
                "include_all_purchase_options": True,
                "include_tag_count": 0,
            },
        }
        body = get("https://api.steampowered.com/IStoreBrowseService/GetItems/v1/",
                   {"input_json": json.dumps(req)}, min_interval=0.5)
        items += body.get("response", {}).get("store_items", [])
    return items


def appdetails(appid, cc="us", lang="english"):
    body = get("https://store.steampowered.com/api/appdetails",
               {"appids": int(appid), "cc": cc, "l": lang}, min_interval=1.6)
    return (body or {}).get(str(appid), {})


# ---------- 评测汇总 ----------

def review_summary(appid, language="all", start=None, end=None):
    """返回 query_summary：total_reviews / total_positive / total_negative / review_score_desc。

    purchase_type=all：包含 key 激活（国区大量玩家通过第三方渠道购买 key）。
    off-topic（刷评）过滤保持 Steam 默认，与商店页展示口径一致。
    start/end（unix 秒）给定时只统计该时间段内发布的评测。
    """
    params = {
        "json": 1,
        "language": language,
        "purchase_type": "all",
        "review_type": "all",
        "filter": "recent",
        "num_per_page": 0,
    }
    if start is not None:
        params.update(start_date=int(start), end_date=int(end), date_range_type="include")
    body = get(f"https://store.steampowered.com/appreviews/{int(appid)}", params, min_interval=0.8)
    return body.get("query_summary", {}) if isinstance(body, dict) else {}
