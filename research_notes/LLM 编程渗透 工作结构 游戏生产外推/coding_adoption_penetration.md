# LLM/AI Coding Tools: Adoption and Penetration Trajectory, Nov 2022 to Sep 2026 (global, with a China subsection)

Compiled 2026-09-28. Every item carries a verification tag:
- **[V1]**: I fetched the primary page in this session and quoted it.
- **[V2]**: confirmed only through a search-engine summary of the linked page. I could not open the page itself because the session's egress proxy blocked most third-party domains: stackoverflow.*, jetbrains.com, github.blog, openai.com, cursor.com, gartner.com, dora.dev, techcrunch.com, menlovc.com, wikipedia, CNBC, Bloomberg and all Chinese sites tried. Spot-check the exact wording and decimals.
- **[V3]**: my prior knowledge of the linked primary source, from training data up to about mid-2026. I could not re-check it because the session's web-search budget ran out partway through (200/200) and the domain was blocked. Verify it before using it as a headline number.

General bias notes:
- **Who runs the surveys.** Nearly all developer surveys are run by vendors: GitHub/Microsoft, JetBrains, Google (DORA) and Atlassian. Stack Overflow also sells AI products.
- **How they are answered.** All are opt-in and self-reported.
- **Wording.** The wording changes from year to year. "Using or planning to use" is not the same as "currently using", "regularly use" or "daily".
- **Company figures.** Companies report their own usage numbers, and the definitions drift over time: "paid subscribers", then "users", "all-time users", and "active users" with no time window.

---

## 1. What do the major recurring developer surveys report, year by year? (individual and organizational adoption)

### Takeaway
Across the major surveys, "any use" of AI in development work grew in three steps:
- about 44% currently using in May 2023 (Stack Overflow);
- 62% in May 2024 (Stack Overflow) and 75.9% in 2024 (DORA);
- 84–90% by mid/late 2025 (SO 84% using or planning; JetBrains 85% regular use; DORA 90%).

JetBrains then found about 90% of professional developers regularly using at least one AI tool at work in January 2026. So breadth of adoption is saturated, and the movement in 2025–26 is in intensity and in agents. Measures of that:
- daily use by 51% of professional developers (SO 2025);
- 68% daily use of AI coding agents in JetBrains' mid-2026 wave, which is definition-sensitive.

The Stack Overflow 2026 survey only opened on 2026-06-23 and I found no primary 2026 results. Web pages titled "Stack Overflow 2026 survey results" are recycling the 2025 numbers.

### Cited Findings

**Table 1: Developer-survey adoption time series (chronological by fieldwork)**

| Fieldwork → publication | Survey (sponsor / bias) | Sample | Metric (wording as reported) | Result | Source |
|---|---|---|---|---|---|
| Early 2023 → 2023-06-13 | GitHub / Wakefield Research (vendor) | 500 US developers at companies with 1,000+ employees | "already using AI coding tools both in and outside of work" | 92% | [GitHub blog](https://github.blog/news-insights/research/survey-reveals-ais-impact-on-the-developer-experience/) [V3] |
| May 2023 → Jun 2023 | Stack Overflow 2023 (opt-in; SO audience) | ~90,000 (89,184) [V3] | "Do you currently use AI tools in your development process?" (Yes / No, but I plan to / No) | 44% currently using; 70% using or planning (≈26% planning) | 70% and 44% restated in the [SO 2024 press release](https://stackoverflow.co/company/press/archive/stack-overflow-2024-developer-survey-gap-between-ai-use-trust/) [V2]; [SO 2023 AI page](https://survey.stackoverflow.co/2023/#ai) [V3] |
| Early 2023 / early 2024 (analyst estimate) | Gartner | n/a | Enterprise software engineers using AI code assistants | "<10% in early 2023"; "<14% in early 2024" | [Gartner PR 2024-04-11](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028) [V2] (also see Q4) |
| Q4 2023 → 2024-04-11 | Gartner survey | 598 global respondents [V3] | Organizations "piloting, deploying or have already deployed AI code assistants" | 63% [V3] | [Gartner PR](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028) [V3] |
| 2024-02-26 to 2024-03-18 → 2024-08 | GitHub "AI in software development 2024" (vendor) | 2,000 non-student, non-manager enterprise respondents (500 each in US, Brazil, India, Germany) at 1,000+ employee companies | "used AI coding tools at work at some point" | >97%. Employer "actively encourages" or "allows" use: 59% (Germany) to 88% (US) | [GitHub blog](https://github.blog/news-insights/research/survey-ai-wave-grows/); [InfoWorld](https://www.infoworld.com/article/3489925/github-survey-finds-nearly-all-developers-using-ai-coding-tools.html) [V2] |
| May–Jun 2024 → 2024-07-24 [V3 date] | Stack Overflow 2024 | 65,000+ | Same question as 2023 | 62% currently using; 76% using or planning | [SO 2024 press release](https://stackoverflow.co/company/press/archive/stack-overflow-2024-developer-survey-gap-between-ai-use-trust/); [SO 2024 AI page](https://survey.stackoverflow.co/2024/ai) [V2] |
| 2024 → 2024-10-22 | Google DORA "2024 Accelerate State of DevOps" (Google-sponsored) | Not stated in blog (≈3,000 [V3]) | Respondents who "rely on AI for at least one daily professional responsibility" | 75%+ (75.9% in the report [V3]) | [Google Cloud blog](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) [V1] |
| 2024 → Dec 2024 | JetBrains State of Developer Ecosystem 2024 (IDE vendor) | 23,262 [V3] | Tried ChatGPT for coding / use it regularly; tried GitHub Copilot / use regularly | 69% / 49%; 40% / 26% [V3] | [JetBrains DevEco 2024](https://www.jetbrains.com/lp/devecosystem-2024/) [V3] |
| Apr 2025 | JetBrains AI Pulse (earlier wave) | n/a | Claude Code used at work | 3% | [JetBrains blog, Apr 2026](https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/) [V2] |
| Apr–Jun 2025 → 2025-10-15 | JetBrains State of Developer Ecosystem 2025 | 24,534 developers, 194 countries | "Regularly use AI tools for coding and development"; "rely on at least one AI coding assistant, agent, or code editor" | 85%; 62% (15% not yet adopted AI in daily work) | [JetBrains blog](https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/); [InfoWorld](https://www.infoworld.com/article/4077352/85-of-developers-use-ai-regularly-jetbrains-survey.html) [V2] |
| May–Jun 2025 → 2025-07-29 | Stack Overflow 2025 | 49,000+ responses, 177 countries | Using or planning to use AI tools in the development process; daily use | 84% (vs 76% in 2024); 51% of professional developers use AI tools daily (47.1% of all respondents, from a low-quality secondary source) | [SO 2025 AI page](https://survey.stackoverflow.co/2025/ai); [SO 2025 press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/) [V2]; 47.1% from [byteiota](https://byteiota.com/stack-overflow-dev-survey-2026-ai-at-84-trust-at-3/) [V2, low quality] |
| Same | Stack Overflow 2025 | Same | AI agents at work | 31% currently use agents; 17% plan to; 38% no plans | [SO 2025 AI page](https://survey.stackoverflow.co/2025/ai) (via secondary summaries) [V2] |
| 2025 → 2025-09-23 | Google DORA "State of AI-assisted Software Development 2025" | "Nearly 5,000 technology professionals" plus >100 hours of qualitative data | "Use AI at work" | 90% (a 14-point rise vs 2024 and a median of ~2 hours/day with AI, both [V3]) | [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) [V1]; [dora.dev](https://dora.dev/dora-report-2025/) [V3] |
| Jan 2026 → Apr 2026 | JetBrains AI Pulse | "More than 10,000 professional developers", localized into 8 languages | "Regularly used at least one AI tool at work for coding and development tasks"; tool used at work | 90%. At work: GitHub Copilot 29%, Cursor 18%, Claude Code 18% | [JetBrains blog](https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/) [V2] |
| May–Jul 2026 → Aug 2026 | JetBrains "AI Coding Agents: Adoption Trends" | Reportedly ~15,000 (per a dev.to write-up) | "Using AI coding agents at work at least weekly / daily" (as summarized); tool used at work | 90% weekly / 68% daily. GitHub Copilot 21% (down from 29%), Cursor 12% (down from 18% in Jan). Copilot awareness 79% | [JetBrains blog](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/) [V2]; sample size from [dev.to](https://dev.to/jamilxt/claude-code-overtakes-github-copilot-what-jetbrains-survey-of-15000-developers-says-about-ai-3nhc) (title only) [V2] |
| Opened 2026-06-23 | Stack Overflow 2026 ("for human developers only") | n/a | n/a | No published results found as of 2026-09-28 | [SO blog](https://stackoverflow.blog/2026/06/23/the-2026-developer-survey-is-now-open-for-human-developers-only/) [V2]; [StackExchange/Survey repo](https://github.com/StackExchange/Survey) [V1]: describes 2026 as still being shaped, and shows no 2026 results |

Supporting details:
- **Mislabeled "2026" pages.** Several pages sell "Stack Overflow Developer Survey 2026" results: 84% adoption, 3% highly trust, 51% daily, "49,000 respondents across 177 countries". These are the 2025 figures relabeled, since the 2026 survey only opened on 2026-06-23. Examples: [byteiota](https://byteiota.com/stack-overflow-dev-survey-2026-ai-at-84-trust-at-3/), [Cadence blog](https://cadence.withremote.ai/blog/stack-overflow-survey-2026) [V2]. The same pages claim developers spend "11.4 hours per week reviewing AI-generated code versus 9.8 hours writing". I could not trace that claim to any Stack Overflow publication, so do not use it.
- **Base of the 2024 figure.** SO 2024: "76% of all respondents are using or planning to use AI tools… up from 70% in 2023", and currently using was "62% vs 44%". One secondary summary attributes the 62% to professional developers, but the SO AI page states it for all respondents. Treat it as all respondents [V2]. ([SO 2024 AI page](https://survey.stackoverflow.co/2024/ai))
- **JetBrains 2025 publication.** The 2025 report was fielded April–June 2025 and unveiled 2025-10-15 ([JetBrains blog](https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/) [V2]). The 2026 Developer Ecosystem survey was open for participation in May 2026 and its report was not yet published ([JetBrains blog, May 2026](https://blog.jetbrains.com/research/2026/05/developer-ecosystem-survey-2026-take-part-in-one-of-the-largest-developer-studies/) [V2]).
- **DORA 2026.** DORA's 2026 output so far is a methodology/ROI report, "ROI of AI-assisted Software Development (2026.01)", covered by InfoQ in May 2026. It frames AI as an "amplifier", a J-curve of value realization and a "verification tax". It is not a new adoption census ([InfoQ](https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/); [dora.dev ROI report](https://dora.dev/ai/roi/report/) [V2]).
- **Enterprise AI-use claims from GitHub (organizational context).** In Jan 2024 Accenture planned to roll out Copilot to 50,000 developers ([MSFT FY24 Q2](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q2) [V1]). Siemens adopted the full GitHub platform "after a successful Copilot rollout to 30,000 of its developers" ([MSFT FY26 Q2](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) [V1]).

### Inferences
- **Breadth is on the flat top of its S-curve.** "Currently using" went 44% (May 2023) → 62% (May 2024) → roughly 85–90% (mid-2025 to Jan 2026, across JetBrains and DORA). A rough logistic reading puts the 50% crossing around H2 2023, about 9–12 months after ChatGPT. It puts 90% at roughly 2025–early 2026. This mixes surveys with different wording and samples, so it is only indicative. The remaining ~10% are mostly policy-constrained environments and refusers.
- **Sanctioned enterprise deployment lagged individual use in 2023–24.** Gartner estimated <14% of enterprise engineers used AI code assistants in early 2024. At the same time, >97% of enterprise developers in GitHub's Feb–Mar 2024 survey had used AI coding tools at work at some point. Much early use was individual or "shadow" use, often via ChatGPT.
- **Wording shift across the series.** SO moved from "using or planning" (2023–25) to daily use (2025). JetBrains moved from "tried / regularly" (2024) to "regularly use at work" and then "agents weekly/daily" (2026). The questions changed because the old ones saturated.
- **Falling SO sample size.** SO respondents fell from ≈90k (2023) to 65k (2024) to 49k (2025). That fits with developers replacing Q&A sites with AI, but it could also be survey fatigue. It is not established.

### Gaps
- **Stack Overflow 2026.** Results were not found. Also missing: the 2025 "currently using" split (the 84% includes planners) and the professional vs all-respondent splits for every year. survey.stackoverflow.co was blocked.
- **JetBrains.** The 2023 AI figures could not be verified. An unverified lead is "77% have used ChatGPT, 46% GitHub Copilot" from the 2023 DevEco report; do not cite it without checking. Also missing: the Claude Code share in the May–Jul 2026 wave. The dev.to title says Claude Code "overtakes GitHub Copilot", which implies more than 21%, but I have no number. The exact question wording of the Aug 2026 post is also unverified: "90% use AI coding agents weekly" may count any agent-mode use.
- **Atlassian State of DevEx, 2024 and 2025.** Not retrieved because the search budget ran out. Unverified leads: 2024 was about 2,100 developers and managers; 2025 was about 3,500 developers and managers in 6 countries, with claims about hours saved per week by AI and hours lost to organizational friction.
- **Analyst and index sources not retrieved.** McKinsey, IDC and Forrester developer-adoption figures, and the Stanford AI Index 2024–2026.
- **DORA 2024 details.** The exact sample size and the published 75.9% decimal (the blog says "75%+").

---

## 2. How did trust and sentiment move alongside adoption?

### Takeaway
On Stack Overflow, usage rose every year while sentiment fell:
- favorability went from 77% (2023) to 72% (2024) to about 60% (2025);
- active distrust of AI accuracy rose from 31% (2024) to 46% (2025);
- only 33% trusted AI accuracy in 2025, and only 3% "highly" trusted it.

DORA's enterprise-leaning sample shows the opposite small move: low or no trust in AI-generated code fell from 39% (2024) to 30% (2025). Perceived productivity gains are widely reported, but independent RCT evidence is mixed. The main friction has shifted to verifying "almost right" output.

### Cited Findings
- **SO favorability.** 77% favorable/very favorable in 2023 and 72% in 2024 ([SO 2024 press release](https://stackoverflow.co/company/press/archive/stack-overflow-2024-developer-survey-gap-between-ai-use-trust/) [V2]). For 2025, SO stated "positive sentiment for AI tools has decreased… from 70%+ in 2023 and 2024 to just 60% this year" ([SO 2025 AI page](https://survey.stackoverflow.co/2025/ai) [V3]).
- **SO trust in 2024.** "Only 43%" trusted the accuracy of AI tools ([SO 2024 press release](https://stackoverflow.co/company/press/archive/stack-overflow-2024-developer-survey-gap-between-ai-use-trust/) [V2]). About 42% trusted in 2023 (3% highly plus ~39% somewhat) ([SO 2023](https://survey.stackoverflow.co/2023/#ai) [V3]).
- **SO trust in 2025.** "More developers actively distrust the accuracy of AI tools (46%) than trust it (33%)", with only 3% highly trusting. The 46% compares with 31% distrust in 2024. ([SO 2025 press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/); [SO 2025 AI page](https://survey.stackoverflow.co/2025/ai) [V2])
- **Conflicting trust figure.** The SO 2025 press materials, as summarized, also say "trust in AI outputs fell to 29% from 40%". This does not match the 33% "trust" figure and may use a different base (for example professional developers only) or combine answers differently. Report both and note the difference. ([SO press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/) [V2])
- **SO 2025 frustrations.**
  - 66% cite "AI solutions that are almost right, but not quite" as their biggest frustration.
  - 45% say "debugging AI-generated code is more time-consuming". Some secondary outlets wrongly attach 45% to "almost right".
  - 75% would still ask another person when they don't trust AI's answers.

  ([SO 2025 AI page](https://survey.stackoverflow.co/2025/ai); [SO press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/) [V2])
- **SO 2025 agents and vibe coding.**
  - Among developers who use AI agents at work, 69% agree agents increased their productivity.
  - Only 17% say agents improved team collaboration.
  - About 72% say "vibe coding" is not part of their professional work, plus 5% who emphatically reject it.

  ([SO 2025 AI page](https://survey.stackoverflow.co/2025/ai) via secondary summaries [V2])
- **DORA 2024** ([Google Cloud blog](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report) [V1]):
  - 39% reported "little to no trust in AI-generated code".
  - More than one-third reported "moderate" to "extreme" productivity increases.
  - DORA modelled the effect of a 25% increase in AI adoption: +7.5% documentation quality, +3.4% code quality, +3.1% code review speed, but an estimated −1.5% delivery throughput and −7.2% delivery stability.
- **DORA 2025.** 30% report "little or no trust" in AI-generated code, "a slightly lower percentage than last year", and more than 80% believe AI increased their productivity ([Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) [V1]).
- **DORA 2026 ROI report.** It introduces a "J-curve" with an initial productivity dip and names the "verification tax", the extra effort needed to check that AI-generated code is reliable, secure and consistent with the architecture ([InfoQ](https://www.infoq.com/news/2026/05/dora-roi-ai-assisted-dev-report/) [V2]).
- **Vendor productivity claims** (vendor-sourced, based on early controlled experiments):
  - Nadella, July 2023: Copilot is "boosting developer productivity by 40% to 50% or more" ([MSFT FY23 Q4](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q4) [V1]).
  - Oct 2023: "increasing developer productivity by up to 55%" ([MSFT FY24 Q1](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q1) [V1]).
  - GitHub's product page today: "up to 55% more productive at writing code" and "up to 75% higher satisfaction" ([github.com/features/copilot](https://github.com/features/copilot) [V1]).
- **Independent RCT (METR, July 2025).** In a randomized trial with 16 experienced open-source developers and 246 tasks, allowing early-2025 AI tools made tasks take 19% longer. The developers still believed AI had sped them up by about 20%. ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) [V3])

### Inferences
- **Why SO trust fell while use rose.** SO's decline is consistent with three things:
  - the user base shifting toward the late majority, including people adopting under employer pressure;
  - AI being used on harder, larger tasks, where "almost right" output is costlier;
  - review and verification becoming the bottleneck, which DORA calls the "verification tax".

  DORA's slight trust improvement likely reflects its enterprise/DevOps-heavy sample and its narrower question (trust in AI-generated code, not AI output in general).
- **Sentiment is not holding adoption back.** Adoption kept rising after trust fell. Adoption appears driven by economics and competition, not by favorability. This is typical of the late-majority phase of a diffusion curve, where use is sustained by organizational norms rather than enthusiasm.

### Gaps
- SO 2025's exact trust wording and base (the 29% vs 33% discrepancy) could not be checked on the blocked SO pages.
- DORA 2025 "reliance" shares and code-quality perceptions were not in the blog. A lead (unverified): 59% reporting better code quality.
- No 2026 trust data from SO. JetBrains 2026 satisfaction/CSAT figures were not retrieved.

---

## 3. Usage-scale milestones for the major tools (Copilot, Cursor, Claude Code, Codex and others), plus aggregate usage signals

### Takeaway
GitHub Copilot grew steadily:
- more than 1M people had used it by Jan 2023;
- 1M paid users by Oct 2023, 1.8M paid by Apr 2024, and 4.7M paid by Jan 2026 (+75% year on year);
- 15M "users" by Apr 2025 and 50M "users" by Jul 2026. These user counts include the free tier launched in Dec 2024.

From 2025 the growth moved to agentic tools, which are growing exponentially:
- **Claude Code** run-rate went from more than $0.5B (Aug/Sep 2025) to $1B (Nov 2025) to more than $2.5B (Feb 2026).
- **Cursor** annualized revenue went from more than $1B (Nov 2025) to $2B (Feb 2026), $3B (Apr 2026) and more than $4B (Jun 2026).
- **Codex** went from under 1M weekly active users (Feb 2026) to 5M (Jun 2026) and 8M (Jul 2026).
- By July 2026, "one in three pull requests on GitHub now involves an agent", and GitHub Copilot had switched to usage-based billing.

In Anthropic's own usage data, coding moved from chat to API/agent traffic.

### Cited Findings

**Table 2: Tool usage and revenue milestones (chronological)**

| Date | Tool / company | Metric (definition) | Value | Source |
|---|---|---|---|---|
| Jun 2021 / Jun 2022 (pre-ChatGPT context) | GitHub Copilot | Technical preview (2021-06-29); GA for individuals (2022-06-21) | n/a | [GitHub blog 2021](https://github.blog/2021-06-29-introducing-github-copilot-ai-pair-programmer/); [GitHub blog 2022](https://github.blog/2022-06-21-github-copilot-is-generally-available-to-all-developers/) [V3] |
| 2023-01-24 (MSFT FY23 Q2) | Copilot / GitHub | Cumulative people who have used Copilot; GitHub developers | "More than one million people have used Copilot to date"; "GitHub is now home to 100 million developers" | [MSFT FY23 Q2](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q2) [V1] |
| 2023-04-25 (FY23 Q3) | Copilot for Business | Organizations signed up, 3 months after broad availability (≈Feb 2023) | "over 10,000 organizations"; 76% of Fortune 500 use GitHub | [MSFT FY23 Q3](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q3) [V1] |
| 2023-07-25 (FY23 Q4) | Copilot for Business | Organizations | "More than 27,000 organizations – up 2X quarter-over-quarter"; "nearly 90% of GitHub Copilot sign-ups are self-service" | [MSFT FY23 Q4](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q4) [V1] |
| 2023-10-24 (FY24 Q1) | Copilot | Paid users; Business orgs | "over 1 million paid Copilot users"; "More than 37,000 organizations… up 40% QoQ"; Copilot Chat capabilities added this quarter | [MSFT FY24 Q1](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q1) [V1] |
| 2024-01-30 (FY24 Q2) | Copilot | Paid subscribers; Business orgs; GitHub revenue growth | "over 1.3 million paid… up 30% QoQ"; "More than 50,000 organizations"; GitHub revenue "over 40%" YoY | [MSFT FY24 Q2](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q2) [V1] |
| 2024-04-25 (FY24 Q3) | Copilot | Paid subscribers | "1.8 million paid subscribers, with growth accelerating to over 35% QoQ"; GitHub revenue +45% YoY; >90% of Fortune 100 are GitHub customers | [MSFT FY24 Q3](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q3) [V1] |
| 2024-07-30 (FY24 Q4) | Copilot / GitHub | Organizations; revenue | "more than 77,000 organizations… up 180% YoY"; Copilot "over 40% of GitHub's revenue growth this year", already larger than all of GitHub at acquisition; GitHub ARR "$2 billion" | [MSFT FY24 Q4](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q4) [V1] |
| 2024-10-30 (FY25 Q1) | Copilot Enterprise | Customers | "increased 55% quarter-over-quarter" | [MSFT FY25 Q1](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q1) [V1] |
| 2025-01-29 (FY25 Q2) | Copilot Free (VS Code, launched Dec 2024) / GitHub | Sign-ups; developers | "more than a million signups in just the first week post-launch"; GitHub "150 million developers, up 50% over the past two years" | [MSFT FY25 Q2](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q2) [V1] |
| 2025-04-30 (FY25 Q3) | Copilot | "Users" (includes free) | "over 15 million GitHub Copilot users, up over 4X YoY"; Code Review Agent "reviewed over 8 million pull requests"; VS + VS Code "over 50 million monthly active users" | [MSFT FY25 Q3](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q3) [V1] |
| 2025-07-30 (FY25 Q4) | Copilot | Users; Enterprise customers; Fortune 100 | "20 million GitHub Copilot users" (reported by press as all-time users [V3]); Enterprise customers +75% QoQ; "90% of the Fortune 100 now use GitHub Copilot" | [MSFT FY25 Q4](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q4) [V1]; [TechCrunch](https://techcrunch.com/2025/07/30/github-copilot-crosses-20-million-all-time-users/) [V3] |
| 2025-09-02 | Claude Code (Anthropic) | Run-rate revenue; usage growth | "over $500 million in run-rate revenue with usage growing more than 10x in just three months". Anthropic overall: ≈$1B run-rate at start of 2025, >$5B by Aug 2025 | [Anthropic Series F](https://www.anthropic.com/news/anthropic-raises-series-f-at-usd183b-post-money-valuation) [V1] |
| 2025-10-29 (FY26 Q1) | Copilot / GitHub | Users; developers | "over 26 million users"; GitHub "over 180 million developers… adding a developer every second"; "80% of new developers on GitHub start with Copilot within their first week"; "over 500 million pull requests merged over the past year"; Agent HQ launched | [MSFT FY26 Q1](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1) [V1] |
| Nov 2025 (announced 2025-12) | Claude Code | Run-rate revenue | "just six months after becoming available to the public [GA May 2025], it reached $1 billion in run-rate revenue" | [Anthropic/Bun](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone) [V1] |
| Nov 2025 | Cursor (Anysphere) | Annualized revenue; funding | ">$1B annualized revenue"; $2.3B Series D at $29.3B post-money | [Cursor blog](https://cursor.com/blog/series-d) [V3] |
| 2026-01-28 (FY26 Q2) | Copilot | Paid subscribers | "over 4.7 million paid Copilot subscribers, up 75% YoY"; "Copilot Pro+ subs for individual devs increased 77% QoQ" | [MSFT FY26 Q2](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) [V1] |
| 2026-02-12 | Claude Code | Run-rate; WAU; commit share; business mix | "over $2.5 billion; this figure has more than doubled since the beginning of 2026"; weekly active users "doubled since January 1"; "4% of all GitHub public commits worldwide… authored by Claude Code—double… one month prior" (third-party estimate); business subscriptions quadrupled since start of 2026; enterprise "over half of all Claude Code revenue". Anthropic overall run-rate $14B | [Anthropic Series G](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) [V1] |
| Feb 2026 | Cursor | Annualized revenue | $2B (reports of a raise at ~$50B valuation) | [Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/); [The Next Web](https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding) [V2] |
| Feb 2026 | OpenAI Codex | Weekly active users at desktop-app launch | "fewer than 1 million" WAU | [OpenAI blog](https://openai.com/index/codex-for-knowledge-work/) and secondary summaries [V2] |
| Mar 2026 | Codex | WAU | ">2 million" | [The New Stack](https://thenewstack.io/gpt-5-6-codex-user-surge/) [V2] |
| Apr 2026 | Anthropic (company) | Run-rate revenue | ≈$30B (Reuters, per search summaries) | [VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth) [V2] |
| Late Apr 2026 (FY26 Q3) | Copilot | Organizations; enterprise subscribers; CLI; pricing | "Nearly 140,000 organizations now use GitHub Copilot, and enterprise subscribers have nearly tripled YoY"; "Copilot CLI, with usage nearly doubling month-over-month"; announced "move to a usage-based pricing model"; "majority of users leverage multiple models"; Copilot usage cited as a gross-margin headwind | [MSFT FY26 Q3](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3) [V1] |
| Late Apr 2026 | Cursor | Annualized revenue | $3B | [Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/) [V2] |
| Early Jun 2026 | Cursor | Annualized revenue; enterprise share | ">$4 billion"; "around 75% from enterprise customers… approximately $2.6B" (internally inconsistent: $2.6B is ≈65% of $4B); acceleration credited partly to the Feb 2026 "Cloud Agents" launch; press forecasts above $6B by end-2026 | [Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/) [V2] |
| Early Jun 2026 | Codex | WAU; user mix | ">5 million weekly active users", "up more than 6x since the launch of the desktop app in February"; knowledge workers ≈20% of users and growing >3x as fast as developers | [OpenAI blog](https://openai.com/index/codex-for-knowledge-work/); [Constellation Research](https://www.constellationr.com/insights/news/openai-touts-broadening-codex-usage-5-million-weekly-active-users) [V2] |
| Jun 2026 | GitHub Copilot | Billing model | Usage-based billing live: "1 AI credit = $0.01"; chat, agents, CLI and Spaces consume credits; completions and next-edit suggestions stay unlimited on paid plans | [github.com/features/copilot](https://github.com/features/copilot) [V1]; [MSFT FY26 Q4](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) [V1] |
| 2026-07-12 to ~07-14 | Codex | WAU after GPT-5.6 (released 2026-07-09) | 6M by Jul 12, 7M ~24h later, 8M "by Sunday" | [The New Stack](https://thenewstack.io/gpt-5-6-codex-user-surge/) [V2] |
| 2026-07-29 (FY26 Q4) | Copilot / GitHub | Users; revenue; agent share of PRs | "GitHub Copilot now has 50 million users"; "Copilot revenue accelerated over 60% quarter-over-quarter" after usage-based billing; "one in three pull requests on GitHub now involves an agent"; GitHub "225 million users", ">90% of the Fortune 500"; "millions of developers have used MAI-Code-1-Flash" | [MSFT FY26 Q4](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) [V1] |
| End Jul 2026 (reported 2026-08-17) | Anthropic (company) | Run-rate revenue | ">$65 billion" (Bloomberg/Reuters). Secondary summaries give ~$47B in late May 2026 | [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-17/anthropic-revenue-run-rate-surpasses-65-billion-ahead-of-ipo) [V2] |
| 2026-08-21 | Codex | "Active users" (window unspecified; may combine Codex and ChatGPT Work) | 20 million (OpenAI's Tibo Sottiaux). Not comparable with the WAU series | [Unite.AI](https://www.unite.ai/openai-says-codex-and-chatgpt-work-hit-10-million-users/); secondary summaries [V2] |

More on the tools:
- **Claude Code after Feb 2026.** Aggregator sites claim "$8B ARR by May 2026" and "54% of the AI coding market". I found no primary or top-tier press source for either. The 54% may be a mis-transfer of Menlo Ventures' model-share figure. Treat both as unverified. ([aibusinessweekly](https://aibusinessweekly.net/p/claude-code-statistics) [V2, low quality])
- **Aggregator figures for Copilot.** One aggregator says the Copilot ARR estimate is "$900M–$1.1B as of Q2 FY2026". That is a third-party estimate; Microsoft does not disclose it. ([GitHub Copilot stats aggregator](https://www.getpanto.ai/blog/github-copilot-statistics) [V2, low quality])
- **OpenAI internal claim.** OpenAI says that since August 2025 "roughly 99% of its own Engineering work" runs through Codex. This is a vendor claim. ([secondary summary of OpenAI blog](https://openai.com/index/codex-for-knowledge-work/) [V2])
- **Coding share of Claude.ai conversations (Anthropic Economic Index; Claude users only, so selection-biased):**

| Report (published) | Data sampled | Claude.ai: "Computer & Mathematical" (coding) share | 1P API coding share | Collaboration/automation notes | Source |
|---|---|---|---|---|---|
| 2025-02-10 | ≈1M Claude.ai Free/Pro conversations (Dec 2024–Jan 2025 [V3]) | 37.2% | n/a | 57% augmentation / 43% automation (directive 27.8%) | [Anthropic](https://www.anthropic.com/news/the-anthropic-economic-index) [V1] |
| Mar 2025 (peak, as restated Jan 2026) | Mar 2025 | 40% (peak) | n/a | n/a | [Anthropic Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) [V1] |
| 2025-04-28 (software development study) | 500,000 coding interactions, Apr 6–13, 2025 | n/a | n/a | Claude Code 79% "automation" vs Claude.ai 49%; feedback-loop pattern 35.8% vs 21.3% | [Anthropic](https://www.anthropic.com/research/impact-software-development) [V1] |
| Sep 2025 | 1M Claude.ai conversations, Aug 4–11, 2025, plus 1M 1P API transcripts, Aug 2025 | 36% (baseline restated at 36%) | "a little less than half", 8+ pp above Claude.ai (≈44%) | Directive share 27% → 39%; "first report where automation usage exceeds augmentation"; creating new code 4.1% → 8.6%; debugging 16.1% → 13.3% | [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) [V1] |
| Jan 2026 | Nov 2025 | 34% | 46% (up from 44% in Aug 2025) | Claude.ai augmented 52% / automated 45%; API directive 64% | [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) [V1] |
| Mar 2026 ("Learning curves") | Feb 2026 | 35% | Since Aug 2025 the category share is "+14% in the API and −18% in Claude.ai" (relative) | "Coding tasks continue to migrate from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic"; Claude Code splits work into many API calls | [Anthropic](https://www.anthropic.com/research/economic-index-march-2026-report) [V1] |
| Jun 2026 ("Cadences") | 2026 | No coding share given; Computer & Math ≈30% of survey respondents | n/a | Claude Code sessions show "0.26 points more autonomy" than chat for the same model; 54% of Claude Code conversations are served by Opus vs 10% of chat/Cowork | [Anthropic](https://www.anthropic.com/research/economic-index-june-2026-report) [V1] |

- **AI share of new code at Google.** In Oct 2024, Google said "more than a quarter of all new code at Google is generated by AI, then reviewed and accepted by engineers" (Sundar Pichai, Q3 2024 call) ([Google blog](https://blog.google/inside-google/message-ceo/alphabet-earnings-q3-2024/) [V3]).

### Inferences
- **Two regimes in the Copilot series.**
  - *2023–mid-2024, seat-led growth.* Organizations went 10k → 27k → 37k → 50k → 77k. Paid users went 1M → 1.8M in about two quarters, with quarter-on-quarter growth of 30–40%.
  - *2025–26, usage-led growth.* User counts that include the free tier went 15M → 50M in 15 months. Paid subscribers grew about 75% a year. Organization count grew more slowly: 77k (Jul 2024) → ~140k (Apr 2026), about 1.8x in 21 months. Monetization then shifted to consumption, with usage-based billing and revenue +60% quarter on quarter.

  Seat penetration is ceasing to be the right measure; spend per developer (tokens/credits) is now the growth axis.
- **Paid-seat penetration.** 4.7M paid Copilot subscribers is about 2.6% of GitHub's ~180M developer accounts (Oct 2025), or about 9% of the 50M VS/VS Code monthly users (Apr 2025). Both are poor denominators, and the ratio is a lower bound on paid AI-coding seats because Cursor, Claude Code and Codex seats sit outside it. The 50M Copilot "users" against 225M GitHub users (Jul 2026) gives about 22% of accounts touching Copilot, including free use.
- **Agentic growth rates.** Using the dates above, the agentic products show exponential growth in 2026:
  - Claude Code about 5x in ~5–6 months (Aug/Sep 2025 → Feb 2026);
  - Cursor about 4x in ~7 months (Nov 2025 → Jun 2026);
  - Codex WAU about 10x in ~5 months (Feb → Jul 2026).

  None shows deceleration yet, so this layer is well before its inflection point.
- **Pull-request share as a penetration metric.** "One in three pull requests on GitHub now involves an agent" (Jul 2026). Anthropic's estimate that Claude Code authored 4% of public commits in Feb 2026, doubling month on month, is the clearest evidence of agent penetration into actual code output rather than just usage.
- **Anthropic's usage data corroborates the chat-to-agent shift.** Claude.ai coding share peaked around 40% (Mar 2025) and drifted to 34–35%, while the API coding share rose (≈44% → 46% and still rising).

### Gaps
- **Windsurf/Codeium, Replit, Lovable and Bolt.** I could not verify any figures (domains blocked, search budget exhausted). Unverified leads, not to be reported as fact:
  - Windsurf: about $82M ARR and 350+ enterprise customers when Cognition acquired it (Jul 2025), after the OpenAI deal collapsed and Google hired its leadership.
  - Replit: ARR from about $10M (end-2024) to about $100M (mid-2025) to about $150M (Sep 2025).
  - Lovable: $100M ARR in about 8 months (Jul 2025), about $200M (late 2025).
  - Bolt.new: about $40M ARR within months of its Oct 2024 launch.
- **Cursor.** Pre-Nov-2025 milestones were not checked. Leads: about $100M ARR around Jan 2025; about $500M around Jun 2025, with a Series C at $9.9B. Also unverified: user and DAU counts, and the "half of the Fortune 500" claim.
- **Claude Code.** No figures after Feb 2026: WAU numbers and run-rate. Primary Anthropic posts listed on the newsroom in Aug–Sep 2026 did not show revenue posts ([Anthropic newsroom](https://www.anthropic.com/news) [V1]).
- **Other aggregate signals.** OpenRouter's programming share of tokens was not retrieved. Lead: the a16z/OpenRouter "100 trillion token" study (Dec 2025) reported programming rising from about 11% of tokens in early 2025 to more than 50% by late 2025. Menlo Ventures figures were also not retrieved. Leads: 2024 report, code copilots top enterprise use case at about 51% adoption; 2025 report, coding the largest departmental AI category (about $4B) with Anthropic holding the leading share of coding workloads.
- **Microsoft 2025 figures.** Microsoft's statement that 20–30% of code in its repos is AI-written (Nadella, Apr 2025) was not retrieved. Nor was Google's 2025 update (a "well over 30%" lead).

---

## 4. Analyst forecasts and their track record

### Takeaway
Gartner's April 2024 forecast was that 75% of enterprise software engineers would use AI code assistants by 2028, up from under 10% in early 2023. It raised this within months to 90% by 2028, from under 14% in early 2024. By 2025, surveys already showed 84–90% of developers using AI (SO, JetBrains, DORA). On the broad definition the 2028 target was hit about three years early, although Gartner's metric, sanctioned enterprise code assistants, is narrower. In May 2026 Gartner reframed the market around agents: the Magic Quadrant became "Enterprise AI Coding Agents", with a forecast that more than 70% of enterprise engineers will rely on coding agents by 2028. Company revenue forecasts have also undershot badly.

### Cited Findings
- **Gartner, 2024-04-11.** "By 2028, 75% of enterprise software engineers will use AI code assistants, up from less than 10% in early 2023" ([Gartner PR](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028) [V2]). The same release cited a Q4 2023 survey of 598 respondents: 63% of organizations piloting, deploying or already deployed ([Gartner PR](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028) [V3]).
- **Gartner's revision.** Later Gartner material, the 2024 Magic Quadrant for AI Code Assistants, stated "By 2028, 90% of enterprise software engineers will use AI code assistants, up from less than 14% in early 2024" ([Gartner via search summary](https://www.gartner.com/en/webinar/674243/1507064) [V2]).
- **Gartner's 2026 reframing.** The Gartner Magic Quadrant for Enterprise AI Coding Agents (report date 2026-05-20) forecasts: "By 2028, more than 70% of enterprise software engineers will rely on AI coding agents for both synchronous and asynchronous development tasks". GitHub, Amazon and Cognition (Windsurf) are among the named Leaders, and GitHub has been a Leader "for the third consecutive year". ([GitHub-hosted Gartner reprint page](https://github.com/resources/whitepapers/gartner-magic-quadrant-and-critical-capabilities-for-ai-code-assistants) [V1])
- **Reality against those forecasts.** DORA found 90% using AI at work (Sep 2025) ([Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) [V1]); SO found 84% using or planning (Jul 2025) ([SO](https://survey.stackoverflow.co/2025/ai) [V2]); JetBrains found 90% of professional developers regularly using AI at work (Jan 2026) ([JetBrains](https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/) [V2]).
- **Company revenue forecasts.** Reuters reported (late 2025) that Anthropic aimed to "nearly triple" annualized revenue in 2026, to about $20–26B ([Reuters via Yahoo](https://finance.yahoo.com/news/exclusive-anthropic-aims-nearly-triple-170234463.html) [V2]; the date is [V3]). Reported actuals were about $30B by Apr 2026 and more than $65B by end-July 2026 ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-17/anthropic-revenue-run-rate-surpasses-65-billion-ahead-of-ipo) [V2]). Coding is the largest single use category in Anthropic's data (see Q3).

### Inferences
- **Gartner's miss was mostly about definitions and timing.** Its baseline measured enterprise-sanctioned code assistants, not any AI use. The rapid upward revision (75% → 90% in roughly four months of 2024) and the 2026 pivot to agents show analysts consistently lagging the diffusion. The forecasting frontier has moved from "will engineers use assistants" to "will they rely on agents for asynchronous work". The 70%-by-2028 agents forecast is likely to be surpassed early too: the GitHub PR share, JetBrains' mid-2026 agent usage and Codex/Claude Code growth all point that way.
- **Company forecasts have undershot as well.** Coding-agent revenue outran company guidance by roughly 2.5x or more within months, which suggests planning models built on seat penetration miss the consumption-driven phase.

### Gaps
- Gartner's exact revision date and the 2025 Magic Quadrant text were not retrieved; gartner.com was blocked.
- IDC, Forrester and McKinsey forecasts and survey numbers on developer AI adoption were not retrieved. Nor was any 2026 Gartner survey of the current share of engineers using AI or agents.

---

## 5. China: developer adoption, domestic tools, and enterprise "AI share of new code" claims

### Takeaway
I could not verify any China-specific figure in this session. The web-search budget ran out before the China queries ran, and every Chinese domain attempted was egress-blocked (caict.ac.cn, ir.baidu.com). What follows is a list of specific leads and sources for a follow-up pass. None of it should be reported as fact without checking.

### Cited Findings
- No verified China-specific findings.
- Indirect context only: JetBrains' 2026 AI Pulse survey was "localized into eight languages" with more than 10,000 professional developers ([JetBrains blog](https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/) [V2]). A China breakdown was not retrieved.
- Global surveys such as Stack Overflow under-represent Chinese developers. SO 2025 drew 49,000+ responses across 177 countries ([SO press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/) [V2]), so global adoption rates should not be read as China rates.

### Inferences
- No evidence-based inference is possible from verified data. Structurally, Chinese adoption measures are dominated by vendor claims from Baidu, Alibaba, Tencent, ByteDance and Ant, on "share of new code AI-generated" and internal engineer coverage. Independent developer-level surveys from CSDN, CAICT and InfoQ are the needed counterweight.

### Gaps
The leads below are unverified recollections that need primary confirmation. They are sorted roughly by my confidence.
- **Baidu Comate / 文心快码.** Robin Li said at Baidu Create in April 2024 that about 27% of Baidu's newly added daily code was generated by Comate (moderate confidence). Later Baidu statements (Baidu World Nov 2024, Create 2025, and earnings calls) reportedly raised this share above 30%, possibly toward 40–50%, but the numbers are unverified. Check the Baidu earnings-call transcripts and Baidu Create keynotes.
- **Tencent CodeBuddy / 腾讯云代码助手.** A 2025 Tencent statement reportedly said more than 90% of Tencent engineers use CodeBuddy and that more than 50% of new code is AI-generated or AI-assisted (low-to-moderate confidence). Check Tencent Cloud press releases.
- **Alibaba 通义灵码 (Tongyi Lingma).** Launched around 2023-10-31 at the Apsara Conference. Cumulative download and lines-of-code claims and an internal "share of code" claim were not verified. Related releases: Qwen3-Coder (Jul 2025) and the Qoder agentic IDE (Aug 2025), both unverified.
- **ByteDance Trae / 豆包 MarsCode.** MarsCode launched in 2024 and Trae in early 2025 (international, then China). MAU claims of more than 1M in mid-2025 and later cumulative-user claims are unverified. Also unverified: the internal share of ByteDance engineers using Trae.
- **Other tools.** Zhipu CodeGeeX: I found no adoption figures (the GitHub README for CodeGeeX4 has none; [GitHub](https://github.com/zai-org/CodeGeeX4) [V1]). Ant Group CodeFuse and iFlytek iFlyCode: not researched.
- **Developer surveys to retrieve.**
  - CSDN 《中国开发者调查报告》, the 2023/2024/2025 editions: share of developers using AI coding tools.
  - 中国信通院 CAICT: AI辅助编程 / 智能化软件工程 (AI4SE) survey reports on enterprise deployment rates.
  - 极客邦 InfoQ 研究中心 reports, such as 《中国软件技术发展洞察和趋势预测报告》.
  - SegmentFault surveys.

---

## 6. Segmentation (experience, company size, region, language/stack) and the modality shift from chat/completion to agents

### Takeaway
Segmentation data is thin but consistent on four points:
- startups adopted agentic coding before enterprises, but enterprise now provides the majority of agent revenue;
- web/UI stacks (JS/TS, HTML/CSS) dominate agentic coding traffic;
- employer permission varied widely by country in 2024;
- usage has clearly moved from chat and completion toward autonomous agents in 2025–26.

The evidence for that last point spans Anthropic's migration of coding from Claude.ai to the API, Claude Code's 79% automation rate, Copilot CLI and coding-agent growth, "one in three PRs involves an agent", and JetBrains' tool-share churn from Copilot and Cursor toward Claude Code and Codex.

### Cited Findings
- **Company size and stage.**
  - In Apr 2025, "startup work" accounted for 32.9% of Claude Code conversations vs 23.8% for enterprise work ([Anthropic](https://www.anthropic.com/research/impact-software-development) [V1]).
  - By Feb 2026, enterprise use was "over half of all Claude Code revenue", and business subscriptions had quadrupled since the start of 2026 ([Anthropic Series G](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation) [V1]).
  - Cursor: about 75% of run-rate from enterprise by Jun 2026, with an internally inconsistent dollar figure ([Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/) [V2]).
  - GitHub Copilot enterprise subscribers "nearly tripled" year on year by Apr 2026 ([MSFT FY26 Q3](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3) [V1]).
- **Region.** In GitHub's 2024 survey of enterprise developers, the share whose employer "actively encourages" or "allows" AI coding tools ranged from 59% (Germany) to 88% (US), with Brazil and India in between. Use at work at some point was above 97% in all four countries. ([GitHub blog](https://github.blog/news-insights/research/survey-ai-wave-grows/); [InfoWorld](https://www.infoworld.com/article/3489925/github-survey-finds-nearly-all-developers-using-ai-coding-tools.html) [V2])
- **Language and stack (Claude.ai + Claude Code, Apr 2025).**
  - Languages: JavaScript/TypeScript 31% of queries, HTML/CSS 28%, Python 14%, SQL 6%.
  - Top use cases: UI/UX component development 12% and web/mobile app development 8%.

  ([Anthropic](https://www.anthropic.com/research/impact-software-development) [V1])
- **Modality: chat vs IDE vs agent.**
  - *Stack Overflow 2025 tool shares.* Among AI-tool/agent users (base as summarized), ChatGPT was used by 82% and GitHub Copilot by 68% ([SO 2025 AI page](https://survey.stackoverflow.co/2025/ai) [V2]). In SO 2025's IDE question, Cursor (~18%) and Claude Code (~10%) appeared for the first time ([byteiota summary, low quality](https://byteiota.com/stack-overflow-dev-survey-2026-ai-at-84-trust-at-3/) [V2]; decimals 17.9%/9.7% [V3]).
  - *Stack Overflow 2025 agents.* 31% currently used AI agents, 17% planned to and 38% had no plans ([SO 2025](https://survey.stackoverflow.co/2025/ai) [V2]).
  - *JetBrains tool shares at work.*
    - Claude Code: 3% (Apr 2025) → 18% (Jan 2026).
    - GitHub Copilot: 29% (Jan 2026) → 21% (May–Jul 2026).
    - Cursor: 18% (Jan 2026) → 12% (May–Jul 2026).
    - Agents: by mid-2026, "90% … at least weekly, 68% daily" (definition unclear).
    - The tools tracked also included Codex, Junie, JetBrains AI Assistant and Google Antigravity.

    ([JetBrains Apr 2026](https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/); [JetBrains Aug 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/) [V2])
  - *Anthropic.*
    - Claude Code conversations were 79% "automation" vs 49% on Claude.ai (Apr 2025) ([Anthropic](https://www.anthropic.com/research/impact-software-development) [V1]).
    - The directive (delegation) share on Claude.ai rose from 27% to 39% (late 2024 → Aug 2025) ([Anthropic Sep 2025](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report) [V1]).
    - API traffic is "automation-dominant", with 64% directive (Nov 2025) ([Anthropic Jan 2026](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report) [V1]).
    - Coding "continue[s] to migrate from augmentative usage in Claude.ai to more automated workflows in our first-party API traffic" (Feb 2026) ([Anthropic Mar 2026](https://www.anthropic.com/research/economic-index-march-2026-report) [V1]).
    - Claude Code runs on the most capable models far more often: 54% on Opus vs 10% of chat/Cowork ([Anthropic Jun 2026](https://www.anthropic.com/research/economic-index-june-2026-report) [V1]).
  - *GitHub and Microsoft.*
    - Code Review Agent had reviewed more than 8M PRs by Apr 2025 ([FY25 Q3](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q3) [V1]).
    - By Jul 2025 it was performing "millions of code reviews each month", and Microsoft said "the surge in vibe coding projects and AI coding agents, whether it is Claude Code, Codex, Cursor, or GitHub Copilot are generating more pull requests and more repos on GitHub" ([FY25 Q4](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q4) [V1]).
    - Agent HQ launched in Oct 2025 as "an organizing layer for all coding agents" from Anthropic, OpenAI, Google, Cognition and xAI ([FY26 Q1](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1) [V1]; [FY26 Q2](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2) [V1]).
    - Copilot CLI usage was "nearly doubling month-over-month" in Apr 2026 ([FY26 Q3](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3) [V1]).
    - By Jul 2026, "one in three pull requests on GitHub now involves an agent" ([FY26 Q4](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4) [V1]).
  - *Beyond developers.* About 20% of Codex users are knowledge workers, growing more than 3x as fast as developers (Jun 2026) ([OpenAI blog](https://openai.com/index/codex-for-knowledge-work/) [V2]).
- **Newcomers.** "80% of new developers on GitHub start with Copilot within their first week" (Oct 2025) ([MSFT FY26 Q1](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1) [V1]). SO 2025 describes vibe coding as a trend among less experienced developers, not professionals ([SO 2025](https://survey.stackoverflow.co/2025/ai) [V2]).

### Inferences
- **Two modality waves.**
  - *Wave 1 (2023–24): chat (ChatGPT) plus inline completion (Copilot).* Near-universal but shallow; the human stays in the loop per suggestion.
  - *Wave 2 (2025–26): delegation to agents.* CLI and IDE agents, cloud/background agents and PR-producing bots.

  Wave 2 shows up as higher automation shares, heavier and more expensive model use (Opus share, usage-based pricing), and output-level penetration (4% of public commits by Claude Code in Feb 2026; a third of PRs involving an agent in Jul 2026).
- **Low switching costs.** Market-share churn is high. JetBrains shows Copilot and Cursor losing ground at work within six months while Claude Code rose from 3% to 18% in nine months. Adoption of the category is sticky, but loyalty to any one tool is not. Capability releases can reorder the market within a quarter.
- **Diffusion order is the classic one.** Startups and early adopters led in 2025, and enterprises caught up via sanctioned procurement in 2026.

### Gaps
- Experience-level splits (SO and JetBrains publish them, for example daily-use rates by years of experience) were not retrieved, and company-size splits from SO and JetBrains were not either.
- Regional splits beyond GitHub 2024 are missing: India, China and the EU in the 2025–26 surveys.
- Language/stack splits from surveys, as opposed to Anthropic's usage data, are missing.
- There is no Claude Code or Codex breakdown by developer segment.

---

## 7. Trend shape: which phase of the S-curve, the inflection points and what triggered them

### Takeaway
There are three nested diffusion curves, not one.
1. **Breadth** (any use): at saturation. It crossed 50% around H2 2023 and has been at about 85–90% since mid-2025.
2. **Intensity** (daily use): in its mid-curve. About 51% of professional developers used AI daily in 2025, rising in 2026.
3. **Delegation and monetization** (agents, consumption revenue): in steep exponential growth with no visible inflection as of Sep 2026.

Each step-up lines up with a capability/product release:
- ChatGPT and GPT-4 (Nov 2022–Mar 2023) brought mass trial.
- Claude 3.5 Sonnet (Jun 2024) set off the AI-native IDE (Cursor) wave.
- Copilot Free (Dec 2024), "vibe coding" (Feb 2025), and Claude Code, Codex and the Copilot coding agent (Feb–May 2025) started the agentic curve.
- The late-2025 frontier agentic models and the early-2026 cloud/desktop agents drove revenue doubling every few months.
- Mid-2026 brought GPT-5.6 and the Copilot switch to usage-based billing.

### Cited Findings

**Table 3: Capability and product releases next to adoption signals**

| Date | Release / event | Source | Adoption signal in the following 1–3 quarters |
|---|---|---|---|
| 2022-11-30 | ChatGPT (GPT-3.5) | [OpenAI](https://openai.com/index/chatgpt/) [V3] | >1M people had used Copilot by Jan 2023 ([MSFT FY23 Q2](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q2) [V1]); SO May 2023: 44% using, 70% using or planning ([SO 2024 PR](https://stackoverflow.co/company/press/archive/stack-overflow-2024-developer-survey-gap-between-ai-use-trust/) [V2]) |
| ≈Feb 2023 | Copilot for Business broadly available | [MSFT FY23 Q3](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q3) [V1] ("three months since") | Orgs: >10k (Apr 2023) → >27k (Jul 2023, 2x QoQ) → >37k (Oct 2023) [V1] |
| 2023-03-14 | GPT-4 | [OpenAI](https://openai.com/index/gpt-4-research/) [V3] | Same period; >1M paid Copilot users by Oct 2023 [V1] |
| Jul–Sep 2023 | Copilot Chat capabilities rolled out | [MSFT FY24 Q1](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q1) [V1] | Paid 1M (Oct 2023) → 1.3M (Jan 2024) → 1.8M (Apr 2024) [V1] |
| 2024-06-20 | Claude 3.5 Sonnet (then the Oct 2024 upgrade and computer use) | [Anthropic](https://www.anthropic.com/news/claude-3-5-sonnet); [Anthropic Oct 2024](https://www.anthropic.com/news/3-5-models-and-computer-use) [V3] | Copilot orgs +180% YoY to 77k (Jul 2024) [V1]; the AI-native IDE (Cursor) takeoff in H2 2024 is a [V3] lead (see Q3 gaps) |
| Dec 2024 | GitHub Copilot Free in VS Code | [MSFT FY25 Q2](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q2) [V1] | >1M sign-ups in week one; 15M Copilot users by Apr 2025, 4x YoY [V1] |
| 2025-02-02 | Karpathy coins "vibe coding" | [X/Karpathy](https://x.com/karpathy/status/1886192184808149383) [V3] | SO 2025: ~72% say vibe coding is not part of professional work [V2] |
| 2025-02-24 | Claude 3.7 Sonnet and Claude Code research preview | [Anthropic](https://www.anthropic.com/news/claude-3-7-sonnet) [V3] | Claude.ai coding share peaked at ~40% in Mar 2025 [V1]; Claude Code 79% automation (Apr 2025) [V1] |
| 2025-04-16 / 2025-05-16 | OpenAI Codex CLI; Codex cloud agent (research preview) | [OpenAI o3/o4-mini + Codex CLI](https://openai.com/index/introducing-o3-and-o4-mini/); [OpenAI Codex](https://openai.com/index/introducing-codex/) [V3] | n/a |
| May 2025 | Claude 4 and Claude Code GA; GitHub Copilot coding agent and agent mode | [Anthropic Claude 4](https://www.anthropic.com/news/claude-4) [V3]; GA month from [Anthropic/Bun](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone) [V1]; Copilot agent form factors in [MSFT FY25 Q4](https://www.microsoft.com/en-us/investor/events/fy-2025/earnings-fy-2025-q4) [V1] | Claude Code >$0.5B run-rate by Aug/Sep 2025, "usage growing more than 10x in just three months" [V1]; Copilot 20M users (Jul 2025) [V1]; automation exceeded augmentation on Claude.ai for the first time (Aug 2025) [V1] |
| 2025-08-07 / 2025-09-15 | GPT-5; GPT-5-Codex | [OpenAI GPT-5](https://openai.com/index/introducing-gpt-5/); [OpenAI Codex upgrades](https://openai.com/index/introducing-upgrades-to-codex/) [V3] | n/a |
| 2025-09-29 | Claude Sonnet 4.5 | [Anthropic](https://www.anthropic.com/news/claude-sonnet-4-5) [V3] | n/a |
| Oct 2025 | GitHub Agent HQ (multi-vendor agents on GitHub) | [MSFT FY26 Q1](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q1) [V1] | 26M Copilot users; 80% of new GitHub devs use Copilot in week one [V1] |
| Nov 2025 | Gemini 3 and Google Antigravity (2025-11-18); Claude Opus 4.5 (2025-11-24) | [Google](https://blog.google/products/gemini/gemini-3/) [V3]; [Anthropic](https://www.anthropic.com/news/claude-opus-4-5) [V3] | Claude Code $1B run-rate in Nov 2025 → >$2.5B by 2026-02-12, "more than doubled since the beginning of 2026" [V1]; Cursor >$1B (Nov 2025) → $2B (Feb 2026) [V3/V2] |
| Feb 2026 | Codex desktop app; Cursor Cloud Agents | [OpenAI blog](https://openai.com/index/codex-for-knowledge-work/); [Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/) [V2] | Codex WAU up >6x to >5M by Jun 2026 [V2]; Cursor $2B → >$4B (Feb → Jun 2026) [V2]; Claude Code authoring 4% of public GitHub commits, doubling in a month [V1] |
| Apr–Jun 2026 | GitHub Copilot moves to usage-based pricing | [MSFT FY26 Q3](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3); [github.com/features/copilot](https://github.com/features/copilot) [V1] | Copilot revenue +60% QoQ; 50M users; one in three PRs involves an agent (Jul 2026) [V1] |
| 2026-07-09 | GPT-5.6 | [The New Stack](https://thenewstack.io/gpt-5-6-codex-user-surge/) [V2] | Codex 5M → 8M WAU within days [V2] |
| 2026-09-01 / 2026-09-22 | Claude Fable 5.1 and Claude Mythos 5.1 ("our most advanced models for coding and knowledge work"); Claude Opus 5.5 | [Anthropic newsroom](https://www.anthropic.com/news) [V1] | Too recent to observe |

### Inferences

**Where we are on each S-curve (as of Sep 2026)**
1. **Breadth: saturated.**
   - The evidence: SO "currently using" 44% (2023) → 62% (2024); DORA 76% (2024) → 90% (2025); JetBrains 85% (2025) → 90% at work (Jan 2026).
   - In Rogers' terms, the early and late majorities have adopted and the remainder is laggards and policy-bound environments.
   - The fastest breadth growth was in the ~18 months after ChatGPT, so the inflection point was around 2023. Breadth has flattened since 2025.
2. **Intensity: mid-curve and still climbing.**
   - Daily use was first measured by SO in 2025 at 51% of professional developers. JetBrains' mid-2026 "68% daily" (agents) suggests a move toward the late majority, but the definitions differ.
   - DORA's median of about 2 hours/day in 2025 [V3] is consistent.
3. **Delegation and monetization: early-majority, exponential phase.**
   - Agent use was 31% in SO's mid-2025 survey. A year later, one in three GitHub PRs involves an agent.
   - Claude Code, Cursor and Codex revenue or WAU doubled every ~2–4 months in H1 2026, and Anthropic's overall run-rate went from $14B (Feb) to more than $65B (Jul 2026).
   - None of these series shows deceleration yet. This curve's inflection point (maximum growth rate) is plausibly still ahead, in 2026–27.

**Inflection points and their triggers**
- **Step 1: mass trial (Nov 2022–mid-2023).** ChatGPT and GPT-4 made conversational coding help universal. Copilot for Business gave enterprises a sanctioned channel: organizations doubled quarter on quarter in mid-2023.
- **Step 2: AI-native editors and multi-file edits (mid-2024).** Triggered by Claude 3.5 Sonnet-class models. Copilot organizations grew 180% year on year, and Cursor started to take share (Cursor metrics before Nov 2025 are unverified).
- **Step 3: free tier plus agents (Dec 2024–May 2025).**
  - Copilot Free expanded the user base: 15M users, 4x year on year.
  - "Vibe coding" (Feb 2025) marked the cultural shift.
  - Claude Code (Feb/May 2025), Codex (Apr/May 2025) and Copilot agent mode/coding agent (2025) moved work from suggestion to delegation.
  - Anthropic's data shows automation overtaking augmentation by Aug 2025.
- **Step 4: frontier agentic models plus background/cloud agents (Nov 2025–Feb 2026).**
  - Opus 4.5, GPT-5.x-Codex and Gemini 3/Antigravity were followed by the Codex app and Cursor Cloud Agents.
  - Result: Claude Code more than doubled in about six weeks, Cursor doubled in about three months, and Codex WAU grew 6x in about four months.
- **Step 5: consumption economics (mid-2026).**
  - GitHub's switch to usage-based billing (Copilot revenue +60% quarter on quarter), plus GPT-5.6's Codex surge, signal that the unit of penetration is now tokens and tasks per developer, not seats.
  - Agent-involved PRs at one-third of the total suggest agents are moving from early majority to majority in actual code production.

**Implications for extrapolation**
- **Seat-based "penetration" is near its ceiling.** Almost every developer uses something.
- **The growth variable is the share of engineering work delegated to agents.** It is measurable as the share of PRs and commits authored by agents, the automation share of interactions, and spend per developer.
- **Plausible logistic parameters for delegation, as of mid-2026:**
  - Current level: roughly 30% of PRs involve agents.
  - Doubling time: a few months in early 2026. Claude Code's commit share doubled in about a month in early 2026, and Codex WAU grew about 10x in five months.
  - If the logistic holds, the 50% point on "PRs involving agents" would plausibly fall in 2026–27.
  - The 90% point would plausibly fall in 2027–28, consistent with Gartner's 70%-by-2028 agents forecast being hit early.
  - These are inference-grade projections, not sourced forecasts.
- **Adoption is decoupled from trust.** Rising use alongside falling SO trust means diffusion is being driven by economics and competition. The binding constraint is shifting to verification and review capacity: DORA's "verification tax", SO's "almost right" frustration, and METR's measured slowdown for experts in early 2025.

### Gaps
- There is no single consistent time series spanning 2022–2026 with identical wording. The S-curve estimates stitch together surveys with different samples and definitions.
- Release dates marked [V3] (most model and product launch dates) were not re-verified in this session. The dates are widely documented, but the exact URLs should be checked.
- Direct measures of the share of all code written by AI, industry-wide, are missing. Only company claims were found (Google >25% in Oct 2024 [V3]) plus Anthropic's commit-share estimate [V1]. Later Google, Microsoft, Meta and Chinese-firm updates were not retrieved.
- Stack Overflow 2026, JetBrains DevEco 2026 and a DORA 2026 State report were not available or not found. These would be the first to confirm or refute the "breadth saturated, intensity rising, delegation exponential" picture.
