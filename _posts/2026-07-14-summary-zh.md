---
layout: default
title: "Horizon Summary: 2026-07-14 (ZH)"
date: 2026-07-14
lang: zh
---

> 从 298 条内容中筛选出 27 条重要资讯。

---

1. [Cursor 零日漏洞：沉默六个月后全面披露](#item-1) ⭐️ 9.0/10
2. [PostgreSQL 的 Rust 重写版通过全部 4.6 万多项回归测试](#item-2) ⭐️ 9.0/10
3. [Ollama 扩展本地大语言模型支持，新增多种模型](#item-3) ⭐️ 9.0/10
4. [2026 年菲尔兹奖得主泄露，两位中国数学家上榜](#item-4) ⭐️ 9.0/10
5. [Bonsai 27B：可在手机上运行的 270 亿参数 AI 模型](#item-5) ⭐️ 8.0/10
6. [AI 代理加剧大型软件项目的协作问题](#item-6) ⭐️ 8.0/10
7. [如何阻止 Claude 过度使用特定短语](#item-7) ⭐️ 8.0/10
8. [我们是否将过多思考外包给了 AI？](#item-8) ⭐️ 8.0/10
9. [Linux 输入延迟实测：X11 vs Wayland、VRR 与 DXVK](#item-9) ⭐️ 8.0/10
10. [Lobste.rs 从 MariaDB 迁移到 SQLite，降低成本](#item-10) ⭐️ 8.0/10
11. [摩擦构建软件项目共享理解](#item-11) ⭐️ 8.0/10
12. [Manim：数学解释视频动画引擎](#item-12) ⭐️ 8.0/10
13. [HeyGen 推出 HyperFrames：面向 AI 智能体的开源 HTML 转视频工具](#item-13) ⭐️ 8.0/10
14. [Nushell：基于 Rust 的现代 Shell 逐渐流行](#item-14) ⭐️ 8.0/10
15. [InfluxDB 3 Core：基于 Apache Arrow 的开源时序数据库](#item-15) ⭐️ 8.0/10
16. [Plano：面向智能体应用的 AI 原生代理](#item-16) ⭐️ 8.0/10
17. [三星 Flex Titanium：钛合金强化折叠屏](#item-17) ⭐️ 8.0/10
18. [IBM 警告 AI 基建热潮挤压企业软件支出](#item-18) ⭐️ 8.0/10
19. [DeepSeek 寻求新一轮融资，估值达 710 亿美元](#item-19) ⭐️ 8.0/10
20. [阶跃星辰发布全球首款 AI 智能体手机与操作系统](#item-20) ⭐️ 8.0/10
21. [新 LLM 协作基准测试显示巨大差距](#item-21) ⭐️ 8.0/10
22. [Cloudflare 推出 Precursor，持续监控鼠标轨迹检测 AI 机器人](#item-22) ⭐️ 8.0/10
23. [DeepSeek 首轮融资超 74 亿美元，采用有限合伙架构维持创始人控制](#item-23) ⭐️ 8.0/10
24. [高德发布 ABot-WorldStudio，内置‘时空任意门’生成 3D 世界](#item-24) ⭐️ 8.0/10
25. [Telegram 的 t.me 域名被注册局冻结](#item-25) ⭐️ 8.0/10
26. [DeepMind CEO 呼吁美国主导全球 AI 监管机构](#item-26) ⭐️ 8.0/10
27. [Anthropic 推出 Claude for Teachers，面向美国 K-12 教师](#item-27) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cursor 零日漏洞：沉默六个月后全面披露](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) ⭐️ 9.0/10

MindGard 发现 Cursor 编辑器存在一个严重零日漏洞，可通过项目文件夹中的恶意 git.exe 执行任意代码；在报告超过六个月未获解决后，他们公布了完整细节。 该漏洞威胁到一款流行 AI 编程助手的用户，尤其是 Windows 用户；六个月未能修复暴露了厂商安全实践和负责任的披露流程的有效性问题。 该利用方式要求攻击者将恶意 git.exe 放入用户项目文件夹，Cursor 会在无提示下执行。漏洞于 2025 年 12 月 15 日通过 HackerOne 报告，最初标记为信息性，后经复现，但从未修复。

hackernews · Synthetic7346 · 7月14日 17:58 · [社区讨论](https://news.ycombinator.com/item?id=48910676)

**背景**: 零日漏洞是指厂商未知、尚无补丁的安全缺陷。全面披露是指在厂商未能修复漏洞后公开所有细节的做法，旨在施压并告知用户。Cursor 编辑器是一款 AI 驱动的代码编辑器，能够代表用户执行命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Full_disclosure_(computer_security)">Full disclosure (computer security) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：有人认为该漏洞被夸大，因为需要系统上已有恶意 exe；另一些人强调不应在无提示下执行不受信任的二进制文件，尤其是 AI 代理。许多人对 Cursor 超过六个月无回应表示失望。

**标签**: `#security`, `#vulnerability`, `#cursor`, `#full disclosure`, `#0day`

---

<a id="item-2"></a>
## [PostgreSQL 的 Rust 重写版通过全部 4.6 万多项回归测试](https://github.com/malisper/pgrust) ⭐️ 9.0/10

pgrust 项目，即用 Rust 完全重写 PostgreSQL 的项目，已通过超过 46,000 项回归测试，输出与 Postgres 18.3 完全一致，实现了完全兼容。该项目现已提供 Docker 镜像和 WebAssembly 演示。 这一里程碑表明，基于 Rust 的数据库能够实现与 PostgreSQL 的二进制级别兼容，为更安全、更高性能的替代方案打开了大门。它可能降低利用 Rust 的内存安全性和 AI 辅助编程进行深层服务器变更实验的门槛。 pgrust 与 Postgres 18.3 磁盘兼容，并能从现有数据目录启动。据报道，即将推出的版本在事务性工作负载上比 Postgres 快 50%，在分析性工作负载上快约 300 倍。

rss · GitHub Trending - Rust Daily · 7月14日 01:40

**背景**: PostgreSQL 是一款广泛使用的开源关系型数据库管理系统，最初用 C 语言编写。将核心数据库组件用 Rust（一种注重安全性和并发的系统编程语言）重写，已成为一种日益增长的趋势，旨在保持兼容性的同时提高可靠性和性能。

**标签**: `#Rust`, `#PostgreSQL`, `#database`, `#systems programming`, `#rewrite`

---

<a id="item-3"></a>
## [Ollama 扩展本地大语言模型支持，新增多种模型](https://github.com/ollama/ollama) ⭐️ 9.0/10

Ollama 已新增对 Kimi-K2.6、GLM-5.1、MiniMax、DeepSeek、Qwen、Gemma 等模型的支持，允许用户本地运行最先进的大语言模型。 这扩展了本地运行大语言模型的生态系统，为开发者和研究人员提供了更多隐私、定制化和离线使用的选择，同时减少了对云端 API 的依赖。 Ollama 提供 REST API、Python 和 JavaScript 库，以及 macOS、Windows、Linux 和 Docker 的一键安装，简化了模型管理和集成。

rss · GitHub Trending - Go Daily · 7月14日 01:35

**背景**: Ollama 是一个开源平台，允许用户在本地硬件上运行大语言模型。它利用 llama.cpp 作为后端实现高效推理，并支持包括中国人工智能公司如 Moonshot AI（Kimi）和 Z.ai（GLM）在内的多种模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K2.6">Kimi K2.6</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.1">GLM-5.1</a></li>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_Group">MiniMax Group - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#Large Language Models`, `#Open Source`, `#Local LLM`, `#Developer Tools`

---

<a id="item-4"></a>
## [2026 年菲尔兹奖得主泄露，两位中国数学家上榜](https://www.36kr.com/p/3895047930100996) ⭐️ 9.0/10

ICM 2026 官网源代码意外泄露了菲尔兹奖得主名单，中国数学家邓煜和王虹名列其中。 如果确认，王虹将成为首位获得菲尔兹奖的中国女性，也是史上第三位女性得主；邓宇也将成为第一位中国籍获奖者，这标志着中国数学的历史性突破。 泄露发生于 2026 年 7 月 13 日，藏在 ICM 2026 官网日程的源代码中，现已被修复。邓煜和王虹均为北京大学数学科学学院 2007 级校友。

rss · 36氪 - 24小时热榜 · 7月14日 08:53

**背景**: 菲尔兹奖是数学界最高荣誉，每四年颁发一次，授予 40 岁以下的杰出数学家。王虹据称攻克了百年难题挂谷猜想（Kakeya 猜想），涉及几何测度论；邓煜则解决了希尔伯特第六问题，旨在为物理学建立公理体系。此前仅有丘成桐和陶哲轩两位华人获奖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Congress_of_Mathematicians">International Congress of Mathematicians - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kakeya_conjecture">Kakeya conjecture</a></li>
<li><a href="https://www.mathunion.org/icm/icm-2026">ICM 2026 - International Congress of Mathematicians in ...</a></li>

</ul>
</details>

**标签**: `#Fields Medal`, `#Mathematics`, `#Chinese Mathematicians`, `#Leak`, `#Awards`

---

<a id="item-5"></a>
## [Bonsai 27B：可在手机上运行的 270 亿参数 AI 模型](https://prismml.com/news/bonsai-27b) ⭐️ 8.0/10

PrismML 发布了 Bonsai 27B，这是基于 Qwen 3.6 27B 的量化版本，在保留 90% 智能水平的同时仅占用 12GB 内存，可在手机上原生运行。 这一突破使得先进的 AI 模型能够在消费级设备上运行，且智能损失很小，可能改变设备端 AI 应用的格局。 该模型通过量化技术将体积从约 50GB 压缩至约 4GB（高质量版本约 12GB），在工具调用和视觉任务中表现良好。

hackernews · xenova · 7月14日 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48910545)

**背景**: 量化技术通过降低模型权重的精度（例如从 16 位降至 4 位），大幅缩小模型体积而精度损失很小。Bonsai 27B 基于阿里云的 Qwen 3.6 27B 模型。设备端 AI 推理可实现隐私保护和离线使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_compression">Model compression - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2411.02530v1">A Comprehensive Study on Quantization Techniques for Large ...</a></li>

</ul>
</details>

**社区讨论**: 评论区将 Bonsai 27B 与 Google 的 Gemma 4 4 位 QAT 版本进行比较，用户质疑其工具调用性能，并指出演示中的食谱计算错误。部分用户反映在 LM Studio 上运行模型时遇到问题。

**标签**: `#AI`, `#model compression`, `#quantization`, `#on-device ML`

---

<a id="item-6"></a>
## [AI 代理加剧大型软件项目的协作问题](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/) ⭐️ 8.0/10

Armin Ronacher 的随笔《不断升高的塔》指出，尽管 AI 代理提升了个人编码速度，但它们加剧了大型软件项目中的协作难题，导致共同理解的丧失却不会立刻失败。 这一分析揭示了 AI 辅助编程一个常被忽视的关键代价：它可能悄无声息地增加软件复杂性和脆弱性，威胁大型代码库的可持续性。 该随笔将这种现象与 Lisp 诅咒相类比——强大工具反而阻碍协作；与圣经中的巴别塔不同，在共同语言丧失后建造仍在继续，使得问题不易被察觉。

hackernews · cdrnsf · 7月14日 16:57 · [社区讨论](https://news.ycombinator.com/item?id=48909785)

**背景**: Lisp 诅咒由 Rudolf Winestock 提出，指 Lisp 的强大能力让开发者独自完成大量工作，从而避免协作，导致库碎片化和文档匮乏。在大型软件项目中，生产力不仅受限于代码产出，更取决于团队成员对系统的共同理解。AI 代理快速生成代码的能力可能加剧这一差距，使个体无需与他人协商就能构建，增加了集成失败的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="http://www.winestockwebdesign.com/Essays/Lisp_Curse.html">The Lisp Curse - Winestock Webdesign</a></li>
<li><a href="https://www.freshcodeit.com/blog/myths-of-lisp-curse">What is the Curse of Lisp: Challenges and Opportunities</a></li>

</ul>
</details>

**社区讨论**: 评论区普遍认同该随笔的观点。有评论者用俄罗斯方块类比可组合性，另一位直接将其与 Lisp 诅咒联系起来，还有一位赞赏了问题并非立即失败而是隐蔽性的细腻观察。

**标签**: `#software engineering`, `#AI-assisted programming`, `#composability`, `#coordination`, `#software complexity`

---

<a id="item-7"></a>
## [如何阻止 Claude 过度使用特定短语](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing) ⭐️ 8.0/10

一篇博客文章详细介绍了如何让 Claude 停止过度使用“load-bearing”等短语，引发了关于大语言模型输出偏见的社区讨论。 该话题获得 405 分和 468 条评论，凸显了模型癖好在规模化输出数百万次后会变得格外刺眼。 文章建议通过全局 CLAUDE.md 配置文件来缓解不想要的措辞，社区成员还追踪了其他固化词汇，如“projection”、“strand”和“frontier”。

hackernews · shintoist · 7月14日 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48905248)

**背景**: Claude 是由 Anthropic 开发的大语言模型，以其宪法式 AI 方法著称。大语言模型可能产生输出偏见，常因训练数据或微调而过度使用某些词汇或短语。当规模化部署时，这些偏见会被放大并更加引人注目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://claude.com/">Claude</a></li>
<li><a href="https://claude.com/product/overview">The AI for Problem Solvers | Claude by Anthropic</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了复杂感受：有人认为在直接编码交互中 Claude 的习惯用语不太烦人，但在看似人类写作的散文中则显得突兀。另一些人指出，大语言模型偏见的可扩展性使其比个人怪癖更显眼。还有人分享了通过全局 CLAUDE.md 修改行为的解决方案。

**标签**: `#LLM`, `#AI behavior`, `#Claude`, `#tone`, `#community discussion`

---

<a id="item-8"></a>
## [我们是否将过多思考外包给了 AI？](https://www.artfish.ai/p/offloading-thinking-to-ai) ⭐️ 8.0/10

一篇文章探讨了过度依赖 AI 进行认知任务是否正在削弱人类的批判性思维，引发了社区关于风险与权衡的讨论。 随着 AI 工具变得无处不在，批判性思维的削弱可能对技能发展产生长期影响，尤其是对初级专业人士和更广泛的劳动力。 讨论中提到了真实案例，例如初级开发者无法解释 AI 生成的代码，以及担忧未来可能强制要求 AI 审批决策。

hackernews · yenniejun111 · 7月14日 15:18 · [社区讨论](https://news.ycombinator.com/item?id=48908178)

**背景**: 认知卸载指利用外部工具减少认知负担，这一概念在心理学中已有研究。历史例子包括计算器和互联网，但 AI 现在处理更高层次的推理，引发了关于更深层依赖和失去理解的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cognitive_offloading">Cognitive offloading</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1364661316300985">Cognitive Offloading - ScienceDirect</a></li>
<li><a href="https://www.computer.org/publications/tech-news/trends/cognitive-offloading">Cognitive Offloading: How AI is Quietly Eroding Our Critical ...</a></li>

</ul>
</details>

**社区讨论**: 社区意见不一：有人认为重度使用 AI 仍能保持用户主导，另一些人则指出有人盲目信任 AI 而不理解结果，并担心未来可能强制服从 AI。

**标签**: `#AI ethics`, `#critical thinking`, `#cognitive offloading`, `#LLM impact`, `#software engineering`

---

<a id="item-9"></a>
## [Linux 输入延迟实测：X11 vs Wayland、VRR 与 DXVK](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/) ⭐️ 8.0/10

一项详尽的实证研究测量了 Linux 显示服务器及相关技术的输入延迟，发现原生 Wayland 游戏延迟最低，而 XWayland 会引入约 3 毫秒的开销。 这一分析帮助 Linux 游戏玩家和开发者就显示服务器及配置做出明智选择，并展示了 Linux 生态系统能够通过公开测试实现自我改进。 测试使用 500Hz 显示器进行精确计时；XWayland 的延迟高于原生 Wayland，而 VRR（可变刷新率）未显著增加延迟。DXVK 作为 DirectX 到 Vulkan 的转换层，性能与原生 D3D 相当。

hackernews · hoechst · 7月14日 16:36 · [社区讨论](https://news.ycombinator.com/item?id=48909424)

**背景**: X11 和 Wayland 是 Linux 上的显示服务器：X11 是传统方案，Wayland 是现代方案。VRR 将显示器刷新率与 GPU 帧率同步。DXVK 将 Direct3D 调用转换为 Vulkan，用于在 Linux 上运行 Windows 游戏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Variable_refresh_rate">Variable refresh rate - Wikipedia</a></li>
<li><a href="https://github.com/doitsujin/dxvk">GitHub - doitsujin/dxvk: Vulkan-based implementation of D3D8 ...</a></li>

</ul>
</details>

**社区讨论**: 评论者赞赏了这次测量的详尽性和重要性，但有人指出 500Hz 显示器可能掩盖了帧时间问题。评论中也对 Hyprland（Wayland 合成器）表现出好奇，并推测 XWayland 的延迟解释了人们认为 Wayland 慢的印象。

**标签**: `#Linux`, `#input latency`, `#Wayland`, `#X11`, `#gaming`

---

<a id="item-10"></a>
## [Lobste.rs 从 MariaDB 迁移到 SQLite，降低成本](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything) ⭐️ 8.0/10

Lobste.rs 已完成从 MariaDB 到 SQLite 的迁移，降低了 CPU 和内存使用量，网站响应更快，并将 VPS 成本减半。这一变更现被视为永久架构。 此次迁移证明了 SQLite 在处理中等流量的 Rails 生产应用中的可行性，挑战了大型数据库需要独立数据库服务器的假设。它提供了一个降低成本、简化运维的真实案例。 Lobsters Rails 应用现在运行在单个 VPS 上，主 SQLite 数据库文件约 3.8GB，另有 1.1GB 缓存数据库、218MB 队列数据库和 555MB 的 rack_attack 数据库。迁移的拉取请求添加了 735 行代码，删除了 593 行，涉及 30 个提交和 188 个文件。

rss · Simon Willison · 7月14日 19:44

**背景**: SQLite 是一种轻量级、嵌入式 SQL 数据库引擎，将数据存储在单个文件中，无需单独的服务器进程。它常用于移动应用和小型应用，但最近的改进使其可用于生产 Web 服务。Lobste.rs 是一个类似于 Hacker News 的社区驱动链接聚合网站，最初使用 MariaDB（MySQL 的分支），自 2018 年起一直计划迁移。

**标签**: `#SQLite`, `#Rails`, `#database migration`, `#web development`, `#lobste.rs`

---

<a id="item-11"></a>
## [摩擦构建软件项目共享理解](https://simonwillison.net/2026/Jul/14/armin-ronacher/#atom-everything) ⭐️ 8.0/10

Armin Ronacher 指出，软件项目的共享语言是通过代码审查、对话和摩擦建立的，而 AI 代理可能绕过这一过程，导致开发者之间深层理解的丧失。 这一见解揭示了 AI 编程代理日益普及中的一个关键风险：它们可能以牺牲团队层面的连贯性和共享心智模型为代价来提高个人生产力，而这些模型对于长期维护复杂系统至关重要。 Ronacher 特别指出，摩擦——例如需要阅读他人代码、提问以及跨团队协调——通过传递理解来同步人员，而这种缓慢并非全部都是浪费。

rss · Simon Willison · 7月14日 18:04

**背景**: 在软件工程中，不变式（invariant）是指在程序执行期间必须始终成立的条件，例如确保对象一致性的类不变式。隐性知识（tacit knowledge）是指团队成员通过协作和摩擦积累的、未被明述的经验性理解。Ronacher 的论点将这些概念联系起来，指出代码审查和对话中的摩擦正是团队内部关于不变式和系统边界的隐性知识得以共享和维护的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Invariant-based_programming">Invariant-based programming - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0950584913000591">Acquiring and sharing tacit knowledge in software development ...</a></li>

</ul>
</details>

**标签**: `#software engineering`, `#shared understanding`, `#AI agents`, `#software development practices`, `#code review`

---

<a id="item-12"></a>
## [Manim：数学解释视频动画引擎](https://github.com/3b1b/manim) ⭐️ 8.0/10

Manim 是由 Grant Sanderson（3Blue1Brown）创建的动画引擎，用于以编程方式生成数学解释视频。该 GitHub 仓库包含原始版本，同时还有一个社区维护的分支版本，旨在提高稳定性和贡献响应速度。 Manim 已成为数学教育和科学传播的关键工具，使创作者能够生成以前难以制作的高质量、精确动画。其开源特性和活跃社区促进了广泛采用，激励许多人创建自己的教育内容。 主要有两个版本：原始的 3b1b/manim（通过 pip 安装为 'manimgl'）和 2020 年分叉的社区版（ManimCommunity/manim）。Manim 需要 Python 3.7+、FFmpeg、OpenGL，以及可选的 LaTeX 和 Pango。

rss · GitHub Trending - Python Daily · 7月14日 01:39

**背景**: Manim 是 Mathematical Animation Engine（数学动画引擎）的缩写。它最初是为了制作热门 YouTube 频道 3Blue1Brown 中的动画而开发的，该频道通过直观的视觉解释数学概念。该工具允许用户编写 Python 脚本定义场景和对象，然后将其渲染为动画。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/3b1b/manim">GitHub - 3b1b/manim: Animation engine for explanatory math ...</a></li>
<li><a href="https://www.manim.community/">Manim Community</a></li>
<li><a href="https://www.3blue1brown.com/lessons/manim-demo/">How I animate 3Blue1Brown | A Manim demo with B... | 3Blue1Brown</a></li>

</ul>
</details>

**标签**: `#animation`, `#math`, `#python`, `#education`, `#open-source`

---

<a id="item-13"></a>
## [HeyGen 推出 HyperFrames：面向 AI 智能体的开源 HTML 转视频工具](https://github.com/heygen-com/hyperframes) ⭐️ 8.0/10

HeyGen 将 HyperFrames 开源，这是一个将 HTML、CSS 和动画转换为确定性 MP4 视频的框架，专为 AI 编码智能体设计。它包含 20 个技能，可指导智能体根据自然语言提示规划、编写和渲染视频。 这降低了 AI 智能体以编程方式生成动态品牌视频的门槛，使得营销、入职培训、社交媒体等工作流中的自动视频制作成为可能。作为 Remotion 的开源替代方案且无按渲染收费，它可能加速基于 HTML 的视频生成的普及。 HyperFrames 使用无头 Chrome 和 FFmpeg 进行渲染，支持基于适配器的动画（GSAP、CSS、Lottie、Three.js 等），并要求 Node.js 版本 22 或更高。它采用 Apache 2.0 许可，且组合文件无需构建步骤。

rss · GitHub Trending - TypeScript Daily · 7月14日 01:41

**背景**: 传统视频创作常需要手动编辑或复杂编程。HyperFrames 建立在将 Web 内容渲染为视频的概念之上，类似于 Remotion 但专注于 AI 智能体工作流。它允许开发者使用熟悉的 HTML/CSS 定义视频，从而对 Web 开发者更加友好。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/heygen-com/hyperframes">GitHub - heygen-com/hyperframes: Write HTML. Render video. Built for agents. · GitHub</a></li>
<li><a href="https://hyperframes.heygen.com/introduction">Introduction - HyperFrames - HeyGen</a></li>
<li><a href="https://www.heygen.com/agent">AI Video Agent | Create and Automate Videos with AI | HeyGen</a></li>

</ul>
</details>

**标签**: `#video generation`, `#HTML`, `#open-source`, `#AI agents`, `#TypeScript`

---

<a id="item-14"></a>
## [Nushell：基于 Rust 的现代 Shell 逐渐流行](https://github.com/nushell/nushell) ⭐️ 8.0/10

Nushell 是一个用 Rust 编写的开源 shell，已达到最小可行产品阶段，许多开发者将其作为日常使用，它提供了结构化数据管道的处理方式。 Nushell 通过将数据视为结构化对象而非纯文本，代表了命令行界面设计的重大转变，为开发者和系统管理员提供了更强大、更直观的工作流程。 Nushell 支持传递结构化数据的管道，拥有插件系统，并能与现有 shell 命令集成。它可通过 Homebrew 和 winget 等包管理器安装，并内置帮助系统以及官方学习手册。

rss · GitHub Trending - Rust Daily · 7月14日 01:40

**背景**: 传统的 Unix shell（如 Bash 和 Zsh）将所有数据视为文本字符串，进行复杂操作时需要手动解析。Nushell 引入了类型化数据模型，命令对结构化值进行操作，从而减少错误并简化脚本编写。选择 Rust 语言是因为其高性能和内存安全性，这有助于 Nushell 的可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nushelle_de_Silva">Nushelle de Silva</a></li>

</ul>
</details>

**标签**: `#shell`, `#rust`, `#developer-tools`, `#nushell`

---

<a id="item-15"></a>
## [InfluxDB 3 Core：基于 Apache Arrow 的开源时序数据库](https://github.com/influxdata/influxdb) ⭐️ 8.0/10

InfluxData 发布了 InfluxDB 3 Core，这是一个基于 Apache Arrow、DataFusion 和 Parquet 构建、已正式可用的开源时序数据库，采用无磁盘架构，查询性能低于 10 毫秒。 此次发布标志着 InfluxDB 架构的重大转变，使其在实时分析和监控领域可与现代云原生数据库竞争，并为专有的 InfluxDB 3.0 Cloud 提供了免费的开源替代方案。 InfluxDB 3 Core 支持 SQL、InfluxQL 和 Flight SQL 进行查询，使用 Line Protocol 写入数据，并将数据以 Apache Parquet 格式存储于对象存储或本地磁盘，同时内置 Python 虚拟机以支持插件和触发器。

rss · GitHub Trending - Rust Daily · 7月14日 01:40

**背景**: Apache Arrow 是一种语言无关的列式内存格式，用于高效的数据交换。DataFusion 是一个用 Rust 编写的可扩展查询引擎，以 Arrow 作为其内存格式。Apache Parquet 是一种列式存储格式，针对压缩和分析查询进行了优化。InfluxDB 3 Core 结合这些技术，提供了高性能的时序数据处理能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Arrow">Apache Arrow</a></li>
<li><a href="https://datafusion.apache.org/">Apache DataFusion — Apache DataFusion documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Parquet">Apache Parquet</a></li>

</ul>
</details>

**标签**: `#time series database`, `#influxdb`, `#open source`, `#apache arrow`, `#datafusion`

---

<a id="item-16"></a>
## [Plano：面向智能体应用的 AI 原生代理](https://github.com/katanemo/plano) ⭐️ 8.0/10

Katanemo 发布了 Plano，这是一个用于智能体应用的开源 AI 原生代理和数据平面，提供内置的编排、安全、可观测性和智能 LLM 路由。它使用 Rust 构建，并基于 Envoy 实现高性能。 Plano 通过集中路由、安全和可观测性等通用基础设施，简化了智能体 AI 系统的生产部署，让开发者专注于智能体逻辑。随着企业从演示转向生产，它填补了智能体 AI 栈中的关键空白。 Plano 支持任何语言或 AI 框架，提供零代码的 Agentic Signals 和 OTEL 跟踪捕获，并包含用于审核和内存钩子的 Filter Chains。它由 Envoy 的核心贡献者基于 Envoy 构建，并得到 LLM 研究的支持。

rss · GitHub Trending - Rust Daily · 7月14日 01:40

**背景**: 智能体 AI 指的是能够自主行动以实现目标的系统，通常结合 LLM、多智能体系统和工作流编排。AI 代理充当 AI 工具与外部系统之间的流量管理器，处理路由、监控和控制。数据平面是网络中处理和转发数据的部分，而控制平面则负责配置。Plano 将这些概念统一应用于智能体应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/katanemo/plano">GitHub - katanemo/plano: Plano is an AI-native proxy and data ...</a></li>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2026/02/24/what-is-an-ai-proxy-how-it-works-and-key-use-cases/">What Is An AI Proxy? How It Works And Key Use Cases - Forbes</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**标签**: `#AI proxy`, `#agentic apps`, `#Rust`, `#LLM routing`, `#observability`

---

<a id="item-17"></a>
## [三星 Flex Titanium：钛合金强化折叠屏](https://www.ithome.com/0/976/778.htm) ⭐️ 8.0/10

三星发布了 Flex Titanium 技术，利用钛合金薄膜和钛板提升折叠屏的耐用性、减少折痕并改善观看体验。该技术将首次应用于下一代 Galaxy Z Fold 设备。 这项创新直接解决了折叠屏手机的两个关键痛点：屏幕折痕和耐用性问题。通过利用钛的强度，三星可能为折叠屏显示质量树立新标准，并加速主流市场采用。 位于 OLED 面板下方的钛合金薄膜的机械刚度是聚合物薄膜的 20 倍，厚度仅约为人类头发直径的三分之一；钛板则通过精密的微图案孔设计来平衡柔韧性与支撑力。显示屏还采用了高分辨率架构和新一代有机材料，以提升画质和能效。

rss · IT之家 · 7月14日 23:37

**背景**: 折叠屏手机依赖于能够反复弯曲的柔性屏幕，但这会导致折痕明显，并引发长期耐用性的担忧。钛以其高强度和高韧性而闻名，但难以加工成薄而柔韧的结构。三星的解决方案使用了两种钛基部件——薄膜和板——来强化显示屏，同时保持纤薄和柔韧性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.samsung.com/global/samsung-introduces-flex-titanium-technology-to-advance-foldable-displays">Samsung Introduces Flex Titanium Technology To Advance ...</a></li>
<li><a href="https://www.pcmag.com/news/samsung-teases-new-screen-substrate-for-its-next-foldable-titanium">Samsung Teases New Screen Substrate for Its Next Foldable ...</a></li>
<li><a href="https://www.androidauthority.com/samsung-flex-titanium-3687554/">Samsung details the secrets of foldable screen Flex Titanium tech</a></li>

</ul>
</details>

**标签**: `#Foldable Phones`, `#Titanium`, `#Display Technology`, `#Samsung`, `#Galaxy Z Fold`

---

<a id="item-18"></a>
## [IBM 警告 AI 基建热潮挤压企业软件支出](https://www.ithome.com/0/976/722.htm) ⭐️ 8.0/10

IBM 警告企业正将资本支出从软件转向 AI 基础设施，导致 IBM 股价暴跌约 20%，并拖累其他软件股。该公司预计第二季度营收约 172 亿美元，低于分析师预期的 178.6 亿美元。 这标志着 AI 基础设施热潮正在蚕食企业软件预算，对软件行业增长构成威胁。长期转变可能从根本上改变科技行业的支出格局。 IBM 首席执行官 Arvind Krishna 表示，客户将资本支出转向服务器、存储设备和内存，以便在涨价前锁定供应。公司承认未能快速调整，丢失了大型订单。调整后每股收益预计为 2.93 美元，低于市场预期的 3.02 美元。

rss · IT之家 · 7月14日 12:36

**背景**: 企业软件支出历来是科技公司稳定的收入来源。然而，生成式 AI 的崛起推动了对数据中心、GPU 和网络设备的大量投资，资金从传统软件许可中分流。IBM 的警告凸显了 AI 基础设施与软件预算之间的紧张关系。

**标签**: `#AI`, `#infrastructure`, `#enterprise software`, `#spending`, `#IBM`

---

<a id="item-19"></a>
## [DeepSeek 寻求新一轮融资，估值达 710 亿美元](https://www.ithome.com/0/976/713.htm) ⭐️ 8.0/10

据报道，DeepSeek 正在与新投资者就新一轮融资进行初步谈判，投前估值达 710 亿美元，距离其首次外部融资仅过去数月。 这一估值体现了 DeepSeek 在 AI 领域的快速增长和战略重要性，其计划将资金用于大规模数据中心和 AI 芯片采购，可能重塑行业竞争格局。 上一轮融资于 2025 年 5 月完成，筹集约 70 亿美元资金，投后估值达 520 亿美元，其中创始人梁文峰出资约 30 亿美元。

rss · IT之家 · 7月14日 11:46

**背景**: DeepSeek 是一家专注于大语言模型的中国 AI 初创公司。融资轮次的快速更迭凸显了 AI 基础设施对资金的巨大需求，企业需投入数十亿美元用于算力和芯片。

**标签**: `#AI funding`, `#DeepSeek`, `#startup`, `#data center`, `#AI chips`

---

<a id="item-20"></a>
## [阶跃星辰发布全球首款 AI 智能体手机与操作系统](https://www.36kr.com/p/3894202301250819) ⭐️ 8.0/10

阶跃星辰发布了全球首个智能体原生操作系统 Step AOS、个人智能体 Amoo，以及大模型原生终端品牌 STEPX 的首款手机 STEPX Neo，该手机已与支付宝、美团、滴滴等主流应用达成生态合作。 这标志着从基于 App 到基于意图的手机交互范式转变，可能重新定义移动设备的角色，并加速 AI 智能体在日常生活中的普及。 Step AOS 具备双域三步记忆结构（用户域和智能体域）、端云协同处理任务的能力，并且所有操作可审计、可撤回。阶跃星辰计划在 100 天内与用户共同打造智能体生态。

rss · 36氪 - 24小时热榜 · 7月14日 01:17

**背景**: AI 智能体是一种自主软件实体，能代表用户理解、规划并执行任务。智能体原生操作系统从头构建，将 AI 智能体作为一等公民来托管和管理，不同于为人类交互设计的传统操作系统。端云协同意味着简单任务在设备端运行以获得低延迟，而复杂任务则卸载到云端进行深度推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zglg.work/en/ai/news/2026-07-13-step-launches-world-s-first-agent-native-os-rebuilt-from-scratch-for-ai-agent">Step Launches World's First Agent-Native OS, Rebuilt from ...</a></li>
<li><a href="https://www.ai-market-watch.com/news/step-ai-launches-worlds-first-agentic-native-os-step-aos-and-personal-ai-agent-a-3w5kon">Step AI unveils world's first agentic-native OS, Step AOS ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3894202301250819">World's First AI Agent Smartphone Launch: Seamlessly ...</a></li>

</ul>
</details>

**标签**: `#AI agent`, `#smartphone`, `#operating system`, `#Stepfun`, `#Chinese tech`

---

<a id="item-21"></a>
## [新 LLM 协作基准测试显示巨大差距](https://www.reddit.com/r/MachineLearning/comments/1uwc6ni/new_llm_coordination_benchmark_benchmarking/) ⭐️ 8.0/10

研究人员推出了 ALM 基准测试，用于评估 LLM 在开放式多智能体协作任务中的表现；他们发现，大多数模型平均仅能达到约 6%的归一化回报，但 Gemini 3.1 Pro 在最难设置下的表现与经过训练的 MARL 智能体相当。 这一基准测试表明，协作是独立于个体任务能力的瓶颈，而 Gemini 3.1 Pro 的惊人成功表明，高级推理模型可以弥合与专门 MARL 算法之间的差距，从而可能实现更强大的多智能体 AI 系统。 该基准测试名为 ALM，涉及智能体在长期开放式世界中探索、通信、交易资源、制作工具、建造结构和对抗怪物；消融研究发现通信是最具影响力的因素。

reddit · r/MachineLearning · /u/ktessera · 7月14日 15:37

**背景**: 多智能体强化学习（MARL）是强化学习的一个子领域，研究多个学习智能体在共享环境中共存。传统的单智能体任务不同于多智能体协作，因为智能体必须通信并推断他人的意图。ALM 基准测试提供了一个具有挑战性的测试平台，用于评估 LLM 是否能在没有显式训练的情况下处理此类协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning">Multi-agent reinforcement learning - Wikipedia</a></li>
<li><a href="https://deepmind.google/models/gemini/pro/">Gemini 3.1 Pro - Google DeepMind</a></li>

</ul>
</details>

**标签**: `#LLM`, `#benchmark`, `#multi-agent`, `#coordination`, `#AI research`

---

<a id="item-22"></a>
## [Cloudflare 推出 Precursor，持续监控鼠标轨迹检测 AI 机器人](https://blog.cloudflare.com/introducing-precursor/) ⭐️ 8.0/10

Cloudflare 发布了 Precursor，这是一个持续行为验证引擎，在整个用户会话中监控鼠标轨迹、键盘节奏等信号，以区分真人与机器人或 AI 代理。 这解决了日益增长的 AI 机器人问题，它们可以绕过验证码等单点挑战，通过在整个用户旅程中提供持续验证，增强网络安全而不影响用户体验。 Precursor 是一个客户端 JavaScript，动态收集行为信号，并与 Cloudflare 的 Bot Management 配合使用；目前面向企业版 Bot Management 用户免费测试，正式版计划今年晚些时候上线。

telegram · zaihuapd · 7月14日 09:44

**背景**: 传统的机器人检测使用验证码或 Turnstile 等单点挑战，但高级 AI 机器人可以短暂模仿人类行为。Precursor 持续分析人类细微的生理特征，如鼠标自然弧线和微小延迟，这些机器难以伪造，从而提供整个会话的验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-precursor/">Introducing Precursor: detecting agentic behavior with ...</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-challenges/precursor/">Precursor · Cloudflare challenges docs</a></li>
<li><a href="https://securityboulevard.com/2026/07/cloudflare-precursor-extends-bot-detection-beyond-browser-checks/">Cloudflare Precursor Extends Bot Detection Beyond Browser ...</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#Bot Detection`, `#Security`, `#Behavior Analysis`, `#AI Agents`

---

<a id="item-23"></a>
## [DeepSeek 首轮融资超 74 亿美元，采用有限合伙架构维持创始人控制](https://t.me/zaihuapd/42557) ⭐️ 8.0/10

DeepSeek 完成了首轮融资，筹资逾 500 亿元人民币（约 74 亿美元），采用有限合伙架构，投资者需将资金投入由 CEO 梁文锋管理的有限合伙企业，而非直接投资 DeepSeek 本身，并接受五年锁定期且不享有表决权。 这一巨额融资轮凸显了业界对 DeepSeek 作为领先 AI 公司的强烈信心，同时这种非常规架构为中国初创企业在获得大额资本时保持创始人控制权开创了先例。 创始人梁文锋在本轮个人投资 200 亿元。腾讯考虑投资 100 亿元，宁德时代计划投资 50 亿元，可能成为最大的外部投资者。

telegram · zaihuapd · 7月14日 11:06

**背景**: 有限合伙（LP）结构将管理权（普通合伙人）与被动投资者（有限合伙人）分离，后者出资但无管理控制权。这种结构使创始人在筹集外部资金时能保留决策权，类似于一些科技公司使用的双重股权结构。DeepSeek 的做法进一步限制了投资者权利，要求五年锁定期且无表决权，确保创始人控制权不受影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://corporatefinanceinstitute.com/resources/management/limited-partnership/">Limited Partnership - Overview, Characteristics, Examples</a></li>
<li><a href="https://www.investopedia.com/terms/l/limitedpartnership.asp">Limited Partnership (LP): What It Is, Pros and Cons, How to ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#DeepSeek`, `#startup`

---

<a id="item-24"></a>
## [高德发布 ABot-WorldStudio，内置‘时空任意门’生成 3D 世界](https://www.ithome.com/0/976/538.htm) ⭐️ 8.0/10

阿里巴巴旗下高德正式发布通用世界模型工坊 ABot-WorldStudio，用户输入文字或图片即可生成可交互的 3D 世界。该工坊内置‘时空任意门’功能，可穿梭于不同 3D 场景，并支持单张 RTX 5090 上长时间本地推理，连续运行超过 1 小时无质量衰减。 该产品首次将交互式视频生成与 3DGS 场景生成统一，可在具身智能仿真训练、游戏影视创作及文旅教育等领域催生新应用。开源基础模型和本地化部署能力降低了研究者和开发者的使用门槛。 ABot-WorldStudio 原生输出具有真实几何结构和照片级视觉保真度的 3DGS 资产，可在单张 RTX 5090 上部署，推理时长无上限，官方实测连续推理超 1 小时无崩溃、无质量衰减。

telegram · zaihuapd · 7月14日 12:22

**背景**: 3D 高斯泼溅（3DGS）是一种用于实时辐射场渲染的光栅化技术，自 2023 年起因能从稀疏 2D 图像创建照片级 3D 场景而流行。世界模型是能模拟交互环境的 AI 系统，常用于机器人和内容生成。ABot-WorldStudio 将这两个领域结合在一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/976/538.htm">内置“任意门”，高德发布通用世界模型工坊 ABot-WorldStudio - IT之家</a></li>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#world model`, `#open source`, `#AI world`, `#interactive simulation`

---

<a id="item-25"></a>
## [Telegram 的 t.me 域名被注册局冻结](https://t.me/zaihuapd/42559) ⭐️ 8.0/10

Telegram 的短域名 t.me 于 7 月 13 日被注册局设置为 serverHold 状态，导致无法正常解析，影响短链接服务。 这一中断影响了数百万依赖 t.me 链接分享频道、群组和机器人的 Telegram 用户，并引发了对平台可靠性和中心化风险的担忧。 WHOIS 记录显示该域名目前受到 serverHold、禁止删除、禁止转移、禁止续费等多种限制，注册商为 GoDaddy，有效期至 2035 年 5 月。

telegram · zaihuapd · 7月14日 12:48

**背景**: 域名注册局是管理顶级域（如.com）的组织，而注册商则向公众销售域名。serverHold 是一种注册局级别的暂停状态，通常会导致域名无法解析，多因违反政策或法律行动所致。注册局而非注册商施加 serverHold，使其更严重且不常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/10717/46/why-was-my-domain-suspended-with-a-serverhold-or-clienthold-status/">Why was my domain suspended with a serverHold or clientHold ...</a></li>
<li><a href="https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en">EPP Status Codes | What Do They Mean, and Why Should I Know?</a></li>
<li><a href="https://www.godaddy.com/help/what-is-the-difference-between-a-registry-registrar-and-registrant-8039">What is the difference between a registry, registrar and ...</a></li>

</ul>
</details>

**标签**: `#Telegram`, `#domain`, `#DNS`, `#registry`, `#outage`

---

<a id="item-26"></a>
## [DeepMind CEO 呼吁美国主导全球 AI 监管机构](https://www.theverge.com/tech/965270/google-deepmind-demis-hassabis-global-ai-watchdog) ⭐️ 8.0/10

Google DeepMind 首席执行官 Demis Hassabis 提议成立一个由美国主导的全球 AI 监管机构，该机构将在部署前审查前沿 AI 模型，并在风险过高时协调全行业暂停部署，力争年底前开始运作。 随着 AI 系统日益强大，通用人工智能可能仅剩数年之遥，该提议解决了国际 AI 治理的紧迫需求，可能为 AI 安全与监管的全球合作树立先例。 Hassabis 表示，他已与特朗普政府、其他 AI 实验室及欧洲官员进行了数月沟通，反馈非常积极。拟议的机构将由独立专家和开源社区代表组成。

telegram · zaihuapd · 7月14日 14:29

**背景**: 通用人工智能（AGI）是一种假设性的 AI，能在几乎所有认知任务上达到或超越人类水平。前沿模型是当前最先进的 AI 模型，在大规模数据集上训练，提供最先进的性能。随着这些模型能力不断增强，对其潜在风险的担忧日益增加，促使人们呼吁进行监管。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#DeepMind`, `#Demis Hassabis`, `#global governance`, `#AI safety`

---

<a id="item-27"></a>
## [Anthropic 推出 Claude for Teachers，面向美国 K-12 教师](https://www.anthropic.com/news/claude-for-teachers) ⭐️ 8.0/10

2026 年 7 月 14 日，Anthropic 正式推出 Claude for Teachers，为经过验证的美国 K-12 教师免费提供高级 Claude 功能，包括与全美 50 个州学术标准对接的教学技能库。 该计划将 AI 融入 K-12 教育，具备严格的隐私保护和课程对齐能力，有望为数百万教师和学生革新备课流程与个性化学习体验。 教师数据默认不用于模型训练，学生信息受符合 FERPA 标准的数据处理协议保护。教师需在 2027 年 6 月 30 日前注册，可获得一整年免费访问。

telegram · zaihuapd · 7月14日 15:37

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，以其“宪法式 AI”方法提升伦理合规性而闻名。FERPA 是美国联邦法律，保护学生教育记录的隐私，赋予家长和符合条件的学生对信息披露的权利。此次发布旨在在兼顾隐私和课程需求的前提下，为教育工作者提供 AI 工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FERPA">FERPA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="http://studentprivacy.ed.gov/ferpa">FERPA | Protecting Student Privacy - ed</a></li>

</ul>
</details>

**标签**: `#AI`, `#Education`, `#Anthropic`, `#Claude`, `#EdTech`

---