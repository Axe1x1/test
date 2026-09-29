"""候选池：官方月度新品榜（+ 年度榜，若可解析）→ 批量拉商店元数据 → pool.csv。"""
import datetime as dt
import json
import re

import pandas as pd

import steam

MONTHS = {m.lower(): i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July",
     "August", "September", "October", "November", "December"], 1)}
SCHINESE, TCHINESE = 6, 7  # ELanguage


def _appids(node):
    """递归找出所有 {"appid": ...}。"""
    if isinstance(node, dict):
        if "appid" in node and isinstance(node["appid"], int):
            yield node["appid"]
        for v in node.values():
            yield from _appids(v)
    elif isinstance(node, list):
        for v in node:
            yield from _appids(v)


def _page_month(page):
    if page.get("start_of_month"):
        d = dt.datetime.fromtimestamp(int(page["start_of_month"]), dt.timezone.utc) + dt.timedelta(days=3)
        return f"{d.year}-{d.month:02d}"
    text = " ".join(str(page.get(k, "")) for k in ("url_path", "name")).lower()
    m = re.search(r"(january|february|march|april|may|june|july|august|september|october|november|december)[ _,]*(20\d\d)", text)
    return f"{m.group(2)}-{MONTHS[m.group(1)]:02d}" if m else None


def monthly_lists():
    body = steam.top_release_pages()
    pages = body.get("response", {}).get("pages", [])
    rows = []
    for page in pages:
        month = _page_month(page)
        for pos, appid in enumerate(dict.fromkeys(_appids(page.get("item_ids", page))), 1):
            rows.append({"appid": appid, "list_month": month, "list_pos": pos, "source": "monthly"})
    return pd.DataFrame(rows)


def _ts(v):
    return dt.datetime.fromtimestamp(int(v), dt.timezone.utc).date() if v else None


def item_row(it):
    rel = it.get("release") or {}
    rev = ((it.get("reviews") or {}).get("summary_filtered")) or {}
    langs = {l.get("elanguage"): l for l in it.get("supported_languages") or []}
    sc = langs.get(SCHINESE, {})
    basic = it.get("basic_info") or {}
    opt = it.get("best_purchase_option") or {}
    first = rel.get("original_steam_release_date") or rel.get("steam_release_date")
    return {
        "appid": it.get("appid") or it.get("id"),
        "name": it.get("name"),
        "type": it.get("type"),
        "is_free": bool(it.get("is_free")),
        "is_early_access": bool(it.get("is_early_access") or rel.get("is_early_access")),
        "steam_release": _ts(rel.get("steam_release_date")),
        "first_release": _ts(first),
        "store_review_count": rev.get("review_count"),
        "store_pct_positive": rev.get("percent_positive"),
        "zh_supported": bool(sc.get("supported")),
        "zh_audio": bool(sc.get("full_audio")),
        "tc_supported": bool(langs.get(TCHINESE, {}).get("supported")),
        "price_usd": (opt.get("original_price_in_cents") or opt.get("final_price_in_cents") or 0) / 100,
        "developers": "; ".join(d.get("name", "") for d in basic.get("developers") or []),
        "publishers": "; ".join(d.get("name", "") for d in basic.get("publishers") or []),
    }


def main():
    lists = monthly_lists()
    lists.to_csv("lists_monthly.csv", index=False)
    print("monthly list rows:", len(lists), "months:", lists["list_month"].nunique())
    appids = sorted(lists["appid"].unique().tolist())
    items = steam.get_items(appids)
    details = pd.DataFrame([item_row(it) for it in items])
    zh_names = {it.get("appid"): it.get("name") for it in steam.get_items(appids, language="schinese")}
    details["name_zh"] = details["appid"].map(zh_names)
    first = lists.sort_values("list_month").groupby("appid").first().reset_index()
    pool = details.merge(first[["appid", "list_month", "list_pos"]], on="appid", how="left")
    pool.to_csv("pool.csv", index=False)
    print(pool.head(20).to_string())
    print("pool:", len(pool))


if __name__ == "__main__":
    main()
