# Has AI Coding Produced Incremental Value for the Software Industry? Evidence from Nov 2022 to Sep 2026

**Tag legend.** Each finding starts with a tag of the form `[LEVEL | TYPE | DATE]`.
- **LEVEL** is one of TASK, TEAM, FIRM, INDUSTRY or MACRO.
- **TYPE** is one of:
  - MEASURED: administrative data, telemetry, RCTs or financial statements.
  - SURVEY: self-reported data.
  - CLAIM: statements by a company or executive, or unaudited ARR.
  - FORECAST: a model or projection.
  - MARKET: asset prices.
  - ANALYSIS: a researcher's interpretation.

**Source-access caveat.** The network egress proxy blocked direct fetches from almost every domain, including BLS, NBER, the regional Feds, Fortune, TechCrunch, Stanford, Stripe and METR. The only pages read in full were on anthropic.com. Every other figure below comes from search-engine summaries of the cited pages. Figures that trace only to aggregator sites are marked "(aggregator; unverified)". The report writer should treat single-source numbers as provisional.

---

## 1. Macro and industry statistics: has AI (and AI coding) shown up in US productivity and output data, 2023–2026?

### Takeaway
US labor productivity has run above its 2007–2019 pace, at about 2.1% a year this cycle, 2.2% for 2025 and 2.2% year-on-year to Q2 2026. BLS also measures a jump in productivity for software publishers (+12.9% in 2025). Beyond that, the aggregate picture does not show AI:
- TFP is nearly flat: utilization-adjusted TFP rose about 0.07% in the four quarters to Q1 2026.
- Fed researchers (May–Jul 2026) find no definitive evidence of an AI-driven productivity regime.
- Goldman finds "no meaningful relationship" between AI and productivity economy-wide.
- AI's contribution to GDP so far has come mainly from investment spending, much of it imported, rather than from productive use.

Forward estimates run from under 0.07pp a year of TFP (Acemoglu) to 1.0–1.8pp a year of labor productivity (Anthropic). Software developers are the largest single contributor in Anthropic's estimate.

### Cited Findings

**Measured aggregate data (MACRO)**
- [MACRO | MEASURED | Q2 2026] BLS, nonfarm business labor productivity:
  - Q2 2026: +1.4% annualized, with output +1.7% and hours +0.3%.
  - Q2 2025 to Q2 2026: +2.2%.
  - The current business cycle has averaged 2.1% a year. That is above the 1.5% of 2007Q4–2019Q4 and equal to the 2.1% average since 1947.
  - Real hourly compensation fell 3.3% in Q2 2026.
  - Sources: [BLS Productivity and Costs, Q2 2026 revised](https://www.bls.gov/news.release/prod2.nr0.htm); [BLS TED](https://www.bls.gov/opub/ted/2026/productivity-up-2-2-percent-from-second-quarter-2025-to-second-quarter-2026.htm)
- [MACRO | MEASURED | 2025] BLS, 2025 productivity:
  - Annual-average productivity rose 2.2% from 2024 to 2025.
  - Q4 2025 was first reported at +2.8% (output +2.6%, hours −0.2%) and later revised to +1.8%.
  - Q3 2025 was +5.2%.
  - Sources: [BLS release, Mar 5 2026](https://www.bls.gov/news.release/archives/prod2_03052026.htm); [Trading Economics](https://tradingeconomics.com/united-states/nonfarm-productivity-qoq)
  - Conflict: some secondary reports give 2.1% for 2025 against 3.0% for 2024. Brynjolfsson's pre-release estimate for 2025 was about 2.7% (see below).
- [MACRO | MEASURED + ANALYSIS | May 26 2026] SF Fed Economic Letter 2026-14:
  - It concludes that "current data on productivity do not yet provide definitive evidence that the U.S. economy has entered a period of high productivity growth."
  - Its regime-switching model puts the probability of a high-growth regime at about 57% using labor productivity but only about 21% using TFP, as of Q4 2025.
  - Labor productivity is about 8pp above its 2022 level, while TFP has shown little growth since 2024. The authors note this divergence looked similar in data through 1997, just before the late-1990s boom.
  - Sources: [SF Fed](https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/05/have-we-entered-era-of-high-productivity-growth/); [Edward Conard summary](https://www.edwardconard.com/macro-roundup/us-labor-productivity-is-8pp-above-2022-levels-while-tfp-has-shown-little-growth-since-2024-echoing-1990s-pre-surge-dynamics-a-regime-switching-model-using-labor-productivity-gives-a-57-probabilit/)
- [MACRO | MEASURED | Q1 2026] Utilization-adjusted TFP grew only about 0.07% in the four quarters ending Q1 2026.
  - Commentary reads the gap between labor productivity and TFP as possible AI-related capital deepening rather than a genuine productivity breakthrough.
  - This number appears in search summaries of both the SF Fed and the St. Louis Fed 2026 pieces, so exact attribution is unverified.
  - Sources: [SF Fed](https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/05/have-we-entered-era-of-high-productivity-growth/); [St. Louis Fed Jul 2026](https://www.stlouisfed.org/on-the-economy/2026/jul/ai-productivity-what-firms-say-earnings-calls)
- [MACRO | ANALYSIS | 2026] A CEPR VoxEU column argues that "higher utilisation explains the recent surge in productivity growth". This offers a non-AI explanation. Only the title was retrieved. — [CEPR VoxEU](https://cepr.org/voxeu/columns/higher-utilisation-explains-recent-surge-productivity-growth)
- [MACRO | MEASURED | H1 2025] Investment in information-processing equipment and software accounted for essentially all US GDP growth in H1 2025, per an analysis of BEA data. BEA's Q1 2026 advance estimate says the rise in intellectual-property investment came mainly from software.
  - Sources: [An Economic Sense, Aug 29 2025](https://aneconomicsense.org/2025/08/29/gdp-growth-in-the-first-half-of-2025-all-of-it-is-from-the-ai-investment-boom/); [BEA Q1 2026](https://www.bea.gov/news/2026/gdp-advance-estimate-1st-quarter-2026)
- [MACRO | ANALYSIS | Feb 2026] Goldman Sachs chief economist Jan Hatzius said AI investment added "basically zero" to US GDP growth in 2025.
  - Reason given: much of the equipment is imported. "A lot of the AI investment that we're seeing in the U.S. adds to Taiwanese GDP, and it adds to Korean GDP but not really that much to U.S."
  - Source: [Gizmodo](https://gizmodo.com/ai-added-basically-zero-to-us-economic-growth-last-year-goldman-sachs-says-2000725380)
- [MACRO/FIRM | ANALYSIS | Mar 2026] Goldman Sachs found "no meaningful relationship between AI and productivity at the economy-wide level."
  - Firms that did implement AI reported median productivity gains of about 30% in two areas, customer support and software development.
  - 70% of S&P 500 management teams discussed AI, but only 10% quantified its impact on specific use cases and only 1% quantified its effect on earnings.
  - Sources: [Fortune, Mar 3 2026](https://fortune.com/2026/03/03/goldman-earnings-ai-anxiety-no-meaningful-impact-productivity-economy-30-percent-in-2-areas/); [Dealroom summary](https://app.dealroom.co/news/feed/goldman-sachs-finds-no-economywide-ai-productivity-gains-but-30-boost-in-customer-support-and-software-development)
- [MACRO | MEASURED (text analysis) | Jul 2026] St. Louis Fed analysis of about 490,000 earnings calls:
  - About 95% of AI-related productivity sentences describe expected future gains. That share has held steady since 2023. For non-AI productivity commentary the share is about 75%.
  - AI's share of all productivity commentary rose from near zero before ChatGPT to about 15% by the end of 2025.
  - Growth in capex and R&D has been driven largely by AI-positive firms.
  - Sources: [St. Louis Fed](https://www.stlouisfed.org/on-the-economy/2026/jul/ai-productivity-what-firms-say-earnings-calls); [Fortune, Jul 31 2026](https://fortune.com/2026/07/31/ai-productivity-doesnt-show-up-in-data-earnings-calls-st-louis-fed/)
  - Coverage adds two points. First, when AI makes output radically cheaper, falling prices can cancel out the measured gains. Second, diffusion of past technologies took 20–30 years. — [Allwork.space, Aug 2026](https://allwork.space/2026/08/ai-may-be-erasing-the-value-of-its-own-productivity-gains-fed-research-finds/)

**Measured industry data: software (INDUSTRY)**
- [INDUSTRY | MEASURED | 2024 data, released Jun 26 2025] BLS: software publishers had the highest output growth of the 31 selected service-providing industries, at +16.2%. Their labor productivity rose 9.4% in 2024. — [BLS prin2 2024](https://www.bls.gov/news.release/prin2.nr0.htm)
- [INDUSTRY | MEASURED | 2025 data, released Aug 26 2026] BLS: software publishers' labor productivity rose 12.9% in 2025, the strongest of the selected service industries. The same release gives +4.0% for 2024.
  - Productivity rose in 15 of 30 selected service industries, and unit labor costs rose in 24 of 30.
  - Sources: [ANI News, Aug 27 2026](https://www.aninews.in/news/business/software-and-gambling-leads-us-productivity-gains-but-rising-labor-costs-hit-most-service-industries-bls20260827141446/); [BLS detailed-industry revisions notice, May 2026](https://www.bls.gov/productivity/notices/2026/revisions-to-productivity-and-costs-for-detailed-industries-may-2026.htm)
  - Conflict: the 2024 figure moved from 9.4% in the 2025 release to 4.0% in the 2026 release, probably because of revisions. The output and hours breakdown for 2025 could not be retrieved.
- [INDUSTRY | SURVEY + correlation | Feb 2025 → 2026] St. Louis Fed economists (Bick and co-authors):
  - Generative-AI users saved an average of 5.4% of their work hours, and 20.5% of users saved 4 or more hours a week.
  - Across all workers, that was 1.4% of total hours in the Feb 2025 version, later updated to 1.6%. The update implies roughly a 1.3% cumulative labor-productivity boost since ChatGPT's release.
  - Industries reporting 1pp more time savings saw 2.7pp faster productivity growth relative to their pre-pandemic trend (correlation 0.32). The authors say explicitly that this is not causal.
  - Sources: [St. Louis Fed, Feb 2025](https://www.stlouisfed.org/on-the-economy/2025/feb/impact-generative-ai-work-productivity); [St. Louis Fed Open Vault, Oct 2025](https://www.stlouisfed.org/open-vault/2025/oct/generative-ai-productivity-future-work); [The Hill op-ed, 2026](https://thehill.com/opinion/technology/5763078-ais-productivity-is-finally-hitting-the-real-economy/)

**Researcher claims (MACRO)**
- [MACRO | ANALYSIS | Feb 2026] Erik Brynjolfsson, in an FT op-ed titled "The AI productivity take-off is finally visible":
  - He estimated US productivity growth of about 2.7% in 2025, against a 1.4% average over the previous decade. His basis was job-creation revisions alongside Q4 GDP tracking +3.7%.
  - He argued the economy is moving from the "investment" phase to the "harvest" phase of the J-curve.
  - He also cited "a small cohort of power users" automating end-to-end workstreams.
  - Sources: [Fortune, Feb 15 2026](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/); [Edward Conard summary](https://www.edwardconard.com/macro-roundup/brynjolfsson-argues-that-downward-revisions-to-job-creation-while-real-gdp-growth-remains-steady-suggest-that-ai-may-be-impacting-us-productivity-growth-he-estimates-labor-productivity-grew-2-7-last/?view=detail)
  - Caveat: he co-founded an AI consulting firm. — [The Decoder](https://the-decoder.com/stanfords-brynjolfsson-sees-ai-boosting-us-productivity-but-he-also-co-founded-an-ai-consulting-firm/)
- [MACRO | ANALYSIS | Feb 2026] Counter-view: "AI is everywhere except in the data", in a Feb 2026 Fortune article (only the headline was seen). AEI similarly argued that "an expected AI productivity boom is still waiting for its proof".
  - Sources: [Fortune, Feb 14 2026](https://fortune.com/2026/02/14/ai-effect-macro-economic-data-labor-enhancement-some-sectors-workers-displacement/); [AEI](https://www.aei.org/economics/an-expected-ai-productivity-boom-is-still-waiting-for-its-proof/)

**Forecasts and models (MACRO)**
- [MACRO | FORECAST | May 2024 / Jan 2025] Acemoglu, "The Simple Macroeconomics of AI":
  - TFP gain of no more than 0.66% over 10 years.
  - Below 0.53% once you allow for early evidence coming from easy-to-learn tasks.
  - Sources: [NBER w32487](https://www.nber.org/papers/w32487); [Economic Policy](https://academic.oup.com/economicpolicy/article-abstract/40/121/13/7728473)
- [MACRO | FORECAST | Nov 25 2025] Anthropic, "Estimating AI productivity gains from Claude conversations" (read directly):
  - Method: Claude-estimated task times from 100,000 conversations.
  - Current models could add 1.8% a year to US labor productivity growth over the next decade, about 1.08% a year of TFP. That would "roughly double the run rate in recent years."
  - Software developers are the largest contributor, at 19% of the total effect.
  - Overall, tasks average about 90 minutes unassisted, and Claude saves about 80% of that time. Software tasks reportedly average about 1.4 hours unassisted.
  - Caveats from the authors: the method "can't account for additional time humans spend on tasks outside of their conversations with Claude, including validating the quality or accuracy of Claude's work", and bottleneck tasks may constrain growth.
  - Sources: [Anthropic](https://www.anthropic.com/research/estimating-productivity-gains); [TIME](https://time.com/7336715/ai-economic-growth-anthropic/)
- [MACRO | FORECAST | Jan 15 2026] Anthropic Economic Index, January 2026 (read directly):
  - Adjusting for task success cuts the implied gain from 1.8pp to 1.2pp a year for Claude.ai usage and 1.0pp for API traffic. If tasks are complements, the gain is 0.7–0.9pp.
  - Success on college-level programming tasks is about 66%.
  - Coding is about a third of Claude.ai conversations and nearly half of first-party API traffic.
  - Source: [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- [MACRO | FORECAST | Sep 8 2025] Penn Wharton Budget Model:
  - AI raises productivity and GDP levels by 1.5% by 2035, nearly 3% by 2055 and 3.7% by 2075.
  - The peak contribution to annual growth is 0.2pp, in 2032. The permanent effect is below 0.04pp a year.
  - About 40% of GDP is substantially exposed.
  - Source: [PWBM](https://budgetmodel.wharton.upenn.edu/p/2025-09-08-the-projected-impact-of-generative-ai-on-future-productivity-growth/)
- [MACRO | FORECAST | 2023, reiterated 2025–26] Goldman Sachs' 2023 forecast had AI beginning to have a measurable impact on US GDP and productivity in 2027. — [Gizmodo](https://gizmodo.com/ai-added-basically-zero-to-us-economic-growth-last-year-goldman-sachs-says-2000725380)
- [MACRO | ANALYSIS | Sep 2025] Goldman estimated that AI has added about $160B to "true GDP" since 2022, but that this is not captured in official statistics. — [Fortune, Sep 17 2025](https://fortune.com/2025/09/17/how-much-gdp-artificial-intelligence-goldman-sachs-160-billion/)

### Inferences
- The aggregate productivity pickup, 2.1% a year this cycle against 1.5% before, is real but cannot yet be pinned on AI. The regime model finds high growth in labor productivity but not in TFP, and utilization and capital deepening are competing explanations. The uptick also began before agentic coding went mainstream in 2025–26.
- The +12.9% for software publishers in 2025 is the strongest measured industry signal consistent with AI-coding value. It is still a weak test, for three reasons:
  - BLS measures output as deflated revenue, so a surge in AI-product sales inside the industry raises measured productivity whether or not AI coding made engineers more productive.
  - Hours fell after the 2023–25 tech layoffs.
  - The 2024 figure was revised by more than half, from 9.4% to 4.0%.
- Every forward estimate is built bottom-up from task-level time savings. Anthropic's own adjustments for reliability and complementarity roughly halve its headline number, which is the Amdahl-type mechanism discussed in section 6.

### Gaps
- BLS tables could not be accessed, so the 2025 output and hours figures for software publishers are missing. No 2023–2025 BLS productivity data was found for computer systems design (NAICS 5415) or BEA value added for software.
- No study was found that attributes any quantified share of US productivity growth from 2023 to 2026 specifically to AI coding.
- The Kansas City Fed bulletin "A New U.S. Productivity Chapter? What Industry Data Say About AI" (2026) could not be retrieved.
- It is unclear whether AI labs such as Anthropic and OpenAI are classified as software publishers (NAICS 5132) or elsewhere, which matters for reading the BLS figures.

---

## 2. Firm-level and enterprise ROI: do firms see P&L impact from AI, and from AI coding in particular?

### Takeaway
Enterprise surveys from 2025–2026 agree: adoption is high, but little of it has reached the P&L.
- PwC (Jan 2026): 56% of 4,454 CEOs saw neither higher revenue nor lower costs.
- NBER (Feb 2026): about 89–90% of about 6,000 executives saw no productivity or employment effect over three years.
- McKinsey (Nov 2025): only 39% report any EBIT impact, mostly under 5% of EBIT.
- BCG (Sep 2025): only 5% of firms are generating value "at scale".
- Danish administrative data (2025) show precise-zero effects on earnings and hours.

Coding-specific evidence is better but still modest. Bain (Sep 2025) finds 10–15% team productivity gains that "rarely translate into business value", Goldman finds about 30% median gains among firms that implemented, and Gartner's engineering leaders self-report about 19%. AI-native startups show extraordinary revenue per employee, but their gross margins are thin or negative.

### Cited Findings

**Enterprise surveys (FIRM, not coding-specific)**
- [FIRM | SURVEY + case review | Jul/Aug 2025] MIT NANDA, "The GenAI Divide: State of AI in Business 2025":
  - 95% of organizations see zero measurable return, despite $30–40B of enterprise investment. Only about 5% of integrated pilots extract millions in value.
  - Method: more than 300 public AI initiatives, 52 interviews and 153 survey responses, collected Jan–Jun 2025. This is a small, non-random sample.
  - Sources: [Virtualization Review, Aug 19 2025](https://virtualizationreview.com/articles/2025/08/19/mit-report-finds-most-ai-business-investments-fail-reveals-genai-divide.aspx); [report PDF](https://cloudelligent.com/wp-content/uploads/2026/02/v0.1_State_of_AI_in_Business_2025_Report.pdf); [Forbes, Aug 26 2025](https://www.forbes.com/sites/jasonsnyder/2025/08/26/mit-finds-95-of-genai-pilots-fail-because-companies-avoid-friction/)
- [FIRM | SURVEY | Nov 2025] McKinsey, State of AI 2025:
  - 88% of organizations use AI.
  - 39% report any enterprise-level EBIT impact, and most of those attribute less than 5% of EBIT to AI.
  - About 6% are "high performers", meaning 5% or more of EBIT from AI plus "significant" value.
  - 80% set efficiency as an objective. High performers also target growth and innovation and redesign workflows.
  - Sources: [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai); [summary](https://winsomemarketing.com/ai-in-marketing/mckinseys-state-of-ai-report-88-adoption-but-only-6-are-actually-winning)
- [FIRM | SURVEY | Sep 30 2025] BCG, "The Widening AI Value Gap":
  - 60% of firms report little or no value, and 35% are scaling without significant value.
  - 5% are "future-built". Compared with laggards they show 1.7x revenue growth, 3.6x three-year TSR and 1.6x EBIT margin.
  - Agents account for 17% of AI value in 2025, expected to reach 29% by 2028.
  - Sources: [BCG press](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings); [BCG report](https://media-publications.bcg.com/The-Widening-AI-Value-Gap-Sept-2025.pdf)
- [FIRM | SURVEY | Jan 2026] PwC 29th Global CEO Survey (4,454 CEOs in 95 countries):
  - 56% saw neither higher revenue nor lower costs from AI in the past 12 months.
  - 30% saw higher revenue and 26% saw lower costs. Only 12% saw both.
  - Sources: [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-global-ceo-survey.html); [Search Engine Journal](https://www.searchenginejournal.com/56-of-ceos-report-no-revenue-gains-from-ai-pwc-survey/565643/)
- [FIRM | SURVEY | Nov 2025–Jan 2026, published Feb 2026] Yotzov, Barrero, Bloom, Bunn, Davis et al., "Firm Data on AI" (NBER w34836):
  - About 6,000 executives in the US, UK, Germany and Australia. 69% of firms actively use AI.
  - More than 90% report no AI impact on employment over the past three years, and 89% report no change in productivity.
  - They expect about +1.4% productivity over the next three years and employment reductions of about 1.75M jobs across the four countries by 2028.
  - Sources: [NBER](https://www.nber.org/papers/w34836); [NBER Digest, May 2026](https://www.nber.org/digest/202605/global-evidence-business-use-ai); [The Register, Feb 18 2026](https://www.theregister.com/2026/02/18/ai_productivity_survey/)
- [FIRM | SURVEY | Mar 2026] Baslandze, Graham, Meyer, Waddell et al. (NBER w34984 / Atlanta Fed), about 750 corporate executives:
  - Labor productivity gains are positive and expected to strengthen in 2026. The largest gains are in high-skill services and finance.
  - Gains reflect revenue-based TFP ("innovation- and demand-oriented channels") rather than capital deepening.
  - There is a "productivity paradox": perceived gains exceed measured gains, "likely reflecting a delay in revenue realizations."
  - There is little evidence of near-term aggregate job losses, but jobs are shifting toward skilled technical roles.
  - Sources: [NBER](https://www.nber.org/papers/w34984); [Atlanta Fed](https://www.atlantafed.org/research-and-data/publications/working-papers/2026/03/25/04-artificial-intelligence-productivity-and-the-workforce-evidence-from-corporate-executives); [SF Fed summary](https://www.frbsf.org/research-and-insights/publications/system-research-atlanta-fed/2026/04/artificial-intelligence-productivity-workforce-evidence-from-corporate-executives/)
  - Press framing: "90% of executives say AI hasn't boosted productivity. Some are still cutting jobs." — [Fortune, Aug 22 2026](https://fortune.com/2026/08/22/executives-ai-productivity-layoffs-study/)
- [FIRM/TEAM | MEASURED (admin data) | 2023–2024 data, published Apr/May 2025] Humlum & Vestergaard, "Large Language Models, Small Labor Market Effects" (NBER w33777):
  - Denmark: 25,000 workers at 7,000 workplaces in 11 AI-exposed occupations, with surveys linked to administrative records.
  - Precise null effects on earnings and recorded hours at both worker and workplace level. Effects larger than 2% two years after ChatGPT are ruled out.
  - Average time saved is about 3%.
  - Sources: [BFI](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/); [NBER PDF](https://www.nber.org/system/files/working_papers/w33777/revisions/w33777.rev0.pdf)

**Coding-specific firm evidence (FIRM/TEAM)**
- [FIRM/TEAM | SURVEY | Sep 23 2025] Bain Technology Report 2025:
  - Two-thirds of software firms have rolled out generative-AI developer tools, but teams see only 10–15% productivity boosts, and "the time saved rarely translates into business value."
  - Coding is only 25–35% of the time from idea to launch.
  - Firms that pair AI with end-to-end process change report 25–30% gains.
  - Sources: [Bain](https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/); [The Register](https://www.theregister.com/2025/09/23/developers_genai_little_productivity_gains/)
- [FIRM | SURVEY + FORECAST | 2024–2026] Gartner:
  - 90% of engineering leaders report improvements, with a net average productivity gain of 19.3% (self-reported; date not precisely identified).
  - Forecast: teams that apply AI across the whole SDLC will reach 25–30% gains by 2028, against about 10% from code-generation-focused approaches in 2024.
  - Forecast: 90% of enterprise software engineers will use AI code assistants by 2028, up from under 14% in early 2024. Gartner's Apr 2024 forecast had said 75%.
  - Sources: [Gartner](https://www.gartner.com/en/articles/ai-in-software-engineering); [Gartner, Apr 11 2024](https://www.gartner.com/en/newsroom/press-releases/2024-04-11-gartner-says-75-percent-of-enterprise-software-engineers-will-use-ai-code-assistants-by-2028)
- [FIRM | ANALYSIS | Mar 2026] Goldman Sachs: median gains of about 30% in software development among firms that implemented AI. Only 1% of S&P 500 firms quantify the earnings impact (see section 1). — [Fortune](https://fortune.com/2026/03/03/goldman-earnings-ai-anxiety-no-meaningful-impact-productivity-economy-30-percent-in-2-areas/)

**AI-native firms and revenue per employee (FIRM)**
- [FIRM | CLAIM | Feb–Mar 2026] Lovable:
  - ARR rose from $400M (Feb 2026) to more than $500M with 146 employees (Mar 2026), about $2.77M of ARR per employee. Typical SaaS firms run $200–400k per employee.
  - It says it added $100M in revenue in a single month. The figures are self-reported run-rates, not filings.
  - Sources: [TechCrunch, Mar 11 2026](https://techcrunch.com/2026/03/11/lovable-says-it-added-100m-in-revenue-last-month-alone-with-just-146-employees/); [TNW](https://thenextweb.com/news/lovable-build-economy-500m-arr-vibe-coding)
- [FIRM | CLAIM | 2026] Cursor (Anysphere):
  - ARR went from $2B (Feb 2026) to $3B (late Apr 2026) to more than $4B (early Jun 2026). About 75% of it, roughly $2.6B, is enterprise.
  - Sources: [Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/); [TNW](https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding)
- [FIRM | MEASURED (company-reported) | 2025] Klarna reports revenue per employee of about $1.1M, against $575k a year earlier (details in section 5). — [Entrepreneur](https://www.entrepreneur.com/business-news/heres-how-klarna-has-cut-staff-in-half-while-raising-pay-by-60)
- [FIRM | MEASURED (reported financials) | 2025] Counterweight: AI-coding startups' gross margins are thin or negative.
  - Replit's gross margin ranged from 36% to −14% during 2025.
  - Lovable's was about 35% in May 2025, and StackBlitz's about 40%.
  - Cursor and Windsurf reportedly had negative gross margins.
  - Anysphere changed its pricing to pass Anthropic's model costs on to its heaviest users.
  - Sources: [TechCrunch, Aug 7 2025](https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/); [The Information via X](https://x.com/theinformation/status/1954939636096041346)

### Inferences
- The "no P&L impact" surveys cover generative AI broadly and are not specific to coding. Coding is the use case where gains are most often quantified (Goldman's roughly 30%, Bain's 10–15%). The fairest reading is real team-level gains in coding that the median firm has not yet turned into revenue or profit, which fits the "delay in revenue realizations" finding.
- For AI-native firms, revenue per employee overstates value added per employee. Their main input, model inference, is bought from AI labs, and gross margins of about 35% or below mean most of the revenue passes through to Anthropic, OpenAI and similar labs. So "$2.77M ARR per employee" is partly a sign of *where value is captured*, not only of how much is created.
- The 5–6% "high performers" (McKinsey, BCG) plus Bain's finding that end-to-end process redesign roughly doubles gains are consistent with an organizational J-curve (section 6).

### Gaps
- Revenue per employee for Midjourney and Gamma, requested in the brief, was not retrieved.
- The Builder.ai collapse and the Windsurf deal were not verified in this session.
- No systematic 2022–2026 panel of revenue or value added per employee across software firms was found.
- Methodological critiques of MIT NANDA (sample size, how "return" was defined) were not retrieved.
- Gartner's 19.3% figure lacks a precise date and method.

---

## 3. Software industry output and structure: is more software being shipped, and does it turn into revenue?

### Takeaway
Output volume clearly surged:
- GitHub commits rose 25% and merged PRs 23% in 2025.
- New app releases rose 60% year-on-year in Q1 2026 and 104% in April 2026.
- 2025 was the App Store's biggest release year in nearly a decade.

Monetization lagged well behind:
- Global consumer app spending grew about 10.6% in 2025, and non-game growth was driven largely by the generative-AI apps themselves.
- The median public SaaS company slowed to low double-digit growth, and CRM and collaboration apps fell to single digits.
- Indian IT services shrank in constant currency, with explicit "AI deflation" of 2–5% a year on pricing.
- Markets priced in commoditization during the Feb 2026 "SaaSpocalypse", when IGV fell about 40% from its Sep 2025 peak, before a partial rebound by June 2026.

### Cited Findings

**Volume of software produced (INDUSTRY)**
- [INDUSTRY | MEASURED | Oct/Nov 2025] GitHub Octoverse 2025:
  - Nearly 1 billion commits pushed in 2025 (+25.1% YoY), 43.2M merged PRs a month on average (+23% YoY), and more than 230 new repositories a minute.
  - More than 36M new developers, taking the total above 180M.
  - 1.1M public repositories use an LLM SDK, 693,867 of them created in the past 12 months (+178% YoY).
  - 80% of new developers use Copilot in their first week.
  - Sources: [GitHub blog](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/); [Forbes, Nov 1 2025](https://www.forbes.com/sites/janakirammsv/2025/11/01/10-key-takeaways-from-github-octoverse-2025-report/)
- [INDUSTRY | MEASURED | Dec 2025] Appfigures: "The App Store Just Logged Its Biggest Release Year in Nearly a Decade" (2025). — [Appfigures, Dec 5 2025](https://appfigures.com/resources/insights/20251205?f=2)
- [INDUSTRY | MEASURED | Q1–Apr 2026] Appfigures data reported by TechCrunch:
  - Worldwide app releases in Q1 2026 were up 60% YoY across the App Store and Google Play, and up 80% on iOS alone. In April 2026 they were up 104% across both stores and 89% on iOS.
  - Productivity apps entered the top five categories and utilities rose to number two. Games are still the largest category.
  - Attributing the surge to AI tools such as Claude Code and Replit is described as a "working hypothesis".
  - Sources: [TechCrunch, Apr 18 2026](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/); [Digital Trends](https://www.digitaltrends.com/phones/ai-boom-fuels-surge-in-new-app-launches-across-app-store-and-google-play/)
- [INDUSTRY | MEASURED | Feb 2026] Stripe reportedly observed "60% more apps YoY" (headline only; details not retrieved). — [SaaStr summary of Stripe data](https://www.saastr.com/stripes-latest-data-startups-are-growing-50-faster-computer-demand-drove-50-of-gdp-growth-60-more-apps-yoy-and-more/)

**Does the volume translate into revenue? (INDUSTRY)**
- [INDUSTRY | MEASURED | 2025, published Jan/Feb 2026] Sensor Tower, State of Mobile 2026:
  - Revenue from in-app purchases and paid apps and games reached $167B in 2025, up 10.6%.
  - Non-game apps took about $85B, up 21%. That was the first year non-game apps out-earned games, "boosted by Gen-AI services".
  - Downloads of AI apps rose 148%.
  - Sources: [Sensor Tower press release](https://sensortower.com/press/press-release-boosted-by-gen-ai-services-consumers-spent-more-money-in-apps-than-games-for-first-time); [Sensor Tower blog](https://sensortower.com/blog/state-of-mobile-2026)
- [INDUSTRY | MEASURED (market data) | Q2 2026] Public SaaS growth:
  - PitchBook's Q2 2026 comp sheet puts estimated median 2026 revenue growth at 13.2%, up from 12.2% in its Q1 estimate. Its title reads "SaaS profits strengthen as AI disrupts valuations."
  - Other benchmark summaries show median growth falling from 14.0% in Q4 2025 to 11.8% in Q2 2026, with consensus below 10% for 2027.
  - CRM, sales, marketing and CX, and collaboration, productivity and creative tools are in single-digit growth. DevOps, ITOps and developer/automation platforms lead at 21.9%.
  - The figures come from sources merged in search summaries and are partly inconsistent.
  - Source: [PitchBook](https://pitchbook.com/news/reports/q2-2026-q2-2026-enterprise-saas-public-comp-sheet-saas-profits-strengthen-as-ai-disrupts-valuations)

**Market pricing of commoditization risk (INDUSTRY)**
- [INDUSTRY | MARKET | Feb 3–5 2026] The "SaaSpocalypse":
  - The selloff followed weak earnings, better AI models and Anthropic's Claude Cowork plugin release. Claude Opus 4.6 launched Feb 5 2026. The exact sequencing of triggers varies by source.
  - About $285–300B was wiped off global software stocks in about 48 hours. The term is attributed to Jefferies trader Jeffrey Favuzza, who described "get me out" style selling.
  - An aggregator reports 12-month drawdowns of Figma −76%, monday.com −72%, Atlassian −65%, HubSpot −57% and Salesforce −29%, and about $2T of software market cap lost over twelve months (aggregator; unverified).
  - Sources: [Bloomberg, Feb 4 2026](https://www.bloomberg.com/news/articles/2026-02-04/what-s-behind-the-saaspocalypse-plunge-in-software-stocks); [Forbes, Feb 4 2026](https://www.forbes.com/sites/donmuir/2026/02/04/300-billion-evaporated-the-saaspocalypse-has-begun/); [NxCode](https://www.nxcode.io/resources/news/saaspocalypse-2026-software-stock-crash)
- [INDUSTRY | MARKET | Jun 2 2026] Software stocks fell almost 40% from their highs, then IGV rallied about 44% off its April 2026 low. By early June it was less than 9% below its Sep 2025 all-time high and positive year-to-date. — [CNBC](https://www.cnbc.com/2026/06/02/software-stocks-just-passed-a-big-milestone.html)

**IT services and price deflation (INDUSTRY/FIRM)**
- [FIRM | MEASURED (financials) | FY26, year to Mar 2026] TCS:
  - Revenue fell 0.5% to $30.0B, its first full-year decline in USD, and about 2.4–2.5% in constant currency.
  - Net headcount fell by 23,460 to 584,519, including more than 12,000 layoffs in July 2025.
  - Its fresher intake target fell from about 40,000 to 25,000.
  - Annualized AI services revenue reached $1.8B in Q3 FY26, up 17.3% quarter-on-quarter in constant currency.
  - Sources: [Whalesbook](https://www.whalesbook.com/news/English/tech/TCS-Reports-First-Full-Year-USD-Revenue-Fall/69d79611e1f61dfbf512a227); [Sahi](https://www.sahi.com/blogs/tcs-q4-fy26-results-analysis); [Business Standard, Apr 23 2026](https://www.business-standard.com/companies/news/top-5-it-cos-net-hiring-down-for-fy26-uncertainties-to-continue-126042301290_1.html); [Multibagg, Q3 FY26](https://www.multibagg.ai/market-pulse/articles/tcs-q3-fy26-results-ai-revenue-cmnrfz0z8w7p4ma0j9f3rbuwp)
- [INDUSTRY | MEASURED | FY26] Net headcount at India's top five IT firms fell by 6,981 in FY26, against a gain of 12,718 the year before. — [Business Standard](https://www.business-standard.com/companies/news/top-5-it-cos-net-hiring-down-for-fy26-uncertainties-to-continue-126042301290_1.html)
- [INDUSTRY | CLAIM + analyst estimate | Apr 2026] "AI deflation" in Indian IT services:
  - HCLTech's CEO says teams need 25–30% more effort to earn the same revenue, that "a $100 million deal would be worth maybe $80 million today", and that deflation will weigh 3–5% on FY27.
  - TCS passes 10–15% of productivity savings to the client at signing and usually recovers it through extra scope.
  - Infosys tracks AI-led deflation internally but does not publish the figure.
  - Infosys and HCLTech have walked away from deals where AI-linked pricing had become too aggressive.
  - Analysts model 2–3% annual deflation across the application-services base.
  - Sources: [The Register, Apr 28 2026](https://www.theregister.com/software/2026/04/28/ai-deflation-comes-to-indias-tech-services-giants/5225686); [Forbes India](https://www.forbesindia.com/article/news/deep-dive/indian-it-braces-for-ai-deflation-as-pricing-pressure-reshapes-growth/2993823/1)
- [FIRM | MEASURED (guidance) | Apr 23 / Jul 23 2026] Infosys guided to FY27 constant-currency revenue growth of 1.5–3.5%, then trimmed it to 1.5–3.0%. It cites "productivity-based pricing" demanded by clients. — [Forbes India](https://www.forbesindia.com/article/news/deep-dive/indian-it-braces-for-ai-deflation-as-pricing-pressure-reshapes-growth/2993823/1); [Infosys 6-K](https://www.sec.gov/Archives/edgar/data/0001067491/000106749126000018/exv99w01.htm)
- [FIRM | MEASURED (financials) | Jun 18 2026] Accenture:
  - Q3 FY26 revenue was $18.7B, up 6% in USD and 3% in local currency. Full-year FY26 guidance is 3–4% in local currency.
  - Headcount is about 799,000.
  - It has booked 104 client deals of $100M or more year-to-date, up 13%.
  - Source: [Accenture Q3 FY26 via BusinessWire](https://www.businesswire.com/news/home/20260618029271/en/Accenture-Reports-Third-Quarter-Fiscal-2026-Results)
- [INDUSTRY | MEASURED (DiD) | 2022–23 data, published 2025] Demirci, Hannane & Zhu (Management Science): within eight months of ChatGPT, Upwork job posts for automation-prone writing and coding work fell 21% relative to manual-intensive jobs. The jobs that remained were more complex and paid more. — [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420)

### Inferences
- **Volume up, value flat or down per unit.**
  - New app releases roughly doubled year-on-year in April 2026, while consumer app spending grew about 11% in 2025, and the fastest-growing spending is on AI apps themselves. Revenue per new app is therefore very likely falling.
  - The extra supply looks mostly like long-tail, low-monetization software. It may still create consumer or creator surplus, but that does not show up as industry revenue.
- **IT services is the clearest measured case of pass-through.** AI productivity gains in outsourced development are being handed to customers through productivity-linked pricing, at 2–5% a year. For IT-services firms the result is flat or negative revenue and shrinking headcount, while buyers get cheaper software work. This is incremental value, but it goes to buyers, not to the industry.
- **Where AI helps, growth has moved to AI-exposed infrastructure.** DevOps and developer platforms grew about 22% while seat-based application SaaS slowed. Markets first priced commoditization of SaaS (Feb–Apr 2026) and then partly reversed (June 2026). That reversal suggests the commoditization thesis is not yet visible in incumbents' reported revenues.

### Gaps
- No data was found on revenue, retention or quality of the AI-era app cohort, for example what share of 2026's new apps earn anything.
- Google Play-only counts, and whether app-review backlogs or spam bias release counts, were not examined.
- Results and pricing commentary for EPAM and Cognizant were not retrieved.
- A clean measure of price deflation for software-development services was not found. FRED PPI series for software publishers turned up, but the search snippets gave inconsistent index values, so they are not used.

---

## 4. Value capture: who gets the value — AI labs and tool vendors, software firms, or customers and consumers?

### Takeaway
The large new revenue pools created by AI coding sit with model labs and coding-tool vendors:
- Anthropic's run-rate went from about $1B (early 2025) to $14B (Feb 2026) to more than $30B (Apr 2026).
- Claude Code alone passed $2.5B of run-rate by Feb 2026.
- Cursor passed $4B ARR (Jun 2026) and was sold to SpaceX for $60B.
- GitHub Copilot had about 4.7M paid subscribers in Jan 2026.

Vendor revenue is not the same as vendor profit. Coding tools run thin or negative gross margins, so part of the value is subsidized through to users. Downstream, buyers of IT services capture gains through price deflation, and consumers capture large unpriced surplus. Incumbent software firms capture value mainly through cost, meaning flat headcount and rising margins, rather than growth in revenue.

### Cited Findings

**AI labs and coding-tool vendors (FIRM/INDUSTRY)**
- [FIRM | CLAIM (run-rate) | Feb–Apr 2026] Anthropic's annualized revenue went from about $1B at the start of 2025 to $14B by Feb 2026, and passed $30B by April 2026 (Reuters, as reported by VentureBeat).
  - Sources: [SaaStr](https://saastr.com/anthropic-just-hit-14-billion-in-arr-up-from-1-billion-just-14-months-ago); [VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth)
  - Later aggregator claims of $47B in May 2026 are unverified. — [aggregator](https://aibusinessweekly.net/p/claude-ai-statistics)
- [FIRM | CLAIM | 2025–Feb 2026] Claude Code reportedly reached a $1B run-rate within about six months of launch and more than $2.5B by Feb 2026.
  - An aggregator claim of $8B by May 2026 and a "54% market share" is unverified.
  - Source: [Panto aggregator](https://www.getpanto.ai/blog/claude-ai-statistics)
- [FIRM | CLAIM + deal terms | Nov 2025–Aug 2026] Cursor:
  - It was valued at $29.3B post-money after raising $2.3B in Nov 2025.
  - On Jun 16 2026, SpaceX agreed to acquire it for $60B in stock. SpaceX had disclosed in April that it held the right to buy Cursor for $60B, or alternatively pay $10B for the companies' joint work.
  - Closing on Aug 14 2026 is reported by aggregators only.
  - Sources: [CNBC, Jun 16 2026](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html); [TechCrunch, Jun 16 2026](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/)
- [FIRM | CLAIM (earnings call) | Jan 28 2026 / Jul 2026] Microsoft:
  - About 4.7M paid GitHub Copilot subscribers, up about 75% YoY (FY26 Q2 call).
  - Microsoft 365 Copilot went from 15M paid seats (Jan 2026) to more than 30M (FY26 Q4 call).
  - Sources: [Office365ITPros](https://office365itpros.com/2026/01/30/microsoft-fy26-q2-results/); [Panto aggregator](https://www.getpanto.ai/blog/github-copilot-statistics); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/microsofts-copilot-just-crossed-30-183023723.html)
- [FIRM | MEASURED | 2025] Vendor margins are thin or negative: Replit swung from +36% to −14% and Lovable ran about 35% (details in section 2). — [TechCrunch, Aug 7 2025](https://techcrunch.com/2025/08/07/the-high-costs-and-thin-margins-threatening-ai-coding-startups/)
- [INDUSTRY | MEASURED | 2025] Consumer spending on non-game apps grew 21%, "boosted by Gen-AI services". The growth in consumer spending is accruing heavily to AI-app vendors. — [Sensor Tower](https://sensortower.com/press/press-release-boosted-by-gen-ai-services-consumers-spent-more-money-in-apps-than-games-for-first-time)

**Customers and consumers (MACRO/INDUSTRY)**
- [MACRO | SURVEY-based valuation | Aug 2025; Apr 2026] Brynjolfsson, Collis, Eggers et al.:
  - Americans got about $97B of consumer surplus from generative-AI tools in 2024.
  - An updated study, "What is Generative AI Worth?", finds aggregate surplus rising from $116B to $172B between 2025 and 2026.
  - This covers all generative AI, not only coding.
  - Sources: [Marginal Revolution, Aug 2025](https://marginalrevolution.com/marginalrevolution/2025/08/the-consumer-surplus-from-ai.html); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6569938); [Stanford DEL](https://digitaleconomy.stanford.edu/publication/what-is-generative-ai-worth/)
- [INDUSTRY | CLAIM | Apr 2026] IT-services buyers capture productivity through pricing, with 2–5% deflation and 10–15% of savings passed on at signing (section 3). — [The Register](https://www.theregister.com/software/2026/04/28/ai-deflation-comes-to-indias-tech-services-giants/5225686)

**Does AI-tool spending substitute for labor or add to it? (FIRM/INDUSTRY)**
- [TASK | MEASURED (usage classification) | Apr 28 2025] Anthropic: 79% of Claude Code conversations were classified as "automation", against 49% on Claude.ai. — [Anthropic](https://www.anthropic.com/research/impact-software-development)
- [TASK | MEASURED (usage classification) | Jan 15 2026] Anthropic: API coding work is 64% automation. — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)
- [INDUSTRY | MEASURED (payroll data) | Aug 2025; update Aug 2026] Brynjolfsson, Chandar & Chen, "Canaries in the Coal Mine":
  - Employment of software developers aged 22–25 fell nearly 20% from its late-2022 peak to July 2025.
  - Early-career workers in AI-exposed occupations saw a 16% relative decline after controlling for firm shocks. Experienced workers were stable.
  - The August 2026 update is headlined "No Widespread Displacement, but the AI Employment Gap for Young Workers Has Widened to 19%".
  - Sources: [Stanford DEL paper page](https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine-six-facts-about-the-recent-employment-effects-of-artificial-intelligence/); [Aug 2026 update](https://digitaleconomy.stanford.edu/news/canariesaug26/)
- [INDUSTRY | MEASURED (job postings) | May 2025–mid 2026] Indeed:
  - US software-development postings remain about 27.5% below their pre-pandemic level, but have rebounded from a low index value of 61.1 in May 2025.
  - They are up about 15% since Claude Code's release, while overall postings fell 7%.
  - 71% of the increase from May 2025 to May 2026 was in senior roles, and 37% was in jobs with "AI" in the title.
  - Sources: [Indeed Hiring Lab, Jul 8 2026](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/); [FRED series](https://fred.stlouisfed.org/series/IHLIDXUSTPSOFTDEVE); [CIO](https://www.cio.com/article/4195780/it-hiring-sees-a-boost-as-software-development-jobs-slowly-bounce-back.html)

### Inferences
- There are three layers of value capture:
  1. **Vendors capture revenue but not yet much profit.** Labs capture more than app-layer tools, because tool gross margins are about 35% or lower.
  2. **Customers and consumers capture a large, unpriced share,** through deflation in IT services, subsidized tool pricing and consumer surplus. The surplus is estimated at $97–172B a year for generative AI generally, set against much smaller revenue.
  3. **Incumbent software firms capture value through cost** where they can restructure (Shopify, Klarna: section 5). They lose it through price and seat pressure where they sell labor hours (IT services) or per-seat subscriptions (SaaS).
- Substitution and complementarity are both present and split by seniority. Junior and outsourced hours are substituted; senior and AI-skilled roles are complemented. So AI-tool spend partly replaces labor spend (the task-level automation shares and junior employment point that way) and partly adds to it (senior postings, AI roles). Net labor-cost savings for the industry are not measured anywhere.

### Gaps
- There is no reliable total for the AI-coding-tool market in 2026, and no audited revenue. ARR figures annualize the peak month.
- No data was found on Cursor's or Claude Code's gross margins in 2026, or on churn at vibe-coding tools.
- There is no measurement of what share of customer IT budgets moved from services or seats to AI tools.

---

## 5. Headcount claims: firms that said AI would let them freeze or cut engineering hiring — what do their results show?

### Takeaway
Firms that froze or cut headcount while citing AI did report strong output per employee:
- Shopify: headcount down about 6% while revenue grew about 30% in 2025.
- Klarna: revenue per employee about $1.1M, with staff roughly halved.

But the confounders are large (post-pandemic overhiring, attrition, the business cycle), and several cases were walked back or re-labelled:
- Klarna is rehiring for customer service.
- Duolingo's CEO scrapped the AI-usage performance rule in May 2026.
- Amazon's CEO said its 30,000 corporate cuts were "not even really AI-driven".

Big-tech figures for the share of code written by AI (Google: 75% of new code, Apr 2026) sit alongside modest reported velocity gains (Google: about 10%, Jun 2025).

### Cited Findings
- [FIRM | CLAIM | Feb 26–27 2025; 2026] Salesforce:
  - In Feb 2025, Marc Benioff said Salesforce would add no software engineers in 2025 because AI had raised engineering productivity "by more than 30%".
  - In 2026 he said its roughly 15,000 engineers are "hugely augmented" but still needed. By May 2026 he said almost nobody was being hired except in sales.
  - Sources: [SF Standard, Feb 27 2025](https://sfstandard.com/2025/02/27/salesforce-marcbenioff-layoffs-tech-agents/); [Salesforce Ben](https://www.salesforceben.com/salesforce-will-hire-no-more-software-engineers-in-2025-says-marc-benioff/); [Salesforce Ben 2026](https://www.salesforceben.com/ai-cant-replace-software-engineers-yet-marc-benioff-says/); [Fortune, May 28 2026](https://fortune.com/2026/05/28/ai-slashes-white-collar-jobs-salesforce-ceo-marc-benioff-one-department-still-hiring-sales/)
- [FIRM | MEASURED (company-reported) | 2022–2025] Klarna:
  - Headcount fell from about 5,527 (2022) to about 2,907 (2025), mostly by not replacing leavers.
  - Revenue per employee is about $1.1M, against $575k a year earlier. Average pay rose from $126k to $203k.
  - Its AI agent is said to do the work of 853 full-time agents and to have saved $60M.
  - The CEO admitted cost had been "a too prominent evaluation factor" and said Klarna would rehire human customer-service staff.
  - Sources: [Entrepreneur](https://www.entrepreneur.com/business-news/heres-how-klarna-has-cut-staff-in-half-while-raising-pay-by-60); [CX Dive](https://www.customerexperiencedive.com/news/klarna-says-ai-agent-work-853-employees/805987/); [TechCrunch, May 19 2025](https://techcrunch.com/2025/05/19/klarnas-revenue-per-employee-soars-to-nearly-1m-thanks-to-ai-efficiency-push/)
- [FIRM | MEASURED (financials) | Apr 2025 memo → FY2025] Shopify:
  - Tobi Lütke's memo of Apr 7 2025 said teams "must demonstrate why they cannot get what they want done using AI" before asking for headcount.
  - Headcount went from about 8,100 to about 7,600 by the end of 2025 (−6%). Revenue rose about 30% to $11.6B, with a 17% free-cash-flow margin.
  - Its annual filing says it intends to expand "without significant additional hiring in the near term."
  - Sources: [CNBC, Apr 7 2025](https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html); [Money.ca](https://money.ca/employment/shopify-ai-hiring-freeze-canadian-jobs); [Shopify Q4 2025 8-K](https://www.sec.gov/Archives/edgar/data/1594805/000159480526000006/exhibit991pressreleaseq420.htm)
- [FIRM | MEASURED (financials) + CLAIM | Apr 28 2025 → May 2026] Duolingo:
  - Its "AI-first" memo said contractors would be phased out for work AI can handle, and it drew user backlash.
  - 2025 revenue was $1.03B and bookings $1.15B (+33%).
  - The stock fell about 50% in 2025 and at one point was more than 80% below its 52-week high.
  - In May 2026 the CEO reportedly scrapped the rule tying performance to AI usage, saying workers had been using AI "just for AI's sake" (secondary source).
  - Sources: [Class Central](https://www.classcentral.com/report/duolingo-2025/); [Fast Company](https://www.fastcompany.com/91499936/duolingo-stock-price-falls-dramatic-collapse-ai-first-memo); [Metaintro](https://www.metaintro.com/blog/duolingo-ceo-walks-back-ai-first-memo-hiring-grows-2026)
- [FIRM | MEASURED + CLAIM | Oct 2025–Jan 2026] Amazon:
  - About 30,000 corporate roles were cut, 14k in Oct 2025 and 16k in Jan 2026.
  - Andy Jassy said "it's not even really AI-driven, not right now at least. It's culture."
  - Sources: [Fortune, Nov 1 2025](https://fortune.com/2025/11/01/ceo-andy-jassy-amazon-layoffs-about-culture-not-ai); [Idaho Business Review, Jan 28 2026](https://idahobusinessreview.com/2026/01/28/amazon-16000-job-cuts-corporate-layoffs-ai-restructuring/)
- [FIRM | CLAIM | Aug 2024] Amazon Q Developer:
  - Amazon migrated 30,000 production applications from Java 8/11 to Java 17. It says this saved 4,500 developer-years and produces about $260M a year in efficiency gains.
  - Average upgrade time fell from about 50 developer-days to a few hours, and 79% of auto-generated code reviews shipped without changes.
  - Sources: [AWS blog](https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone); [Digiday](https://digiday.com/media/how-amazons-genai-tool-for-developers-is-saving-4500-years-of-work-260-million-annually/)
- [FIRM | CLAIM | Oct 2024 → Apr 2026] Google:
  - AI-generated share of new code: more than 25% (Oct 2024), more than 30% (Apr 2025), 50% (autumn 2025) and 75% "AI-generated and approved by engineers" (Apr 2026).
  - Sundar Pichai put the gain at about 10% in "engineering velocity" (mid-2025).
  - A complex agent-assisted code migration was said to be 6x faster than a year earlier (2026).
  - Sources: [Fortune, Oct 30 2024](https://fortune.com/2024/10/30/googles-code-ai-sundar-pichai); [9to5Google, Jun 30 2025](https://9to5google.com/2025/06/30/google-engineers-ai-code/); [Fast Company, 2026](https://www.fastcompany.com/91531519/google-ceo-says-75-of-the-companys-code-is-ai-generated); [DevOps.com](https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/)

### Inferences
- In these cases, "flat or falling headcount with growing revenue" is a real improvement in firm-level labor productivity, captured as margin. But no case isolates AI from other drivers: correcting pandemic overhiring (which Jassy says explicitly), attrition-based cuts, and cyclical revenue recovery.
- There is a large gap between "share of code written by AI" (Google 75%) and "velocity" (Google about 10%). Lines of code are an input metric, and the bottleneck lies elsewhere (section 6).
- Walk-backs (Klarna in customer service, Duolingo) and relabelling (Amazon) suggest "AI-washing" of restructuring runs in both directions. This is a measurement problem for anyone using layoff announcements as evidence of AI value.

### Gaps
- Salesforce's engineering output and revenue growth during the 2025 freeze were not retrieved.
- Microsoft's 2025 layoffs and its claims about AI's share of code, and Meta's claims, were not verified because the search budget ran out.
- No study was found comparing AI-citing hiring-freeze firms with matched controls.

---

## 6. Mechanisms: why task-level speedups have not, or not yet, become industry-level value

### Takeaway
Task-level gains are real but vary widely: RCTs find about 26% more completed tasks, and isolated tasks can be 55–80% faster. They shrink at team and firm level through several well-evidenced mechanisms:
1. **Amdahl-type limits.** Coding is only 25–35% of idea-to-launch time.
2. **Review and QA bottlenecks.** PR review time rose 91% on high-AI teams.
3. **Quality and rework debt.** AI-written PRs carry about 1.7x more issues, duplicated code rose 8x, and AI adoption correlates with delivery instability.
4. **Perception gaps.** Experienced developers were 19% slower while believing they were 20% faster (2025).
5. **J-curve adjustment and slow diffusion,** with only 5–6% of firms redesigning workflows.
6. **Competition passing gains to customers** as price deflation.
7. **Measurement.** Consumer surplus, imported capex and lagged revenue are all missed.

### Cited Findings

**Task-level evidence (TASK)**
- [TASK | MEASURED (RCT) | published Sep 2024; Management Science 2025] Cui, Demirer, Jaffe, Musolff, Peng & Salz:
  - Three field experiments at Microsoft, Accenture and a Fortune 100 firm, covering 4,867 developers.
  - Developers with an AI coding assistant completed 26.08% more tasks (standard error 10.3%).
  - Adoption and gains were higher among less-experienced developers.
  - Sources: [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535); [MIT draft](https://economics.mit.edu/sites/default/files/inline-files/draft_copilot_experiments.pdf)
- [TASK | MEASURED (RCT) | Jul 2025] METR:
  - Experienced open-source developers took 19% longer with AI (CI +2% to +39%), yet estimated afterwards that AI had made them about 20% faster.
  - Source: [ScienceBlog summary](https://scienceblog.com/t-a-randomized-trial-by-metr-found-that-experienced-developers-completed-real-coding-tasks-19-slower-when-allowed-to-use-ai-tools-yet-afterwards-they-estimated-on-average-that-ai-had-made-them-20-fast/)
- [TASK | MEASURED (RCT, compromised) | Feb 24 2026] METR follow-up (late 2025):
  - Returning developers: "speedup" of −18% (CI −38% to +9%). New recruits: −4% (CI −15% to +9%). These are changes in completion time; secondary coverage reads them as a flip to about 18% faster.
  - METR calls the signal unreliable because many developers declined to take part without AI, which biases the estimate downward. It believes developers are more sped up in early 2026 than in early 2025, and is redesigning the study.
  - A May 2026 METR survey measured self-reported impact of early-2026 AI; details were not retrieved.
  - Sources: [METR, Feb 24 2026](https://metr.org/blog/2026-02-24-uplift-update/); [METR, May 11 2026](https://metr.org/blog/2026-05-11-ai-usage-survey/); [secondary "18% faster" framing](https://valueaddvc.com/blog/ai-coding-productivity-study-data-what-metr-mckinsey-and-github-actually-found-in-2026)
- [TASK | FORECAST inputs | Nov 2025 / Jan 2026] Anthropic: about 80% time savings per task in Claude conversations, but about 66% success on complex programming tasks. Adjusting for reliability and bottlenecks roughly halves the aggregate gain (section 1). — [Anthropic](https://www.anthropic.com/research/anthropic-economic-index-january-2026-report)

**Team-level evidence: throughput up, bottlenecks and instability up (TEAM)**
- [TEAM | MEASURED (telemetry) | Jul 2025] Faros AI:
  - Data from more than 10,000 developers on 1,255 teams.
  - High-AI teams complete 21% more tasks and merge 98% more PRs, but PR review time rises 91%.
  - Bugs per developer rise 9% and average PR size rises 154%.
  - There is "no significant correlation" between AI adoption and improvement at company level in throughput, DORA metrics or quality.
  - Sources: [Faros report](https://www.faros.ai/blog/ai-software-engineering); [PDF](https://243608892.fs1.hubspotusercontent-na2.net/hubfs/243608892/AI_Engineering_Impact_Report_July_2025_Faros_AI.pdf)
- [TEAM | SURVEY + modelling | Sep 2025] DORA 2025, State of AI-assisted Software Development:
  - AI adoption now correlates positively with delivery throughput, but still correlates with higher instability: more change failures, more rework and longer time to resolve issues.
  - It describes AI as an "amplifier" of a team's existing strengths and weaknesses.
  - Sources: [DORA](https://dora.dev/dora-report-2025/); [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)
- [TEAM | MEASURED (repo data) + SURVEY | Dec 2 2025] Anthropic internal study (read directly):
  - Engineers' self-reported productivity gain rose from +20% to +50% over a year, and merged PRs per engineer rose about 67%.
  - Most engineers can "fully delegate" only 0–20% of their work.
  - They report concerns about skills atrophy and a "supervision paradox": overseeing Claude needs the very skills that may atrophy.
  - Source: [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)

**Quality and rework debt (TEAM/INDUSTRY)**
- [INDUSTRY | MEASURED (code analysis) | Feb 2025] GitClear, analyzing 211M lines of code:
  - Code blocks with five or more duplicated lines rose 8x during 2024, and moved (refactored) lines fell 39.9%.
  - Refactoring's share of changed lines fell from 25% (2021) to under 10% (2024). The copy/paste share rose from 8.3% to 12.3%.
  - 2024 was the first year copy/pasted lines exceeded moved lines.
  - Sources: [GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research); [DevClass](https://www.devclass.com/ai-ml/2025/02/20/ai-is-eroding-code-quality-states-new-in-depth-report/1626250)
- [TEAM | MEASURED (vendor analysis) | Dec 17 2025] CodeRabbit, 470 open-source PRs:
  - AI-generated PRs had 10.83 issues each against 6.45 for human PRs, about 1.7x.
  - By category: logic 1.75x, maintainability 1.64x, security 1.57x, performance 1.42x. XSS vulnerabilities were 2.74x as likely.
  - The authors caveat that labelling PRs as human- or AI-authored is uncertain.
  - Sources: [CodeRabbit](https://www.coderabbit.ai/newsroom/state-of-ai-vs-human-code-generation-report); [BusinessWire](https://www.businesswire.com/news/home/20251217666881/en/CodeRabbits-State-of-AI-vs-Human-Code-Generation-Report-Finds-That-AI-Written-Code-Produces-1.7x-More-Issues-Than-Human-Code)
- [TASK | SURVEY | Jul–Dec 2025] Stack Overflow 2025 Developer Survey:
  - 84% of developers use or plan to use AI.
  - 46% distrust AI accuracy against 33% who trust it, and only 3% "highly trust" it. Trust fell to 29% from 40%.
  - 66% struggle with AI solutions that are "almost right".
  - Sources: [Stack Overflow survey](https://survey.stackoverflow.co/2025/ai); [press release](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/)

**Amdahl's law and process scope (FIRM)**
- [FIRM | SURVEY | Sep 2025] Bain: code generation is only 25–35% of idea-to-launch time. Gains reach 25–30% only when AI is applied across the whole lifecycle. — [Bain](https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/)

**J-curve and diffusion (MACRO)**
- [MACRO | ANALYSIS | 2018 WP; AEJ: Macro, Jan 2021] Brynjolfsson, Rock & Syverson, "The Productivity J-Curve":
  - General-purpose technologies need large intangible complementary investments. Those investments cause productivity to be under-measured early and over-measured later.
  - Adjusting for intangibles tied to computer hardware and software puts the 2017 TFP level 15.9% above official measures.
  - Sources: [AEA](https://www.aeaweb.org/articles?id=10.1257%2Fmac.20180386); [NBER w25148](https://www.nber.org/papers/w25148)
- [MACRO | ANALYSIS | 2026] Related evidence from sections 1–2:
  - Diffusion historically takes 20–30 years (St. Louis Fed coverage).
  - 95% of AI productivity talk on earnings calls is about the future.
  - The divergence between labor productivity and TFP resembles 1997 (SF Fed).
  - Perceived gains exceed measured gains because revenue arrives with a delay (Atlanta Fed/NBER w34984).
  - Sources: [Fortune, Jul 31 2026](https://fortune.com/2026/07/31/ai-productivity-doesnt-show-up-in-data-earnings-calls-st-louis-fed/); [SF Fed](https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/05/have-we-entered-era-of-high-productivity-growth/); [NBER w34984](https://www.nber.org/papers/w34984)

**Demand constraints and price pass-through (INDUSTRY)**
- [INDUSTRY | MEASURED/CLAIM | 2025–2026] Evidence covered in section 3:
  - Deflation in Indian IT services, and HCLTech needing 25–30% more effort for the same revenue.
  - Upwork coding and writing job posts down 21%.
  - App supply up 60–104% while spending grew about 11%.
  - The St. Louis Fed coverage argues that cheaper output loses value, offsetting the measured gains.
  - Sources: [The Register](https://www.theregister.com/software/2026/04/28/ai-deflation-comes-to-indias-tech-services-giants/5225686); [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2024.05420); [Allwork.space](https://allwork.space/2026/08/ai-may-be-erasing-the-value-of-its-own-productivity-gains-fed-research-finds/)
- [INDUSTRY | MEASURED | 2025–2026] Jevons-type counter-evidence:
  - Software postings are up about 15% since Claude Code's release while overall postings fell 7%, and senior and AI roles lead the growth.
  - GitHub added 36M new developers in a year.
  - Sources: [Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/); [GitHub](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)

**Measurement (MACRO)**
- [MACRO | ANALYSIS | 2025–2026] Consumer surplus of $97B (2024) and $116–172B (2025–26) from generative AI. Goldman's $160B of "true GDP" missing from official statistics. Imported AI capex adding to Taiwan's and Korea's GDP rather than the US's. Only 1% of S&P 500 firms quantifying earnings impact.
  - Sources: [Marginal Revolution](https://marginalrevolution.com/marginalrevolution/2025/08/the-consumer-surplus-from-ai.html); [Fortune](https://fortune.com/2025/09/17/how-much-gdp-artificial-intelligence-goldman-sachs-160-billion/); [Gizmodo](https://gizmodo.com/ai-added-basically-zero-to-us-economic-growth-last-year-goldman-sachs-says-2000725380); [Fortune](https://fortune.com/2026/03/03/goldman-earnings-ai-anxiety-no-meaningful-impact-productivity-economy-30-percent-in-2-areas/)

### Inferences
- **Amdahl arithmetic.** This is my calculation from Bain's range, not a sourced figure:
  - If coding is 30% of cycle time and AI doubles coding speed, end-to-end time falls only 15%.
  - If review time also rises, as the 91% in Faros suggests, net cycle-time gains can disappear.
  - This is enough on its own to explain why task-level speedups of 26–80% become 10–15% team gains (Bain), about 10% "velocity" (Google), and no significant company-level correlation (Faros).
- The quality evidence mostly comes from vendors with commercial interests: GitClear, CodeRabbit and Faros sell code-quality or engineering-analytics tools. It still consistently points to more rework and instability, so part of the throughput gain is borrowed from future maintenance. That debt would show up as later costs, not current value.
- Early METR evidence (−19% for experts, alongside a +20% perceived speedup) warns that self-reported gains, which underpin most firm surveys and the St. Louis Fed time-savings estimates, can overstate real gains. The 2026 follow-up suggests the sign may have flipped for newer tools, but that remains unestablished.
- The J-curve and "delayed revenue realization" explanations fit the evidence, but so far they cannot be falsified: nothing yet separates "not yet" from "not at all".

### Gaps
- The DORA 2024 finding that AI adoption was associated with lower throughput and stability, and older RCTs such as Peng et al. (2023), were not re-verified in this session.
- No independent, non-vendor study of AI code quality at large scale was found.
- There is no direct measurement of end-to-end cycle time (idea to production) before and after AI adoption at industry level.

---

## 7. Evidence in the other direction: where AI coding clearly created new value

### Takeaway
There is dated evidence of new value creation:
- **Company formation and time to revenue.** Stripe Atlas formations rose 41%. The share of Atlas startups charging their first customer within 30 days rose from 8% (2020) to 20%. The number of companies reaching $10M ARR within three months doubled.
- **Tiny teams.** Base44, a solo founder's company with fewer than 10 staff, sold for $80M about six months after founding.
- **Work that would not otherwise be done.** 27% of Claude-assisted work at Anthropic.
- **Legacy migrations.** Amazon cites 4,500 developer-years saved.
- **More apps and repositories.**
- **Rising measured productivity at software publishers** (+12.9% in 2025).
- **Large consumer surplus.**
- **A rebound in software-development job postings** since mid-2025.

Much of this value is either not captured in revenue (surplus, internal tools, long-tail apps) or is captured by AI vendors. That is why it is hard to see in industry P&Ls.

### Cited Findings
- [FIRM/INDUSTRY | MEASURED (platform data) | 2025, published ~Feb 2026] Stripe's 2025 annual letter and related data:
  - Businesses on Stripe processed $1.9T in total volume, up 34%.
  - Atlas formations rose 41%, and 20% of Atlas startups charged their first customer within 30 days, against 8% in 2020.
  - The 2025 startup cohort is growing about 50% faster than the 2024 cohort, and the number of companies reaching $10M ARR within three months of launch doubled YoY.
  - The top 100 AI companies on Stripe reached $1M of annualized revenue in a median 11.5 months, four months ahead of the fastest-growing SaaS companies. This figure may come from the prior letter (Feb 2025); attribution is uncertain.
  - Sources: [Stripe newsroom](https://stripe.com/newsroom/news/stripe-2025-update); [Stripe annual letter](https://stripe.com/annual-updates/2025); [SaaStr summary](https://www.saastr.com/stripes-latest-data-startups-are-growing-50-faster-computer-demand-drove-50-of-gdp-growth-60-more-apps-yoy-and-more/)
- [FIRM | MEASURED (deal) | Jun 2025] Wix agreed to buy Base44 for $80M, with more possible on revenue targets through 2029.
  - Base44 was built by solo founder Maor Shlomo about six months earlier, with no outside funding and fewer than 10 staff.
  - It had about 250,000 users and was profitable. Shlomo shared $25M with his eight-person team.
  - Sources: [Calcalist](https://www.calcalistech.com/ctechnews/article/s1iflnlelx); [Wix press release](https://www.wix.com/press-room/home/post/wix-further-expands-into-vibe-coding-with-acquisition-of-base44-a-hyper-growth-startup-that-simplif)
- [TEAM | SURVEY + transcripts | Dec 2 2025] At Anthropic, 27% of Claude-assisted work "consists of tasks that wouldn't have been done otherwise", such as scaling projects, dashboards, documentation and exploratory work. — [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- [TASK | MEASURED (usage) | Apr 28 2025] Startups account for 32.9% of Claude Code conversations and enterprises for 23.8%.
  - Web front-end work dominates: JavaScript/TypeScript is 31% of queries and HTML/CSS 28%.
  - Anthropic suggests simple apps and UIs face "earlier disruption" and that startups gain an edge from faster adoption.
  - Source: [Anthropic](https://www.anthropic.com/research/impact-software-development)
- [FIRM | CLAIM | Aug 2024; 2026] Time to completion on legacy work:
  - Amazon: Java upgrades fell from about 50 developer-days to hours, saving 4,500 developer-years and about $260M a year.
  - Google: a complex agent-assisted migration was 6x faster (2026).
  - Sources: [AWS](https://aws.amazon.com/blogs/devops/amazon-q-developer-just-reached-a-260-million-dollar-milestone); [DevOps.com](https://devops.com/google-ceo-says-75-of-new-code-is-ai-generated/)
- [FIRM | CLAIM | 2025–2026] New revenue pools that did not exist in Nov 2022 (section 4): Cursor more than $4B ARR, Claude Code more than $2.5B run-rate, Lovable more than $500M ARR with 146 staff.
  - Sources: [Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/); [TechCrunch](https://techcrunch.com/2026/03/11/lovable-says-it-added-100m-in-revenue-last-month-alone-with-just-146-employees/)
- [INDUSTRY | MEASURED | 2025] Software publishers' labor productivity rose 12.9%. — [ANI/BLS](https://www.aninews.in/news/business/software-and-gambling-leads-us-productivity-gains-but-rising-labor-costs-hit-most-service-industries-bls20260827141446/)
- [MACRO | SURVEY-based valuation | 2024–2026] Consumer surplus from generative AI was $97B (2024), rising from $116B to $172B (2025–26). — [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6569938)
- [INDUSTRY | MEASURED | 2025–2026] Software-development postings are up about 15% since Claude Code's release, while overall postings fell 7%. — [Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/)
- [FIRM | SURVEY | Sep 2025] BCG's 5% of "future-built" firms show 1.7x revenue growth and 1.6x EBIT margin compared with laggards. This is correlational, and selection is likely. — [BCG](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings)

### Inferences
- The strongest "new value" evidence is at the **extensive margin**: new firms, new apps, work that would not otherwise be done, and faster time to first revenue. That value tends to show up as:
  - consumer or user surplus, which is unpriced or cheap;
  - revenue for AI vendors;
  - small revenues spread across a very long tail.

  It does **not** show up as higher profits for incumbent software firms. That fits both "real value creation" and "no measurable incremental value for the (incumbent) industry" at once.
- Legacy-migration savings (Amazon, Google) are real cost value, but they fall in the category of "keeping the lights on". They show up as avoided cost, often reinvested, rather than as new output.

### Gaps
- There is no systematic measurement of internal or "long-tail" software built with AI, such as internal tools and scripts, or of its value.
- No estimate was found of consumer surplus specific to coding.
- Revenue for the median AI-built app, or the median vibe-coded business, is unknown.
- Stripe's figures describe Stripe's own customer base and are not representative of all new firms.

---

## 8. Synthesis: has AI coding produced incremental industry-level value? Where yes, where no, and why (with confidence levels)

### Takeaway
The user's hypothesis is that "even in coding, AI does not yet seem to have directly produced incremental value for the industry". The evidence supports it at the macro level and for the median incumbent firm's P&L (high confidence). It does not survive as a blanket statement about the software industry broadly defined, for three reasons:
1. Measured labor productivity at software publishers accelerated sharply in 2025.
2. A new AI-coding tool industry with tens of billions of dollars of run-rate revenue now exists.
3. New-product and new-firm formation measurably accelerated.

For these counter-signals, attribution to AI coding, value net of substitution, and profitability all remain uncertain (medium to low confidence).

The best-supported restatement: AI coding has produced large task-level gains and a fast-growing tooling industry. As of Sep 2026, little of this has become measurable incremental profit for incumbent software producers or measurable aggregate TFP. The value has mostly been:
- (a) captured as revenue, not yet profit, by AI labs and tool vendors;
- (b) passed to customers through price deflation and unpriced surplus;
- (c) absorbed by review, rework and organizational bottlenecks.

### Cited Findings

**Evidence FOR the hypothesis (no incremental industry value yet)**
- [MACRO] Utilization-adjusted TFP +0.07% over four quarters to Q1 2026, and no definitive high-productivity regime (SF Fed, May 2026). — [SF Fed](https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/05/have-we-entered-era-of-high-productivity-growth/)
- [MACRO] "No meaningful relationship between AI and productivity at the economy-wide level" (Goldman, Mar 2026). AI investment added "basically zero" to 2025 GDP (Hatzius, Feb 2026).
  - Sources: [Fortune](https://fortune.com/2026/03/03/goldman-earnings-ai-anxiety-no-meaningful-impact-productivity-economy-30-percent-in-2-areas/); [Gizmodo](https://gizmodo.com/ai-added-basically-zero-to-us-economic-growth-last-year-goldman-sachs-says-2000725380)
- [MACRO] About 95% of AI productivity statements on earnings calls refer to future gains (St. Louis Fed, Jul 2026). — [St. Louis Fed](https://www.stlouisfed.org/on-the-economy/2026/jul/ai-productivity-what-firms-say-earnings-calls)
- [FIRM] 89–90% of about 6,000 executives saw no productivity or employment impact (Feb 2026). 56% of CEOs saw no revenue or cost benefit (Jan 2026). Only 39% of firms report any EBIT impact, mostly under 5% (Nov 2025). Precise-zero earnings and hours effects in Denmark (2025).
  - Sources: [NBER w34836](https://www.nber.org/papers/w34836); [PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-global-ceo-survey.html); [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai); [BFI](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/)
- [FIRM/TEAM] In software specifically: 10–15% team gains that "rarely translate into business value" (Bain, Sep 2025). No company-level correlation between AI adoption and delivery metrics (Faros, Jul 2025). Higher instability (DORA, Sep 2025).
  - Sources: [Bain](https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/); [Faros](https://www.faros.ai/blog/ai-software-engineering); [DORA](https://dora.dev/dora-report-2025/)
- [INDUSTRY] Incumbents' revenue is under pressure:
  - TCS's first full-year USD revenue decline (FY26) and 2–5% AI deflation in Indian IT.
  - SaaS median growth in the low teens, with single digits in CRM and collaboration.
  - App supply up about 60–104% against spending up about 11%.
  - Sources: [Whalesbook](https://www.whalesbook.com/news/English/tech/TCS-Reports-First-Full-Year-USD-Revenue-Fall/69d79611e1f61dfbf512a227); [The Register](https://www.theregister.com/software/2026/04/28/ai-deflation-comes-to-indias-tech-services-giants/5225686); [PitchBook](https://pitchbook.com/news/reports/q2-2026-q2-2026-enterprise-saas-public-comp-sheet-saas-profits-strengthen-as-ai-disrupts-valuations); [TechCrunch](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/); [Sensor Tower](https://sensortower.com/press/press-release-boosted-by-gen-ai-services-consumers-spent-more-money-in-apps-than-games-for-first-time)

**Evidence AGAINST the hypothesis (incremental value is appearing)**
- [INDUSTRY] BLS: software publishers' labor productivity +12.9% in 2025, the top of the selected service industries (released Aug 2026). — [ANI/BLS](https://www.aninews.in/news/business/software-and-gambling-leads-us-productivity-gains-but-rising-labor-costs-hit-most-service-industries-bls20260827141446/)
- [FIRM/INDUSTRY] New revenue: Cursor more than $4B ARR (Jun 2026), Claude Code more than $2.5B (Feb 2026), Anthropic more than $30B run-rate (Apr 2026), Lovable $500M ARR with 146 staff.
  - Sources: [Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/); [VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth); [TechCrunch](https://techcrunch.com/2026/03/11/lovable-says-it-added-100m-in-revenue-last-month-alone-with-just-146-employees/)
- [FIRM] Among firms that implemented, median gains of about 30% in software development (Goldman). Shopify revenue +30% with headcount −6% (2025). Klarna revenue per employee about $1.1M.
  - Sources: [Fortune](https://fortune.com/2026/03/03/goldman-earnings-ai-anxiety-no-meaningful-impact-productivity-economy-30-percent-in-2-areas/); [Money.ca](https://money.ca/employment/shopify-ai-hiring-freeze-canadian-jobs); [Entrepreneur](https://www.entrepreneur.com/business-news/heres-how-klarna-has-cut-staff-in-half-while-raising-pay-by-60)
- [TASK/TEAM] RCTs show +26% completed tasks. Anthropic engineers merged 67% more PRs per engineer, and 27% of their Claude-assisted work would not otherwise have been done.
  - Sources: [Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535); [Anthropic](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic)
- [INDUSTRY/MACRO] Stripe Atlas formations +41%. Consumer surplus of $116–172B from generative AI (2025–26). Software postings rebounding about 15% since Claude Code's release.
  - Sources: [SaaStr/Stripe](https://www.saastr.com/stripes-latest-data-startups-are-growing-50-faster-computer-demand-drove-50-of-gdp-growth-60-more-apps-yoy-and-more/); [SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6569938); [Indeed](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/)
- [MACRO] Brynjolfsson's claim of a 2025 "harvest phase" at about 2.7% productivity growth (disputed: BLS annual average 2.2%; TFP flat). The industry-level correlation between time saved and productivity growth is 0.32 (not causal). — [Fortune](https://fortune.com/2026/02/15/ai-productivity-liftoff-doubling-2025-jobs-report-transition-harvest-phase-j-curve/); [St. Louis Fed](https://www.stlouisfed.org/open-vault/2025/oct/generative-ai-productivity-future-work)

### Inferences

**Graded conclusions**

1. **Aggregate US TFP and GDP show no clear AI-coding signal as of Q1–Q2 2026.** Confidence: **High.** Multiple independent Fed and Goldman analyses agree, and labor-productivity gains have non-AI explanations.
2. **The median firm has not yet booked P&L gains from generative AI.** Confidence: **High.** Five large surveys (2025–26) agree. **Medium** that this holds for coding specifically, because coding is the use case with the most frequently reported gains.
3. **Task-level coding productivity gains are real and positive on average, and larger for less-experienced developers and greenfield or simple tasks.** Confidence: **Medium-high.** The 2025 METR result shows experts on mature codebases can be slower, and the 2026 follow-up is unreliable.
4. **Team and firm gains are much smaller than task gains (roughly 10–15%, up to about 30% with process redesign), because of review and QA bottlenecks, Amdahl limits and rework.** Confidence: **Medium-high.** The telemetry comes mostly from tool vendors, but it all points the same way.
5. **Software publishers' measured productivity accelerated in 2025.** Confidence: **Medium**, since BLS revises heavily. That AI coding caused it: **Low.** Output is deflated revenue, the industry includes AI-product sellers, and hours fell after the layoffs.
6. **AI-coding vendors created genuinely new revenue, on the order of $10B+ of run-rate by mid-2026 across Cursor, Claude Code, Copilot, Lovable and others.** This is my rough aggregation of the figures above, not a sourced total. Confidence: **High** that the revenue is real; **Medium** that it is net-incremental, since part replaces labor or other software spend; **Low** that it is profitable at the application layer.
7. **Where value exists, a large share goes to customers:** IT-services deflation of 2–5% a year, subsidized tool pricing and consumer surplus. Confidence: **Medium-high** for IT services, **Medium** for SaaS and apps.
8. **New products and firms exist that otherwise would not** (the app surge, Base44, the Stripe cohorts, work not otherwise done). Confidence: **Medium-high** that the volume is real; **Low-medium** that it is yet economically significant, given revenue per app and the long tail.
9. **Job effects are compositional, not aggregate:** junior and outsourced hours are substituted, senior and AI roles are complemented. Confidence: **Medium.**

**Why the gap, ranked by strength of evidence**
1. **End-to-end bottlenecks and Amdahl's law.** Coding is 25–35% of the cycle, and review time rose 91% (strong).
2. **Competitive pass-through.** Productivity turns into lower prices rather than higher industry revenue (strong in IT services, emerging elsewhere).
3. **The organizational J-curve.** Only 5–6% of firms redesign workflows; they are the ones reporting gains (moderate, and correlational).
4. **Quality and rework debt** (moderate; mostly vendor studies).
5. **Measurement.** Unpriced surplus, internal tools, imported capex and revenue lags (moderate in theory, hard to quantify).
6. **Demand saturation versus Jevons.** Mixed evidence: app volume outruns spending, but software postings are rebounding.

**What would falsify or confirm the hypothesis by 2027**
- BLS 2026 productivity data for software publishers and computer systems design, due around Aug 2027.
- Whether TFP (not only labor productivity) accelerates in H2 2026 and 2027.
- Whether SaaS or IT-services revenue growth re-accelerates as volume gains outrun deflation.
- METR's redesigned RCT.
- Revenue and retention of AI-built apps.
- Whether coding-tool vendors reach positive gross margins without raising prices.

**Implication for extrapolating to other creative-software industries** (inference only)
- Industries whose output is sold per unit of labor (outsourcing, services) or per seat are likely to see deflation first.
- Industries where AI expands the long tail of products are likely to see volume growth well ahead of revenue growth.

### Gaps
- No causal study links AI-coding adoption to value added or profit at firm or industry level. All firm and industry links are correlational or self-reported.
- Primary BLS, BEA, NBER and Fed documents could not be read directly (egress blocked). Numbers come from search summaries and should be verified before publication, especially:
  - the BLS software-publisher figures (+12.9% for 2025, and 2024 revised from 9.4% to 4.0%);
  - the attribution of the 0.07% TFP figure;
  - the PitchBook SaaS growth numbers;
  - the Stripe "11.5 months" attribution;
  - revenue claims that appear only on aggregators (Claude Code $8B, Anthropic $47B, the close of the Cursor acquisition).
- These items from the brief were not covered: Midjourney and Gamma revenue per employee, the Builder.ai collapse, EPAM results, software-specific PPI deflation, the Microsoft and Meta headcount and AI-code claims, and Salesforce's results during the freeze.
