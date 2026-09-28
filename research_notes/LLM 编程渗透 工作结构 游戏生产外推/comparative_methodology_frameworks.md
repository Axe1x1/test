# Analytical frameworks and a draft comparative methodology for extrapolating AI's impact on software coding to game production

**Legend.** Every bullet carries one of these tags:

| Tag | Meaning |
|---|---|
| **[THEORY]** | Established, peer-reviewed theory |
| **[EVIDENCE]** | Empirical result from a peer-reviewed paper or an academic/NBER working paper |
| **[INDUSTRY]** | Industry, vendor, government-outlook or press data. Lower reliability; methods are often opaque |
| **[GOV]** | Official government publications (e.g., US Copyright Office reports, BLS occupational outlooks) |
| **[FRAMING]** | Published essays or talks by recognized AI researchers (not peer-reviewed) |
| **[INFERENCE]** | My own reasoning from the cited material |
| **[PROPOSED]** | My own design for this study |

**How the research was done.** Researched on 2026-09-28. Several primary pages could not be fetched: karpathy.bearblog.dev, jasonwei.net, gdconf.com, quanticfoundry.com, arxiv.org, techcrunch.com and the Stanford Digital Economy Lab. For those, figures come from search-result summaries and are flagged as such. The session's web-search budget ran out before a final verification pass.

Seminal papers are cited by DOI or JSTOR link from standard bibliographic knowledge and were not re-fetched. Their characterizations are the standard textbook ones.

**Scope.** Sibling notes in this folder hold the coding and game data series:
- `coding_adoption_penetration.md`
- `ai_code_share_productivity.md`
- `software_work_composition_shift.md`
- `game_industry_ai_adoption_pipeline.md`
- `creative_content_industries_analog.md`
- `game_ai_opportunities_frontier.md`

This file supplies the theory, the methods, and a draft methodology to structure them. The C/E/D labels match those in `software_work_composition_shift.md`:
- **C** = creative / intent-setting
- **E** = execution / mass-production
- **D** = decision / iteration

---

## 1. Which economic theories structure a coding → game-production comparison, and what do they predict?

### Takeaway
Six bodies of theory do most of the work:
1. **The task-based framework.** AI acts on tasks. Whether it helps or hurts labor depends on how much it displaces versus how many new tasks it creates, and on whether the removed tasks were expert or inexpert.
2. **O-ring, weak-link, Baumol and Amdahl logic.** When tasks are quality complements or sequential bottlenecks, speeding up many tasks barely moves product value, and the cost share and value of the non-automated tasks rise. This is the formal reason polish matters.
3. **Demand elasticity and Jevons.** Cheaper production becomes more total value only where demand is elastic. Games face a hard constraint on players' time and attention.
4. **Superstar and "nobody knows" economics.** Returns are heavy-tailed and hard to predict, so more volume mostly means more lottery tickets.
5. **The productivity J-curve.** Organizational complements delay measured gains.
6. **Exposure indices.** These measure technical potential, not realized value.

The empirical creative-AI studies agree on one pattern: individual productivity and quality go up, while collective diversity and novelty go down.

### Cited Findings

#### 1a. Task-based framework
- **[THEORY] Autor, Levy & Murnane (2003).** Computer capital substitutes for workers in routine, rule-following tasks. It complements workers in non-routine problem-solving and complex-communication tasks. Tasks, not jobs, are the unit of analysis. — [QJE 118(4)](https://doi.org/10.1162/003355303322552801)
- **[THEORY] Acemoglu & Restrepo (2019).**
  - Automation shifts the task content of production against labor through a *displacement effect*.
  - New tasks in which labor has a comparative advantage offset this through a *reinstatement effect*.
  - They attribute three decades of slower US employment growth to faster displacement, weaker reinstatement and slower productivity growth.
  - — [JEP 33(2)](https://doi.org/10.1257/jep.33.2.3)
- **[THEORY/EVIDENCE] Autor & Thompson, "Expertise" (NBER w33941, June 2025).**
  - Whether automation raises or lowers the value of labor depends on whether removing tasks raises or lowers the expertise the remaining tasks require.
  - Automation that removed inexpert tasks raised wages and cut employment. Automation that removed expert tasks lowered wages and raised employment.
  - — [NBER](https://www.nber.org/papers/w33941)
- **[THEORY/EVIDENCE] Acemoglu, "The Simple Macroeconomics of AI" (2024).**
  - Aggregating task-level exposure × productivity gains (a Hulten-style calculation) gives ≤0.66% total factor productivity (TFP) over 10 years.
  - Early evidence comes from "easy-to-learn" tasks. Future gains must come from "hard-to-learn" tasks, "where there are many context-dependent factors affecting decision-making and no objective outcome measures".
  - On that basis the prediction falls below 0.53%.
  - — [NBER w32487](https://www.nber.org/papers/w32487)
- **[THEORY] Agrawal, Gans & Goldfarb.** AI lowers the cost of prediction. Prediction and human judgment are complements, so cheaper prediction raises the value of judgment. — [NBER w24243](https://www.nber.org/papers/w24243)

#### 1b. Quality complementarity, weak links and bottlenecks
- **[THEORY] Kremer (1993), the O-ring theory.** Production is a chain of tasks, and a mistake in any one can sharply cut the product's value (quality multiplies across tasks). As a result, workers of similar skill are matched together, and small skill differences produce large differences in output and pay. — [QJE 108(3)](https://doi.org/10.2307/2118400)
- **[THEORY] Gans & Goldfarb, "O-Ring Automation" (NBER w34639, Jan 2026).**
  - When tasks are quality complements, task-by-task substitution logic is incomplete: automating one task changes the return to automating others.
  - Adoption is discrete and bundled, even when AI quality improves smoothly.
  - Labor income can *rise* under partial automation, because automation scales up the value of the remaining bottleneck tasks.
  - In their words: "Widely-used exposure indices, which aggregate task-level automation risk using linear formulas, will overstate displacement when tasks are complements. The relevant object is not average task exposure but the structure of bottlenecks."
  - — [NBER](https://www.nber.org/papers/w34639); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5962594)
- **[THEORY] Baumol (1967), unbalanced growth ("cost disease").** When an economy has "progressive" and "non-progressive" activities, the relative cost of the non-progressive activity rises persistently. — [AER 57(3)](https://www.jstor.org/stable/1812111)
- **[THEORY] Aghion, Jones & Jones (2017).** In models with automation, growth "may be constrained not by what we do well but rather by what is essential and yet hard to improve". This is Baumol applied to AI. — [NBER w23928](https://www.nber.org/papers/w23928)
- **[THEORY] Amdahl (1967).** Speeding up part of a job speeds up the whole job only up to the share that stays slow: S = 1 / ((1 − p) + p/s). — [AFIPS 1967](https://doi.org/10.1145/1465482.1465560)
- **[THEORY] Theory of constraints (Goldratt).** A system's throughput is set by its bottleneck. — [overview](https://en.wikipedia.org/wiki/Theory_of_constraints)
- **[INDUSTRY] Faros AI: the bottleneck shifts in coding.**
  - Telemetry on 10,000+ developers across 1,255 teams.
  - High-AI-adoption teams complete 21% more tasks and merge 98% more PRs.
  - But PR review time rises 91%, PR size 154% and bugs 9%, and delivery does not improve measurably at the organization level.
  - Caveat: vendor data; the method is not independently audited.
  - — [Faros AI](https://www.faros.ai/blog/ai-software-engineering)
- **[INDUSTRY/EVIDENCE] DORA (survey-based).**
  - **2024:** a 25% increase in AI adoption was associated with −1.5% delivery throughput and −7.2% delivery stability, and +7.5% documentation quality. — [RedMonk](https://redmonk.com/rstephens/2024/11/26/dora2024/); [DX](https://getdx.com/blog/2024-dora-report/)
  - **2025:** AI is now positively associated with throughput and product performance, but still with instability (more change failures and rework). "AI doesn't fix a team; it amplifies what's already there." — [DORA 2025](https://dora.dev/dora-report-2025/); [Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)

#### 1c. Demand elasticity and Jevons
- **[THEORY/EVIDENCE] Bessen (2019).**
  - Productivity-enhancing automation raises industry employment if the price elasticity of demand is above 1.
  - US textiles, steel and autos grew employment for about a century alongside automation. Once demand became satiated, they shed jobs.
  - — [Economic Policy 34(100)](https://academic.oup.com/economicpolicy/article-abstract/34/100/589/5709812); [VoxEU](https://cepr.org/voxeu/columns/automation-and-jobs-when-technology-boosts-employment)
- **[THEORY] Jevons paradox.** Efficiency gains in using a resource can raise total use of it. — [Alcott 2005, Ecological Economics](https://doi.org/10.1016/j.ecolecon.2005.03.020)
- **[EVIDENCE — firm self-study] Anthropic internal study.**
  - Data: an August 2025 survey of 132 engineers and researchers, 53 interviews and Claude Code data.
  - Staff self-report using Claude in 60% of their work, with a 50% productivity boost.
  - 27% of Claude-assisted work consisted of tasks that "wouldn't have been done otherwise" (scaling projects, nice-to-have tools). That is new-task creation, not substitution.
  - — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- **[INDUSTRY] Supply response in apps: supply surges, downloads flat.**
  - About 560,000 new apps reached the App Store in H1 2026, close to all of 2025. The store is on track for more than 1M in 2026, against the 2016 record of 890,000.
  - Press attributes the surge mainly to vibe-coding tools.
  - Press summaries report App Store downloads up only ~3% in 2025 and ~2% in H1 2026.
  - Headline growth rates differ by outlet and period: 9to5Mac reports "+84%", Strataigize "+60%". The underlying data vendor was not verified.
  - — [Mobile Marketing Reads](https://www.mobilemarketingreads.com/app-store-added-nearly-560000-new-apps-in-h1-2026-approaching-all-of-2025s-total/); [9to5Mac](https://9to5mac.com/2026/04/06/app-store-sees-84-surge-in-new-apps-as-ai-coding-tools-take-off/); [TechCrunch](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/); [Strataigize](https://www.strataigize.com/blog/new-app-store-launches-up-60)
- **[INDUSTRY] Newzoo: games face an attention constraint.**
  - Games at least six years old took 67% of PC playtime (under 50% on PlayStation/Xbox).
  - New releases have held about 12–13% of total playtime for three years (PC 8%, console 15%).
  - A re-analysis argues the picture is "slightly less bad".
  - — [Kotaku](https://kotaku.com/pc-gaming-newzoo-balatro-helldivers-2-gdc-time-spent-1851771352); [PC Games Insider](https://www.pcgamesinsider.biz/feature/75052/newzoo-reports-on-the-state-of-pc-gaming-at-gdc-2025/); [Game File](https://www.gamefile.news/p/newzoo-new-games-playing-time-xbox-boycott-neowiz-lies-of-p)

#### 1d. Superstars and "nobody knows"
- **[THEORY] Rosen (1981).** When technology lets one seller serve a large market, and lesser talent substitutes poorly for greater talent, small talent differences produce huge earnings differences. — [AER 71(5)](https://www.jstor.org/stable/1803469)
- **[THEORY] Caves (2000), *Creative Industries*.** Seven properties of creative goods:
  - **"Nobody knows":** demand is uncertain.
  - **"Art for art's sake":** creators care about the work itself.
  - **"Motley crew":** many diverse inputs must all perform, an O-ring-like property.
  - **"Infinite variety":** products are highly differentiated.
  - **"A list/B list":** talent is ranked vertically by quality.
  - **"Time flies":** coordination is time-critical.
  - **"Ars longa":** works earn durable rents.
  - — [Harvard University Press](https://www.hup.harvard.edu/books/9780674008083)
- **[EVIDENCE] De Vany & Walls (1999).** Film box-office revenues follow a stable Paretian distribution with effectively infinite variance, so a film's success cannot be forecast reliably ahead of release. — [Journal of Cultural Economics 23](https://doi.org/10.1023/A:1007608125988)
- **[INDUSTRY] Steam is a heavy-tailed, oversupplied market.** All revenue figures below are model-based estimates, not Valve data.
  - **Releases:** SteamDB counted a record 19,468 releases in 2025, up from 18,556 in 2024. Almost half of 2025 releases had fewer than 10 user reviews; only about 1,200 passed 500 reviews. — [PC Gamer](https://www.pcgamer.com/gaming-industry/more-than-19-000-games-launched-on-steam-this-year-but-almost-half-have-fewer-than-10-reviews/); [KitGuru](https://www.kitguru.net/gaming/joao-silva/steam-data-shows-over-19000-games-released-in-2025/); [SteamDB](https://steamdb.info/stats/releases/)
  - **Revenue of 2025 releases (Gamalytic-based estimates):**
    - 66% earned under $1,000 and 9.9% earned $50,000 or more.
    - The median was $249 (2024: $222).
    - More than 5,000 games did not recoup the $100 listing fee.
    - Total and average revenue ($4.7B; $358,900) were the lowest of 2020–2025.
    - — [80.lv](https://80.lv/articles/analysts-report-drop-in-game-revenue-on-steam-despite-growing-number-of-releases); [GamesRadar](https://www.gamesradar.com/games/over-5-000-games-released-on-steam-this-year-didnt-make-enough-money-to-recover-the-usd100-fee-to-put-a-game-on-valves-store-research-estimates/)
  - **Concentration:** another analysis finds the top 1% of games earn 84.5% of estimated Steam revenue. — [GamesRadar](https://www.gamesradar.com/games/behold-the-whole-history-of-steams-economy-in-one-picture-the-top-1-percent-of-games-earn-84-5-percent-of-estimated-revenue-and-most-games-barely-make-anything/)

#### 1e. The J-curve and lags
- **[THEORY] Brynjolfsson, Rock & Syverson (2021).** General-purpose technologies need large, poorly measured intangible complementary investments (new processes, human capital). So measured productivity growth is understated early and overstated later: the "Productivity J-curve". — [AEJ: Macro 13(1)](https://doi.org/10.1257/mac.20180386)
- **[EVIDENCE/HISTORY] David (1990).** Electrification paid off in productivity only decades later, once factories were redesigned around it. — [AER P&P 80(2)](https://www.jstor.org/stable/2006600)

#### 1f. Exposure indices and usage-based task mapping
- **[EVIDENCE] Eloundou et al., "GPTs are GPTs".**
  - About 80% of US workers could have at least 10% of their tasks affected by LLMs, and about 19% could have at least 50% affected.
  - With LLM-powered software, 47–56% of all tasks could be done significantly faster at the same quality.
  - — [Science 384](https://doi.org/10.1126/science.adj0998); [arXiv 2303.10130](https://arxiv.org/abs/2303.10130)
- **[EVIDENCE] Felten, Raj & Seamans, AI Occupational Exposure (AIOE).** The index links measured progress in AI applications to O*NET abilities. A language-model-specific AIOE followed. — [Strategic Management Journal 42(12)](https://doi.org/10.1002/smj.3286); [arXiv 2303.01157](https://arxiv.org/abs/2303.01157)
- **[EVIDENCE] Anthropic Economic Index (Feb 2025).**
  - **Method:** Clio mapped about 1M Claude.ai conversations to about 20,000 O*NET tasks.
  - **Mix:** Computer & Mathematical was 37.2% of conversations, versus 10.3% for Arts, Design, Entertainment, Sports & Media.
  - **Mode:** 57% augmentation vs 43% automation.
  - **Depth:** about 36% of occupations use AI for at least 25% of their tasks; only about 4% for at least 75%.
  - **Stated caveats:** coding is overrepresented, work and personal use can't be told apart, and it is unknown how outputs were used.
  - — [Anthropic](https://www.anthropic.com/news/the-anthropic-economic-index); method papers: [Tamkin et al. (Clio)](https://arxiv.org/abs/2412.13678); [Handa et al.](https://arxiv.org/abs/2503.04761)
- **[EVIDENCE] Anthropic software-development report (Apr 2025).** 79% of Claude Code conversations were "automation" vs 49% on Claude.ai. The "feedback loop" pattern was 35.8% vs 21.3%. — [Anthropic](https://anthropic.com/research/impact-software-development)
- **[EVIDENCE] Anthropic "economic primitives" (Jan 2026).**
  - **Five primitives:**
    - task complexity (including human time with and without AI);
    - human and AI skill (years of education);
    - use case;
    - AI autonomy (1–5);
    - task success.
  - **Success and speed-up by task level:**

    | Education level of the task | Success rate | Estimated speed-up |
    |---|---|---|
    | 12 years | 70% | 9× |
    | 16 years | 66% | 12× |

  - **Implied US labor-productivity growth:** 1.8 pp/yr. This falls to 1.0–1.2 pp/yr after adjusting for success rates, and to 0.7–0.9 pp/yr if tasks are complements (elasticity 0.5).
  - **Selection caveat, stated explicitly:** "users choose which tasks to bring to Claude".
  - — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)

#### 1g. AI and creative work: quality vs quantity, individual vs collective
- **[EVIDENCE] Doshi & Hauser (2024).**
  - Short stories written with LLM-generated ideas were rated more creative, better written and more enjoyable, especially for less creative writers.
  - But AI-enabled stories were more similar to each other.
  - The authors call this a social dilemma: individual gains, collective loss of novelty.
  - — [Science Advances](https://www.science.org/doi/10.1126/sciadv.adn5290)
- **[EVIDENCE] Zhou & Lee (2024).**
  - Data: 4M+ artworks from 50,000+ users.
  - Adopting text-to-image AI raised creative productivity by 25% and favorites per view by 50%.
  - Peak novelty rose while average novelty fell, which the authors describe as an "expanding but inefficient idea space".
  - — [PNAS Nexus 3(3)](https://academic.oup.com/pnasnexus/article/3/3/pgae052/7618478)
- **[EVIDENCE] Dell'Acqua et al. (2023), the "jagged technological frontier".**
  - 758 BCG consultants.
  - On 18 tasks inside AI's capability frontier, AI users completed 12.2% more tasks, 25.1% faster, at more than 40% higher quality.
  - On a task outside the frontier, AI users were 19 percentage points less likely to be correct.
  - — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321); [PDF](https://mitsloan.mit.edu/sites/default/files/2023-10/SSRN-id4573321.pdf)
- **[EVIDENCE] Noy & Zhang (2023).** On professional writing tasks, ChatGPT cut time by about 40% and raised quality by about 18%. — [Science 381](https://doi.org/10.1126/science.adh2586)
- **[EVIDENCE] Brynjolfsson, Li & Raymond.** An AI assistant raised customer-support issues resolved per hour by 14% on average and by 34% for novice or low-skilled agents. — [NBER w31161](https://www.nber.org/papers/w31161)
- **[EVIDENCE] Hui, Reshef & Zhou (2024).**
  - After ChatGPT's release, freelancers in exposed occupations saw −2% jobs and −5.2% monthly earnings.
  - Image-generating models had similar effects.
  - Top freelancers were not protected; there is suggestive evidence they were hit harder.
  - — [Organization Science 35(6)](https://pubsonline.informs.org/doi/abs/10.1287/orsc.2023.18441); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4527336)

#### 1h. Coding: large task-level gains, weak aggregate signal (the evidence behind proposition (b))
- **[EVIDENCE] Peng et al. (2023).** Copilot users finished a controlled HTTP-server task 55.8% faster. — [arXiv 2302.06590](https://arxiv.org/abs/2302.06590)
- **[EVIDENCE] Cui et al.** Field RCTs at Microsoft, Accenture and a Fortune 100 firm, with 4,867 developers. Completed tasks rose 26.08% (SE 10.3%), with larger gains for less-experienced developers. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566); [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535)
- **[EVIDENCE] METR RCT (early 2025).**
  - 16 experienced open-source developers, 246 tasks, in mature repositories (22k+ stars, 1M+ lines of code).
  - With AI access they were **19% slower**.
  - They had forecast a 24% speed-up, and afterwards believed they had been 20% faster.
  - METR redesigned the study in February 2026.
  - — [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [METR update](https://metr.org/blog/2026-02-24-uplift-update/)
- **[EVIDENCE] Humlum & Vestergaard (2025).**
  - Danish adoption surveys (25,000 workers, 7,000 workplaces, 11 exposed occupations), linked to administrative records.
  - Difference-in-differences finds precise null effects on earnings and hours. Effects larger than 2% two years after ChatGPT are ruled out.
  - Average reported time savings were about 3%.
  - — [NBER w33777](https://www.nber.org/system/files/working_papers/w33777/revisions/w33777.rev0.pdf); [BFI](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/)
- **[EVIDENCE] Bick, Blandin & Deming.** Generative AI assisted about 1–5% of all US work hours in late 2024. Reported time savings equal 1.4% of total work hours. — [NBER w32966](https://www.nber.org/papers/w32966)
- **[INDUSTRY] GitClear.**
  - 211M changed lines, 2020–2024.
  - Duplicated blocks of five or more lines rose 8× in 2024.
  - "Moved" (refactored) lines fell from 24.1% (2020) to 9.5% (2024).
  - In 2024, copy-pasted lines exceeded moved lines for the first time.
  - Caveat: vendor data; correlational.
  - — [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research)
- **[EVIDENCE] Brynjolfsson, Chandar & Chen, "Canaries in the Coal Mine?" (ADP payroll data).**
  - Workers aged 22–25 in the most AI-exposed occupations saw a **13%** relative employment decline, controlling for firm-level shocks (2025 versions). A later version is summarized as **16%**.
  - Software developers aged 22–25 are down about 20% since late 2022.
  - Declines concentrate where AI automates rather than augments.
  - — [Stanford DEL](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/); [Nov 2025 slides](https://cehd.uchicago.edu/wp-content/uploads/2025/11/Brynjolfsson-etal-Canaries-AI-HO-2025-11-06a_jbb.pdf); [Aug 2026 version](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)

### Inferences
- **[INFERENCE] What the theories predict for games together.**
  - AI speeds up execution tasks (E) the most.
  - Game value multiplies across disciplines (Caves' "motley crew", Kremer's O-ring). The binding constraints are taste-driven decision and polish work (D) and creative direction (C).
  - So product value should move far less than task speed (Amdahl, Baumol).
  - Meanwhile the cost share and wage premium of C/D work should rise (Baumol, Autor–Thompson, Gans–Goldfarb).
- **[INFERENCE] Demand elasticity decides whether cheaper production becomes value.**
  - Coding shows signs of latent demand: Anthropic's 27% of new tasks, and the app-supply surge.
  - Games face a fixed time and attention budget (Newzoo). A fall in E-type costs therefore most plausibly becomes more releases and more content per title, with lower returns per title.
  - The exception is if AI creates new products that expand demand, such as AI-native games. These are "new tasks" in Acemoglu–Restrepo terms.
- **[INFERENCE] There is a counter-argument to pure "volume ≠ value".**
  - In heavy-tailed markets, when quality can't be predicted in advance, more draws can raise realized welfare (Aguiar & Waldfogel, Q5).
  - But AI-driven homogenization (Doshi–Hauser; Zhou–Lee) may shrink the variance of the draws, and with it the chance of outlier hits.
  - Which effect dominates is empirical, so the study must measure novelty and diversity directly.
- **[INFERENCE] Use exposure indices only as the first stage of the funnel ("potential").** They are not forecasts of value. Gans–Goldfarb show that linear aggregation is biased when tasks are complements, which is exactly the game case.
- **[INFERENCE] Coding shows big task-level gains but little aggregate value.**
  - Task-level gains are 26–56% in RCTs.
  - Yet measured earnings and productivity effects are near zero, and instability is higher.
  - Three mechanisms fit this, and they can operate together:
    1. bottlenecks (Amdahl; Faros);
    2. J-curve lags;
    3. value leaking to consumers or AI vendors.
  - Section 6 designs tests to tell them apart.

### Gaps
- **Sources not fetched:** Karpathy's and Wei's primary pages were blocked. Their quotes come from several consistent search summaries.
- **Canaries headline differs by version (13% vs 16%).** The Stanford pages could not be opened to reconcile the two figures.
- **App Store download growth (+3% in 2025, +2% in H1 2026) comes from press summaries.** The underlying data vendor was not verified.
- **No peer-reviewed estimate of aggregate demand elasticity for games was found** (playtime or spend with respect to content supply). The attention-constraint inference rests on Newzoo playtime shares only.
- **Steam revenue distributions are model-based,** usually estimated from review counts. Valve publishes no per-title revenue.

---

## 2. Which empirical methods support comparison and extrapolation across sectors, and what do historical cases of production technology spreading through creative industries teach?

### Takeaway
A defensible extrapolation stacks five methods:
1. **An outside view.** Use reference classes: earlier technology shocks in creative industries, plus coding as the "lead market".
2. **Analogy checked by structure mapping and formal transportability logic.**
3. **Diffusion models that separate timing from intensity.** Model adoption timing (who uses AI at all) apart from intensity of use (how much of the work it touches), with an explicit lead–lag between coding and games.
4. **Quasi-experimental identification around adoption shocks.** Staggered difference-in-differences (DiD), event studies, synthetic control and regression discontinuity (RD).
5. **Triangulation** across surveys, telemetry and disclosures.

The historical cases share a pattern:
- **Covered cases:** desktop publishing (DTP), CAD, digital photography, DAWs and digital music, and CGI/VFX.
- **Execution:** production roles and unit prices collapse.
- **Volume:** output explodes, and value concentrates in a few hits and in the platforms.
- **Creative work:** creative and direction work persists or gains.
- **Quality:** quality at the top does not fall.

### Cited Findings

#### 2a. Forecasting under analogy
- **[THEORY] Kahneman & Lovallo (1993).** Forecasters take an "inside view", anchoring on plans for the case at hand and ignoring the statistics of similar past cases, which yields bold forecasts. The "outside view" corrects for this. — [Management Science 39(1)](https://doi.org/10.1287/mnsc.39.1.17)
- **[THEORY/EVIDENCE] Flyvbjerg, reference-class forecasting.**
  - The method has three steps:
    1. identify a reference class;
    2. establish its outcome distribution;
    3. place the case within that distribution.
  - It is more accurate than conventional forecasting.
  - — [Flyvbjerg 2006 (arXiv 1302.3642)](https://arxiv.org/pdf/1302.3642); [PMI](https://www.pmi.org/learning/library/nobel-project-management-reference-class-forecasting-8068)
- **[EVIDENCE] Tetlock / Good Judgment Project.** In a geopolitical forecasting tournament, accuracy improved with training in probabilistic reasoning, with teaming, and with tracking top forecasters into elite teams. — [Mellers et al. 2014, Psychological Science](https://doi.org/10.1177/0956797614524255)
- **[THEORY] Gentner (1983), structure-mapping.** A sound analogy maps relational (causal) structure, not surface attributes. Mapping connected systems of relations ("systematicity") is what separates good analogies from bad ones. — [Cognitive Science 7(2)](https://doi.org/10.1207/s15516709cog0702_3)
- **[THEORY] Pearl & Bareinboim (2014), transportability.** A causal effect can be carried from a source population to a target only when the mechanisms that differ between them are known and can be adjusted for with target-side data. The differing mechanisms are marked in a "selection diagram". — [Statistical Science 29(4)](https://doi.org/10.1214/14-STS486)
- **[THEORY] Cartwright & Hardie (2012).** "It worked there" supports "it will work here" only if the cause plays the same causal role here and the needed support factors are present. — [Oxford University Press](https://global.oup.com/academic/product/evidence-based-policy-9780199841622)
- **[EVIDENCE] Vivalt (2020).** Impact-evaluation results vary widely across contexts, and effect sizes vary systematically with study characteristics. The lesson: expect transfer error. — [JEEA 18(6)](https://doi.org/10.1093/jeea/jvaa019)

#### 2b. Diffusion and lags
- **[THEORY] Bass (1969).** Adoption driven by innovation (p) and imitation (q) coefficients produces S-curves. — [Management Science 15(5)](https://doi.org/10.1287/mnsc.15.5.215)
- **[EVIDENCE] Griliches (1957).** Hybrid-corn diffusion followed logistic curves whose origin, slope and ceiling differed by region and were explained by profitability. — [Econometrica 25(4)](https://www.jstor.org/stable/1905380)
- **[EVIDENCE] Comin & Hobijn (2010).** Across 15 technologies and 166 countries, the average adoption lag is about 45 years, and newer technologies are adopted faster. — [AER 100(5)](https://doi.org/10.1257/aer.100.5.2031)
- **[EVIDENCE] Comin & Mestieri (2018).** Adoption lags converged across countries, but intensity of use diverged. Adoption and penetration are different things. — [AEJ: Macro 10(3)](https://doi.org/10.1257/mac.20150175)
- **[THEORY] Lead–lag diffusion models** (Takada & Jain 1991 and successors). Later-adopting markets can inherit diffusion parameters from lead markets and diffuse faster. — [Jain 2020 review (CEIBS)](https://www.ceibs.edu/files/2021-02/044-jain-dipak_dec-2020.pdf)
- **[EVIDENCE] Bick, Blandin & Deming.**
  - Work adoption of generative AI has been as fast as the PC's, and overall adoption faster than the PC's or the internet's.
  - Late-2024 adoption among US adults 18–64:

    | Measure | Share |
    |---|---|
    | Used generative AI at all | ~40% |
    | Employed and used it for work in the prior week | 23% |
    | Used it every workday | 9% |

  - — [NBER w32966](https://www.nber.org/papers/w32966)

#### 2c. Quasi-experimental identification around adoption shocks
- **[EVIDENCE] del Rio-Chanona, Laurentsyeva & Wachs (2024).**
  - Design: DiD against counterfactual platforms.
  - Stack Overflow activity fell 25% within six months of ChatGPT's release, relative to two comparison groups:
    - Russian and Chinese Q&A sites, where ChatGPT access was restricted;
    - math forums, where ChatGPT was weaker.
  - — [PNAS Nexus 3(9)](https://academic.oup.com/pnasnexus/article/3/9/pgae400/7754871)
- **[EVIDENCE] Hoffmann et al., "Generative AI and the Nature of Work".**
  - Design: regression discontinuity on eligibility for Copilot, using millions of GitHub panel observations over two years.
  - Developers with access shifted from project management and collaborative work toward core coding. The shift was strongest for lower-skill developers.
  - — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5007084)
- **[EVIDENCE] Other designs worth reusing:**
  - Hui, Reshef & Zhou: event study around model releases on an online labor market. — [Organization Science](https://pubsonline.informs.org/doi/abs/10.1287/orsc.2023.18441)
  - Humlum & Vestergaard: surveys linked to administrative data, plus DiD. — [BFI](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/)
- **[THEORY/METHOD] Staggered adoption.** Two-way fixed-effects DiD is biased when adoption timing is staggered and effects are heterogeneous (Goodman-Bacon decomposition). Group-time average-treatment-effect estimators fix this. — [Goodman-Bacon 2021, J. Econometrics](https://doi.org/10.1016/j.jeconom.2021.03.014); [Callaway & Sant'Anna 2021, J. Econometrics](https://doi.org/10.1016/j.jeconom.2020.12.001)

#### 2d. Triangulation: why no single source suffices
- **[EVIDENCE] Self-reports and measurement diverge in sign.** In METR's trial, developers perceived +20% while measured performance was −19%. — [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- **[INDUSTRY] Game-developer surveys disagree by frame:**

  | Survey | Sample | Headline finding |
  |---|---|---|
  | Google Cloud / Harris Poll (vendor-commissioned), June–July 2025 | 615 developers in US/KR/FI/NO/SE | 90% integrate generative AI into workflows; 87% use AI agents |
  | GDC 2026 | 2,300+ respondents | About one-third personally use generative AI; 52% say it harms the industry |

  — [Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research); [Game Developer](https://www.gamedeveloper.com/business/one-third-of-game-workers-use-generative-ai-but-half-think-it-s-bad-for-the-industry); [GameSpot](https://www.gamespot.com/articles/more-developers-than-ever-believe-generative-ai-is-hurting-the-game-industry/1100-6537793/)
- **[INDUSTRY] Product-level disclosure data (Steam).**
  - About 7,818 Steam games disclose generative-AI use: roughly 7% of the catalogue and about 20% of 2025 releases.
  - A year earlier the figure was about 1,000 (1.1%).
  - About 60% of disclosures concern visual assets.
  - Disclosure is self-reported. Growth figures differ between reports (about 700% vs "800%").
  - — [Totally Human](https://www.totallyhuman.io/blog/the-surprising-new-number-of-genai-games-on-steam); [Digital Watch](https://dig.watch/updates/generative-ai-now-powers-20-of-new-steam-games); [VGC](https://www.videogameschronicle.com/news/steam-games-disclosing-generative-ai-use-are-up-800-this-year/)

#### 2e. Historical cases of production technology spreading through creative industries

**Digital music (DAWs, then digital distribution)**
- **[EVIDENCE] Waldfogel (2017).**
  - Digitization cut the cost of bringing new products to market.
  - US feature films rose from about 500 (1990) to about 1,200 (2000) to nearly 3,000 (2010).
  - Because quality is unpredictable, some of the many new products turned out very good, giving consumers a "golden age".
  - — [JEP 31(3)](https://www.aeaweb.org/articles?id=10.1257%2Fjep.31.3.195)
- **[EVIDENCE] Aguiar & Waldfogel (2018).** New music products tripled between 2000 and 2008 as production, promotion and distribution costs fell. When quality is unpredictable, the welfare gain from extra entry is far larger than when it is predictable. — [JPE 126(2)](https://www.journals.uchicago.edu/doi/abs/10.1086/696229); [NBER w22675](https://www.nber.org/papers/w22675)
- **[EVIDENCE] Waldfogel (2012).** The quality of new recorded music did not fall after Napster, despite the revenue collapse. Quality was indexed by critics' retrospective best-of lists and by usage. — [J. Law & Economics 55(4)](https://doi.org/10.1086/665824)
- **[INDUSTRY] Luminate.**
  - About 99,000 new tracks (ISRCs) per day reached streaming services in 2024, about 106,000 per day in 2025, and about 150,000 per day by September 2026 (per Luminate's CEO).
  - Of 253M tracks, 88% had 1,000 streams or fewer in 2025, and about 120.5M had 0–10.
  - — [Hypebot](https://www.hypebot.com/luminate-reports-music-streaming-saturation-2025-2026/); [Music Business Worldwide](https://www.musicbusinessworldwide.com/there-are-now-more-than-200m-tracks-on-audio-streaming-services-nearly-100m-of-them-attracted-no-more-than-10-plays-each/); [Billboard](https://www.billboard.com/pro/luminate-says-150000-songs-uploaded-on-streaming-daily/)

**Desktop publishing**
- **[INDUSTRY/GOV]**
  - Typesetters, paste-up workers and film strippers were largely replaced.
  - DTP tasks moved to graphic designers, web designers and editors.
  - The desktop-publisher occupation was projected to shrink (−14%, 2016–2026).
  - BLS projects graphic-designer employment at −2% for 2025–2035.
  - — [EBSCO Research Starters](https://www.ebsco.com/research-starters/social-sciences-and-humanities/desktop-publisher); [WhatTheyThink](https://whattheythink.com/articles/55522-day-typesetting-industry-died/); [BLS graphic designers](https://www.bls.gov/ooh/arts-and-design/graphic-designers.htm)

**CAD/BIM in architecture and engineering**
- **[GOV]** CAD and BIM raised drafter productivity and let engineers and architects do tasks drafters used to do, so fewer drafters are needed per project. Drafter employment is projected at +1% for 2025–2035. — [BLS Drafters](https://www.bls.gov/ooh/architecture-and-engineering/drafters.htm)

**Digital photography and microstock**
- **[INDUSTRY]**
  - From the 2000s, microstock accepted far more photographers at lower quality bars and sold images for very little, sometimes about $0.25 an image, against hundreds of dollars for traditional stock.
  - Commentary reports average prices falling from about $250 (royalty-free) and $500 (rights-managed) to about $6.50.
  - These figures are unaudited.
  - — [Wikipedia: Microstock photography](https://en.wikipedia.org/wiki/Microstock_photography); [Fstoppers](https://fstoppers.com/stock/end-stock-photographer-621731)

**CGI/VFX in film**
- **[INDUSTRY]**
  - Rhythm & Hues filed for Chapter 11 on Feb 11, 2013, and laid off about 254 people, just before it won the Oscar for *Life of Pi*.
  - 21 VFX companies closed or went bankrupt between 2003 and 2013.
  - Under fixed-bid contracts, underbidding and thin margins, VFX vendors captured little of the value they created for studios.
  - — [Wikipedia](https://en.wikipedia.org/wiki/Rhythm_%26_Hues_Studios); [TheWrap](https://www.thewrap.com/rhythm-hues-sends-shockwaves-77181/); [Cartoon Brew](https://www.cartoonbrew.com/documentary-2/life-after-pi-documentary-exposes-flawed-vfx-business-model-96579.html)

### Inferences
- **[INFERENCE] Reference-class lessons for games (the outside view):**
  1. Execution roles shrink, and their tasks are absorbed by adjacent creative roles (typesetters → designers; drafters → architects).
  2. Unit prices collapse for commodity creative output (microstock). Aggregators and platforms capture more of the value.
  3. Volume explodes, with extreme concentration (music, Steam, apps).
  4. Quality at the top is maintained or improves (Waldfogel). Consumer welfare rises through variety.
  5. Vendors of production labor get squeezed (VFX houses; by analogy, art-outsourcing studios).
  6. Organizational redesign creates lags (David).

  None of the historical cases shows production technology removing the need for creative direction. All of them show a shift in which input is scarce.
- **[INFERENCE] Coding is the natural lead market for a lead–lag diffusion model.** But Comin–Mestieri implies fitting two curves per discipline: adoption (any use) and intensity (share of tasks and hours). Vendor surveys already show high "any use" in games, while intensity in core art and design is likely low. So the lag to estimate is mainly a lag in intensity.
- **[INFERENCE] Natural experiments available for games:**
  - image, 3D and animation model releases, as common shocks with exposure that differs by discipline;
  - platform policy changes (e.g., Steam's disclosure rules);
  - staggered rollouts of AI features in engines and DCC (digital content creation) tools;
  - labor agreements restricting AI in performance work (voice, motion capture);
  - differences in access and norms between China and the West, echoing del Rio-Chanona's use of Russian and Chinese sites as controls.

### Gaps
- **CGI/VFX:** no quantitative before/after study of CGI's effect on VFX labor (hours per shot, shots per film) was found. The VFX lesson here is qualitative (who captures value).
- **DAWs:** no peer-reviewed study isolates DAW adoption from digital distribution. Waldfogel's work blends the two cost declines.
- **Coding → games lag:** no published lead–lag diffusion estimate between software and game production exists. It has to be estimated.
- **Steam disclosure policy:** its exact scope (development tools vs shipped content) was not verified here. See sibling `game_industry_ai_adoption_pipeline.md` §2.

---

## 3. What conditions determine whether AI gains in coding transfer to a given game-production task?

### Takeaway
The best-supported single predictor is **verifiability**. Tasks whose outputs can be checked cheaply, objectively, quickly and repeatedly have two advantages:
- They are easier to train AI on (reinforcement learning with verifiable rewards).
- They are easier to deploy with humans supervising (Karpathy's "autonomy slider").

Coding is unusually verifiable (compilers, tests, CI), digital-native, and backed by huge training corpora. Most value-defining game tasks are not:
- Art direction, fun, narrative, performance and polish are judged by taste, by delayed audience response, and by consistency across assets.
- They are further constrained by copyright rules, labor agreements and a strong audience penalty for disclosed AI use.

Transfer should therefore be scored **task by task on a structural profile**, not discipline by discipline.

### Cited Findings
- **[FRAMING] Jason Wei (July 2025), "Asymmetry of verification and verifier's law".**
  - Some tasks are much easier to verify than to solve (e.g., a Sudoku, or whether a website works). Now that RL works generally, this asymmetry is central.
  - Verifier's law: "the ease of training AI to solve a task is proportional to how verifiable the task is. All tasks that are possible to solve and easy to verify will be solved by AI."
  - Reverse asymmetry also exists: fact-checking an essay can take longer than writing it.
  - — [Jason Wei](https://www.jasonwei.net/blog/asymmetry-of-verification-and-verifiers-law); [X post](https://x.com/_jasonwei/status/1945287045251052007)
- **[FRAMING] Karpathy (Nov 2025), "Verifiability".**
  - "Software 1.0 easily automates what you can specify. Software 2.0 easily automates what you can verify."
  - An environment is verifiable if it is **resettable** (new attempts are possible), **efficient** (many attempts can be made) and **rewardable** (an automated process can reward each attempt).
  - Verifiable tasks progress fast, sometimes past top experts: math, code, puzzles with correct answers. Tasks that are creative, strategic, or combine real-world knowledge, state, context and common sense lag.
  - — [karpathy.bearblog.dev](https://karpathy.bearblog.dev/verifiability/); [X](https://x.com/karpathy/status/1990116666194456651)
- **[FRAMING] Karpathy (June 2025), "Software Is Changing (Again)".**
  - The valuable near-term products are "partial autonomy apps".
  - They have an "autonomy slider" and purpose-built GUIs that keep the human generate-then-verify loop fast.
  - The idea draws on Tesla Autopilot.
  - — [Latent Space](https://www.latent.space/p/s3); [transcript](https://singjupost.com/andrej-karpathy-software-is-changing-again/)
- **[THEORY] Acemoglu (2024), easy- vs hard-to-learn tasks.** "Easy-to-learn" tasks have objective outcome measures and a reliable map from actions to success. "Hard-to-learn" tasks are context-dependent, with "no objective outcome measures", and gains there will be smaller. — [NBER w32487](https://www.nber.org/papers/w32487)
- **[EVIDENCE] Reinforcement learning with verifiable rewards (RLVR).**
  - Tülu 3 introduced RLVR, where the reward is a programmatic check of correctness. — [arXiv 2411.15124](https://arxiv.org/abs/2411.15124)
  - DeepSeek-R1 trained reasoning with rule-based accuracy and format rewards on math and code. — [arXiv 2501.12948](https://arxiv.org/abs/2501.12948)
- **[EVIDENCE] METR time horizons.**
  - The length of software task that frontier agents complete with 50% success has doubled about every 7 months since 2019, and faster (about 4 months) in 2024–25.
  - METR defines 16 "messiness" factors that degrade performance, including:
    - mistakes that can't be undone;
    - consuming limited resources on each attempt;
    - not being able to tell whether an outcome came from your own actions;
    - success being hard to measure.
  - — [METR](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/); [arXiv 2503.14499](https://arxiv.org/abs/2503.14499)
- **[EVIDENCE] GDPval.**
  - 1,320 tasks from 44 occupations in 9 sectors (about $3T in annual earnings).
  - Built from real work products by professionals averaging about 14 years' experience.
  - Graded mainly by blinded expert pairwise comparison, because automatic grading is hard.
  - Secondary summaries report frontier models at about 48% win-or-tie against experts, and an automated grader agreeing with humans about 66% of the time.
  - — [OpenAI](https://openai.com/index/gdpval/); [arXiv 2510.04374](https://arxiv.org/abs/2510.04374); [secondary summary](https://medium.com/@pranil.dasika/openais-gdpval-why-the-66-automated-grading-problem-matters-more-than-the-48-win-rate-a5e542508196)
- **[EVIDENCE] Jagged frontier (Dell'Acqua et al.).** Tasks that look equally hard can fall on either side of AI's capability, with no warning. — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321)
- **[EVIDENCE] Automation leans on environmental feedback.** The Claude Code "feedback loop" pattern (AI acts, the environment returns errors or test results) is 35.8% of conversations vs 21.3% on Claude.ai. — [Anthropic](https://anthropic.com/research/impact-software-development)
- **[EVIDENCE] Success falls with task complexity** (70% vs 66%), and observed success partly reflects which tasks users choose to bring. — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- **[GOV] IP/legal: US Copyright Office, Part 2 report (Jan 29, 2025).**
  - Copyright protects only human authorship.
  - "Prompts alone do not provide sufficient human control" to make the user the author.
  - AI output is protectable where a human determines sufficient expressive elements, e.g., perceptible human-authored inputs, or creative selection, arrangement or modification.
  - Decisions are case-by-case.
  - — [USCO Part 2 report](https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf); [USCO](https://www.copyright.gov/ai/)
- **[INDUSTRY] Audience acceptance: Quantic Foundry (Dec 2025).**
  - 85% of gamers view generative-AI use in games negatively (62% "very negative"); 7.6% approve.
  - Most negative for art, music, sound, narrative and dialogue. More open to uses such as dynamic difficulty adjustment.
  - The more a gamer values story and design, the more negative they are.
  - — [Quantic Foundry](https://quanticfoundry.com/2025/12/18/gen-ai/); [Boing Boing](https://boingboing.net/2025/12/20/survey-finds-very-negative-attitude-toward-gen-ai-in-games.html)
- **[INDUSTRY] Audience acceptance: the Clair Obscur case.**
  - In December 2025, two days after the ceremony, The Indie Game Awards rescinded *Clair Obscur: Expedition 33*'s Game of the Year and Debut awards.
  - Generative-AI placeholder textures had shipped at launch (later patched). That broke the rule that "games developed using generative AI are strictly ineligible".
  - — [Engadget](https://www.engadget.com/gaming/the-indie-game-awards-snatches-back-two-trophies-from-clair-obscur-over-its-use-of-generative-ai-164730842.html); [GamesRadar](https://www.gamesradar.com/games/rpg/clair-obscur-expedition-33s-controversial-goty-wins-at-the-indie-game-awards-retracted-after-the-rpgs-use-of-generative-ai/)
- **[INDUSTRY] Developer sentiment by discipline (GDC 2026).**

  | Group | Say generative AI is harming the industry |
  |---|---|
  | All respondents, 2026 | 52% |
  | All respondents, 2025 | 30% |
  | All respondents, 2024 | 18% |
  | Visual & technical art (2026) | 64% |
  | Design & narrative (2026) | 63% |
  | Programming (2026) | 59% |

  Only 7% see a positive impact. — [GameSpot](https://www.gamespot.com/articles/more-developers-than-ever-believe-generative-ai-is-hurting-the-game-industry/1100-6537793/); [GDC](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)
- **[INDUSTRY] Steam disclosures skew to visual assets** (about 60%), the most audience-visible category. — [Totally Human](https://www.totallyhuman.io/blog/the-surprising-new-number-of-genai-games-on-steam)

### Inferences

**[PROPOSED] Structural transfer profile.** Score each task in both sectors from 1 to 5 on ten dimensions:

| # | Dimension | Operational question | Coding (typical) | Game examples, high → low | Basis |
|---|---|---|---|---|---|
| T1 | Verifiability | Is there an objective, automated check whose cost is far below generation cost? | High (compiler, tests, CI) | High: build/crash/perf/memory budgets, string-length fit, navmesh validity. Low: art direction, fun, emotional impact | Wei; Karpathy; Acemoglu; RLVR |
| T2 | Feedback latency & reset cost | How fast and cheap is one try → feedback → retry? | Seconds to minutes | Minutes (render preview) → days (playtest) → months (market response) | Karpathy (resettable/efficient); METR messiness |
| T3 | Modularity / coupling | Can the output be accepted in isolation, with errors localized? | Moderate–high (modules, APIs) | Content is coupled through style, canon, level flow and pacing (O-ring coupling) | Kremer; Caves "motley crew"; Gans–Goldfarb |
| T4 | Digital-native artifact & training data | Is the artifact text-like, with large, licensable public corpora? | Very high | 2D images: high but legally contested. Rigged 3D, animation, proprietary engine data: lower | Inference (see Gaps) |
| T5 | Error tolerance / reversibility | Are errors caught before reaching users, and cheap to roll back? | High (review, rollback), though AI raises instability (DORA) | Shipped visual or narrative errors are public and reputational (Clair Obscur) | METR messiness; DORA |
| T6 | Tacit knowledge / taste | Does acceptance depend on uncodified judgment? | Moderate (architecture, "taste") | High (art direction, game feel, comedy, horror pacing) | Acemoglu (hard-to-learn); Karpathy (lagging domains) |
| T7 | Consistency requirements | Must outputs cohere with a long-lived style, canon or character voice across thousands of assets? | Conventions checkable by linters | High, and mostly not machine-checkable | METR long-horizon; inference |
| T8 | IP / legal / labor constraints | Copyrightability, licensing of training data, performer consent | Low–moderate | High for art, music and voice/performance | USCO Part 2; sibling note on SAG-AFTRA |
| T9 | Audience acceptance | Is the AI contribution visible to buyers, and is there a disclosure penalty? | Invisible to end users | High penalty for visible creative assets; low for tools, QA, backend | Quantic Foundry; Indie Game Awards case; GDC sentiment |
| T10 | Value mechanism | Does cheaper or more output raise willingness to pay (elastic demand, B2B productivity), or only volume (attention-constrained, heavy-tailed)? | Partly elastic (new tasks, more apps) | Attention-constrained; hits dominate | Bessen; Newzoo; De Vany & Walls |

**[PROPOSED] Transfer rules.** A transportability procedure:
1. **Classify every coding finding by type**, because each type depends on different dimensions:

   | Finding type | Depends on |
   |---|---|
   | Production (speed, throughput, defects) | T1, T2, T4, T5 (plus T3) |
   | Value (willingness to pay, revenue) | T6, T7, T9, T10 (plus T3 coupling) |
   | Labor (employment, wages, seniority mix) | T10 (demand elasticity), expertise structure (Autor–Thompson), seniority composition (Canaries) |

2. **Draw a selection diagram.** List the mechanism nodes and mark where the game task differs from the coding task by 2 points or more.
3. **Decide per finding:**
   - **Transfer as-is** if no relevant dimension differs.
   - **Transfer as a bound** if the game task is less verifiable, slower to give feedback, or less digital-native (T1/T2/T4). Treat the coding effect as an *upper bound*. If the task also scores worse on T8/T9, discount adoption and value further, even when production gains transfer.
   - **Re-estimate on game data** if the mechanism itself differs, e.g., labor effects under a different demand elasticity.
4. **Time-stamp every judgment and re-score every six months.** Capability moves fast (METR doubling) and unevenly (jagged frontier).
5. **Track "verification engineering" as a separate driver.** Tooling can make a task more verifiable:
   - simulation-based balance metrics;
   - trained style-consistency classifiers;
   - automated playtest bots;
   - "autonomy slider" review GUIs.

   Each raises T1/T2. This is how game tasks move toward coding-like transfer, and it is a leading indicator.

**[PROPOSED] Initial priors by transfer class**, to be validated with the rubric:

| Transfer class | Tasks |
|---|---|
| **High (coding-like)** | Gameplay, engine and tools programming; build/CI; scripting; shader and tech-art code; automated test generation; telemetry/data pipelines; porting and optimization against measurable budgets; string-level localization with a linguistic QA gate |
| **Conditional** | QA (regression automation transfers; exploratory "feel" testing does not); level blockout (navmesh and metrics are checkable, flow and fun are not); economy and balance tuning (the parts that can be simulated); UI implementation; live-ops content variants |
| **Volume-only** (speed transfers, value does not) | Concept exploration; 2D illustration; textures and materials; props; ambient dialogue ("barks"); marketing variants. These are C-type or visible E-type tasks with high T6/T7/T9 |
| **Low** | Art direction; core design and "fun"; narrative arcs and characterization; performance (voice, mocap, animation acting); final polish decisions |

### Gaps
- **Wei's property list:** the post reportedly lists specific properties of easily verifiable tasks (e.g., objective truth, fast and scalable verification, low noise, continuous reward). The post could not be fetched to confirm the list. The rubric above is my own and should not be attributed to Wei.
- **No academic study measures the verifiability of game-production tasks** or links it to AI adoption in games. The scoring above is a proposal.
- **Training data (T4):** no source was found quantifying data availability for 3D, animation and rigging versus code. The T4 contrast is inference.
- **SAG-AFTRA:** the 2024–25 video-game strike and its AI provisions were not sourced here. See sibling `game_industry_ai_adoption_pipeline.md` §7.
- **Conflicting audience evidence:** search summaries attribute to another survey (possibly MIDiA Research) a finding that about 60% of gamers are neutral about AI in development if the final product is high quality. Its source and wording could not be verified. It shows how sensitive audience-acceptance results are to question framing.

---

## 4. How can the three work types (creative / execution-mass-production / decision-iteration) be measured, and what are the strengths and weaknesses of each data source?

### Takeaway
No single instrument measures the C/E/D split; each source captures a different margin with different biases:
- **Time-use surveys** capture how people spend their time, but are distorted by perception.
- **Telemetry and logs** capture behavior, but only inside instrumented tools, and mostly E-type work.
- **AI-conversation labeling** (Clio-style) captures what AI is used for, but on one platform and with users choosing the tasks.
- **Job postings** capture intended labor demand, with lags and boilerplate.
- **Headcount composition** captures realized outcomes, but mixes AI with macro shocks.

Triangulate with at least three sources.

### Cited Findings

**Time-use and surveys**
- **[EVIDENCE]** The Real-Time Population Survey estimates that 1–5% of work hours are AI-assisted, with time savings equal to 1.4% of total hours. — [NBER w32966](https://www.nber.org/papers/w32966)
- **[EVIDENCE]** Surveys linked to Danish administrative data: self-reported time savings of about 3%, but null effects on earnings and hours. — [BFI](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/)
- **[EVIDENCE]** Perception gap: in METR's trial, developers perceived +20% but measured −19%. — [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
- **[EVIDENCE — firm self-study]** Anthropic staff report using Claude in 60% of their work, with a +50% productivity boost; 27% of Claude-assisted work is tasks that would not otherwise have been done. — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)

**Telemetry and activity logs**
- **[EVIDENCE]** Field RCTs measured outcomes from version-control and build data (completed PRs, commits, builds). — [Cui et al.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4945566)
- **[EVIDENCE]** GitHub activity panels split work into coding vs project management (issues, reviews, comments) and show time moving between them. — [Hoffmann et al.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5007084)
- **[INDUSTRY]** Faros measures PR throughput, review latency and PR size. GitClear classifies code changes as added, moved, copy-pasted or churned. — [Faros AI](https://www.faros.ai/blog/ai-software-engineering); [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research)
- **[INDUSTRY]** DORA's delivery metrics (throughput, stability) are measured by survey, not telemetry. — [DORA](https://dora.dev/dora-report-2025/)

**Labeling AI conversations**
- **[EVIDENCE]** Clio summarizes conversations with a model and clusters them hierarchically, preserving privacy. — [Tamkin et al.](https://arxiv.org/abs/2412.13678)
- **[EVIDENCE]** Conversations are then mapped to O*NET tasks and to automation modes ("directive", "feedback loop") and augmentation modes ("task iteration", "learning", "validation"). — [Handa et al.](https://arxiv.org/abs/2503.04761); [Anthropic](https://www.anthropic.com/news/the-anthropic-economic-index)
- **[EVIDENCE]** The Jan 2026 primitives (human time with and without AI, autonomy, success) are validated against external benchmarks such as BLS education data and METR. — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- **[EVIDENCE]** Limits Anthropic states:
  - It can't confirm whether use was for work or personal.
  - It can't see how outputs were used.
  - The sample comes from one platform.
  - Classifiers make errors.
  - Coding is overrepresented.
  - — [Anthropic](https://www.anthropic.com/news/the-anthropic-economic-index)

**Job postings**
- **[EVIDENCE] Acemoglu, Autor, Hazell & Restrepo (2022).**
  - Establishments with AI-exposed task structures posted more AI-related vacancies, hired fewer people into non-AI roles, and changed skill requirements.
  - There were no detectable aggregate employment effects at the occupation or industry level (2010–2018 data).
  - — [JOLE 40(S1)](https://doi.org/10.1086/718327)

**Headcount and payroll composition**
- **[EVIDENCE]** ADP payroll by age × occupation, with firm-by-time controls (the Canaries design). — [Stanford DEL](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/)
- **[INDUSTRY]** Confounders in software hiring: the end of zero interest rates, and the US Section 174 rule forcing R&D salaries to be amortized (effective 2022, largely reversed in 2025). One analysis judges Section 174 a contributor but not the main cause. — [Pragmatic Engineer](https://blog.pragmaticengineer.com/the-pulse-section-174-is-reversed-mostly-that-is/)
- **[INDUSTRY]** Stanford published a follow-up note on interest rates and timing as alternative drivers. — [Stanford DEL](https://digitaleconomy.stanford.edu/news/canaries-interest-rates-and-timinga-more-on-recent-drivers-of-employment-changes-for-young-workers)
- **[INDUSTRY] UK games workforce composition** (Ukie census, as summarized by Statista; the census year, 2021 or 2022, and category definitions were not verified at source):

  | Role | Share of workforce |
  |---|---|
  | Business operations | ~20% |
  | Programming / development | ~19% |
  | Sales / marketing / communications | ~19% |
  | Art | ~16% |
  | Game / level design | ~11% |
  | Project management | ~8% |
  | QA | ~8% |

  — [Statista](https://www.statista.com/statistics/1096364/job-role-distribution-in-the-games-industry-uk/); [Ukie census 2022](https://ukie.org.uk/news/uk-games-industry-census-2022)

**Quality measurement for non-verifiable work**
- **[EVIDENCE]** Blinded expert pairwise grading (GDPval). — [OpenAI](https://openai.com/index/gdpval/)
- **[EVIDENCE]** Human creativity ratings, plus embedding similarity as a measure of collective diversity (Doshi & Hauser). — [Science Advances](https://www.science.org/doi/10.1126/sciadv.adn5290)
- **[EVIDENCE]** Engagement (favorites per view) and content-novelty metrics (Zhou & Lee). — [PNAS Nexus](https://academic.oup.com/pnasnexus/article/3/3/pgae052/7618478)

### Inferences

**[PROPOSED] Operational definitions of the work types.** Shared by coding and games.

| Type | Operational definition | Classification rule | Coding examples | Game examples | Measurement proxies |
|---|---|---|---|---|---|
| **C: creative / intent-setting** | Output is a *new specification of what should exist* (concept, style, mechanic, narrative, architecture or product intent). No reference solution exists; success is judged afterwards, by taste or audience | No spec or reference defines a correct output, **and** the output is itself a brief or spec → C | Product/UX intent; system architecture; API design; novel algorithms | Art direction and style bible; core loop and mechanics; world, characters and story arcs; audio identity; key art | Hours in pre-production and exploration; alternatives generated per accepted concept; tickets with no acceptance criteria; approval by a creative authority rather than a test; director/lead/concept job titles and skills |
| **E: execution / mass-production** | Turns an *existing* spec or reference into conforming artifacts, often at volume. Conformity is checkable (tests, budgets, style guide) | A spec or reference exists, **and** the output is an artifact whose conformity can be checked → E | Implementing to spec; boilerplate; tests; migrations; bug fixes with a repro; docs | Props, textures, LODs, UVs, retopology; rigging to standard skeletons; animation cleanup; VFX variants; localization; VO editing; content variants; porting; executing test cases | Throughput per FTE (PRs, assets, strings, lines); outsourcing volume and unit price; time in authoring tools; coverage by automated validators |
| **D: decision / iteration** | Output is a *choice, evaluation or parameter change* inside a feedback loop | The primary output is a judgment, selection or parameter rather than an artifact → D | Code review; triage and prioritization; incident decisions; design review; acceptance | Art and design reviews; playtest analysis; balance and economy tuning; polish passes; cutting features; milestone greenlights; certification decisions; live-ops A/B decisions | Number and latency of review cycles; iterations per asset or feature before approval; time in reviews, playtests and meetings; experiments run on telemetry; review-queue length |

**[PROPOSED] Measurement rules:**
1. **Label task instances, not people.** Give each task C/E/D shares (e.g., 0.2 / 0.5 / 0.3), because many tasks are mixed. Aggregate to hours by discipline and seniority.
2. **Two independent coders label the task inventory**, targeting inter-rater agreement of Cohen's κ ≥ 0.7. LLM classifiers are allowed only after validation against the human-coded set, mirroring how Anthropic validated its primitives. Report classifier-versus-human agreement.
3. **Record, for each source, which margin it measures and its bias:**

| Source | What it measures | Main biases | Game-studio implementation |
|---|---|---|---|
| Time-use diaries / experience sampling | Human hours by C/E/D, and AI use per task | Perception gap (METR); social desirability; stigma in games → under-reporting of AI | Two-week experience sampling of studio staff, coded by C/E/D, AI-use and discipline |
| Tool telemetry (IDE; DCC tools such as Maya, Blender, Substance, Houdini; engine editors) | Behavior inside tools | Only instrumented tools are seen, which skews toward E; privacy limits | Time in tool per asset; AI-feature invocations; edit/iteration counts |
| Version control, asset management, ticketing (Git/Perforce; ShotGrid/ftrack; Jira) | Artifacts, iterations, cycle times | Commit and ticket semantics vary between teams | Iterations to approval per asset; review-note counts; cycle and queue times per pipeline stage |
| AI-conversation labeling | What AI is used for | One platform; users choose tasks; can't see whether outputs were adopted | Map game-related conversations onto a game task inventory (O*NET lacks game detail), labeled C/E/D × automation/augmentation |
| Job postings | Intended labor demand; skill mix | Boilerplate; lags; ghost postings | Share of junior E-type roles (junior 3D, QA tester, localization) vs senior C/D roles; AI-skill mentions by discipline |
| Headcount / payroll / credits | Realized labor outcomes | Macro confounders (interest rates, post-pandemic correction, 2023–25 game layoffs); outsourcing moves headcount outside studios | Discipline × seniority composition over time (payroll or LinkedIn-type data; game credits databases such as MobyGames); outsourcing-vendor headcount as an E-type barometer |
| Product disclosures (Steam AI disclosure; credits) | Adoption visible in shipped products | Self-reported; stigma → under-disclosure; scope definitions | Share of releases disclosing AI, overall and within revenue tiers |

**[INFERENCE] Coding evidence already maps onto C/E/D:**
- AI moves developer time from D-type coordination toward E-type coding (Hoffmann et al.).
- It creates D-type review bottlenecks (Faros).
- It hits E-heavy junior employment first (Canaries).

The same three signatures are the first things to look for in game studios.

### Gaps
- **No time-use baseline of C/E/D shares by discipline for game studios was found.** The sibling note found no authoritative cost or headcount splits by discipline either.
- **O*NET has few game-specific task statements, and no public game-task inventory was found.** One must be built.
- **No peer-reviewed validation of Steam AI disclosures against actual AI use was found.**

---

## 5. How should value be distinguished from volume, and how do creative industries measure value?

### Takeaway
The indicator chain has to run through four stages:
1. **Volume:** units produced.
2. **Quality-adjusted output.**
3. **Value created:** revenue, playtime, consumer surplus.
4. **Value captured:** and by whom.

In hit-driven markets, use statistics that respect the distribution (medians, quantiles, hit rates above thresholds, concentration and tail indices), because a few titles dominate the means.

Evidence from both coding and digitized creative industries says volume is a poor proxy for value:
- **Coding:** big task-level gains, null earnings effects, more instability, and supply surges against flat demand.
- **Creative industries:** a volume explosion in which most output goes unconsumed, welfare gains through variety, and value captured by platforms.

But the creative-industry literature also shows that cheaper "lottery tickets" can raise consumer welfare when quality is unpredictable.

### Cited Findings
- **[EVIDENCE] Welfare from more draws.** When quality is unpredictable, more entry raises welfare from new products. — [Aguiar & Waldfogel 2018](https://www.journals.uchicago.edu/doi/abs/10.1086/696229)
- **[EVIDENCE] Vintage-quality indices.** Quality by release year can be indexed with critics' retrospective lists and usage data. — [Waldfogel 2012](https://doi.org/10.1086/665824); [Waldfogel 2017](https://www.aeaweb.org/articles?id=10.1257%2Fjep.31.3.195)
- **[EVIDENCE] Consumer surplus of digital goods.** Measured with massive online choice experiments that ask people what they would accept to give a good up. — [Brynjolfsson, Collis & Eggers 2019, PNAS](https://doi.org/10.1073/pnas.1815663116)
- **[THEORY] Value capture.** Who profits from an innovation depends on the appropriability regime and on control of complementary assets. — [Teece 1986, Research Policy](https://doi.org/10.1016/0048-7333(86)90027-2)
- **[EVIDENCE] Reviews and game sales.** Online reviews affect video-game sales more for less popular games and for more internet-experienced players. Quality signals matter most in the long tail. — [Zhu & Zhang 2010, Journal of Marketing](https://doi.org/10.1509/jmkg.74.2.133)
- **[EVIDENCE] Heavy tails in creative revenues** (infinite variance). — [De Vany & Walls 1999](https://doi.org/10.1023/A:1007608125988)
- **[INDUSTRY] Steam 2025 hit rates** (revenue figures are model-based estimates):
  - About half of releases had fewer than 10 reviews.
  - About 1,200 of 19,468 releases (~6%) reached 500+ reviews.
  - 9.9% earned $50k or more in their first year.
  - The median was $249.
  - — [PC Gamer](https://www.pcgamer.com/gaming-industry/more-than-19-000-games-launched-on-steam-this-year-but-almost-half-have-fewer-than-10-reviews/); [80.lv](https://80.lv/articles/analysts-report-drop-in-game-revenue-on-steam-despite-growing-number-of-releases)
- **[INDUSTRY] Music 2025.** 88% of 253M tracks had 1,000 streams or fewer. — [Hypebot](https://www.hypebot.com/luminate-reports-music-streaming-saturation-2025-2026/)
- **[INDUSTRY] Apps.** Supply surged while downloads stayed nearly flat (+2–3%). — [Mobile Marketing Reads](https://www.mobilemarketingreads.com/app-store-added-nearly-560000-new-apps-in-h1-2026-approaching-all-of-2025s-total/)
- **[EVIDENCE] Coding: task-level gains versus aggregate value** (sources in §1h):
  - Task level: +26% (Cui), +55.8% (Peng), but −19% for experienced developers (METR).
  - Earnings: null effects (Humlum–Vestergaard).
  - Macro: modest. Acemoglu projects ≤0.66% TFP over 10 years; Anthropic projects 1.0–1.2 pp/yr after success adjustment and 0.7–0.9 pp/yr if tasks are complements.
- **[INDUSTRY] Coding: volume versus quality** (sources in §1b and §1h):
  - Faros: +98% PRs, with +91% review time and +9% bugs.
  - DORA: higher instability.
  - GitClear: more duplicated code.
- **[EVIDENCE] Individual quality up, collective diversity down** (Doshi & Hauser; Zhou & Lee). — sources in §1g
- **[INDUSTRY] Value capture in past cases.** VFX vendors went bankrupt while their films succeeded; microstock prices collapsed. — sources in §2e

### Inferences

**[PROPOSED] Value ladder.** Measure every rung at the same unit of analysis, in both sectors:

| Rung | Definition | Coding indicators | Game indicators |
|---|---|---|---|
| **V0 Volume** | Units per period and per FTE | PRs, commits, lines of code, apps released | Titles released; assets and content-hours per title; updates per live game |
| **V1 Surviving volume** | Units that pass acceptance and survive N days | Lines merged and not reverted after 30/90 days | Assets in the final build; content kept after polish |
| **V2 Quality-adjusted output** | V1 × quality indices | Change-failure rate, incidents, defects per KLOC, maintainability | Blind expert ratings (art, design, narrative); bug density per play-hour; performance; review score; refund rate; D1/D7/D30 retention |
| **V3 Value created** | Revenue, usage, consumer surplus | Revenue per employee; usage per app; price-adjusted output | Revenue and playtime distributions (median, P90, P99); hit rate (share above thresholds, e.g., ≥500 reviews or ≥$50k); top-1% share / Gini / tail index; consumer surplus (choice experiments; variety-welfare models) |
| **V4 Value captured** | Who gets V3 | Software-firm margins; developer wages and employment by seniority; AI-vendor revenue; consumer prices | Studio margins; wages and employment by discipline × seniority; platform, store and engine fees; AI-tool spend; outsourcer revenue and prices; consumer prices and free-to-play content |

**[PROPOSED] Key ratios:**
- **V3/V0, value per unit.** A decline means dilution.
- **V1/V0, survival rate.** This captures churn and rework.
- **V4 shares over time.** These show who captures the value.
- **Value elasticity of volume at market level, %ΔV3 / %ΔV0.** Under a pure attention constraint it is ≈0. Under elastic demand it is >0.

**[PROPOSED] Reporting rules:**
- Never report V0 without V3 for the same unit.
- Report distributions, not means, for games.
- Use quality-adjusted price indices when comparing value across years.
- Measure "AI contribution" as the survival-weighted share of shipped output (V1 basis), not as suggestions accepted or characters generated. The latter inflate contribution and are not comparable across companies.

**[INFERENCE] Creative-industry economics complicates "volume ≠ value" in two ways:**
1. **Value may shift rather than vanish.** Consumers can gain through variety and free content even when producer revenue is flat. "No incremental industry value" in revenue terms can therefore coexist with gains in consumer surplus.
2. **Aggregate numbers can hide dilution.** Aggregate value can hold steady while value per release collapses and concentration rises. Each outcome belongs to a different stakeholder and needs its own indicator.

### Gaps
- **No official quality-adjusted price index for games or software isolates AI.** One would have to be constructed.
- **No consumer-surplus estimates for games (GDP-B-style) were found.**
- **Studio-level margins are rarely public.** Value-capture analysis will lean on public companies: publishers, engines, platforms and outsourcers.

---

## 6. Draft comparative methodology for "coding → game production" (proposed design, built around the user's two propositions)

### Takeaway
**[PROPOSED]** A task-anchored design in six layers:
1. Build parallel task inventories for coding and for each game discipline, labeled C/E/D and scored on the ten-dimension transfer profile (§3).
2. Measure an eight-stage indicator funnel at matched units: exposure → adoption → penetration → AI contribution → volume → quality → value created → value captured.
3. Use coding (2022–2026) and five historical creative-technology shocks as reference classes.
4. Estimate lead–lag diffusion, separately for adoption and for intensity.
5. Identify causal effects with staggered DiD, event studies and within-studio RCTs.
6. Aggregate task effects to product and market value with models that account for complementarity and bottlenecks, and validate the result against observed studio and market outcomes.

The user's two propositions become pre-registered hypotheses with explicit falsifiers:
- **(a)** Games are not mostly coding; much of their value comes from creative work and polish.
- **(b)** In coding, volume ≠ value: large task-level gains have not clearly become industry-level value.

### Cited Findings
Anchors used in the design (full sources in §§1–5):
- **Programming is roughly one-fifth of the UK games workforce** (~19%), against art ~16%, design ~11%, QA ~8% and project management ~8%. — [Statista/Ukie](https://www.statista.com/statistics/1096364/job-role-distribution-in-the-games-industry-uk/)
- **Linear exposure aggregation overstates displacement when tasks are complements.** — [Gans & Goldfarb](https://www.nber.org/papers/w34639)
- **Assuming complementarity cuts Anthropic's implied productivity growth** from 1.8 to 0.7–0.9 pp/yr. — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- **New releases get about 12–13% of total playtime.** — [Kotaku/Newzoo](https://kotaku.com/pc-gaming-newzoo-balatro-helldivers-2-gdc-time-spent-1851771352)
- **Adoption lags and intensity of use behave differently.** — [Comin & Mestieri](https://doi.org/10.1257/mac.20150175)
- **Staggered-DiD estimators.** — [Callaway & Sant'Anna](https://doi.org/10.1016/j.jeconom.2020.12.001); [Goodman-Bacon](https://doi.org/10.1016/j.jeconom.2021.03.014)
- **Coding volume–value divergence:**
  - [Faros](https://www.faros.ai/blog/ai-software-engineering)
  - [DORA](https://dora.dev/dora-report-2025/)
  - [Humlum & Vestergaard](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/)
  - [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
  - [App Store](https://www.mobilemarketingreads.com/app-store-added-nearly-560000-new-apps-in-h1-2026-approaching-all-of-2025s-total/)
- **Supply surges with concentrated demand.**
  - Steam: [PC Gamer](https://www.pcgamer.com/gaming-industry/more-than-19-000-games-launched-on-steam-this-year-but-almost-half-have-fewer-than-10-reviews/)
  - Music: [Hypebot/Luminate](https://www.hypebot.com/luminate-reports-music-streaming-saturation-2025-2026/)

### Inferences (the proposed design)

#### 6.1 Units of analysis (nested) [PROPOSED]

| Level | Definition | Coding instance | Game instance | What is measured here | Main data |
|---|---|---|---|---|---|
| L1 Task | Verb + object + context statement (O*NET-style), labeled C/E/D and scored T1–T10 | "Write unit tests for payment module" | "Retopologize hero character to LOD targets"; "Write branching dialogue for side quest" | Exposure, AI success, speed-up, quality vs human | RCTs, benchmarks, AI-conversation labels |
| L2 Workflow / pipeline stage | Sequence of tasks with hand-offs and review gates | Spec → implement → review → test → deploy → operate | Concept → sculpt → retopo → UV → texture → rig → animate → integrate → QA → art-director sign-off | Bottlenecks, queue times, rework (Amdahl/ToC), O-ring coupling | Ticketing, VCS, asset management |
| L3 Discipline × seniority | Role family and level | Frontend/backend/DevOps/QA; junior/senior | Programming, 2D/3D/tech art, animation, design (systems/level/narrative), audio/VO, QA, production, localization, live-ops/UA | Time mix, headcount, wages, postings | Surveys, payroll/LinkedIn, postings, credits |
| L4 Product / project | Shipped title, live-ops season, or app/service | App or service release | Title or season | Quality, polish, willingness to pay, revenue, playtime, reviews | Store data, reviews, telemetry |
| L5 Firm / studio | Adopting organization | Software firm or team | Studio, publisher, outsourcer | Adoption timing, complementary investment (J-curve), cost structure, margins | Surveys, financials, partnerships |
| L6 Market / platform | Segment or storefront | App stores, SaaS categories | Steam, consoles, mobile, genres, regions (incl. China) | Supply volume, concentration, prices, consumer surplus, value capture | SteamDB/Gamalytic-type trackers, Newzoo, Luminate-type analogs |

**Matching rule.** Compare like with like:
- A coding **L1** effect (e.g., +26% completed tasks) is evidence only for a game **L1** effect on a task with a similar profile.
- **L4–L6** claims about games need **L4–L6** evidence, or an explicit aggregation model (§6.6).

#### 6.2 Indicator system [PROPOSED]

| # | Indicator | Operational definition | Coding measurement | Game measurement | Main pitfalls |
|---|---|---|---|---|---|
| I1 | Exposure (potential) | Share of task-weighted hours where AI could cut time by ≥50% at equal quality (Eloundou-style rubric) | O*NET-based β; AIOE; benchmark coverage | Game-task inventory rated by an expert panel, plus model benchmarks for image/3D/animation/voice | Linear aggregation overstates displacement under complementarity (Gans–Goldfarb) |
| I2 | Adoption (extensive margin) | Share of workers or studios using AI for work at least weekly (tiers: ever / monthly / weekly / daily) | Developer surveys; RPS-type population surveys | GDC, Unity, Google-type surveys, stratified by discipline; studio census; share of Steam releases disclosing AI | Vendor-commissioned samples; "ever used" inflates; stigma deflates |
| I3 | Penetration (intensive margin) | Share of task-instances or hours in which AI is in the loop | Telemetry (agent sessions, completions); Clio task share | DCC/engine AI-feature telemetry; asset metadata; time-use sampling | Only instrumented tools are observed |
| I4 | AI contribution share | Survival-weighted share of shipped output authored by AI (lines, assets, dialogue lines, test cases) that survives acceptance and N days | Merged AI-authored lines still present after 90 days | Shipped assets with AI provenance (e.g., content credentials, pipeline tags); retained AI-drafted strings | "Accepted suggestions" and "characters generated" inflate; definitions differ by firm |
| I5 | Output volume | Units per period and per FTE | PRs, commits, releases, apps | Releases; assets per title; content-hours; live-ops updates | Goodhart effects; composition shifts |
| I6 | Quality | Verifiable metrics plus blind expert or audience judgments; plus diversity/novelty | Change-failure rate; incidents; defects; maintainability | Bug density; crash rate; performance; blind art/design ratings; review score; refund rate; retention; embedding-based diversity | Quality lags release; subjective ratings need blinding |
| I7 | Value created | Revenue, usage/playtime, consumer surplus; quality-adjusted | Revenue per employee; usage per app; sector labor productivity | Distribution of revenue and playtime per title; hit rate; market totals; consumer surplus | Heavy tails; model-based revenue estimates |
| I8 | Value captured | Split of I7 among studios, labor, platforms, engines, AI vendors, consumers | Margins; wages; AI-vendor revenue; prices | Studio margins; wages by discipline × seniority; store fees; engine fees; outsourcer prices; consumer prices | Little public data for private studios |
| I9 | Bottleneck & cost structure (diagnostic) | Queue and review latency per stage; rework rate; cost share by C/E/D | PR review time; queue length | Art-director and design review latency; iterations to approval; QA/cert queue; budget share by discipline and by C/E/D | Needs studio partners |

**Funnel conversion ratios** diagnose where gains stall: I2→I3 (intensity gap), I3→I4 (survival gap), I5→I6 (quality gap), I6→I7 (demand gap), I7→I8 (capture gap).

#### 6.3 Work-type taxonomy and predicted trajectories
Definitions and proxies are in §4.

**[INFERENCE] Theory-based predictions.** These are what must be tested:

| Measure | Direction | Basis |
|---|---|---|
| Human E-time | ↓ | — |
| D-time (review, playtest, iteration) | ↑ | Amdahl/ToC; Faros analog |
| C-time | Flat or ↑ | — |
| E-output volume | ↑↑ | — |
| Cost share of C/D work | ↑ | Baumol |
| Junior E-type employment | ↓ first | Canaries analog |
| Wage premium of senior C/D | ↑ | Autor–Thompson; Gans–Goldfarb |
| Collective diversity of visible creative assets | ↓ unless actively managed | Doshi–Hauser; Zhou–Lee |

#### 6.4 Transfer procedure (from §3) [PROPOSED]
For each coding finding:
1. State the finding and its mechanism.
2. Pick the relevant T-dimensions for its type (production, value or labor).
3. Score the matched game task.
4. Draw a selection diagram.
5. Decide: transfer, bound, or re-estimate.
6. Record the date and the capability level.

Also keep a **"transfer ledger"**: a table of findings × game tasks with a confidence grade (A = direct evidence in games; B = transported, with matching profile; C = bound only; D = speculative).

#### 6.5 Turning the user's propositions into testable hypotheses [PROPOSED]

**Proposition A: "Games are not mostly coding; much of the value comes from creative work and polish that create willingness to pay."**

| Hypothesis | Test design | Falsified if |
|---|---|---|
| **H-A1 (labor/cost structure).** Programming is a minority of production labor and cost | Discipline shares of FTE-months and payroll across a stratified sample of shipped titles, revenue-weighted. Sources: studio time-tracking (partners), public credits databases (role counts), Ukie-type censuses, job postings. Baseline: Ukie puts programming at ~19% of the whole workforce (≈31% of the core production roles listed: programming, art, design, QA, PM) | Programming ≥50% of production FTE-months or payroll in the revenue-weighted sample, **or** programming ≥ art + design combined |
| **H-A2 (sources of willingness to pay).** Creative and polish attributes explain more variation in willingness to pay and revenue than code-side or technical attributes, once a technical threshold is met | (i) Hedonic models on Steam titles. Outcome: log revenue/owners/wishlists, or review score. Regressors: blind expert ratings of art and visual quality, design novelty and narrative; technical indicators (crash and performance complaints from NLP on reviews, bug-report density); content volume (hours); price, genre, marketing proxies. (ii) Player conjoint experiments valuing art quality vs content volume vs polish vs AI disclosure. (iii) Review-text mining for categories of praise and complaint | Technical or volume attributes explain as much or more variance as creative/polish attributes; **or** conjoint willingness to pay for content volume ≥ that for art/polish; **or** AI-generated art is indistinguishable in blind tests **and** there is no disclosure penalty (then creative AI gains would convert to value) |
| **H-A3 (O-ring / polish).** Title value is governed by the weakest quality dimension | Compare fit of a multiplicative/min model vs an additive model of quality dimensions; test interaction terms; event studies of major post-launch polish/bug-fix/performance patches on review sentiment, player counts and sales (candidate cases: high-profile post-launch rehabilitations; outcomes to be measured) | The additive model fits as well; **or** improving the weakest dimension returns no more than improving the strongest; **or** polish patches have no measurable effect on outcomes |
| **H-A4 (Amdahl consequence).** AI gains confined to programming produce only small title-level time or cost cuts | Compute the bound S = 1/((1−p)+p/s) from measured programming share p and measured speed-up s; compare with observed schedule and cost changes | Observed title-level reductions exceed the programming-only bound. This would imply gains in other disciplines or reorganization, and would itself be informative |

**[INFERENCE] Illustrative arithmetic, not data (for H-A4).** Take a programming share of p = 0.25:

| Programming speed-up | Basis | Title-level time reduction |
|---|---|---|
| s = 1.26 | Cui et al. | ≈5% |
| s = 2 | Doubling | ≈12.5% |
| s → ∞ | Programming made instant | 25% maximum |

**Proposition B: "In coding, large task-level gains have not clearly become incremental industry-level value; volume ≠ value."**

| Hypothesis | Test design | Falsified if |
|---|---|---|
| **H-B1 (divergence).** Since 2023, software volume indicators have risen much more than value indicators | Build index series for 2019–2026: V0 (commits, PRs per developer, app releases); V2 (change-failure, incidents); V3 (revenue per employee, labor productivity in software publishing and IT services, usage/downloads per app, consumer spending). Firm-level staggered DiD by AI intensity (telemetry-measured), with pre-trend tests | High-adoption firms show sustained (≥4 quarters) value growth over low adopters, consistent with task speed-up × exposed share (Hulten-consistent); **or** software-sector labor productivity accelerates about ≥1 pp/yr above its 2015–2022 trend (≈ Anthropic's success-adjusted 1.0–1.2 pp/yr projection); **or** downloads/usage per new app stop diluting |
| **H-B2 (bottleneck mechanism)** | Measure review latency, queue lengths and change-failure rates alongside throughput | Throughput rises without rising review latency or instability |
| **H-B3 (J-curve mechanism).** Value lags complementary investment | Interact adoption with intangible investments: process redesign, test automation, platform engineering, training | No catch-up among heavy-investing adopters after ~3 years (the J-curve predicts early understatement, later catch-up) |
| **H-B4 (value-leakage mechanism).** Value goes to consumers and AI vendors, not to software-firm revenue | Software/SaaS price indices; AI-vendor revenue relative to software-firm margins; consumer-surplus estimates | Software-firm margins and revenue per employee rise in line with task-level gains |

**The key design point for Proposition B:** distinguish "**not yet**" (J-curve) from "**not in producer revenue**" (leakage) from "**not at all**" (bottleneck or quality offsets). Each implies a different game forecast.

**Game-side predictions derived from A + B** (pre-registered; each with a falsifier):

| Prediction | Expected pattern | Falsified if |
|---|---|---|
| **G1 Volume with dilution** | Releases and assets per title ↑; median revenue per release ↓; concentration stable or ↑; value elasticity of volume ≈0 | Total spend or playtime accelerates above the pre-2023 trend in proportion to supply; **or** median revenue per release holds while releases rise |
| **G2 Returns conditional on quality** | AI-disclosing titles pay a visible-asset penalty and depend on polish | No review or revenue gap after matching on team size, budget proxy, genre and price; **and** no interaction with polish measures |
| **G3 Bottleneck shift** | Art-director, design-review and QA/cert queue times rise in AI-adopting studios | Throughput rises with no increase in review latency |
| **G4 Baumol cost shift** | C/D budget share ↑ | C/D share stable or falling |
| **G5 Labor composition** | Junior E roles (junior art, QA testers, localization, outsourced art) fall first; senior C/D stable; their wage premium rises | Uniform declines, or junior art hiring rises after adoption |
| **G6 Homogenization** | Lower visual/design diversity (embedding dispersion) among AI-heavy titles; possibly fewer breakout hits | Diversity equal or higher, **and** breakout-hit rate among AI-heavy titles ≥ others |

#### 6.6 Research design: phases [PROPOSED]

- **P0 — Pre-registration and definitions dictionary.** Fix units and indicator definitions (tiers of "AI use"; survival-weighted contribution; disclosure scope; release-count source). Fix hypotheses and falsifiers.
- **P1 — Task inventories.**
  - Coding: O*NET plus SDLC tasks.
  - Games: build ~150–300 task statements across ~10 disciplines from pipeline documents, job postings, credits and practitioner talks.
  - Label C/E/D with two coders and validated LLM assistance.
- **P2 — Transfer-profile scoring.** Expert panel (≥3 per discipline), run as a Delphi with two rounds. Report inter-rater agreement. Link each score to evidence.
- **P3 — Reference classes and outside-view priors.**
  - Code coding (2022–26) and DTP, CAD, digital photography, digital music and CGI on the same outcome variables: volume multiple, unit price, concentration, E-role employment, C/D wages, years to peak effect.
  - Use these as priors (Kahneman–Lovallo; Flyvbjerg).
- **P4 — Diffusion and lag.**
  - Fit Bass curves per discipline for adoption **and** for intensity (Comin–Mestieri).
  - Estimate the coding → games lag with lead–lag Bass models or cross-correlation.
  - Data: surveys, Steam disclosures, postings, telemetry.
- **P5 — Causal identification.**
  - Staggered DiD (Callaway–Sant'Anna) of studio outcomes on AI-adoption timing.
  - Event studies around model releases, with exposure varying by discipline.
  - Synthetic control for markets or regions.
  - Within-studio RCTs on E-type asset tasks, graded by blind art-director review for speed, quality, iterations and style consistency.
  - METR-style RCTs for experienced game programmers, to measure the perception gap.
- **P6 — Aggregation and validation.**
  - Task → workflow: Amdahl and queueing with measured review capacity.
  - Workflow → product: an O-ring / CES model with elasticity below 1.
  - Product → market: a demand model with an attention constraint and heavy-tailed quality draws (Aguiar–Waldfogel logic).
  - Validate predictions against observed studio and market outcomes before forecasting.
- **P7 — Forecasting and monitoring.**
  - Scenario ranges with probabilities.
  - Scoring by Brier score, recalibrated quarterly (Tetlock).
  - A leading-indicator dashboard (§6.7).

#### 6.7 Leading indicators for games [PROPOSED]

| Area | Indicators |
|---|---|
| **Diffusion into hits vs the tail** | Share of new Steam releases disclosing AI, overall and within the top 1% / top 100 by revenue |
| **Disclosure penalty** | Review-score and refund gaps between AI-disclosing and matched non-disclosing titles |
| **Microstock-style price collapse** | Asset-marketplace (engine asset stores) submission volumes and prices |
| **E-type barometer** | Outsourcing-vendor revenue, occupancy and per-asset prices |
| **Job postings** | Junior art, QA and localization share; AI-skill mentions by discipline; creative-director and technical-art-director demand |
| **Tool usage** | Engine and DCC AI-feature usage (vendor-reported; low weight) |
| **Verification engineering** | Adoption of automated playtesting, style classifiers, balance simulators |
| **Capability** | Model performance on game-relevant verifiable benchmarks (3D asset validity, retargeting accuracy, localization QA), and time-horizon analogs for game tasks |
| **Legal and labor** | Copyright decisions, union agreements, platform policy changes |
| **Coding lead signals** | Automation share of agentic coding; review latency; instability metrics. These typically lead the corresponding game-programming signals |

#### 6.8 Pitfalls and mitigations

| # | Pitfall | Evidence it is real | Mitigation [PROPOSED] |
|---|---|---|---|
| 1 | **Volume ≠ value** | App supply up while downloads grow 2–3%; Steam median revenue $249; 88% of music tracks ≤1,000 streams; Faros PRs +98% vs review time +91% | Pair every V0 with V3 at the same unit; survival-weight contribution; use distributional statistics |
| 2 | **Survey bias** | METR perception gap (+20% felt vs −19% measured); vendor-commissioned "90% use" vs GDC "one-third"; stigma in games (52% negative sentiment; award rescinded) likely suppresses disclosure | Anchor to behavioral data; ask about specific tasks and frequencies; use list experiments for sensitive items; grade sources by independence |
| 3 | **Definitional inconsistency** | "AI use" (ever vs daily); "% of code by AI" (accepted suggestions vs surviving lines); Steam "disclosure" (shipped content vs tools); release counts differ by tracker (SteamDB 19,468 for 2025 vs other trackers; press summaries give other figures); "productivity" (speed vs throughput vs value) | Definitions dictionary (P0); sensitivity analyses across definitions |
| 4 | **Selection effects** | Users pick tasks they expect AI to handle (Anthropic caveat); early adopters differ in skill, budget and genre; AI-disclosing Steam titles likely skew small and low-budget (to be verified); survivorship in success stories | Matching on team size, budget and genre; DiD with pre-trends; RCTs; instruments such as exogenous access to tools |
| 5 | **Vendor claims** | Faros, GitClear and Google Cloud have commercial interests; company "% of code by AI" statements use undisclosed definitions | Source grading; prefer independent or peer-reviewed; demand method disclosure; replicate |
| 6 | **Confounding shocks** | End of zero interest rates, Section 174, the post-pandemic correction, 2023–25 game-industry layoffs | Less-exposed comparison groups; within-firm seniority contrasts (Canaries design); explicit macro controls |
| 7 | **Heavy tails** | Top 1% ≈84.5% of estimated Steam revenue; Paretian box office | Medians, quantiles, log models, hit rates, tail indices; avoid means |
| 8 | **Moving, jagged frontier** | METR time horizon doubling every ~4–7 months; jagged frontier | Time-stamp all transfer judgments; re-score every six months; task-level rather than discipline-level claims |
| 9 | **Aggregation bias** | Gans–Goldfarb: linear exposure overstates displacement under complementarity; Anthropic's complementarity scenario roughly halves projected gains | CES/O-ring aggregation with elasticity below 1; bottleneck modeling |
| 10 | **Level mismatch** | Comparing coding RCT task gains to game market revenue | The unit-matching rule (§6.1) |
| 11 | **Goodhart** | PR counts and asset counts are easily inflated | Report value and quality metrics next to every count |
| 12 | **Homogenization** | Individual quality up, collective diversity down (Doshi–Hauser; Zhou–Lee) | Measure diversity and novelty at market level; track breakout-hit rates |
| 13 | **Composition shifts** | Non-programmers shipping code (vibe coding) and solo AI-assisted game developers change what "per developer" or "per studio" means | Report per-person and per-title metrics alongside population counts; segment by team size |
| 14 | **Transfer error** | Effects vary widely across contexts (Vivalt) | Report transfer confidence grades; treat transported coding effects as priors to be updated with game data |

#### 6.9 What is established vs what is proposed

| Component | Status |
|---|---|
| Task-based framework; O-ring; Baumol; Amdahl/ToC; Jevons/demand elasticity; superstars; "nobody knows"; J-curve | **Established theory** (§1) |
| O-ring applied to AI automation (Gans–Goldfarb 2026); Expertise (Autor–Thompson 2025) | **Recent theory** (working papers) |
| Coding productivity RCTs; null aggregate labor effects; instability and bottleneck evidence; creative-AI diversity findings; historical creative-tech outcomes | **Empirical evidence**, of mixed quality: tagged per bullet in §§1–5 |
| Verifiability as the key transfer predictor | **Researcher framing** (Wei, Karpathy), consistent with **theory** (Acemoglu's easy/hard-to-learn tasks) and **evidence** (RLVR; METR messiness). Not yet tested on game tasks |
| Ten-dimension transfer profile; transfer rules and ledger | **Proposed** |
| C/E/D operational definitions, classification rules and proxies | **Proposed** (labels match sibling notes) |
| Units L1–L6; indicator funnel I1–I9; value ladder V0–V4 | **Proposed** |
| Hypotheses H-A1–4, H-B1–4, G1–G6 and their falsifiers | **Proposed** |
| Phases P0–P7; leading-indicator dashboard | **Proposed** |

### Gaps
- **Data access.** Studio time-tracking, pipeline telemetry and budgets are proprietary. H-A1, G3 and G4 need studio partnerships or public proxies (credits, postings, tax-credit filings), which are noisier.
- **No validated instrument yet exists for labeling game tasks C/E/D,** and no public game task inventory was found. P1 must build and validate one.
- **No published estimate of aggregate demand elasticity for games,** and no consumer-surplus estimate for games. G1 and H-B4-analog tests rest on proxies (playtime shares, spend totals).
- **Anchor data flagged as uncertain:**
  - UK census role shares (census year and definitions);
  - the Steam top-1% revenue share (analysis provenance);
  - Steam 2025 revenue statistics (model-based);
  - App Store download growth (vendor unverified).
- **Threshold choice.** The falsification thresholds above (≥4 quarters; ≥1 pp/yr; ≥50% programming share) are my calibration choices, not literature standards. They should be set in pre-registration with power calculations.
