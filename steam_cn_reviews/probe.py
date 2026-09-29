"""探测各接口的真实返回结构，原始结果写到 raw/。"""
import json
import sys
from pathlib import Path

import steam

RAW = Path(__file__).resolve().parent / "raw"
RAW.mkdir(exist_ok=True)


def dump(name, obj):
    (RAW / name).write_text(obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, indent=1))
    print(f"-- {name}: {len(obj) if isinstance(obj, str) else len(json.dumps(obj))} bytes")


def attempt(name, fn):
    try:
        out = fn()
        dump(name, out)
        return out
    except Exception as e:  # noqa: BLE001
        print(f"!! {name}: {e}")


attempt("top_release_pages.json", steam.top_release_pages)
for method in ["GetBestOfYearPages", "GetYearTopAppReleases", "GetMonthTopAppReleases"]:
    attempt(f"{method}.json", lambda m=method: steam.get(f"https://api.steampowered.com/ISteamChartsService/{m}/v1/"))
for year in [2022, 2023, 2024, 2025]:
    attempt(f"bestofyear_{year}.html",
            lambda y=year: steam.get(f"https://store.steampowered.com/charts/bestofyear/{y}", as_json=False))
attempt("topnewreleases_april_2025.html",
        lambda: steam.get("https://store.steampowered.com/charts/topnewreleases/april_2025", as_json=False))
attempt("getitems_sample.json", lambda: steam.get_items([2358720, 1245620, 2807960]))
attempt("appdetails_sample.json", lambda: steam.appdetails(2358720))
# 黑神话：全语言 / 简中 / 指定时段（验证 date range 是否作用于 query_summary）
for lang in ["all", "schinese"]:
    attempt(f"reviews_2358720_{lang}.json", lambda l=lang: steam.review_summary(2358720, l))
attempt("reviews_2358720_all_first30d.json",
        lambda: steam.review_summary(2358720, "all", start=1724112000, end=1724112000 + 30 * 86400))
