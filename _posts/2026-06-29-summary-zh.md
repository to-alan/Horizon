---
layout: default
title: "Horizon Summary: 2026-06-29 (ZH)"
date: 2026-06-29
lang: zh
---

> 从 172 条内容中筛选出 12 条重要资讯。

---

1. [GLM 5.2 在网络安全基准测试中击败 Claude](#item-1) ⭐️ 8.0/10
2. [开发者用 Claude Code 做 MRI 第二意见](#item-2) ⭐️ 8.0/10
3. [布朗大学爆发 AI 作弊丑闻](#item-3) ⭐️ 8.0/10
4. [KIDS 法案要求在线访问进行年龄验证](#item-4) ⭐️ 8.0/10
5. [北京率先开展外卖平台降本增利协商](#item-5) ⭐️ 8.0/10
6. [Firmus 与 NVIDIA 联手在印尼建设 360MW AI 工厂，部署 17 万颗 GPU](#item-6) ⭐️ 8.0/10
7. [AR 游戏数据被用于军事 AI 引发国安警告](#item-7) ⭐️ 8.0/10
8. [多家巨头组建电池循环经济设计联盟](#item-8) ⭐️ 8.0/10
9. [Anthropic 联合创始人预测 AI 将在 2028 年实现自我改进](#item-9) ⭐️ 8.0/10
10. [英伟达「最危险」论文：AI 自繁衍代码无限进化](#item-10) ⭐️ 8.0/10
11. [可交互的微型 Transformer 学习工具](#item-11) ⭐️ 8.0/10
12. [Google 因算力短缺限制 Meta 使用 Gemini](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM 5.2 在网络安全基准测试中击败 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.0/10

一篇新的博客文章称，来自 Z. AI 的开源大语言模型 GLM 5.2 在内部网络安全基准测试中优于 Claude。该模型拥有 753B 参数和 1M token 的上下文窗口。 这一说法的提出挑战了像 Claude 这样的专有模型在特定领域的主导地位，为网络安全任务提供了一种经济高效的替代方案。然而，社区对基准测试的可靠性和实际影响展开了辩论。 GLM 5.2 在 Terminal-Bench 2.1 上得分为 81.0，在 SWE-bench Pro 上得分为 62.1，可通过 OpenRouter 和 Ollama 使用。尽管基准测试成绩令人印象深刻，但一些用户报告在重复测试中性能存在不一致。

hackernews · jms703 · 6月28日 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48709670)

**背景**: 大语言模型越来越多地用于网络安全任务，如漏洞查找和威胁情报。基准测试用于衡量它们的性能，但结果可能被操纵或无法反映实际场景。GLM 5.2 是一个 753B 参数的模型，专为长周期代理任务优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ollama.com/library/glm-5.2">GLM - 5 . 2 is Z. ai ’s flagship model for the era of long-horizon tasks.</a></li>
<li><a href="https://openrouter.ai/z-ai/glm-5.2">GLM 5 . 2 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/glm-5-2-review-2026">GLM - 5 . 2 Review 2026: Z. ai 's 1M-Context AI Model</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人称赞 GLM 5.2 是日常编程的经济高效选择，而另一些人则质疑基准测试方法。一个主要担忧是代理基准测试很容易被操纵，且每月 160 美元的价格与 Claude 和 Codex 等竞品接近。

**标签**: `#AI`, `#LLM`, `#cybersecurity`, `#benchmarks`

---

<a id="item-2"></a>
## [开发者用 Claude Code 做 MRI 第二意见](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

一名开发者使用 AI 编程助手 Claude Code 分析自己的 MRI 影像，就肩部损伤诊断获取第二意见。 这凸显了个人使用通用 AI 工具进行健康分析的增长趋势，引发了关于 AI 在医疗决策中的信任、准确性和作用的重大讨论。 作者向 Claude Code 提供 MRI 影像并请求解读，其回答与原始放射科医生报告相矛盾，导致作者质疑自己的治疗方案。但放射科医生的评论强调，由于该领域训练数据有限，AI 模型尚不能可靠地解读医学影像。

hackernews · engmarketer · 6月28日 16:35 · [社区讨论](https://news.ycombinator.com/item?id=48708941)

**背景**: Claude Code 是 Anthropic 开发的 AI 编程助手，旨在帮助开发者编写代码、调试和自动化任务，并非用于医疗诊断。该文章描述了一种非常规使用方式——用该工具解读医学影像，这超出了其预期用途，引发了对医疗中过度依赖 AI 的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>
<li><a href="https://claude.com/solutions/coding">Coding | Claude by Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论中的放射科医生警告说，像 Claude Code 这样的 AI 模型没有经过足够的医学影像数据训练，无法达到临床专业水平。评论者们还讨论了在无时间压力下向 AI 提问的心理舒适感，与对人类专家的信任形成了对比。

**标签**: `#AI in healthcare`, `#Claude Code`, `#medical imaging`, `#LLM applications`, `#trust in AI`

---

<a id="item-3"></a>
## [布朗大学爆发 AI 作弊丑闻](https://english.elpais.com/education/2026-06-28/ai-fraud-at-brown-university-academic-integrity-is-at-risk.html) ⭐️ 8.0/10

布朗大学的一位教授公开谴责考试中广泛存在的 AI 辅助作弊行为，凸显了学术诚信方面日益严重的危机。 这一事件凸显了机构在大语言模型时代重新设计评估方式的紧迫性，可能促使回归线下手写考试和口试。 计算机科学系的教授指出，AI 生成的答案很容易识别，但滥用规模令人震惊，引发了关于是否采用对抗性课程设计和线下评估的讨论。

hackernews · geox · 6月28日 16:41 · [社区讨论](https://news.ycombinator.com/item?id=48708991)

**背景**: 随着 GPT-4 等强大语言模型的兴起，学生可以生成像样的开卷考试答案，这对传统的学术诚信观念构成了挑战。大学正在努力适应这一变化，有人提议采用手写考试和一对一面试来验证理解水平。

**社区讨论**: 评论者大多同意手写考试是必要的，尽管有人指出监考过程繁琐。另一些人从博弈论角度认为，在当前激励机制下使用 AI 是理性选择，并对评分本身的目地提出质疑。

**标签**: `#AI`, `#education`, `#academic integrity`, `#exams`, `#cheating`

---

<a id="item-4"></a>
## [KIDS 法案要求在线访问进行年龄验证](https://www.eff.org/deeplinks/2026/06/kids-act-would-require-age-checks-get-online) ⭐️ 8.0/10

美国国会提出的 KIDS 法案要求在线平台强制进行年龄验证，引发了关于隐私和有效性的辩论。 若通过，该法律可能从根本上改变用户访问互联网的方式，潜在地削弱匿名性，并为政府强制在线身份核查树立先例。 该法案由众议员 Brett Guthrie（共和党-肯塔基州）和 Frank Pallone（民主党-新泽西州）发起，因隐私风险和潜在的数据泄露而受到批评，早期的年龄验证系统已发生过此类事件。

hackernews · bilsbie · 6月28日 11:56 · [社区讨论](https://news.ycombinator.com/item?id=48706560)

**背景**: 在线年龄验证通常要求用户提交个人身份证件或使用第三方服务，引发了对数据安全和公民自由的担忧。目前互联网缺乏内置的年龄验证机制，使得未成年人很容易绕过限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Age_verification">Age verification - Wikipedia</a></li>
<li><a href="https://hyperverge.co/blog/how-does-age-verification-works-online/">How Does Age Verification Work Online? A Complete Guide</a></li>
<li><a href="https://ondato.com/blog/what-is-age-verification/">Age Verification: How It Works and Key Approaches Explained | Ondato</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了怀疑，指出关于社交媒体对儿童伤害的研究尚无定论，并质疑国际社会突然推动年龄验证，怀疑是特殊利益集团的游说。其他人则强调家长已有工具控制子女的设备使用。

**标签**: `#privacy`, `#age verification`, `#internet regulation`, `#children's safety`, `#policy`

---

<a id="item-5"></a>
## [北京率先开展外卖平台降本增利协商](https://www.ithome.com/0/969/776.htm) ⭐️ 8.0/10

北京市市场监管局率先建立平台经济“破卷向善”协商对话机制，并围绕餐饮外卖商家降本增利，首次与美团、淘宝闪购、京东外卖三家平台开展协商。 这标志着中国外卖市场迎来监管转向，旨在解决长期以来困扰数百万餐饮商家的激烈竞争和高成本问题。在补贴、收费、配送时间等方面达成的共识可能重塑平台行为，惠及商家和消费者。 五点共识包括优化补贴、收费让利、理性营销、对“明厨亮灶”商家给予扶持，以及不开展“分钟级竞速”配送。

rss · IT之家 · 6月29日 01:49

**背景**: 近年来，中国外卖平台陷入激烈的价格战和补贴战，商家常被迫承担高额佣金和配送压力。‘内卷’一词形容这种过度竞争。‘明厨亮灶’是政府推行的通过视频公开后厨的餐饮展示项目。‘分钟级竞速’指平台比拼最短送达时间，可能影响安全和质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://scjgj.beijing.gov.cn/zwxx/scjgdt/202606/t20260629_4733520.html">北京市率先建立平台经济“破卷向善”协商对话机制，围绕餐饮外卖商家降...</a></li>
<li><a href="https://society.yunnan.cn/system/2026/06/29/034059689.shtml">北京率先启动平台“破卷”对话机制，三大外卖平台承诺为商家减负</a></li>
<li><a href="https://beijing.qianlong.com/2026/0629/8689501.shtml">北京率先启动平台“破卷”对话机制，三大外卖平台承诺为商家减负</a></li>

</ul>
</details>

**标签**: `#platform economy`, `#food delivery`, `#regulation`, `#competition`, `#China`

---

<a id="item-6"></a>
## [Firmus 与 NVIDIA 联手在印尼建设 360MW AI 工厂，部署 17 万颗 GPU](https://www.ithome.com/0/969/763.htm) ⭐️ 8.0/10

这项大规模基础设施投资表明全球 AI 算力竞赛正在加速，Firmus 预计前六年从已签订的承购协议中获得 250-300 亿美元收入，凸显了大规模 AI 训练和推理的强劲需求。 该工厂将采用 NVIDIA DSX 平台进行设计与运营，GPU 包括当前 Blackwell 架构及未来的 Vera Rubin 架构。Firmus 与 NVIDIA 的战略合作延续至 2034 年，NVIDIA 还参与了 Firmus 2024 年 4 月的股权融资。

rss · IT之家 · 6月29日 01:37

**背景**: NVIDIA DSX 是一个集成参考设计、API 和软件的平台，用于构建和运营以最低 Token 成本为目标的 AI 工厂。Grace Blackwell 和 Vera Rubin 架构是 NVIDIA 面向 AI 负载的最新 GPU 设计，其中 Vera Rubin 于 2024 年发布，是 Blackwell 的继任者。AI 工厂是专门用于训练和运行生成式 AI 模型的大规模数据中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/data-center/products/dsx/">AI Factory Design, Simulation, and Operations | NVIDIA DSX Platform</a></li>
<li><a href="https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)">Blackwell (microarchitecture) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rubin_(microarchitecture)">Rubin (microarchitecture) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#NVIDIA GPU`, `#data center`, `#cloud computing`

---

<a id="item-7"></a>
## [AR 游戏数据被用于军事 AI 引发国安警告](https://www.ithome.com/0/969/750.htm) ⭐️ 8.0/10

国家安全部警告称，某知名 AR 手游旗下 AI 公司收集了用户近 300 亿份环境扫描数据，并可能利用这些数据训练可用于军事目的的人工智能模型，因其与某国军工企业存在合作关系。 这一揭露凸显了民用数据军事化的严重风险，威胁个人隐私、行业信任以及国家地理空间安全，促使各界呼吁加强数据治理。 该 AR 游戏的数据采集包括三维点云扫描、高精度 GPS 坐标和实时上传，能够精确重建室内空间和用户移动轨迹，远超传统拍照的信息量。

rss · IT之家 · 6月29日 00:51

**背景**: 增强现实游戏利用智能手机摄像头和传感器将虚拟物体叠加到现实世界中。为了运行，它们持续扫描环境，捕获视觉和空间数据。这些收集到的地理空间数据汇总后，可用于创建敏感区域的详细三维模型，构成国家安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/jun/12/pokemon-go-data-trained-ai-that-could-assist-military-drones-in-war-zones">Pokémon Go data trained AI that could assist military ... | The Guardian</a></li>
<li><a href="https://medium.com/arway/point-clouds-and-its-significance-in-ar-155db2673865">Point Clouds and it’s significance in AR! | by Mayank Raj | ARWAY | Medium</a></li>

</ul>
</details>

**标签**: `#data security`, `#AR technology`, `#national security`, `#privacy`, `#military use`

---

<a id="item-8"></a>
## [多家巨头组建电池循环经济设计联盟](https://www.ithome.com/0/969/728.htm) ⭐️ 8.0/10

CATL, BMW, Renault, Volvo, Google, Xiaomi, and others have launched the Global Energy Circular Economy Alliance and initiated a development plan for a Battery Recyclability Design Guide, expected to be released in 2027. This collaborative effort by major global companies could set industry-wide standards for battery recyclability, influencing regulations and design practices, and accelerating the transition to a circular economy for batteries. The guide will cover design principles for easy disassembly, diagnosis, repair, remanufacturing, and material recycling, and establish unified evaluation criteria for battery history, health status, degradation data, and recycling responsibility.

rss · IT之家 · 6月28日 14:29

**背景**: Battery circular economy aims to maximize resource efficiency and minimize environmental impact by extending battery life through repair, reuse, remanufacturing, and recycling. Recyclability design involves intentionally planning battery structures to facilitate efficient material recovery. This alliance builds on a growing global push for sustainable battery lifecycle management.

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rmi.org/battery-circular-economy-initiative/">Battery Circular Economy Initiative - RMI</a></li>
<li><a href="https://learn.sustainability-directory.com/area/battery-recyclability-design/">Battery Recyclability Design → Area → Sustainability</a></li>

</ul>
</details>

**标签**: `#battery recycling`, `#circular economy`, `#electric vehicles`, `#sustainability`, `#energy storage`

---

<a id="item-9"></a>
## [Anthropic 联合创始人预测 AI 将在 2028 年实现自我改进](https://www.36kr.com/p/3872524038362121) ⭐️ 8.0/10

Anthropic 联合创始人 Jack Clark 预测，递归自我改进（RSI）很可能在 2028 年底前成为现实，使 AI 能够自主发明并构建出比自己更强的继任者，无需人类研究人员参与。此外，谷歌 DeepMind 首席执行官哈萨比斯证实，所有前沿 AI 实验室都在全力推进 RSI。 来自著名 AI 人物的这一时间表标志着向人工超级智能（ASI）的潜在范式转变，可能影响全球经济、安全和治理。主要实验室专注于 RSI 的确认表明，该领域正在迅速接近一个关键里程碑。 Clark 基于对数百份公开 AI 发展数据的分析，给他的预测赋予了 60%的概率。MirrorCode 基准测试显示，Claude Opus 4.7 在 14 小时内以 251 美元的成本重建了一个 16000 行的 Go 代码库，其中一项任务让 AI 连续运行了 19 天，无需人工干预。

rss · 36氪 - 24小时热榜 · 6月28日 08:28

**背景**: 递归自我改进是指 AI 系统重写自身代码以变得更智能的过程，可能引发智力爆炸，导致超级智能。人工超级智能（ASI）是一种假设的 AI，在所有领域超越人类智能。2028 年的时间表基于加速发展的 AI 能力，例如能够执行持续超过 16 小时的任务，这已经超出了许多基准测试的衡量范围。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.ibm.com/think/topics/artificial-superintelligence">What Is Artificial Superintelligence? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#RSI`, `#AGI`, `#Anthropic`, `#DeepMind`

---

<a id="item-10"></a>
## [英伟达「最危险」论文：AI 自繁衍代码无限进化](https://www.36kr.com/p/3872518454776841) ⭐️ 8.0/10

英伟达与剑桥大学研究人员提出「红皇后哥德尔机器」（RQGM），该框架让 AI 智能体与其评估者共同进化，实现无需每次改动都进行数学证明的递归自我改进。 RQGM 克服了以往自我改进 AI 的关键局限，允许评估标准与智能体共同进化，可能加速迈向人工超级智能（ASI）的进程。 该系统采用「受控效用进化」过程：评估器在每个 epoch 内冻结，仅当新评估器在留出锚点数据上统计优于旧评估器时才被替换。论文报告了代码生成（通过率从 69.9%提升至 71.7%）和科学论文写作（接受率从 21.8%提升至 40.5%）的提升。

rss · 36氪 - 24小时热榜 · 6月28日 07:33

**背景**: 哥德尔机由 Jürgen Schmidhuber 于 2003 年提出，是一种理论上自我改进的 AI，但要求数学证明每次自我修改都有益——这使得其不切实际。最近的变体如达尔文哥德尔机（DGM）使用进化代替证明，但评估器固定不变。RQGM 通过共同进化智能体和评估器打破了这一限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.26294">The Red Queen Gödel Machine : Co-Evolving Agents and Their...</a></li>
<li><a href="https://arxiv.org/abs/2505.22954">[2505.22954] Darwin Godel Machine: Open-Ended Evolution of Self ...</a></li>

</ul>
</details>

**标签**: `#AI Safety`, `#Self-Improving AI`, `#NVIDIA`, `#Machine Learning`

---

<a id="item-11"></a>
## [可交互的微型 Transformer 学习工具](https://www.reddit.com/r/MachineLearning/comments/1uhw7fu/i_shrank_a_transformer_until_every_number_fitted/) ⭐️ 8.0/10

作者制作了一个完全可交互、可编辑的微型 Transformer，所有权重和向量都可修改，并能实时重新计算前向传播。 该工具提供了一种直观、可视化的方式理解 Transformer 的内部机制，对学生、教育者和自学人士很有价值。它弥合了抽象理论与具体计算之间的鸿沟。 该 Transformer 使用 6 个词汇、3 维嵌入，并包含一个注意力头和一个前馈块。所有权重都是随机且未经训练的，页面包含一个随机化按钮来重置它们。

reddit · r/MachineLearning · /u/DanielMoGo · 6月28日 12:35

**背景**: Transformer 是一种使用自注意力和前馈层处理序列的神经网络架构。前向传播通过注意力机制和前馈网络，从输入嵌入计算预测结果。该工具一步步展示前向传播过程，使每一步的计算都可见且可编辑。

**标签**: `#transformer`, `#education`, `#visualization`, `#interactive`, `#LLM`

---

<a id="item-12"></a>
## [Google 因算力短缺限制 Meta 使用 Gemini](https://www.ft.com/content/c5d52f72-71ef-40bc-bad3-61afdba8b378) ⭐️ 8.0/10

今年 3 月，Google 告知 Meta 因算力限制无法提供其要求的 Gemini AI 模型全部容量，相关限制至今有效，干扰了 Meta 的内部 AI 项目。Meta 因此要求员工更高效使用 AI tokens，并加速自研模型的开发。 这一事件凸显了主要科技公司之间实际存在的 AI 算力容量限制，揭示了影响战略合作与内部开发的供应瓶颈。它强调了 GPU 资源竞争的加剧，以及 Meta 等公司投资自有 AI 基础设施的紧迫性。 Meta 自身没有云业务，正在大力自建数据中心，并承诺到 2028 年在美国投资 6000 亿美元。Google 近期与 SpaceX 签署了每月 9.2 亿美元的算力租赁协议，并在 4 月财报会上承认近期算力受限。Meta 已开始优先采用其新的 Muse Spark 模型，以减少对外部模型的依赖。

telegram · zaihuapd · 6月28日 07:38

**背景**: Gemini 是由 Google DeepMind 开发的一系列多模态大语言模型，是 LaMDA 和 PaLM 2 的继任者。AI tokens 是 AI 模型在训练和推理过程中处理的数据单元（如子词或字符），按 token 计费决定了生成式 AI 应用的成本。Meta 没有自营公有云业务，正在加紧建设自有 AI 算力基础设施，并开发 Muse Spark 等自研模型以减少对第三方的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gemini_(language_model)">Gemini (language model ) - Wikipedia</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-tokens-explained/">What Are AI Tokens? The Language and Currency Powering Modern AI</a></li>
<li><a href="https://www.aol.com/finance/meta-launches-muse-spark-ai-171109554.html">Meta launches Muse Spark AI model as part of its AI turnaround - AOL</a></li>

</ul>
</details>

**标签**: `#AI`, `#Gemini`, `#Meta`, `#Google`, `#compute`

---