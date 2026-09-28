# AI 抬高产能，游戏价值仍看打磨

## 摘要

本报告的数据截至 2026 年 9 月；口径与来源见正文，凡标为"自报""公司说法""估算""预测"的数字都不是独立测量。对用户三个问题的回答如下。

**问题一（编程领域的渗透趋势）。** 编程领域的 AI 扩散已经从"要不要用"进入"交给代理做多少"：开发者层面的使用广度在 2025 年前后基本见顶（Stack Overflow"正在使用或计划使用"从 2023 年的 70% 升到 2025 年的 84%，DORA 2025 为 90%），约一半职业开发者每天使用，真正还在陡峭上升的是代理委托（JetBrains 调查中 Claude Code 的工作使用率半年内从 18% 升到 39%）。"AI 写了多少代码"则完全取决于口径：独立分类器估计 2024 年末美国 Python 函数约 29% 由 AI 编写，公开 GitHub 提交中可识别的单一代理署名份额只有约 4%（下限），而头部公司 2025–26 年自报的 50%–80% 都没有公开定义。代码份额也不等于工作份额：Google 称 AI 贡献约 30% 的代码生成，整体工程速度却只提高约 10%。

**问题二（创意、执行量产、决策三类工作的比例）。** 必须分开记两本账。产出账本里机器量产的份额和总产量大幅上升——用户"因 AI 产能提升，量产类占比上升"的假设在产出口径上成立；但在人的工时账本里，执行类占比在代理时代是下降的：代理会话中人保留约 70% 的规划决策、只做约 20% 的执行决策，瓶颈移到了评审、测试和验收（PR 评审时长 +91% 至 +441.5%），创意定向的份额持平到上升。所以第三类工作更准确的名字是"决策/验收"而不是"决策/迭代"；而"指挥代理"必须单列"E-委托"标签，否则 E 与 D 的分界一挪就能移动 10–20 个百分点。价值层面，"产量≠价值"在既有软件生产者的利润和宏观全要素生产率上成立（高置信），在 AI 工具层不成立（新增价值主要流向了模型与工具厂商和客户），在社会价值层面无法判定。

**问题三（外推到游戏：趋势与机会）。** 编程只占游戏业岗位的约两成，而游戏的主体劳动（美术、内容、测试、本地化）本身就是执行密集的，它们被一致性、版权与玩家可见性三道门把守，而不只是被可验证性把守。游戏工作者个人使用率三年停在 31%→36%→36%，认为 AI 有害的比例升到 52%；Steam 上 AI 标注作品已占 2026 年（截至 7 月）新发行的 30.8%，估算销量份额却只有约 10%–27%。因此最可能的趋势是"执行层降本 + 长尾供给稀释"，机会集中在玩家看不见的降本、把"品味"变成可校验信号的验证工程、UGC 平台与本地化带来的触达，以及规模仍小但直接创造新需求的 AI 原生体验；主要陷阱是高端 PC 与主机上可见的 AI 污名、模板化赛道的买量军备竞赛，以及推理成本与权利约束。

**结构。** 第一至四节是调研基线（问题一、问题二与游戏基线），第五节是编程→游戏的比较研究方法论（把用户的两条视角写成七条可证伪假设），第六、七节把方法论用于调研结果，得出外推、机会地图与十个季度监测指标；重型研究设计放在附录 A，口径说明与未采用的数字放在附录 B。

## 一、编程：九成开发者在用，增长已转向"交给代理做多少"

衡量编程领域的 AI 渗透，至少要分开三条曲线：**广度**（有没有用）、**强度**（用得多频繁、多长时间）、**委托与贡献**（交给 AI 做了多少、最终产出里 AI 占多少）。三条曲线处在各自 S 曲线的不同位置，把它们压成一个"渗透率"是最常见的误读。广度在 ChatGPT 发布后约两年半内基本见顶：Stack Overflow 年度调查中"正在使用或计划使用 AI 工具"的比例从 2023 年的 70% 升到 2024 年的 76%，再到 2025 年的 **84%**（2025 年 49,009 份答卷）([Stack Overflow 2025](https://survey.stackoverflow.co/2025/ai); [Stack Overflow 2023](https://stackoverflow.co/company/press/archive/developer-survey-2023/))；按 SO 新闻稿口径，职业开发者中"正在使用"的比例从 2023 年的 44% 升到 2024 年的 **62%** ([Stack Overflow 2024](https://stackoverflow.co/company/press/archive/stack-overflow-2024-developer-survey-gap-between-ai-use-trust/))，而 2025 年同口径数字未能确认，所以不能把 84% 接在 44%、62% 后面画成一条线。DORA 的技术从业者样本方向一致：2024 年 75% 以上的人依赖 AI 完成至少一项日常职责，2025 年 **90%** 在工作中使用 AI，使用时长中位数约每天 2 小时 ([DORA 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report); [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report); [Google](https://blog.google/innovation-and-ai/technology/developers-tools/dora-report-2025/))；JetBrains 从 2025 年的 85%"经常使用"升到 2026 年 1 月的 90% ([JetBrains 2025](https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/); [JetBrains 2026-04](https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/))。剩下的一成左右主要是受合规约束的环境和明确拒用者。

强度处在曲线中段：2025 年 **51%** 的职业开发者每天使用 AI 工具 ([Stack Overflow 2025 新闻稿](https://stackoverflow.co/company/press/archive/stack-overflow-2025-developer-survey/))。更值得注意的是使用与信任脱钩：同一调查里，不信任 AI 准确性的人（46%，2024 年为 31%）多于信任的人（33%），只有 3%"高度信任"，正面情绪从 2023–24 年的 70% 以上降到约 60%（SO 在别处还发布过一个 29% 的信任数字，题目与分母不同）([Stack Overflow 2025 结果](https://stackoverflow.blog/2025/12/29/developers-remain-willing-but-reluctant-to-use-ai-the-2025-developer-survey-results-are-here/))。扩散靠的是经济与竞争压力、组织规范，而不是好感——这是扩散后期的典型特征，也意味着瓶颈正在从"会不会用"转向"敢不敢收"。

真正还在陡峭上升的是委托层。SO 2025 年有 31% 的开发者在工作中使用 AI 代理，到 2026 年 5 月的脉冲调查，任意频率使用代理的比例升到 59%，但多数人仍"拴着绳子"使用 ([Stack Overflow 2026-05](https://stackoverflow.blog/2026/05/27/agents-on-a-leash-agentic-ai-remains-mostly-monitored-at-work/))；JetBrains 对 1.5 万余名职业开发者的调查显示，Claude Code 在工作中的使用率从 2025 年 4 月的 3%、2026 年 1 月的 18% 升到 2026 年年中的 **39%**，GitHub Copilot 则从一年前的 29% 降到 21%，Cursor 从 18% 降到 12%——品类黏性高、单一工具忠诚度低 ([JetBrains 2026-04](https://blog.jetbrains.com/research/2026/04/which-ai-coding-tools-do-developers-actually-use-at-work/); [JetBrains 2026-08](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/))。厂商收入同样显示出按用量计费的消费型增长：Claude Code 年化收入 2025 年 11 月达到 10 亿美元、2026 年 2 月超过 25 亿美元 ([Anthropic/Bun](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone); [Anthropic](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation))；Cursor 年化收入从 2026 年 2 月的 20 亿美元增至 6 月初的 **40 亿美元以上**（约四分之三来自企业；此为 Dealroom/福布斯口径，路透社在收购时报道的年化收入约 26 亿美元，各媒体口径不一），随后被 SpaceX 以 600 亿美元股票收购（6 月 16 日宣布、8 月 14 日生效）([Dealroom](https://dealroom.co/news/134107-cursor-tops-4b-annualized-revenue/); [CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html); [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-14/spacex-completes-its-60-billion-cursor-acquisition))；GitHub Copilot 付费订阅从 2023 年 10 月的 100 万增至 2026 年 1 月的 **470 万**（同比 +75%），含免费层的"用户"到 2026 年 7 月为 5,000 万，两个口径不能互相换算 ([Microsoft FY24 Q1](https://www.microsoft.com/en-us/investor/events/fy-2024/earnings-fy-2024-q1); [Microsoft FY26 Q2](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2); [Microsoft FY26 Q4](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4))；OpenAI Codex 的周活用户 2026 年 6 月超过 500 万，8 月 21 日宣布的"2,000 万活跃用户"未说明统计窗口，与周活口径不可比 ([Constellation Research](https://www.constellationr.com/insights/news/openai-touts-broadening-codex-usage-5-million-weekly-active-users); [OpenAI 社区](https://community.openai.com/t/20-million-codex-users-a-free-banked-reset-for-everyone/1391683))。微软称"三分之一的 GitHub PR 涉及代理"，但 GitHub 自己的口径是"超过五分之一的代码评审有代理参与"，所以这句话包含代理评审，不能读成"三分之一的 PR 由代理编写" ([GitHub](https://github.com/features/copilot))。Anthropic 的使用数据给出同一方向的结构证据：2025 年 4 月 Claude Code 会话中 79% 属于"自动化"模式，而 Claude.ai 聊天中只有 49%；Claude.ai 上"直接委托"的对话占比从 2024 年底的 27% 升到 2025 年 8 月的 39%，自动化首次超过增强 ([Anthropic 2025-04](https://www.anthropic.com/research/impact-software-development); [Anthropic 2025-09](https://www.anthropic.com/research/anthropic-economic-index-september-2025-report))。

### AI 写了多少代码：至少七种互不可比的口径

"AI 贡献的工作量"是用户最关心、也最容易被口径误导的指标。下表按分母列出目前能引用的数字，只有前两行是独立测量。

| 口径（分子/分母） | 数值 | 性质 | 来源 |
|---|---|---|---|
| 分类器识别的 AI 编写函数 / 美国开发者公开 Python 函数 | 约 **29%**（2024 年末）；AI 使用使季度产出 +3.6%，收益主要归资深开发者 | 独立测量，基于 16 万名开发者的 3,000 万次以上提交，发表于 *Science* | [Science](https://www.science.org/doi/10.1126/science.adz9311); [CSH](https://csh.ac.at/news/ai-is-already-writing-almost-one-third-of-new-software-code/) |
| 带 Claude Code 署名的提交 / 全部公开 GitHub 提交 | 约 **4%**（2026 年 2 月，约 13.5 万次/天） | 第三方测量，署名可删除，是下限；"年底 20%"只是预测 | [SemiAnalysis](https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point) |
| "AI 生成并经工程师接受"的新代码 / Google 新代码 | >25%（2024-10）→ >30%（2025-04）→ 约 50%（2025 秋）→ **75%**（2026-04） | CEO 表态，定义从未公开 | [Fortune](https://www.fortune.com/2024/10/30/googles-code-ai-sundar-pichai); [Google](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q1-2025/); [Google Cloud Next](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/cloud-next-2026-sundar-pichai/) |
| "由 Claude 编写"的代码 / Anthropic 代码 | 约 **80%**（2026-09）；季度交付代码为 2021–25 年的 8 倍 | 公司自报，计量单位未说明 | [Claude 博客](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic) |
| "AI 辅助生成"的新代码 / 腾讯新代码 | 50%（2025）；2026 年 6 月称"今年大部分代码由 AI 生成"，94% 的代码评审有 AI 参与 | 公司表态 | [IT之家](https://www.ithome.com/0/960/323.htm); [新浪财经](https://finance.sina.com.cn/jjxw/2026-06-05/doc-iniaiqkv1838867.shtml) |
| 文心快码生成 / 百度每日新增代码 | >40%（2025-04）→ >43%（2025-09） | 公司表态 | [新浪科技](https://finance.sina.com.cn/tech/roll/2025-04-27/doc-ineurmit7374002.shtml); [InfoQ](https://www.infoq.cn/news/UjVrrcyCLgOLVSmddO0C) |
| 代码生成采纳率（被接受的建议 / 全部建议） | 42.61%（2025 年中国企业平均） | 行业调查；**不是**"AI 写的代码占比" | [InfoQ/信通院](https://www.infoq.cn/article/e40mGRhF9o583Yi3akyM) |
| 自报"80% 以上代码由代理生成"的开发者比例 | 约 22%（全球，2026 年中）；东亚 32%–35%，欧洲约 16%；过半开发者手写代码不足 20% | 自报分布，是代码份额不是工时份额 | [JetBrains 2026-08](https://blog.jetbrains.com/research/2026/08/how-much-code-do-developers-really-let-agents-write/) |

2024 年，公司口径与独立测量大体吻合（Google 的"四分之一以上"对应分类器的约 29%）；2026 年的 75%–80% 只适用于重度内部使用的前沿公司，外部数据核验不了，而公开 GitHub 上单一代理的可识别份额只有 4% 的下限。更重要的是**代码份额不等于工作份额**：Google 在 2025 年 6 月说 AI 贡献了约 30% 的代码生成，但整体工程速度只提高约 10% ([The Hans India](https://www.thehansindia.com/technology/tech-news/sundar-pichai-says-ai-boosts-google-engineers-productivity-by-10-foresees-rise-of-autonomous-ai-agents-978596))，这是本报告反复出现的 Amdahl 缺口最干净的单一公司例证。中国的曲线形状相似但口径更难比：CSDN 2024 年调查中 69% 的中国开发者使用 AI 工具 ([CSDN 2024 摘要](https://www.cnblogs.com/yyds114/p/18359126))，信通院 2026 年报告称约三成企业的智能开发工具渗透率超过 90% ([InfoQ/信通院](https://www.infoq.cn/article/e40mGRhF9o583Yi3akyM))，头部公司的"AI 辅助/生成"份额与美国前沿公司处在同一数量级，但不可直接比较。

能力侧的斜率比部署更陡：METR 测得前沿模型以 50% 成功率完成的软件任务时长，从 2025 年初 Claude 3.7 Sonnet 的约 1 小时，升到 Claude Opus 4.6 的约 12 小时，2024–25 年模型的倍增周期约 4 个月，但 METR 明言超过约 16 小时的测量已不可靠 ([METR 2025](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/); [METR TH1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/))。能力远超实际部署中的自主运行时长，说明约束 AI 工作份额的是部署、验证与信任，而不是原始能力。综合来看，编程的趋势可以概括为三条嵌套曲线：**广度**已在 2025 年见顶（约 85%–90%）；**强度**处在中段（约一半人每天用，中位每天约 2 小时）；**委托与收入**仍处在指数段，已披露的序列看不到减速，但披露本身是有选择的。

## 二、工作结构：产出里量产暴涨，人的时间转向决策与验收

回答"创意类、执行量产类、决策迭代类工作的比例如何变化"，先要给三类工作可操作的定义（第五节详述），并且分开记两本账。**创意类（C）** 的产出是"应该存在什么"的新规格（概念、架构、机制）；**执行量产类（E）** 把既有规格变成可校验的制品（实现、测试、迁移、文档）；**决策类（D）** 的产出是判断、选择或参数（评审、验收、取舍、优先级）。**人时账本**记录人把时间花在哪里，**产出账本**记录产出物中有多少是机器量产的。编程的证据显示，两本账在代理时代走向相反。基线来自微软 5,928 名开发者的时间日志（2019）：读写代码与测试 15%、修 bug 14%、运行测试 8%、需求 4%、代码评审 5%、文档 2%，会议 15%、邮件 10% ([Meyer et al.](https://www.microsoft.com/en-us/research/wp-content/uploads/2019/04/devtime-preprint-TSE19.pdf))。只在开发类活动内归一化，得到 E 约 55%–60%、D 约 30%–35%、C 约 8%–12%；若把一半会议、协助和临时沟通计入 C/D，则是 E 约 40%–45%、D 约 35%–40%、C 约 15%–25%。这是单一公司、自报、2019 年的数据，只能作锚点，而且原文没有"创意"类别，C 是推算出来的。

**第一阶段（补全与聊天，2022–24 年）的方向与直觉相反。** Hoffmann 等人利用 GitHub Copilot 对头部开源维护者免费开放的资格门槛做断点回归，发现获得 Copilot 后，维护者 GitHub 活动中的编码份额上升约 5.4 个百分点（相对 +12.4%），项目管理份额下降约 10 个百分点（相对 −24.9%），工作变得更独立，低技能开发者变化最大 ([Hoffmann et al.](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5007084))。这衡量的是活动份额而不是工时，且只有一项研究，所以"补全时代人的执行份额短暂上升"只能算有证据支持的假说。这一时期及稍后的随机对照试验显示任务级产出确实上升：三项覆盖 4,867 名开发者的现场实验中，使用 AI 助手的开发者完成任务数 +26%，经验较少者增益更大 ([Management Science](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.00535))；但 METR 的试验中，资深开源开发者在自己熟悉的大型代码库上用 2025 年初的工具反而慢了 19%，却自以为快了 20% ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/))；METR 2026 年 2 月的后续数据中回访开发者快了约 18%、新招募者慢了约 4%，但 METR 自己认为数据不可靠，因为许多开发者已不愿在没有 AI 的条件下工作 ([METR 2026](https://metr.org/blog/2026-02-24-uplift-update/))。

**第二阶段（代理，2025–26 年）才真正把执行交给机器。** Anthropic 对约 40 万个 Claude Code 会话（2025 年 10 月至 2026 年 4 月）的分析显示，人平均做出约 **70% 的规划决策、只做约 20% 的执行决策**；"修复坏代码"的会话占比从 33% 降到 19%，"操作软件"从 14% 升到 21% ([Anthropic 2026-06](https://www.anthropic.com/research/claude-code-expertise))。Anthropic 内部研究（2025 年 12 月发布）中，工程师在 **59%** 的工作中使用 Claude（一年前为 28%），自报生产率 +50%，每人每天合并的 PR 增加 67%，但过半的人只能把 0–20% 的工作"完全委托"；Claude Code 任务中新功能实现从 14% 升到 37%，设计与规划从 1% 升到 10%；研究者的概括是各类任务"花的时间净减少，而产出量净增加得更多"，且 27% 的 AI 辅助工作是"否则不会做"的新任务 ([Anthropic 2025-12](https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic))。前沿样本的极端值来自 Anthropic 2026 年 9 月：约 80% 的代码由 Claude 编写，工程师每季度交付的代码是 2021–2025 年的 8 倍，测试量涨了 10 倍，CI 任务 6 个月涨了 25 倍，而工程人数只是名义增长——原话是"写代码不再是约束……PR 评审加速之后，CI 开始感到压力" ([Claude 博客](https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic))。这些都是厂商在自家用户身上的数据，代表前沿而不是中位数。

**产出账本毫无悬念地向量产倾斜。** GitHub 创新图谱的推送量增速从 2024 年的 +8.6% 跳到 2025 年的 +34.3%，2026 年一季度同比 **+80%**（按经济体加总；平台已剔除超出人类活动阈值的账户，因此代理密集的活动被低估）([GitHub Innovation Graph](https://github.com/github/innovationgraph))；Octoverse 2025 年度提交近 10 亿次（+25.1%），月均合并 PR 4,320 万（+23%）([GitHub Octoverse](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/))；应用商店新应用 2026 年一季度同比 +60%、4 月 +104%，归因于 AI 仍是"工作假说" ([TechCrunch](https://techcrunch.com/2026/04/18/the-app-store-is-booming-again-and-ai-may-be-why/))。加速出现在代理工具普及之后，而不是补全时代——2023、2024 年推送增速反而在放缓（时间上吻合，不是因果识别）。

**人时账本里上升的是验证。** Faros 对 1 万余名开发者、1,255 个团队的遥测显示，高 AI 采用团队多完成 21% 的任务、多合并 98% 的 PR，但 PR 评审时间 **+91%**、人均 bug +9%、PR 平均体量最多 +154%，公司级交付指标没有改善 ([Faros 2025](https://www.faros.ai/blog/ai-software-engineering))；其 2026 年报告覆盖 2.2 万名开发者、4,000 多个团队，比较各组织 AI 采用最低与最高的时期，中位 PR 评审时长 **+441.5%**，每个 PR 对应的线上事故 +242.7%，未经评审就合并的 PR +31.3% ([Faros 2026](https://www.faros.ai/blog/ai-acceleration-whiplash-takeaways))。DORA 2024 年的模型显示 AI 采用每提高 25%，交付吞吐 −1.5%、交付稳定性 −7.2%；2025 年吞吐关联转正，但不稳定性仍在 ([DORA 2024](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report); [DORA 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report))；2026 年 DORA 直接提出价值兑现的 J 曲线与"验证税" ([DORA ROI](https://dora.dev/ai/roi/report/))。质量侧，GitClear 分析 2.11 亿行变更，2024 年 5 行以上的重复代码块增加 8 倍，重构（移动行）占比从 2020 年的 24.1% 降到 9.5% ([GitClear](https://www.gitclear.com/ai_assistant_code_quality_2025_research))；CodeRabbit 发现 AI 参与的 PR 平均问题数约为人工 PR 的 1.7 倍 ([CodeRabbit](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report))。这些质量与瓶颈数据多来自出售分析或评审工具的厂商，但非厂商来源（DORA、Anthropic 自己的 CI 数据）指向同一方向。

**劳动力市场呈现资历偏向。** 斯坦福"煤矿里的金丝雀"研究（ADP 工资数据截至 2026 年 6 月）发现，AI 暴露职业中 22–25 岁员工的就业比反事实低 **19%**，22–25 岁软件开发者自 2022 年底下降约 20%，机制是少招而非多裁，资深员工没有类似缺口 ([Stanford DEL](https://digitaleconomy.stanford.edu/app/uploads/2026/08/Canaries_August2026.pdf))；Indeed 的软件开发岗位发布量仍比 2020 年 2 月低约 27.5%，但 2025 年 5 月至 2026 年 5 月的反弹中 **71%** 来自资深岗位、37% 来自职位名含"AI"的岗位 ([Indeed Hiring Lab](https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/))；采用生成式 AI 的企业初级岗位就业相对下降、资深岗位基本不变 ([Hosseini & Lichtinger](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555))。

下表是研究者的三角推算，不是测量。2024 年之后没有任何工时调查按 C/E/D 记录人的时间，这是整个问题最大的数据缺口。

| 人的工程时间（规则：亲手写 = E；指挥与评审代理 = D） | 前 AI 基线（2019 微软日志，仅开发活动） | 2023–24 补全/聊天期 | 2026 年中·中位开发者 | 2026 年中·AI 密集团队（情景示意） |
|---|---|---|---|---|
| E 执行/量产 | 55%–60%（宽口径 40%–45%） | 持平或略升（仅开源活动份额证据） | 35%–50% | 10%–25% |
| D 决策/验收 | 30%–35%（宽口径 35%–40%） | 约持平 | 35%–50% | 50%–65% |
| C 创意/定意图 | 8%–12%（另有藏在"编码"里的设计） | 持平或略升（探索增多） | 10%–20% | 15%–25% |
| 置信度 | 中（单一公司、自报） | 低（仅方向） | 很低（无工时测量，±15 个百分点） | 水平低，方向高 |

对用户第二个问题的直接回答是：**因为 AI 产能提升，"量产类"在产出中的占比确实大幅上升**——前沿公司机器生成的代码从少数变为多数，总产量增速成倍提高；到 2026 年年中，过半开发者自报"手写代码不足 20%"（这是代码份额，不是工时份额）。**但在人的工时里，执行类占比在代理时代是下降的，决策/验收与创意定向的占比上升。** 背后有五个有证据支撑的驱动：执行成本塌缩（代理）；验证能力没有同步扩张（评审时长 +91% 到 +441.5%）；人保留规划与验收决策（70/20）；新增产能被用于新任务而不只是加速旧任务（27% 的新任务；Anthropic 对 8 万余名用户的调查中，报告增益的人里"扩大范围"占 48%，多于"更快完成"的 40% ([Anthropic 81k](https://www.anthropic.com/research/81k-economics))）；企业用 AI 替代初级执行产能，把招聘转向资深与 AI 岗位。还需要两处修正。其一，D 本身也在被自动化——修 bug 会话的占比从 33% 降到 19%（这是会话构成的变化，不是对人均调试时间的测量），提示机械的"运行—报错—修改"迭代正在被代理吸收，留给人的是验收、取舍和优先级，所以第三类更应该叫"决策/验收"而不是"决策/迭代"。其二，"E 降 D 升"有一部分只是改名：给代理下指令、看它运行再接受，本质上是换一种方式做执行，必须单列"E-委托"标签，否则分界线一挪就能在 E 与 D 之间移动 10–20 个百分点。

## 三、价值账本："产量≠价值"只在在位者和宏观层面成立

用户的判断——"即便在编程，AI 也还没有直接产生行业级增量价值"——先要定义"行业"。如果指**既有软件生产者的利润与宏观全要素生产率**，证据支持这一判断且置信度高。截至 2026 年一季度的四个季度，利用率调整后的 TFP 只增长约 0.07%，财报电话会里约 95% 的 AI 生产率表述谈的是未来预期 ([St. Louis Fed](https://www.stlouisfed.org/on-the-economy/2026/jul/ai-productivity-what-firms-say-earnings-calls))；旧金山联储认为数据还不能证明进入了高生产率时期，其模型给出的高增长状态概率按劳动生产率约 57%、按 TFP 仅约 21% ([SF Fed](https://www.frbsf.org/research-and-insights/publications/economic-letter/2026/05/have-we-entered-era-of-high-productivity-growth/))；高盛称在全经济层面看不到 AI 与生产率的"有意义关系"，但在已落地的企业中，软件开发与客服两个领域的中位增益约 30% ([Fortune](https://fortune.com/2026/03/03/goldman-earnings-ai-anxiety-no-meaningful-impact-productivity-economy-30-percent-in-2-areas/))。企业层面，覆盖美英德澳约 6,000 名高管的 NBER 调查中 69% 的企业在用 AI，但超过八成（约九成）报告过去三年 AI 对就业和生产率没有影响，预期未来三年生产率只提高 1.4% ([NBER w34836](https://www.nber.org/papers/w34836))；普华永道调查的 4,454 名 CEO 中 56% 既没看到增收也没看到降本 ([PwC](https://www.pwc.com/gx/en/news-room/press-releases/2026/pwc-2026-global-ceo-survey.html))；丹麦行政数据给出精确的零效应，排除了 ChatGPT 发布两年后超过 2% 的收入与工时效应 ([Humlum & Vestergaard](https://bfi.uchicago.edu/working-papers/large-language-models-small-labor-market-effects/))。编程专项的证据是：三分之二的软件公司已铺开 AI 开发工具，团队层面 10%–15% 的增益"很少转化为商业价值"，因为编码只占从想法到上线时间的 25%–35%，只有做端到端流程改造的公司报告 25%–30% 的增益 ([Bain](https://www.bain.com/insights/from-pilots-to-payoff-generative-ai-in-software-development-technology-report-2025/))。自下而上的估算同样在聚合时大幅缩水：Anthropic 由对话估算的"每年 +1.8 个百分点劳动生产率"，在按任务成功率和任务互补性调整后降到约 0.6–0.8 个百分点 ([Anthropic](https://www.anthropic.com/research/economic-index-primitives))。

但把它当作全称判断就错了。**第一，AI 工具层创造了真实的新收入池**：Claude Code 年化收入超过 25 亿美元、Cursor 超过 40 亿美元并以 600 亿美元被收购、Anthropic 整体年化收入在 2026 年 4 月超过 300 亿美元 ([VentureBeat](https://venturebeat.com/technology/anthropic-says-it-hit-a-30-billion-revenue-run-rate-after-crazy-80x-growth))——尽管这些都是未经审计的年化值，应用层毛利偏薄。**第二，行业统计出现了强信号**：美国劳工统计局测得"软件出版商"劳动生产率 2025 年增长 **12.9%**，为所选服务业之首（2024 年修正为 4.0%，此前曾报 9.4%）([BLS](https://www.bls.gov/news.release/prin2.t03.htm))；但产出按平减后的收入计量、行业内含 AI 产品销售者、裁员后工时下降，这个数字不能归因于 AI 编程，单年读数也不能当作证伪依据，而且 NAICS 5132 包含电子游戏出版商，它本身部分就是游戏业数据。**第三，新产品与新公司的形成加快**：Stripe Atlas 新注册公司 +41%，30 天内收到首笔付款的比例从 2020 年的 8% 升到 20% ([Stripe](https://stripe.com/annual-updates/2025))；生成式 AI 给美国消费者带来的剩余估计从 2025 年的 1,160 亿美元升到 2026 年的 1,720 亿美元（覆盖全部生成式 AI，基于选择实验）([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6569938))。

价值去了哪里？按证据强度排序的机制是：**端到端瓶颈与 Amdahl 限制**（强：编码只占周期的 25%–35%，评审时长同时上升）＞**竞争性传导给客户**（在 IT 服务中强：印度 IT 业把生产率节省按每年约 2%–5% 的"AI 通缩"让利给客户，HCLTech 称同样收入需要多付出 25%–30% 的工作量，TCS 出现首次全年美元收入下降 ([The Register](https://www.theregister.com/software/2026/04/28/ai-deflation-comes-to-indias-tech-services-giants/5225686); [TCS](https://www.tcs.com/who-we-are/newsroom/press-release/tcs-financial-results-q4-fy-2026))）＞**组织 J 曲线**（中：只有约 5%–6% 的企业属于流程重构后的"高绩效者"，且是相关性证据 ([McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai); [BCG](https://www.bcg.com/press/30september2025-ai-leaders-outpace-laggards-revenue-growth-cost-savings))）＞**质量与返工债**（中，多为厂商数据）＞**计量遗漏**（理论上中等，难以量化）。宏观上，美国非农部门劳动收入份额在 2026 年二季度降至 52.8%，为 1947 年以来最低 ([BLS](https://www.bls.gov/news.release/prod2.nr0.htm))——不能证明 AI 因果，但与"收益流向资本和厂商而非劳动者"一致。供给侧的稀释也清楚可见：2025 年全球应用内消费只增长 10.6%，其中非游戏应用的增长主要由生成式 AI 服务推动 ([Sensor Tower](https://sensortower.com/press/press-release-boosted-by-gen-ai-services-consumers-spent-more-money-in-apps-than-games-for-first-time))，而 2026 年一季度新应用发行量同比增长 60%、4 月增长 104%（两者期间不同，只能说新增供给远快于任何合理的消费增速）。

结论可以写成一个**三分诊断**："尚未兑现"（J 曲线）、"不在生产者收入里"（外溢给 AI 厂商与客户）、"根本没有"（被瓶颈与质量成本抵消）。目前的证据更支持后两者，而不是单纯的"尚未"。平衡的表述是：**AI 编程在任务层面产生了真实的增益，并催生了一个高速增长的工具产业；但截至 2026 年 9 月，几乎看不到它变成既有软件生产者可测量的增量利润或宏观 TFP——价值主要被 AI 厂商以收入形式捕获、通过降价与消费者剩余传给客户、被评审与返工吸收，并摊薄在大量长尾新应用上。"产量≠价值"在在位产业与宏观层面成立（高置信），在 AI 工具层不成立（中高置信），在社会价值层面无法判定（很大但未计价）。** 这个区分对游戏外推至关重要，因为三种诊断对游戏给出的预测完全不同。

## 四、游戏基线：个人使用停在 36%，AI 作品占三成发行却只拿一到两成多的销量

游戏业的"采用率"至少有四层——工作室层面的任何使用、工作者个人使用、玩家可见的已发行内容、以及中国企业调查——不能合成一条曲线。**最干净的工作者层面序列来自 GDC 年度调查：个人在工作中使用生成式 AI 的比例 2024 年 31%、2025 年 36%、2026 年 36%，自 2025 年起基本持平**；所在公司已部署生成式 AI 的比例 2025 年约 52%，2026 年大致持平 ([GDC 2025](https://gdconf.com/article/gdc-2025-state-of-the-game-industry-devs-weigh-in-on-layoffs-ai-and-more/); [GDC 2026](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/); [Game Developer 2024](https://www.gamedeveloper.com/business/gdc-2024-state-of-the-game-industry-devs-discuss-layoffs-generative-ai-and-more))。2026 年样本中游戏工作室员工的使用率只有 30%，发行、支持与市场公关岗位则为 58%——工艺生产岗位的渗透明显低于头条数字 ([Game Developer](https://www.gamedeveloper.com/business/one-third-of-game-workers-use-generative-ai-but-half-think-it-s-bad-for-the-industry))。使用者的用途集中在研究与头脑风暴（81%）、代码辅助（47%，约占全部受访者的 17%）和原型（35%），而不是最终资产。与此同时，认为生成式 AI 正在损害行业的比例从 18%（2024）升到 30%（2025）再到 **52%**（2026），GDC 发布的分职能数据中视觉与技术美术（64%）、设计与叙事（63%）、程序（59%）最负面。口径不同，但量级上游戏工作者 2026 年的个人使用率（36%）仍低于编程侧 2023 年的水平（Stack Overflow 职业开发者"正在使用"44%），而编程侧到 2025–26 年各项调查已达约九成（DORA、JetBrains，口径各异，不能连成一条线）——这是两个领域最清楚的对照。厂商调查测的是更宽的东西：Unity 2026 年约 300 名用户中 95%"采用 AI"（即只有 5% 表示不会用），用途是编程辅助 62%、叙事写作 44%、NPC 行为 40%、自动化试玩 35%；其"开发时间下降 77%"指的是 Unity 遥测中项目开发时长中位数从 2022 年 1 月的 91 小时降到 2025 年 12 月的 21 小时，**不是** AI 带来的生产率 ([Unity](https://unity.com/blog/2026-unity-game-development-report-trends); [Wccftech](https://wccftech.com/unity-2026-game-development-report-points-to-smaller-teams-making-games-in-less-time-with-ai/))。Google Cloud 委托 Harris Poll 调查五国 615 名开发者，90% 把 AI 纳入工作流、87% 使用 AI 代理，是厂商委托样本 ([Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research))。

**中国的数字高得多，但几乎全部是自报或行业撰写。** 伽马数据 2025 年报告中 99% 以上受访者所在公司或部门引入了 AI，约八成感知效率提升超过 20%，约六成头部企业已建成 AI 生产管线 ([GameRes](https://www.gameres.com/906453.html))；2026 年 4 月在北京发布的《双向赋能：AI 与游戏的协同进化》白皮书（大湾区人工智能应用研究院联合完美世界、三七互娱、腾讯开悟）给出生产侧 AI 应用率 86.36%、美术环节渗透率 84.2%，部分项目 AI 生成代码可达 90%、人力成本节省约 30%，属于参与企业撰写而非代表性抽样 ([澎湃新闻](https://www.thepaper.cn/newsDetail_forward_33077088))；三七互娱称单季度产出 50 万张以上 2D 美术资产、提效 80% 以上，3D 资产中 AI 占比 30% 以上，AI 深度参与 70% 以上的广告视频素材——这里的"80%"是提效幅度，不等于"80% 的 2D 美术由 AI 生成" ([澎湃新闻](https://m.thepaper.cn/newsDetail_forward_32204806); [每日经济新闻](https://www.nbd.com.cn/articles/2025-08-01/3997601.html))。游戏工委 2025 年 12 月的 AI 应用报告只调研了 22 家企业，其中 90.9% 年收入过亿元 ([GameLook](http://www.gamelook.com.cn/2025/12/584581/))，中小团队的采用基本没有被测量。中国的领先领域是美术与买量素材而不是代码，这与移动游戏占国内收入约 73% 的结构一致 ([IT之家](https://www.ithome.com/0/906/428.htm))。

**玩家可见的一层增长最快，但价值没有同步跟上。** Sulka Haro 对 2023 年 7 月至 2026 年 7 月 53,597 款 Steam 新作的普查显示，带 AI 标注的作品占发行量的比例从 2024 年的 **10.9%**、2025 年的 **19.9%** 升到 2026 年（截至 7 月）的 **30.8%**，月度发行量增长的 60%–90% 来自 AI 标注作品；非 AI 作品从每月约 1,030 款增至约 1,320 款，AI 标注作品约 530 款/月 ([Haro](https://fragwyz.substack.com/p/three-years-of-ai-on-steam); [GamesRadar](https://www.gamesradar.com/games/steam-study-of-over-53-000-games-finds-60-90-percent-of-the-growth-in-monthly-releases-on-valves-store-is-from-games-using-ai-and-almost-none-of-them-make-money/))。但 AI 标注作品的估算销量份额（以评论数推算）只从 2024 年的约 3%–6% 升到 2025 年底至 2026 年的约 **10%–27%**，低于其约三分之一的发行份额，达到"小有成功"档位的比例只有非 AI 作品的约 55%。Haro 推算 2027–28 年 AI 标注作品将超过发行量的一半，这是外推而不是测量；而且 Valve 在 2026 年 1 月 16 日修改规则，豁免编程助手等效率工具，只要求披露玩家可见的"预生成"与"实时生成"内容，2026 年与 2024–25 年的份额并不严格可比，编程类 AI 在 Steam 数据里完全不可见 ([Slashdot](https://games.slashdot.org/story/26/01/19/1735231/); [Remio](https://www.remio.ai/post/steam-ai-disclosure-policy-updated-efficiency-tools-now-exempt))。存量口径下，约 10,258 款 Steam 作品带 AI 披露（约占目录 8%，多数只是商店图、背景、图标或占位语音等外围用途），累计估算总收入约 6.6 亿美元 ([Totally Human](https://www.totallyhuman.io/blog/games-with-ai-disclosures-have-grossed-an-estimated-660m-on-steam))，而 GameDiscoverCo 估算 Steam 仅 2025 年一年就约 169 亿美元 ([GameDiscoverCo](https://newsletter.gamediscover.co/p/who-won-steams-best-of-2025-revenue))。

**可见的 AI 会被打折，但这主要是"接收折扣"，还不是已识别的收入惩罚。** Game Oracle 对 2025 年 1–10 月 9,879 款游戏（剔除垃圾作品与免费游戏）的匹配分析显示，披露 AI 的作品首月评论数少约 53%（首月平均约 4 条对 7 条，基数很小），在评论数≥100 的作品中好评率 84.6% 对 88.3%；它控制了开发者经验、发行商、品类与发售时间，但没控制预算和质量 ([PC Gamer](https://www.pcgamer.com/software/ai/data-analyst-finds-ai-stigma-on-steam-can-reduce-the-number-of-reviews-a-game-gets-by-around-53-percent-and-the-reviews-it-does-get-are-more-negative/))。Bazzaz 与 Cooper 分析 508,192 条英文评论（预印本），披露生成式 AI 的游戏推荐率比"程序化生成"标签的游戏低约 18 个百分点（68.4% 对 86.3%），玩家把生成式 AI 解读为"开发者投入低" ([arXiv](https://arxiv.org/abs/2608.11539))。需要注意，这三项研究（Haro、Game Oracle、Bazzaz 与 Cooper）都以评论为信号——评论数量、评论情绪，或由评论数推算的销量——是同一信号的三个视角，而不是三个独立的收入测量。Haro 的成功/失败画像更有操作意义：失败的 AI 标注作品中 72% 把 AI 用在视觉上，成功者则更多把 AI 用在玩家不盯着看的地方——配音（24% 对 8%）与本地化（18% 对 6%）([Cinevva](https://app.cinevva.com/news/2026-07-20-steam-ai-disclosure-study))。玩家态度的强度取决于样本：Circana 的美国面板中略超 25% 表示知道用了生成式 AI 会降低购买意愿 ([GameSpot](https://www.gamespot.com/articles/genai-in-games-most-players-just-dont-care-study-finds/1100-6538972/))，Quantic Foundry 的自选样本（n=1,799，偏年轻核心玩家）中 85% 持负面态度 ([Quantic Foundry](https://quanticfoundry.com/2025/12/18/gen-ai/))——一个强烈的少数派加一个无所谓的多数派，而前者恰恰是写评论、驱动算法可见性的人群。两个标志性案例：《ARC Raiders》用授权演员声音做 TTS，引发争议后重录了部分台词，CEO 承认"存在质量差距"，游戏仍卖出 1,400 万份以上 ([Engadget](https://www.engadget.com/gaming/arc-raiders-replaced-some-of-its-ai-generated-voice-lines-with-professional-actors-184915627.html); [GameSpot](https://www.gamespot.com/articles/arc-raiders-now-has-fewer-ai-voices-as-dev-re-recorded-lines-amid-controversy/1100-6538780/))；《光与影：33 号远征队》因发售版本残留 AI 生成的海报纹理，2025 年 12 月被独立游戏大奖收回最佳游戏与最佳首作 ([Engadget](https://www.engadget.com/gaming/the-indie-game-awards-snatches-back-two-trophies-from-clair-obscur-over-its-use-of-generative-ai-164730842.html))。

**市场背景是供给膨胀、分布极化、需求缓慢增长——但需求并非固定。** Steam 发行量 2025 年约 1.95–2.03 万款，2026 年上半年 11,979 款，全年约 2.4 万款的节奏 ([SteamDB](https://steamdb.info/stats/releases/); [Notebookcheck](https://www.notebookcheck.net/Steam-averages-almost-70-new-games-a-day-in-2026.1374113.0.html))；2025 年 1 月至 10 月 21 日上架的约 1.27 万款作品中位估算收入仅 249 美元，65.9% 不足 1,000 美元，只有 8% 超过 10 万美元（新近作品的收入期较短）([GamesRadar](https://www.gamesradar.com/games/over-5-000-games-released-on-steam-this-year-didnt-make-enough-money-to-recover-the-usd100-fee-to-put-a-game-on-valves-store-research-estimates/); [OpenCritic](https://opencritic.com/news/22399/only-8-of-steam-games-gross-over-100-thousand-40-make-less-than-steam-listing-fees))；在全部有评论的付费游戏中，终身收入中位数不到 4,000 美元，前 1% 拿走约 84.5% 的估算收入 ([GamesRadar](https://www.gamesradar.com/games/behold-the-whole-history-of-steams-economy-in-one-picture-the-top-1-percent-of-games-earn-84-5-percent-of-estimated-revenue-and-most-games-barely-make-anything/))。但"注意力池固定"并不成立：Newzoo 显示新作一直占 PC+主机游戏时长约 13%，非年货新作在 PC 时长中的占比从 4% 升到 10%、在 PC 收入中从 16% 升到 30%（2022–25），PC 支出中前 20 名以外的份额从 48% 升到 56%——"中腰部"在变宽 ([GameDev Reports/Newzoo](https://gamedevreports.substack.com/p/newzoo-pc-and-console-market-in-2026); [TechSpot](https://www.techspot.com/news/112092-2026-pc-console-gaming-report-shows-most-revenue.html))；Steam 2026 年上半年收入约 111 亿美元、同比 +14.5%，驱动因素是中国玩家涌入、新作提价与合作类爆款，当年新作占收入的比例从 2024 年上半年的 29% 降到 21% ([GameDev Reports/Alinea](https://gamedevreports.substack.com/p/alinea-analytics-steam-reached-highest))。全球市场 Newzoo 2026 版为 2,139 亿美元（+6.1%），但它 2025 年起重述了方法论，不同版本的数字不可比 ([PocketGamer.biz](https://www.pocketgamer.biz/no-single-model-for-growth-says-newzoo/))；中国 2025 年国内实际销售收入 3,507.89 亿元（+7.68%），小程序游戏 535.35 亿元（+34.39%）([新华网](http://www.news.cn/20251219/71b9f7db89c84eee968cddeeeb86baf1/c.html))。没有任何来源把这些增长归因于 AI。

**劳动与制度的基线决定了哪些门先开。** 英国游戏业普查中编程约占岗位的 20%，美术 16%，设计 11%，项目管理与 QA 各 8%（仅英国、可多选、是人数不是成本）([Statista/Ukie](https://www.statista.com/statistics/1096364/job-role-distribution-in-the-games-industry-uk/))。裁员统计分歧很大：GDC 2026 年受访者中 28% 在过去两年被裁（美国 33%），被裁者中 48% 尚未找到新工作 ([Variety](https://variety.com/2026/gaming/news/one-third-video-game-workers-laid-off-2025-1236644512/))，各追踪器对 2025–26 年总数的估计差距悬殊，只能引用区间，而 2023–24 年的裁员高峰早于生产级 AI 管线。AI 对劳动的影响最先体现在外包价格与初级岗位，而不是被归因的裁员：2023 年中国一位招聘者估计游戏插画岗位一年下降约 70%（原因同时包括监管与经济）([Rest of World](https://restofworld.org/2023/ai-china-video-game-layoffs-illustrators/))，外包角色原画单价从约 8,000 元降到约 2,000 元 ([GameLook](http://www.gamelook.com.cn/2023/04/514084/))；据报道伽马数据 2026 年人才报告称传统美术与初级策划执行岗需求同比下降约 35%、技术美术与 AI 应用岗上升约 42%（原始报告未能找到，仅作参考）([搜狐](https://www.sohu.com/a/1010056456_121984121))；翻译业 2025 年产值约 701.2 亿元、同比 −1.0%，66% 以上项目由机器翻译或"机翻+译后编辑"完成 ([中国翻译协会](https://www.tac-online.org.cn/2026-04/28/content_43415316.html))。制度门槛在西方更高：SAG-AFTRA 2025 年游戏协议以 95.04% 通过，要求数字复制品的书面同意与披露 ([SAG-AFTRA](https://www.sagaftra.org/contracts-industry-resources/interactive/2025-interactive-media-video-game-agreement))，工会还就《堡垒之夜》AI 达斯·维达语音提出不当劳动行为指控 ([Variety](https://variety.com/2025/gaming/news/sag-aftra-fortnite-ai-darth-vader-unfair-labor-practices-james-earl-jones-1236403553/))；美国版权局认为仅靠提示词不足以构成人类创作控制 ([USCO](https://www.copyright.gov/ai/))；中国《人工智能生成合成内容标识办法》自 2025 年 9 月 1 日起施行、覆盖虚拟场景，但没有发现针对游戏版号的 AI 专门规则 ([网信办](https://www.cac.gov.cn/2025-03/14/c_1743654685899683.htm))。

## 五、比较方法论：先对齐层级与分母，再按五道门判断迁移方向

把编程的经验搬到游戏，最危险的做法是拿编程的任务级增益（例如 RCT 中 +26% 的完成任务数）直接推断游戏行业的价值变化。本节给出一套精简的比较研究方法论，它把用户提出的两条视角——"游戏的价值主要来自创意与打磨，而不是编码"和"即便在编程，产量也不等于价值"——写成可证伪的假设而不是前提，并且规定每个结论能迁移到哪一层、朝哪个方向迁移。完整的十维评分表、六层单元、分阶段研究设计与陷阱清单放在附录 A。

### 同级证据才能互证：任务、职能、产品、市场四层

分析单元分四层：**任务**（含所在流水线阶段）→ **职能×资历** → **产品**（一款作品或一个赛季）→ **市场**（平台与区域）。匹配规则是：编程侧的任务级效应只能作为游戏侧任务级效应的证据；关于产品和市场的结论，必须有同级证据，或经过显式的聚合模型——任务到流程用 Amdahl 定律 S = 1/((1−p)+p/s) ([Amdahl](https://doi.org/10.1145/1465482.1465560))，流程到产品用 O 型环或替代弹性小于 1 的 CES 模型（质量在环节间相乘，任务互补时线性加总的暴露指数会高估替代）([Kremer](https://doi.org/10.2307/2118400); [Gans & Goldfarb](https://www.nber.org/papers/w34639))，产品到市场用注意力约束下的重尾需求模型（质量不可预测时，更多"抽签"本身可能提高福利）([Aguiar & Waldfogel](https://www.journals.uchicago.edu/doi/abs/10.1086/696229))。每个数字都要标明它属于哪一层；"层级错配"是这个问题上最常见的错误。

### 七级指标阶梯：不报价值，就不报产量

指标按七级阶梯组织：**采用**（有无使用，分任何/每周/每日）→ **渗透**（AI 介入的任务实例或工时份额）→ **AI 贡献**（以存活下来的已发布产出计，而不是"被接受的建议"或"生成的字符"）→ **产出量** → **质量**（可校验指标、盲评与多样性）→ **价值创造**（收入、时长、消费者剩余，按分布报告）→ **价值捕获**（工作室、劳动者、平台、引擎、AI 厂商、消费者各得多少）；另设一个诊断侧栏，记录评审时延、返工率与 C/E/D 的成本份额。"暴露度"只代表潜力，不当作证据。三条报告规则：不单独报告产量而不报告同一单元的价值；游戏侧一律报告分布（中位数、P90、命中率、头部份额），不用均值；任何"AI 贡献"都写明分子、分母和定义。关键比率是**供给的价值弹性** %ΔV/%ΔQ，而且要先扣除玩家基数与时长的增长——Steam 十年内发行量增长约 7 倍而总收入创新高，主要是需求增长的功劳，不是供给本身的功劳 ([SteamDB](https://steamdb.info/stats/releases/); [GameDiscoverCo](https://newsletter.gamediscover.co/p/who-won-steams-best-of-2025-revenue))。编程已经示范了阶梯各级之间的"漏损"：广度约 90%，代码份额自报 50%–80%，速度却只提高约 10%，宏观 TFP 几乎为零。

### 一条规则切分三类工作，外加"E-委托"标签与两本账

三类工作按任务实例而不是岗位打分：**没有规格、且产出本身就是规格 → C；有规格或参照、且产出是可校验的制品 → E；产出是判断、选择或参数 → D**。一个任务可以按比例分摊到多类，由两位编码者独立打分，一致性目标为 κ≥0.7。补充一个"E-委托"标签：人向代理下达执行指令、看它运行、再接受结果的时间单独记录——写一份设定新意图的功能简报算 C，让代理实现既有规格算 E-委托，评审并接受结果算 D。这样"指挥代理"就不会被悄悄地改名为决策，编程与游戏的账本才可比。第三类定名为"决策/验收"：机械迭代正在被代理吸收，留给人的是接受与否、取舍和优先级。人时账本与产出账本必须分开记，编程证据表明后者的变化远大于前者。游戏侧目前没有任何按 C/E/D 记录的工时数据，所以本报告对游戏只给方向和置信度，不给百分比。

### 五道门加一个需求开关：决定编程经验能否迁移、朝哪个方向迁移

对每个游戏任务，与最相近的编程任务在五道门上逐一比较。**第一道门是可验证性与反馈回路**：有没有便宜、客观、可重复的自动校验，一次尝试到得到反馈要多久，错误能否在触达玩家前被发现。这是最强的单一预测变量——"软件 2.0 容易自动化能被验证的东西"，而可验证的环境需要可重置、可高效多次尝试、可自动给出奖励 ([Karpathy](https://karpathy.bearblog.dev/verifiability/))；经济学上对应"易学任务"与"缺乏客观结果度量的难学任务"之分 ([Acemoglu](https://www.nber.org/papers/w32487))。编程恰好在这道门上得分极高（编译器、测试、CI）。**第二道门是耦合与一致性**：产出能否单独验收，是否必须与画风、世界观、角色声音、关卡节奏在成百上千个资产之间保持一致。**第三道门是数据与流水线契合**：制品是否文本化、有没有大规模可用语料，能否直接进入引擎、DCC 与 CAT 工具链。**第四道门是权利与接受度**，必须中西分列：版权可保护性、训练数据授权、表演者同意、平台披露规则、玩家可见性与污名。**第五道门是品味与隐性知识**：验收是否依赖无法编码的判断。门之外还有一个**需求开关**：更便宜、更多的产出究竟提高了付费意愿（需求有弹性、B2B 生产率），还是只增加了供给（注意力约束、重尾分布）。

使用规则有四条。按任务而不是按职能评分。迁移方向由门的比较决定，而不是一律把编程效果当作上限——买量素材由点击率和投资回报率自动校验、而且用完即弃，中国 2D 外包的替代比编程更快更深，这些任务上的效果可能高于编程。每项判断标注日期和当时的模型能力水平，每 6 个月重评一次，因为能力前沿既快又不均匀。把"验证工程"——自动试玩、画风一致性分类器、平衡模拟器、让"生成—验收"循环变快的评审界面——当作单独的驱动因素跟踪，因为它们正是把游戏任务推向"像编程一样可迁移"的杠杆。

### 五类迁移结论：高、有条件、仅产量、低，以及"新任务"

据此把游戏任务分入五类：**高**（原样迁移）；**有条件**（可校验的部分迁移，其余不迁移）；**仅产量**（速度迁移、价值不迁移），它有两个亚型——**品味型**（可见的创意资产，伴随污名与同质化）和**军备竞赛型**（买量素材，产量转化为竞争而不是价值）；**低**；以及**新任务（N）**——运行时与 AI 原生体验。N 类不是编程增益的迁移，而是 Acemoglu–Restrepo 意义上的"新任务"，应当按需求扩张与单位经济来评估，而不是按生产率 ([Acemoglu & Restrepo](https://doi.org/10.1257/jep.33.2.3))。第六节的迁移地图即按此分类，并对中国与西方分列。

### 把两条命题写成七条可证伪的假设

| 假设 | 内容 | 目前的证据 | 什么情况下被证伪 |
|---|---|---|---|
| A1 劳动结构 | 编程是游戏生产劳动与成本的少数 | 英国普查中编程约占岗位 20%（人数口径，非成本） | 收入加权的作品样本中，编程占生产人月或薪酬 ≥50% |
| A2 付费意愿来源 | 越过技术门槛后，创意与打磨属性对收入/评价的解释力高于技术与内容量属性 | 游戏销量对质量呈递增回报 ([Binken & Stremersch](https://journals.sagepub.com/doi/10.1509/jmkg.73.2.88))；有明确目标玩家的项目 83% 商业成功、没有的 50%（相关性）([Bain](https://www.bain.com/about/media-center/press-releases/2026/gamings-next-winners-will-be-built-on-player-focus-ai-powered-personalization-and-direct-relationships-bain-co-report-finds/))；可见 AI 的接收折扣 | 技术或内容量属性解释同等或更多方差；或 AI 美术在盲测中无法区分**且**没有披露折扣 |
| A3 打磨的乘法效应 | 作品价值在各质量维度间相乘（O 型环），短板拖累整体 | 只有案例（如《ARC Raiders》重录）；"打磨是最后 10%–20% 的工作量"只是从业者说法 | 加性模型拟合得一样好；打磨补丁对评价与销量无可测影响（需同时比较加性、乘法与"最短板"三种函数形式） |
| A4 Amdahl 上界 | 只限编程的 AI 增益对整款游戏工期与成本的影响有上界 | 算术：编程占工期 p=0.25 时，编程提速 1.26 倍（RCT 量级）→ 整体约 5%；提速 2 倍 → 12.5%；编程瞬间完成 → 至多 25%（固定范围） | 观测到的整款工期或成本降幅超过编程单独的上界——说明其他职能也在迁移，本身就是重要信息 |
| B1 量价背离 | 2023 年以来软件的产量指标远快于价值指标 | 推送 +80%、TFP 约 0.07%、中位企业无 P&L 变化 | 用 TFP 类指标或企业级双重差分（而非单年行业劳动生产率）、持续两年以上、剔除 AI 工具商自身收入与裁员后工时效应后，价值增速接近"任务增益×暴露份额×成功率"推出的水平 |
| B2 瓶颈机制 | 增益被评审、测试与验收吸收 | 评审时长 +91% 至 +441.5%；CI 任务 25 倍 | 吞吐上升而评审时延与不稳定性不升 |
| B3 尚未 vs 外溢 | 区分"J 曲线尚未兑现"与"价值流向厂商与客户" | 5%–6% 的流程重构企业报告增益；IT 服务 2%–5% 年通缩 | 重投入组织三年后仍无追赶（否定 J 曲线）；或软件企业人均收入与利润率随任务增益同步上升（否定外溢） |

两条命题都应以平衡的形式进入外推。**命题（a）的平衡表述**：编程确实只是游戏生产劳动的少数，编码增益单独对整款游戏的影响被 Amdahl 限定在几个百分点到至多四分之一；玩家付费的是相对的、由品味判断的东西——新颖的乐趣、手感与打磨、IP、社交与长线运营——而这些恰恰是最难验证的任务，所以编程经验在价值产生之处迁移得最弱。但"游戏不主要是编程"不等于"游戏基本免疫"：游戏的非编程劳动本身就是执行密集的（资产、变体、测试、本地化），AI 已经在其中大宗、不可见、可按指标校验的层面实质替代（本地化、买量素材、次要配音、外包 2D，中国最深）。更准确的说法是：**AI 的生产增益经由执行层进入游戏，这些执行层由一致性、权利与可见性把守，而不只是由可验证性把守；价值转化则取决于 AI 触及最少的决策层与创意层。** **命题（b）的平衡表述**见第三节：价值已经产生，但被厂商捕获、传导给客户、被验证吸收、摊薄在长尾上，所以尚未体现在在位生产者的利润与 TFP 里；它不能被当作"AI 在游戏里也不会产生价值"的直接证据，而应当用三分诊断逐层检验。

### 外部视角：编程之外，还要看五次创意技术冲击和游戏自己的四次自然实验

参考类有三组：编程 2022–26 年（领先市场）；五个历史案例——桌面出版、CAD、数码摄影与微图库、数字音乐（DAW 与数字分发）、CGI/VFX；以及游戏自身的四个自然实验——免费引擎加 Steam 开放、超休闲游戏、UGC 平台、微信小游戏。共同模式是：执行岗位与单价坍缩，产量爆炸，价值向平台与头部集中，顶部质量并不下降，创意方向不会消失，组织重构带来滞后；数字化让新品数量激增而质量未降 ([Waldfogel 2012](https://doi.org/10.1086/665824); [Waldfogel 2017](https://www.aeaweb.org/articles?id=10.1257/jep.31.3.195))，质量不可预测时更多新品反而提高福利 ([Aguiar & Waldfogel](https://www.journals.uchicago.edu/doi/abs/10.1086/696229))。游戏自然实验补上一个关键修正：**廉价生产是必要条件而不是充分条件**。它与新渠道、新商业模式或新品类一起到来时（移动 F2P、模组衍生的新品类、UGC 平台、合作类独立游戏），扩大了市场；单独到来时，只稀释中位数，并把租金转移给平台和发现渠道。生成式 AI 迄今属于后者。

### 阅读规则：七个最常见的误读

读本报告及同类数据时应遵守七条规则。一，产量不等于价值，任何产量数字都要配同一单元的价值数字。二，自报有偏：资深开发者在 RCT 中用 AI 慢了 19% 却自认为快了 20%，游戏业的污名又会压低 AI 使用的自报与披露。三，定义不一致："使用"分任何与每日，"AI 写的代码"分被接受的建议与存活的代码行，"Steam 披露"分发行份额、目录份额与销量份额。四，选择效应：用户挑 AI 擅长的任务交给 AI，低预算团队更常用 AI，AI 标注作品的表现差距部分来自选择。五，重尾：用中位数、分位数和命中率，不用均值。六，层级错配：不把任务级 RCT 当作市场结论。七，构成变化：非程序员写代码、单人借助 AI 发游戏，会改变"每开发者""每工作室"的含义。

## 六、外推：AI 从执行层进入游戏，价值被卡在决策层

把第五节的方法用到第一至四节的基线上，第一步是逐项比较游戏任务与最相近的编程任务在五道门上的差异。下表是截至 2026 年 9 月的迁移地图，分类是研究者依据所列证据作出的判断，证据类型各不相同（调查、公司说法、内部测试、第三方测量），应当每 6 个月重评一次。

| 游戏任务 | 迁移类别（西方 / 中国） | 起决定作用的门 | 关键证据 | 置信度 |
|---|---|---|---|---|
| 工具、构建与 CI、测试脚手架、后端服务、遥测、UI 实现代码 | 高 | 可校验、反馈快、玩家看不见 | Unity 2026 编程辅助 62% ([Unity](https://unity.com/blog/2026-unity-game-development-report-trends))；编程 RCT 完成任务 +26% | 采用中高；游戏专属增益无测量 |
| 成熟专有代码库中的玩法、引擎、渲染、性能代码 | 有条件 | 可校验但反馈慢（构建、性能分析、主机认证） | 资深开发者在成熟大型库上慢 19% ([METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)) | 中 |
| 文本本地化、语言质检、商店与补丁文案 | 高（两地） | 可对照原文校验，已有 CAT/TMS 流水线，可见度低 | 中国 66% 以上翻译项目为机翻或机翻加译后编辑；成功的 AI 标注作品更多用于本地化（18% 对 6%） | 高 |
| 买量与营销素材、商店图、预告片变体 | 迁移高，价值"仅产量·军备竞赛型"（中国更深） | 点击率与投资回报率自动校验、用完即弃，收益被竞争抵消 | 三七 AI 深度参与 70% 以上广告视频；头部广告主每款产品每季度 2,400–2,600 条素材（+25%–30%），广告曝光 +20% ([AppsFlyer](https://www.appsflyer.com/company/newsroom/pr/gaming-marketing/)) | 迁移高；市场层零和亦高 |
| 概念探索、预可视化、内部参考图、原型 | 有条件偏高（内部使用） | 无玩家惩罚，但仍靠品味验收；有同质化风险 | GDC 使用者中原型 35%；AI 辅助让个体作品更好、整体更相似 ([Doshi & Hauser](https://www.science.org/doi/10.1126/sciadv.adn5290)) | 中 |
| 上线的 2D 插画、主视觉、UI 图标 | 仅产量·品味型；中国生产渗透高，西方低到中、AAA 有争议 | 可见、污名、整套资产一致性 | 外包原画单价约 8,000→2,000 元；失败的 AI 作品 72% 用于视觉；首月评论少约 53% | 中高 |
| 3D 道具、场景布置、材质、LOD | 有条件（流水线门） | 拓扑、UV、LOD 部分可机检，风格一致性不可 | 腾讯混元 3D 内测建模 8 小时→2.5 小时 ([BAAI](https://hub.baai.ac.cn/view/49146))；Meshy 年化收入 1,500 万→4,000 万美元 ([PR Newswire](https://www.prnewswire.com/news-releases/meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-302828384.html)) | 中 |
| 主角角色与环境、绑定、look-dev、过场 | 低 | 一致性要求最高、品味、高可见 | 尚无经审计的案例 | 中 |
| 动画循环、重定向、清理 | 有条件 | 执行型，在引擎内部分可校验 | EA 称跑动循环从 12 套增至 1,200 套（2023 年公司说法）([Game Developer](https://www.gamedeveloper.com/production/ea-ceo-60-percent-of-dev-processes-could-be-impacted-by-generative-ai-)) | 低到中 |
| 表演型工作（主角配音、动捕表演） | 低 | 品味、同意制度、高可见 | SAG-AFTRA 2025 协议的同意与披露条款；《ARC Raiders》重录 | 中 |
| 次要配音、群杂、占位语音 | 西方有条件（受同意约束）；中国高 | 授权复制、低显著性 | 成功的 AI 作品更多用于配音（24% 对 8%） | 中 |
| QA：回归、崩溃、性能、合规 / 探索性"手感"测试 | 有条件偏高 / 低 | 结果可校验 / 依赖手感 | Unity 自动化试玩 35%；史克威尔艾尼克斯目标到 2027 年底由生成式 AI 承担 70% 的 QA 与调试（目标，非结果）([VGC](https://www.videogameschronicle.com/news/square-enix-says-it-wants-generative-ai-to-be-doing-70-of-its-qa-and-debugging-by-the-end-of-2027/)) | 中 |
| 关卡白盒与程序化变体 / 心流与乐趣 | 有条件 / 低 | 导航网格与指标可查，乐趣不可 | 据匿名信源报道，King 以自研 AI 工具替代部分关卡设计与文案岗位 ([mobilegamer.biz](https://mobilegamer.biz/laid-off-king-staff-set-to-be-replaced-by-the-ai-tools-they-helped-build-say-sources/)) | 低到中 |
| 次要叙事文本 / 主线与角色塑造 | 仅产量·品味型 / 低 | 可见，被玩家读作"低投入" | Unity 叙事写作 44%；评论主题分析 ([arXiv](https://arxiv.org/abs/2608.11539)) | 中 |
| 经济与平衡调优、长线运营内容变体 | 有条件 | 可模拟部分迁移；内容节奏是军备竞赛，会侵蚀稀缺性 | 使用 AI 代理的开发者中 38% 用于动态平衡与调优 ([Google Cloud](https://www.googlecloudpresscorner.com/2025-08-18-90-of-Games-Developers-Already-Using-AI-in-Workflows,-According-to-New-Google-Cloud-Research)) | 低到中 |
| 运行时 AI 与 AI 原生：LLM NPC、陪伴、生成式 UGC、世界模型 | 新任务（N） | 按需求扩张与单位经济评估，而非生产率 | 《逆水寒》手游 3 天内玩家自捏 AI NPC 超过 500 万 ([IT之家](https://www.ithome.com/0/791/380.htm))；AI 陪伴应用 2025 年约 1.2 亿美元 ([TechCrunch](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025)) | 低 |
| 研究、行政、市场、社区等非工艺工作 | 高 | 文本为主、玩家看不见 | GDC 使用者中研究与头脑风暴 81%；发行与支持岗使用率 58% 对工作室 30% | 高 |

这张地图揭示了用户命题（a）真正的含义。游戏在工时上比软件**更**偏执行（资产生产本身就是量产工作），所以如果内容类执行任务能像代码一样迁移，AI 对整款游戏的 Amdahl 上限反而会**高于**只算编程的上界；它没有这样迁移，是因为主导游戏的执行工作被一致性、权利与可见性三道门把守，而且这些门在中西方开合程度不同。另一方面，游戏里稀缺的投入早在 AI 之前就是判断：Supercell 到 2023 年初为推出 5 款成功游戏砍掉了 30 多款 ([VentureBeat](https://venturebeat.com/games/supercell-ceo-says-company-has-5-hit-mobile-games-and-killed-30/))，Voodoo 每年测试上千个原型、只有少数正式上线 ([Deconstructor of Fun](https://www.deconstructoroffun.com/blog/2024/6/3/voodoos-secret-sauce-from-0-to-250m-hybridcasual-revenue-in-3-years))，近年的小团队爆款几乎都在生成式 AI 普及之前、以很低的成本做成——《PEAK》开发成本不到 20 万美元卖出 200 万份 ([Game Developer](https://www.gamedeveloper.com/production/how-co-op-climbing-hit-peak-achieved-2-million-sales-for-less-than-200-000-))，《光与影：33 号远征队》核心团队约 30 人（不含外包与发行商营销）、预算不到 1,000 万美元 ([GameSpot](https://www.gamespot.com/articles/clair-obscur-expedition-33-budget-was-under-10-million-report/1100-6536874/))，《小丑牌》由单人开发、销量超过 500 万份 ([Game Developer](https://www.gamedeveloper.com/business/balatro-sells-5-million-copies-after-end-of-year-spike))。编程里"写代码不再是约束"是 AI 带来的新状态；在游戏里，"生产不是约束"早已是常态。

### 游戏的三类工作：只能给方向，不能给百分比

游戏业没有任何按 C/E/D 记录工时的数据，下表按"职能权重 × 各职能的 C/E/D 结构 × 迁移类别"推出方向与置信度，不给百分比。

| 度量（游戏生产） | 预期方向 | 最明显的地方 | 置信度 | 附注 |
|---|---|---|---|---|
| 人的执行（E）工时份额 | 下降 | 中国移动 2D、买量素材、配音（2023–26 年已明显下降）；各地的代码、QA、本地化；西方 AAA 主角内容基本不变 | 方向中，幅度无 | 增益数字几乎全是公司说法或自我感知，没有受控研究 |
| 执行产出量（资产、变体、发行数） | 大幅上升 | Steam 长尾、小游戏、买量素材、长线运营内容 | 高 | 发行与素材数量有测量，单作资产量没有 |
| 人的决策/验收（D）工时份额（筛选"抽卡"、精修、语言质检、评审、试玩分析） | 上升 | 所有引入 AI 初稿的管线 | 中 | 底部的 D 在扩张且被折价，签字权向顶部集中——"D 升"不等于"溢价升" |
| 人的创意（C）工时份额 | 持平到上升 | 方向、核心设计、叙事 | 低到中 | AI 已进入构思（研究与头脑风暴 81%），C 是被增强而非不受影响 |
| 初级执行岗与外包 | 率先下降 | 外包 2D、翻译、QA 供应商、初级美术 | 方向中，AI 归因低 | 与中国版号冻结、疫情后收缩、资本成本重置混杂 |
| C/D 的成本份额 | 上升（Baumol 效应） | 保留资深员工的工作室 | 低 | 没有工作室预算数据；前提是 C/D 薪酬不降 |

"D 升但被折价"是游戏与编程最需要区分的地方。编程里评审与验收仍由资深工程师承担，招聘反弹也集中在资深岗位；创意行业里，验收层却常常被压价：中国游戏插画师被邀请以原稿酬约十分之一的价格"修改 AI 图" ([Rest of World](https://restofworld.org/2023/ai-china-video-game-layoffs-illustrators/))，译后编辑的单价更低、工作量却"不比重译少" ([虎嗅](https://www.huxiu.com/article/4876156.html))，新出现的岗位是围绕"抽卡"（大量生成、挑出最好）组织的 ([新浪科技](https://finance.sina.com.cn/tech/roll/2026-09-23/doc-inisvcpx6082362.shtml))。创意验证没有编译器和单元测试，只能依赖美术总监的眼睛、双语审校或上线后的指标，所以游戏的方向与筛选层会比编程更大、更资深，而底部的"修图工"会更便宜。

### 趋势预测：五条可检验的判断

以下是研究者据方法论推出的预测，不是测量，每条都附证伪条件。**G1 产量稀释**：发行量继续上升（Steam 2026 年约 2.4 万款的节奏），AI 标注份额继续上升，但中位收入不回升、头部份额不下降，供给的价值弹性接近零；若发行量上升的同时中位收入止跌，或总时长与支出按供给比例加速，则被证伪。**G2 可见 AI 的接收折扣**在 PC 与主机核心玩家中至少持续到 2027 年，收益取决于打磨；若匹配后评论数差距缩小到 10% 以内、推荐率差距缩小到 5 个百分点以内，则说明这道门正在打开。**G3 瓶颈移向验收**：采用 AI 的工作室里，美术总监评审、设计评审、QA 与主机认证队列的时延上升，C/D 的预算份额上升；若吞吐上升而评审时延不升，则被证伪（这需要工作室数据）。**G4 初级执行岗先减**：初级美术、QA、本地化岗位相对资深 C/D 岗位下降，外包从按件计价转向"AI 初稿 + 精修"的费率；若初级美术招聘在采用 AI 后反而上升，则被证伪。**G5 同质化**作为 G1 的子指标：AI 重度作品的视觉与设计多样性下降、突破性爆款比例不升；已有研究显示文本生成图像让创作者产量提高约 25%、每次浏览的收藏提高约 50%，但平均新颖度下降 ([Zhou & Lee](https://academic.oup.com/pnasnexus/article/3/3/pgae052/7618478))。

时间维度上（同样是预测）：2026–27 年是执行层与不可见任务的降本期，引擎把第三方模型接入编辑器——虚幻 5.8 已加入实验性 MCP 插件，虚幻 6 的抢先体验目标定在 2027 年底 ([Epic](https://www.unrealengine.com/news/state-of-unreal-2026-top-news-from-the-show))；世界模型仍停留在构思与预演级别，Project Genie 单个世界约一分钟、720p/24fps ([Naavik](https://naavik.co/digest/project-genie-and-the-stock-markets-category-error/))；2027–29 年更可能出现"传统引擎掌管状态与逻辑、生成模型负责视觉或内容"的混合形态；完全由神经网络运行的商业游戏没有可靠的时间表。

### 三分诊断用在游戏上：长尾"根本没有"，在位者"不在生产者收入里"，AI 原生"尚未"

把第三节的三分诊断搬到游戏，预测是分层的。**长尾里是"根本没有"**：AI 标注作品占三成发行、一到两成多的估算销量，成功比例只有非 AI 作品的一半多，这是供给稀释而不是价值创造——但也只是"缺乏增量价值的证据加上供给膨胀的正面证据"，不是 AI 摧毁价值的证明。**在位者与平台那里是"不在生产者收入里"**：不可见任务上节省的成本会被竞争投入更大的内容范围、更快的更新节奏与更多的买量，持久收益归平台（Steam、Roblox、Epic、微信）、IP 持有者、善于买量的发行商，以及在中腰部崛起、有品味的团队。**AI 原生体验是最可能属于"尚未"的通道**，也是与触达、UGC 一起少数几条能扩张需求而不只是扩张供给的通道，其中只有它直接创造新的需求类别。与软件相比，游戏的转化率更低但不是零：软件的需求是生产性的、潜在需求会随造价下降被释放；游戏卖进的是一个缓慢增长、由爆款驱动的时间预算。历史表明，当廉价生产遇上新的触达或参与方式时，蛋糕会变大——这正是 AI 在游戏里还没有押中的那一注。

## 七、机会地图：六条上行通道、三个陷阱、十个监测指标

机会地图由方法论直接推出：机会出现在三类地方——门都开着的地方（玩家看不见、可校验、按指标验收的任务），需求开关可能被拨动的地方（触达、UGC、AI 原生），以及新瓶颈所在的地方（验证与判断）。下表把每条通道的机制、证据、价值归属与风险放在一起；"领先指标"一列给出判断它是否兑现的观测点。六条通道按证据成熟度排序：第 1–2 条证据最实、可立即执行，但收益会被竞争部分消耗；第 3–4 条已有正相关证据，兑现取决于团队品味与发行能力；第 5–6 条上限最高、证据最弱，是需求侧的押注。

| 上行通道 | 机制与迁移类别 | 当前证据 | 价值归属 | 主要风险 | 领先指标 |
|---|---|---|---|---|---|
| 1. 玩家看不见的降本：代码与工具、QA、本地化、次要配音、数据分析、原型白盒 | 高或有条件，五道门基本敞开 | 成功的 AI 标注作品集中在配音与本地化；Valve 豁免开发工具；编程 RCT +26% | IP 持有者、平台、中腰部工作室；部分被竞争消耗 | 红皇后效应：节省被投入更大范围和更快节奏 | 外包单价；QA 与本地化的单位成本 |
| 2. 验证工程与引擎内代理：自动试玩、画风一致性分类、平衡模拟、评审界面、MCP | 把"有条件"任务推向"高" | 虚幻 5.8 实验性 MCP 插件、虚幻 6 抢先体验目标 2027 年底；Unity 调查中半数开发者使用 MCP 服务器；游戏 QA 类 AI 初创合计融资约 3,580 万美元、无一到 B 轮 ([Naavik](https://naavik.co/ai-gaming/the-state-of-ai-for-game-qa/)) | 引擎与模型厂商（租金上移），独立插件空间窄 | 可靠性不足；被引擎捆绑 | 第一个经审计的"QA 或语言质检工时减半且质量不降"案例 |
| 3. 更快地找到乐趣：原型与迭代搜索 | 对有品味的团队是主要上行，也是历史上新品类诞生的机制 | Supercell、Voodoo 的高淘汰率；PC 支出中前 20 名以外的份额 48%→56% | 有品味的团队、中腰部 | "AI 不降低风险，只会让工作室更快地放大错误的赌注" ([Bain](https://www.bain.com/about/media-center/press-releases/2026/gamings-next-winners-will-be-built-on-player-focus-ai-powered-personalization-and-direct-relationships-bain-co-report-finds/)) | AI 标注小团队的命中率对比匹配的非 AI 团队 |
| 4. 触达：本地化与配音进入新语言市场 | 高；目前唯一与"成功"正相关的 AI 用途 | 成功画像偏重本地化（18% 对 6%）与配音（24% 对 8%）；Steam 2026 年上半年增长部分来自中国玩家涌入 | 发行商、平台 | 叙事与文化质量；配音同意 | AI 本地化作品在非英语地区的收入占比 |
| 5. UGC 平台与"创作即游玩" | 平台拥有发现渠道并按参与度付费时，廉价创作能扩大平台价值 | Roblox 截至 2026 年 6 月的 12 个月创作者分成约 17 亿美元（约 +50%，其中包含 4 月兑换率上调 42%），中位创作者约 1,500 美元 ([TechSpot](https://www.techspot.com/news/113855-roblox-top-creators-making-65-million-year-while.html); [Roblox](https://about.roblox.com/newsroom/2026/04/roblox-fuels-high-fidelity-games-over-18-players-increases-qualifying-devex-rate-42))；《堡垒之夜》创作者岛屿 2024 年占 36.5% 游戏时长，累计分成超过 10 亿美元 ([Fortnite](https://www.fortnite.com/news/fortnite-ecosystem-2024-year-in-review-celebrating-creators-and-looking-ahead); [Tubefilter](https://www.tubefilter.com/2026/06/17/epic-games-unreal-editor-for-fortnite-creator-payouts/))；微信在开发让普通用户用自然语言写小游戏的 AI 编程 ([腾讯新闻](https://news.qq.com/rain/a/20260529A05IF300))；超过八成微信小游戏开发者是 30 人以下团队 ([证券日报](http://www.zqrb.cn/gscy/gongsi/2026-01-17/A1768566351773.html)) | 平台为主，创作者收入极度集中 | 爆款驱动的波动；推理成本；未成年人安全与审核 | 创作者分成与时长份额，结合 AI 创作工具的采用率 |
| 6. AI 原生体验（新任务） | 唯一直接创造新需求类别（而非放大既有需求）的通道 | AI 陪伴应用 2025 年约 1.2 亿美元（仅应用商店，是下限），约为全球游戏市场的 0.06%；《逆水寒》手游玩家 3 天自捏 500 万个 AI NPC；Rec Room 于 2026 年 6 月关停，据 IBTimes UK 报道其 AI 功能的单用户月成本高于订阅净收入 ([TechCrunch](https://techcrunch.com/2026/03/31/social-gaming-platform-rec-room-once-valued-at-3-5b-is-shutting-down/); [IBTimes UK](https://www.ibtimes.co.uk/rec-room-shuts-down-ai-costs-overwhelm-revenue-1789414)) | 模型厂商与平台 | 单位经济；安全与监管；"最后 20%"的打磨 | AI 原生品类占全球游戏收入超过 1%（约 20 亿美元），或头部 50 款游戏披露 AI 功能带来的留存或付费提升 |

对工具供应商而言，资产生成是第一个出现九位数收入业务的环节，但它们卖的是横向市场：Meshy 在 2026 年 7 月以 15 亿美元估值融资约 4 亿美元，年化收入从 2025 年 11 月的 1,500 万美元增至 2026 年 4 月的 4,000 万美元 ([PR Newswire](https://www.prnewswire.com/news-releases/meshy-raises-nearly-400-million-at-a-1-5-billion-valuation-the-largest-round-to-date-in-ai-3d-302828384.html))，ElevenLabs 2025 年底年化收入超过 3.3 亿美元 ([TechCrunch](https://techcrunch.com/2026/01/13/elevenlabs-ceo-says-the-voice-ai-startup-crossed-330-million-arr-last-year/))——游戏只是它们的一个客户群，游戏预算本身撑不起这些估值。与编程一样，编辑器内的代码与操作代理正在被引擎通过 MCP 吸收，租金流向引擎方与模型厂商，给独立的"AI for Unity/Unreal"插件留下的空间很薄。

### 三个陷阱：可见污名、模板化军备竞赛、推理成本与权利

**第一个陷阱是在高端 PC 与主机上把 AI 用在玩家看得见的地方。** 首月评论少一半、推荐率低约 18 个百分点、奖项被收回，这些代价落在"高潜力"作品上最重——Game Oracle 的分析者直言，对低质量游戏 AI 没有差别，对高潜力游戏"AI 污名"是真实而严厉的惩罚 ([PC Gamer](https://www.pcgamer.com/software/ai/data-analyst-finds-ai-stigma-on-steam-can-reduce-the-number-of-reviews-a-game-gets-by-around-53-percent-and-the-reviews-it-does-get-are-more-negative/))。移动端与中国市场缺少同类数据，折扣大小未知。**第二个陷阱是模板化赛道的同质化与买量军备竞赛。** AppsFlyer 的数据显示 2025 年游戏买量支出约 250 亿美元、只增长 3.8%，广告曝光却增长 20%——单次曝光并没有更贵，问题是更多素材在争夺持平的注意力，其原话是"不是创意短缺，而是创意过剩" ([AppsFlyer](https://www.appsflyer.com/company/newsroom/pr/gaming-marketing/))；行业媒体报道中国小游戏广告素材的平均生命周期只有 5.2 天，创意同质化推高了获客成本（行业媒体数据）([游戏陀螺](https://www.youxituoluo.com/533295.html))。音乐是最清楚的外部类比：Deezer 每日上传中 AI 生成曲目已超过一半，但只占 1%–3% 的播放量，其中 85% 被判定为欺诈播放 ([TechCrunch](https://techcrunch.com/2026/07/21/music-streamer-deezer-says-more-than-50-of-daily-uploads-are-ai-generated/))——供给份额远高于消费份额，平台最终以标注、排除推荐和去货币化作为质量闸门。**第三个陷阱是推理成本、安全与权利。** Rec Room 的关停被报道为推理成本随用户量增长、最终压垮单位经济的案例（关停本身有多方报道，AI 成本细节仅见于 IBTimes UK）；Character.AI 在诉讼压力下禁止未成年人进行开放式聊天 ([CNBC](https://www.cnbc.com/2025/11/24/characterai-to-ban-teens-from-open-ended-chats-human-interaction-is-crucial-psychotherapist-says.html))；表演者同意、训练数据授权与"仅靠提示词不构成作者身份"的版权立场，决定了 AI 生成资产能否被独占与保护。

中西方的机会结构并不相同。中国没有工会这道门，披露规范较弱，移动与小游戏占比高，2D 美术、配音与买量素材的替代发生得更早、更深；机会在小团队借助 AI 进入小游戏与出海、以及平台内的 AI 创作，风险在同质化、平台抽成与流量分配，以及 2025 年 9 月起施行的 AI 内容标识义务。西方的代码辅助是最主要的生产用途，工会协议、Steam 披露与玩家污名把守着可见内容；机会在不可见降本、验证工程与 UGC 平台，风险在声誉与劳资冲突。

### 十个季度指标：何时应当改写本报告的结论

| # | 指标 | 当前读数（口径见前文） | 改变结论的阈值 |
|---|---|---|---|
| 1 | GDC 工作者个人使用率，工作室与发行/支持岗分列 | 36%；工作室 30%、发行/支持 58% | 两期之内工作室员工使用率超过 50%：游戏进入编程 2024–25 年的强度阶段 |
| 2 | AI 标注作品的发行份额与估算销量份额 | 30.8% 对约 10%–27% | 连续 3 个季度销量份额 ≥ 发行份额：AI 供给开始转化为价值 |
| 3 | 匹配后的评论数与推荐率差距 | 首月评论少约 53%；推荐率低约 18 个百分点 | 评论差距小于 10%、推荐差距小于 5 个百分点：可见 AI 的门在打开 |
| 4 | 头部作品中的 AI 披露 | 12 款八位数收入作品带披露，多为后来加入 AI 的既有游戏 | 收入前 100 的披露率 ≥ 整体发行披露率：AI 进入爆款而不只在长尾 |
| 5 | 发行量与中位收入 | 约 2.4 万款/年的节奏；2025 年上架作品中位约 249 美元 | 发行量上升同时中位收入止跌：需求在扩张 |
| 6 | 新作时长份额与总时长 | 新作约占 13%；2025 年 PC+主机总时长 −1% ([GameDev Reports](https://gamedevreports.substack.com/p/newzoo-pc-and-console-market-in-2026)) | 新作份额超过 20% 或总时长年增超过 5%：注意力约束放松 |
| 7 | 玩家态度（代表性样本） | 美国约 25%"降低购买意愿" | 代表性样本中低于 15%：可见 AI 的折扣在消退 |
| 8 | 外包与初级岗位晴雨表 | 外包原画单价约 8,000→2,000 元（2023）；据报道传统美术岗需求 −35% | "AI 初稿 + 精修"费率卡取代按件计价；初级美术/QA/本地化岗位相对资深岗位下降 30% |
| 9 | 编程的领先信号 | DORA 稳定性关联仍为负；评审时长 +91% 至 +441.5% | 稳定性关联转正且评审时延下降：验证瓶颈被解决，预计游戏编程增益随后 12–18 个月兑现 |
| 10 | AI 原生与需求扩张收入 | 陪伴应用约 1.2 亿美元（约 0.06%）；Roblox 分成约 17 亿美元 | AI 原生品类超过全球游戏收入 1%，或头部游戏披露 AI 功能带来留存/付费提升 |

每个季度记录读数、日期与定义；任意两个指标连续越过阈值，就应当按第五节的规则重评迁移地图。

## 结论

编程给游戏最可迁移的经验，不是"AI 让产量翻倍"，而是"产量翻倍之后，瓶颈转移到验证与验收"。在编程里，验证有编译器、测试与 CI 可以扩容，前沿公司正在把验收本身工程化；在游戏里，验收的核心是品味——乐趣、手感、画风一致性、情感可信度——它没有编译器，只能依赖少数资深判断者和上线后的玩家反应。因此游戏里最稀缺、也最值得投资的，是让判断变快、变得可复制的能力：一边是验证工程，把一部分品味转写成可校验的信号；另一边是更便宜的"找乐子"搜索，更多原型、更早砍掉错误的项目。能同时做好这两件事的团队，才会把廉价执行转化为命中率，而不是转化为长尾里更多无人问津的作品；做不到的团队，AI 只会让它们更快地放大错误的赌注。

第二个新判断关乎价值的去向。编程的增量价值流向了模型与工具厂商和客户；游戏的增量价值更可能流向平台、IP 持有者和注意力的所有者，因为游戏卖的是时间而不是功能。用户的两条视角因此都成立，但需要改写：游戏不主要是编程，却主要是被一致性、权利和可见性三道门把守的执行，这些门在中国和西方开合不同；产量不等于价值，但"不在生产者收入里"和"根本没有"必须分开看，AI 原生体验是唯一可能属于"尚未"的地方。按 2026 年的证据，AI 在游戏里仍是"单独到来"的廉价生产；只有当它与一种新的触达或参与方式——UGC 创作、个性化的社交体验、低门槛的跨语言发行——一起到来时，游戏业的蛋糕才会变大。第七节监测表中的第 2、4、10 项，就是判断这一转折是否发生的最早信号。

## 附录 A　严格研究设计（未来工作）

正文只执行了方法论中本报告能用现有数据完成的部分（参考类、任务级迁移判断、对现有数据的假设检验、监测指标）。若要把外推变成可验证的研究，需要下列更重的设计。

**A.1 十维迁移评分表。** 正文的五道门由以下十个维度合并而来，每个任务在编程与游戏两侧各打 1–5 分，差异≥2 分的维度视为"差异节点"。这是结构化类比的评分启发法，借用了可迁移性分析"标出机制差异"的思路，但不是形式化的因果可迁移性演算 ([Cartwright & Hardie](https://global.oup.com/academic/product/evidence-based-policy-9780199841622))。

| 维度 | 操作问题 | 编程典型值 | 游戏示例（高 → 低） |
|---|---|---|---|
| T1 可验证性 | 是否有成本远低于生成成本的客观自动校验 | 高（编译器、测试、CI） | 构建、崩溃、性能与内存预算、字符串长度、导航网格 → 美术方向、乐趣、情感冲击 |
| T2 反馈时延与重试成本 | 一次尝试到反馈、再重试要多久、多贵 | 秒到分钟 | 渲染预览（分钟）→ 试玩（天）→ 市场反应（月） |
| T3 模块化与耦合 | 产出能否单独验收、错误能否定位 | 中到高 | 内容通过画风、正典、关卡心流与节奏彼此耦合 |
| T4 数字原生与训练数据 | 制品是否类文本、是否有大规模可授权语料 | 很高 | 2D 图像高但法律有争议；带绑定的 3D、动画、专有引擎数据较低 |
| T5 容错与可逆 | 错误能否在触达用户前被拦截、能否低成本回滚 | 高（但 AI 提高了不稳定性） | 已发布的视觉或叙事错误公开且有声誉代价 |
| T6 隐性知识与品味 | 验收是否依赖无法编码的判断 | 中 | 美术方向、手感、喜剧与恐怖节奏：高 |
| T7 一致性要求 | 是否需在成千上万资产间保持风格、正典、角色声音一致 | 规范可由 lint 检查 | 高，且大多不可机检 |
| T8 IP、法律与劳动约束 | 可版权性、训练数据授权、表演者同意 | 低到中 | 美术、音乐、配音与表演：高 |
| T9 受众接受度 | AI 贡献是否对买家可见、是否有披露折扣 | 终端用户不可见 | 可见创意资产折扣高；工具、QA、后端低 |
| T10 价值机制 | 更便宜或更多的产出是否提高付费意愿，还是只增加供给 | 部分有弹性 | 注意力约束、爆款主导 |

**A.2 六层分析单元。** 正文的四层之外，严格设计还应单列"工作流/流水线阶段"（用于测量交接、评审闸口、排队与返工，即 Amdahl 与约束理论的对象）和"企业/工作室"（用于测量采用时点、互补性投入、成本结构与利润率，即 J 曲线的对象）([Brynjolfsson, Rock & Syverson](https://doi.org/10.1257/mac.20180386))。

**A.3 八个研究阶段。** P0 预注册与定义词典（"AI 使用"的分级、存活加权的贡献、披露口径、发行量数据源、各假设的阈值与统计功效）。P1 建立任务清单：编程用 O*NET 加开发生命周期任务，游戏从流水线文档、招聘启事、制作名单与从业者演讲中整理约 150–300 条任务陈述，两位编码者加经过验证的 LLM 辅助标注 C/E/D。P2 由每个职能至少 3 名专家做两轮德尔菲评分，报告评分者一致性。P3 以编程 2022–26 年与五个历史案例作参考类，统一编码产量倍数、单价、集中度、执行岗就业、C/D 薪酬与见效年数，作为外部视角的先验 ([Flyvbjerg](https://arxiv.org/pdf/1302.3642))。P4 按职能分别拟合"采用"与"强度"两条扩散曲线——跨国经验表明采用时滞会收敛而使用强度会分化 ([Comin & Mestieri](https://doi.org/10.1257/mac.20150175))——并估计编程到游戏的领先—滞后。P5 因果识别：以采用时点做交错双重差分（避免双向固定效应偏误）([Callaway & Sant'Anna](https://doi.org/10.1016/j.jeconom.2020.12.001))，以模型发布做事件研究（各职能暴露不同），在工作室内部对执行型资产任务做随机对照试验并由美术总监盲评，对资深游戏程序员复制 METR 式试验以测量感知偏差。P6 聚合与验证：任务到流程用 Amdahl 与排队模型（代入实测评审产能），流程到产品用 O 型环/CES，产品到市场用注意力约束下的重尾需求模型，先用观测到的工作室与市场结果验证再做预测。P7 情景预测，按季度用 Brier 分数校准。

**A.4 十四项陷阱与缓解。**

| 陷阱 | 缓解 |
|---|---|
| 产量≠价值 | 每个产量指标配同一单元的价值指标；贡献按存活加权；报分布 |
| 调查偏差（感知差距、厂商样本、污名导致少报） | 以行为数据为锚；问具体任务与频率；敏感问题用列表实验；按独立性给来源评级 |
| 定义不一致 | 定义词典；跨定义的敏感性分析 |
| 选择效应 | 按团队规模、预算、品类匹配；检验前趋势；随机对照试验 |
| 厂商说法 | 来源分级；要求方法披露；尽量复现 |
| 混杂冲击（利率、税制、疫情后修正、游戏业裁员潮） | 低暴露对照组；企业内资历对比；宏观控制 |
| 重尾 | 中位数、分位数、对数模型、命中率、尾部指数 |
| 移动且参差的能力前沿 | 判断标注日期，每 6 个月重评；做任务级而非职能级结论 |
| 聚合偏误 | 替代弹性小于 1 的 CES/O 型环聚合；瓶颈建模 |
| 层级错配 | 四层匹配规则 |
| 古德哈特效应（PR 数、资产数易被刷高） | 每个计数旁报告价值与质量指标 |
| 同质化 | 在市场层面测量多样性与新颖度；跟踪突破性爆款比例 |
| 构成变化 | 人均与单作指标与总量并列；按团队规模分层 |
| 迁移误差（效应随情境差异很大） | 给出迁移置信等级；把迁移来的编程效应当作先验，用游戏数据更新 |

## 附录 B　口径说明与未采用的数字

本报告的数据截至 2026 年 9 月 28 日。多数一手页面是经搜索摘要核对的，数字以研究笔记与事后质检（含协调人最终核验）的结论为准；标为"公司说法""自报""厂商调查""估算""预测"的数字，都不应被当作独立测量。几条贯穿全文的口径：Stack Overflow 的"正在使用或计划使用"与"正在使用""每日使用"是三个不同指标；DORA 样本是技术从业者而非只有开发者；"AI 写的代码占比"至少有七种不可比口径，只有分类器研究与提交署名统计属于独立测量；Copilot 的"用户"含免费层，与付费订阅不可换算；各公司年化收入是按近期月份或周数年化的运行率，不是审计收入（Cursor 的年化收入各媒体口径不一：路透社在收购时报道约 26 亿美元，Dealroom/福布斯为 40 亿美元以上）；Steam 的 AI 披露份额分"发行份额""目录份额""估算销量份额"三种，而且 2026 年 1 月规则变化后不再覆盖编程工具；Newzoo 的市场规模不跨版本比较；游戏裁员总数只引用区间与具体追踪器。

以下数字因来源不足、口径错误或已被更正而**未被采用**：所谓"Stack Overflow 2026 年调查结果"页面（实为 2025 年数据）；SO 2025 年"正在使用 78%"；"开发者每周 11.4 小时审 AI 代码"；Claude Code"2026 年 5 月年化 80 亿美元"及"占 AI 编程市场 54%"作为 2026 年事实；百度"2025 年底 AI 代码超过一半"；METR"16 小时以上"作为点估计；SemiAnalysis"2026 年底 20%"作为数据；把"三分之一的 PR 涉及代理"当作代理编写份额；Daniotti 等人预印本 v1 的旧数字（以 *Science* 版本为准）；Unity"开发时间下降 77%"作为 AI 生产率；Steam AI 披露"增长 681%"；2026 年 Steam 截至 9 月"20,253 款"；"游戏业 2022–26 年累计裁员 45,000/58,494 人"；短剧"98.7% 亏损""超过 95% 由 AI 制作"；"《帕鲁》3,050 万份"；Voodoo"0.4% 原型上线"；"堡垒之夜 47% 时长来自创作者岛屿"；"新作的游戏时长份额在下降"（Newzoo 数据显示大致稳定）；以及把"AI 标注作品评论少 53%"说成"销量少 53%"。
