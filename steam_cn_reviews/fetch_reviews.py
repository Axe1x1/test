"""对两期候选按评测数排序，取前 N 抓分语言评测汇总 → reviews.csv。"""
import datetime as dt

import pandas as pd

import steam

COHORTS = {
    "A": (dt.date(2024, 9, 1), dt.date(2026, 8, 31)),   # 黑神话之后
    "B": (dt.date(2022, 9, 1), dt.date(2024, 8, 31)),   # 前一个 24 个月
}
EXCLUDE = {2358720}  # 黑神话：悟空
PREFETCH = 80        # 每期先取 80 个候选，重排后保留前 50
TOP_N = 50
DAY = 86400


def cohort_of(d):
    for name, (lo, hi) in COHORTS.items():
        if d is not None and lo <= d <= hi:
            return name
    return None


def summarize(appid, lang, start=None, end=None):
    q = steam.review_summary(appid, lang, start, end)
    return q.get("total_reviews"), q.get("total_positive")


def main():
    pool = pd.read_csv("pool.csv", parse_dates=["first_release", "steam_release"])
    pool["first_release"] = pool["first_release"].dt.date
    pool["cohort"] = pool["first_release"].map(cohort_of)
    cand = pool[(pool["cohort"].notna()) & (~pool["is_free"]) & (~pool["appid"].isin(EXCLUDE))]
    cand = cand[cand["type"].isin([0, "0", "game"]) | cand["type"].isna()]
    picked = (cand.sort_values("store_review_count", ascending=False)
                  .groupby("cohort").head(PREFETCH))
    rows = []
    for i, g in enumerate(picked.itertuples(), 1):
        t0 = dt.datetime.combine(g.first_release, dt.time(), dt.timezone.utc).timestamp()
        row = {"appid": g.appid}
        for lang, key in [("all", "all"), ("schinese", "sc"), ("tchinese", "tc")]:
            row[f"{key}_n"], row[f"{key}_pos"] = summarize(g.appid, lang)
        # 首发窗口：发售前 7 天（抢先体验版）到发售后 30 天
        for lang, key in [("all", "all"), ("schinese", "sc")]:
            row[f"{key}_n30"], row[f"{key}_pos30"] = summarize(g.appid, lang, t0 - 7 * DAY, t0 + 30 * DAY)
        rows.append(row)
        print(f"[{i}/{len(picked)}] {g.cohort} {g.name}: all={row['all_n']} sc={row['sc_n']}")
    rev = picked.merge(pd.DataFrame(rows), on="appid")
    rev = (rev.sort_values("all_n", ascending=False).groupby("cohort").head(TOP_N)
              .sort_values(["cohort", "all_n"], ascending=[True, False]))
    rev["rank"] = rev.groupby("cohort").cumcount() + 1
    rev.to_csv("reviews.csv", index=False)
    print(rev.groupby("cohort").size())


if __name__ == "__main__":
    main()
