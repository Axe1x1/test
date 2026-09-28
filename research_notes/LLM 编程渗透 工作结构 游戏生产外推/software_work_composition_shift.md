# How the composition of software-engineering work shifted during the LLM wave (Nov 2022 → Sep 2026): creative/generative vs execution/mass-production vs decision/iteration

*Tag legend used below.* **Work category:** **C** = creative/generative (problem framing, product ideation, architecture/system design, novel solutions); **E** = execution/mass-production (implementing specified features, boilerplate, tests, docs, migrations, refactors, routine bug fixes); **D** = decision/iteration (reviewing, validating, debugging, prioritizing, trade-offs, refining specs, integrating feedback, orchestrating/supervising agents); **O** = coordination/overhead (meetings, email, admin; outside the three categories but needed for the baseline). **Evidence type:** **M** = measured (telemetry, usage logs, payroll/admin data, RCTs, public activity data); **S** = survey/self-report; **A** = anecdote, company claim, or expert opinion; **P** = prediction/projection. "(via search summary)" = the number comes from a search-engine digest of the named primary source, because the session's network proxy blocked the primary page (e.g., faros.ai, dora.dev, survey.stackoverflow.co, hiringlab.indeed.com, gitclear.com, stanford.edu, arxiv.org). Treat those numbers with slightly lower confidence. Pages on anthropic.com, microsoft.com and github.com were read directly.

## 1. Pre-AI baseline: how did developers allocate their time before LLMs?

### Takeaway
Before LLMs, writing new code took a minority of developer time: about 11–16% for pure coding or "application development" in broad telemetry and surveys, and about 25% for code + tests + docs in Microsoft's 5,928-person time study. Debugging and review took about 19%, and meetings + email another 25%. Explicit specification/design was small (about 4%). This means E was the single largest engineering block but was capped as a share of the whole job, which bounds how much any E-speedup can change total time (Amdahl-style).

### Cited Findings
- **[Baseline, all categories | S, time diary]** Meyer, Barr, Bird & Zimmermann, "Today was a Good Day: The Daily Life of Software Developers" (IEEE TSE; preprint 2019). 5,928 Microsoft developers self-reported minutes spent on their previous workday (mean 9.08 hours at work). Shares (minutes): coding, i.e. "reading or writing code and tests", **15% (84 min)**; bugfixing, i.e. "debugging or fixing bugs", **14% (74)**; testing **8% (41)**; specification, i.e. "working on/with requirements", **4% (20)**; reviewing code **5% (25)**; documentation **2% (9)**; meetings (planned + unplanned) **15% (85)**; email **10% (53)**; interruptions / impromptu sync-ups **4% (24)**; helping, managing or mentoring **5% (26)**; networking **2% (10)**; learning **3% (17)**; administrative tasks **2% (12)**; breaks **8% (44)**; various, e.g. travel, planning, infra set-up, **3% (21)**. — [Microsoft Research preprint, Table 2](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/04/devtime-preprint-TSE19.pdf)
- **[E valued | S]** Same study: developers' "good" days had more coding (18%, 96 min) than "bad" days (11%, 66 min) and fewer meetings (14% vs 18%). The paper also finds that "meetings and interruptions are only unproductive during development phases; during phases of planning, specification and release, they are common and constructive." — [Microsoft Research preprint](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/04/devtime-preprint-TSE19.pdf)
- **[E share | S]** IDC ("How Do Software Developers Spend Their Time?", Adam Resnick, 2024 survey): application development was **16%** of developer time in 2024, up from **15%** in 2023. Security rose from **8% to 13%**. Most time went to operational/supporting tasks such as CI/CD, application-performance monitoring and infrastructure monitoring (via search summary). — [InfoWorld](https://www.infoworld.com/article/3831759/developers-spend-most-of-their-time-not-coding-idc-report.html); [itc.ua](https://itc.ua/en/news/developers-spend-only-16-of-their-working-time-on-coding-the-rest-is-spent-on-background-and-operational-tasks/)
- **[E share | M, IDE telemetry]** Software.com Code Time Report (first edition Jan 2022, 250K+ developers). "Code time" is active writing or editing in the editor. It averaged **52 minutes/day**, or 4h21m per week (about **11% of a 40-hour week**). A further **41 min/day** went to other in-editor work (reading code, reviewing PRs, browsing docs). Fewer than 10% of developers coded more than 2 hours/day. — [Software.com report](https://www.software.com/reports/code-time-report); [PR Newswire](https://www.prnewswire.com/news-releases/first-code-time-report-from-software-a-devops-company-reveals-most-developers-are-coding-less-than-an-hour-per-day-301462343.html)
- **[E/D routine maintenance | S]** Stripe "The Developer Coefficient" (Sept 2018; >1,000 developers and >1,000 C-level executives in five countries): developers spent **17.3 h of a 41.1-h week (42%)** on maintenance: 13.5 h on technical debt and 3.8 h on bad code (via search summary). — [Stripe PDF](https://stripe.com/files/reports/the-developer-coefficient.pdf)
- **[O friction | S]** Atlassian State of DevEx 2025: the top time-wasters are "finding information, adopting new technology, and context switching between tools" (via search summary). — [Atlassian](https://www.atlassian.com/blog/developer/developer-experience-report-2025); [SD Times](https://sdtimes.com/ai/report-ai-productivity-gains-cancelled-out-by-friction-points-in-other-areas-that-slow-developers-down/)

### Inferences
- Mapping the Meyer et al. table to the three categories. The assignment puts "routine bug fixes" in E and "debugging" in D, so bugfixing is split roughly 50/50.
  - **E** is about 25–32% of the whole workday: coding 15 + testing 8 + docs 2, plus about half of bugfixing.
  - **D** is about 12–19%: the other half of bugfixing plus code review 5. Decision content inside meetings and mentoring adds a few more points.
  - **C** is about 4–7% explicit: specification 4 plus part of "various/planning". Design embedded in coding and meetings is not separately measured.
  - **O** plus breaks is about 45%.
- Normalized over engineering work only (E+D+C), the pre-AI split was roughly **E 50–60% / D 30–40% / C 8–15%**. Confidence is medium on ordering and low on exact values, because the design share hidden inside "coding" is unmeasured.
- Stripe's 42% maintenance share and IDC's operational-task dominance mean a large pool of routine E and D work (migrations, refactors, debt, bug fixes) was the most automatable part of the job.
- Code-typing was only about 11–25% of time, so doubling its speed saves at most a few hours per week unless review, coordination and org friction also change. This foreshadows the "productivity paradox" findings in Q4.

### Gaps
- No pre-AI study cleanly separates creative design from implementation inside "coding". The C baseline is inferred.
- The IDC 2025 edition exists (IDC doc US53933325) but its content was not accessible. The Meyer et al. data are Microsoft-only and self-reported.
- No post-AI replication of a Meyer-style time diary (2025–26) was found. This is the single most important missing measurement for the hypothesis.

## 2. What direct evidence shows the task mix changing (2022–2026)?

### Takeaway
The evidence shows **two phases**.
- **Completion/chat era (2022–24):** AI made coding cheaper, and developers did *more* of their own coding and *less* project management and coordination (Hoffmann et al.). The human E share rose.
- **Agentic era (2025–26):** the model increasingly makes execution decisions. In Claude Code sessions, people make about **70% of planning decisions but only 20% of execution decisions**. Anthropic engineers report a net *decrease* in time per task category with a *larger* increase in output. The human role shifts toward directing, reviewing and validating, while AI begins to take over hands-on debugging too.

### Cited Findings
- **[E↑ time, O(PM)↓, C(exploration)↑ | M, natural experiment]** Hoffmann, Boysel, Nagle, Peng & Xu, "Generative AI and the Nature of Work" (SSRN 2024; HBS WP 25-021). Using GitHub Copilot's deployment to open-source developers, they find Copilot access raised the share of time on core coding by **12.4%** and cut the share on project management by **24.9%**. Mechanisms were more independent (less collaborative) work and more *exploration* relative to exploitation. Effects were larger for lower-ability developers (via search summary). — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5007084); [Wharton Mack Institute PDF](https://mackinstitute.wharton.upenn.edu/wp-content/uploads/2025/04/WTIC.2025_Nagle-Frank_Generative-AI.pdf)
- **[E throughput↑ | M, RCTs]** Cui, Demirer, Jaffe, Musolff, Peng & Salz (three RCTs; 4,867 developers at Microsoft, Accenture and a Fortune 100 firm; Management Science 2025): Copilot-style completion access produced a **26.08% (SE 10.3%) increase in completed tasks**. "Less experienced developers had higher adoption rates and greater productivity gains." — [Microsoft Research](https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/); [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535)
- **[D↑ cost for experts; contradicting | M, RCT]** METR (July 2025): 16 experienced OSS developers, 246 real tasks in their own large repos (22k+ stars, 1M+ LOC). With early-2025 AI tools they took **19% longer**, while believing they were **20% faster**. A Feb 2026 update said later data showed some evidence of speedup, but selection effects made the central estimate unreliable, so the study design was changed (via search summary). — [METR 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); [METR Feb 2026 update](https://metr.org/blog/2026-02-24-uplift-update/)
- **[E automation vs D augmentation, by tool | M, usage logs]** Anthropic Economic Index (AEI) software report, 500k coding interactions, Apr 6–13, 2025:
  - Automation share was **79% on Claude Code vs 49% on Claude.ai**.
  - "Directive" (full delegation) was **43.8% vs 27.5%**. "Feedback loop" (task completion guided by environmental feedback) was **35.8% vs 21.3%**.
  - JS/TS made up 31% of queries and HTML/CSS 28%. UI/UX component development was the top task (12%).
  - Startups were 32.9% of Claude Code conversations vs enterprises 23.8%.
  - Anthropic's interpretation: developers may "shift toward higher-level design and user experience work", and feedback loops show "humans are still very often involved."
  — [Anthropic](https://www.anthropic.com/research/impact-software-development)
- **[E↑ within AI use; D(debugging)↓ | M]** AEI September 2025 report (Dec 2024 → Aug 2025): the directive share of Claude.ai conversations rose from **27% to 39%**. "Creating new code" rose from **4.1% to 8.6%** of conversations, while debugging/error-correction fell from **16.1% to 13.3%**. 77% of business API use showed automation patterns, vs about 50% on Claude.ai. Computer & mathematical tasks were 36% of usage. — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report)
- **[D-mode rebound | M]** AEI January 2026 report (Nov 2025 data):
  - Computer & mathematical tasks were about one-third of Claude.ai conversations and nearly half of first-party API traffic. The top task was "modifying software to correct errors" (~10% of API records, 6% of Claude.ai).
  - Claude.ai augmentation was **52% vs automation 45%**, after automation briefly led in Aug 2025. Directive share fell from **39% to 32%**.
  - For software requests, the model-estimated human time without AI was about **3.3 hours**, and the success rate was **61%** (vs 78% for personal tasks).
  — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- **[D-mode among skilled users | M]** AEI March 2026 report (Feb 2026 data):
  - Computer & mathematical tasks were **35%** of Claude.ai conversations. In first-party API traffic they rose **14%** since Aug 2025, while falling **18%** in Claude.ai (relative changes as reported). Coding is migrating into API/agentic workflows.
  - High-tenure users (6+ months) are more likely to "iterate on their work, and much less likely to delegate greater responsibility through directive use patterns". They have about 10% higher success rates.
  - 34% of Software Developer tasks use Opus.
  — [Anthropic](https://www.anthropic.com/research/economic-index-march-2026-report)
- **[E autonomy↑ | M]** AEI June 2026 "Cadences" report (Apr 10–Jun 10, 2026):
  - AI autonomy is higher on Claude Code than in chat/Cowork for 26 of 31 output types. Scripts and code get **+0.53 autonomy points** (1–5 scale) on Claude Code.
  - **54%** of Claude Code sessions run on Opus, vs 10% of chat/Cowork.
  - On weekends, backend architecture, API debugging and data storage fall, while AI-agent design, quant trading and gaming rise.
  — [Anthropic](https://www.anthropic.com/research/economic-index-june-2026-report)
- **[E time↓, E output↑↑, D↑, C kept | S + M]** Anthropic internal study, "How AI is transforming work at Anthropic" (published Dec 2025; survey of 132 engineers/researchers in Aug 2025; 53 interviews; 200k internal Claude Code transcripts from Feb–Aug 2025):
  - Claude is used in **59%** of work (vs 28% a year earlier). Self-reported productivity is **+50%** (vs +20%).
  - Share of daily users using Claude for each task: debugging 55%, code understanding 42%, implementing new features 37%.
  - Claude Code task mix, Feb → Aug 2025: feature implementation **14.3% → 36.9%**; code design/planning **1.0% → 9.9%**; "papercut" fixes 8.6%.
  - Autonomy: max consecutive tool calls **9.8 → 21.2 (+116%)**; human turns per transcript **6.2 → 4.1 (−33%)**; task complexity **3.2 → 3.8**.
  - Across task categories: "we see a net decrease in time spent, and a larger net increase in output volume".
  - "More than half said they can 'fully delegate' only between 0-20% of their work".
  - Engineers keep "high-level or strategic thinking, or … design decisions that require organizational context or 'taste'". One said: "I usually keep the high-level thinking and design. I delegate anything I can from new feature development to debugging".
  - Some spend *more* time on Claude-assisted tasks because of "more debugging and cleanup of Claude's code".
  - One engineer expects work to shift "70%+ to being a code reviewer/reviser rather than a net-new code writer".
  — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- **[C/D human, E AI — most direct split | M]** Anthropic, "Agentic coding and persistent returns to expertise" (Jun 16, 2026; about 400k interactive Claude Code sessions from about 235k users, Oct 2025–Apr 2026):
  - "On average, people make about 70% of the planning decisions but only 20% of the execution decisions."
  - "The share of sessions spent fixing broken code fell from 33% to 19%… Operating software grew from 14% to 21% of sessions. Writing and data analysis roughly doubled, from about 10% to 20%."
  - "The estimated value of the average session rose by 27% between October and April."
  — [Anthropic](https://www.anthropic.com/research/claude-code-expertise)
- **[Broad adoption; valuable-work time | S]** DORA 2025 "State of AI-assisted Software Development" (via search summaries):
  - AI adoption is **90%** ("a 14% increase from last year" as reported; unclear whether percentage points). Median time interacting with AI is about **2 hours/workday**.
  - **>80%** perceive a productivity increase, and **59%** report a positive effect on code quality.
  - Trust: 24% trust "a great deal"/"a lot"; 30% "a little" (23%) or "not at all" (7%).
  - AI is now associated with better throughput, product performance and "time spent on valuable work". Throughput reversed from a negative 2024 finding, but delivery instability kept rising.
  — [DORA](https://dora.dev/dora-report-2025/); [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report); [Adam Ferrari](https://adamferrari.substack.com/p/ai-insights-from-the-2025-dora-report); [IT Revolution](https://itrevolution.com/articles/ais-mirror-effect-how-the-2025-dora-report-reveals-your-organizations-true-capabilities/)
- **[Humans keep C/D planning & ops | S]** Stack Overflow Developer Survey 2025 (via search summaries):
  - **84%** use or plan to use AI.
  - **76%** do not plan to use AI for deployment & monitoring, and **69%** not for project planning.
  - Agents: **52%** don't use agents or stick to simpler AI tools; **38%** have no plans to adopt; **14.1%** use agents daily.
  - The New Stack summarized this as about **23%** "regularly" using agents.
  — [SO 2025 AI section](https://survey.stackoverflow.co/2025/ai); [The New Stack](https://thenewstack.io/23-of-devs-regularly-use-ai-agents-per-stack-overflow-survey/); [DevOps.com](https://devops.com/stack-overflow-survey-shows-ai-adoption-for-devs/)
- **[E routine delegated first; core coding kept | S]** JetBrains State of Developer Ecosystem 2025 (24,534 developers, 194 countries, Apr–Jun 2025):
  - **85%** regularly use AI; **62%** rely on at least one AI coding assistant, agent or editor.
  - About **9 in 10** save ≥1 hour/week; **1 in 5** save ≥8 hours.
  - Writing tests and writing natural-language artifacts (comments/docs) are the tasks developers find most unpleasant and would most like to delegate. They "do not wish to delegate" understanding and writing code, which they find relatively enjoyable.
  — [JetBrains AI section](https://devecosystem-2025.jetbrains.com/artificial-intelligence); [JetBrains blog](https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/); [InfoWorld](https://www.infoworld.com/article/4077352/85-of-developers-use-ai-regularly-jetbrains-survey.html)
- **[Freed time → quality/features; O friction | S]** Atlassian State of DevEx 2025 (via search summaries):
  - **68%** save more than 10 h/week with AI, but **50%** lose 10+ h/week and **90%** lose 6+ h/week to organizational inefficiencies. The summary describes this as up from 33% the prior year; the comparison basis is unclear.
  - Saved time is reinvested, in ranked order, in "improving code quality, developing new features, improving engineering culture, and developing documentation."
  — [Atlassian](https://www.atlassian.com/blog/developer/developer-experience-report-2025); [Techzine](https://www.techzine.eu/news/devops/132992/ai-saves-development-time-but-inefficiencies-still-cause-losses/)
- **[E output↑ | A, company-internal]** Atlassian internal blog headline: "The AI-native SDLC is paying off: 19% more PRs and 2–3 hours saved per developer per week" (date and method not verified). — [Atlassian](https://www.atlassian.com/blog/ai-at-work/ai-native-sdlc-paying-off-per-developer-per-week)

### Inferences
- **Phase 1 (2022–24) moved against the hypothesis on time shares.** Completion tools raised coding throughput inside human hands and reduced coordination (Hoffmann). The human E share of time likely *rose* slightly, and PM/coordination time fell.
- **Phase 2 (2025–26) moves with the hypothesis.** Execution decisions shift to the model (people make only 20% of them), while humans keep about 70% of planning decisions (C/D). Anthropic's internal data show "less time, much more output" per task category, which is the individual-level form of the hypothesis.
- **D itself is being partly automated.** In Claude Code, "fixing broken code" sessions fell from 33% to 19%, and AEI debugging shares fell. What stays human in D is judgment (what to verify or accept, trade-offs, prioritization), not hands-on bug hunting. The hypothesis should say "decision" more than "iteration".
- **Skilled users keep an iterative style.** Augmentation rebounded and high-tenure users iterate more rather than delegating wholesale. The durable human mode is iterative supervision, not "fire and forget".
- **The median developer lags the frontier.** In mid-2025 only about 14% used agents daily, and many devs want to keep writing code. Frontier-firm findings overstate the median shift.

### Gaps
- No large-sample time-use measurement of human hours by category after 2024. AEI and Claude Code data measure *shares of AI sessions*, not shares of human time.
- DORA 2025's detailed breakdown of where freed time went, and any DORA 2026 report, were not accessible or found.
- JetBrains 2026 and Stack Overflow 2026 results appear not to be published yet. The SO 2026 survey opened Jun 23, 2026 ([SO blog](https://stackoverflow.blog/2026/06/23/the-2026-developer-survey-is-now-open-for-human-developers-only/)). One secondary site claims agent usage "doubled" ([Dev|Journal](https://earezki.com/ai-news/2026-06-23-the-2026-developer-survey-is-now-open-for-human-developers-only/)); this is unverified.
- Hoffmann et al.'s exact sample, period and variable definitions could not be read directly (SSRN/Wharton blocked).

## 3. Did output volume rise as capacity rose (Jevons-type effects), and did value per unit fall?

### Takeaway
Yes on volume: measured public-activity data show a sharp acceleration once agentic tools spread.
- GitHub pushes grew **+8.6% in 2024 → +34% in 2025 → +80% YoY in Q1 2026** (my aggregation of GitHub Innovation Graph).
- Commits rose **+25%** and merged PRs **+23%** (Octoverse 2025).
- New app releases rose **+60% to +104% YoY** in early 2026.
- Google's AI-generated share of new code went **~25% (Oct 2024) → ~50% (fall 2025) → 75% (Apr 2026)**.

Much new output is work "that wouldn't have been done otherwise" (27% at Anthropic). Value per unit is poorly measured. Quality signals suggest lower value density for marginal units, while model-estimated session value rose.

### Cited Findings
- **[E output volume | M, own aggregation]** GitHub Innovation Graph. Data are public and by economy; I summed all economies and excluded the "EU" aggregate to avoid double counting. The release is dated 2026-05-08, with data through 2026Q1. The metric is git pushes: "the number of times developers in a given economy uploaded code to GitHub during each quarter". Developer counts are a quarter-end stock of accounts, excluding bots/spam and including inactive accounts. — [Innovation Graph repo](https://github.com/github/innovationgraph); [datasheet](https://github.com/github/innovationgraph/blob/main/docs/datasheet.md); [git_pushes.csv](https://raw.githubusercontent.com/github/innovationgraph/main/data/git_pushes.csv); [developers.csv](https://raw.githubusercontent.com/github/innovationgraph/main/data/developers.csv)

  | Period | Git pushes (sum of economies) | YoY | Developer accounts (quarter-end) | Pushes per account |
  |---|---|---|---|---|
  | 2022 (year) | 503.5M | — | 92.5M (Q4) | 1.46 (Q4) |
  | 2023 (year) | 582.0M | +15.6% | 115.5M (Q4) | 1.29 (Q4) |
  | 2024 (year) | 632.0M | +8.6% | 139.6M (Q4) | 1.20 (Q4) |
  | 2025 (year) | 848.6M | +34.3% | 178.7M (Q4) | 1.38 (Q4) |
  | 2024 Q1 / Q2 / Q3 / Q4 | 153.0 / 158.3 / 152.9 / 167.8M | +6.1 / +7.7 / +8.2 / +12.3% | | |
  | 2025 Q1 / Q2 / Q3 / Q4 | 177.7 / 209.2 / 215.0 / 246.8M | +16.1 / +32.2 / +40.6 / +47.1% | | |
  | 2026 Q1 | 319.8M | **+80.0%** | 192.3M | **1.66** (+38% YoY) |
- **[E output volume | M]** GitHub Octoverse 2025 (Sept 1, 2024–Aug 31, 2025): "nearly 1 billion commits" (**+25.1%** YoY); **43.2M** PRs merged per month on average (**+23%**); 630M total repositories; >230 new repos per minute; **36M** new developers and 180M+ total (via search summary). — [GitHub blog](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)
- **[C/E output | M]** Octoverse 2024: 5.2B contributions across 518M projects; the number of generative-AI projects rose **+98%** and contributions to them **+59%** (via search summary). — [GitHub blog](https://github.blog/news-insights/octoverse/octoverse-2024/)
- **[E share of code output | A, company metric]** Google CEO Sundar Pichai (2026; coverage places the remark at Google Cloud Next 2026) said **75%** of Google's new code is AI-generated, up from about 25% in 2024 and 50% in fall 2025. He said a complex code migration ran six times faster than a year earlier, and described the workflow as "truly agentic", with engineers supervising agents. Google's definition of "AI-generated" was not verified. — [Fast Company](https://www.fastcompany.com/91531519/google-ceo-says-75-of-the-companys-code-is-ai-generated); [DevOps.com](https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/); [Fortune, Oct 2024 (25%)](https://fortune.com/2024/10/30/googles-code-ai-sundar-pichai)
- **[E+C product output | M for counts; attribution is press inference]** Appfigures data (via search summaries):
  - 2025 was the App Store's biggest release year in nearly a decade (~557,000 new apps).
  - Q1 2026 new releases were **+60% YoY** across App Store + Google Play, and **+80%** on iOS. April 2026 was **+104%** across both stores and **+89%** on iOS.
  - Productivity, utilities and lifestyle moved into the top categories.
  - TechCrunch attributes the surge to tools like ChatGPT, Claude, Cursor and Replit that let non-technical founders "vibe code".
  — [Appfigures](https://appfigures.com/resources/insights/20251205?f=2); [TechCrunch, Apr 18 2026](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/); [Digital Trends](https://www.digitaltrends.com/phones/ai-boom-fuels-surge-in-new-app-launches-across-app-store-and-google-play/)
- **[Unverified | A]** A low-credibility blog claims App Store review queues reached 45 days because of vibe-coded submissions. — [kkm-mako](https://kkm-mako.com/en/blog/articles/app-store-review-delay-vibe-coding-crisis/)
- **[Net-new work, lower-priority units | S]** Anthropic internal: "27% of Claude-assisted work consists of tasks that wouldn't have been done otherwise, such as scaling projects, making nice-to-have tools (e.g. interactive data dashboards), and exploratory work". "Papercut" fixes are 8.6% of Claude Code tasks. — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- **[Scope expansion | S]** Anthropic survey of 81,000 Claude users (April 2026): among those reporting productivity gains, "scope expansion" was the most common form (**48%**), ahead of speed (**40%**). Software developers reported among the highest gains. — [Anthropic](https://www.anthropic.com/research/81k-economics)
- **[E output per team | M]** Faros AI (July 2025; telemetry from about 10k developers across 1,255 teams): teams with high AI adoption "complete 21% more tasks and merge 98% more pull requests" (via search summary). — [Faros AI](https://www.faros.ai/blog/ai-software-engineering)
- **[Value per session | M, model-estimated]** "The estimated value of the average session rose by 27% between October and April" (Claude Code, Oct 2025–Apr 2026). — [Anthropic](https://www.anthropic.com/research/claude-code-expertise)

### Inferences
- **The Jevons-type output effect is real and appeared with agents, not autocomplete.** Push growth *decelerated* through the chat/completion era (2023 +15.6%, 2024 +8.6%) and accelerated sharply only from 2025Q2 (+32% → +80%). That timing matches agentic tools (e.g., Claude Code's 2025 launch, which Indeed also uses as a marker in Q6). Pushes per account also reversed their 2022–24 decline. Execution output scales with agent autonomy.
- **The share of mass-produced output rose sharply** (high confidence in direction at frontier firms, medium industry-wide). Machine-generated code went from a minority to a majority of new code at Google, and total code flow rose much faster than developer headcount.
- **Value per unit likely fell at the margin** (low–medium confidence). The marginal units are nice-to-have tools, papercuts, exploratory repos and a flood of small apps. The quality indicators in Q4 (duplication, churn, issues per PR) point the same way. Total value probably rose (session value +27%, Faros task completion +21%). "More units, lower average value per unit, higher total value" is the most consistent reading.
- **Part of the output surge comes from non-developers** (non-technical app founders; non-software occupations using Claude Code; see Q5). Execution capacity is diffusing beyond the software job family.

### Gaps
- No robust measure of value per unit over time (revenue or usage per app, per repo, or per PR) was found.
- Innovation Graph covers public activity, counts pushes rather than lines, and cannot separate agent-authored pushes made under human accounts. Very small economies are suppressed (below 100 developers), so totals are lower bounds.
- Full-year 2026 app data, and the share of new apps that are AI-built, are not available.
- Solo-founder and startup-formation statistics (e.g., Carta) were not retrieved because the session's web-search budget ran out.

## 4. Where did the bottleneck move (review, QA, specification, product decisions), and what happened to quality?

### Takeaway
As generation became cheap, the constraint moved to **human verification and integration (D)**.
- PR review time rose **+91%** at high-adoption teams, with no measurable company-level delivery gain (Faros).
- DORA reports rising delivery instability.
- AI PRs carry **~1.7x** more issues (CodeRabbit), and AI-generated code picks an insecure option **45%** of the time (Veracode).
- Duplication and churn are up and refactoring is down (GitClear).
- The industry coined "verification debt" (Werner Vogels), and firms added process gates such as Amazon's reported senior sign-off on AI-assisted changes.

### Cited Findings
- **[D bottleneck | M]** Faros AI (about 10k developers, 1,255 teams; July 2025): +21% tasks and +98% PRs merged, but "PR review time increases 91%, revealing a critical bottleneck: human approval". Developers say they work faster, but companies see no measurable improvement in delivery velocity or business outcomes (via search summary). Faros figures often cited elsewhere (PR size +154%, bugs per developer +9%) were **not verified** here. — [Faros AI report](https://www.faros.ai/blog/ai-software-engineering); [Faros paradox page](https://www.faros.ai/ai-productivity-paradox)
- **[D/quality | S]** DORA 2025: AI is "an amplifier"; "speed without stability is just accelerated chaos". Throughput improved but instability kept climbing unless the seven foundational capabilities (the AI Capabilities Model) are in place (via search summaries). — [DORA](https://dora.dev/dora-report-2025/); [Scrum.org summary](https://www.scrum.org/resources/blog/dora-report-2025-summary-state-ai-assisted-software-development)
- **[E quality / maintainability | M]** GitClear 2025 (211M changed lines, 2020–2024, repos including Google, Microsoft, Meta and enterprises):
  - Code blocks with ≥5 duplicated lines rose **8x** in 2024.
  - For the first time, copy/pasted lines exceeded "moved" (refactored) lines.
  - Moved lines fell from **24.1% (2020) to 9.5% (2024)**; copy/pasted lines rose from **8.3% to 12.3%**.
  - A secondary summary puts churn at about 3.3% pre-AI → 5.7% (2024) → 7.1% (2025).
  - GitClear published a 2026 "Maintainability Gap" report, whose details were not retrieved.
  — [GitClear 2025](https://www.gitclear.com/ai_assistant_code_quality_2025_research); [DevClass](https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250); [Larridin (churn, secondary)](https://larridin.com/developer-productivity-hub/code-churn-ai-era-doubled); [GitClear 2026](https://www.gitclear.com/the_ai_code_quality_maintainability_gap)
- **[D load per unit | M, vendor study]** CodeRabbit "State of AI vs Human Code Generation" (Dec 17, 2025; 470 open-source PRs): AI-generated PRs averaged **10.83 issues vs 6.45** for human PRs (~1.7x). Logic/correctness issues were +75%, security issues 1.5–2x, readability issues >3x, and performance inefficiencies ~8x (via search summary). — [CodeRabbit](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report); [BusinessWire](https://www.businesswire.com/news/home/20251217666881/en/CodeRabbits-State-of-AI-vs-Human-Code-Generation-Report-Finds-That-AI-Written-Code-Produces-1.7x-More-Issues-Than-Human-Code)
- **[D security review | M, benchmark]** Veracode 2025 GenAI Code Security Report (Jul 30, 2025; 80 tasks; 100+ LLMs; Java/Python/C#/JS): given a secure or insecure option, models chose the insecure one **45%** of the time. Java had a **72%** failure rate. The Spring 2026 update says syntax correctness now exceeds 95% while the security pass rate stays around **55%**, "virtually identical" to two years earlier (via search summary). — [BusinessWire](https://www.businesswire.com/news/home/20250730694951/en/AI-Generated-Code-Poses-Major-Security-Risks-in-Nearly-Half-of-All-Development-Tasks-Veracode-Research-Reveals); [Veracode Spring 2026](https://www.veracode.com/blog/spring-2026-genai-code-security/)
- **[D time↑ | S]** Stack Overflow 2025: the top frustration is "AI solutions that are almost right, but not quite" (**66%**). "Debugging AI-generated code is more time-consuming" is second (**45%**). 46% distrust AI accuracy vs 33% who trust it; only 3% "highly trust".
  - **Conflict:** several secondary sources say 29% trust AI (−11 points vs 2024). This likely reflects a different question wording or denominator.
  — [SO 2025 AI](https://survey.stackoverflow.co/2025/ai); [SO press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/); [secondary 29% figure](https://blog.codercops.com/blog/developer-ai-adoption-84-percent-2026)
- **[D verification criterion | S]** Anthropic engineers delegate tasks that are "easily verifiable", where "validation effort isn't large in comparison to creation effort". Some report "more debugging and cleanup of Claude's code" and more "cognitive overhead for understanding Claude's code". — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- **[D bottleneck framing | A, expert]** Werner Vogels (AWS CTO, re:Invent keynote, Dec 2025) popularized **"verification debt"**: AI makes code generation nearly free, but human review capacity has not scaled. He urged spec-driven development, automated reasoning, test pipelines and human code review, and said builders ("Renaissance developers") still own quality. — [Serverless Guru recap](https://www.sls.guru/blog/recap-of-dr-werner-vogels-aws-re-invent-2025-keynote-the-renaissance-developer); [LeadTechie](https://www.leadtechie.com/p/20251214-the-real-risk-of-ai-coding)
- **[D governance response; incidents | A, partly contested]** Amazon:
  - CNBC (Mar 10, 2026) reported an internal "deep dive" meeting on a "trend of incidents" with "high blast radius" and "Gen-AI assisted changes".
  - Secondary reports describe a Dec 2025 incident in which the Kiro agent deleted and recreated an environment (about 13 hours of downtime), and March 2026 retail outages.
  - Reported responses include senior-engineer sign-off on AI-assisted changes from junior and mid-level engineers, and a 90-day "code safety reset" for 335 critical systems. These details come mostly from secondary or low-credibility blogs.
  - Some coverage says Amazon disputed the AI attribution.
  — [CNBC](https://www.cnbc.com/2026/03/10/amazon-plans-deep-dive-internal-meeting-address-ai-related-outages.html); [Fortune](https://fortune.com/2026/03/11/elon-musk-amazon-outage-ai-relate-incident-meeting-report-cybersecurity); [paddo.dev (denial angle)](https://paddo.dev/blog/kiro-escalation/); [Vibe Graveyard](https://vibegraveyard.ai/story/amazon-ai-code-retail-outages/)
- **[O friction absorbs gains | S]** Atlassian 2025: developers "saving 10 hours a week using AI and losing 10 hours a week to inefficiencies" (via search summary). — [Atlassian](https://www.atlassian.com/blog/developer/developer-experience-report-2025); [SD Times](https://sdtimes.com/ai/report-ai-productivity-gains-cancelled-out-by-friction-points-in-other-areas-that-slow-developers-down/)
- **[D need per task | M]** In AEI data, software requests succeed only **61%** of the time (vs 78% for personal tasks), so a large share of AI outputs needs human correction. — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)

### Inferences
- **The bottleneck moved from E to D.** The scarce inputs are now review bandwidth, test and QA capacity, security review, integration, and organizational decision latency. Review load scales with PR count × PR size × defect density, and all three rose, while senior reviewer supply is fixed in the short run.
- **Mass-produced output carries more downstream D-work per unit.** Duplication, churn, issues per PR and insecure defaults all add review work. This partly offsets E savings and explains why org-level gains are modest (Faros, METR, Atlassian) even though individual output rises.
- **Policy responses institutionalize D as the scarce human role.** Examples are senior sign-off, spec-driven development, and delegating only "easily verifiable" work.
- **Specification is becoming an explicit bottleneck.** Vogels' spec-driven recommendation and experts' "precise framing" (Q5) show that clear intent is now a gating input. This is C/D work at the front of the pipeline.

### Gaps
- No causal, industry-wide measure of incident rates attributable to AI-written code. The Amazon details are partly secondary and contested.
- No industry data on the share of senior engineers' time spent on code review in 2022 vs 2026.
- Faros 2026 updates, GitClear 2026 details and DX-type telemetry (share of AI-authored code, hours saved) were not retrieved.

## 5. How did roles and skills evolve (orchestrator/reviewer/spec-writer; vibe coding; non-engineers shipping code)?

### Takeaway
The developer role is moving from author to **director and verifier**. Karpathy describes "orchestrating agents" instead of writing code "99% of the time", and Anthropic engineers describe themselves as "manager[s] of AI agents". The scarce skills are framing, specification, verification and domain expertise. Coding-agent success rates for non-engineers approach those of engineers, so execution is diffusing out of the profession. Measured risks: AI use reduces skill formation (17% lower comprehension, biggest gap in debugging), and supervision depends on skills that may atrophy.

### Cited Findings
- **[Role framing | A, practitioner]** Andrej Karpathy coined "vibe coding" in Feb 2025: "fully giving in to the vibes, embracing exponentials, and forgetting that the code even exists". A year later (Feb 2026) he proposed "agentic engineering": the new default is that "you are not writing the code directly 99% of the time, you are orchestrating agents who do". He stressed that it has "an art & science and expertise to it". — [Karpathy on X](https://x.com/karpathy/status/2019137879310836075); [The New Stack](https://thenewstack.io/vibe-coding-is-passe/)
- **[Role shift to D; breadth↑; skill risks | S/A]** Anthropic internal (Dec 2025):
  - Engineers become more "full-stack" ("I can very capably work on front-end… where previously I would've been scared").
  - Roles move toward "manager[s] of AI agents".
  - The "paradox of supervision": "supervising Claude requires the very coding skills that may atrophy from AI overuse".
  - Claude becomes the "first stop for questions that once went to colleagues". One engineer said "more junior people don't come to me with questions as often".
  — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- **[Skill formation risk; D skills | M, RCT]** Anthropic "How AI assistance impacts the formation of coding skills" (early 2026; RCT on learning a new Python library):
  - The AI group scored **17% lower** on a quiz about concepts used minutes earlier. The speedup was not statistically significant.
  - The largest gap was in **debugging**.
  - Participants who used AI for conceptual questions scored **≥65%**; those who delegated code generation scored **<40%** (via search summary).
  — [Anthropic](https://www.anthropic.com/research/AI-assistance-coding-skills)
- **[Expertise = framing + verification | M]** Anthropic "Agentic coding and persistent returns to expertise" (Jun 2026):
  - Expertise is rated on "how precisely the user frames their directions, what they ask Claude to verify, and whether the user tends to correct Claude or Claude tends to correct the user".
  - "Sessions rated expert reach verified success more than twice as often as those rated novice, and when a session hits trouble, novices abandon the session at several times the rate of everyone else."
  - Per the page summary (not verbatim): novice verified success about 15% vs 28–33% for intermediate and above. Expert prompts trigger about 2.4x more actions and about 5x more output per instruction. Returns flatten between intermediate and expert.
  — [Anthropic](https://www.anthropic.com/research/claude-code-expertise)
- **[Non-engineers ship code; E diffuses | M]** Same study: "Every one of the ten largest occupations in our dataset lands within seven points of software engineers in terms of their success". Per the page summary (not verbatim): software occupations have about 34% verified success vs about 29% for others, and management, sales and legal are the fastest-growing non-software user groups. — [Anthropic](https://www.anthropic.com/research/claude-code-expertise)
- **[Non-engineers ship code | S/A]** 81k survey quote: "I'm a non tech guy but now I'm a full stack developer". Early-career developers voice more displacement concern than seniors. — [Anthropic](https://www.anthropic.com/research/81k-economics)
- **[Non-engineers ship apps | A, press]** Non-technical founders can "vibe code" functional apps "in days, not months". — [TechCrunch](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/)
- **[Seniors = skeptical verifiers | S]** Stack Overflow 2025: experienced developers have the lowest "highly trust" rate (**2.6%**) and the highest "highly distrust" rate (**20%**) (via search summary). — [SO 2025 AI](https://survey.stackoverflow.co/2025/ai)
- **[Developers want to keep hands-on coding | S]** JetBrains 2025: developers want to delegate tests and docs but not code writing or understanding. Their concerns centre on losing control and "preserving their sense of competence". — [JetBrains](https://devecosystem-2025.jetbrains.com/artificial-intelligence)
- **[Ownership of quality | A, expert]** Werner Vogels: the "Renaissance developer" owns the quality of AI-written software, including regulatory compliance. — [Serverless Guru](https://www.sls.guru/blog/recap-of-dr-werner-vogels-aws-re-invent-2025-keynote-the-renaissance-developer)

### Inferences
- **Valued skills shift toward C and D:** precise problem framing, spec writing, verification design, taste, system-level judgment and domain knowledge. Syntax-level production (E) is commoditizing. Anthropic's expertise measure is literally "framing + what to verify + who corrects whom".
- **A pipeline paradox.** D-competence (debugging, review judgment) has historically been built through E-work. If juniors do less E (Q6) and AI use reduces debugging skill formation (RCT), the future supply of D-capable seniors may shrink. Hosseini & Lichtinger make this "erosion of the development pathway" argument explicitly.
- **Craft identity is a friction on the shift.** Developers enjoy hands-on coding (JetBrains), and some mourn the loss of craft (Anthropic). This slows the E→D shift for the median developer, compared with what capability alone would allow.
- **PMs, designers and domain experts increasingly perform E via agents.** The engineering role concentrates on D and C for systems that must be reliable.

### Gaps
- No quantitative survey was found on the share of PMs or designers shipping production code, or on "product engineer" role growth.
- Employer skill-demand trends (LinkedIn/Lightcast postings for system design, code review, "AI agents", domain expertise) were not retrieved because the search budget ran out.

## 6. What happened in the labor market (junior vs senior hiring, postings, AI-attributed layoffs)?

### Takeaway
Measured evidence points to **seniority-biased** change.
- Early-career employment and hiring in AI-exposed software roles fell. The Aug 2025 Canaries paper found a 6–16% employment fall in exposed occupations for ages 22–25, and about −20% from peak for software developers aged 22–25. By mid-2026 the gap was 19% below the counterfactual.
- Software postings remain about **27.5% below** Feb 2020, but have rebounded about 15% since Feb 2025. **71%** of that rebound is senior roles and **37%** is AI-titled roles.
- Unemployment in exposed occupations is not systematically up.
- AI-attributed layoff announcements rose from about **5%** of cuts in 2025 to about **23%** in H1 2026.

Macro confounders make causal attribution contested.

### Cited Findings
- **[Junior E-heavy roles↓ | M, payroll]** Brynjolfsson, Chandar & Chen, "Canaries in the Coal Mine?" (Stanford Digital Economy Lab; ADP payroll data).
  - Anthropic's Mar 2026 summary of the Aug 2025 version: "a 6—16% fall in employment in exposed occupations among workers aged 22 to 25", attributed "primarily to a slowdown in hiring rather than an increase in separations".
  - Search summaries of the Stanford pages: software developers aged 22–25 are down about **20%** from the late-2022 peak. In the **Aug 2026 update** (data through June 2026), young workers in AI-exposed occupations are **19% below** where they would be had they kept pace with less-exposed peers. Experienced workers show no comparable gap, and there is no evidence of economy-wide displacement.
  - The widely cited Aug-2025 headline figure of "13%", and the finding that declines concentrate where AI *automates* rather than *augments*, were **not re-verified** in this session.
  — [Anthropic summary](https://www.anthropic.com/research/labor-market-impacts); [Stanford publication page](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/); [Aug 2026 PDF](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)
- **[Exposure high; unemployment flat; junior entry↓ | M, CPS]** Anthropic "Labor market impacts of AI: A new measure and early evidence" (Mar 5, 2026):
  - "Computer Programmers are at the top, with 75% coverage" of tasks under its new "observed exposure" measure.
  - "The unemployment rate for young workers in the exposed occupations is flat."
  - For ages 22–25, "Entry into the most exposed jobs decreases by about half a percentage point. The averaged estimate in the post-ChatGPT era is a 14% drop in the job finding rate". This is described as barely statistically significant, with no similar decline for workers over 25.
  - The authors reconcile this with Canaries: "slowed hiring may not necessarily manifest as increased unemployment, since many young workers are labor market entrants without a listed occupation."
  — [Anthropic](https://www.anthropic.com/research/labor-market-impacts)
- **[Seniority-biased change | M, résumés/postings]** Hosseini Maasoum & Lichtinger, "Generative AI as Seniority-Biased Technological Change" (SSRN 2025; about 285k firms, 62M workers, 245M postings, 2015–2025): after GenAI adoption, junior employment declines sharply in adopting firms relative to non-adopters, while senior employment is largely unchanged. The effect is concentrated in the most exposed occupations and driven by slower hiring. The authors argue this "can erode the future supply of the very expertise it complements" (via search summary). — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555)
- **[Postings: level low, rebound senior/AI-skewed | M]** Indeed Hiring Lab (Jul 8, 2026 post and monthly snapshots; via search summary): software development postings are about **27.5% below** the Feb 2020 level, with a trough index of **61.1 in May 2025**. They are up about **15%** since Claude Code's release in late Feb 2025. **71%** of the May 2025–May 2026 increase comes from senior roles, and **37%** from jobs with "AI" in the title. — [Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/); [FRED series](https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE); [CIO](https://www.cio.com/article/4195780/it-hiring-sees-a-boost-as-software-development-jobs-slowly-bounce-back.html)
- **[New-grad hiring↓ | M, VC dataset]** SignalFire State of Talent 2025: new-grad hiring is down **>50%** from pre-pandemic levels. New grads are **7%** of Big Tech new hires, and the share of new grads landing at the "Magnificent Seven" has fallen by more than half since 2022. A 2026 edition exists but was not retrieved. — [SignalFire 2025](https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025)
- **[AI-attributed layoffs↑ | M, announcements with employer-stated reasons]** Challenger, Gray & Christmas:
  - **2025:** AI was cited for **54,836** announced cuts (about 5% of the total). Cumulative since May 2023 through Dec 2025: 71,825.
  - **2026:** Jan 7,624; Feb 4,680; through March 27,645 (~13% of cuts). April: 21,490, or 26% of that month's cuts, with AI the top reason. Through June: **101,743 (~23% of all cuts)**. AI was the leading reason for the fifth straight month in July (10,970).
  - Technology-sector cuts Jan–Jul 2026: 149,023 (**+67% YoY**).
  — [GitHub gist compiling Challenger AI passages](https://gist.github.com/mcphil/08f8f011f27c9864d157ead0b9d716d9); [Challenger (July 2026)](https://www.challengergray.com/blog/challenger-report-layoffs-fall-hiring-picks-up-ai-leads-for-fifth-straight-month/); [Challenger (June 2026)](https://www.challengergray.com/blog/challenger-report-june-layoffs-cool-to-45849-down-53-from-may-ai-leads-reasons-for-fourth-consecutive-month/); [Challenger April 2026 PDF](https://www.challengergray.com/wp-content/uploads/2026/05/Challenger-Report-Apr2026001249.pdf)
- **[Junior productivity gains vs junior hiring | M]** RCTs show "less experienced developers had higher adoption rates and greater productivity gains". — [Microsoft Research (Cui et al.)](https://www.microsoft.com/en-us/research/publication/the-effects-of-generative-ai-on-high-skilled-work-evidence-from-three-field-experiments-with-software-developers/)
- **[Unverified | A]** A press claim that Snap reached 65% AI-generated code and cut planned headcount appears in coverage of Google's 75% statement; it was not verified. — [DevOps.com](https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/)
- **[Prediction | P]** Anthropic "Scenarios for our Economic Future" (Sep 2026) sets out three 2030 scenarios. In the "substantial" scenario, knowledge-worker wages are "essentially flat". In the "extreme" scenario they "fall by more than 10% by 2030", and "coders and call service center agents may have to switch to jobs like electrician and nurse". — [Anthropic](https://www.anthropic.com/institute/econ-scenarios)

### Inferences
- **Headcount patterns fit the hypothesis on the labor side.** AI plus seniors substitutes for entry-level E capacity (juniors historically did implementation, tests and bug fixes). Demand concentrates on D/C-heavy senior roles and AI-specific roles, as the senior- and AI-skewed posting rebound shows.
- **Why juniors are hired less despite gaining most per task.** RCTs show juniors gain most per task, yet firms hire fewer juniors. This suggests the binding constraint is D (judgment, verification, accountability), not E throughput, which is consistent with the bottleneck evidence in Q4.
- **A partial Jevons effect on labor demand.** Postings rose about 15% since Feb 2025 while output accelerated, but the new demand is senior and AI-skewed and has not restored junior hiring.
- **Attribution caution.** Posting declines began in 2022, before ChatGPT's impact, amid interest-rate tightening and a post-2021 over-hiring correction. Challenger counts reflect employer-stated reasons, which may overstate AI's role. The exposure-comparison designs (Canaries, Anthropic) are the most credible evidence and still find modest effects.

### Gaps
- BLS OES/CPS software-developer employment for 2025–26, NY Fed recent-graduate unemployment by major, LinkedIn Economic Graph and ADP series were not retrieved (search budget exhausted and domains blocked).
- Contradicting studies could not be verified in-session and should be checked before use: Humlum & Vestergaard, "Large Language Models, Small Labor Market Effects" (Denmark; NBER w33777), reportedly finding near-zero effects on earnings and hours; and the Yale Budget Lab's reported finding of little aggregate occupational disruption.
- Confounders (interest rates, the US Section 174 R&D amortization change, post-pandemic correction) were not quantified here.

## 7. Which frameworks map software tasks to creative / routine / judgment categories, and what do they predict about the three-way split?

### Takeaway
Task-exposure and usage frameworks consistently rate **execution-type programming tasks as most exposed**:
- Computer programmers have **75%** task coverage in Anthropic's observed exposure measure.
- Programmers, web developers and QA testers score above software developers, and far above computer & IS managers, on Microsoft's applicability score.

They rate **judgment and management tasks as least exposed**. Usage taxonomies (automation = directive + feedback loop; augmentation = iteration, validation, learning) give a measurable proxy for E vs D. Together they predict that human E-time falls, D rises, and C holds or rises. Critical thinking remains the least exposed skill (per Eloundou et al.; not re-verified here).

### Cited Findings
- **[Exposure by occupation | M/framework]** Microsoft Research "Working with AI" (Tomlinson, Jaffe, Wang, Counts, Suri; July 2025). It uses 200k anonymized Bing Copilot conversations (Jan–Sep 2024) mapped to O*NET work activities and separates user goals from AI actions. AI applicability scores (0–1):

  | Occupation (SOC) | Score |
  |---|---|
  | Data Scientists | 0.357 |
  | Web Developers | 0.353 |
  | Software QA Analysts & Testers | 0.328 |
  | Computer Systems Analysts | 0.313 |
  | Computer Programmers | 0.310 |
  | Web & Digital Interface Designers | 0.294 |
  | Software Developers | 0.278 |
  | Computer & Information Systems Managers | 0.152 |
  | *Top overall:* Interpreters & Translators | 0.492 |
  | *Top overall:* Writers & Authors | 0.454 |

  The authors: "our study does not draw any conclusions about jobs being eliminated". — [arXiv 2507.07935](https://arxiv.org/abs/2507.07935); [scores CSV](https://raw.githubusercontent.com/microsoft/working-with-ai/main/ai_applicability_scores.csv); [MSR blog, Aug 21 2025](https://www.microsoft.com/en-us/research/blog/applicability-vs-job-displacement-further-notes-on-our-recent-research-on-ai-and-occupations/)
- **[Automation vs augmentation taxonomy | framework + M]** Anthropic Economic Index modes:
  - **Automation** = "directive" (complete delegation with minimal interaction) and "feedback loop" (task completion guided by environmental feedback).
  - **Augmentation** = task iteration, validation and learning.
  - Coding is split: Claude Code is 79% automation vs Claude.ai 49%.
  — [Anthropic](https://www.anthropic.com/research/impact-software-development)
- **[Observed exposure | framework]** Anthropic (Mar 2026) combines Eloundou et al.'s theoretical β with real usage, weighting work-related and automated uses more heavily. Computer programmers rank highest (75% coverage). "AI is far from reaching its theoretical capability: actual coverage remains a fraction of what's feasible." — [Anthropic](https://www.anthropic.com/research/labor-market-impacts)
- **[Empirical planning vs execution split | M]** In Claude Code sessions, humans make about 70% of planning decisions and 20% of execution decisions. This operationalizes C/D (human) vs E (AI). — [Anthropic](https://www.anthropic.com/research/claude-code-expertise)
- **[Seniority-biased technological change | framework]** GenAI "substitutes for entry-level execution while complementing expert judgment" (Hosseini & Lichtinger; via search summary). — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555)
- **[Amplifier framework | framework]** DORA's AI Capabilities Model: seven foundational practices determine whether AI's throughput gains turn into instability or into performance. — [DORA](https://dora.dev/dora-report-2025/)
- **[Practitioner framework | A]** Vibe coding vs agentic engineering (Karpathy). — [The New Stack](https://thenewstack.io/vibe-coding-is-passe/)
- **[Taxonomy exists; details not retrieved]** JetBrains "AIDEs Framework: A Definitive 5-Level AI System" (Sept 2026). — [JetBrains](https://blog.jetbrains.com/research/2026/09/aides-framework/)

### Inferences
- **Mapping frameworks to the three categories:**
  - **E** matches "automation"-mode usage and high-exposure O*NET tasks (write/modify code, test, document). This is why programmer, web-developer and QA scores exceed those of the broader "software developer" and of IS managers.
  - **D** matches augmentation modes (validation, iteration) and management and oversight tasks. These have lower exposure, and demand for them rises with output (Q4).
  - **C** matches problem framing and critical thinking, which have the lowest exposure in theory. However, usage data show AI entering design (1.0% → 9.9% of Claude Code tasks at Anthropic), so C is augmented rather than untouched.
- **Break with the Autor-style routine/non-routine lens.** Earlier automation took *routine* tasks, while coding is non-routine cognitive work. LLMs automate a large share of non-routine cognitive *execution*. Human comparative advantage shifts to accountable judgment (D) and intent-setting (C) rather than to "non-routine" work per se.
- **Framework prediction for the split.** Expect the human time share E↓, D↑, C↑ or flat. Expect the output share of E to rise (mass-produced) and headcount to be pulled toward roles defined by D/C. All of these are consistent with Q2–Q6.

### Gaps
- No published taxonomy directly measures the C/E/D split over time. Constructing one would require mapping O*NET task statements for SOC 15-1252/15-1251 into the three categories and weighting them with usage data.
- Background frameworks were not re-verified in-session: Eloundou, Manning, Mishkin & Rock, "GPTs are GPTs" ([arXiv 2303.10130](https://arxiv.org/abs/2303.10130)), reported to find programming and writing skills positively associated with exposure and science and critical thinking negatively associated; and Autor, Levy & Murnane (2003).

## 8. Synthesis: how has the three-way split of developer time and of output moved (Nov 2022 → Sep 2026)?

### Takeaway
**The hypothesis is broadly supported for the agentic era (2025–26), with three qualifications:**
1. In 2022–24 the human time shift went the other way (more hands-on coding, less coordination).
2. D-work itself is being partly automated (debugging share falling), so scarce human time concentrates in *decision* (what to build, what to accept, trade-offs) more than in hands-on *iteration*.
3. The shift is much larger at frontier, AI-intensive teams than for the median developer.

Output moved more than time. Machine-produced E-output went from a minority to a majority of new code at frontier firms, and total output accelerated sharply in 2025–26.

### Cited Findings
Key anchors, each sourced above:
- **Baseline:** E (coding + tests + docs) was about 25% of the workday, D (bugfixing + review) about 19%, and specification 4%. — [Meyer et al.](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/04/devtime-preprint-TSE19.pdf)
- **2022–24:** coding share +12.4%, project-management share −24.9% with Copilot. — [Hoffmann et al.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5007084)
- **2025–26:** humans make about 70% of planning decisions and 20% of execution decisions. Debugging sessions fell from 33% to 19%. — [Anthropic](https://www.anthropic.com/research/claude-code-expertise)
- **Individual level:** "net decrease in time spent, and a larger net increase in output volume"; "70%+… code reviewer/reviser"; 27% net-new work. — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- **Frontier practice:** "not writing the code directly 99% of the time". — [Karpathy](https://x.com/karpathy/status/2019137879310836075)
- **Output volume:** pushes +34% (2025) and +80% YoY (2026Q1). — [GitHub Innovation Graph](https://github.com/github/innovationgraph). Commits +25%, PRs +23%. — [Octoverse 2025](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/). App releases +60% to +104% YoY. — [TechCrunch](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/)
- **Machine share of new code:** Google 25% → 50% → 75%. — [Fast Company](https://www.fastcompany.com/91531519/google-ceo-says-75-of-the-companys-code-is-ai-generated)
- **Bottleneck:** review time +91%. — [Faros](https://www.faros.ai/blog/ai-software-engineering). Instability rising. — [DORA](https://dora.dev/dora-report-2025/). Issues per PR 1.7x. — [CodeRabbit](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report)
- **Median-developer adoption:** DORA median AI interaction is 2 h/day. — [DORA](https://dora.dev/dora-report-2025/). Only 14.1% used agents daily in mid-2025. — [Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai)
- **Labor:** junior employment 19% below counterfactual by mid-2026 ([Canaries Aug 2026](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf)); posting rebound 71% senior ([Indeed](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/))

### Inferences
**Estimated share of *engineering* time** (E+D+C = 100%; coordination/overhead, about 35–45% of the workday, excluded). These are my triangulated estimates, not measurements:

| Category | Pre-AI baseline (≈2019–Nov 2022) | 2023–24 (completion/chat era) | Median developer, mid-2026 | AI-intensive / agent-first teams, mid-2026 | Confidence |
|---|---|---|---|---|---|
| **E: execution / mass production** (hands-on writing of code, tests, docs, routine fixes) | ~50–60% | ~same or slightly **higher** (Hoffmann: more coding, less PM) | ~40–50% | ~15–25% | Direction: **high** at frontier, **medium** for median. Magnitude: **low–medium** |
| **D: decision / iteration** (review, validation, debugging oversight, spec refinement, prioritizing, supervising agents) | ~30–40% | ~same | ~40–45% | ~55–65% | Direction: **medium–high**. Magnitude: **low**. Note: hands-on debugging within D is itself being automated, so the growth is in review, acceptance and steering |
| **C: creative / generative** (framing, ideation, architecture, novel solutions) | ~8–15% | slightly ↑ (more exploration) | ~10–15% | ~15–20% | Direction: **medium** (humans keep ~70% of planning decisions; exploration and new projects ↑). Magnitude: **low**. AI is also entering design work (1% → 10% of Claude Code tasks) |
| *Coordination/overhead (outside split)* | ~35–45% of the day | slightly ↓ (less PM) | ~flat (org friction offsets AI savings) | ~flat or ↑ (more review coordination) | **Low** |

**Estimated output composition:**

| Output dimension | Nov 2022 | Sep 2026 | Confidence |
|---|---|---|---|
| Share of new code that is machine-produced (E mass production) | Low. Earliest datapoint found is ~25% at Google in Oct 2024 | 50–75%+ at frontier firms; lower industry-wide | **High** direction; **medium** level (company definitions) |
| Growth of total code output (GitHub pushes) | +15.6% (2023), +8.6% (2024) | +34.3% (2025), +80% YoY (2026Q1) | **High** (measured; public activity only) |
| Product and project output (apps, repos, "work that wouldn't have been done") | Baseline | App releases +60% to +104% YoY in early 2026; 27% net-new work at Anthropic | **Medium–high** |
| Value per unit of output | Baseline | Likely **lower** for marginal units: duplication 8x, churn ~2x, issues/PR 1.7x, nice-to-have tools. Total value higher (session value +27%) | **Low–medium** |
| Headcount mix | Junior pipeline intact | Junior (E-heavy) employment and hiring down (6–16% fall in exposed occupations for ages 22–25 per Aug 2025 Canaries; ~−20% from peak for software developers aged 22–25; 19% below counterfactual by mid-2026; new grads 7% of Big Tech hires); rebound led by senior (71%) and AI roles | **Medium–high** for junior decline; **medium** for AI causation |

Interpretation notes:
- **The path is non-monotonic.** Completion tools first *increased* the human E-share by stripping coordination overhead. Agents then *decreased* it by moving execution decisions to the model. Any "Nov 2022 vs Sep 2026" comparison hides this U-shape.
- **Jevons holds for output, only partly for labor.** Execution output grew far faster than headcount. Labor demand is recovering only in senior and AI-skewed roles, because D capacity (review, verification, accountability) is the binding constraint.
- **"Iteration" is being split in two.** Mechanical iteration (fix-run-fix loops, "feedback loop" automation) is moving to agents. Human D-time is concentrating in *decisions*: acceptance, trade-offs, specification and prioritization. The hypothesis is best restated as: "AI raised production capacity, so the share of mass-produced output rose. Scarce human time shifted toward decision-making, verification and creative direction, while mechanical iteration is increasingly automated too."
- **Heterogeneity is large.** Effects are strongest in web/front-end, greenfield and startup contexts (JS/TS and HTML/CSS dominate AI coding use; startups over-index on Claude Code). They are weakest in large legacy codebases maintained by experts (METR) and in ops/deployment (76% don't plan to use AI there).

### Gaps
- **No direct measurement exists** of human time by C/E/D category after 2024. The estimates above triangulate from shares of AI sessions, self-reports, frontier-company claims and one pre-AI time diary, so magnitudes carry wide uncertainty (±10–15 points).
- Frontier data (Anthropic, Google, Claude Code users) over-represent AI-intensive settings. Industry-median evidence is mostly from 2025 surveys, and 2026 editions of Stack Overflow, JetBrains and DORA were not available.
- Value-per-unit and incident-rate data are thin and vendor-heavy (CodeRabbit, Veracode, GitClear, Faros).
- Research constraint: this session's web-search budget ran out mid-research, and many primary domains were blocked. Several figures are therefore from search-engine digests of primary sources (marked "via search summary") and should be spot-checked before publication.
