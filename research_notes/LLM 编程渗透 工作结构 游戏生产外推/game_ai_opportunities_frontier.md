# AI in Games: Frontier, Value Pools and Opportunity Map (status as of late September 2026)

_How this was researched: 2026-09-28. The session-wide WebSearch budget (200 calls, shared with the parallel researchers) ran out partway through. WebFetch was blocked by the egress proxy for almost every domain tried, including sec.gov, techcrunch.com, wikipedia.org, naavik.co, unity.com, cac.gov.cn, copyright.gov, artificialintelligenceact.eu and thenextweb.com. As a result, **the findings below come from search-engine result summaries of the linked pages, not from reading the full pages.** Figures that appear the same across several results are more reliable. Where a summary looked internally inconsistent, it is flagged. Sections 6 (risks) and 7 (forecasts) could only be partly researched. Their Gaps sections list "UNVERIFIED LEADS" from the model's background knowledge (cutoff mid-2026). These are not findings and must not be cited without a source._

---

## 1. AI-native games and AI features (NPCs, companions, co-players): traction and recurring problems

### Takeaway
The only AI-NPC deployments that reach tens of millions of players are **features inside big incumbent live games**: NetEase Justice Mobile and Where Winds Meet, Krafton inZOI and PUBG Ally, and Fortnite's creator NPCs. Standalone "AI-native" games reliably get **viral attention but modest sales**. AI companion platforms make more money but face heavy safety and regulatory pressure. Cost, controllability and safety are pushing designs toward on-device small models, cheap "flash/lite" cloud models and tight content rules.

### Cited Findings
**Incumbent-embedded AI NPCs (largest reach)**
- **NetEase Justice Mobile (逆水寒手游).** NetEase marketed it as the first game with an in-game "游戏GPT" (2023). In "逆水寒GPT", NPC dialogue text, expressions, voice and camera work are all AI-generated. Players can talk to NPCs by text or voice — [游侠网](https://www.ali213.net/news/html/2023-2/739377.html); [游戏陀螺](https://www.youxituoluo.com/530350.html)
- Justice's NPC model was pre-trained mostly on wuxia novels, history books and classical poetry. The aim was to keep NPCs "in character" as people of the Song-dynasty martial-arts world and avoid breaking immersion. This is an early example of constraining a model through its data for controllability — [游戏陀螺](https://www.youxituoluo.com/530350.html)
- Justice later added player-created AI NPCs (the "捏 AI 江湖友人" mode, Feb 2024) — [AI旋风](https://www.aixuanfeng.com/2024/02/%E7%8E%A9%E5%AE%B6%E8%87%AA%E5%B7%B1%E6%89%93%E9%80%A0-npc%EF%BC%9A%E7%BD%91%E6%98%93%E3%80%8A%E9%80%86%E6%B0%B4%E5%AF%92%E3%80%8B%E6%8D%8F-ai-%E6%B1%9F%E6%B9%96%E5%8F%8B%E4%BA%BA%E6%A8%A1/). It added one-click AI character generation in Oct 2024 — [南方都市报](https://epaper.oeeee.com/epaper/TK/html/2024-10/31/content_18739.htm)
- NetEase Fuxi and Justice ran an in-game "AI arena". Five external LLM vendors (Alibaba Tongyi, Baidu ERNIE, MiniMax abab, Moonshot Kimi, ByteDance Doubao) each powered NPCs across 9 story themes. This amounts to a model-agnostic NPC layer — [极客公园](https://www.geekpark.net/news/343404); [网易伏羲](https://fuxi.163.com/database/1264); [知乎](https://zhuanlan.zhihu.com/p/9834820905)
- **Where Winds Meet (燕云十六声, NetEase/Everstone)** launched globally on 14 Nov 2025 on PC/PS5, on mobile on 12 Dec 2025 and on Xbox in June 2026. Launch figures: 10M pre-registrations, about 2M players in 24 hours, a Steam peak of about 194K concurrent players, and about 80% positive from 13K+ reviews. Some NPCs ("Jianghu Friends") run on an LLM, and players type free text instead of choosing scripted lines — [Arcanum RPGs](https://arcanumrpgs.com/blog/where-winds-meet-ai/); [PCGamesN](https://www.pcgamesn.com/where-winds-meet/reception-ai-chatbots)
- Reception of the Where Winds Meet AI NPCs was mixed but loud:
  - Wccftech called them "unironically the game's best feature" — [Wccftech](https://wccftech.com/where-winds-meet-ai-chatbot-npcs-are-unironically-the-games-best-feature/)
  - PCGamesN said the chatbot NPCs "overshadowed the combat" — [PCGamesN](https://www.pcgamesn.com/where-winds-meet/reception-ai-chatbots)
  - Players pushed the NPCs to their limits and "tricked" them — [Arcanum RPGs](https://arcanumrpgs.com/blog/where-winds-meet-ai/); [The Outpost](https://theoutpost.ai/news-story/where-winds-meet-players-push-ai-chatbot-np-cs-to-their-limits-in-creative-and-chaotic-ways-21744/)
  - The game shipped live AI characters without a Steam AI disclosure. The disclosure only appeared on 12 Dec 2025 — [Arcanum RPGs](https://arcanumrpgs.com/blog/where-winds-meet-ai/)
- **Krafton inZOI** passed 1M sales within one week of Steam Early Access (as of 4 Apr 2025), Krafton's fastest-selling title ever. About 95% of sales came from outside Korea — [Krafton PR](https://www.krafton.com/en/news/press/krafton-hits-1-million-sales-of-inzoi-in-first-week-of-early-access-launch/); [Game Developer](https://www.gamedeveloper.com/business/krafton-brands-life-simulator-inzoi-a-long-term-franchise-after-it-hits-1-million-sales)
- inZOI's "Smart Zoi" characters use NVIDIA ACE with a Mistral-NeMo-Minitron small language model running **entirely on-device**. The characters generate inner thoughts and daily schedules and make autonomous decisions from 400+ mental elements — [InZOI (Wikipedia)](https://en.wikipedia.org/wiki/InZOI); [TheGamesWiki](https://thegameswiki.com/inzoi/wiki/inzoi-game-overview)
- **Krafton Q1 2026** set a quarterly revenue record of about $931M (+57%). The growth came mainly from PUBG Mobile and BGMI, not AI features. Coverage frames Krafton's strategy as "AI-first", including AI script-modding tools for inZOI — [Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/krafton-q1-2026-revenue-surges-57-via-pubg-ai-first-strategy)
- **PUBG Ally** (a "Co-Playable Character"):
  - On 17 Jun 2026 Krafton launched the "Ally Duo" beta, an Arcade mode where a player teams with the AI character "Ella" on Sanhok — [Krafton PR](https://www.krafton.com/en/news/press/krafton-introduces-pubg-ally-beta-test/); [Massively OP](https://massivelyop.com/2026/06/17/krafton-is-testing-an-ai-powered-ally-for-pubg-and-making-esports-deals-for-pubg-mobile/)
  - It runs an on-device SLM built on NVIDIA ACE with speech-to-text and text-to-speech. It supports English, Korean and Chinese and understands PUBG terminology, maps and items — [NVIDIA Technical Blog](https://developer.nvidia.com/blog/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace/); [Krafton PR](https://www.krafton.com/en/news/press/krafton-reveals-playtest-plans-for-pubg-ally-built-with-nvidia-ace/)
  - It was revealed at CES 2025 and moved from "early 2026 test" to a June 2026 beta, a slow path to production — [KitGuru](https://www.kitguru.net/gaming/joao-silva/pubg-ally-public-testing-begins-in-early-2026/)
- **Fortnite / UEFN "Conversations"** (formerly teased as the "Persona device"):
  - Creators can build AI NPCs that hold unscripted real-time voice conversations. It shipped as experimental in v40.20 (16 Apr 2026), and creators could publish islands with it from 30 Jul 2026 — [Fortnite news](https://www.fortnite.com/news/bring-npcs-to-life-with-ai-powered-conversations); [TweakTown](https://www.tweaktown.com/news/111153/fortnite-developers-can-now-create-ai-characters-that-players-can-actually-talk-to/index.html)
  - Stack: Google **Gemini 3.1 Flash Lite** processes audio and generates text, and **ElevenLabs** produces the voice. Creators define personality and knowledge in "as few as 20 lines" of prompt — [Wccftech](https://wccftech.com/fortnite-uefn-ai-npc-conversations-gemini-elevenlabs/); [Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/epic-launch-ai-voice-npcs-via-gemini-elevenlabs-in-fortnite-uefn)
  - Epic's rules ban romance simulation, medical advice and hateful output, and Epic says it does not store player audio — [Wccftech](https://wccftech.com/fortnite-uefn-ai-npc-conversations-gemini-elevenlabs/); [LevelUp](https://www.levelup.com/en/news/fortnite-unveils-tool-to-create-chatbot-npcs-powered-by-ai/)
  - A lower-quality source reports Epic added AI voices for 36 Fortnite characters usable on creator islands (July 2026) — [NoSmokeSport](https://nosmokesport.com/game-news/epic-games-ai-voices-fortnite-creator-islands-july-2026/)

**Standalone AI-native games (attention far exceeds revenue)**
- **Whispers from the Star** (Anuttacon, the studio founded by miHoYo co-founder Cai Haoyu per background knowledge) launched on **14 Aug 2025**:
  - It is an open-ended voice, video and text conversation game with a stranded astronaut, "Stella". It uses a custom fine-tuned LLM with no dialogue trees — [Steam](https://store.steampowered.com/app/3730100/); [Steambase](https://steambase.io/games/whispers-from-the-star/reviews)
  - Steam rating is "Very Positive" (82% of about 1,575 reviews), but only 61% of just 21 reviews in the last 30 days, i.e. low ongoing volume — [Steam](https://store.steampowered.com/app/3730100/); [Steambase](https://steambase.io/games/whispers-from-the-star/reviews)
- **Suck Up!** (Proxima), a comedic vampire sandbox of voice-driven AI agents:
  - It claims 50M+ social views and 100M+ YouTube views with zero marketing, and calls itself "the first commercially successful game utilizing immersive agents" — [Proxima](https://www.proxima.gg/); [LinkedIn](https://www.linkedin.com/company/proximagg)
  - Third-party estimates for its Steam release (1 Oct 2025): about 12K copies, about $131.7K gross and about $75K net. Another tracker estimates about $62K — [GameRevenueData](https://gamerevenuedata.com/games/suck-up/); [Games-Stats](https://games-stats.com/steam/game/suck-up/). These are low-confidence estimates, and sales on its own pre-Steam launcher are not included.
- **AI Dungeon / Latitude**:
  - Launched in 2019. Cited at 8M+ downloads and 1.5M+ MAU; one estimate puts ARR at only about $1.4–1.8M (low confidence) — [IntelPilot](https://www.intelpilot.ai/company/latitude/6a028ebda6715bdc30963e7e)
  - Latitude launched **Voyage** in April 2026, an "AI-native RPG platform". Testers created 160K+ unique AI characters. Planned subscriptions run $15–$99 a month — [TechCrunch](https://techcrunch.com/2026/04/21/voyage-is-an-ai-rpg-platform-for-creating-custom-gaming-worlds-with-ai-generated-npc-interactions/); [Latitude](https://latitude.io/news/voyage-launches-first-ai-native-rpg-platform)
- Commentary: Joseph Kim's essay "The Last 20% Is Worth $100 Million" argues that polish and design, not the AI demo, drive commercial value (title-level only; not read in full) — [Gamemakers](https://www.gamemakers.com/p/the-last-20-is-worth-100-million)

**AI character and companion platforms**
- **Character.AI**:
  - Banned open-ended 1:1 chat for under-18s from 24–25 Nov 2025. Minors get a structured "Stories" interactive-fiction mode instead, with age checks via Persona selfie scans. The move followed lawsuits alleging psychological harm — [CNBC](https://www.cnbc.com/2025/11/24/characterai-to-ban-teens-from-open-ended-chats-human-interaction-is-crucial-psychotherapist-says.html); [TechCrunch](https://techcrunch.com/2025/10/29/character-ai-is-killing-the-chatbot-experience-for-minors/?rand=23331); [MediaNama](https://www.medianama.com/2025/11/223-character-ai-under-18-users-ai-chatbots-stories-alternative/)
  - Revenue: about $30M annualized (Sacra, Jul 2025), with the company projecting about $50M by end-2025. About 20M users — [SQ Magazine](https://sqmagazine.co.uk/character-ai-statistics/)

**NPC middleware**
- **Inworld AI** raised $50M at a $500M+ valuation (Aug 2023; Lightspeed, M12, Samsung Next, First Spark, LG), with more than $100M raised in total. It was then the best-funded AI-gaming startup — [BusinessWire](https://www.businesswire.com/news/home/20230802502983/en/Inworld-AI-the-Leading-Character-Engine-Raises-New-Funding-From-Lightspeed-Stanford-Microsofts-M12-Fund-First-Spark-Eric-Schmidt-and-More-Bringing-Valuation-to-Over-$500-Million); [GamesBeat](https://gamesbeat.com/inworld-ai-raises-new-round-at-500m-valuation-for-ai-game-characters/)
- Inworld now markets "the first AI runtime engineered to scale **consumer applications** from 10 to 10M users", i.e. positioning wider than games. Its CES 2025 showcase was a Streamlabs streaming assistant, not a game — [Inworld/Tracxn profile summary](https://tracxn.com/d/companies/inworld-ai/__tjWZC3FjI2Vxjo9ijvchq0joN7t3zWc5nHkAN9FWwuk); [PitchBook](https://pitchbook.com/news/articles/generative-ai-gaming-inworld-venture-funding)

### Inferences
- **Distribution beats novelty.** AI NPCs reach scale when an incumbent with an existing audience bolts them onto a proven loop (Where Winds Meet, Justice, PUBG, Fortnite). Standalone AI-native titles show a large gap between attention and conversion: Suck Up! had about 100M views but only about 12K estimated Steam copies. Whispers from the Star has roughly 1.5K Steam reviews. Under the common 30–60× reviews-to-sales heuristic that suggests tens of thousands of copies (a rough inference, not data).
- **Architecture is converging on two cost patterns.** (a) On-device SLMs (NVIDIA ACE plus Minitron in inZOI and PUBG Ally) push inference cost onto the player's GPU. (b) The cheapest cloud tiers (Gemini Flash Lite plus ElevenLabs in Fortnite) accept a per-use cost at platform scale. The on-device pattern ties the feature to high-end PCs.
- **Controllability and safety are now designed in, not bolted on.** The mechanisms seen so far are domain-restricted training data (Justice), prompt-level persona definitions with banned-content categories (Epic), and age gating that cut off minors from open-ended chat (Character.AI). Where Winds Meet shows that players will jailbreak NPCs for fun. That makes the problem both a risk and a source of content.
- The strongest design fit seen so far is **social, comedic and emergent content that is streamable**, not core progression loops (inference).

### Gaps
- No hard engagement, retention or monetization data was found for any AI-NPC feature. That covers AI-feature DAU, session length or ARPU lift for Justice, Where Winds Meet, inZOI or PUBG Ally. Company figures seen are total-game metrics only.
- No verified sales figures for Whispers from the Star, 1001 Nights or Infinite Craft. Convai funding, the Nvidia ACE adoption list and Ubisoft's "Teammates"/NEO NPC status were not researched because the search budget ran out.
- Inference cost per player-hour, latency benchmarks and failure-rate data were not found in any source.
- UNVERIFIED LEADS (background knowledge; verify before use):
  - Epic's AI Darth Vader voice in Fortnite (May 2025; Gemini plus ElevenLabs) drew a SAG-AFTRA unfair-labor-practice charge.
  - Other ACE titles include Wemade's MIR5 and NetEase's NARAKA teammates.
  - Infinite Craft (Neal Agarwal, Jan 2024) went viral and later shipped on mobile.

---

## 2. World models and generative interactive environments: status, limits, plausible timelines

### Takeaway
2026 brought a **capital flood and consumer-facing demos, but no production game use**:
- Google's Project Genie (Genie 3) reached paying consumers in January 2026 and briefly knocked 7–21% off game-platform stocks.
- World Labs ($1B at about $5B), Decart ($300M at about $4B) and General Intuition ($320M at $2.3B) raised mega-rounds.
- Tencent open-sourced HY World 2.0 explicitly for game workflows.

Current limits are about 1-minute sessions at 720p/24fps with weak persistence, and the leading startups' first revenue comes from **simulation (autonomous vehicles, robotics) and exportable 3D scenes**, not from "neural games". The near-term game value is in previsualization, blockout and ideation. Fully neural games remain speculative.

### Cited Findings
- **Google DeepMind Project Genie** launched on 29 Jan 2026 for Google AI Ultra subscribers. It is built on Genie 3 (Aug 2025) and lets users create, explore and remix interactive worlds from text or image prompts, with features including "World Sketching" — [The Register](https://www.theregister.com/2026/01/29/googles_project_genie_ai); [9to5Google](https://9to5google.com/2026/01/29/google-project-genie/); [PYMNTS](https://www.pymnts.com/google/2026/google-deepmind-introduces-project-genie-for-interactive-ai-world-building/); [Investing.com](https://www.investing.com/news/stock-market-news/unity-stock-falls-alongside-taketwo--roblox-after-googles-project-genie-launch-4476580)
- Genie 3 is described as the first real-time, interactive, general-purpose world model: navigable 3D worlds at 24 fps that stay consistent over "several minutes" — [Genie (Wikipedia)](https://en.wikipedia.org/wiki/Genie_(world_model)). Search results still describe Genie 3 as the latest public version, with **no "Genie 4" found** as of late Sep 2026 (absence of evidence only) — [Genie (AI model), Wikipedia](https://en.wikipedia.org/wiki/Genie_(AI_model))
- **Limits reported by analysts:** each Project Genie world lasts about a minute before breaking down, runs at 720p/24fps, and looks "closer to a low-resolution video stream than a modern 3D game" — [Naavik](https://naavik.co/digest/project-genie-and-the-stock-markets-category-error/); [Kotaku](https://kotaku.com/video-game-stocks-down-take-two-gta-nintendo-roblox-unity-google-ai-game-maker-2000664594)
- **Market reaction (30 Jan 2026):**
  - Unity fell about 12%, Take-Two about 7% and Roblox about 8% per Investing.com. Other reports give larger intraday drops: Unity about 21%, Take-Two about 10%, Roblox about 12% — [Yahoo/Investing.com](https://finance.yahoo.com/news/unity-stock-falls-alongside-two-155219712.html); [Seeking Alpha](https://seekingalpha.com/news/4544948-video-game-stocks-nosedive-as-googles-project-genie-allows-virtual-world-creation); [GIGAZINE](https://gigazine.net/gsc_news/en/20260131-game-stocks-slide-google-project-genie); [Cryptopolitan](https://www.cryptopolitan.com/take-two-roblox-and-unity-crash-after-google-launches-project-genie-ai/)
  - Sherwood's headline stressed that the tool "can create playable, **copyrighted** worlds", an IP flag — [Sherwood News](https://sherwood.news/markets/gaming-stocks-plunge-following-release-of-googles-ai-tool-that-can-create/)
  - Critics called the selloff a "category error" (Naavik) and "a very dumb reason" (Kotaku) — [Naavik](https://naavik.co/digest/project-genie-and-the-stock-markets-category-error/); [Kotaku](https://kotaku.com/video-game-stocks-down-take-two-gta-nintendo-roblox-unity-google-ai-game-maker-2000664594)
- **Research focus has shifted to long-horizon stability and cheaper compute.** Examples are new 2026 benchmarks for multi-turn interactive world models (WBench) and long-horizon stability in open worlds (WorldRoamBench), and "low-compute real-time controllable" world models (DreamForge-World 0.1) — [WBench, arXiv](https://arxiv.org/pdf/2605.25874); [WorldRoamBench, arXiv](https://arxiv.org/pdf/2606.31672); [DreamForge-World, arXiv](https://arxiv.org/pdf/2606.30292)
- **Decart** (its Oasis Minecraft-like real-time demo dates to Oct 2024, per background knowledge):
  - Raised **$300M at about a $4B valuation** (reported May 2026), led by Radical Ventures with NVIDIA, Adobe Ventures, Toyota Ventures and eBay Ventures, among others. Amazon is a strategic customer. Total raised is $456M.
  - Sources label the round differently: Series B (InvestGame, TAMradar) vs Series C (Contrary). Sources: [CTech](https://www.calcalistech.com/ctechnews/article/sjt9ncukgl); [InvestGame](https://investgame.net/news/decart-raises-300m-series-b-at-4b-valuation/); [Contrary Research](https://research.contrary.com/company/decart)
  - **Oasis 3 (June 2026) targets photorealistic driving simulation**, sold through an API to autonomous-vehicle developers. TechCrunch says it can simulate "hours" of driving "with some caveats" — [TechCrunch](https://techcrunch.com/2026/06/10/decarts-new-world-model-can-simulate-hours-of-photorealistic-driving-with-some-caveats/); [Crypto Briefing](https://cryptobriefing.com/decart-oasis-3-driving-simulation-api/)
  - A single secondary source says Anthropic was reported in Aug 2026 to be in talks to buy Decart for $6–7B, with a reportedly higher NVIDIA bid. This is **unverified** — [Contrary Research](https://research.contrary.com/company/decart)
- **World Labs (Fei-Fei Li)** raised **$1B at about $5B** (18 Feb 2026), for $1.23B in total. Investors include a16z, NVIDIA, AMD, Cisco and Autodesk ($200M) — [World Labs blog](https://www.worldlabs.ai/blog/funding-2026); [Crowdfund Insider](https://www.crowdfundinsider.com/2026/02/262836-ai-firm-world-labs-raises-1-billion-at-5-billion-valuation/); [The AI Insider](https://theaiinsider.tech/2026/02/19/fei-fei-lis-world-labs-raises-1b-in-fresh-funding-to-advance-development-of-world-models/)
  - **Marble** went into limited beta in Nov 2025 and launched commercially in Feb 2026. It takes text, photos, video, panoramas or rough 3D layouts and outputs **navigable, persistent, editable 3D environments**. Target uses are games, VFX, VR and robotics. No user metrics were found — [StartupHub](https://www.startuphub.ai/ai-news/ai-figures/2026/figure-fei-fei-li-company-financial-breakdown-2026-06-03); [AI CERTs](https://www.aicerts.ai/news/world-labs-funding-targets-5b-amid-marble-momentum/)
- **General Intuition** (spun out of the game-clip platform Medal) raised **$320M at $2.3B** in June 2026, led by Khosla, for $454M in total including a $134M seed (Oct 2025) — [TechCrunch](https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/); [MLQ](https://mlq.ai/news/general-intuition-raises-320m-at-23b-valuation-to-train-ai-agents-on-gameplay-data/)
  - Its data moat: Medal users (10M+ MAU) upload about 2B clips a year with **embedded action labels** (which buttons were pressed and when). Agents are the product and the world model is the training ground — [TechCrunch](https://techcrunch.com/2026/06/25/general-intuitions-2-3b-bet-that-video-games-can-train-ai-agents-for-the-real-world/)
  - Headlines say OpenAI tried to buy this gaming data (reported as a "$500M gaming data grab"); unverified detail — [TNW](https://thenextweb.com/news/general-intuition-300m-world-models-gaming-data); [TechBuzz](https://www.techbuzz.ai/articles/openai-s-500m-gaming-data-grab-signals-world-model-war)
- **Tencent Hunyuan:**
  - HunyuanWorld 1.0 was released and open-sourced in 2025 — [知乎](https://zhuanlan.zhihu.com/p/1933125331369296287)
  - **HY World 2.0** was released and open-sourced in April 2026, with "seamless integration into game workflows". It accepts text, image or video input, supports sketch-to-map and image-to-space, and lets game characters move through generated 3D scenes. Tencent frames it as moving "AI creating worlds" from concept to industrial application — [IT之家](https://www.ithome.com/0/939/747.htm); [东方财富](https://finance.eastmoney.com/a/202604173708636551.html)
  - Hunyuan-GameCraft is an interactive game-video generation framework. One summary said its open-sourcing was still "scheduled", which conflicts with background knowledge of a 2025 code release, so verify — [IT之家](https://www.ithome.com/0/939/747.htm)
  - Tencent runs a dedicated Hunyuan game-creation portal — [腾讯混元游戏](https://hunyuan.tencent.com/game/home)
- **Microsoft Muse (WHAM)**:
  - Announced 19 Feb 2025 with Ninja Theory and trained on *Bleeding Edge* gameplay. It generates consistent gameplay from about 10 initial frames plus controller actions. Microsoft positioned it for **gameplay ideation and game preservation/porting** — [Xbox Wire](https://news.xbox.com/en-us/2025/02/19/muse-ai-xbox-empowering-creators-and-players/); [Microsoft Research](https://www.microsoft.com/en-us/research/video/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/)
  - A Newsweek opinion piece called it "impressive, but utterly baffling" — [Newsweek](https://www.newsweek.com/entertainment/video-games/opinion-microsofts-generative-ai-model-muse-impressive-utterly-baffling-2033713)
  - One search summary dated the Nature paper to "May 2026", which conflicts with the Feb 2025 announcement. Treat that as a summarizer error.
  - No 2026 production deployment was found.
- **Dynamics Lab Mirage 2** (Aug 2025) bills itself as a real-time "AI-native UGC game engine":
  - It turns uploaded images (sketches, photos, paintings) into playable worlds that players modify with text commands. It runs in the cloud and a browser and was built by a team of fewer than 10 people — [The Decoder](https://the-decoder.com/mirage-2-allows-users-to-turn-sketches-and-photos-into-interactive-game-worlds/); [Hacker News](https://news.ycombinator.com/item?id=44978286)
  - Its blog now promotes "Magica: AI UGC game engine" — [Dynamics Lab blog](https://blog.dynamicslab.ai/)

### Inferences
- **Two technical branches with different paths to production (inference):**
  1. **Explicit 3D world generation** (World Labs Marble, Tencent HY World 2.0, and 3D generators in §4) produces assets that load into Unity or Unreal. This branch can enter pipelines now for previs, blockout, background environments and UGC creation.
  2. **Frame-generating "neural engines"** (Genie 3, Oasis, Mirage, Muse) replace the renderer and game logic with a model. They are limited by session length, persistence, resolution, determinism, multiplayer sync and per-user GPU cost.
- **First revenue for neural world models is outside games.** Decart pivoted its flagship to AV driving simulation, and General Intuition sells agents trained on game data. Games act more as a **data source and demo surface** than a paying customer. That creates a new monetization line for owners of gameplay data (clip platforms, publishers with telemetry).
- **Timeline (speculation, clearly labeled):** No source in this session gave a dated forecast for neural world models in shipped commercial games. The only dated engine roadmap found is Unreal Engine 6 early access in late 2027 (§4), and it is about agentic tooling, not neural rendering. Given the 2026 limits (about 1 minute, 720p/24fps), plausible sequencing is:
  - 2026–27: ideation, previs and "toy" experiences (Project Genie, Mirage)
  - 2027–29: hybrid designs where a conventional engine owns state and logic while generative models handle visuals or content
  - Later: fully neural commercial games
- **The market is pricing narrative risk ahead of capability.** Project Genie's stock impact on Unity, Roblox and Take-Two shows public-market sensitivity to "AI replaces engines/platforms" stories, even though analysts judged current capability far from that.

### Gaps
- No usage or revenue numbers for Project Genie, Marble, Mirage or HY World.
- Not researched due to the search cap: Skywork Matrix-Game 2.0/3.0, Odyssey (funding, Odyssey-2), Runway's world model, xAI's announced AI-generated game ambitions, NVIDIA Cosmos's relevance to games, and Etched/Decart hardware tie-ups.
- Per-user inference cost of real-time world models: no source found.
- The Decart acquisition-talks report needs primary confirmation.

---

## 3. UGC and AI creation platforms; release volume and AI disclosure; China mini-games

### Takeaway
UGC platforms are where "creators replacing studios" already has real money behind it:
- **Roblox** pays creators about $363M a quarter (+15% YoY).
- **Fortnite/UEFN** passed **$1B in cumulative payouts** (about $370M in 2025).
- Both are embedding generative AI (Roblox Cube/4D generation; Fortnite "Conversations" NPCs) to further lower the creation barrier.

AI-native creation platforms are raising money (**Astrocade**: $56M, 20M users). But **Rec Room's shutdown** (June 2026), with AI features that reportedly cost more per user than subscriptions earned, shows the economics can break.

Supply is exploding while attention is flat:
- **Steam releases** went from 9,654 (2020) to 18,556 (2024) and 19,468 (2025), with a pace of about 24K for 2026. About half of 2025 releases got fewer than 10 reviews, and about 1 in 5 disclose generative AI.
- **China's mini-game (小程序游戏) market** reached ¥53.5B in 2025 (+34%) with 500K+ WeChat developers, mostly teams under 30 people.

### Cited Findings
**Roblox**
- Q2 2026 results:
  - Revenue $1.5B (+36% YoY); bookings $1.6B (+8%, at the low end of guidance); **DAU 123M (+10%)**
  - **DevEx creator payouts $363M (+15%)**, reflecting the creator-earnings increase announced 5 Sep 2025
  - Operating cash flow $318M (+60%); free cash flow $294M (+66%)
  - **Q3 2026 bookings guidance $1.58–1.65B, i.e. down 14–18% YoY**; shares fell on the bookings news
  - Sources: [Roblox Q2 2026 shareholder letter (SEC)](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm); [GuruFocus](https://www.gurufocus.com/news/8993610/roblox-corp-rblx-q2-2026-earnings-call-highlights-revenue-surges-36-to-15b-but-q3-bookings-forecast-signals-sharp-decline); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-roblox-q2-2026-beats-eps-but-shares-sink-on-bookings-93CH-4826338); [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/roblox-corp-rblx-q2-2026-050249366.html)
- Roblox AI stack:
  - The **Cube foundation model** (Cube 3D launched at GDC 2025; its open-sourcing is from background knowledge) is now used for "accelerating creation" (Feb 2026) — [Roblox Newsroom](https://about.roblox.com/newsroom/2026/02/accelerating-creation-powered-roblox-cube-foundation-model); [VentureBeat/GamesBeat](https://venturebeat.com/game-development/roblox-unveils-roblox-cube-genai-and-other-game-dev-tools-for-gdc/)
  - **4D generation** creates *functional, interactive* objects. It started as an early-access feature for in-experience 4D functional objects and moved to beta — [DevForum early access](https://devforum.roblox.com/t/early-access-introducing-in-experience-4d-functional-objects-and-enhanced-3d-generation/4050893); [DevForum beta](https://devforum.roblox.com/t/beta-4d-generation-unlock-new-types-of-gameplay/4331818)
- **RDC 2026 (Sept 2026):**
  - Roblox's VP of foundation AI (Anupam Singh) set out four AI pillars: **coding, 3D objects, multiplayer NPCs, video/realism**.
  - The Cube model lets users build functional 3D environments from text prompts **on mobile inside the Roblox Player app**.
  - Roblox's stated goal is for any creator to generate full scenes (assets, environments, code, animation) from natural language.
  - Roblox showcased "Dream Racers", an AI-built racing game.
  - Sources: [GamesBeat RDC briefing](https://gamesbeat.com/roblox-dives-into-the-details-on-its-rdc-engine-updates-roblox-wallet-and-offline-play-press-briefing/); [Tekkie Pinas (low-quality blog)](https://www.tekkiepinas.xyz/2026/09/roblox-unveils-major-updates-to-expand.html); [Yahoo Tech](https://tech.yahoo.com/ai/articles/robloxs-game-changing-ai-3d-143000680.html)

**Epic / Fortnite UEFN**
- In 2024, creators earned **$352M**; about 70K creators made 198K islands, about 60K islands were played daily, and creator islands took about one-third of Fortnite play time — [Tubefilter](https://www.tubefilter.com/2025/01/23/fortnite-epic-games-creator-payouts-2024/)
- Cumulative UEFN creator payouts passed **$1B** (June 2026). Naavik estimates about **$370M paid in 2025** (range $350–390M) — [Tubefilter](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/); [Tech Insider CA](https://tech-insider.org/ca/fortnite-creator-economy-1-billion-2026/). The Tech Insider headline also cites creator content at "47% of playtime" (title-level only).
- Mechanics: 40% of net Item Shop and real-money revenue goes into the engagement pool, paid out by engagement and retention metrics — [Epic docs](https://dev.epicgames.com/documentation/fortnite/engagement-payout-in-fortnite-creative)
- AI NPC "Conversations" for UEFN creators went generally publishable on 30 Jul 2026 (see §1) — [Fortnite news](https://www.fortnite.com/news/bring-npcs-to-life-with-ai-powered-conversations)

**Failures and stalls**
- **Rec Room** (once valued at $3.5B; 150M+ lifetime players):
  - Announced on 31 Mar 2026 that it would shut down on 1 Jun 2026.
  - It cut 16% of staff in Mar 2025 and about half the remainder in Aug 2025 (about 310 down to about 100 people).
  - It had launched **Maker AI** (AI game creation) and **Roomie** (AI companion). Coverage reports that **per-user AI costs exceeded subscription revenue** and that Rec Room kept only about $0.30 of each dollar after platform and creator fees.
  - Sources: [TechCrunch](https://techcrunch.com/2026/03/31/social-gaming-platform-rec-room-once-valued-at-3-5b-is-shutting-down/); [GeekWire](https://www.geekwire.com/2026/rec-room-shutting-down-seattles-3-5b-social-gaming-platform-says-it-cant-make-the-business-work/); [UploadVR](https://www.uploadvr.com/rec-room-to-shut-down-in-june/); [Metaintro](https://www.metaintro.com/blog/rec-room-shutdown-150-million-users-startup-job-instability-2026)
  - The AI-cost detail comes from aggregated search summaries; confirm it against the TechCrunch or GeekWire text.

**AI-native creation platforms**
- **Astrocade** raised **$56M** (Series A led by Sea, Series B led by Sequoia; with Google's AI Futures Fund, NVIDIA and LG Tech Ventures). It claims **20M+ users and 75K+ games from 80 countries within 8 months** of public launch — [Fortune](https://fortune.com/2026/05/05/astrocade-raises-56-million-series-b-sequoia-video-games-platform-ali-amir-sadeghian/); [PocketGamer.biz](https://www.pocketgamer.biz/astrocade-raises-56m-to-expand-ai-powered-games-creation-platform/)
  - One summary claims Fei-Fei Li co-founded Astrocade. That is unverified and probably conflates an advisor or investor tie. Fortune names co-founders including Amir Sadeghian.
  - Comparable companies: Rosebud AI and Spawn.co — [explainx](https://explainx.ai/blog/astrocade-56m-funding-sequoia-sea-ai-game-creation-2026)

**Steam supply and AI disclosure**
- Steam releases:
  - 2020: 9,654; 2024: 18,556; **2025: 19,468**, a record, with **almost half getting fewer than 10 reviews**
  - Steam earned $16B+ in 2025
  - H1 2026: 11,979 releases (about 66 a day), a **pace of about 24K for 2026**
  - Sources: [SteamDB stats](https://steamdb.info/stats/releases/); [SteamDB on X](https://x.com/SteamDB/status/1999420488271937702); [80.lv](https://80.lv/articles/steam-earned-usd16b-in-2025-but-nearly-half-of-19-000-games-got-under-10-reviews); [KitGuru](https://www.kitguru.net/gaming/joao-silva/steam-data-shows-over-19000-games-released-in-2025/); [TechSpot](https://www.techspot.com/news/110592-nearly-half-19000-games-released-steam-year-went.html)
  - An alternative count gives 20,282 for 2025 (methodologies differ) — [Steam Page Analyzer](https://www.steampageanalyzer.com/blog/how-many-games-release-on-steam)
- AI disclosure (Totally Human Media analysis of the Steam API, 2025):
  - **7,818 titles disclose generative AI use, about 7% of the whole Steam library**
  - **About 1 in 5 (just under 20%) of 2025 releases disclose AI use**, up about 700–800% YoY, from about 1,000 disclosing games in 2024
  - Visual assets make up **about 60% of disclosures**, followed by audio (voice-over, narration, music), text/narrative and marketing
  - Sources: [Tom's Hardware](https://www.tomshardware.com/video-games/pc-gaming/1-in-5-steam-games-released-in-2025-use-generative-ai-up-nearly-700-percent-year-on-year-7-818-titles-disclose-genai-asset-usage-7-percent-of-entire-steam-library); [ScreenHub](https://www.screenhub.com.au/news/games/steam-generative-ai-games-2673234/); [Totally Human](https://www.totallyhuman.io/blog/the-surprising-new-number-of-genai-games-on-steam); [Digital Watch](https://dig.watch/updates/generative-ai-now-powers-20-of-new-steam-games)
  - A 2026 piece headlined "Steam AI Disclosure Hits 20% of Games as Rivals Skip" suggests other stores have no equivalent disclosure (title-level) — [Tech Insider](https://tech-insider.org/steam-ai-disclosure-2026/)

**China mini-games (小程序游戏)**
- 2025 domestic mini-game revenue was **¥53.535B (+34.39% YoY)**. In-app purchases brought ¥36.464B (68.11%) and ad monetization (IAA) ¥17.071B (31.89%) — [163/网易订阅 summary](https://www.163.com/dy/article/L3DP9MMH0518G5DJ.html); [证券日报](http://www.zqrb.cn/gscy/gongsi/2026-01-17/A1768566351773.html)
- WeChat mini-games developer base:
  - 400K+ cumulative developers by Jan 2026, with 5,000+ first-time publishers in 2025. **500K+ developers by Jan–May 2026, over 80% of them teams of fewer than 30 people** — [证券日报](http://www.zqrb.cn/gscy/gongsi/2026-01-17/A1768566351773.html); [虎嗅](https://www.huxiu.com/article/4862416.html)
  - About 500M MAU. 300+ titles grossed over ¥10M in a single quarter (2025 developer conference) — [GameRes](https://www.gameres.com/912988.html); [DoNews](https://www.donews.com/news/detail/1/5534130.html)
- AI in mini-game production:
  - At the May 2026 conference, the WeChat team said AI tools have further cut art and testing costs. It is building **AI coding** so ordinary users can write a mini-game in natural language.
  - The framing is that making money now requires "AI 提效 + 玩法创意 + 精准运营" (AI efficiency, gameplay creativity and precise operations) rather than riding platform traffic — [腾讯新闻](https://news.qq.com/rain/a/20260529A05IF300?id=20260529A05IF300&path=a&app=news&suid=&redirect_pc=1); [DoNews](https://www.donews.com/news/detail/1/6575058.html)
- The H1 2026 China industry report singled out mini-program games as a highlight (see §5 for totals) — [新华网](https://www3.xinhuanet.com/tech/20260731/c5593cc57b18411ab328cd3ed98b554c/c.html)

### Inferences
- **Creator payouts put a floor on "creators replace studios" in some genres.** Roblox is at about $1.4B a year run-rate (4 × $363M) and Fortnite at about $370M a year, which together exceed the budgets of many mid-size publishers (inference). AI features (Cube/4D, Conversations, WeChat AI coding) target the next barrier, which is non-coders creating functional content.
- **The UGC economy is hit-driven and volatile.** Roblox guided Q3 2026 bookings down 14–18% YoY even as AI creation tools shipped. AI lowers creation cost but does not fix demand concentration. The likely comparison base is the viral hits of Q3 2025, but that is not verified.
- **AI-heavy social or UGC products need unit economics that survive per-user inference.** Rec Room is the cautionary case, especially when the platform keeps only about 30% of each dollar.
- **The supply surge is real, and discoverability is the binding constraint.** Steam's 2026 pace (about 24K) is about 23% above 2025 after only about 5% growth in 2025. The acceleration coincides with about 20% of releases disclosing AI use, but causation is not established. About half of releases already get almost no traction.
- In China, mini-games (+34%) are the fastest-growing segment and are dominated by small teams. It is the most likely place for AI-driven "many more games from small teams" to show up first in the revenue data (inference).

### Gaps
- Numbers not found: share of Roblox creators using AI tools, count of Cube/4D generations, AI Assistant usage, and any retention or revenue uplift from AI-made experiences.
- Epic's official 2025 payout figure; only a Naavik estimate was found.
- Steam releases for 2022–2023 were not captured. UNVERIFIED LEAD: roughly 12.5K in 2022 and 14.5K in 2023 per SteamDB. Also missing: Steam 2026 AI-disclosure share, and sales/review performance of AI-disclosed vs other games.
- Not researched due to the search cap:
  - Rosebud AI metrics
  - Pieter Levels' fly.pieter.com (UNVERIFIED LEAD: built with AI coding tools in Feb 2025; reported about $1M ARR within weeks from in-game ads)
  - Vibe-coding game jams
  - Douyin mini-games (抖音小游戏)
  - AI penetration statistics in Chinese mini-game art
- UNVERIFIED LEAD: Roblox DAU peaked around 150M in Q3 2025 during viral hits. If true, 123M in Q2 2026 is a sizable drop. Age checks introduced for chat in early 2026 may also matter.

---

## 4. AI tooling for game production by pipeline stage; funding, revenue and M&A

### Takeaway
Money is concentrating in **horizontal, cross-industry generation tools** whose revenue is now measurable:
- **3D generation:** Meshy at $40M ARR with a $1.5B valuation; Tripo near $200M raised and unicorn status.
- **Voice:** ElevenLabs at $330M+ ARR at end-2025, $500M+ by 2026, and an $11B valuation.

Game-specific middleware (QA agents, NPC engines) is still sub-scale. The engines, **Unity 6 AI and Unreal 5.8/6**, are becoming **hosts for third-party frontier models** (Claude, Gemini) via MCP rather than building their own models. That shifts inference revenue to model providers and makes "agentic editing" the main production-AI pattern.

### Cited Findings
**3D asset generation**
- **Meshy:**
  - Series B of **about $400M at a $1.5B valuation** (21 Jul 2026), the largest AI-3D round to date.
  - **ARR went from $15M (Nov 2025) to $30M (Mar 2026) to $40M (Apr 2026)**, growing about 12× YoY.
  - **12M+ registered users; 100M+ models created.** The company pitches "a usable 3D model in about a minute and a dollar" versus "weeks" before.
  - Sources: [PR Newswire](https://www.prnewswire.com/news-releases/meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-302828384.html); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/meshy-raises-nearly-400-million-150000477.html); [Naavik](https://naavik.co/ai-gaming/inside-meshys-400m-raise-for-3d-assets/); [TFN](https://techfundingnews.com/from-mit-research-to-1-5b-unicorn-ethan-hus-meshy-raises-400m-for-ai-powered-3d-creation/)
- **Tripo (parent VAST):**
  - About **$200M raised in 2026** at unicorn status (>$1B). A $50M Series A was led by Alibaba (Mar 2026), then about $150M came from Geely Capital, **4399, Giant Network** and Fosun, among others.
  - It released Tripo H3.1 (detailed geometry) and P1.0 (production-ready meshes in seconds) in March 2026. VAST also names a "world model roadmap".
  - Sources: [GlobeNewswire](https://www.globenewswire.com/news-release/2026/06/01/3304603/0/en/tripo-ai-raises-nearly-200-million-in-series-a-and-series-a-financing-to-advance-ai-3d-and-world-model-roadmap.html); [Implicator](https://www.implicator.ai/vast-raises-nearly-200-million-for-tripo-ai-3d-models/); [Yinji](https://yinji3d.com/en/news/tripo-ai-funding-2026/)
- **Hyper3D / Deemos (Rodin):** a new round of "hundreds of millions" (currency unclear, likely RMB) and Rodin Gen-2.5 (mid-2026). It reached **$1M ARR within 45 days** of launch — [3Druck](https://3druck.com/en/programs/hyper3d-chinese-ai-3d-model-platform-secures-millions-in-funding-in-series-a-round-54143154/); [Tracxn](https://tracxn.com/d/companies/hyper3d/__siHfR_jpS-90Lcf9ntD5YONsKXVhFv_5yTb5IfSo2ZM)
- Industry view: an "AI 3D generation funding boom" in 2026 — [Neural4D blog](https://blog.neural4d.com/neural4d/ai-3d-generation-funding-boom/)

**Audio and voice**
- **ElevenLabs:**
  - The CEO said ARR passed **$330M at end-2025** — [TechCrunch](https://techcrunch.com/2026/01/13/elevenlabs-ceo-says-the-voice-ai-startup-crossed-330-million-arr-last-year/)
  - **$500M Series D at an $11B valuation** (Feb 2026, led by Sequoia) — [ElevenLabs](https://elevenlabs.io/blog/series-d)
  - Later passed **$500M ARR** — [ElevenLabs](https://elevenlabs.io/blog/500m-arr-and-new-investors). A third-party write-up claims about $600M ARR by June 2026 (unverified) — [Postbeam](https://www.postbeam.ai/blog/how-elevenlabs-grows)
  - Game customers include Paradox Interactive. Its voice marketplace pays voice actors royalties (about $0.03 per 1,000 characters) — [Sacra](https://sacra.com/c/elevenlabs/)
  - ElevenLabs voices Fortnite's creator NPC "Conversations" (§1) — [Wccftech](https://wccftech.com/fortnite-uefn-ai-npc-conversations-gemini-elevenlabs/)

**Engines and code agents**
- **Unity AI (Unity 6+)** includes:
  - a project-aware in-editor assistant/agent
  - AI generators for placeholder materials, sounds and cubemaps
  - an **AI Gateway to bring third-party agents such as Claude into Unity**, and an **official Unity MCP server**
  - models from third parties such as Google Gemini
  - Sources: [Unity: What is Unity AI](https://unity.com/resources/what-is-unity-ai); [Unity blog](https://unity.com/blog/unity-ai-how-to-get-started); [Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/unity-6-introduces-built-in-ai-suite-for-faster-game-creation)
- **Unity 2026 Game Development Report** (as summarized; not read in full):
  - Back-end AI use is mainly **coding assistance (62%)** and **writing/narrative (44%)**
  - **50% of developers use MCP servers**; among them 90% use them for engine/editor connectivity and 74% for production and project management
  - "70% of Unity developers credit AI with faster, lower-cost production"
  - Source: [Unity 2026 report](https://unity.com/blog/2026-unity-game-development-report-trends)
- **Epic / Unreal:**
  - **UE 5.8 (17 Jun 2026)** added an experimental **MCP plugin** that exposes the project to models such as Claude to operate inside the editor.
  - At State of Unreal 2026, Epic announced **Unreal Engine 6** with Claude and Gemini integrations "integral". Early access is slated for **late 2027**, covering level assembly, character setup, code assistance, crash analysis and test generation.
  - Epic stresses the editor stays "in developers' hands". UE6 is also reported to converge Unreal and Fortnite/UEFN.
  - Sources: [Dataconomy](https://dataconomy.com/2026/06/18/unreal-engine-6-generative-ai-integration/); [Wccftech](https://wccftech.com/epic-games-unreal-engine-6-claude-gemini-developer-control/); [Engadget](https://www.engadget.com/2196807/epic-games-details-how-its-embracing-gen-ai-in-unreal-engine/); [Tech Insider](https://tech-insider.org/unreal-engine-6-state-of-unreal-2026/)
- Third-party tools such as Ludus AI fill the gap of a built-in Unreal assistant — [Ludus AI blog](https://ludusengine.com/blog/unreal-engine-built-in-ai-assistant)

**QA**
- **nunu.ai** raised a **$6M seed**, co-led by **a16z speedrun** and TIRTA with YC participating, for $8M in total. It builds multimodal agents that play and test games — [PocketGamer.biz](https://www.pocketgamer.biz/nunuai-secures-6m-to-scale-ai-agents-for-game-qa/); [Startupticker](https://www.startupticker.ch/en/news/nunu-ai-closes-6-million-seed-round)
- Game-QA AI startups have raised **only about $35.8M combined** (led by modl.ai and nunu.ai), and **none has reached Series B scale** — [Naavik: State of AI for Game QA](https://naavik.co/ai-gaming/the-state-of-ai-for-game-qa/). Filuta AI is another entrant — [CB Insights](https://www.cbinsights.com/company/filuta-ai/financials)

**Investors seen in the deals above:** Sequoia (ElevenLabs, Astrocade, Decart), a16z (World Labs; the speedrun program in nunu.ai), NVIDIA (World Labs, Decart, Astrocade), Khosla (General Intuition). Chinese strategic investors include Alibaba, Geely, 4399 and Giant Network (Tripo).

### Inferences
- **Value capture by stage (inference):**
  - Asset generation (3D, voice, texture) is the first stage with nine-figure revenue businesses.
  - Code and editor agents are being absorbed into engines through MCP. Rents flow to the frontier-model providers and the engine owners, which leaves thin room for standalone "AI for Unity/Unreal" plug-ins.
  - QA, localization and player-support AI remain small, services-like markets.
- **Horizontal demand justifies the valuations.** Meshy, Tripo and ElevenLabs sell to games plus e-commerce, 3D printing, film, ads and education. Game studios are one customer segment among many, so game budgets alone do not determine these companies' prospects.
- **Chinese game companies are investing strategically in AI 3D** (4399 and Giant in Tripo). Studios want influence over supply of the asset-generation layer.

### Gaps
- Not researched due to the search cap:
  - animation and motion: Move.ai, Cascadeur, Kinetix
  - CSM, Kaedim and the Hunyuan3D adoption numbers
  - texturing-specific tools
  - localization and player-support AI
  - UA creative generation (UNVERIFIED LEAD: Sett raised about $27M for AI agents making playable ads; AppLovin's AXON dominates ad optimization)
  - Konvoy, Griffin and a16z Speedrun aggregate funding data
  - AI acquisitions (UNVERIFIED LEADS: Netflix bought Ready Player Me in late 2025; Canva bought Leonardo.ai in 2024)
- No survey found quantifying Cursor or Claude Code usage specifically among game developers, beyond Unity's MCP and coding-assistance percentages.
- UNVERIFIED LEAD: a Google Cloud/Harris survey (Aug 2025) reported about 90% of game developers using AI agents or AI in their workflows.

---

## 5. Market size, economics, supply glut and discoverability

### Takeaway
The overall market is growing at mid-single digits globally and low double digits in China, driven by **deeper spending per player, not more players**. Content supply is growing much faster (Steam releases about +23% annualized in 2026; China's mini-game developer base above 500K). That combination, flat attention plus falling content cost, points to per-title revenue compression and to **distribution, UA and taste/IP as the scarce resources**. Hard, audited evidence that AI has cut total development budgets was not found.

### Cited Findings
- **Newzoo 2026 forecast:**
  - Global games revenue of **$213.9B (+6.1%)**: mobile $121.1B (about 57%), console $46.9B, PC $45.9B
  - **3.7B players**, of which **1.65B payers (+4.7%)**; mobile has 3.10B players, PC 977M and console 651M
  - Growth increasingly comes from **deeper spending per player rather than more downloads**, and audience growth is slowing
  - Sources: [PocketGamer.biz](https://www.pocketgamer.biz/no-single-model-for-growth-says-newzoo/); [Game Wisdom](https://game-wisdom.com/general/global-games-market-grows-toward-213-9-billion); [Storyboard18](https://www.storyboard18.com/amp/gaming-news/global-games-market-to-hit-2139b-by-2026-growth-slows-ws-l-110433.htm); [G-M News](https://g-mnews.com/en/global-games-market-will-generate-usd-213-9-billion-in-2026/)
  - Consistency flag: +6.1% implies a 2025 base of about $201.6B, above earlier Newzoo 2025 estimates of about $189B (background knowledge). This suggests a methodology revision; check before comparing years.
- **China, H1 2026 (游戏工委, 30 Jul 2026):**
  - Domestic revenue **¥188.45B (+12.17%)**; users **684M (+0.82%)**
  - Self-developed games: domestic ¥163.356B (+16.31%); **overseas $12.372B (+30.22%)**
  - Mobile +7.9%; **PC/client +27.92%**; mobile shooters became the top-grossing genre; mini-program games stood out
  - Sources: [腾讯新闻](https://news.qq.com/rain/a/20260730A0AJA000); [新华网](https://www3.xinhuanet.com/tech/20260731/c5593cc57b18411ab328cd3ed98b554c/c.html); [新浪科技](https://finance.sina.com.cn/tech/roll/2026-07-30/doc-inikqupy9622230.shtml); [机核](https://www.gcores.com/articles/217761); [东方财富](https://wap.eastmoney.com/a/202607303827120269.html)
- **Discoverability:** about half of Steam's 19K+ 2025 releases got fewer than 10 reviews — [80.lv](https://80.lv/articles/steam-earned-usd16b-in-2025-but-nearly-half-of-19-000-games-got-under-10-reviews); [PC Guide](https://www.pcguide.com/news/steam-breaks-another-record-for-annual-game-releases-but-almost-half-of-them-have-fewer-than-10-reviews/)
- **Attention vs conversion:** Suck Up! reached about 100M YouTube views with only an estimated 12K Steam copies (§1) — [Proxima](https://www.proxima.gg/); [GameRevenueData](https://gamerevenuedata.com/games/suck-up/)
- **Cost claims (surveys and vendors only):**
  - "70% of Unity developers credit AI with faster, lower-cost production" — [Unity 2026 report](https://unity.com/blog/2026-unity-game-development-report-trends)
  - Meshy's "a minute and a dollar" per usable 3D model versus weeks previously (vendor claim) — [PR Newswire](https://www.prnewswire.com/news-releases/meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-302828384.html)
  - WeChat says AI has lowered art and testing costs for mini-games (no figure given) — [腾讯新闻](https://news.qq.com/rain/a/20260529A05IF300?id=20260529A05IF300&path=a&app=news&suid=&redirect_pc=1)
- **Public-market sensitivity:** the Project Genie selloff (§2) and Roblox shares falling on its Q3 bookings guidance (§3) — [Investing.com](https://www.investing.com/news/stock-market-news/unity-stock-falls-alongside-taketwo--roblox-after-googles-project-genie-launch-4476580); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-roblox-q2-2026-beats-eps-but-shares-sink-on-bookings-93CH-4826338)

### Inferences
- **Supply is outgrowing demand:**
  - Global revenue +6% and China users +0.8%
  - versus Steam releases about +23% (2026 pace), 5,000+ new WeChat mini-game publishers in 2025, and Astrocade's 75K games in 8 months
- **Expected consequences (inference):**
  - (a) Median revenue per title falls further.
  - (b) UA and distribution costs, and platform take, gain relative power: Steam, WeChat, Roblox, Fortnite, app stores, and the influencer/streamer channel.
  - (c) Curation, brand, IP and "taste" (knowing what is fun and polishing the last 20%) become the scarce inputs.
- **Where growth is real (China, 2026):** client/PC (+28%), overseas (+30%) and mini-games (+34% in 2025). These are the segments where AI-enabled cost reduction and volume could matter most.

### Gaps
- Not found in-session:
  - Newzoo 2023–2025 actuals
  - Circana US spending
  - 游戏工委 full-year 2024/2025 totals. UNVERIFIED LEADS: 2024 about ¥325.8B (+7.5%); 2025 about ¥350.8B (+7.7%).
  - Layoff counts for 2024–2026. UNVERIFIED LEAD: about 10.5K (2023) and about 14.6K (2024) per public trackers; Microsoft cut about 9,000 roles in July 2025, including Xbox studios.
- No audited or quantitative case study of AI reducing a shipped game's total budget or schedule was found.
- UNVERIFIED LEADS on AI cost claims:
  - Square Enix's goal to automate about 70% of QA with generative AI by end-2027
  - Reports that the EA take-private ($55B, PIF/Silver Lake/Affinity, announced Sept 2025) relies on AI-driven cost cuts
  - Chinese reports of large AI-driven cuts to 2D art headcount
- UA cost trends and data on AI-generated ad creatives were not found.

---

## 6. Risks and constraints: player acceptance, platform policy, regulation, IP/copyright, labor

### Takeaway
Verified in-session evidence on risks is thin because the search cap was hit before these queries ran. What is sourced shows four things:
- **Disclosure is becoming normal but inconsistent.** Steam requires it and about 20% of new releases comply. Where Winds Meet added its disclosure weeks after launch, and rival stores reportedly have no equivalent rule.
- **Platforms are setting AI-NPC content rules.** Epic bans romance simulation and medical advice.
- **Companion-style AI faces child-safety crackdowns.** Character.AI banned open-ended chat for under-18s.
- **Economic fragility.** Rec Room's AI costs.

Player-backlash cases, regulation (China labeling rules, EU AI Act Art. 50), copyright rulings and labor agreements are **gaps in this session**; leads are listed below for verification.

### Cited Findings
- **Steam disclosure practice:** about 20% of 2025 releases and 7,818 titles disclose generative AI — [Tom's Hardware](https://www.tomshardware.com/video-games/pc-gaming/1-in-5-steam-games-released-in-2025-use-generative-ai-up-nearly-700-percent-year-on-year-7-818-titles-disclose-genai-asset-usage-7-percent-of-entire-steam-library). Where Winds Meet shipped live LLM NPCs and only added the disclosure on 12 Dec 2025 — [Arcanum RPGs](https://arcanumrpgs.com/blog/where-winds-meet-ai/). A 2026 headline says rival stores "skip" disclosure — [Tech Insider](https://tech-insider.org/steam-ai-disclosure-2026/). A law-firm guide covers Steam AI policy — [Legal Moves](https://legalmoveslawfirm.com/steam-ai-policy/)
- **Platform content rules for AI NPCs:** Epic bans romance simulation, medical advice and hateful content in UEFN AI NPCs and says it does not store player audio — [Wccftech](https://wccftech.com/fortnite-uefn-ai-npc-conversations-gemini-elevenlabs/)
- **Child safety and companion AI:** Character.AI ended open-ended chat for under-18s (Nov 2025) after lawsuits alleging psychological harm and introduced Persona-based age checks — [CNBC](https://www.cnbc.com/2025/11/24/characterai-to-ban-teens-from-open-ended-chats-human-interaction-is-crucial-psychotherapist-says.html); [TechCrunch](https://techcrunch.com/2025/10/29/character-ai-is-killing-the-chatbot-experience-for-minors/?rand=23331)
- **Player reception of AI NPCs is mixed:** "best feature" (Wccftech) versus "overshadowed the combat" (PCGamesN) in Where Winds Meet — [Wccftech](https://wccftech.com/where-winds-meet-ai-chatbot-npcs-are-unironically-the-games-best-feature/); [PCGamesN](https://www.pcgamesn.com/where-winds-meet/reception-ai-chatbots)
- **IP:** media flagged that Project Genie could create "playable, copyrighted worlds" — [Sherwood News](https://sherwood.news/markets/gaming-stocks-plunge-following-release-of-googles-ai-tool-that-can-create/)
- **Economic risk:** Rec Room's AI features reportedly cost more per user than subscriptions brought in, before its shutdown — [GeekWire](https://www.geekwire.com/2026/rec-room-shutting-down-seattles-3-5b-social-gaming-platform-says-it-cant-make-the-business-work/); [TechCrunch](https://techcrunch.com/2026/03/31/social-gaming-platform-rec-room-once-valued-at-3-5b-is-shutting-down/)
- **Voice-actor economics:** ElevenLabs' marketplace pays royalties of about $0.03 per 1,000 characters to actors who license voice clones. This is one emerging consent-and-pay model — [Sacra](https://sacra.com/c/elevenlabs/)

### Inferences
- Governance is converging on **disclosure plus content rules plus age gating**, not bans. The biggest open risks for AI features in games are:
  - (a) minors and companion-style emotional attachment
  - (b) IP leakage from generative models
  - (c) reputational backlash in core PC/console communities
  - (d) cost overruns from per-user inference
- The fast growth of AI-disclosed Steam titles suggests the stigma is not stopping supply. The **demand-side** effect (sales of disclosed vs non-disclosed games) is unmeasured in this session.

### Gaps
Unresolved, with UNVERIFIED LEADS from background knowledge. Each needs a primary source before use.
- **Player sentiment surveys.** No 2025–2026 consumer survey was retrieved. GDC State of the Industry: the 2025 survey reportedly found about 30% of developers saw generative AI as having a negative impact (up from about 18%) and about 52% worked at companies using it. The 2026 figures were not retrieved.
- **Backlash cases:**
  - **Clair Obscur: Expedition 33.** The Indie Game Awards (Dec 2025) reportedly rescinded its Game of the Year and Debut awards after Sandfall confirmed that generative-AI placeholder textures shipped at launch (later patched).
  - **ARC Raiders.** Embark used TTS voices built from contracted actors. Some reviews criticized this (e.g., a low Eurogamer score), yet the game was a major commercial hit.
  - Other reported cases: Call of Duty: Black Ops 7 AI art (Nov 2025); Larian's Swen Vincke comments on generative AI for concepting (Dec 2025).
- **Platform policies:**
  - Steam introduced disclosure in Jan 2024 and reportedly revised it in Jan 2026 to focus on AI content that ships to players rather than efficiency tools such as code assistants.
  - Tim Sweeney argued (Nov 2025) that "made with AI" tags make little sense for game stores because AI will be involved in nearly all production. One 2026 summary garbled this, so verify.
  - Apple, Google, Sony, Nintendo and Microsoft console AI policies were not researched.
- **China:**
  - 《人工智能生成合成内容标识办法》 (CAC, MIIT, MPS and NRTA; issued 14 Mar 2025; **effective 1 Sep 2025**) requires explicit and implicit labels on AI-generated content, alongside the mandatory standard GB 45438-2025.
  - The CAC reportedly released draft rules on "anthropomorphic AI interactive services" (人工智能拟人化互动服务) in Dec 2025, directly relevant to AI companions and NPCs.
  - How the NPPA 版号 review handles AI content was not established.
- **EU AI Act Art. 50** transparency obligations (chatbot disclosure, machine-readable marking, deepfake labels, with a lighter-touch rule for evidently artistic or fictional works) apply from **2 Aug 2026**. The Commission's Digital Omnibus (Nov 2025) proposed some timing relief. Current status is unverified.
- **Copyright:**
  - The US Copyright Office's Part 2 report (29 Jan 2025) says purely AI-generated material is not copyrightable, prompts alone are insufficient, and human-authored selection, arrangement or modification can be protected. Part 3 (pre-publication, May 2025) covers training.
  - *Thaler v. Perlmutter* (D.C. Cir., Mar 2025) affirmed the human-authorship requirement.
  - China: the Beijing Internet Court (Nov 2023, Li v. Liu) protected an AI-assisted image where human input was sufficient. Later local courts (e.g., Zhangjiagang, 2025) reportedly denied protection when users could not show the creative process. The Guangzhou Internet Court's Ultraman case (2024) found an AI platform liable for infringing output.
- **Labor:**
  - The SAG-AFTRA video game strike (Jul 2024 – mid-2025) ended with an agreement ratified in Jul 2025 that adds consent and disclosure requirements for digital replicas.
  - SAG-AFTRA filed an unfair-labor-practice charge over Fortnite's AI Darth Vader voice (May 2025).
  - Status of UK Equity and Chinese illustrator displacement was not researched.

---

## 7. Expert and industry forecasts: where value will accrue; what is contested

### Takeaway
The sourced statements show platform holders betting that **AI will turn every player into a creator inside their walled gardens**:
- Roblox: "any creator" generating full scenes, assets, code and animation.
- Epic: UE6 with Claude and Gemini built in, plus Fortnite Conversations.
- Tencent: HY World 2.0 moving "AI creating worlds" to industrial application.
- WeChat: natural-language mini-game creation.

Investors are betting on **world models and gameplay data** (World Labs, General Intuition, Decart). Contested points:
- whether neural world models threaten engines and platforms (market fear vs the "category error" critique)
- whether AI-native gameplay can monetize
- whether AI mainly helps incumbents with distribution or empowers new entrants

Direct quotes from Jensen Huang, Microsoft Gaming leadership, Tencent/NetEase executives, Krafton's CEO and a16z could not be retrieved this session.

### Cited Findings
- **Roblox:** four AI pillars (coding, 3D objects, multiplayer NPCs, video/realism). The stated aim is that 4D generation and Cube will eventually let any creator generate full scenes, including assets, environments, code and animation, from natural-language prompts — [GamesBeat RDC 2026](https://gamesbeat.com/roblox-dives-into-the-details-on-its-rdc-engine-updates-roblox-wallet-and-offline-play-press-briefing/); [Roblox Newsroom](https://about.roblox.com/newsroom/2026/02/accelerating-creation-powered-roblox-cube-foundation-model)
- **Epic:** UE6 (early access late 2027) will integrate Claude and Gemini through MCP while keeping "the editor in developers' hands". UE 5.8 already has an MCP plugin — [Wccftech](https://wccftech.com/epic-games-unreal-engine-6-claude-gemini-developer-control/); [Dataconomy](https://dataconomy.com/2026/06/18/unreal-engine-6-generative-ai-integration/). Coverage attributes to Tim Sweeney the view that "made with AI" labels matter for art exhibits and content-licensing contexts rather than game stores (paraphrased; verify wording) — [Dataconomy](https://dataconomy.com/2026/06/18/unreal-engine-6-generative-ai-integration/)
- **Tencent:** HY World 2.0 is positioned as moving "AI creating worlds" from concept to industrial application, with game-workflow integration — [IT之家](https://www.ithome.com/0/939/747.htm); [东方财富](https://finance.eastmoney.com/a/202604173708636551.html)
- **WeChat (Tencent):** future mini-game winners need "AI 提效 + 玩法创意 + 精准运营", and the platform is building natural-language AI coding for ordinary users — [腾讯新闻](https://news.qq.com/rain/a/20260529A05IF300?id=20260529A05IF300&path=a&app=news&suid=&redirect_pc=1)
- **Krafton:** its "AI-first" strategy is explicitly tied to co-op AI features (PUBG Ally) and AI modding tools (inZOI) — [Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/krafton-q1-2026-revenue-surges-57-via-pubg-ai-first-strategy)
- **Investors:**
  - General Intuition is described as Khosla's largest bet since OpenAI (Latent Space title) — [Latent Space](https://www.latent.space/p/world-models-and-general-intuition)
  - a16z and NVIDIA back World Labs — [World Labs](https://www.worldlabs.ai/blog/funding-2026)
  - Sequoia backs Astrocade and ElevenLabs; a16z speedrun co-led nunu.ai (§4)
  - Hartmann Capital's Q3 2025 report is titled "The AI Revolution Reshaping Gaming" (not read) — [Hartmann Capital](https://hartmanncapital.substack.com/p/the-ai-revolution-reshaping-gaming)
- **Contested:**
  - Naavik ("category error") and Kotaku ("very dumb reason") versus the market's Project Genie selloff — [Naavik](https://naavik.co/digest/project-genie-and-the-stock-markets-category-error/); [Kotaku](https://kotaku.com/video-game-stocks-down-take-two-gta-nintendo-roblox-unity-google-ai-game-maker-2000664594)
  - Muse was described as "impressive but utterly baffling" — [Newsweek](https://www.newsweek.com/entertainment/video-games/opinion-microsofts-generative-ai-model-muse-impressive-utterly-baffling-2033713)
  - Joseph Kim argues the "last 20%" (polish and design) holds the value — [Gamemakers](https://www.gamemakers.com/p/the-last-20-is-worth-100-million)

### Inferences
- **Consensus among platform holders (inference):** gen AI is a *creation-funnel expander* that platforms own (Roblox, Fortnite, WeChat, and Unity/Unreal as model hosts). The strategic battle is over who owns the creator and player relationship once creation cost collapses.
- **Contested areas:**
  - (1) Do neural world models displace engines (bull case: Project Genie and investors) or feed them (skeptics: Naavik)?
  - (2) Does AI-native gameplay (NPC conversation, infinite content) create new willingness to pay, or is it a feature that raises engagement inside existing hits?
  - (3) Do the gains go to incumbents with distribution (current evidence: Where Winds Meet, Fortnite, Roblox) or to AI-native newcomers (Astrocade: 20M users but no disclosed revenue)?

### Gaps
- UNVERIFIED LEADS:
  - **Jensen Huang** has said repeatedly that future games will have pixels "generated, not rendered", with fully AI-generated games within about 5–10 years.
  - **Microsoft Gaming**: Phil Spencer framed Muse around preservation and ideation (2025). Reports in early 2026 say Spencer retired and Asha Sharma (from Microsoft CoreAI) became CEO of Microsoft Gaming.
  - **Krafton's CEO** declared "AI First" in Oct 2025, with a large GPU-cluster investment.
  - **Roblox CEO David Baszucki** has repeatedly framed AI as enabling every user to create.
  - **Tencent (Martin Lau) and NetEase (Ding Lei)** earnings-call statements on AI productivity in game development.
  - **a16z games** partners (e.g., Jonathan Lai) on AI-native games and Speedrun cohorts.
  - **xAI/Elon Musk** said he aimed to release an AI-generated game by end-2026.
- None of these were retrieved or verified in-session.

---

## 8. Opportunity map: segments, traction, key players, main risks

### Takeaway
The strongest evidence of traction (revenue, payouts, users) is in four places:
- (1) **UGC platforms adding AI creation**
- (2) **horizontal asset generation (3D, voice)**
- (3) **engine-embedded agentic tooling**
- (4) **China mini-games built by small AI-assisted teams**

Venture capital is heavily funding **world models** ahead of game revenue. **Standalone AI-native games and NPC middleware** show attention but weak monetization, and several stalled or failed. As content cost falls, scarcity moves to **distribution, IP and taste**, which favors platforms, publishers with audiences and curation/UA businesses.

### Cited Findings
- All evidence is cited in §§1–7. Key anchors:
  - Roblox DevEx $363M in Q2 2026 — [Roblox Q2 2026 letter](https://www.sec.gov/Archives/edgar/data/0001315098/000162828026051059/ex991-robloxq22026earnin.htm)
  - UEFN payouts $1B cumulative — [Tubefilter](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/)
  - Meshy $40M ARR — [PR Newswire](https://www.prnewswire.com/news-releases/meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-302828384.html)
  - ElevenLabs $330M+ ARR at end-2025 — [TechCrunch](https://techcrunch.com/2026/01/13/elevenlabs-ceo-says-the-voice-ai-startup-crossed-330-million-arr-last-year/)
  - China mini-games ¥53.5B (+34%) — [证券日报](http://www.zqrb.cn/gscy/gongsi/2026-01-17/A1768566351773.html)
  - Steam 19,468 releases in 2025, about half with fewer than 10 reviews — [SteamDB](https://steamdb.info/stats/releases/); [80.lv](https://80.lv/articles/steam-earned-usd16b-in-2025-but-nearly-half-of-19-000-games-got-under-10-reviews)
  - Rec Room shutdown — [GeekWire](https://www.geekwire.com/2026/rec-room-shutting-down-seattles-3-5b-social-gaming-platform-says-it-cant-make-the-business-work/)

### Inferences
Each area below is rated for **evidence strength** (Strong, Medium or Weak) and **opportunity type**.

1. **AI-accelerated UGC and creator platforms.** Evidence: Strong. Type: platform or tools for creators.
   - *Traction:*
     - Roblox DevEx $363M a quarter (+15%) and DAU 123M
     - Fortnite about $370M in 2025 payouts, $1B cumulative
     - Roblox Cube/4D and mobile text-to-world at RDC 2026
     - Fortnite Conversations publishable from Jul 2026
     - Astrocade 20M users in 8 months
   - *Players:* Roblox, Epic (UEFN), Astrocade, Rosebud, Spawn; Dynamics Lab (Mirage/Magica) as an AI-native challenger.
   - *Risks:*
     - hit-driven volatility (Roblox Q3 guide down 14–18%)
     - per-user inference cost (Rec Room)
     - child safety and moderation of AI-generated content
     - platform dependence for creators
     - AI-slop flooding discovery

2. **Horizontal asset generation (3D, texture, voice) sold into games.** Evidence: Strong for 3D and voice revenue. Type: SaaS or API.
   - *Traction:*
     - Meshy: $15M → $40M ARR in about 5 months, $1.5B valuation, 100M+ models
     - Tripo: about $200M raised, with 4399 and Giant as strategics
     - Hyper3D: $1M ARR in 45 days
     - ElevenLabs: $330M+ ARR at end-2025, then $500M+
     - about 60% of Steam AI disclosures involve visual assets
   - *Players:* Meshy, Tripo/VAST, Hyper3D/Deemos, Tencent Hunyuan3D (open source), ElevenLabs. Not researched: CSM, Kaedim.
   - *Risks:*
     - commoditization by open-source models (Hunyuan) and frontier labs
     - IP and copyright status of outputs (human-authorship requirements)
     - player backlash in core PC/console audiences
     - price compression
     - labor and consent disputes over voice

3. **Agentic engine tooling (code, editor automation, MCP).** Evidence: Medium-Strong on adoption, weak on measured productivity. Type: engine features and model-provider revenue; thin room for independents.
   - *Traction:*
     - Unity AI Gateway and official MCP server; 50% of surveyed Unity developers use MCP; 62% use AI coding assistance
     - UE 5.8 MCP plugin; UE6 with Claude and Gemini integral (early access late 2027)
     - WeChat building natural-language game coding
   - *Players:* Unity, Epic, Anthropic (Claude), Google (Gemini), Ludus AI and other plug-ins.
   - *Risks:*
     - rents captured by engines and model labs
     - reliability on large codebases
     - studio data and IP security
     - pushback from unions and developers

4. **China mini-games and small-team AI production.** Evidence: Strong for market growth, Medium for the AI contribution. Type: studios, publishing, tools.
   - *Traction:* ¥53.5B in 2025 (+34.39%), 500K+ WeChat developers, >80% of them teams under 30 people, 300+ titles above ¥10M in a quarter, and the platform saying AI has cut art and testing costs.
   - *Players:* WeChat, Douyin, small studios, AI tool vendors.
   - *Risks:*
     - platform take and traffic allocation
     - IAA ad dependence (32% of revenue)
     - 版号 and content-labeling compliance (标识办法)
     - copycat speed as AI lowers cloning cost

5. **AI features inside incumbent live games (NPCs, co-players, companions).** Evidence: Medium on reach, Weak on monetization. Type: feature differentiation; middleware and inference vendors.
   - *Traction:* Where Winds Meet (2M players on day 1; LLM "Jianghu Friends"), Justice Mobile's AI NPC ecosystem, inZOI (1M in a week; on-device Smart Zoi), PUBG Ally beta (Jun 2026), Fortnite Conversations.
   - *Players:* NetEase (Fuxi), Krafton, Epic, NVIDIA ACE, Google Gemini, ElevenLabs. Inworld and Convai are the middleware incumbents, and Inworld is moving toward general consumer apps.
   - *Risks:*
     - no demonstrated ARPU or retention uplift
     - jailbreaks and controllability
     - safety (minors)
     - hardware limits of on-device SLMs
     - disclosure missteps (Where Winds Meet's late Steam disclosure)

6. **Standalone AI-native games and AI RPG/companion apps.** Evidence: Weak commercially. Type: high-variance consumer bets.
   - *Traction:* viral but modest sales. Suck Up! had about 100M views vs an estimated 12K Steam copies. Whispers from the Star has about 1.5K Steam reviews. Latitude's estimated ARR is low single-digit millions (low confidence) and Voyage is in beta. Character.AI is at about $30–50M revenue but banned under-18 open chat.
   - *Players:* Anuttacon, Proxima, Latitude/Voyage, Character.AI.
   - *Risks:*
     - novelty decay
     - inference cost per session
     - regulation of companion AI (child safety; China's reported anthropomorphic-AI draft rules)
     - "last 20%" design and polish gap

7. **World models / generative interactive environments.** Evidence: Strong on capital, Weak on game revenue. Type: frontier-lab platforms; near-term use in previs, blockout and UGC toys.
   - *Traction:*
     - Project Genie is live for paying consumers
     - World Labs $1B at about $5B, with Marble commercial and exporting editable 3D
     - Decart $300M at about $4B, but its revenue push is AV driving simulation
     - General Intuition $320M at $2.3B, trained on game clips
     - Tencent HY World 2.0 open-sourced for game workflows
   - *Players:* Google DeepMind, World Labs, Decart, General Intuition, Tencent Hunyuan, Microsoft Muse, Dynamics Lab. Not researched: Skywork Matrix-Game, Odyssey, Runway.
   - *Risks:*
     - about 1-minute sessions at 720p/24fps; weak persistence, determinism and multiplayer
     - GPU cost per user
     - IP (the "copyrighted worlds" critique)
     - startups pivoting away from games toward robotics and AV
     - timelines unproven (speculation: hybrid engine plus generative layer before fully neural games)

8. **Gameplay data as an asset (licensing clips and telemetry to AI labs).** Evidence: Medium (large rounds; revenue undisclosed). Type: data licensing and new revenue for platforms and publishers.
   - *Traction:* General Intuition's model rests on Medal's roughly 2B action-labelled clips a year. OpenAI's reported interest in buying that data. Muse was trained on a first-party game's data.
   - *Players:* Medal/General Intuition, publishers with telemetry, clip and streaming platforms.
   - *Risks:* player-consent and privacy law; publisher ToS and IP ownership of footage; concentration of buyers.

9. **Discovery, curation, UA and "taste" layers for an oversupplied market.** Evidence: Medium on the structural need, Weak on specific winners in-session. Type: curation, marketing tech, publishing, IP.
   - *Traction:* about half of Steam's 19.5K 2025 releases got fewer than 10 reviews; Steam's 2026 pace is about 24K; global payers grow only about 4.7% and China users about 0.8%; Newzoo says growth comes from deeper spending per player.
   - *Players:* platform stores (Steam, WeChat, Roblox and Fortnite discovery), publishers with IP and brand, influencer marketing, UA and creative-generation vendors (not researched).
   - *Risks:* platforms internalize curation; ad-network concentration; AI-generated creative fatigue.

10. **Game QA, localization and player-support automation.** Evidence: Weak-Medium; small but steady. Type: B2B services and SaaS.
    - *Traction:* nunu.ai $6M seed (a16z speedrun); game-QA AI startups at about $35.8M combined, none at Series B.
    - *Players:* modl.ai, nunu.ai, Filuta; background leads include large publishers' in-house programs (e.g., Square Enix's QA automation target).
    - *Risks:* small total market; engines and model labs bundling testing agents (UE6 lists test generation); in-house builds by large publishers.

**Structural shifts (inference, graded against the evidence above):**
- **Content cost trending toward zero:** supported for discrete assets (3D, voice, placeholder art) by vendor metrics and developer surveys. **Not demonstrated** for full-game budgets, where no audited case was found.
- **Many more games:** supported by Steam (9.7K in 2020 → 19.5K in 2025 → about 24K pace in 2026), WeChat's developer base (500K+) and Astrocade (75K games in 8 months). The causal share attributable to AI is unquantified.
- **Personalization (AI NPCs, companions, generated worlds):** plausible and shipping, but monetization is unproven. Safety and regulation are the binding constraints.
- **Creators replacing studios in some genres:** supported in UGC platforms (about $1.4B/yr Roblox run-rate, about $370M/yr Fortnite) and Chinese mini-games (>80% of developers are teams under 30 people). Less evidence for premium PC/console.
- **Scarcity shifting from production to taste, IP and distribution:** strongly implied by the supply-versus-attention data and by attention-without-conversion cases (Suck Up!). It is also consistent with investors paying for platforms and data (Roblox, Epic, General Intuition) rather than for standalone AI games.

### Gaps
- The map omits UA creative generation, localization, player support, animation/motion capture and AI-assisted live-ops analytics, because the search budget ran out before they were researched.
- No sourced timelines for world models in production; no sourced consumer-sentiment data for 2025–2026; no verified regulatory or copyright details. See the §6–7 leads, which must be verified before the report relies on them.
