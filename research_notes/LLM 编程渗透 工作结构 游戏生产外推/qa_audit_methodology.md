# QA Audit — Comparative methodology (coding → game production)

**Scope.** Independent methodology review of `comparative_methodology_frameworks.md` (primary; 949 lines, read in full). Evidence notes read for operability: `software_work_composition_shift.md` (in full), and the synthesis/takeaway sections plus the sections that feed the indicator ladder of `coding_adoption_penetration.md` (§1, §7), `ai_code_share_productivity.md` (§1–§5), `ai_coding_value_evidence.md` (§6–§8), `creative_content_industries_analog.md` (§6, §8), `game_industry_ai_adoption_pipeline.md` (§6, §8 + summary table), `game_ai_opportunities_frontier.md` (§7, §8), `game_value_economics.md` (§2–§6). Existing audit read in full: `qa_audit_game_creative.md`. **Not available at review time:** `qa_audit_coding_adoption_share.md`, `qa_audit_workmix_value.md`, `qa_audit_game_value.md` (not yet in the folder), so figures from the coding and game-value notes are used here "as reported, with the note's own tag".

**Date.** 2026-09-28.

**Method.** (1) Every framework and paper in the note was checked for attribution, year, venue and claim against the reviewer's bibliographic knowledge; items the reviewer could not settle from knowledge were checked online. (2) Four primary pages on the fetchable domains were opened to verify the load-bearing Anthropic and DORA figures (anthropic.com: Jan 2026 Economic Index report; "How AI is transforming work at Anthropic"; Feb 2025 Economic Index; software-development report; cloud.google.com: DORA 2025 announcement). (3) Four WebSearch queries ran successfully (Gans & Goldfarb w34639; Autor & Thompson w33941; Humlum & Vestergaard w33777; Karpathy "Verifiability"). (4) Arithmetic and internal-consistency checks (Amdahl table, Ukie share arithmetic, the Meyer-based C/E/D baseline, cross-note figure conflicts). (5) Each element of the proposed design was checked against what the evidence notes can actually populate.

**Limits.** NBER, arXiv, JSTOR, Steam trackers and survey vendors were not fetched (proxy 403); seminal papers are graded from memory and the table says so. No game-side figure was checked at source here; the game/creative audit's corrections are taken as given. Grades: **OK** = attribution and characterization correct as far as the reviewer can tell; **VERIFIED** = confirmed at source or by search this session; **CORRECTED** = something to change; **VERIFY** = plausible but the coordinator should check (queued at the end).

---

## 1. Verdict

The methodology note is theoretically literate, unusually honest about what is established versus proposed, and its citations are almost all right: I found **no misattributions**, only one retitled working paper (Humlum & Vestergaard w33777 is now "Still Waters, Rapid Currents"), two small figure slips (Anthropic staff use Claude in 59% of work, not 60%; the Jan 2026 projection falls to 0.6–0.8 pp/yr when the success and complementarity adjustments are combined, not only to 0.7–0.9), and three over-stretched applications (Kremer's O-ring is multiplicative, not "weakest link", so H-A3 conflates two functional forms; the Pearl–Bareinboim "selection diagram" is used as a metaphor, not as transportability calculus; Autor–Thompson's expertise logic is cited only for the direction that favors the note's wage prediction). The one substantive error is a **mis-scaled falsifier for Proposition B**: the "≥1 pp/yr" threshold is borrowed from Anthropic's economy-wide projection and applied to the software sector, where the BLS 2025 print for software publishers (+12.9% labor productivity, per `ai_coding_value_evidence.md`) already trips it for reasons the same note judges unrelated to AI value. The larger problems are structural rather than factual: the apparatus is far too big for a report (6 units × 9 indicators × 5 value rungs × 10 transfer dimensions × 14 hypotheses × 8 phases × 14 pitfalls); it does not use two sibling notes (`ai_coding_value_evidence.md`, `game_value_economics.md`) that hold the strongest evidence for and against both user propositions; its transfer classes omit runtime/AI-native uses and the China–West split that the game notes show to be decisive; and its three-way work taxonomy conflicts at the boundary with the one used in `software_work_composition_shift.md` (telling an agent what to build is "D" in one note and "C/E" under the other's rule). None of this undermines the design. It needs to be cut to a spine, reconciled, and populated with evidence already in the folder. On faithfulness: the two user propositions are taken seriously and the note preserves the main upside argument (Aguiar–Waldfogel "more draws"; Acemoglu–Restrepo "new tasks"), but the coding-side counter-evidence (a $10B+ tool industry, faster firm formation, consumer surplus, the 2025 BLS print) is absent from the note and must be added, and the game-side upside cases (UGC platforms, small-team hits, live-ops cost relief, AI-native experiences) need their own indicators so the report does not read as a one-sided "volume ≠ value" brief.

---

## 2. Theory-citation check table

| Framework / paper | As stated in note | Status | Correct attribution or characterization / comment |
|---|---|---|---|
| Autor, Levy & Murnane (2003) | QJE 118(4); routine vs non-routine tasks; tasks not jobs | OK | Citation correct. **Application caveat:** LLMs automate non-routine cognitive *execution*, so the routine/non-routine split does not predict the current shift; `software_work_composition_shift.md` §7 makes this point ("break with the Autor-style lens"); the methodology should adopt it and replace routine/non-routine with verifiable/non-verifiable (Acemoglu 2024 easy/hard-to-learn). |
| Acemoglu & Restrepo (2019) | JEP 33(2); displacement vs reinstatement | OK | Correct, including the "three decades of slower employment growth" reading. |
| Autor & Thompson, "Expertise" | NBER w33941, June 2025 | VERIFIED | Confirmed by search (NBER w33941; SSRN 5315761; 303 occupations, 1980–2018). **Application is one-sided:** the note uses it only for "wage premium of senior C/D ↑". The same framework predicts *lower* wages where automation removes expert tasks and de-expertises what remains; the creative note documents exactly that (MTPE and paintover priced at a discount; hands-on debugging being automated). The prediction must be conditional: premium rises only where the residual tasks are more expert. |
| Acemoglu (2024), "Simple Macroeconomics of AI" | NBER w32487; ≤0.66% TFP/10 yrs; <0.53% with hard tasks | OK | Correct (also published in Economic Policy 2025). |
| Agrawal, Gans & Goldfarb | NBER w24243; prediction cheap, judgment complements | OK | "Prediction, Judgment and Complexity" (2018); popular statement in *Prediction Machines* (2018). |
| Kremer (1993), O-ring | QJE 108(3); quality multiplies across tasks | OK on citation; **CORRECTED on application** | O-ring production is *multiplicative* in task quality (q1·q2·…·qn), which still allows a strong dimension to offset a weak one in logs. H-A3 ("title value governed by the weakest quality dimension") is a *weakest-link / min* claim, a different functional form. The test should compare three specifications: additive, multiplicative (log-additive) and CES with σ<1 or min. Gans–Goldfarb use the multiplicative form. |
| Gans & Goldfarb, "O-Ring Automation" | NBER w34639, Jan 2026; SSRN 5962594 | VERIFIED | Confirmed (NBER w34639, 2026; SSRN 5962594). The four bullet claims match the abstract. The block quoted "in their words" is a close paraphrase of the abstract, not a checked verbatim quote; present it as a paraphrase. |
| Baumol (1967) | AER 57(3); unbalanced growth | OK | Correct. Application requires that C/D wages do not fall (see Autor–Thompson row); otherwise the cost share of C/D can stay flat even as E hours fall. |
| Aghion, Jones & Jones (2017) | NBER w23928; "constrained… by what is essential and yet hard to improve" | OK | Correct; the quote is from the paper's Baumol section (also in *The Economics of AI: An Agenda*, 2019). |
| Amdahl (1967) | AFIPS; S = 1/((1−p)+p/s) | OK | Citation and formula correct. The H-A4 table arithmetic checks: p=0.25 gives 5.2% (s=1.26), 12.5% (s=2), 25% (s→∞). Caveat to add: Amdahl bounds time for a *fixed* scope; under Jevons-type scope expansion the bound is on time-per-scope, not on cost. |
| Theory of constraints (Goldratt) | Wikipedia overview | OK | Cite Goldratt & Cox, *The Goal* (1984) rather than Wikipedia. |
| Faros AI (2025) | +21% tasks, +98% PRs, +91% review time, +154% PR size, +9% bugs; no org-level gain | VERIFY (industry) | +21/+98/+91 are consistent across three sibling notes (via search summaries). The sibling coding note explicitly says PR size +154% and bugs +9% were **not verified**; the methodology presents them as report content. Mark them "as cited elsewhere". |
| DORA 2024 | +25% adoption ↔ −1.5% throughput, −7.2% stability, +7.5% doc quality | OK | Matches the 2024 report's modelled associations (also +2.1% individual productivity). |
| DORA 2025 | Positive throughput, still instability; "AI doesn't fix a team; it amplifies what's already there" | VERIFIED | Fetched cloud.google.com: 90% use AI; positive association with throughput and product performance; negative with delivery stability; the quote is verbatim; ~5,000 respondents; seven capabilities in the AI Capabilities Model. |
| Bessen (2019) | Economic Policy 34(100); employment rises if demand elasticity >1; textiles/steel/autos | OK | Correct. Keep distinct from Jevons: Bessen is about *employment*, Jevons about *output/consumption*. |
| Jevons paradox (Alcott 2005) | Ecological Economics; efficiency raises total use | OK | Alcott, "Jevons' paradox", Ecol. Econ. 54(1), 2005. Correct. |
| Anthropic internal study (Dec 2025) | Aug 2025 survey of 132; 53 interviews; 60% of work; +50%; 27% new tasks | **CORRECTED** (minor) | Fetched: 132 engineers/researchers, 53 interviews, 200k transcripts; Claude used in **59%** of work (28% a year earlier); +50% (from +20%); 27% "wouldn't have been done otherwise"; >half can fully delegate only 0–20%. Add the output metric the note omits: **67% more merged PRs per engineer per day** after Claude Code adoption. |
| App Store supply surge | ~560k new apps H1 2026; downloads +2–3% | VERIFY (press) | Sibling note gives Appfigures counts (+60% Q1 2026, +104% April). Download-growth figures unverified; already flagged in the note. |
| Newzoo attention constraint | ≥6-year-old games 67% of PC playtime; new releases 12–13% of playtime | VERIFY (industry) | Not checked at source; consistent with `game_value_economics.md` (PC/console play time −1% in 2025; new releases 21% of Steam H1 2026 *revenue*, a different metric — do not conflate). |
| Rosen (1981) | AER 71(5); superstars | OK | Correct: imperfect substitution + joint consumption technology → convex returns. |
| Caves (2000) | HUP; seven properties | OK | Correct list (nobody knows; art for art's sake; motley crew; infinite variety; A list/B list; time flies; ars longa). |
| De Vany & Walls (1999) | J. Cultural Economics 23; stable Paretian, infinite variance | OK | "Uncertainty in the Movie Industry: Does Star Power Reduce the Terror of the Box Office?", 23(4), 285–318. Correct. |
| Steam heavy tail (SteamDB, Gamalytic, GamesRadar) | 19,468 releases; median $249; top 1% = 84.5% | VERIFY (industry) | Model-based; consistent with the game notes. **Harmonize the median:** $249 is the Gamalytic estimate for *all 2025 releases*; `game_value_economics.md` cites "median paid game under $4k" for the whole catalog. State both with their bases. |
| Brynjolfsson, Rock & Syverson (2021) | AEJ: Macro 13(1); Productivity J-curve | OK | Correct. |
| David (1990) | AER P&P 80(2); dynamo | OK | Correct. |
| Eloundou et al., "GPTs are GPTs" | Science 384; arXiv 2303.10130; 80%/19%; 47–56% | OK | Add years: arXiv March 2023; Science 384(6702), June 2024. Figures correct. |
| Felten, Raj & Seamans (AIOE) | SMJ 42(12); arXiv 2303.01157 | OK | SMJ 2021, "Occupational, industry, and geographic exposure to artificial intelligence"; LLM variant 2023. Correct. |
| Anthropic Economic Index (Feb 2025) | 1M conversations → ~20k O*NET tasks; 37.2% vs 10.3%; 57/43; 36%/4%; caveats | VERIFIED | All figures confirmed at source. Add one stated caveat the note omits: the sample is Claude.ai Free/Pro only (no API/Enterprise). |
| Anthropic software-development report (Apr 2025) | 79% vs 49% automation; feedback loop 35.8% vs 21.3% | VERIFIED | Confirmed; also directive 43.8% vs 27.5%; 500k interactions, Apr 6–13 2025. |
| Anthropic "economic primitives" (Jan 2026) | 1.8 pp/yr → 1.0–1.2 (success-adjusted) → 0.7–0.9 (σ=0.5); 70%/9× and 66%/12×; selection caveat | VERIFIED, **incomplete** | Confirmed: 1.8 → 1.2 (Claude.ai) / 1.0 (API) after success adjustment; 0.7–0.9 with complementarity alone; **0.8 (Claude.ai) / 0.6 (API) with both adjustments** — the note should quote the combined 0.6–0.8 since that is the scenario it uses (complements). Selection quote is verbatim. |
| Doshi & Hauser (2024) | Science Advances; individual ↑, collective diversity ↓ | OK | 10(28), eadn5290. Correct. |
| Zhou & Lee (2024) | PNAS Nexus 3(3); +25% productivity, +50% favorites/view; "expanding but inefficient idea space" | OK on findings; VERIFY quote | Findings correct (4M+ artworks, 50k+ users; peak novelty ↑, average ↓). The paper's own term is "generative synesthesia"; the quoted phrase was not verified. |
| Dell'Acqua et al. (2023) | SSRN 4573321; 758 consultants; +12.2%/+25.1%/+40%; −19 pts outside frontier | OK | HBS WP 24-013. Correct. |
| Noy & Zhang (2023) | Science 381; −40% time, +18% quality | OK | 381(6654), 187–192. Correct. |
| Brynjolfsson, Li & Raymond | NBER w31161; +14% avg, +34% novices | OK | "Generative AI at Work" (2023; QJE 2025). Correct. |
| Hui, Reshef & Zhou (2024) | Organization Science 35(6); −2% jobs, −5.2% earnings | OK | Correct. |
| Peng et al. (2023) | arXiv 2302.06590; 55.8% faster | OK | Correct (95 developers, HTTP server task). |
| Cui et al. | 4,867 developers; +26.08% (SE 10.3%); Management Science | OK | Correct. |
| METR (Jul 2025; Feb 2026 redesign) | 16 devs, 246 tasks, −19%; forecast +24%, believed +20% | OK | Correct; sibling note gives the Feb 2026 details. |
| Humlum & Vestergaard (2025) | NBER w33777; "Large Language Models, Small Labor Market Effects"; effects >2% ruled out; ~3% time savings | **CORRECTED** (title) | The NBER page now carries the revised title **"Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI"** (same w33777; earlier title as cited). The 2% bound is confirmed ("ruling out effects larger than 2% two years after adoption"); time savings ≈2.8%. |
| Bick, Blandin & Deming | NBER w32966; 1–5% of hours AI-assisted; 1.4% time savings; adoption table (~40% / 23% / 9%) | OK on headline; VERIFY table | Headline figures consistent with the paper's updated version; the three table shares were not checked. |
| GitClear (2025) | 211M lines; duplication 8×; moved lines 24.1% → 9.5% | OK (industry) | As reported in the sibling note; vendor data. |
| Brynjolfsson, Chandar & Chen, "Canaries" | 13% (2025) vs 16% later; devs 22–25 −20% | VERIFY | Version conflict already flagged by the note; the Aug 2026 version reportedly says "19% below counterfactual". Cite one version with its date. |
| Kahneman & Lovallo (1993) | Management Science 39(1) | OK | Correct. |
| Flyvbjerg (2006) | reference-class forecasting; arXiv 1302.3642 | OK | Project Management Journal 37(3), 2006. Correct. |
| Mellers et al. (2014) | Psychological Science; GJP | OK | 25(5), 1106–1115. Correct. |
| Gentner (1983) | Cognitive Science 7(2); structure-mapping | OK | Correct. |
| Pearl & Bareinboim (2014) | Statistical Science 29(4); transportability, selection diagrams | OK on citation; **application over-stretched** | The note's "mark where the game task differs by ≥2 points" is a scoring heuristic, not the do-calculus. Present it as *structured analogy with explicit difference nodes* and lean on Cartwright & Hardie; do not claim formal transportability. |
| Cartwright & Hardie (2012) | OUP; "it worked there" | OK | Correct. |
| Vivalt (2020) | JEEA 18(6) | OK | Correct. |
| Bass (1969) | Management Science 15(5) | OK | Correct. |
| Griliches (1957) | Econometrica 25(4) | OK | Correct. |
| Comin & Hobijn (2010) | AER 100(5); 15 technologies, 166 countries; ~45-year lag | OK | Correct. |
| Comin & Mestieri (2018) | AEJ: Macro 10(3); lags converge, intensity diverges | OK | Correct. |
| Lead–lag diffusion (Takada & Jain 1991) | via a 2020 review | OK | Add the original: Takada & Jain, Journal of Marketing 55(2), 1991. |
| del Rio-Chanona, Laurentsyeva & Wachs (2024) | PNAS Nexus 3(9); Stack Overflow −25% | OK | Correct. |
| Hoffmann et al., "Generative AI and the Nature of Work" | SSRN 5007084; RD on Copilot eligibility; "millions of GitHub panel observations over two years" | OK on findings; VERIFY design wording | Coding +12.4%, PM −24.9% consistent across notes. The RD is on the top-maintainer threshold for free Copilot; the "millions of observations" description was not checked. |
| Goodman-Bacon (2021); Callaway & Sant'Anna (2021) | J. Econometrics | OK | Both 225(2), 2021. Correct. |
| Waldfogel (2017) | JEP 31(3); films ~500 → ~1,200 → ~3,000 | OK on citation; VERIFY counts | "How Digitization Has Created a Golden Age…" correct; the three film counts not checked. |
| Aguiar & Waldfogel (2018) | JPE 126(2); NBER w22675 | OK | Correct. |
| Waldfogel (2012) | J. Law & Economics 55(4); quality after Napster | OK | Correct. |
| Brynjolfsson, Collis & Eggers (2019) | PNAS; massive online choice experiments | OK | 116(15). Correct. |
| Teece (1986) | Research Policy | OK | 15(6), 285–305. Correct. |
| Zhu & Zhang (2010) | Journal of Marketing 74(2) | OK | Correct. |
| Acemoglu, Autor, Hazell & Restrepo (2022) | JOLE 40(S1) | OK | Correct. |
| Jason Wei, "Asymmetry of verification and verifier's law" (Jul 2025) | quoted law | VERIFY (framing) | Not fetched; wording consistent with secondary coverage. The note correctly refuses to attribute its rubric to Wei. |
| Karpathy, "Verifiability" (Nov 2025) | "Software 1.0 … specify; Software 2.0 … verify"; resettable/efficient/rewardable | VERIFIED | Confirmed by search: karpathy.bearblog.dev/verifiability/, 17 Nov 2025; quotes and the three properties match. |
| Karpathy, "Software Is Changing (Again)" (Jun 2025) | autonomy slider; partial-autonomy apps | OK | YC AI Startup School talk, June 2025. Correct. |
| RLVR: Tülu 3; DeepSeek-R1 | arXiv 2411.15124; 2501.12948 | OK | Correct. |
| METR time horizons | arXiv 2503.14499; ~7-month doubling; 16 messiness factors | OK | Correct. |
| GDPval | arXiv 2510.04374; 1,320 tasks, 44 occupations; ~48% win-or-tie; ~66% grader agreement | OK (VERIFY low priority) | Consistent with the reviewer's knowledge of the Sept 2025 release. |
| USCO Part 2 (Jan 29, 2025) | prompts alone insufficient | OK | Correct. |
| Quantic Foundry (Dec 2025) | 85% negative; 62% "very negative"; 7.6% approve | VERIFY / harmonize | `game_value_economics.md` says 63% chose the most negative option; N=1,799 opt-in. Harmonize and label the sample. |
| Ukie census via Statista | programming ~19%, art ~16%, design ~11%, QA ~8%, PM ~8% | VERIFY | Year (2021/2022) and definitions unverified, as the note says. It is a *whole-industry workforce* split (publishers, services, business roles included), not a production-cost split; the note's "≈31% of core production roles" arithmetic is right (19/62). |
| Meyer et al. (2019), IEEE TSE (in sibling note) | 5,928 Microsoft developers time diary | OK | Correct ("Today Was a Good Day"). |

**Net:** 0 misattributions; 3 corrections (Anthropic 59%; combined 0.6–0.8 pp/yr; Humlum–Vestergaard retitle); 3 application caveats (O-ring vs min; Pearl–Bareinboim as metaphor; Autor–Thompson two-sided); ~10 VERIFY items, all industry figures or exact quotes.

---

## 3. Coherence and parsimony: what to keep as the spine, what to relegate

**Diagnosis.**
1. **Duplication.** The indicator funnel (I1–I9) and the value ladder (V0–V4) overlap almost one-to-one (I5=V0, I6=V2, I7=V3, I8=V4; V1 "surviving volume" is the same idea as I4's survival weighting). Present one ladder.
2. **Six units of analysis** is two too many for a report: L2 (workflow) is a property of L1 tasks; L5 (firm) is where adoption timing and cost structure live but the notes have almost no studio-level data. Keep four: task (with pipeline stage), discipline × seniority, product, market.
3. **Ten transfer dimensions** collapse naturally into five gates plus one switch (see §5); the full rubric belongs in an appendix.
4. **Phases P0–P7** (pre-registration, Delphi panels, Bass lead–lag fits, staggered DiD, synthetic control, within-studio RCTs, Brier scoring) describe a multi-year research program, not the method of this report. Relegate to "如果要做严格研究" (appendix); keep only the parts the report actually performs: reference classes, task-level transfer scoring, hypothesis tests on existing data, and a monitoring dashboard.
5. **Fourteen hypotheses** (H-A1–4, H-B1–4, G1–6) can be cut to seven without losing the user's two propositions.
6. **Missing inputs.** The note's scope list omits `ai_coding_value_evidence.md` and `game_value_economics.md`. The former holds the counter-evidence to Proposition B and the mechanism ranking; the latter holds the Steam AI-disclosure performance data (the only direct game-side test of value), the four game-native natural experiments (open Steam, hyper-casual, UGC platforms, mini-games), hit base rates, and small-team-hit cases. Both must feed the spine.
7. **Taxonomy conflict.** `software_work_composition_shift.md` files "spec refinement, orchestrating/supervising agents" under D; the methodology's rule files "output is itself a brief or spec" under C and "turn an existing spec into an artifact" under E. Telling an agent to implement a feature is therefore D in one note and C/E in the other. Resolve with one rule (§5.3).
8. **Transfer rule direction.** "Treat the coding effect as an upper bound" is wrong for tasks that score *higher* than coding on the gates (metric-verified ad creatives; China 2D outsourcing, where substitution ran faster and deeper than in coding). The bound runs in the direction the gate comparison indicates.
9. **Missing classes.** The transfer priors cover production tasks only. Runtime/AI-native uses (LLM NPCs, companions, generative UGC, world models) are *new tasks* in Acemoglu–Restrepo's sense, not transfers, and need their own class judged on demand expansion. Non-craft work (research, admin, marketing, community), which carries the highest adoption in every survey, is also absent.
10. **No regional split.** The game notes' most robust finding is that China leads in art and ad creatives while the West leads in code assistance and is gated by unions, disclosure rules and audience backlash. T8/T9 differ by region; the map needs two columns.

**Recommended core methodology (the spine) — 报告主干（可直接改写进报告）**

> 以下用中文给出，供报告作者改写；括号内为英文术语。全部细节（十维迁移量表、六层单元、P0–P7 研究阶段、14 项陷阱）移入附录。

**§0 研究问题与两条命题。** 报告回答三问（编程领域 2022-11 以来的采用/渗透/AI 贡献趋势；创意—执行—决策三类工作占比如何变化及原因；向游戏生产外推）。用户的两条方法论命题——(a) 游戏的价值主要来自创意与打磨而非编码；(b) 编程领域"产量 ≠ 价值"，尚未见到行业级增量价值——被写成可证伪假设（§6），而不是前提。

**§1 分析单元（四层，匹配规则）。**
- 任务（task，含其所在流水线阶段）→ 职能×资历（discipline × seniority）→ 产品（title / 赛季）→ 市场（平台 / 区域）。
- 匹配规则：编程侧任务级效应（如 RCT 的 +26%）只能作为游戏侧*任务级*效应的证据；产品级、市场级结论必须有同级证据，或经过显式聚合模型（任务→流程：Amdahl；流程→产品：O-ring/CES，σ<1；产品→市场：注意力约束下的重尾需求）。
- 每个数字都标注所属层级；"层级错配"是最常见的错误（把编程 RCT 的任务级增益直接说成游戏行业价值）。

**§2 指标阶梯（七级 + 一个诊断侧栏）。** 采用率（adoption，extensive：任何使用/每周/每日）→ 渗透率（penetration，intensive：AI 介入的任务实例或工时份额）→ AI 贡献份额（AI contribution：以*存活的已发布产出*计，不以"接受的建议"或"生成的字符"计）→ 产出量（volume）→ 质量（quality：可验证指标 + 盲评 + 多样性）→ 价值创造（value created：收入、时长、消费者剩余，按分布而非均值报告）→ 价值捕获（value captured：工作室/劳动/平台/引擎/AI 供应商/消费者各得多少）。侧栏：瓶颈与成本结构诊断（评审时延、返工率、C/E/D 成本份额）。
- 第 0 级"暴露度"（exposure）只表示潜力，不作为证据；线性加总的暴露指数在任务互补时高估替代（Gans–Goldfarb）。
- 三条报告规则：不单独报告产量而不报同一单元的价值；游戏侧报告分布（中位数、P90、命中率、头部份额）；"AI 贡献"必须写明分母与定义。
- 关键比率：供给的价值弹性 %ΔV/%ΔQ，须控制玩家基数与时长增长（Steam 十年内发行量 ×7 而总收入创新高，是需求增长而非供给的功劳）。

**§3 三类工作的操作定义与一条分类规则。**
- C 创意/定意图：产出是"应该存在什么"的新规格（概念、风格、机制、叙事、架构）；无参照答案，事后由品味或受众判断。
- E 执行/量产：把*既有*规格或参照变成可校验的制品（实现、资产、本地化、测试用例）。
- D 决策/验收：产出是判断、选择或参数（评审、验收、取舍、调参、砍需求）。
- 规则：无规格且产出本身是规格→C；有规格且产出可校验→E；产出是判断→D。按任务实例打分，允许混合份额；两位编码者，κ≥0.7。
- 补充标签 **E-委托（E-delegated）**：人向 agent 下达执行指令、看它跑、再接受的时间单独标出。否则"E↓、D↑"可能只是把同一活动改了名。
- 两本账分开：人时账本（human-hours ledger）与产出账本（output ledger）。编程证据表明产出账本的变化远大于人时账本。
- 第三类宜称"决策/验收"而非"决策/迭代"：机械迭代（跑—报错—改）正被 agent 吸收，留给人的是接受与否、取舍与优先级。

**§4 迁移条件（五道门 + 一个开关）。** 对每个游戏任务与其最相近的编程任务比较：
1. 可验证性与反馈回路（verifiability & feedback loop；原 T1+T2+T5）：有无便宜、客观、可重复的自动校验；一次尝试到反馈要多久；错误能否在触达玩家前被捕获。
2. 耦合与一致性（coupling & consistency；T3+T7）：产出能否单独验收；是否必须与风格、正典、关卡节奏在成百上千资产间保持一致。
3. 数据与流水线契合（data & pipeline fit；T4）：制品是否文本化、有大规模可用语料；能否直接进入引擎/DCC/CAT 工具链。
4. 权利与接受度（rights & acceptance；T8+T9，**中西分列**）：版权可保护性、训练数据授权、表演者同意（SAG-AFTRA 2025 IMA）、平台披露规则、玩家可见性与污名。
5. 品味/隐性知识（taste；T6）：验收是否依赖不可编码的判断。
- 开关：需求机制（demand mechanism；T10）——更便宜、更多的产出是否提高付费意愿（需求弹性、B2B 生产率），还是只增加供给（注意力约束、重尾）。
- 规则：按*任务*而非职能评分；决定"原样迁移 / 作为界限迁移（方向由门的比较决定）/ 用游戏数据重估"；注明日期与模型能力水平，每 6 个月重评；把"验证工程"（自动试玩、风格一致性分类器、平衡模拟器、评审 GUI）作为使任务变得更像编程的单独驱动因素跟踪。

**§5 迁移分类（五类，见 §5 表）。** 高 / 有条件 / 仅产量（两个亚型：品味型——可见创意资产，有污名与同质化；军备竞赛型——买量素材，产量转化为竞争而非价值）/ 低 / **新任务（N）**——运行时与 AI 原生体验，不是编程增益的迁移，按需求扩张证据评估。

**§6 假设与证伪条件（七条 + 三分诊断）。**
- 命题 A：A1 编程是游戏生产劳动与成本的少数（证伪：收入加权样本中编程 ≥50% 的人月或薪酬）；A2 创意与打磨属性对付费意愿的解释力高于技术/产量属性（证伪：技术或产量属性解释同等或更多方差；或盲测下 AI 美术不可分辨*且*无披露惩罚）；A3 产品价值对最弱维度敏感（证伪：加性模型拟合同样好；打磨补丁对评价/销量无影响）；A4 仅限编程的 AI 增益对整款游戏的工期/成本影响受 Amdahl 上界约束（p=0.25 时 ≤25%）。
- 命题 B：B1 2023 年以来软件的产量指标远快于价值指标（证伪条件须改写，见下）；B2 瓶颈机制（证伪：吞吐上升而评审时延与不稳定性不升）；B3 J 曲线（证伪：重投入组织三年后仍无追赶）；B4 价值外溢（证伪：软件企业人均收入与利润率随任务级增益同步上升）。
- 三分诊断："尚未（J 曲线）/ 不在生产者收入里（外溢给用户与 AI 供应商）/ 根本没有（瓶颈与质量抵消）"。三者对游戏的预测不同，报告必须写明当前证据更支持哪一个（编程证据笔记的排序：瓶颈 > 竞争性传递 > J 曲线 > 质量债 > 计量遗漏）。
- 游戏侧预测精简为四条：G1 产量稀释（发行量↑、中位收入↓、集中度不降、供给价值弹性≈0）；G2 可见 AI 内容有需求惩罚、收益取决于打磨；G3/G4 合并：瓶颈与成本份额向 C/D 移动（需工作室数据）；G5 初级执行岗先减少（含外包）。G6（同质化）作为 G1 的子指标。

**§7 外部视角（参考类）。** 编程 2022–26（领先市场）+ 五个历史案例（DTP、CAD、数码摄影/微图库、DAW/数字音乐、CGI/VFX）+ **游戏自身的四个自然实验**（免费引擎 + Steam 开放、超休闲、UGC 平台、微信小游戏；见 `game_value_economics.md` §3）。共同模式：执行岗位与单价坍缩、产量爆炸、价值向平台与头部集中、顶部质量不降、创意方向不消失、组织重构带来滞后。

**§8 监测。** 8–12 个领先指标的季度仪表盘（§7 表），每个指标写明来源、当前值与"改变结论的阈值"。

---

## 4. Evidence-operability table

| Spine element | Evidence available now (from the notes) | Proxy / how to label uncertainty |
|---|---|---|
| Units: game task inventory (L1) labeled C/E/D and scored on gates | None. No public game task inventory; O*NET has few game tasks. Discipline-level material exists: `game_industry_ai_adoption_pipeline.md` §8 table (discipline × adoption × claimed gains × blockers); creative note §8 tiers | Present the discipline × task matrix as **the researchers' judgment**, evidence-tagged per cell. Say explicitly that task-level scoring for games is a proposal (P1/P2 in the appendix). |
| Adoption — coding | Strong series: SO 44% (2023) → 62% (2024) → 84% (2025); DORA 76% → 90%; JetBrains 85% → ~90% (Jan 2026); daily use 51% (SO 2025); agents 14% daily (mid-2025) → one in three GitHub PRs agent-involved (Jul 2026) | Report the three nested curves (breadth saturated; intensity mid-curve; delegation exponential). Label vendor figures (GitHub/Microsoft) as vendor. |
| Adoption — games | The only clean worker-level series: GDC personal use 31% (Jan 2024) → 36% (Jan 2026); studio staff 30% vs publisher/support 58% (verified in the game audit). Company-level "any use": GDC 2025 52%; vendor 90–96% (Unity, Google/Harris). China: 80–86% in white papers (tiny large-firm samples) | Lead with the GDC series; label every other figure by layer (studio any-use / worker personal use / player-facing shipped content). Never chain Unity's yearly figures into a series. |
| Penetration (intensity) — coding | DORA 2025 median ~2 h/day; Anthropic 59% of work (frontier); Claude Code automation 79%; directive share 27% → 39% → 32% | Good for direction; frontier data over-represent AI-intensive settings — say so. |
| Penetration — games | None measured. Proxies: task use among AI users (GDC: research 81%, code 47%, prototyping 35%; Unity 2026: coding 62%, narrative 44%, playtesting 35%); China company claims (37 Games >80% of 2D "AI-involved") | Label task shares as "conditional on being an AI user" (GDC code ≈17% of all respondents). Company claims as "claimed; AI-involved then human-refined". |
| AI contribution share — coding | Company claims with shifting definitions (Google 25% → 50% → 75%); independent: Daniotti ~30% of US public Python functions (end-2024); SemiAnalysis ~4% of public commits by Claude Code (Feb 2026); GitHub bot-authored PRs 0.3–3% | Present as "definition-dependent upper bounds"; the survival-weighted definition the methodology wants does not exist anywhere yet — say so. |
| AI contribution share — games | None. Steam disclosure share (19.9% of 2025 releases; 30.8% of 2026 YTD) is *adoption of player-facing content*, not contribution; since Jan 2026 it excludes coding tools | Do not call the Steam share a contribution share. No game-side proxy exists; state the gap. |
| Volume — coding | Strong: GitHub pushes +34% (2025), +80% YoY (Q1 2026); commits +25%; app releases +60–104% (early 2026); Anthropic 8× code shipped (vendor) | Measured public activity; note that agent output under human accounts cannot be separated. |
| Volume — games | Strong: Steam 19,468 releases (2025), ~24k pace (2026); AI-flagged titles 60–90% of release growth (Haro); analogs: Deezer >50% of uploads, Adobe Stock ~48% of inventory | Counts vary by tracker; the Jan 2026 disclosure regime change breaks the AI-flag series. |
| Quality — coding | GitClear duplication 8×; CodeRabbit 1.7× issues per AI PR; Veracode 45% insecure choices; DORA instability; METR perception gap | All vendor or benchmark data; direction consistent. |
| Quality — games | AI-disclosed titles: 84.6% vs 88.3% positive among ≥100-review games (Game Oracle); −17.9 pts recommendation vs procedural-generation games (Bazzaz & Cooper, arXiv 2608.11539); ARC Raiders re-recorded lines; no blind expert ratings; no diversity metrics | Usable as reported, with the selection caveat (low-budget developers use AI more). Homogenization measured only indirectly (China creative lifespans 5.2 days). |
| Value created — coding | Against value: TFP +0.07% (SF Fed); Goldman "no meaningful relationship"; Bain 10–15% team gains rarely reach business value; IT-services deflation 2–5%. For: BLS software publishers +12.9% labor productivity (2025; medium confidence, low attribution); tool-vendor run-rate $10B+ (rough aggregation); consumer surplus $116–172B; Stripe formations +41% | The methodology must cite both columns; the coding-value note's graded conclusions (§8) are the right template. |
| Value created — games | Market growth +6–9% attributed by sources to spend per player and hits, not AI; AI-flagged titles 31% of releases but 10–27% of estimated sales by quarter; AI-disclosed cumulative gross ~$0.66B (est.) vs Steam ~$16–17B/yr (est.); AI companion apps ~$120M/yr (≈0.06% of market) | All model-based estimates; label. This is "absence of evidence of incremental value plus positive evidence of supply inflation", not proof of value destruction. |
| Value captured — coding | IT-services deflation; SaaS growth low-teens; Cursor >$4B ARR, Claude Code >$2.5B (vendor figures); IT-services deflation 2–5% | Direction: value to vendors and customers; incumbents' margins not systematically measured. |
| Value captured — games | Roblox DevEx ~$1.7B (top 10 ≈39%; median creator ~$1,500); Fortnite payouts $1B cumulative; outsourcer squeeze (Keywords Globalize weakness, Virtuos cuts, China concept-art rate cards ¥8,000 → ¥2,000); no studio margins | Platform capture is measurable; studio capture is not. Outsourcing prices are the best E-type barometer but confounded by the post-2021 China licensing freeze and the post-pandemic contraction. |
| Bottleneck diagnostic | Coding: review time +91% (Faros); integration time +41.6% (Song et al.); 25× CI load (Anthropic). Games: none | Present the coding signature as the thing to look for in studios; no game data. |
| Work taxonomy — coding C/E/D | Pre-AI baseline from Meyer et al. (Microsoft, 2019); Hoffmann (2022–24 direction); Anthropic 70% planning / 20% execution decisions; debugging sessions 33% → 19% | See §5.4: use ordinal shifts and the two-phase story; ranges only with the ±10–15-point label. |
| Work taxonomy — games C/E/D | None (no time-use data for any game discipline; both game notes and the game audit say so) | Qualitative derivation only (§5.4); no percentages. |
| Transfer conditions per discipline | Discipline evidence in the game pipeline note §8 table and creative note §8 tiers; player penalty data in the game-value note §4; union/legal facts in the pipeline note §7 | Populate the map (§5) with evidence-type tags [T]/[C]/[S]/[Tgt]/[A] carried over. |
| H-A1 (labor share) | Ukie: programming ~19% of UK workforce, ≈31% of core production roles (year/definitions unverified); no cost split; vendor rule of thumb "art 25–30% of total budget" (weak) | Directionally supported; state that it is UK-only, workforce-not-cost, and that no revenue-weighted sample exists. |
| H-A2 (WTP drivers) | Partial: increasing returns to quality (Binken & Stremersch 2009); followers/CCU/reviews predict revenue (Ma 2025); clear target audience 83% vs 50% success (Bain); AI-disclosure penalty (§4 of game-value note); small-team hits won on design/direction | No hedonic decomposition of creative vs technical attributes exists; the report can present the review-text and disclosure evidence as a first-pass test and mark the conjoint/hedonic study as future work. |
| H-A3 (O-ring/polish) | None quantitative; candidate cases (Cyberpunk 2077 rehabilitation, No Man's Sky, ARC Raiders re-recording) not analysed in the notes; "polish = last 10–20% of effort" is practitioner framing | Present as case-study evidence at most; label the functional-form question open. |
| H-A4 (Amdahl bound) | Arithmetic only (checked) | Present as illustration with p and s ranges; note it needs the programming share of *schedule*, not headcount. |
| H-B1 (divergence) | Volume ↑↑ vs TFP flat and median-firm P&L null: supported. Complication: BLS software publishers +12.9% (2025) | Rewrite the falsifier (§6.2) before using; otherwise the hypothesis is already "falsified" by a print the same note attributes to deflated revenue, AI-product sellers and post-layoff hours. |
| H-B2/B3/B4 (mechanisms) | B2: Faros, Song et al., DORA, CodeRabbit; B3: 5–6% of firms redesign workflows (Bain/McKinsey, correlational); B4: IT-services deflation, vendor revenue, consumer surplus | Present the coding-value note's ranked mechanisms; all correlational. |
| G1–G5 (game predictions) | G1: Steam medians declining 12 years; AI-flagged sales share < release share; playtime −1% (2025). G2: Game Oracle/Bazzaz–Cooper/Haro. G3/G4: none. G5: China illustrators −70% (2023 recruiter estimate), outsourcing rate cards, TAC juniors, King (hearsay) | G1/G2 testable now with caveats; G3/G4 need studio partners; G5 direction consistent, causal attribution weak. |
| Reference classes | Coding 2022–26 (rich); DTP/CAD/microstock/music/VFX (qualitative); game-native cases A–E in `game_value_economics.md` §3 (rich) | Add the game-native cases to the reference-class table; they are the closest analogs (hyper-casual ≈ AI mass production). |

---

## 5. Recommended game-production transfer map and the qualitative C/E/D estimate

### 5.1 Corrections to the note's initial classes

- **Split programming.** "Gameplay, engine and tools programming" is not one class. Tools, build/CI, test scaffolding, backend services, telemetry and UI code are coding-like (High). Gameplay, rendering and performance code in mature proprietary C++ codebases is the METR/Stanford "brownfield" case (experts, large codebases, slow feedback: builds, profiling, console cert) → Conditional.
- **UA/marketing creatives are not "volume-only for taste reasons".** They are metric-verified and disposable, so production transfer is *high* (China: AI in ~70% of 37 Games' video material; Meta 8M+ advertisers), but the industry-level value effect is an arms race (AppsFlyer: creatives +25–30%, impressions +20%; China creative lifespan 5.2 days; rising CPIs). Give them the "volume-only / arms-race" subtype.
- **Concept exploration is not the same as shipped 2D.** Internal exploration and pre-vis carry no audience penalty (T9 irrelevant) → Conditional-High; shipped illustration, key art and icons are visible → Volume-only (taste subtype), with a China/West split.
- **3D props are gated by production-readiness, not taste.** Topology, UVs, LODs and rigs are partly machine-checkable, so props and set dressing are Conditional (pipeline gate), while hero assets and look-dev stay Low. The creative note puts production 3D in its lowest tier; the methodology's "volume-only" over-states current transfer.
- **Add class N (new tasks).** Runtime and AI-native uses are demand-side bets, not transfers of coding gains.
- **Add non-craft work** (research, admin, marketing, community), the highest-adoption layer in every survey.
- **Regionalize.** China: no union gate, weaker disclosure norms, mobile 73% of the market, earlier and deeper substitution in 2D art, dubbing and ad creatives. West: code assistance is the top production use; SAG-AFTRA IMA, Steam disclosure and audience stigma gate visible content.

### 5.2 Recommended map (as of Sept 2026; evidence tags carried from the notes: [T] internal test, [C] company claim, [S] survey, [Tgt] target, [A] anecdote/press, [M] measured/third-party)

| Discipline / task | Transfer class (West / China if different) | Rationale (gates) | Key evidence | Main blocker | Confidence |
|---|---|---|---|---|---|
| Tools, build/CI, test scaffolding, backend services, telemetry, UI implementation code | **High** | Verifiable, fast loops, invisible to players; same tooling as general software | Unity 2026 coding 62% [S]; GDC 2026 code 47% of AI users [S]; MCP 50% [S]; coding RCTs +26% on scoped work [M] | 59% of programmers negative; data/IP concerns | Medium-high (adoption); low (measured gain — none game-specific) |
| Gameplay, engine, rendering, performance code in mature proprietary codebases | **Conditional** (was High) | Verifiable but slow feedback (builds, profiling, cert); expert brownfield work | METR −19% for experts on mature repos [M]; Stanford brownfield 0–10% [M, not peer-reviewed] | Verification bottleneck; legacy code | Medium |
| Text localization + LQA, store/patch copy | **High** (both regions) | Reference-based verification; CAT/TMS pipelines; low visibility | Creative tier 1; TAC >66% MT/MTPE [S]; successful AI-flagged games over-index localization 18% vs 6% [M]; Unity 2025 top automation area [S] | Narrative/cultural quality; dubbed VO under union terms | High |
| UA / marketing creatives, store assets, trailers variants | **High transfer, Volume-only (arms-race subtype)** | Metric-verified (CTR/ROAS), disposable; value competed away | 37 Games ~70% of video material [C]; Meta 8M advertisers [A]; AppsFlyer creatives +25–30%, impressions +20% [M]; China creative life 5.2 days [A] | Red Queen; brand risk | High (transfer); high (zero-sum at market level) |
| Concept exploration, pre-vis, internal reference art, prototyping | **Conditional-High** (internal) | No audience penalty; taste still judges; homogenization risk | GDC prototyping 35% of AI users [S]; Unity 2024 68% "speeds prototyping" [S]; 伽马 ~50% concept-art efficiency [S, perceived] | Artist sentiment (64% negative); idea homogenization (Doshi–Hauser; Zhou–Lee) | Medium |
| Shipped 2D illustration, key art, UI icons | **Volume-only (taste subtype)**; China: high production penetration / West: low–medium, contested in AAA | Visible; stigma; consistency across sets | 37 Games >80% of 2D "AI-involved" [C]; outsourced character ¥8,000 → ¥2,000 [A]; 72% of failed AI-flagged games used AI visuals [M]; −53% reviews (matched) [M]; BO7 backlash [A] | Disclosure penalty; IP; client no-AI clauses | Medium-high |
| 3D props, set dressing, textures/materials, LODs | **Conditional** (pipeline gate), not Volume-only | Engine constraints partly auto-checkable; style consistency not | Tencent Hunyuan3D 8h → 2.5h [T]; Meshy $40M ARR [C]; Unity 2025 asset creation top use [S] | Production-readiness (topology/UV/rig); consistency | Medium |
| Hero characters/environments, rigging, look-dev, cinematics | **Low** | Consistency across hundreds of assets; taste; visible | Creative tier 4; no audited case anywhere | Hero quality bar; sentiment; IP | Medium |
| Animation: cycles, retargeting, cleanup | **Conditional** | E-type, partly checkable in engine | EA run cycles 12 → 1,200 (2023) [C]; Unity 2024 46% of AI-using studios [S] | Quality; performer replica terms | Low-medium |
| Animation/performance acting, mocap, lead VO | **Low** | Taste; consent regime; visible | SAG-AFTRA 2025 IMA consent/disclosure/replica minimums; Equity 99.6% ballot; ARC Raiders re-recording [A] | Unions (West); quality gap | Medium |
| Incidental VO, barks, placeholder voice | **Conditional** (West, consent-gated) / **High** (China dubbing) | Licensed replicas; low salience | ARC Raiders TTS then partial re-record [A]; successful AI-flagged games over-index voice 24% vs 8% [M]; NAVA 21% lost work [S, method unknown] | Consent; audience reaction when noticed | Medium |
| QA: regression, crash, performance, compliance automation | **Conditional-High**; exploratory "feel" testing **Low** | Verifiable outcomes; agents unreliable on feel | Unity 2026 automated playtesting 35% [S]; Square Enix 70% by end-2027 [Tgt]; Keywords Globalize weakness [A] | Reliability; no outcome data | Medium |
| Level design: blockout, procedural variants | **Conditional**; flow/fun **Low** | Navmesh/metrics checkable; fun is not | GiiNEX city 5 days → 25 min [C]; 37% procedural generation among agent users [S]; King tools [A, hearsay] | Judging fun; designer sentiment 63% negative | Low-medium |
| Narrative: barks, ambient, secondary text | **Volume-only (taste subtype)**; core arcs/characterization **Low** | Visible; read as "low investment" | Unity 2026 narrative/writing 44% [S]; Bazzaz–Cooper thematic coding [M]; King copywriters [A, hearsay] | Backlash; quality | Medium |
| Economy/balance tuning; live-ops content variants | **Conditional** | Simulation-verifiable parts transfer; content cadence is an arms race and erodes scarcity | Google: dynamic balancing 38% of agent users [S]; Genshin ~$200M/yr content (2021) [C] | Perceived craft; Red Queen | Low-medium |
| Runtime AI / AI-native: LLM NPCs, companions, generative UGC, world models, personalization | **N — new task (demand-side)**, not a transfer | Judged on demand expansion and unit economics, not production gains | Justice Mobile 5M NPCs in 3 days [C]; companion apps ~$120M/yr [M est.]; Fortnite Conversations; Roblox Cube; Rec Room shutdown [A, AI-cost detail unconfirmed]; Muse/WHAMM research-grade [verified] | Inference cost; safety; unproven ARPU; "last 20%" | Low (form and size) |
| Business, production, research, community, marketing ops (non-craft) | **High** | Text-centric; invisible | GDC: research/brainstorming 81% of AI users; publisher/support staff 58% vs studio staff 30% [S, verified] | Few | High |

### 5.3 The C/E/D taxonomy: one rule for both notes

Adopt the methodology's operational rule (no spec and output is a spec → C; spec exists and output is checkable → E; output is a judgment → D) **and** add the E-delegated tag. Then: writing a feature brief for an agent is C only if it sets new intent; prompting an agent to implement an existing spec is E-delegated; reviewing and accepting the result is D. This keeps "supervising agents" from being silently reclassified as D and makes the coding and game ledgers comparable.

### 5.4 Check of the coding C/E/D estimates in `software_work_composition_shift.md`

- **Baseline arithmetic (Meyer et al., Microsoft 2019).** From the diary shares — coding 15, bugfixing 14, testing 8, specification 4, review 5, docs 2 — with bugfixing split 50/50: E = 15+8+2+7 = 32 points; D = 7+5 = 12 points (up to ~19 if the decision content of meetings/mentoring is counted); C = 4–7 points. Normalized over E+D+C this gives **E ≈ 55–65% / D ≈ 22–37% / C ≈ 8–14%**. The note's "E 50–60 / D 30–40 / C 8–15" tilts D up and E down relative to its own arithmetic; acceptable only if the note states that part of meeting time is counted as D. It is Microsoft-only, self-reported and from 2019.
- **2023–24 direction (Hoffmann et al.).** Coding share +12.4% and PM −24.9% are shares of *GitHub activity* among open-source maintainers under an RD design, not industry hours. Extrapolating to "the human E share rose" is a reasonable direction, not a magnitude.
- **Mid-2026 median ("E 40–50 / D 40–45 / C 10–15").** No measurement exists; the note's ±10–15-point label is honest. Keep it labeled "triangulated estimate".
- **AI-intensive teams ("E 15–25 / D 55–65 / C 15–20").** Anchored on Anthropic's "70% of planning decisions / 20% of execution decisions" (who decides in a session, not how hours are spent), Karpathy's "99%", and interview quotes. The numbers are not derivable from those inputs; present this column as an **illustrative scenario**, not an estimate, or move it to the appendix.
- **Two good findings to keep:** the U-shape (completion tools raised the human E share; agents lowered it) and "D itself is being automated" (fixing-broken-code sessions 33% → 19%), which is why the third category should be defined as decision/acceptance.
- **Output ledger** (Google 25% → 75% of new code; pushes +80%; PR creation 4.7×) is well supported in direction; magnitudes are vendor-defined.
- **Verdict:** usable as ordinal shifts with the two-phase story; never as measurements; the game audit's rule "do not present percentages for the three-way split" should apply to the game side, and the coding side should show ranges only with the uncertainty label.

### 5.5 Qualitative estimate for game production (no time-use data exist; direction only)

Derivation recipe the report can state: (i) discipline weights from the only public workforce split (Ukie; production subset: programming ≈31%, art ≈26%, design ≈18%, QA ≈13%, production/PM ≈13% — UK, year unverified, headcount not cost); (ii) each discipline's C/E/D mix from pipeline structure (asset production, implementation, testing and localization are E-heavy; reviews, playtests, tuning and cert are D; direction, core design and narrative are C); (iii) apply the transfer classes above to the E tasks; (iv) report ordinal shifts with confidence. Two structural points follow:
- Games are *more* E-heavy than software in hours (asset production is volume work), so if art/content E-tasks transferred, the Amdahl ceiling on AI's title-level effect would be *higher* than the programming-only bound. The transfer map says that transfer is conditional and regional, which is the real content of proposition (a): not "games are not E-work" but "the E-work that dominates games is gated by consistency, rights and visibility".
- The scarce input in games was already judgment (Supercell killed 30+ games to launch 5; Voodoo launches ~0.4% of prototypes; polish = "last 10–20%"), so D and C were binding before AI.

| Measure (game production) | Expected move | Where strongest | Confidence | Caveat |
|---|---|---|---|---|
| Human E-hours share | ↓ | China mobile 2D art, UA creatives, dubbing (already ↓↓ by 2023–26); code/QA/localization everywhere (↓); Western AAA hero content (≈ →) | Medium (direction); none (magnitude) | All gain figures are company claims or perceptions; no controlled study |
| E-output volume (assets, variants, releases) | ↑↑ | Long-tail Steam, mini-games, ad creatives, live-ops content | High | Measured for releases and creatives; not for assets per title |
| Human D-hours share (curation/"抽卡", paintover, LQA, review, playtest analysis) | ↑ | Everywhere AI drafts enter pipelines | Medium | D is expanding at the bottom *and* being priced at a discount (MTPE, paintover) while sign-off concentrates at the top; "D↑" is not automatically "premium↑" |
| Human C-hours share | → to ↑ (residual) | Direction, core design, narrative | Low-medium | AI enters ideation (research/brainstorming 81% of AI users), so C is augmented, not untouched |
| Junior E roles and outsourcing | ↓ first | Outsourced 2D, translation, QA vendors, junior art | Medium (direction); low (AI attribution) | Confounded by China's licensing freeze, post-pandemic contraction, capital-cost reset; the only "AI-attributed" layoff case is hearsay |
| Cost share of C/D | ↑ (Baumol) | Studios with retained senior staff | Low | No studio budget data; requires C/D wages not to fall |

Rule for the report: state these as directions with confidence; do not print a three-way percentage split for games.

---

## 6. Balanced formulation of the two propositions and the upside cases

### 6.1 Proposition (a) — games are not mostly coding; value comes from creative work and polish

**As the report should state it.** Programming is a minority of game-production labor (UK census: ~19% of the workforce, ≈31% of core production roles; cost split unknown), so coding gains alone bound the title-level effect to a few percent (Amdahl: ≈5% at p=0.25, s=1.26; 25% even if programming became instant). What players pay for is relative and taste-judged — novel fun, feel and polish, IP, social context, live operations — and these are the least verifiable tasks, so the coding transfer is weakest exactly where value is made (H-A2/H-A3 are open, but the Steam disclosure data show a visible-AI penalty: −53% reviews matched; −17.9 pts recommendation; failures over-index on AI visuals). **But** the non-coding majority of game work is itself execution-heavy (assets, variants, testing, localization), and the evidence shows AI is already substituting in the commodity, invisible and metric-verified layers (localization, UA creatives, incidental VO, outsourced 2D — deepest in China), so "not mostly coding" does not mean "mostly immune". The balanced claim: *AI's production gains reach games through the E-layers that are gated by consistency, rights and visibility rather than by verifiability alone; value conversion depends on the D/C layers that AI touches least.*

### 6.2 Proposition (b) — in coding, volume ≠ value; no incremental industry-level value yet

**As the report should state it.** Task-level gains are real (+26% to +56% on scoped work; −19% for experts on mature code) and output has exploded (pushes +80% YoY; 75% of new code at Google by its own definition), yet aggregate TFP is flat, the median firm reports no P&L effect, and Denmark shows precise nulls on earnings and hours (effects >2% ruled out). The mechanisms, in order of evidence strength: review/verification bottlenecks (review time +91%), competitive pass-through to customers (IT-services deflation 2–5%), organizational J-curve (5–6% of firms redesign workflows), quality and rework debt, measurement gaps. **But** "no incremental industry-level value" is false as a blanket statement: a tool industry with ~$10B+ run-rate exists, firm and product formation accelerated (Stripe Atlas +41%; app releases +60–104%), consumer surplus is large ($116–172B, survey-based), and software publishers' measured labor productivity jumped +12.9% in 2025 (attribution to AI: low). The balanced claim: *value has been created but is (i) captured by AI vendors, (ii) passed to customers, (iii) absorbed by verification, and (iv) spread over a long tail — so it is not yet visible in incumbent producers' P&L or in TFP.* The report should carry the three-way diagnosis (not yet / not in producer revenue / not at all) and say which the evidence currently favors (bottlenecks and pass-through over "not yet").

**Falsifier fix for H-B1.** Replace "software-sector labor productivity accelerates ≥1 pp/yr above trend" with: (i) multifactor/TFP-type measure or firm-level DiD, not a single-year sector labor-productivity print; (ii) sustained ≥2 years; (iii) excluding AI-tool vendors' own revenue and post-layoff hours effects; (iv) threshold re-derived at sector level from task gains × exposed share × success rate (team-level 10–15% gains would imply several pp/yr if converted), with the derivation shown. As written, the BLS 2025 print would "falsify" the hypothesis for reasons unrelated to value.

### 6.3 Upside cases that must be able to show up (each with its own indicator; see §7)

1. **AI-native and new genres** (LLM NPCs, companions, generative UGC, world models): the only channel that expands demand rather than supply; currently ≈0.06% of market revenue (companion apps), with attention-without-conversion cases (Suck Up!) and one platform failure (Rec Room, AI-cost detail unconfirmed). Indicator: AI-native revenue share.
2. **Small-team hits**: Balatro, PEAK (<$200k), Vampire Survivors, Clair Obscur (<$10M) — all pre-generative-AI in production; AI lowers the cost of *attempts*, and the Supercell/Voodoo model says more prototypes per hit is real value for teams with taste. Indicator: hit rate among AI-flagged small teams vs matched non-AI teams.
3. **Personalization and live-ops responsiveness**: plausible, unmeasured; risk of scarcity erosion and Red Queen. Indicator: retention/ARPU uplift disclosed for AI features.
4. **UGC platforms**: cheap creation enlarges a platform's value when it owns discovery and pays by engagement (Roblox DevEx +~50%/yr; Fortnite creator islands 36.5% of play time in 2024 per Epic's own review — the "47% by May 2026" figure comes from a weak source the game audit says not to cite), partly by reallocating time from other games (Roblox play time +52% while total PC/console hours fell 1%); extreme creator concentration (Roblox top 10 ≈39% of DevEx; median creator ~$1,500). Indicator: creator payouts and share of playtime, with AI-creation tool adoption.
5. **Cost relief in invisible tasks** (code, QA, localization, secondary VO, tools, analytics): no player penalty; savings likely competed into scope and cadence; durable margin for IP owners and platforms. Indicator: outsourcing prices and QA/localization cost per unit.
6. **China mini-games and small-team production**: ¥53.5B (+34%), >80% of developers in teams ≤30, platform says AI cut art and testing costs (claim); homogenization and CPI inflation already visible. Indicator: mini-game revenue concentration and creative lifespan.

---

## 7. Compact leading-indicator dashboard (12 indicators)

| # | Indicator | Source (public) | Current value (as in notes; verify at source) | Threshold that would change the conclusion |
|---|---|---|---|---|
| 1 | Worker-level gen-AI use in game jobs; studio vs publisher split | GDC State of the Game Industry (annual, Jan) | 31% (2024) → 36% (2026); studio staff 30% vs publisher/support 58% | Studio-staff use >50% within two editions → games enter the intensity phase coding reached in 2024–25 |
| 2 | AI-flagged share of Steam releases vs share of estimated sales | Sulka Haro census / SteamDB / Gamalytic or VG Insights | Releases 10.9% → 19.9% → 30.8% (2026 YTD); sales share 27% / 17% / 10% (Q4'25–Q2'26) | Sales share ≥ release share for 3 consecutive quarters → AI-flagged supply converting to value |
| 3 | AI-disclosed vs matched non-AI review and recommendation gap | Game Oracle-type matched analysis; Bazzaz & Cooper replication | −53% reviews; 84.6% vs 88.3% positive; −17.9 pts recommendation | Gap <10% on reviews and <5 pts on recommendation → stigma dissipated (T9 gate opens) |
| 4 | AI disclosure among top grossers | Steam top-100 / top-1% by estimated revenue vs disclosure flag | AI-disclosed titles: 12 eight-figure earners, mostly established games that added AI | Top-100 disclosure share ≥ overall release share → diffusion into hits, not just the tail |
| 5 | Steam release count and median revenue per release | SteamDB; Gamalytic | 19,468 (2025), ~24k pace (2026); median $249 (2025 releases, est.); 12 consecutive years of median decline | Median stops falling while releases keep rising → demand expansion / supply elasticity >0 |
| 6 | New-release share of playtime and total play hours | Newzoo (PC/console), Circana (US) | New releases ~12–13% of playtime; PC/console hours −1% (2025) | New-release playtime share >20% or total hours growth >5%/yr → attention constraint loosening |
| 7 | Player attitude series | Quantic Foundry; Circana PlayerPulse; GameDiscoverCo; Bain | 85% negative (opt-in); 25% "less likely to buy" (US); 8% refuse (Steam users); 42% more comfortable than a year ago (Bain) | "Less likely to buy" <15% in a representative sample → visible-AI penalty fading |
| 8 | Outsourcing barometer | Keywords Studios (Create/Globalize segments), Virtuos headcount; China rate cards (GameLook-type reports) | Keywords Globalize "ongoing challenges" (2024); Virtuos −7% (2025); concept art ¥8,000 → ¥2,000 (2023) | Create-segment revenue −20% YoY with stable publisher output → E-substitution at scale; rate cards for "AI draft + paintover" replacing per-asset rates |
| 9 | Job-posting mix | Indeed/Lightcast; GameJobs/Hitmarker; 猎聘/BOSS直聘 (China) | Not measured in the notes (gap); Gamma Data "−35% traditional art/junior planning" is unverified | Junior art/QA/localization postings −30% relative to senior C/D postings → labor composition shift confirmed |
| 10 | Coding lead signals | GitHub (agent-involved PR share); DORA (stability association); Faros/DX (review latency) | ~1/3 of PRs agent-involved (Jul 2026); DORA stability still negative (2025); review time +91% | DORA stability association turns positive **and** review latency falls → verification bottleneck solved; expect game-programming gains to convert 12–18 months later |
| 11 | Verification engineering in games | Unity/GDC surveys; Square Enix QA target; vendor case studies | Automated playtesting 35% of Unity 2026 respondents; SQEX 70% QA/debug target by end-2027 (target) | First audited case of QA or LQA hours −50% at shipped quality → T1/T2 gates rising for D-type tasks |
| 12 | AI-native and demand-expansion revenue | Appfigures (companion apps); company disclosures; Roblox/Fortnite creator payouts | Companion apps ~$120M/yr (≈0.06% of market); Roblox DevEx ~$1.7B (+~50%); Fortnite $1B cumulative | AI-native category >1% of global games revenue (≈$2B) or a disclosed retention/ARPU uplift from an AI feature in a top-50 title → demand-side channel open |

Update quarterly; record each reading with date and definition; treat any two consecutive threshold crossings as a trigger to re-score the transfer map.

---

## 8. Other specific recommendations for the report writer

1. Add `ai_coding_value_evidence.md` §8 (graded conclusions) and `game_value_economics.md` §3–§6 to the methodology's inputs; the note currently argues both propositions without them.
2. Fill the "—" cells in §6.3's prediction table: E-time ↓ (task framework, exposure); C-time flat/↑ (residual; reinstatement); E-output ↑↑ (Jevons for output).
3. Label the Steam disclosure share as *player-facing content adoption* everywhere; since 16 Jan 2026 it excludes coding tools and uses a two-tier form, so 2026 is not comparable with 2024–25.
4. Harmonize cross-note figures: Anthropic 59%; Quantic 62%/63%; Steam median ($249 for 2025 releases vs "<$4k paid, all-time"); Canaries version (13/16/19%).
5. In H-A2's falsifier, note that the current disclosure penalty is confounded by selection (low-budget developers use AI more); a matched design (Game Oracle) reduces but does not remove this.
6. Replace "treat the coding effect as an upper bound" with "bound in the direction indicated by the gate comparison".
7. Present the ten-dimension rubric, the six-level unit table, P0–P7 and the fourteen pitfalls as an appendix titled "严格研究设计（未来工作）"; keep pitfalls 1–4, 7, 10 and 13 as a one-paragraph "reading rules" box in the main text.
8. Keep the Amdahl illustration but show p as a range (0.2–0.35 of *schedule*, not headcount) and say it applies to fixed scope.

---

## 9. VERIFICATION QUEUE (for the coordinator; priority order; one query each)

1. **Zhou & Lee (2024) quoted phrase** "expanding but inefficient idea space" (the paper's term is "generative synesthesia"). Query: `Zhou Lee 2024 PNAS Nexus "generative synesthesia" text-to-image artists novelty "idea space" 25% productivity 50% favorites`
2. **BLS 2025 labor productivity, software publishers (+12.9%)** — needed for the rewritten H-B1 falsifier and dashboard baseline. Query: `BLS "Productivity and Costs by Industry" 2025 "software publishers" labor productivity 12.9 percent selected service-providing industries August 2026`
3. **Haro's AI-flagged share of estimated Steam sales by quarter** (27% / 17% / 10%) and the "60–90% of release growth" figure — dashboard indicator #2. Query: `Sulka Haro "Three years of AI on Steam" share of sales AI-flagged games Q4 2025 27% Q1 2026 17% Q2 2026 10% Cinevva`
4. **Game Oracle matched analysis and Bazzaz & Cooper (arXiv 2608.11539)** — dashboard indicator #3. Query: `Game Oracle Ross Burton AI stigma Steam 53% fewer reviews matched 9,879 games 84.6% 88.3% arXiv 2608.11539 "17.9" recommendation`
5. **Ukie UK games industry census** role shares (programming ~19%, art ~16%, design ~11%, QA ~8%, PM ~8%), census year and definitions. Query: `Ukie "UK Games Industry Census" 2022 job role distribution programming 19% art 16% design 11% QA 8% Statista`
6. **Newzoo playtime shares** (games ≥6 years old 67% of PC playtime; new releases 12–13% of total playtime for three years). Query: `Newzoo GDC 2025 PC gaming playtime "six years or older" 67% new releases 12% 13% share of playtime Balatro Helldivers`
7. **Bick, Blandin & Deming adoption table** (~40% any use; 23% employed and used at work in prior week; 9% every workday; 1–5% of hours; 1.4% time savings). Query: `Bick Blandin Deming "The Rapid Adoption of Generative AI" NBER w32966 updated November 2024 percent of work hours assisted 1.4 percent time savings every workday`
8. **Canaries headline by version** (13% Aug 2025; 16% later; 19% below counterfactual Aug 2026) and the automation-vs-augmentation concentration finding. Query: `Brynjolfsson Chandar Chen "Canaries in the Coal Mine" August 2026 update 22-25 exposed occupations 13 percent 16 percent 19 percent below counterfactual`
9. **Faros AI 2025 secondary figures** (PR size +154%; bugs per developer +9%) used in the methodology note. Query: `Faros AI "AI Productivity Paradox" report 2025 "PR review time" 91% "154%" PR size bugs 9% 1,255 teams 10,000 developers`
10. **Hoffmann, Boysel, Nagle, Peng & Xu design and sample** (RD on free-Copilot eligibility threshold; sample size; period). Query: `Hoffmann Nagle "Generative AI and the Nature of Work" Copilot regression discontinuity top maintainers sample size 12.4% coding 24.9% project management HBS 25-021`
11. **Waldfogel (2017) US feature-film counts** (~500 in 1990; ~1,200 in 2000; ~3,000 in 2010). Query: `Waldfogel 2017 JEP "golden age" number of new feature films 1990 2000 2010 IMDb 500 1200 3000`
12. **Quantic Foundry Dec 2025 exact splits** (85% negative; 62% or 63% most negative; 7.6% approve; N=1,799). Query: `Quantic Foundry December 2025 generative AI games survey 85% negative "very negative" 62% 63% 7.6% approve 1,799`
13. **Jason Wei "verifier's law" exact wording and the property list** attributed in the note's Gaps. Query: `Jason Wei "Asymmetry of verification" "verifier's law" July 2025 blog properties objective truth fast verification scalable low noise continuous reward`
14. **GDPval figures** (1,320 tasks; 44 occupations; 9 sectors; ~48% win-or-tie; ~66% automated-grader agreement). Query: `OpenAI GDPval September 2025 1,320 tasks 44 occupations "win or tie" 47.6% 48% automated grader 66% agreement arXiv 2510.04374`
15. **Steam median revenue harmonization** ($249 median for 2025 releases per Gamalytic vs "<$4k median paid game" per GamesRadar/whole-history analysis). Query: `Gamalytic 2025 Steam releases median revenue $249 2024 $222 66% under $1,000 vs "median" paid game "$4,000" top 1% 84.5% estimated revenue`
