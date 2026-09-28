# Generative AI / LLM Adoption in Game Development (2022 → Sept 2026) and the Structure of Game-Production Work

> **Research-method note for the report writer:** All findings below come from web-search result extracts gathered on 2026-09-28. Every attempt to open the full pages failed because the network proxy blocked those domains (gdconf.com, gamedeveloper.com, businesswire.com, totallyhuman.io, gamelook.com.cn, gameres.com, substack, wikipedia, sagaftra.org, news.cn). Partway through, the session's web-search budget also ran out. So the figures here have **not** been checked against the original wording, and definitions (denominators, question wording) are only as precise as the search extracts. Where sources conflict or a figure is weak, I say so inline. I also list claims I could not verify in the Gaps sections as **unverified leads**. Do not cite those as facts.

---

## 1. Global survey time series (GDC, Unity, Google Cloud/Harris, a16z): adoption baselines and metric definitions

### Takeaway
Headline "AI adoption" in game development runs from about **36% to 96%**, depending on what is counted:
- **Vendor surveys of studios or developers** give the high end: Unity 2024 62% → Unity 2025 96% → Unity 2026 95%, and Google Cloud/Harris (Aug 2025) 90%.
- **GDC's independent survey of individual workers** gives the low end: 36% personally used gen-AI tools at work in 2026, and 52% worked at companies that had implemented gen AI in 2025.
- **What AI is used for:** reported use is concentrated in research/brainstorming, code assistance, prototyping and back-end tasks, not in final shipped assets.

### Cited Findings

**Time-series table (metric definitions as reported):**

| Survey | Published / fieldwork | Sample | Metric (as reported) | Result | Source |
|---|---|---|---|---|---|
| a16z Games AI tooling survey | May 2023 | 243 game studios; respondents 55% executives, 15% game designers, 12% developers | Studios already using AI tools / planning to | 87% using; 99% plan to | [The Decoder](https://the-decoder.com/gaming-executives-embrace-ai-tools-with-open-arms/); [T. Kirwin/a16z LinkedIn](https://www.linkedin.com/posts/troykirwin_a16z-games-ai-tooling-survey-activity-7064633856494080000-HLEG) |
| GDC State of the Game Industry 2024 | Jan 18, 2024 | GDC industry survey (n not verified) | Respondents either using AI or knowing a colleague who uses AI at work | 49% | [Game Developer](https://www.gamedeveloper.com/business/gdc-2024-state-of-the-game-industry-devs-discuss-layoffs-generative-ai-and-more); [BusinessWire](https://www.businesswire.com/news/home/20240118843393/en/Game-Developers-Conferences-2024-State-of-the-Game-Industry-Survey-Shows-Developer-Concern-About-Layoffs-Generative-AI-Usage-Game-Engine-Pricing-Changes-and-Return-to-Office-Policies) |
| Unity Gaming Report 2024 | Mar 18, 2024 | Unity studio survey | Studios incorporating AI in their workflows | 62% | [Game Developer](https://www.gamedeveloper.com/production/unity-2024-gaming-report-indicates-62-percent-of-devs-are-currently-using-ai-tools); [Unity IR](https://investors.unity.com/news/news-details/2024/2024-Unity-Gaming-Report-Highlights-Game-Studios-Continued-Resilience-As-They-Boldly-Stretch-Resources-Amidst-Shifting-Market-Forces/default.aspx) |
| GDC State of the Game Industry 2025 (13th annual) | Jan 21, 2025 | >3,000 developers and industry professionals | Respondents working at companies that have implemented gen AI | 52% | [BusinessWire](https://www.businesswire.com/news/home/20250121745145/en/The-2025-Game-Industry-Survey-Reveals-Increasing-Impact-Of-Layoffs-Concerns-With-The-Usage-Of-Generative-AI-Funding-Challenges-and-More); [GDC](https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/) |
| Unity Gaming Report 2025 | 2025 | Unity studio survey | Studios using AI tools in select workflows | 96% | [Unity blog](https://unity.com/blog/2025-unity-gaming-report-launch); [Gamereactor](https://www.gamereactor.eu/96-of-game-developers-are-integrating-ai-tools-into-their-workflow-according-to-unity-1516063) |
| Google Cloud / The Harris Poll | Fieldwork Jun 20–Jul 9, 2025; published Aug 18, 2025 | 615 game developers in the US, South Korea, Norway, Finland and Sweden | Developers already integrating AI into workflows | 90% (87% using AI agents; 97% say gen AI is reshaping the industry) | [Google Cloud press](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research); [PRNewswire](https://www.prnewswire.com/news-releases/90-of-games-developers-already-using-ai-in-workflows-according-to-new-google-cloud-research-302531363.html); [Techmeme/GamesIndustry.biz](https://www.techmeme.com/250818/p11) |
| GDC State of the Game Industry 2026 (14th annual) | Jan 29, 2026 | >2,300 game-industry professionals | Professionals personally using gen-AI tools as part of their job | 36% | [GDC](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [BusinessWire](https://www.businesswire.com/news/home/20260129438528/en/2026-State-of-the-Game-Industry-Report-Reveals-Widening-Effect-of-Layoffs-Broader-Perspectives-on-Generative-AI-Unionization-Tariffs-and-More); [Game Developer](https://www.gamedeveloper.com/business/one-third-of-game-workers-use-generative-ai-but-half-think-it-s-bad-for-the-industry) |
| Unity 2026 Game Development Report | 2026 | >300 game developers using Unity | Respondents who have adopted AI in their work | 95% (only 5% say they would not use AI) | [Unity blog](https://unity.com/blog/2026-unity-game-development-report-trends); [Digital Today](https://www.digitaltoday.co.kr/en/view/34682/unity-releases-2026-game-development-report) |

**Uses and tasks:**

GDC 2026:
- **Tasks among gen-AI users:** research or brainstorming 81%; daily tasks such as writing emails 47%; code assistance 47%; prototyping 35%. — [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [Yahoo Finance/BusinessWire](https://finance.yahoo.com/news/2026-state-game-industry-report-170100347.html)
- **Tools used:** ChatGPT 74%, Google Gemini 37%, Microsoft Copilot 22%. — [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)
- **Characterization:** "Most AI usage focuses on research, coding assistance, and prototyping — not final game assets." — [Game Developer](https://www.gamedeveloper.com/business/one-third-of-game-workers-use-generative-ai-but-half-think-it-s-bad-for-the-industry); [Yahoo Finance](https://finance.yahoo.com/news/2026-state-game-industry-report-170100347.html)

GDC 2025:
- **Use by department:** business and finance roles were most likely to use gen-AI tools (51%), followed by production and team leadership (41%) and community, marketing and PR (39%). — [GDC 2025](https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/); [Game Developer](https://www.gamedeveloper.com/business/developers-still-aren-t-warming-up-to-generative-ai)

Unity 2024:
- **Tasks:** 46% used AI to improve character animation; 37% to speed up code writing; 36% to generate artwork and levels, test gameplay loops, or automate narrative elements.
- **Reported benefits:** 71% of AI-using studios said AI improved delivery and operations; 68% said it speeds up prototyping.
- **Where used:** AI was most common in online multiplayer and VR/AR games.
- Sources: [Game Developer](https://www.gamedeveloper.com/production/unity-2024-gaming-report-indicates-62-percent-of-devs-are-currently-using-ai-tools); [Creative Bloq](https://www.creativebloq.com/news/unity-gaming-report-2024-ai-impact); [Game Rant](https://gamerant.com/game-studios-ai-unity-survey-report/)

Unity 2025:
- **Tasks:** mostly asset creation, code simplification and automated testing. Testing, localization and content generation led the automation areas.
- **Breadth vs depth:** "less than half of devs" used AI tools in any one workflow.
- Sources: [Gamereactor](https://www.gamereactor.eu/96-of-game-developers-are-integrating-ai-tools-into-their-workflow-according-to-unity-1516063); [Mobile Marketing Reads](https://www.mobilemarketingreads.com/2025-unity-gaming-report/); [Unity](https://unity.com/blog/2025-unity-gaming-report-launch)

Unity 2026:
- **Top AI uses:** coding assistance 62%; narrative and writing design 44%; NPC behaviour 40%; market research 37%; automated playtesting 35%.
- **Top benefits:** greater efficiency 73%; better decision-making 62%.
- **Sentiment:** 79% feel positive about AI.
- Sources: [Unity](https://unity.com/blog/2026-unity-game-development-report-trends); [Game Developer](https://www.gamedeveloper.com/production/unity-claims-79-percent-of-developers-are-feeling-positive-about-generative-ai); [GamesMarket](https://www.gamesmarket.global/2026-unity-game-development-report-released/)
- **Caution:** a Korean outlet headlined the Unity 2026 report as citing a "77% drop in development time". The metric's definition could not be verified. — [Digital Today](https://www.digitaltoday.co.kr/en/view/34682/unity-releases-2026-game-development-report). Wccftech framed the report as "smaller teams are making games in less time with AI tools handling the back-end work". — [Wccftech](https://wccftech.com/unity-2026-game-development-report-points-to-smaller-teams-making-games-in-less-time-with-ai/)

Google Cloud / Harris (2025):
- **How AI-agent users apply agents:** content optimization that adapts to in-game needs 44%; dynamic balancing and tuning 38%; procedural world generation 37%; automated content moderation 37%.
- **Challenges:** cost of AI integration 24%; staff upskilling 23%; difficulty measuring success 22%. 63% are concerned about data ownership.
- **Small studios:** 29% believe AI can level the playing field for smaller studios.
- Sources: [Google Cloud press](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research); [Techmeme](https://www.techmeme.com/250818/p11); [Cybernews](https://cybernews.com/ai-news/game-developers-ai-google-cloud/)

a16z (May 2023):
- Studios used AI tools mainly for design and storytelling. The most popular tools were ChatGPT and Midjourney, followed by Stable Diffusion and GitHub Copilot. — [The Decoder](https://the-decoder.com/gaming-executives-embrace-ai-tools-with-open-arms/)

### Inferences
- **Three measurement layers need to be kept apart.**
  - Layer 1: "Any AI use anywhere in the studio" (vendor surveys): ~90–96% by 2025–26. This is saturated and no longer informative.
  - Layer 2: "Individual workers personally using gen AI at work" (GDC): ~36% in 2026.
  - Layer 3: "Gen AI in player-facing shipped content" (Steam disclosures, section 2): ~20–31% of new releases, heavily skewed toward small publishers.
  - The report should not merge these into one "adoption rate."
- **Vendor surveys are likely biased upward.** Unity and Google sell AI tooling. Unity samples its own user base, and a16z's 2023 sample was 55% executives. GDC's independent, worker-heavy sample gives the lower figures.
- **Breadth is near-universal; depth is not.** Unity 2025's own caveat ("less than half … in any one workflow") suggests that by 2025, depth per workflow is the useful metric, not breadth.
- **Coding is the most consistently reported production use.**
  - The figures: 62% in Unity 2026; 47% of GDC 2026 AI users; 37% in Unity 2024.
  - This is directly relevant to extrapolating from LLM coding penetration.
  - But Steam disclosures exempt coding tools from 2026 (section 2), so coding adoption is invisible in shipped-product data.
- **GDC's figures are not a clean time series.** The 2024 figure (49%) includes "a colleague uses it". The 2025 figure (52%) is company-level. The 2026 figure (36%) is personal use.

### Gaps
- **Unverified leads (not confirmed in this session):**
  - GDC 2024's personal-use share (often cited as ~31%).
  - GDC 2025's personal-use share.
  - GDC 2026's company-level implementation share. A Medium post titled "The 52/52 split" says 52% of companies use gen AI *and* 52% of developers view it negatively in 2026 ([Medium/Cinevva](https://medium.com/@vio-202020/the-52-52-split-of-ai-use-in-the-game-industry-now-2ea497ef2c44)). It appears to pair the 2025 company figure with the 2026 sentiment figure. Treat it with caution.
- **a16z's 2024 games-AI survey** (a [GameDev Reports summary](https://gamedevreports.substack.com/p/a16z-games-use-of-ai-in-gaming-in) exists) could not be read. The "over 70% of studios" figure seen in [GAMES.GG](https://games.gg/news/game-studios-using-ai/) is unverified.
- **No data found** from the Game Developer Collective.
- **No 2022 quantitative baseline found.** The earliest survey in hand is a16z (May 2023).
- **Japan and Korea:** no Japan-specific (e.g., CESA) or Korea-specific (e.g., KOCCA) developer-survey figures could be retrieved. Google's sample includes South Korea, but a country split was not available.
- **No studio-size breakdowns** of adoption were retrieved from Unity, GDC or Google.
- **Unity 2026:** the exact publication date and the definition of the "77% development-time drop" were not verified. The 79% "positive" figure appears in coverage of both the 2025 and 2026 Unity reports ([Gamereactor 2025](https://www.gamereactor.eu/96-of-game-developers-are-integrating-ai-tools-into-their-workflow-according-to-unity-1516063) vs [Game Developer](https://www.gamedeveloper.com/production/unity-claims-79-percent-of-developers-are-feeling-positive-about-generative-ai)). It is unclear whether this is a repeat figure or a misattribution.

---

## 2. Steam generative-AI disclosure data (2024 → 2026)

### Takeaway
Steam AI disclosures have grown fast:
- **Games carrying a disclosure:** from ~1,000 in 2024 to ~7,818 by mid-2025 (~7% of the library), then 10,258 (~8%).
- **Share of new releases disclosing gen AI:** **10.9% (2024) → 19.9% (2025) → 30.8% (2026 through mid-year)**. At that trajectory, the share crosses ~50% in 2027–28.
- **Where the growth comes from:** almost entirely small, one-off publishers.
- **What is measured:** only self-reported, player-facing gen-AI content. Since January 2026, coding and other efficiency tools are explicitly exempt.

### Cited Findings
- **Disclosure rule:** since January 2024, Valve has required developers to disclose AI-generated content on Steam store pages. — [Cinevva](https://app.cinevva.com/news/2026-07-20-steam-ai-disclosure-study); [Sulka Haro](https://fragwyz.substack.com/p/three-years-of-ai-on-steam)
- **Totally Human (Ichiro Lambe, who built Valve's Steam Labs):**
  - **Counts:** 7,818 Steam titles disclose gen-AI use, about 7% of ~114,126 titles. That is up from "barely 1,000" in 2024 (+681%; "we've octupled last year's figure").
  - **New releases:** 20% of games released in 2025 disclosed AI use.
  - **Type of use:** about 60% of disclosures mention visual-asset generation (characters, backgrounds, models, textures). Others cover audio (music to voice-over) and text/narrative (item descriptions to story arcs).
  - Sources: [Tom's Hardware](https://www.tomshardware.com/video-games/pc-gaming/1-in-5-steam-games-released-in-2025-use-generative-ai-up-nearly-700-percent-year-on-year-7-818-titles-disclose-genai-asset-usage-7-percent-of-entire-steam-library); [PC Gamer](https://www.pcgamer.com/software/ai/the-boffin-behind-valves-steam-labs-says-the-number-of-steam-releases-featuring-genai-in-2025-is-1-in-5-with-7-percent-of-all-games-on-there-now-incorporating-it-weve-octupled-last-years-figure/); [80.lv](https://80.lv/articles/the-number-of-steam-games-featuring-gen-ai-has-increased-eightfold-in-a-year)
- **Totally Human, later update:** the count rose to **10,258 games (8% of all Steam games)**. Games with AI disclosures have grossed an estimated **~$660M** on Steam (Boxleiter method).
  - Developers' stated reasons: cutting cost and time to stay within tight budgets; faster prototyping (placeholder art, voices, ideas); making localization, translation and multilingual voice-overs affordable; and scaling up auxiliary, decorative or repetitive assets.
  - Source: [Totally Human](https://www.totallyhuman.io/blog/games-with-ai-disclosures-have-grossed-an-estimated-660m-on-steam)
- **Sulka Haro study (~53,600 Steam releases, mid-2023 to mid-2026):**
  - **Share of releases AI-flagged:** 10.9% in 2024, 19.9% in 2025, 30.8% in 2026 to date.
  - **Monthly launches:** AI-flagged launches rose from ~13/month before the mandate to ~530/month. Non-AI launches rose only from ~1,030 to ~1,320/month. AI-flagged games account for **60–90% of all growth** in Steam's monthly release count.
  - **Publisher concentration:** ~80% of the 37,000 distinct publishers have never shipped an AI-flagged game. Of those that have, 89% shipped exactly one.
  - **Projection:** at this trajectory, AI-disclosed games pass ~50% of releases in 2027–2028.
  - Sources: [Sulka Haro](https://fragwyz.substack.com/p/three-years-of-ai-on-steam); [PC Gamer](https://www.pcgamer.com/gaming-industry/steam-week-in-review-take-cover-because-it-looks-like-more-than-half-of-steam-games-will-have-an-ai-disclosure-by-2027-2028/); [GamesRadar+](https://www.gamesradar.com/games/half-of-all-games-released-on-steam-will-use-ai-by-2028-study-predicts-ai-lowers-the-barrier-not-just-to-make-a-game-but-to-make-several/); [Cinevva](https://app.cinevva.com/news/2026-07-20-steam-ai-disclosure-study)
- **Lower-quality aggregator figures:** "as of late July 2026, roughly one in five games listed in Steam's store content survey carries an AI disclosure label", and some reports say 40% of games launched in one week of June 2026 disclosed gen AI. — [Tech-Insider](https://tech-insider.org/steam-ai-disclosure-2026/). The denominator differs from Haro's (library or listing vs new releases). Treat as weak.
- **Valve policy update (January 2026):**
  - Back-end efficiency tools are exempt from disclosure, including code assistants (e.g., GitHub Copilot), automated bug-checking and office tools. Valve's wording: "Efficiency gains through the use of [AI-powered dev tools] is not the focus of this section."
  - Disclosure now focuses on gen-AI content "consumed by players" (art, sound, text, narrative).
  - A two-tier classification replaces the binary checkbox, and new requirements apply to runtime (live) AI generation.
  - Developers remain liable, and players can report issues through the Steam Overlay.
  - Sources: [GameSpot](https://www.gamespot.com/articles/valve-updates-ai-disclosure-guidelines-to-allow-for-ai-powered-tools/1100-6537483/); [Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/valve-clarifies-steam-ai-policy-focus-shifts-to-content-consumed); [Notebookcheck](https://www.notebookcheck.net/Steam-updates-AI-disclosure-form-requiring-developers-to-report-visible-and-in-game-AI-but-not-background-tools.1206103.0.html)
- **AAA disclosure example:**
  - Activision's *Call of Duty: Black Ops 7* Steam page states: "Our team uses generative AI tools to help develop some in game assets." Players flagged Ghibli-style calling cards as AI-generated.
  - Activision said AI-powered tools help "empower and support our teams to create the best gaming experiences possible for our players."
  - Sources: [PCGamesN](https://www.pcgamesn.com/call-of-duty-black-ops-7/ai-assets-steam-disclosure); [PC Gamer](https://www.pcgamer.com/games/call-of-duty/call-of-duty-black-ops-7-under-fire-for-using-what-sure-looks-like-ai-generated-studio-ghibli-style-calling-card-art/); [Kotaku](https://kotaku.com/call-of-duty-black-ops-7-ai-art-activision-statement-blops7-steam-ps5-2000644397)

### Inferences
- **Steam disclosure is a lower bound on player-facing gen AI**, because it is self-reported on an honor system. It is also a *non-measure* of production use. After the January 2026 update, code assistants (the most-used AI in dev surveys) are explicitly exempt. Steam data therefore understates programming adoption and cannot track "LLM coding penetration" in games.
- **The growth reflects supply expansion by new, small entrants more than AI in established pipelines.** Evidence: AI-flagged games drive 60–90% of release-count growth, and 89% of AI-shipping publishers have shipped exactly one AI game. For the discipline analysis, Steam shows gen AI substituting for art/audio/text budgets that small teams never had, rather than displacing existing AAA roles.
- **Visual assets dominate disclosures (~60%).** This matches China's art-first adoption pattern (section 4), but contrasts with Western worker surveys, where code and research dominate.

### Gaps
- Exact publication dates of the Totally Human 7,818 and 10,258 analyses were not verified. Search extracts place the first around the first half of 2025.
- No breakdown of AI-disclosed games by developer country (e.g., China-based vs Western), genre or price tier was retrieved.
- No revenue *share* data (AI-disclosed vs total Steam gross) was retrieved, beyond the ~$660M cumulative estimate.
- The share of *top-grossing* or AAA releases carrying disclosures was not found.

---

## 3. Developer sentiment and its trend; differences by role

### Takeaway
Among game workers, the share saying gen AI is having a **negative** impact on the industry rose from **18% (GDC 2024) to 30% (2025) to 52% (2026)**. The positive share fell from 13% to 7% (2025 → 2026).

By role, visual and technical artists (64% negative), game designers and narrative staff (63%) and programmers (59%) are most negative. Business and services roles are the least negative.

Executives and vendor surveys paint a far more positive picture (Unity: 79% positive), so there is a clear executive-vs-craft-worker divide. Sentiment worsened even as usage spread.

### Cited Findings
- **GDC 2026:** 52% think gen AI is having a negative impact, up from 30% in 2025 and 18% in 2024. About 7% think it is positive, down from 13% in 2025. — [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [80.lv](https://80.lv/articles/gdc-survey-over-50-of-game-devs-say-generative-ai-harms-industry); [GIANTY](https://www.gianty.com/gdc-2026-report-about-generative-ai/)
- **GDC 2026 by role:** the most unfavorable views are in visual and technical art (64% negative), game design and narrative (63%), and game programming (59%). Business operations and services roles had higher positivity (19% each). — [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [80.lv](https://80.lv/articles/gdc-survey-over-50-of-game-devs-say-generative-ai-harms-industry)
- **GDC 2026, users vs non-users:** "One third of game workers using genAI, but half think it's bad." Even among AI users, about half think it harms the industry. — [Game Developer](https://www.gamedeveloper.com/business/one-third-of-game-workers-use-generative-ai-but-half-think-it-s-bad-for-the-industry)
- **GDC 2025:** 30% negative, "a 12% increase from last year". — [BusinessWire](https://www.businesswire.com/news/home/20250121745145/en/The-2025-Game-Industry-Survey-Reveals-Increasing-Impact-Of-Layoffs-Concerns-With-The-Usage-Of-Generative-AI-Funding-Challenges-and-More)
- **Vendor-survey framing:**
  - Unity 2026: 79% of respondents feel positive about using AI; 5% are apprehensive. — [Game Developer](https://www.gamedeveloper.com/production/unity-claims-79-percent-of-developers-are-feeling-positive-about-generative-ai)
  - Google/Harris: 97% believe gen AI is reshaping the industry, but 63% are concerned about data ownership. — [Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research); [Techmeme](https://www.techmeme.com/250818/p11)
- **Executive statements (positive):**
  - EA CEO Andrew Wilson: AI is meant to "augment, enhance, extend, and expand" rather than replace. — [Game Developer](https://www.gamedeveloper.com/production/ea-ceo-60-percent-of-dev-processes-could-be-impacted-by-generative-ai-); [Insider Gaming](https://insider-gaming.com/ea-ceo-ai-development-process-impact/)
  - Tencent President Liu Chiping (刘炽平): games are among the industries that benefit from AI. — [Tencent News](https://news.qq.com/rain/a/20260319A08TD000)
  - NetEase CEO Ding Lei (丁磊): AI lowers the "entry threshold" (准入门槛) but greatly raises the "success threshold" (成功门槛) for top products. — [The Paper](https://www.thepaper.cn/newsDetail_forward_32585947); [Tencent News](https://news.qq.com/rain/a/20260211A07KNA00)
- **miHoYo co-founder Cai Haoyu (蔡浩宇), Aug 2024 on LinkedIn:** "AIGC has completely changed game development." Only the top 0.0001% of geniuses and the 99% of amateurs will make games meaningfully, and ordinary professional developers "might consider switching careers." — [The Paper](https://www.thepaper.cn/newsDetail_forward_28579496); [36Kr](https://36kr.com/p/3218346434661254)
- **Chinese practitioner perception (伽马数据 2025):** about 80% of respondents perceive project-efficiency gains above 20%, and about 10% perceive gains above 50%. — [Jiemian](https://www.jiemian.com/article/11326157.html); [GameRes](https://www.gameres.com/906453.html)
- **Consumer and producer backlash:**
  - Embark CEO Patrick Söderlund on ARC Raiders' AI voices: "There is a quality difference. A real professional actor is better than AI; that's just how it is." — [Engadget](https://www.engadget.com/gaming/arc-raiders-replaced-some-of-its-ai-generated-voice-lines-with-professional-actors-184915627.html); [Kotaku](https://kotaku.com/arc-raiders-replaced-ai-generated-content-human-recorded-dialogue-voices-2000678774)
  - *Black Ops 7* AI calling cards drew criticism. — [PC Gamer](https://www.pcgamer.com/games/call-of-duty/call-of-duty-black-ops-7-under-fire-for-using-what-sure-looks-like-ai-generated-studio-ghibli-style-calling-card-art/)

### Inferences
- **Adoption and sentiment are diverging.** Personal use sits at ~36% and company-level implementation was ~52% (2025), while negative sentiment went from 18% to 52% in two years. Together with layoffs (section 7), this points to top-down, management-driven adoption rather than a bottom-up pull from craft workers.
- **Negativity is highest where output is most substitutable** (2D/visual art, writing and design) and in roles hit by layoffs (GDC 2026: designers were the most affected profession). Programmers are also strongly negative (59%) despite coding being the most-used task. So negativity is not purely about displacement. It likely reflects ethics/IP concerns, the layoffs backdrop and quality concerns (inference).
- **Western vs Chinese discourse:** Chinese industry reports and executives frame AI as mainstream efficiency infrastructure. Western worker surveys and player reactions frame it as contested. This affects how fast player-facing AI can ship in each market (inference).

### Gaps
- **Unverified leads:**
  - GDC 2024's positive share (often cited ~21%).
  - GDC 2024's "ethics concern" share (extracts say ~80%; commonly cited as 84%).
- Role breakdowns of sentiment for 2024 and 2025 were not retrieved.
- No executive-only sentiment series was found (a16z 2023 was 55% executives, but reported adoption, not sentiment).
- No Chinese, Japanese or Korean worker-level sentiment surveys were found.
- The Game Developer Collective's sentiment data was not found.

---

## 4. China (dedicated section): adoption share, per-discipline efficiency claims, company cases, art-outsourcing effects

### Takeaway
**Adoption claims have climbed from "over 60% of top-50 firms" to near-universal.**
- 2023: >60% of top-50 revenue firms had deployed AIGC.
- 2025: >99% of surveyed practitioners' companies had introduced AI tools.
- 2026: ~80%+ of enterprises, with 84–86% penetration of development stages.
- Samples skew toward large firms.

**The art pipeline, not code, is the lead application.**
- Art-stage AI application is claimed at >80%.
- 三七互娱 (37 Interactive, "37 Games") says AI generates >80% of its 2D art assets and saves 60–80% of hours in character concept art.
- Tencent's Hunyuan 3D cut modeling time from 8h to 2.5h in internal tests.
- NetEase claims its "AI-native pipeline" lifts efficiency in some stages by 300%.

**The labor-side signal came early and is concentrated in 2D illustration and outsourcing.** Illustrator job openings fell ~70% (2023, recruiter estimate), and outsourced character-design prices fell ~75% (anecdotal).

### Cited Findings

**Market context:**
- 游戏工委 (the China Audio-Video and Digital Publishing Association's game committee), *2025 China Game Industry Report*: domestic market ¥350.789B (+7.68% YoY); mobile games 73.29% of revenue. — [GameLook](http://www.gamelook.com.cn/2025/12/584413/); [IT之家](https://www.ithome.com/0/906/428.htm); [CGIGC](https://www.cgigc.com.cn/details.html?id=08de474f-eed0-496a-8fdc-bb4a06b1b1a1&tp=report)

**Adoption share over time (metric definitions differ; see Inferences):**
- **2023 — 伽马数据 (Gamma Data):** more than 60% of China's top-50 game companies by revenue had explicitly deployed AIGC. — [The Paper (我国超六成游戏企业应用AI)](https://m.thepaper.cn/newsDetail_forward_24054724); [南方都市报/oeeee](https://m.mp.oeeee.com/a/BAAFRD000020230731825322.html); [199IT](https://www.199it.com/archives/1637421.html)
- **2024 — 伽马数据, *China Game Industry AIGC Development Outlook Report 2024*:** AI can raise concept-art (原画) efficiency by nearly 50%. AI does the first ~50% of the work and the artist revises the remaining ~50%. AIGC helps artists find reference shapes, colors and elements, cutting draft-iteration time. — [Tencent News](https://news.qq.com/rain/a/20240626A03QMV00); [STCN](https://www.stcn.com/article/detail/1241443.html); [GameNews](https://www.gamenewstc.com/nd.jsp?id=2001)
  - The same coverage characterized AIGC in 2024 as still a "simple plug-in" (简单外挂), with real cost reduction "still hard". — [Tencent News](https://news.qq.com/rain/a/20240626A03QMV00)
- **July 2025 — 伽马数据, *China Game Industry New Quality Productive Forces Report* (《中国游戏产业新质生产力发展报告》):**
  - **>99% of respondents' companies or departments** had introduced AI technology and tools.
  - ~80% perceive overall project-efficiency gains >20%, and ~10% perceive >50%.
  - ~70% of game companies significantly increased tech investment.
  - Nearly 80% of the top 50 have layouts in AI, digital twins, engines, cloud and XR.
  - Sources: [Jiemian](https://www.jiemian.com/article/11326157.html); [GameRes](https://www.gameres.com/906453.html); [新快网](https://www.xkb.com.cn/articleDetail/321956); [China.com](https://m.tech.china.com/articles/20250707/202507071695709.html)
- **December 2025 — 游戏工委, *Game Enterprise AI Technology Application Report* (《游戏企业AI技术应用报告》):**
  - Surveyed 22 representative companies, including Tencent Games, NetEase Games and Century Huatong (世纪华通). The extract's names "Kaixin Network" and "Xiashan Ju" appear garbled.
  - Companies were concentrated in Beijing, Shanghai, Guangdong, Fujian and Zhejiang; 90.9% had annual revenue >¥100M.
  - Source: [GameLook](http://www.gamelook.com.cn/2025/12/584581/)
- **2026 — industry media, conflicting figures:**
  - "Nearly 80% of domestic game enterprises" use AI in business operations; AI penetration of development stages "exceeds 84%"; generating static visual assets has become an "industry standard". — [Xinhua, 2026-09-07 (与AI同"游")](https://www.news.cn/tech/20260907/0b635667b2c04c21bb2ebfe06e1a59aa/c.html); [Eastmoney, 2026-06-12](https://caifuhao.eastmoney.com/news/20260612161156694575740)
  - Coverage around ChinaJoy 2026 reports "游戏企业AI普及率达86%" (game-company AI penetration 86%), with overall adoption in game development "exceeding 86.36%" and art-stage AI application rate ">80%". It references the white paper 《双向赋能：AI与游戏的协同进化》. — [Sina Tech, 2026-08-01](https://finance.sina.com.cn/tech/roll/2026-08-01/doc-inikvnzz3648216.shtml); [Sina Finance, 2026-08-08](https://finance.sina.com.cn/wm/2026-08-08/doc-inimqimt2723745.shtml)
  - The 84% vs 86.36% figures conflict, and the underlying survey could not be opened.
- **ChinaJoy 2026** (opened July 31, 2026) ran under the theme "与AI同游" ("playing with AI"). — [Xinhua](http://www.news.cn/tech/20260626/a35e1fb600e149879a653e222a4711f1/c.html)

**Company cases:**

Tencent (腾讯):
- **Hunyuan 3D (混元3D), internal testing:**
  - Average modeling time fell from **8 hours to 2.5 hours** (~3x).
  - Scene-prop iteration cycles were **shortened 60%**.
  - Asset reusability **improved 50%**.
  - Deployed in dozens of internal game projects.
  - Sources: [BAAI Hub (混元3D Studio architecture)](https://hub.baai.ac.cn/view/49146); [Tencent News](https://news.qq.com/rain/a/20251127A03RPD00); [InfoQ](https://www.infoq.cn/article/vmkbfaargbtscpu4smuf)
- **Hunyuan 3D v2.5** went live on Tencent Cloud for game developers (Q2 2025 results coverage). — [Xinhua](http://www.news.cn/tech/20250813/28167f68cd2b4a83a87cb5d7f7683c39/c.html)
- **Hunyuan 3D 3.0** coverage described a game-AI "arms race" entering deep water. — [STCN](https://www.stcn.com/article/detail/3346933.html)
- **FY2025 results (Mar 18, 2026):**
  - Game revenue ~¥241.6B (+22% YoY).
  - AI improved content-production efficiency, user experience and marketing effectiveness across *Honor of Kings*, *Peace Elite* and *Delta Force*.
  - Coverage states **40+ Tencent games** deployed AI across R&D, gameplay and operations in 2025.
  - Sources: [Xinhua](http://www.news.cn/tech/20260318/f8dd0672c8554770b9d3bffdf783c7c1/c.html); [Xinhua](https://www.news.cn/tech/20260318/8b00d51b86ca42e88f9b98dd9134ab2e/c.html); [Tencent News](https://news.qq.com/rain/a/20260319A08TD000)
- **R&D spend:** Tencent put "800多亿元" (¥80B+) into R&D in 2025. — [Beijing News](https://m.bjnews.com.cn/detail/1774079710169610.html)
- **GiiNEX (Tencent's game-AI engine), GDC 2025:**
  - Virtual-city development cut from **5 days to 25 minutes**.
  - Building-exterior generation **50x** faster.
  - An LLM-based AICoaching system for *Honor of Kings* players.
  - Sources: [Sohu](https://www.sohu.com/a/875925906_122004016); [游戏陀螺](https://www.youxituoluo.com/533274.html)

NetEase (网易):
- **FY2025 (reported Feb 11, 2026):**
  - Net revenue ¥112.6B (+6.9%); attributable net profit ¥33.8B (+13.8%).
  - Games ≈82% of revenue.
  - R&D ¥17.7B (the sixth straight year above ¥10B).
  - Ding Lei says AI is now a foundational core capability for R&D and operations.
  - Sources: [CNR](https://finance.cnr.cn/ycbd/20260211/t20260211_527523623.shtml); [Sina](https://finance.sina.com.cn/roll/2026-02-13/doc-inhmrnzp6180065.shtml); [Tencent News](https://news.qq.com/rain/a/20260211A07KNA00)
- **AI-native pipeline:** NetEase's "AI原生管线" covers concept art, modeling, animation, audio, level design and testing, with "some stages" seeing **+300% efficiency**. — [iiMedia](https://www.iimedia.cn/c1040/109721.html); [Tencent News](https://news.qq.com/rain/a/20260211A07KNA00)
- **Q1 2025 call:** AI is "fully applied" in game R&D and user-experience work. — [Sina (Q1 2025 call transcript)](https://finance.sina.com.cn/tech/2025-05-15/doc-inewsfmx1921508.shtml)
- ***Justice Mobile* (逆水寒手游) player-created AI NPCs:**
  - The "自捏AI江湖友人" feature let players create their own AI companions. It launched Aug 23 and drew **>5 million player-created intelligent NPCs within three days**.
  - Sources: [IT之家](https://www.ithome.com/0/791/380.htm)
- ***Justice Mobile* AI arena (with NetEase Fuxi 伏羲, Nov 2024):**
  - Fuxi invited five LLM vendors (Alibaba Tongyi, Baidu ERNIE, MiniMax abab, Moonshot Kimi, ByteDance Doubao). Each model drives NPCs across nine story themes.
  - Sources: [GeekPark](https://www.geekpark.net/news/343404); [NetEase Fuxi](https://fuxi.163.com/database/1264); [Justice official site](https://h.163.com/news/official/20241119/37231_1194592.html)

37 Interactive / 37 Games (三七互娱):
- **Internal AI platforms:** "易览" (market intelligence for greenlighting), "天工" (art project management) and "图灵" (2D art asset generation, shared by R&D and publishing).
- **Output:** 图灵 produces **>280,000 2D images per month** and saves **60–80% of hours** in character concept art.
- **AI share of assets:**
  - AI-generated 2D art assets exceed 80%.
  - AI-assisted 3D models exceed 30%.
  - AI participates in ~70% of video (ad) material.
- **Office tooling:** the internal AI assistant "小七" is used by >90% of employees, running on an internal AI-agent platform built in 2023.
- Sources: [Tencent News, 2025-12-10](https://news.qq.com/rain/a/20251210A07R6E00?media_id=&suid=); [Sina](https://finance.sina.com.cn/roll/2025-12-10/doc-inhaiuqy8625008.shtml); [Guancha](https://user.guancha.cn/main/content?id=1293030&s=fwtjgzwz); [Sina, 2025-04-21](https://finance.sina.com.cn/stock/stockzmt/2025-04-21/doc-inetxwtq4866821.shtml)

Giant Network (巨人网络):
- **AI strategy:** set up an AI lab in late 2022. In 2024, founder Shi Yuzhu (史玉柱) declared AI as important as the game business. — [21世纪经济报道](https://www.21jingji.com/article/20240411/59f49861fdf4abf53b8ff2bfa65b3545.html)
- **FY2025 results:** revenue ¥5.047B (+72.69%); net profit ¥1.755B (+23.13%). Technical staff *grew* by 117.
- ***Supernatural Action Group* (《超自然行动组》):** uses LLM-driven real-time NPC interaction and passed 10M DAU by Jan 2026.
- **Investment:** in Feb 2025 Giant invested in LiblibAI (哩布哩布AI, image generation) for game-art cost reduction.
- Sources: [Tencent News, 2026-04-21](https://news.qq.com/rain/a/20260421A0207F00); [Eastmoney](https://caifuhao.eastmoney.com/news/20260709165457243395710); [Eastmoney](https://caifuhao.eastmoney.com/news/20260417211634603861710)

miHoYo (米哈游) / Cai Haoyu:
- Cai's August 2024 statement is quoted in section 3.
- He founded the AI company **Anuttacon**, with 30–40 staff, about half from miHoYo. — [The Paper](https://www.thepaper.cn/newsDetail_forward_28579496); [Tencent News](https://news.qq.com/rain/a/20250213A08Z7V00); [Jiemian](https://www.jiemian.com/article/13849253.html)
- No information on miHoYo art-team layoffs was found.

**Art outsourcing and junior art roles:**
- **Rest of World (April 2023):**
  - A Hangzhou game recruiter (Leo Li) estimated **illustrator job openings fell ~70% in a year**. He attributed this to regulatory pressure and the economy as well as AI.
  - Chinese developers including Tencent were using Midjourney and Stable Diffusion for characters, backgrounds and promotional material.
  - A freelance illustrator who earned ¥3,000–7,000 per poster saw that work disappear.
  - Sources: [Rest of World](https://restofworld.org/2023/ai-china-video-game-layoffs-illustrators/); [Game World Observer](https://gameworldobserver.com/2023/04/12/game-artist-jobs-china-down-70-percent-gen-ai-adoption)
- **GameLook (April 2023):** prices for domestic outsourced concept art "plunged". Some foreign publishers *banned* AI in outsourced work and required human-drawn art. — [GameLook](http://www.gamelook.com.cn/2023/04/514084/)
- **Reported price compression:**
  - One character design fell from ~¥8,000 to ~¥2,000.
  - Two mobile-game scene illustrations fell from several thousand yuan to ~¥1,500 in total.
  - Image-revision work fell to as low as ¥200 per image.
  - Some mature projects used AI as a pretext to compress prices, while AI was mainly applied to non-core design phases that still needed manual refinement.
  - Sources (exact attribution among these could not be verified): [Jiemian](https://www.jiemian.com/article/9548103.html); [GameLook](http://www.gamelook.com.cn/2023/04/514084/); [三易生活](https://m.3elife.net/Art/internet/202304/12/82162.html)
- **Anecdotal cuts:** there are reports of outsourcing teams cutting half their concept artists, and some firms cutting 50–80% of art staff. — [Zhihu question](https://www.zhihu.com/question/593474870); [三易生活](https://m.3elife.net/Art/internet/202304/12/82162.html)
- **Outsourcing vendors pivoting** to AI generation plus human refinement. — [游戏陀螺](https://www.youxituoluo.com/530988.html)
- **Low-reliability secondary claim:** a 7.GAME Zhihu column says the 2025 "game-job layoff rate" reached 53%, and that art roles were hardest hit (~24%, tied with programming). — [Zhihu/7.GAME](https://zhuanlan.zhihu.com/p/2029904588564898253)

### Inferences
- **The Chinese adoption series mixes units.**
  - Top-50 firms with AIGC deployed (>60%, 2023).
  - Respondents whose company or department uses AI (>99%, 2025).
  - Enterprises using AI (~80%, 2026).
  - Development-stage penetration (84% / 86.36%, 2026).
  - These are not comparable points on one curve. The 游戏工委 sample is 90.9% firms with >¥100M revenue, and small-studio adoption in China is largely unmeasured.
- **Chinese efficiency figures are mostly company-claimed or self-perceived, not audited.** Tencent's Hunyuan 3D (8h → 2.5h) is described as internal testing, the closest thing to a measurement. 37 Games and NetEase figures are company claims. 伽马数据's figures are respondent perceptions.
- **China's AI lead is in art and UA/marketing creatives, not code.** Plausible drivers (inference): mobile/F2P economics with heavy 2D character art and ad-creative volume (mobile is 73% of the domestic market); a large domestic art-outsourcing base; and weaker union or contractual constraints than Western voice and art workforces.
- **Big Chinese firms are not cutting R&D.** NetEase R&D ¥17.7B, Tencent ¥80B+, and Giant added technical staff. At the majors, AI appears to reallocate effort toward more content, AI features and runtime AI, rather than cutting total R&D. At the same time, it squeezes the external 2D outsourcing layer and junior illustration roles.
- **2024 → 2025–26 shift in tone.** In 2024, industry commentary still called AIGC a "simple plug-in" with little real cost reduction. By 2025–26, firms claim end-to-end AI pipelines. Much of the production-scale integration therefore likely happened in 2025.

### Gaps
- The per-stage percentages in 游戏工委's December 2025 AI application report (art/program/design/QA/ops) could not be retrieved; the page was blocked.
- No 腾讯研究院 (Tencent Research Institute) game-AI report data was found.
- No 游戏葡萄 (Youxiputao) or 触乐 (Chuapp) quantitative coverage was retrieved.
- No data was found on Perfect World (完美世界), or on miHoYo's internal AI pipeline or headcount.
- No China job-posting data (e.g., BOSS直聘 or 智联招聘 art vs engineering postings) was found.
- No audited cost-saving figures were found (e.g., art-outsourcing spend in annual reports before and after AI).
- The source of the 84% vs 86.36% "dev-stage penetration" figures, and the white paper 《双向赋能：AI与游戏的协同进化》, could not be opened.
- 数数科技 (ThinkingData) published a "2025 AI game-industry application white paper" ([ThinkingData](https://www.thinkingdata.cn/thinking/whitepaper/8529.html)); its contents were not retrieved.

---

## 5. Company adoption cases and strategies outside China (Japan / Korea / Western)

### Takeaway
Strategies outside China range across four modes:
- **Corporate "AI-first" transformation:** Krafton (Oct 2025, ~₩100B GPU cluster).
- **Explicit automation targets:** Square Enix aims to automate 70% of QA and debugging with gen AI by end-2027. EA's CEO says ~60% of EA processes are highly feasible for gen-AI impact.
- **Research prototypes:** Microsoft Muse/WHAM and the WHAMM Quake II demo; Ubisoft NEO NPC → Teammates.
- **Selective shipped use under backlash:** Embark's TTS voices; Activision's *Black Ops 7* asset disclosure.

The clearest reported AI-linked headcount substitution is at King (~200 layoffs, July 2025).

### Cited Findings

**Korea — Krafton:**
- On Oct 23, 2025, CEO Changhan Kim declared Krafton an "AI First" company, with key commitments:
  - ~₩100B (~$70M) on a GPU cluster for agentic AI.
  - ~₩30B (~$20.8M) per year to support employees' use of AI.
  - Automating work around agentic AI while staff focus on creative work.
  - Overhauling HR systems and organizational operations to be AI-centered.
- Sources: [Asia Business Daily](https://www.asiae.co.kr/en/article/2025102311585579811); [Game Developer](https://www.gamedeveloper.com/business/subnautica-owner-krafton-outlines-plans-to-transform-into-an-ai-first-company); [PC Gamer](https://www.pcgamer.com/software/ai/krafton-is-now-an-ai-first-company-will-spend-usd70-million-on-a-gpu-cluster-to-serve-as-the-foundation-for-accelerating-the-implementation-of-agentic-ai/)

**Korea / Sweden — Nexon's Embark Studios:**
- *The Finals* used AI TTS built from actors' recordings for announcers, commentators and most team voice lines.
- *ARC Raiders* (launched October 2025, peaking near half a million concurrent Steam users) used TTS for less immersion-critical lines. Embark paid actors to license their voices.
- After backlash, Embark re-recorded *some* lines with human actors.
- Sources: [Engadget](https://www.engadget.com/gaming/arc-raiders-replaced-some-of-its-ai-generated-voice-lines-with-professional-actors-184915627.html); [Kotaku](https://kotaku.com/arc-raiders-replaced-ai-generated-content-human-recorded-dialogue-voices-2000678774); [Game Rant](https://gamerant.com/arc-raiders-controversial-ai-voice-change/); [AI and Games](https://www.aiandgames.com/p/arc-raiders-and-the-ethical-use-of)

**Japan — Square Enix (Nov 2025):**
- Target: generative AI to handle **70% of QA and debugging by end-2027**.
- Joint research with the University of Tokyo's Matsuo Lab ("Joint Development of Game QA Automation Technology Using Generative AI"), with a team of 10+ researchers and engineers.
- Part of the "Square Enix Reboots and Awakens" plan.
- Sources: [VGC](https://www.videogameschronicle.com/news/square-enix-says-it-wants-generative-ai-to-be-doing-70-of-its-qa-and-debugging-by-the-end-of-2027/); [GameSpot](https://www.gamespot.com/articles/square-enix-wants-genai-to-automate-70-of-game-qa-by-2027/1100-6535996/); [Game Developer](https://www.gamedeveloper.com/business/square-enix-wants-to-use-gen-ai-to-automate-70-percent-of-qa-and-debugging-by-late-2027)

**US — EA:**
- CEO Andrew Wilson: ~**60% of EA's processes** have high feasibility for gen-AI impact, framed as efficiency, expansion and transformation.
- Examples he gave: work that took six weeks could take six days, and *EA Sports FC 24* run cycles grew from 12 to 1,200.
- Sources: [Game Developer](https://www.gamedeveloper.com/production/ea-ceo-60-percent-of-dev-processes-could-be-impacted-by-generative-ai-); [Insider Gaming](https://insider-gaming.com/ea-ceo-ai-development-process-impact/); [GamesRadar+](https://www.gamesradar.com/games/sports/ea-boss-doubles-down-on-commitment-to-ai-believes-more-than-50-of-our-development-process-will-be-impacted/)

**US — Microsoft / Xbox:**
- **Muse (Feb 2025):** a World and Human Action Model (WHAM) built with Ninja Theory. It was trained on *Bleeding Edge* gameplay (~7 years of continuous human play) and published in *Nature*. — [Microsoft Research](https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/); [Xbox Wire](https://news.xbox.com/en-us/2025/02/19/muse-ai-xbox-empowering-creators-and-players/)
- **WHAMM (Apr 2025):** a real-time version. A Quake II demo trained on about one week of data runs at 640×360 in the browser via Copilot for Gaming. — [Microsoft Research WHAMM](https://www.microsoft.com/en-us/research/articles/whamm-real-time-world-modelling-of-interactive-environments/); [WinBuzzer](https://winbuzzer.com/2025/04/05/microsofts-ai-powered-quake-ii-demo-signals-a-shift-in-game-development-tools-xcxwbn/); [PC Gamer (critical)](https://www.pcgamer.com/software/ai/microsoft-unveils-ai-generated-demo-inspired-by-quake-2-that-runs-worse-than-doom-on-a-calculator-made-me-nauseous-and-demanded-untold-dollars-energy-and-research-to-make/)

**Microsoft-owned King (Candy Crush), July 2025:**
- About 200 layoffs. Reportedly, level designers who had spent months building AI level-design tools were replaced by those tools, and copywriters faced the same.
- Cuts hit level design, user research, UX and narrative writing in London, Barcelona, Stockholm and Berlin. The *Farm Heroes Saga* team lost ~50.
- This comes from sources, not company confirmation.
- Sources: [Mobilegamer.biz](https://mobilegamer.biz/laid-off-king-staff-set-to-be-replaced-by-the-ai-tools-they-helped-build-say-sources/); [Engadget](https://www.engadget.com/gaming/laid-off-candy-crush-studio-staff-reportedly-replaced-by-the-ai-tools-they-helped-build-174141524.html); [Game Developer](https://www.gamedeveloper.com/business/report-candy-crush-maker-king-is-allegedly-replacing-employees-with-internal-ai-tools)

**Microsoft-owned Activision:** *Black Ops 7* carries a Steam gen-AI disclosure for "some in game assets" (see section 2). — [PCGamesN](https://www.pcgamesn.com/call-of-duty-black-ops-7/ai-assets-steam-disclosure)

**France — Ubisoft:**
- NEO NPC (March 2024) showed conversational NPCs in static environments.
- **Teammates (Nov 2025)** is Ubisoft's first playable gen-AI research project:
  - An AI assistant (Jaspar) and two voice-commanded squad NPCs.
  - Built by a team of **80** using Google Gemini plus internal middleware, with an API that embeds guardrails.
  - Closed testing with **300 players** from Oct 29.
- Sources: [Ubisoft News](https://news.ubisoft.com/en-us/article/3mWlITIuWuu0MoVuR6o8ps/ubisoft-reveals-teammates-an-ai-experiment-to-change-the-game); [Variety](https://variety.com/2025/gaming/news/ubisoft-generative-ai-game-teammates-neo-npc-developers-1236588038/); [AI and Games](https://www.aiandgames.com/p/ubisofts-teammates-demo-and-their)

**Services / co-development vendors:**
- **Virtuos** (July 2025) laid off ~270 staff, 7% of its workforce: ~200 in Asia and ~70 in Europe. The company employs 4,200+.
  - The stated reason was "lower occupancy and slower demand due to structural shifts in the industry."
  - Sources say it is exploring gen AI with mandatory training.
  - Sources: [Engadget](https://www.engadget.com/gaming/virtuos-the-studio-behind-oblivion-remastered-is-laying-off-around-270-employees-135722222.html); [Game Developer](https://www.gamedeveloper.com/business/virtuos-confirms-layoffs-affecting-270-roles-across-asia-and-europe); [PocketGamer.biz](https://www.pocketgamer.biz/virtuos-lays-off-270-employees/)
- **Keywords Studios:** see section 6.

### Inferences
- **Player-facing gen AI in premium Western titles draws backlash**, and companies partially retreat: Embark re-recorded lines, and Activision faced criticism over BO7. The Western frontier is therefore internal and back-end work (QA automation, code, prototyping), plus experimental runtime-AI prototypes, rather than final art.
- **Two firm targets and one strategic commitment stand out:** Square Enix's 70% QA target, EA's "60% of processes" and Krafton's AI-first program. None of them yet reports a *measured* outcome.
- **Microsoft's world-model work is research-grade**, not a production pipeline tool (640×360 demo; PC Gamer's critical review).
- **Headcount substitution shows up first in casual/mobile content roles** (King's level design and copy) and in **outsourced services** (Virtuos' "lower occupancy"), not in AAA core teams (inference).

### Gaps
The following leads could **not** be verified in this session (search budget exhausted and fetch blocked). Check them before use; no figures are given here on purpose.
- Nexon CEO Junghun Lee's widely reported late-2025 remark that one should assume every game company now uses AI.
- EA's partnership with Stability AI (reported October 2025) and reports of EA's internal AI tooling push.
- Epic's AI-voiced Darth Vader in Fortnite (2025) and the related SAG-AFTRA unfair-labor-practice charge.
- Roblox's Cube 3D model and Assistant usage metrics.
- Unity's move from Muse to "Unity AI".
- Sony/PlayStation AI prototypes and statements.
- Capcom's reported use of LLMs for idea generation.
- Level-5's AI use in code and art.
- Take-Two's AI statements.
- Nintendo's stance.
- NCSoft (VARCO) and Netmarble.
- Krafton's inZOI "Smart Zoi" / PUBG Ally (NVIDIA ACE) and any Krafton workforce measures.
- Ubisoft Ghostwriter (2023).
- Microsoft's 2025 company-wide layoffs and their Xbox share.

---

## 6. Pre-AI structure of game production: cost, headcount, time by discipline; outsourcing

### Takeaway
There are no audited, public discipline-level cost splits. The evidence base is:
- **Leaked or court-disclosed budgets:** *Spider-Man 2* $315M; *Horizon Forbidden West* $212M; *Cyberpunk 2077* ~$316M; *Spider-Man 3* planned at $385M.
- **Vendor rules of thumb:**
  - AAA budgets are $200M+ for 2024–25 releases.
  - Development is 40–50% of total budget, with ~70% of it payroll.
  - Art production is 25–30%, and marketing 20–25%.
  - Testing takes 15–20% of development time.
- **Long cycles:** ~5 to 6–8 years for AAA, reportedly ~40% longer in the ninth console generation.
- **An exposed services layer:** Keywords Studios ~$0.88B revenue in 2024, Virtuos 4,200+ staff, and third-party estimates of a ~$9B outsourcing market in 2025.

### Cited Findings
- **Leaked and disclosed budgets:**
  - The Insomniac leak (Dec 2023) showed *Marvel's Spider-Man 2* at **$315M** with 10.5M expected sales, and **$385M** planned for the third game. — [Game World Observer](https://gameworldobserver.com/2023/12/19/playstation-pc-game-sales-leak-insomniac-budgets-roi); [WN Hub](https://wnhub.io/news/investment/item-42610); [MP1st](https://mp1st.com/news/marvels-spider-man-2-budget-was-315-million-leaks-reveal)
  - *Horizon Forbidden West* cost **$212M** (FTC v. Microsoft documents). *Cyberpunk 2077*'s total budget was ~**$316M**. — [MP1st](https://mp1st.com/news/marvels-spider-man-2-budget-was-315-million-leaks-reveal); [Game World Observer](https://gameworldobserver.com/2023/12/19/playstation-pc-game-sales-leak-insomniac-budgets-roi)
- **Vendor/consultancy estimates (not audited; treat as rules of thumb):**
  - $100M is a rough floor for modern AAA excluding marketing. Budgets used to range $50–150M; 2024–2025 releases see "$200 million and higher".
  - Development is 40–50% of the budget and covers programmers, artists, level designers and animators over 3–5 years.
  - Art production (3D characters, environments, weapons, vehicles, textures, effects, cinematics) is 25–30%.
  - Marketing is 20–25%.
  - Roughly 70% of the development half is payroll, "which is why a schedule slip and a budget overrun are the same event."
  - Testing takes 15–20% of total development time.
  - Sources: [Innovecs Games](https://www.innovecsgames.com/blog/aaa-game-development-cost/); [Cubix](https://www.cubix.co/blog/game-development-cost-guide/); [DEV Community](https://dev.to/oceanviewgames/game-development-budget-breakdown-where-does-the-money-go-ao1); [VSQUAD](https://vsquad.art/blog/what-is-a-aaa-game-the-reality-of-the-aaa-game-budget)
- **Team size:** AAA core teams typically run 200–1,000 people. Big titles involve 2,000–3,000 contributors, including outsourcing, localization, QA and marketing. — [Innovecs Games](https://www.innovecsgames.com/blog/what-are-aaa-games/); [Game Rant](https://gamerant.com/aaa-games-most-developers/) (weak sources)
- **Cycle length:**
  - Around 5 years on average for large AAA; many now take 6–8 years.
  - Examples: *Horizon Zero Dawn* (2011 → 2017), *Red Dead Redemption 2* (2010 → 2018).
  - AAA games reportedly took ~40% longer in the ninth generation than the eighth.
  - Annualized franchises like Call of Duty run ~2-year cycles on shared tech.
  - Sources: [GamerBraves newsletter](https://gamerbraves.substack.com/p/gamerbraves-newsletter-vol-118-why); [ResetEra thread](https://www.resetera.com/threads/it-takes-6-to-8-years-for-most-aaa-games-now-how-does-that-make-you-feel.626929/); [Juego Studio](https://www.juegostudio.com/blog/how-long-does-it-take-to-develop-video-game) (low-to-medium quality; original data source for "40%" not verified)
- **Content volume, one data point:** EA's *FC 24* run cycles went from 12 to 1,200 with ML/gen-AI assistance. — [Game Developer](https://www.gamedeveloper.com/production/ea-ceo-60-percent-of-dev-processes-could-be-impacted-by-generative-ai-)
- **Outsourcing and services:**
  - **Keywords Studios:**
    - Segments: Create (concept art, 2D/3D assets, animation, co-development, porting), Globalize (audio, testing, localization) and Engage (trailers, PR, community management).
    - 2024 revenue: ~$879.2M vs ~$842.6M in 2023, with a net loss of ~$56.9M. Keywords reports in EUR; these figures are MarketScreener's USD conversions.
    - H1 2024 revenue: +7% to ~$440M, with organic growth of −2%.
    - Performance was hit by "ongoing challenges in Globalize" and a "more muted performance in Create", offset by Engage.
    - Sources: [MarketScreener FY2024](https://www.marketscreener.com/quote/stock/KEYWORDS-STUDIOS-PLC-13612097/news/Keywords-Studios-plc-Reports-Earnings-Results-for-the-Full-Year-Ended-December-31-2024-50399246/); [Investegate interim results](https://www.investegate.co.uk/announcement/rns/keywords-studios--kws/interim-results-/8417319); [MarketScreener H1](https://www.marketscreener.com/quote/stock/KEYWORDS-STUDIOS-PLC-13612097/news/Keywords-Studios-Reports-19-Growth-in-H1-Revenue-44477229/)
  - **Virtuos:** 4,200+ employees; 7% cut in 2025 (see section 5). — [Engadget](https://www.engadget.com/gaming/virtuos-the-studio-behind-oblivion-remastered-is-laying-off-around-270-employees-135722222.html)
  - **Third-party market estimates (low quality; they disagree on scope):**
    - "Game outsourcing service market" ~$9.15–9.18B in 2025, forecast at ~$25B by 2034–35.
    - Asia-Pacific ~$4.8B in 2025.
    - Mobile game-dev outsourcing ~$5.08B in 2025.
    - Sources: [Verified Market Reports](https://www.verifiedmarketreports.com/product/game-outsourcing-service-market/); [WiseGuy Reports](https://www.wiseguyreports.com/reports/game-outsourcing-service-market); [Market.us](https://market.us/report/game-outsourcing-services-market/); [Market Research Intellect](https://www.marketresearchintellect.com/product/mobile-game-development-outsourcing-market/)
- **China market structure:** mobile is 73.29% of China's ¥350.8B market (2025). This shapes the discipline mix toward 2D character art, live-ops content and UA creatives. — [IT之家](https://www.ithome.com/0/906/428.htm)

### Inferences
- **Order-of-magnitude art spend.** Applying the vendor rule of thumb (art ≈25–30% of total budget) to $200–315M AAA budgets implies roughly **$50–95M of art spend per AAA title**. This is illustrative arithmetic, not sourced data.
- **Why single-discipline gains look small at the budget level.** Development spend is mostly payroll, so AI savings arrive as fewer person-months or shorter schedules. A 50% productivity gain confined to art (25–30% of budget) is worth ≤12.5–15% of total budget, and less if marketing is included. Budget-level impact requires gains across several disciplines, or schedule compression (inference).
- **Outsourced services are the marginal capacity layer.** Art outsourcing, QA and localization are therefore the first place AI substitution shows up in revenue and headcount. Examples: Keywords' Globalize (testing, localization, audio) weakness in 2024, Virtuos' "lower occupancy" in 2025, and Chinese outsourced-art price compression in 2023. Weak demand after the post-pandemic boom is a confounder, and the sources do not isolate AI.

### Gaps
- No authoritative headcount-by-discipline data was found for AAA, mobile or live-service teams (e.g., % artists vs engineers vs designers vs QA).
- No mobile/live-service cost split was found (e.g., live-ops content vs UA spend). No live-ops update-cadence or asset-count trend data (e.g., assets per title across console generations) was found.
- No verified Call of Duty budgets were found.
- No reliable, methodology-transparent outsourcing market size was found; the market-research figures above conflict and are low quality.
- No China-specific cost-by-discipline data was found.

---

## 7. Labor-market impacts: layoffs, AI attribution, hiring, SAG-AFTRA 2025, outsourcing and junior art roles

### Takeaway
**Scale of layoffs:**
- Trackers estimate ~10,500 layoffs in 2023 and ~14,600 in 2024 (the peak).
- 2025 is lower in at least one tracker (~5,300), but trackers disagree.
- ~45,000 jobs were lost from 2022 to mid-2025.
- GDC 2026: **28% of respondents were laid off in the past two years (33% in the US)**.

**AI attribution is mostly indirect.** The layoff wave predates production-scale gen AI, and explicit AI attribution is rare. King (July 2025) is the clearest reported case. AI effects show up more clearly in the outsourcing layer, in Chinese 2D illustration demand, and in labor contracts. The SAG-AFTRA 2025 Interactive Media Agreement (95% approval, July 9, 2025) adds consent and disclosure rules plus compensation minimums for digital replicas.

### Cited Findings
- **Layoff totals:**
  - ~10,500 people lost jobs in 2023, and ~14,600 in 2024. One tracker estimates ~5,300 in 2025.
  - ~45,000 jobs were lost from 2022 to July 2025. A MAGES Institute compilation puts 2022–2026 at ~58,494.
  - Trackers differ in scope, so treat as estimates. — [GameDev Reports (2023: 10,526)](https://gamedevreports.substack.com/p/game-industry-layoffs-10526-people); [VG Layoffs tracker 2025](https://publish.obsidian.md/vg-layoffs/Archive/2025); [Wikipedia](https://en.wikipedia.org/wiki/2022%E2%80%932026_video_game_industry_layoffs); [ShaneTheGamer](https://www.shanethegamer.com/research/game-industry-layoffs/); [Udonis](https://www.blog.udonis.co/mobile-marketing/mobile-games/game-industry-layoffs); [Gaming Layoffs 2026](https://gaminglayoffs.com/)
- **GDC 2026 layoff findings:**
  - 28% of respondents were laid off in the past two years (33% in the US).
  - Half said their current or most recent employer had conducted layoffs in the past 12 months.
  - Game designers were the most affected profession (20%); services and business functions were least affected (8%).
  - Two-thirds of AAA respondents reported layoffs at their company, vs one-third at indies.
  - 48% of those laid off had not found a new job.
  - Sources: [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [Variety](https://variety.com/2026/gaming/news/one-third-video-game-workers-laid-off-2025-1236644512/); [PC Gamer](https://www.pcgamer.com/gaming-industry/one-third-of-us-games-industry-workers-were-laid-off-in-the-last-2-years-gdc-survey-says/)
- **Explicit or reported AI-linked cuts:**
  - King: ~200 roles in July 2025, with level designers and copywriters reportedly replaced by the AI tools they built. — [Mobilegamer.biz](https://mobilegamer.biz/laid-off-king-staff-set-to-be-replaced-by-the-ai-tools-they-helped-build-say-sources/)
  - Virtuos: ~270 roles citing "structural shifts", plus reported gen-AI training mandates. — [Game Developer](https://www.gamedeveloper.com/business/virtuos-confirms-layoffs-affecting-270-roles-across-asia-and-europe)
- **China illustrators and outsourcing:**
  - Illustrator openings fell ~70% (recruiter estimate, 2023, with mixed causes). — [Rest of World](https://restofworld.org/2023/ai-china-video-game-layoffs-illustrators/)
  - Outsourced concept-art prices plunged, and some foreign clients banned AI. — [GameLook](http://www.gamelook.com.cn/2023/04/514084/)
  - Reported per-character price fell from ¥8,000 to ¥2,000. — [Jiemian](https://www.jiemian.com/article/9548103.html)
  - Low-reliability claim: art roles were hit hardest in 2025. — [Zhihu/7.GAME](https://zhuanlan.zhihu.com/p/2029904588564898253)
- **SAG-AFTRA 2025 Interactive Media (Video Game) Agreement:**
  - Approved by members with **95% in favor on July 9, 2025**.
  - Requires informed consent and disclosure for AI digital-replica use. Producers must give a "reasonably specific description" of intended use.
  - Performers can **suspend consent** for generating new material during a strike.
  - Sets collectively bargained minimums for digital replicas made from IMA-covered performances, with **7.5x scale for "Real Time Generation"**.
  - Sources: [SAG-AFTRA](https://www.sagaftra.org/sag-aftra-members-approve-2025-video-game-agreement); [SAG-AFTRA IMA page](https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement); [Frankfurt Kurnit (FKKS)](https://technologylaw.fkks.com/post/102mewu/inside-the-new-sag-aftra-interactive-media-agreement-new-standards-for-ai-and-di); [Davis+Gilbert](https://www.dglaw.com/sag-aftras-new-video-game-agreement/)
- **Voice practice under the new terms:** Embark paid actors to license voices for TTS, then re-recorded some lines after backlash. — [Engadget](https://www.engadget.com/gaming/arc-raiders-replaced-some-of-its-ai-generated-voice-lines-with-professional-actors-184915627.html)
- **Hiring counter-signal:** Giant Network increased technical staff by 117 in 2025 while expanding AI. — [Tencent News](https://news.qq.com/rain/a/20260421A0207F00)

### Inferences
- **Layoffs peaked in 2024, before production-scale gen AI.** The 2023–24 layoff peak came before most production-scale AI pipelines were claimed (2025–26). The main drivers were post-pandemic over-hiring and a capital-cost reset (context, not sourced here). AI's labor effect is therefore better seen as:
  - (a) Structural pressure on services and outsourcing (art, QA, localization, audio).
  - (b) Selective substitution in casual/mobile content roles (level design, copy) and in 2D illustration, especially in China.
  - (c) Reduced backfilling rather than mass AI-attributed layoffs.
- **Contracts cover voice, not art.** The SAG-AFTRA terms (consent, strike suspension, 7.5x real-time generation scale) raise the cost and friction of AI voice replicas for covered US productions. Nothing comparable protects 2D/3D artists, which is consistent with art being the discipline where substitution evidence is strongest.

### Gaps
- **No job-posting trend data was found** for artists vs engineers, in the West (e.g., Hitmarker, Indeed) or in China. This is an important unanswered question.
- The Xbox share of Microsoft's 2025 company-wide cuts, and any AI attribution for them, were not verified.
- **Unverified lead:** the SAG-AFTRA video-game strike start and end dates (commonly cited as July 2024 to mid-2025, about 11 months) and the agreement's wage increases.
- No Japanese or Korean labor data was found (e.g., Krafton or Square Enix headcount changes linked to AI).
- No independent data was found on junior-role hiring (entry-level art or QA) in any region.

---

## 8. Where AI is measurably adopted vs not, and claimed/measured gains per discipline (with summary table)

### Takeaway
**Where adoption is deepest:**
1. Non-shipping, text-centric work: research and brainstorming (81% of GDC 2026 AI users), email and admin, code assistance (47–62%), and market research.
2. Prototyping, placeholder and "auxiliary" content.
3. In China, 2D art and UA/marketing creatives at production scale, with 3D assets ramping up.

**Where it is thinnest:** final hero assets in Western AAA, performance-driven voice and animation under union terms, and VFX, where no data was found.

**Quality of the gain evidence:** almost all efficiency evidence is company-claimed or self-reported. Examples:
- Tencent: 3x modeling speed (internal test).
- 37 Games: 60–80% of concept-art hours saved.
- GiiNEX: city generation cut from 5 days to 25 minutes.
- NetEase: +300% in some stages.
- EA: 6 weeks → 6 days.
- 伽马数据: ~80% perceive >20% efficiency.

**No independent controlled study of game-production productivity was found.**

### Cited Findings
- **Programming:**
  - Coding assistance is the top AI use in Unity 2026 (62%). It is used by 47% of GDC 2026 AI users and was 37% in Unity 2024. — [Unity](https://unity.com/blog/2026-unity-game-development-report-trends); [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [Game Developer](https://www.gamedeveloper.com/production/unity-2024-gaming-report-indicates-62-percent-of-devs-are-currently-using-ai-tools)
  - It is exempt from Steam disclosure from January 2026. — [GameSpot](https://www.gamespot.com/articles/valve-updates-ai-disclosure-guidelines-to-allow-for-ai-powered-tools/1100-6537483/)
- **Prototyping and ideation:**
  - 35% of GDC 2026 AI users use AI for prototyping. — [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)
  - 68% of Unity 2024 respondents say AI speeds up prototyping. — [Creative Bloq](https://www.creativebloq.com/news/unity-gaming-report-2024-ai-impact)
  - Steam developers use AI for placeholder art, voices and ideas. — [Totally Human](https://www.totallyhuman.io/blog/games-with-ai-disclosures-have-grossed-an-estimated-660m-on-steam)
  - Microsoft positions Muse for "gameplay ideation". — [Microsoft Research](https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/)
- **2D/3D art:** see the section 4 figures (37 Games, Tencent Hunyuan 3D, GiiNEX, 伽马数据 ~50% for concept art). About 60% of Steam disclosures involve visual assets. — [Tom's Hardware](https://www.tomshardware.com/video-games/pc-gaming/1-in-5-steam-games-released-in-2025-use-generative-ai-up-nearly-700-percent-year-on-year-7-818-titles-disclose-genai-asset-usage-7-percent-of-entire-steam-library)
- **Animation:**
  - 46% of AI-using studios in Unity 2024 used it for character animation. — [Game Developer](https://www.gamedeveloper.com/production/unity-2024-gaming-report-indicates-62-percent-of-devs-are-currently-using-ai-tools)
  - EA's run cycles went from 12 to 1,200. — [Game Developer](https://www.gamedeveloper.com/production/ea-ceo-60-percent-of-dev-processes-could-be-impacted-by-generative-ai-)
- **QA:**
  - Automated testing is a leading AI area in Unity 2025, and 35% of Unity 2026 respondents use AI for automated playtesting. — [Gamereactor](https://www.gamereactor.eu/96-of-game-developers-are-integrating-ai-tools-into-their-workflow-according-to-unity-1516063); [Unity](https://unity.com/blog/2026-unity-game-development-report-trends)
  - Square Enix targets 70% by end-2027. — [VGC](https://www.videogameschronicle.com/news/square-enix-says-it-wants-generative-ai-to-be-doing-70-of-its-qa-and-debugging-by-the-end-of-2027/)
- **Localization:**
  - A leading automation area in Unity 2025. — [Mobile Marketing Reads](https://www.mobilemarketingreads.com/2025-unity-gaming-report/)
  - Steam developers cite affordable localization and multilingual voice-over. — [Totally Human](https://www.totallyhuman.io/blog/games-with-ai-disclosures-have-grossed-an-estimated-660m-on-steam)
- **Narrative:**
  - 44% of Unity 2026 respondents use AI for narrative and writing. — [Unity](https://unity.com/blog/2026-unity-game-development-report-trends)
  - King's copywriters were reportedly replaced. — [Mobilegamer.biz](https://mobilegamer.biz/laid-off-king-staff-set-to-be-replaced-by-the-ai-tools-they-helped-build-say-sources/)
- **Runtime AI and live-ops:**
  - Among AI-agent users: content optimization 44%, dynamic balancing 38%, procedural world generation 37%, automated moderation 37%. — [Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research)
  - *Justice Mobile*: 5M+ player-created AI NPCs in 3 days. — [IT之家](https://www.ithome.com/0/791/380.htm)
  - *Supernatural Action Group*: 10M+ DAU with LLM NPCs. — [Tencent News](https://news.qq.com/rain/a/20260421A0207F00)
  - NPC behaviour: 40% of Unity 2026 respondents. — [Unity](https://unity.com/blog/2026-unity-game-development-report-trends)
- **Marketing and UA:**
  - At 37 Games, AI participates in ~70% of video material. — [Tencent News](https://news.qq.com/rain/a/20251210A07R6E00?media_id=&suid=)
  - Community, marketing and PR roles: 39% use (GDC 2025). — [GDC 2025](https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/)
  - Tencent cites improved marketing effectiveness. — [Xinhua](http://www.news.cn/tech/20260318/f8dd0672c8554770b9d3bffdf783c7c1/c.html)

### Inferences
- **Extrapolating from LLM coding penetration to game production:**
  - Code is the most-adopted *production* use in Western game-dev surveys, mirroring general software.
  - But in content-heavy games, programming is not the dominant cost line. Art and content (~25–30% of total budget by vendor rule of thumb), plus outsourced QA and localization, are larger or equally exposed.
  - So the size of AI's impact on game-production cost depends far more on penetration of art, content and services than on coding.
  - That penetration is (a) already high in China's mobile pipelines, (b) growing fast in indie and long-tail Steam content, and (c) constrained in Western AAA by worker sentiment, player backlash, IP risk, disclosure rules and union contracts.
- **Most "gains" are throughput or time metrics on narrow tasks** (hours per model, days per city), not total project cost or headcount. Converting task-level speed-ups into project-level savings requires assumptions about the task's share of the pipeline and about rework and review costs, and none of the sources report those.
- **Where evidence is strongest:** 2D concept art (multiple independent Chinese sources plus outsourcing price data) and code assistance (consistent survey usage). **Where it is weakest:** VFX, player support, and audio beyond TTS.

### Gaps
- No independent, controlled productivity studies were found for any game discipline.
- No VFX-specific adoption or gain data was found.
- Player-support data is thin: only Google's moderation figure and Tencent's AICoaching.
- No per-discipline adoption rates from an *independent* multi-region survey were found (GDC reports tasks, not disciplines × adoption).
- No measured outcome yet for Square Enix's QA target, EA's 60% claim or Krafton's AI-first program.

### Summary table: discipline × current adoption × evidence of gains × main blockers (as of Sept 2026)

*Adoption levels are the researcher's judgment from the cited evidence. The evidence type is marked [T] internal test, [C] company claim, [S] survey self-report, [Tgt] target, [A] anecdote/press.*

| Discipline / pipeline stage | Current AI adoption level | Evidence of measured or claimed gains | Main blockers |
|---|---|---|---|
| Programming / engineering | **High, and the most common production use in Western surveys.** Unity 2026 62% ([Unity](https://unity.com/blog/2026-unity-game-development-report-trends)); GDC 2026 47% of AI users ([GDC](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)). Invisible in Steam data since the Jan 2026 exemption ([GameSpot](https://www.gamespot.com/articles/valve-updates-ai-disclosure-guidelines-to-allow-for-ai-powered-tools/1100-6537483/)). | Only [S]: "greater efficiency" 73% (Unity 2026). No game-specific measured productivity data. | 59% of programmers view gen AI negatively ([80.lv](https://80.lv/articles/gdc-survey-over-50-of-game-devs-say-generative-ai-harms-industry)); data-ownership concerns 63% ([Techmeme](https://www.techmeme.com/250818/p11)); proprietary engine and legacy code (inference). |
| Concept art / 2D illustration | **China: High.** 37 Games >80% of 2D assets AI-generated; art-stage application >80% claimed ([Tencent News](https://news.qq.com/rain/a/20251210A07R6E00?media_id=&suid=); [Sina](https://finance.sina.com.cn/tech/roll/2026-08-01/doc-inikvnzz3648216.shtml)). **West: Medium in indie** (~60% of Steam disclosures are visual; [Tom's Hardware](https://www.tomshardware.com/video-games/pc-gaming/1-in-5-steam-games-released-in-2025-use-generative-ai-up-nearly-700-percent-year-on-year-7-818-titles-disclose-genai-asset-usage-7-percent-of-entire-steam-library)), **Low and contested in AAA** (BO7 backlash; [PC Gamer](https://www.pcgamer.com/games/call-of-duty/call-of-duty-black-ops-7-under-fire-for-using-what-sure-looks-like-ai-generated-studio-ghibli-style-calling-card-art/)). | [C] 60–80% of hours saved in character concept art (37 Games). [S/C] ~50% concept-art efficiency (伽马数据 2024; [Tencent News](https://news.qq.com/rain/a/20240626A03QMV00)). [A] Outsourced character design ¥8,000 → ¥2,000 ([Jiemian](https://www.jiemian.com/article/9548103.html)). | Artist opposition (64% of visual/tech art negative); consumer backlash and Steam disclosure; IP/copyright; some clients ban AI in outsourced art ([GameLook](http://www.gamelook.com.cn/2023/04/514084/)). |
| 3D modeling / environment & props | **Medium, entering production at Chinese majors.** Hunyuan 3D in dozens of Tencent projects ([BAAI](https://hub.baai.ac.cn/view/49146)); 37 Games 3D assistance >30%. Unity 2025 lists asset creation as a top use ([Gamereactor](https://www.gamereactor.eu/96-of-game-developers-are-integrating-ai-tools-into-their-workflow-according-to-unity-1516063)). | [T] Modeling 8h → 2.5h, prop iteration −60%, reuse +50% (Tencent). [C] City 5 days → 25 min and building exteriors 50x (GiiNEX; [Sohu](https://www.sohu.com/a/875925906_122004016)). | Production-readiness and style consistency (inference, not sourced); artist sentiment. |
| Animation | **Medium.** 46% of AI-using studios (Unity 2024; [Game Developer](https://www.gamedeveloper.com/production/unity-2024-gaming-report-indicates-62-percent-of-devs-are-currently-using-ai-tools)); animation is in NetEase's AI pipeline ([iiMedia](https://www.iimedia.cn/c1040/109721.html)). | [C] EA run cycles 12 → 1,200 ([Game Developer](https://www.gamedeveloper.com/production/ea-ceo-60-percent-of-dev-processes-could-be-impacted-by-generative-ai-)). [C] NetEase "some stages +300%" (not stage-specific). | Performer and digital-replica terms ([SAG-AFTRA](https://www.sagaftra.org/sag-aftra-members-approve-2025-video-game-agreement)); hero-quality bar (inference). |
| VFX | **Unknown / Low.** No data found. | None found. | Gap. |
| Level / world design | **Medium in casual/mobile and procedural content.** King's AI level-design tools ([Mobilegamer.biz](https://mobilegamer.biz/laid-off-king-staff-set-to-be-replaced-by-the-ai-tools-they-helped-build-say-sources/)); 37% of AI-agent users do procedural world generation ([Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research)); level design is in NetEase's AI pipeline. | [C] GiiNEX city generation 5 days → 25 min. [A] King ~200 layoffs including level designers. | Designer sentiment (63% of design and narrative negative); judging "fun" and quality (inference). |
| Narrative / writing | **Medium for back-end and secondary text.** Unity 2026 44% ([Unity](https://unity.com/blog/2026-unity-game-development-report-trends)); LLM text in Steam disclosures ([Tom's Hardware](https://www.tomshardware.com/video-games/pc-gaming/1-in-5-steam-games-released-in-2025-use-generative-ai-up-nearly-700-percent-year-on-year-7-818-titles-disclose-genai-asset-usage-7-percent-of-entire-steam-library)); King copywriters reportedly replaced. | None measured. | 63% of design and narrative staff negative; player backlash; quality. |
| Audio / voice | **Medium for prototyping and secondary lines.** Embark TTS in The Finals and ARC Raiders ([Engadget](https://www.engadget.com/gaming/arc-raiders-replaced-some-of-its-ai-generated-voice-lines-with-professional-actors-184915627.html)); Steam developers cite AI voice-over ([Totally Human](https://www.totallyhuman.io/blog/games-with-ai-disclosures-have-grossed-an-estimated-660m-on-steam)); audio is in NetEase's AI pipeline. | None quantified. Embark re-recorded lines, citing a quality gap. | SAG-AFTRA 2025 IMA consent and disclosure, strike-time consent suspension, 7.5x scale for real-time generation ([FKKS](https://technologylaw.fkks.com/post/102mewu/inside-the-new-sag-aftra-interactive-media-agreement-new-standards-for-ai-and-di)); player backlash. |
| QA / testing | **Medium and rising.** Automated testing is a top use (Unity 2025); 35% automated playtesting (Unity 2026); testing is in NetEase's AI pipeline. | [Tgt] Square Enix 70% of QA and debugging by end-2027 ([VGC](https://www.videogameschronicle.com/news/square-enix-says-it-wants-generative-ai-to-be-doing-70-of-its-qa-and-debugging-by-the-end-of-2027/)). Testing takes ~15–20% of dev time (vendor estimate; [Innovecs](https://www.innovecsgames.com/blog/aaa-game-development-cost/)). | Reliability of automated agents; no outcome data yet; vendor contracts. Keywords' Globalize weakness suggests demand shifts ([MarketScreener](https://www.marketscreener.com/quote/stock/KEYWORDS-STUDIOS-PLC-13612097/news/Keywords-Studios-plc-Reports-Earnings-Results-for-the-Full-Year-Ended-December-31-2024-50399246/)). |
| Localization | **Medium–High.** A leading automation area (Unity 2025; [Mobile Marketing Reads](https://www.mobilemarketingreads.com/2025-unity-gaming-report/)); Steam developers say AI makes localization and multilingual VO affordable. | None measured. Keywords' Globalize segment (audio, testing, localization) had "ongoing challenges" in 2024, with AI not isolated. | Quality for narrative-heavy or culturally sensitive text; voice-actor terms for dubbed VO. |
| Live-ops content / runtime AI (NPCs, balancing) | **Medium.** Among AI-agent users, content optimization 44% and dynamic balancing 38% ([Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research)); NPC behaviour 40% (Unity 2026). China: *Justice Mobile* 5M+ AI NPCs ([IT之家](https://www.ithome.com/0/791/380.htm)); *Supernatural Action Group* 10M+ DAU ([Tencent News](https://news.qq.com/rain/a/20260421A0207F00)). West: Ubisoft Teammates prototype with 300 testers ([Ubisoft](https://news.ubisoft.com/en-us/article/3mWlITIuWuu0MoVuR6o8ps/ubisoft-reveals-teammates-an-ai-experiment-to-change-the-game)). | Engagement or cost effects not isolated. | Inference cost and safety guardrails; Valve's runtime-generation disclosure rules ([Notebookcheck](https://www.notebookcheck.net/Steam-updates-AI-disclosure-form-requiring-developers-to-report-visible-and-in-game-AI-but-not-background-tools.1206103.0.html)); SAG-AFTRA real-time generation terms; player acceptance. |
| Marketing / UA creatives | **High in Chinese mobile.** 37 Games: AI in ~70% of video material ([Tencent News](https://news.qq.com/rain/a/20251210A07R6E00?media_id=&suid=)). **Medium in the West:** 39% of community, marketing and PR staff use gen AI (GDC 2025). Tencent cites improved marketing effectiveness ([Xinhua](http://www.news.cn/tech/20260318/f8dd0672c8554770b9d3bffdf783c7c1/c.html)). | [C] Share-of-output only; no cost-per-creative or ROAS data found. | Brand risk and backlash (inference); no data on ad-platform policies. |
| Player support / community / moderation | **Low–Medium.** 37% of AI-agent users automate content moderation ([Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research)); Tencent AICoaching for *Honor of Kings* ([Sohu](https://www.sohu.com/a/875925906_122004016)). | None found. | Sparse data (gap). |
| Business / production / research (non-craft, for context) | **High.** Business and finance 51%, production and leadership 41% (GDC 2025; [GDC](https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/)); research and brainstorming 81% of AI users (GDC 2026); market research 37% (Unity 2026). | [S] only. | Few; these roles are the least negative (19% positive in business/services, GDC 2026). |
