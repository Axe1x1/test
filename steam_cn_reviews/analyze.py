"""指标计算 + 统计 + 出图。输入 reviews.csv（fetch_reviews.py 产出）。"""
import json
import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from adjustText import adjust_text
from matplotlib import font_manager
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
from scipy import stats

import os
from matplotlib import patheffects

FONTS = [os.environ.get("CJK_FONT", ""), "/tmp/claude-0/-home-user-test/54b15a71-23f1-5ce5-a659-7ec19da27459/scratchpad/fonts/NotoSansCJKsc-Regular.otf",
         "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"]
FONT = next(f for f in FONTS if f and os.path.exists(f))
font_manager.fontManager.addfont(FONT)
mpl.rcParams.update({
    "font.family": font_manager.FontProperties(fname=FONT).get_name(),
    "axes.unicode_minus": False,
    "svg.fonttype": "none",
})

SURFACE, INK, INK2, MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#898781"
GRID, AXIS, CONTEXT = "#e1e0d9", "#c3c2b7", "#d6d5cf"
COLOR = {"B": "#2a78d6", "A": "#eb6834"}
LABEL = {"B": "2022.09–2024.08（不含黑神话）", "A": "2024.09–2026.08（黑神话之后）"}
ORDER = ["B", "A"]
BOLD = [patheffects.withStroke(linewidth=0.9, foreground=INK)]


def load(path="reviews.csv"):
    df = pd.read_csv(path)
    df["zh_share"] = df.sc_n / df.all_n
    df["zh_rate"] = df.sc_pos / df.sc_n
    df["row_rate"] = (df.all_pos - df.sc_pos) / (df.all_n - df.sc_n)
    df["all_rate"] = df.all_pos / df.all_n
    df["gap"] = df.zh_rate - df.row_rate
    df["zhtc_share"] = (df.sc_n + df.tc_n) / df.all_n
    if {"sc_n30", "all_n30"} <= set(df.columns):
        df["zh_share30"] = df.sc_n30 / df.all_n30
        df["zh_rate30"] = df.sc_pos30 / df.sc_n30
        df["row_rate30"] = (df.all_pos30 - df.sc_pos30) / (df.all_n30 - df.sc_n30)
        df["gap30"] = df.zh_rate30 - df.row_rate30
    return df


def fit(x, y):
    ok = x.notna() & y.notna()
    x, y = x[ok], y[ok]
    rho, p = stats.spearmanr(x, y)
    r, pr = stats.pearsonr(x, y)
    lr = stats.linregress(x, y)
    return {"n": int(ok.sum()), "spearman": rho, "spearman_p": p, "pearson": r, "pearson_p": pr,
            "slope": lr.slope, "intercept": lr.intercept}


def summary(df, suffix=""):
    out = {}
    for c in ORDER + ["all"]:
        d = df if c == "all" else df[df.cohort == c]
        s = {
            "n": len(d),
            "median_zh_share": d[f"zh_share{suffix}"].median(),
            "median_zh_rate": d[f"zh_rate{suffix}"].median(),
            "median_row_rate": d[f"row_rate{suffix}"].median(),
            "median_gap": d[f"gap{suffix}"].median(),
            "share_vs_zhrate": fit(d[f"zh_rate{suffix}"], d[f"zh_share{suffix}"]),
            "share_vs_rowrate": fit(d[f"row_rate{suffix}"], d[f"zh_share{suffix}"]),
        }
        sub = d[d.zh_supported.astype(bool)]
        s["share_vs_zhrate_zh_supported"] = fit(sub[f"zh_rate{suffix}"], sub[f"zh_share{suffix}"])
        if "cn_dev" in d:
            sub = d[~d.cn_dev.astype(bool)]
            s["share_vs_zhrate_ex_cn_dev"] = fit(sub[f"zh_rate{suffix}"], sub[f"zh_share{suffix}"])
        out[c] = s
    return out


def pct(v, _=None):
    return f"{v * 100:.0f}%"


def pick_labels(d, k_top=6, k_extreme=2):
    idx = list(d.nlargest(k_top, "all_n").index)
    idx += list(d.nlargest(k_extreme, "zh_share").index)
    idx += list(d.nsmallest(k_extreme, "zh_rate").index)
    return list(dict.fromkeys(idx))


def scatter(df, out_png, title, subtitle, notes, labels=None):
    fig = plt.figure(figsize=(16, 9.4), dpi=150, facecolor=SURFACE)
    gs = fig.add_gridspec(1, 2, left=0.075, right=0.985, top=0.745, bottom=0.15, wspace=0.07)
    xmin = max(0, np.floor((df.zh_rate.min() - 0.04) * 10) / 10)
    ymax = np.ceil((df.zh_share.max() + 0.03) * 20) / 20
    axes = []
    for i, c in enumerate(ORDER):
        ax = fig.add_subplot(gs[0, i], sharey=axes[0] if axes else None)
        axes.append(ax)
        ax.set_facecolor(SURFACE)
        d, other = df[df.cohort == c], df[df.cohort != c]
        ax.scatter(other.zh_rate, other.zh_share, s=26, color=CONTEXT, linewidths=0, zorder=1)
        filled = d[d.zh_supported.astype(bool)]
        hollow = d[~d.zh_supported.astype(bool)]
        ax.scatter(filled.zh_rate, filled.zh_share, s=70, color=COLOR[c], edgecolors=SURFACE,
                   linewidths=1.6, zorder=3)
        ax.scatter(hollow.zh_rate, hollow.zh_share, s=62, facecolors=SURFACE, edgecolors=COLOR[c],
                   linewidths=1.8, zorder=3)
        f = fit(d.zh_rate, d.zh_share)
        xs = np.linspace(d.zh_rate.min(), d.zh_rate.max(), 50)
        ax.plot(xs, f["intercept"] + f["slope"] * xs, color=COLOR[c], lw=2, solid_capstyle="round", zorder=2)
        p = f["spearman_p"]
        ptxt = "p<0.001" if p < 0.001 else f"p={p:.3f}"
        sign = "+" if f["slope"] >= 0 else "−"
        ax.text(0, 1.075, LABEL[c], transform=ax.transAxes, fontsize=15, color=INK, path_effects=BOLD, va="bottom")
        ax.text(0, 1.02, f"Top {len(d)} · Spearman ρ = {f['spearman']:.2f}（{ptxt}）· 中文好评率 +10pp → "
                f"中文评测占比 {sign}{abs(f['slope']) * 10:.1f}pp",
                transform=ax.transAxes, fontsize=11.5, color=INK2, va="bottom")
        texts = []
        for j in (labels or {}).get(c, pick_labels(d)):
            r = d.loc[j]
            texts.append(ax.text(r.zh_rate, r.zh_share, r.short_name, fontsize=10.5, color=INK, zorder=4))
        adjust_text(texts, ax=ax, x=d.zh_rate.values, y=d.zh_share.values,
                    arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7),
                    expand=(1.3, 1.6), force_text=(0.4, 0.6))
        ax.set_xlim(xmin, 1.0)
        ax.set_ylim(0, ymax)
        ax.xaxis.set_major_formatter(FuncFormatter(pct))
        ax.yaxis.set_major_formatter(FuncFormatter(pct))
        ax.grid(True, color=GRID, lw=0.8)
        ax.set_axisbelow(True)
        for side in ["top", "right"]:
            ax.spines[side].set_visible(False)
        for side in ["left", "bottom"]:
            ax.spines[side].set_color(AXIS)
        ax.tick_params(colors=MUTED, labelsize=11, length=0, pad=6)
        ax.set_xlabel("中文（简体）好评率", fontsize=12, color=INK2, labelpad=8)
        if i == 0:
            ax.set_ylabel("中文（简体）评测占全部评测比例", fontsize=12, color=INK2, labelpad=8)
        else:
            plt.setp(ax.get_yticklabels(), visible=False)
    handles = [
        Line2D([], [], ls="", marker="o", ms=8.5, color=COLOR["B"], mec=SURFACE, label=LABEL["B"]),
        Line2D([], [], ls="", marker="o", ms=8.5, color=COLOR["A"], mec=SURFACE, label=LABEL["A"]),
        Line2D([], [], ls="", marker="o", ms=8, mfc=SURFACE, mec=INK2, mew=1.6, label="空心 = 不支持简体中文"),
        Line2D([], [], ls="", marker="o", ms=6, color=CONTEXT, label="灰点 = 另一期（对照）"),
        Line2D([], [], color=INK2, lw=2, label="线性趋势"),
    ]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.068, 0.885), ncol=5, frameon=False,
               fontsize=11, labelcolor=INK2, handletextpad=0.4, columnspacing=1.4)
    fig.text(0.075, 0.945, title, fontsize=21, path_effects=BOLD, color=INK)
    fig.text(0.075, 0.905, subtitle, fontsize=13, color=INK2)
    fig.text(0.075, 0.035, notes, fontsize=9.8, color=MUTED, va="bottom", linespacing=1.5)
    fig.savefig(out_png, facecolor=SURFACE)
    plt.close(fig)


def main():
    df = load(sys.argv[1] if len(sys.argv) > 1 else "reviews.csv")
    if "short_name" not in df:
        df["short_name"] = df["name"]
    res = {"lifetime": summary(df)}
    if "zh_share30" in df:
        res["launch30"] = summary(df, "30")
    print(json.dumps(res, ensure_ascii=False, indent=1, default=float))
    scatter(df, "chart_preview.png", "标题待定（看数据后再写结论）", "副标题", "注释")


if __name__ == "__main__":
    main()
