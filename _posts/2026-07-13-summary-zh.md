---
layout: default
title: "Horizon Summary: 2026-07-13 (ZH)"
date: 2026-07-13
lang: zh
---

> 从 290 条内容中筛选出 26 条重要资讯。

---

1. [用 Rust 重写的 PostgreSQL 通过全部回归测试](#item-1) ⭐️ 9.0/10
2. [Cpp2Rust：C++到安全 Rust 的自动翻译](#item-2) ⭐️ 9.0/10
3. [Ruff：基于 Rust 的超快速 Python 代码检查与格式化工具](#item-3) ⭐️ 9.0/10
4. [无需 Xcode 图形界面即可构建和发布 Mac/iOS 应用](#item-4) ⭐️ 8.0/10
5. [Apple SpeechAnalyzer API 基准测试：比 Whisper 快但精度稍低](#item-5) ⭐️ 8.0/10
6. [Sega CD 版 Silpheed 技术深度解析](#item-6) ⭐️ 8.0/10
7. [三星健康应用威胁：退出 AI 训练则删除数据](#item-7) ⭐️ 8.0/10
8. [开放数据在气候.gov 关停后被保存](#item-8) ⭐️ 8.0/10
9. [Pydantic 发布 Pydantic AI 代理框架](#item-9) ⭐️ 8.0/10
10. [公共 API 仓库：精选免费 API 列表](#item-10) ⭐️ 8.0/10
11. [微软发布 TRELLIS.2，实现快速 3D 生成](#item-11) ⭐️ 8.0/10
12. [ComfyUI：一个强大的模块化图形界面，用于扩散模型](#item-12) ⭐️ 8.0/10
13. [谷歌发布开源 Gemini 命令行工具](#item-13) ⭐️ 8.0/10
14. [OpenAI 发布 Codex CLI：轻量级终端编码助手](#item-14) ⭐️ 8.0/10
15. [微软发布 MXC 沙箱代码执行系统](#item-15) ⭐️ 8.0/10
16. [Screenpipe：本地 AI 记忆记录器，赋能智能体](#item-16) ⭐️ 8.0/10
17. [InfluxDB 3 Core 开源时序数据库发布](#item-17) ⭐️ 8.0/10
18. [Tailscale 开源其核心 VPN 守护程序与 CLI](#item-18) ⭐️ 8.0/10
19. [Cloudflared：Cloudflare 隧道客户端](#item-19) ⭐️ 8.0/10
20. [Kubescape：开源 Kubernetes 安全平台](#item-20) ⭐️ 8.0/10
21. [SOPS：多功能的密钥管理工具现已纳入 CNCF](#item-21) ⭐️ 8.0/10
22. [Telegram 的 t.me 域名被注册局暂停](#item-22) ⭐️ 8.0/10
23. [CrashStealer 恶意软件瞄准 Mac，窃取 14 款密码管理器数据](#item-23) ⭐️ 8.0/10
24. [我国团队创造钙钛矿-有机叠层太阳能电池 28.04%效率纪录](#item-24) ⭐️ 8.0/10
25. [中国电动汽车电池新国标：热失控后 2 小时不起火](#item-25) ⭐️ 8.0/10
26. [GPUHedge 将无服务器 GPU 冷启动 p95 延迟从 117 秒降至 30 秒](#item-26) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [用 Rust 重写的 PostgreSQL 通过全部回归测试](https://github.com/malisper/pgrust) ⭐️ 9.0/10

开源项目 pgrust 达成里程碑，100%通过了 PostgreSQL 18.3 的回归测试，涵盖超过 46,000 个查询。该项目是用 Rust 完全重写 PostgreSQL，旨在实现兼容性和性能提升。 这证明了用 Rust 这类内存安全语言重写复杂生产级数据库的可行性，有望提升可靠性和安全性。如果 pgrust 成熟，它可能提供一种现代替代方案，具有更好的性能和更易扩展的特性。 pgrust 与 PostgreSQL 18.3 磁盘兼容，可直接从现有数据目录启动。一个尚未发布的新版本已展现出显著性能提升：事务负载比原生 PostgreSQL 快 50%，分析负载快约 300 倍。

rss · GitHub Trending - Daily · 7月13日 01:33

**背景**: PostgreSQL 是一款广泛使用的开源关系型数据库，拥有名为回归测试的大型测试套件，用于确保兼容性和正确性。pgrust 用 Rust 重写 PostgreSQL，Rust 是一种以内存安全和性能著称的系统编程语言，旨在保持 PostgreSQL 行为的同时，实现更深入的服务器改动和更好的性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now passing 100% of the Postgres regression tests · GitHub</a></li>
<li><a href="https://pgrust.com/">pgrust — postgres, rewritten in rust</a></li>

</ul>
</details>

**标签**: `#rust`, `#postgresql`, `#database`, `#reimplementation`, `#systems-programming`

---

<a id="item-2"></a>
## [Cpp2Rust：C++到安全 Rust 的自动翻译](https://github.com/Cpp2Rust/cpp2rust) ⭐️ 9.0/10

Cpp2Rust 是一款利用 Clang 的抽象语法树（AST）将 C++ 代码自动翻译为安全 Rust 的工具，其算法已在 PLDI 2026 上发表。 该工具可大幅降低将 C++ 代码库迁移到 Rust 的门槛，推动更安全的系统编程，并支持从 C++ 逐步迁移到 Rust。 Cpp2Rust 默认使用引用计数模型生成完全安全的 Rust 代码，同时提供不安全模式用于调试。它依赖运行时库 libcc2rs，通过 Ptr<T> 类型处理 C 指针语义。

rss · GitHub Trending - Rust Daily · 7月13日 01:41

**背景**: Clang 的 AST（抽象语法树）是 Clang 编译器用于分析和转换 C++ 源代码的树形表示。PLDI（编程语言设计与实现）是编程语言研究领域的顶级会议。引用计数是 Rust 中 Rc 和 Arc 类型使用的内存管理技术，用于在不使用垃圾回收的情况下共享所有权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://clang.llvm.org/docs/IntroductionToTheClangAST.html">Introduction to the Clang AST — Clang 23.0.0git documentation</a></li>
<li><a href="https://pldi26.sigplan.org/">Pldi 2026</a></li>
<li><a href="https://chomsky.hashnode.dev/rc-and-arc-in-rust-explained-for-beginners-part-1">Rust Rc vs Arc: Beginner's Guide</a></li>

</ul>
</details>

**标签**: `#C++`, `#Rust`, `#automatic translation`, `#safe programming`, `#PLDI`

---

<a id="item-3"></a>
## [Ruff：基于 Rust 的超快速 Python 代码检查与格式化工具](https://github.com/astral-sh/ruff) ⭐️ 9.0/10

Ruff 是一个用 Rust 编写的极速 Python 代码检查器和格式化工具，声称比 Flake8 和 Black 等现有工具快 10 到 100 倍。 Ruff 通过将代码检查、格式化和导入排序集成到一个高性能工具中，显著改善了 Python 开发工作流，减少了持续集成时间和开发者负担。 Ruff 提供与 Flake8、isort 和 Black 的无缝兼容，包含超过 900 条内置规则，并支持缓存和自动修复。

rss · GitHub Trending - Rust Daily · 7月13日 01:41

**背景**: Python 的代码检查和格式化工具有助于保证代码质量和风格，但可能速度较慢。Ruff 利用 Rust 的高性能实现了显著的提速，同时支持与 Flake8 和 Black 等流行工具相同的规则。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://docs.astral.sh/ruff/formatter/">The Ruff Formatter - Astral Docs</a></li>
<li><a href="https://docs.astral.sh/ruff/">Ruff - Astral Docs</a></li>

</ul>
</details>

**标签**: `#Python`, `#Rust`, `#linter`, `#formatter`, `#tooling`

---

<a id="item-4"></a>
## [无需 Xcode 图形界面即可构建和发布 Mac/iOS 应用](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 8.0/10

一篇详细指南展示了如何完全通过 xcodebuild 和 altool 等命令行工具构建、签名、公证并将 Mac 和 iOS 应用上传到 App Store Connect，完全绕过 Xcode 图形界面。 这种方法使得苹果平台开发能够实现完全自动化的 CI/CD 管道，减少了对 Xcode 臃肿图形界面的依赖，并为偏好终端工作流或工作于无头环境的开发者提供了便利。 该工作流使用 xcodebuild 进行构建，altool 进行上传，以及标准的签名和公证命令；它需要安装 Xcode 命令行工具并设置 App Store Connect API 密钥。

hackernews · speckx · 7月13日 18:22 · [社区讨论](https://news.ycombinator.com/item?id=48896665)

**背景**: Xcode 是苹果的集成开发环境，但许多核心任务（如编译、签名和上传）可以通过 Xcode 命令行工具包中包含的命令行工具执行。xcodebuild 和 altool 等工具允许开发者在不打开图形界面的情况下自动进行构建和发布，这对持续集成和部署特别有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.apple.com/library/archive/technotes/tn2339/_index.html">Technical Note TN2339: Building from the Command Line with Xcode...</a></li>
<li><a href="https://keith.github.io/xcode-man-pages/altool.1.html">altool (1) - GitHub Pages</a></li>
<li><a href="https://github.com/fastlane/fastlane">GitHub - fastlane/fastlane: 🚀 The easiest way to automate building and releasing your iOS and Android apps</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了相关开源项目，如 strudel（用于构建/签名/公证的 CLI）、xtool（从 Linux 构建 iOS 应用）和 Axiom（用于 LLM 辅助开发的工具包）。一些人提出了关于在没有沙盒的情况下在 Mac 上运行自动化代理的安全担忧，并引用了最近 xAI 上传用户主目录的事件。

**标签**: `#iOS development`, `#macOS`, `#Xcode alternatives`, `#command-line tools`, `#CI/CD`

---

<a id="item-5"></a>
## [Apple SpeechAnalyzer API 基准测试：比 Whisper 快但精度稍低](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 8.0/10

Apple 在 WWDC 2025 上推出的全新 SpeechAnalyzer API 与 OpenAI 的 Whisper-Large-V2 和 Whisper Small 进行了基准测试，结果显示其运行速度约为 Whisper Small 的三倍，同时是测试中最准确的设备端语音引擎。 这项基准测试突显了 Apple 在设备端语音识别方面的努力，可能会威胁到那些仅仅封装 Whisper 的第三方应用，因为 Apple 在 macOS 和 iOS 上提供了原生、更快且更私密的转录功能。这也标志着向实时、本地处理的 ASR 的转变，这可能会改善整个 Apple 生态系统的用户体验。 该 API 在 LibriSpeech 的干净和噪声子集上击败了所有已发布的 Whisper 模型，包括 Whisper Small，同时运行速度是 Whisper Small 的三倍。然而，根据对数学讲座的基准测试，其精度略低于 Whisper-Large-V2。

hackernews · get-inscribe · 7月13日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48894752)

**背景**: Whisper 是 OpenAI 开发的开源自动语音识别（ASR）模型，以其对口音和噪声的鲁棒性而闻名，但通常运行在云服务器或强大的台式机上。Apple 的 SpeechAnalyzer API 专为设备端处理而设计，提供更低的延迟和更好的隐私。该基准测试在 LibriSpeech 和真实录音上比较了速度和精度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48894752">Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor | Hacker News</a></li>
<li><a href="https://www.callstack.com/blog/on-device-speech-transcription-with-apple-speechanalyzer">On-Device Speech Transcription with Apple SpeechAnalyzer and AI SDK</a></li>
<li><a href="https://www.argmaxinc.com/blog/apple-and-argmax">Apple SpeechAnalyzer and Argmax WhisperKit - Argmax</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Whisper 可能不是最先进的基准，建议使用 Nvidia 的 Nemotron 和 Parakeet、Mistral 的 Voxtral 以及 Cohere Transcribe 等模型。一些人担心 Apple 可能会用原生录音机 GUI 淘汰付费的 Whisper 封装应用，而另一些人则称赞该 API 在实时转录方面的速度，并分享了将其集成到 Handy.computer 等项目中的经验。

**标签**: `#Apple`, `#Speech Recognition`, `#Whisper`, `#Benchmark`, `#Machine Learning`

---

<a id="item-6"></a>
## [Sega CD 版 Silpheed 技术深度解析](https://fabiensanglard.net/silpheed/index.html) ⭐️ 8.0/10

Fabien Sanglard 发表了一篇关于 Sega CD 游戏《Silpheed》的详细技术分析，解释了开发者如何利用 FMV 和实时 3D 技巧营造电影般体验。 该分析揭示了 Sega CD 最令人印象深刻的游戏之一的创新工程，展示了开发者如何充分利用有限硬件实现突破性视觉效果。 文章详细介绍了《Silpheed》如何采用全动态视频背景配合实时精灵叠加，营造出伪 3D 效果，让玩家误以为它是一款多边形游戏。

hackernews · ibobev · 7月13日 14:52 · [社区讨论](https://news.ycombinator.com/item?id=48893639)

**背景**: Sega CD 是 Sega Genesis 的外设，增加了 CD-ROM 功能但 3D 硬件有限。《Silpheed》由 Game Arts 开发，是一款创造性使用 FMV 的知名游戏。Fabien Sanglard 以深入的复古游戏工程分析而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Silpheed">Silpheed - Wikipedia</a></li>
<li><a href="https://racketboy.com/retro/sega-cd-101-a-beginners-guide">Sega CD 101: A Beginner’s Guide – RetroGaming with Racketboy</a></li>
<li><a href="https://jsgroth.dev/blog/posts/sega-cd-pcm-overview/">Sega CD PCM Chip - An Overview | jsgroth's blog</a></li>

</ul>
</details>

**社区讨论**: 评论中包括关于 Sega CD 音频设置的技术纠正，以及对游戏技术的赞赏。一些用户分享了展示类似能力的演示场景示例。

**标签**: `#game development`, `#retro computing`, `#Sega CD`, `#technical analysis`, `#Fabien Sanglard`

---

<a id="item-7"></a>
## [三星健康应用威胁：退出 AI 训练则删除数据](https://neow.in/cWsyMTV3) ⭐️ 8.0/10

三星健康更新了条款，要求用户同意将其健康数据用于 AI 训练，否则应用将删除数据并限制功能。 这引发了重大的隐私担忧，因为它迫使用户在丢失健康数据或允许三星将敏感信息用于 AI 训练之间做出选择，可能为其他健康应用树立先例。 目标数据类别包括睡眠、药物、医疗记录和周期追踪详情；拒绝不仅会删除数据，还会禁用关键功能，实际上降低了设备的可用性。

hackernews · bundie · 7月13日 20:01 · [社区讨论](https://news.ycombinator.com/item?id=48897991)

**背景**: 在健康数据上训练 AI 可以改善诊断和个性化护理，但也引发了伦理和隐私问题。像三星这样的公司经常收集用户数据来训练模型，但用数据删除来强制同意是一种有争议的做法，可能违反用户信任和监管规范。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.coursera.org/specializations/artificial-intelligence-for-healthcare">Artificial Intelligence for Healthcare | Coursera</a></li>
<li><a href="https://online.stanford.edu/artificial-intelligence/ai-healthcare-professionals">AI for Healthcare Professionals - Stanford Online</a></li>

</ul>
</details>

**社区讨论**: 评论普遍持批评态度，用户对强制做法表示沮丧，并将其与其他公司的做法进行比较。一些人讽刺地表示数据删除可能是一种好处，而另一些人则指出应用功能差和数据导出问题。

**标签**: `#privacy`, `#AI`, `#data deletion`, `#Samsung Health`, `#ethics`

---

<a id="item-8"></a>
## [开放数据在气候.gov 关停后被保存](https://werd.io/climate-gov-was-destroyed-open-data-saved-it/) ⭐️ 8.0/10

气候.gov 网站被关闭，但开放数据活动人士将其数据集归档，保留了公众对关键气候信息的访问。 这一事件凸显了开放数据和数据永久性对政府透明度、科学研究和公众问责的重要性。 存档站点依赖捐赠维持运行，动态后端服务未能完全保留，限制了部分功能。

hackernews · benwerd · 7月13日 19:57 · [社区讨论](https://news.ycombinator.com/item?id=48897945)

**背景**: 开放数据指任何人都可以自由访问、使用和共享的数据。数据永久性是指数字数据应无限期存在，免于删除或丢失。政府网站可能因政策变化而被移除，但开放数据倡议和草根存档努力有助于确保持续访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_remanence">Data remanence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_permanence">Digital permanence - Wikipedia</a></li>
<li><a href="https://opendatahandbook.org/glossary/en/terms/data-preservation/">Data preservation</a></li>

</ul>
</details>

**社区讨论**: 评论者担心基于捐赠的存档的长期可行性，有人指出政府数据应属于公共领域。还有人建议对静态政府内容使用 IPFS 等分布式系统，而部分人对全部依赖捐赠的说法提出质疑。

**标签**: `#open data`, `#climate`, `#government`, `#data preservation`

---

<a id="item-9"></a>
## [Pydantic 发布 Pydantic AI 代理框架](https://github.com/pydantic/pydantic-ai) ⭐️ 8.0/10

Pydantic 宣布推出 pydantic-ai，这是一个 Python 代理框架，用于构建生产级的生成式 AI 应用和工作流，它利用 Pydantic 验证和现代 Python 类型提示。 作为 Pydantic 团队（其验证层已被许多主流 LLM SDK 使用）构建的框架，pydantic-ai 可能成为在 Python 中构建可靠、类型安全 AI 代理的标准。 该框架支持包括 OpenAI、Anthropic、Gemini 和 DeepSeek 在内的数十个模型提供商，并与 Pydantic Logfire 无缝集成，用于可观测性和调试。

rss · GitHub Trending - Python Daily · 7月13日 01:40

**背景**: Pydantic 是一个使用类型提示进行数据验证的流行 Python 库。该团队之前创建了广泛使用的 Web 框架 FastAPI。新的代理框架旨在将相同的人体工程学设计带到生成式 AI 开发中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pydantic.dev/docs/ai/overview/">Pydantic AI | Pydantic Docs</a></li>
<li><a href="https://github.com/pydantic/pydantic-ai">GitHub - pydantic/pydantic-ai: AI Agent Framework, the Pydantic way · GitHub</a></li>

</ul>
</details>

**标签**: `#python`, `#ai`, `#agent-framework`, `#pydantic`, `#llm`

---

<a id="item-10"></a>
## [公共 API 仓库：精选免费 API 列表](https://github.com/public-apis/public-apis) ⭐️ 8.0/10

GitHub 上的 public-apis 仓库是一个社区精选的免费 API 列表，仍在积极维护中，并不断添加各领域的新 API。 该仓库是开发者的重要资源，节省了寻找免费 API 用于原型开发和学习的時間。其社区驱动的特性保证了多样性和可靠性。 该仓库由 APILayer 赞助，页面顶部展示其 API，但主列表仍由社区管理。它包含动物、音乐、金融等类别的 API。

rss · GitHub Trending - Python Daily · 7月13日 01:40

**背景**: API（应用程序编程接口）允许不同软件应用程序之间通信。像 public-apis 这样的精选列表帮助开发者快速找到免费 API，无需搜索多个来源。该仓库在 GitHub 上拥有超过 30 万颗星，体现了其受欢迎程度和信任度。

**标签**: `#APIs`, `#open-source`, `#developer tools`, `#resources`

---

<a id="item-11"></a>
## [微软发布 TRELLIS.2，实现快速 3D 生成](https://github.com/microsoft/TRELLIS.2) ⭐️ 8.0/10

微软发布了 TRELLIS.2，这是一个拥有 40 亿参数的 3D 生成模型，采用新颖的 O-Voxel 表示法，能从图像生成高达 1536³分辨率的高质量 3D 资产，耗时约一分钟。 该模型在图像到 3D 生成领域取得了显著进展，能处理任意拓扑结构、支持完整 PBR 材质且推理速度极快，使游戏、虚拟现实和设计行业的 3D 资产创作更加便捷。 TRELLIS.2 采用名为 O-Voxel 的“无场”稀疏体素结构，能够无损转换地建模开放表面、非流形几何和内部结构，并支持基色、粗糙度、金属度和不透明度等属性。

rss · GitHub Trending - Python Daily · 7月13日 01:40

**背景**: 3D 生成通常依赖 NeRF、3D 高斯或网格等表示法，往往需要单独的优化或渲染步骤。本工作基于结构化潜在表示，统一了不同输出格式，从而实现可扩展且多功能的生成，这与先前研究一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.01506">[2412.01506] Structured 3D Latents for Scalable and Versatile 3D Generation</a></li>
<li><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Xiang_Structured_3D_Latents_for_Scalable_and_Versatile_3D_Generation_CVPR_2025_paper.pdf">Structured 3D Latents for Scalable and Versatile 3D Generation</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#machine learning`, `#computer vision`, `#Microsoft`, `#generative AI`

---

<a id="item-12"></a>
## [ComfyUI：一个强大的模块化图形界面，用于扩散模型](https://github.com/Comfy-Org/ComfyUI) ⭐️ 8.0/10

ComfyUI 是一个广泛使用的开源节点式图形界面，用于扩散模型，无需编程即可实现强大的 AI 内容创作。 它使复杂的 AI 工作流平民化，让创意人员对每个参数和输出拥有完全控制，成为开源 AI 生态系统中的关键工具。 ComfyUI 原生支持最新的开源模型，并提供用于闭源模型的 API 节点；它可通过桌面应用、便携式安装或云服务在 Windows、Linux 和 macOS 上使用。

rss · GitHub Trending - Python Daily · 7月13日 01:40

**背景**: 扩散模型是一类生成式 AI，通过迭代去噪随机噪声来创建图像、视频和音频。传统上，运行这些模型需要命令行或脚本界面。ComfyUI 提供了一个可视化的节点图，代表生成流程的每一步，使复杂工作流的设计、共享和复现变得更容易，且无需编程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Comfy-Org/ComfyUI">Comfy-Org/ComfyUI: The most powerful and modular diffusion model ...</a></li>
<li><a href="https://opensourceai.tech/tool/comfyui.html">ComfyUI — Node - graph control over image pipelines | Open-Source AI</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#AI`, `#GUI`, `#backend`, `#modular`

---

<a id="item-13"></a>
## [谷歌发布开源 Gemini 命令行工具](https://github.com/google-gemini/gemini-cli) ⭐️ 8.0/10

谷歌发布了名为 Gemini CLI 的开源命令行工具，使开发者可以直接在终端中与 Gemini AI 模型交互。该工具可通过 npm、Homebrew 等包管理器安装。 该工具为开发者提供了轻量级、终端优先的接口，以利用 Gemini 强大的 AI 能力，包括 100 万 token 的上下文窗口和内置工具，有望加速开发工作流中的 AI 集成。 Gemini CLI 提供免费套餐，每分钟 60 次请求，每天 1000 次请求，支持 Gemini 3 模型，并通过 MCP 支持可扩展性。该工具采用 Apache 2.0 许可证。

rss · GitHub Trending - TypeScript Daily · 7月13日 01:42

**背景**: Gemini CLI 是谷歌 Gemini AI 模型的命令行界面，Gemini 模型是具有推理能力和处理大上下文能力的大型语言模型。该 CLI 提供内置工具，如 Google 搜索接地、文件操作和 shell 命令，使其成为开发者的多功能代理。

**标签**: `#AI`, `#CLI`, `#Google Gemini`, `#Open Source`

---

<a id="item-14"></a>
## [OpenAI 发布 Codex CLI：轻量级终端编码助手](https://github.com/openai/codex) ⭐️ 8.0/10

OpenAI 发布了 Codex CLI，这是一款轻量级编码助手，可在终端本地运行，支持 macOS、Linux 和 Windows。 该工具将 AI 辅助编码直接带入开发者的终端，无需依赖 IDE 或云服务，有望简化许多开发者的工作流程。 Codex CLI 可通过 curl、npm 或 Homebrew 安装，需使用 ChatGPT 账户登录或 API 密钥。它采用 Apache-2.0 许可证。

rss · GitHub Trending - Rust Daily · 7月13日 01:41

**背景**: Codex 是 OpenAI 的 AI 系统，可以将自然语言转换为代码。此前以云服务或 IDE 插件形式提供，Codex CLI 现提供本地终端版本。

**标签**: `#AI`, `#coding agent`, `#OpenAI`, `#developer tools`, `#terminal`

---

<a id="item-15"></a>
## [微软发布 MXC 沙箱代码执行系统](https://github.com/microsoft/mxc) ⭐️ 8.0/10

微软开源了 MXC（Microsoft eXecution Container），这是一个策略驱动的沙箱代码执行系统，可在 Windows、Linux 和 macOS 上运行不受信任的代码，支持进程容器、虚拟机、操作系统沙箱等多种隔离后端。 MXC 通过提供统一的跨平台沙箱层来隔离模型输出、插件和工具，满足了 AI 安全和不可信代码隔离的关键需求。随着 AI 代理和代码生成工具需要安全执行环境，这一点尤为重要。 MXC 使用基于 JSON 的配置模式来定义执行参数和安全策略，并包含一个 TypeScript SDK，提供一次性及状态感知的 API。当前早期预览版存在已知的过度宽松策略，不应被视为安全边界。

rss · GitHub Trending - Rust Daily · 7月13日 01:41

**背景**: 沙箱代码执行涉及在隔离环境中运行不可信程序，以防止它们损害主机系统。MXC 基于微软现有的沙箱技术（如 Windows Sandbox）构建，并增加了跨平台支持，采用策略驱动的方法。它专为执行大型语言模型的输出或安全运行第三方插件等场景设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/mxc">GitHub - microsoft / mxc : Policy-driven, layered isolation and...</a></li>
<li><a href="https://devlery.com/en/blog/microsoft-mxc-agent-sandbox">Microsoft MXC Preview Is an OS Sandbox for Windows AI... - Devlery</a></li>

</ul>
</details>

**标签**: `#sandbox`, `#security`, `#AI safety`, `#microsoft`, `#code execution`

---

<a id="item-16"></a>
## [Screenpipe：本地 AI 记忆记录器，赋能智能体](https://github.com/screenpipe/screenpipe) ⭐️ 8.0/10

Screenpipe，一个 YC 支持的工具，现已采用源代码可用的许可证，并声称其 AI PII 模型在计算机录制数据上优于 Google、Microsoft 和 OpenAI 的模型，在消费设备上运行仅需 9 毫秒。 这使得 AI 智能体可以私有地在本地记录用户所有活动，有可能在不牺牲隐私的前提下，彻底改变生产力和自动化工作流。 它与 OpenClaw 和 Hermes 智能体以及 100 多个应用集成，桌面应用可下载并支持自动更新。

rss · GitHub Trending - Rust Daily · 7月13日 01:41

**背景**: Screenpipe 是一个本地优先的工具，持续录制屏幕和音频，为 AI 智能体创建可搜索的记忆。它属于不断增长的个人 AI 助手生态系统的一部分，如 OpenClaw 和 Hermes agent，这些助手旨在用户设备上运行，并利用捕获的数据实现自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://github.com/openclaw/openclaw">GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — The Agent That Grows With You</a></li>

</ul>
</details>

**标签**: `#AI`, `#Privacy`, `#Screen Recording`, `#Automation`, `#Memory`

---

<a id="item-17"></a>
## [InfluxDB 3 Core 开源时序数据库发布](https://github.com/influxdata/influxdb) ⭐️ 8.0/10

InfluxData 发布了 InfluxDB 3 Core，这是一款基于 Apache Arrow、DataFusion 和 Parquet 构建的开源时序数据库，自 2025 年 4 月起已正式发布。它提供低于 10 毫秒的快速查询响应时间，并支持 SQL 和 InfluxQL。 此次发布标志着广泛使用的时序数据库的重大演进，利用现代列式格式提升了性能和可扩展性。它为实时分析和监控提供了免费的开源替代方案。 InfluxDB 3 Core 具有无磁盘架构，支持对象存储，内嵌 Python 虚拟机用于插件，并兼容 InfluxDB 1.x 和 2.x API。它使用 Apache Parquet 进行持久化，并作为单一二进制文件运行。

rss · GitHub Trending - Rust Daily · 7月13日 01:41

**背景**: Apache Arrow 提供了一种语言无关的列式内存格式，用于高效的数据分析。DataFusion 是一个用 Rust 编写的可扩展查询引擎，使用 Arrow 格式。Apache Parquet 是一种面向列的存储格式。InfluxDB 是一个流行的时序数据库，v3 Core 代表了重大的架构转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Arrow">Apache Arrow - Wikipedia</a></li>
<li><a href="https://github.com/apache/datafusion">GitHub - apache/datafusion: Apache DataFusion SQL Query Engine · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Parquet">Apache Parquet - Wikipedia</a></li>

</ul>
</details>

**标签**: `#InfluxDB`, `#time series database`, `#Apache Arrow`, `#DataFusion`, `#open source`

---

<a id="item-18"></a>
## [Tailscale 开源其核心 VPN 守护程序与 CLI](https://github.com/tailscale/tailscale) ⭐️ 8.0/10

Tailscale 已将其核心 `tailscaled` 守护程序和 `tailscale` 命令行工具开源，可在 GitHub 仓库 tailscale/tailscale 中找到。 这一举措使社区能够审查、审计和贡献底层 VPN 技术，增加了信任度，并促进了基于 WireGuard 的安全网络的更广泛采用。 该仓库包含适用于 Linux、Windows、macOS 的守护程序和 CLI，并部分支持 FreeBSD 和 OpenBSD，但不包含 iOS 和 Android 的移动 GUI 代码。

rss · GitHub Trending - Go Daily · 7月13日 01:37

**背景**: Tailscale 是一种 VPN 服务，通过利用 WireGuard（一种现代高效的 VPN 协议）简化了安全网络连接。其核心组件的开源发布使用户能够理解和自定义其 VPN 设置。此仓库包含 Tailscale 的大部分开源代码，是透明度和社区开发的关键资源。

**标签**: `#networking`, `#VPN`, `#WireGuard`, `#security`, `#Go`

---

<a id="item-19"></a>
## [Cloudflared：Cloudflare 隧道客户端](https://github.com/cloudflare/cloudflared) ⭐️ 8.0/10

Cloudflared 是 Cloudflare Tunnel 的命令行客户端，它是一个守护进程，可将流量从 Cloudflare 网络代理到您的源服务器，而无需开放防火墙端口。它支持第 4 层（TCP）流量，适用于 SSH 和 RDP 等协议。 该工具可实现仅出站的安全连接，无需公网 IP 或开放端口。它被开发者和 DevOps 广泛采用，通过 Cloudflare 的全球网络安全地暴露本地服务。 Cloudflared 可通过独立二进制文件、Docker、Debian/RPM 包或 Homebrew 安装。它还支持在第 4 层访问 TCP 流量的隧道源，无需 HTTP/WebSocket，适用于 SSH 和 RDP。

rss · GitHub Trending - Go Daily · 7月13日 01:37

**背景**: 隧道守护进程在两个网络之间创建安全加密连接，常用于将内部服务暴露到互联网而无需开放防火墙端口。Cloudflare Tunnel 使用仅出站连接，即守护进程主动连接到 Cloudflare 边缘节点，再由边缘节点将流量路由到源服务器。这种方法通过保持源网络封闭来增强安全性，减少攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/tunnel/">Cloudflare Tunnel</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel · Cloudflare One docs</a></li>

</ul>
</details>

**标签**: `#networking`, `#tunneling`, `#cloudflare`, `#security`, `#devops`

---

<a id="item-20"></a>
## [Kubescape：开源 Kubernetes 安全平台](https://github.com/kubescape/kubescape) ⭐️ 8.0/10

Kubescape 是一个 CNCF 孵化项目，提供全面的 Kubernetes 安全功能，包括风险分析、合规扫描和配置错误检测，覆盖 IDE、CI/CD 和集群。 该项目解决了 Kubernetes 环境中的关键安全需求，通过在整个开发生命周期中自动化安全检查，帮助 DevOps 和安全团队节省时间和资源。 Kubescape 支持加固、态势管理和运行时安全，作为开源工具提供，其徽章显示 CNCF 孵化状态和 OpenSSF 最佳实践合规性。

rss · GitHub Trending - Go Daily · 7月13日 01:37

**背景**: Kubernetes 是一个管理容器化应用的容器编排平台。由于其动态特性和众多组件，Kubernetes 的安全性复杂。Kubescape 帮助用户在开发早期和运行时识别漏洞和配置错误。

**标签**: `#Kubernetes`, `#Security`, `#Open Source`, `#DevOps`, `#Go`

---

<a id="item-21"></a>
## [SOPS：多功能的密钥管理工具现已纳入 CNCF](https://github.com/getsops/sops) ⭐️ 8.0/10

SOPS（Secrets OPerationS）是一个成熟的开源工具，用于加密和管理文件中的密钥，支持多种格式和密钥管理后端。它最初于 2015 年由 Mozilla 创建，并于 2023 年被接纳为 CNCF Sandbox 项目。 SOPS 通过支持使用云 KMS 或离线工具（如 age 和 PGP）管理密钥来简化配置文件的加密，为 DevOps 和安全团队提供了便利。其广泛的后端支持以及与 CI/CD 流水线的集成使其成为安全软件交付中的关键组件。 SOPS 支持 YAML、JSON、ENV、INI 和二进制文件的加密和解密，可使用 AWS KMS、GCP KMS、Azure Key Vault、华为云 KMS、age 和 PGP 作为密钥管理后端。它使用 Go 语言编写，遵循 MPL 2.0 许可证。

rss · GitHub Trending - Go Daily · 7月13日 01:37

**背景**: 密钥管理涉及安全存储和访问敏感数据，如密码、API 密钥和证书。SOPS 允许用户直接在配置文件中加密这些数据，从而可以将其提交到版本控制而无需暴露明文密钥。该工具支持多种云和离线密钥管理系统，为不同部署环境提供了灵活性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.huaweicloud.com/intl/en-us/usermanual-dew/dew_01_0094.html">Using KMS for Encryption_Data Encryption Workshop-Huawei Cloud</a></li>

</ul>
</details>

**标签**: `#secrets management`, `#encryption`, `#devops`, `#security`, `#Go`

---

<a id="item-22"></a>
## [Telegram 的 t.me 域名被注册局暂停](https://www.nodeseek.com/post-820652-1) ⭐️ 8.0/10

Telegram 的短链接域名 t.me 已被注册局级暂停，WHOIS 现在显示'serverHold'状态，完全阻止 DNS 解析。所有 t.me 链接目前无法访问，链接分享功能受损。 这一中断影响了全球数百万依赖 t.me 链接共享频道、群组和机器人的 Telegram 用户。此事件凸显了集中式域名控制的风险以及即使对于主要平台来说互联网基础设施的脆弱性。 'serverHold'状态是一种注册局级暂停，会禁用整个 DNS 区域，意味着该域名无法被任何 DNS 服务器解析。Telegram 应用本身仍可运行，但在暂停解除前所有 t.me 链接均失效。

rss · NodeSeek · 7月13日 23:40

**背景**: 在域名系统中，'serverHold'状态是一种由注册局施加的暂停，阻止域名被用于任何服务。这与由注册商设置的'clientHold'不同。当域名被置于 serverHold 时，其 DNS 记录不会被发布，导致所有关联服务如网站和电子邮件停止工作。出现这种情况可能由于法律问题、违规或过期等原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/10717/46/why-was-my-domain-suspended-with-a-serverhold-or-clienthold-status/">Why was my domain suspended with a serverHold or clientHold ...</a></li>
<li><a href="https://sidebysidedomains.com/blog/serverhold-domain-status.html">"ServerHold" Domain Status Explained: Causes & Solutions ...</a></li>

</ul>
</details>

**标签**: `#telegram`, `#domain`, `#dns`, `#internet infrastructure`, `#service disruption`

---

<a id="item-23"></a>
## [CrashStealer 恶意软件瞄准 Mac，窃取 14 款密码管理器数据](https://www.ithome.com/0/976/263.htm) ⭐️ 8.0/10

Jamf Threat Labs 披露了针对 macOS 用户的 CrashStealer 恶意软件，该软件从 14 款密码管理器和 80 个加密货币钱包扩展中窃取凭证。苹果在收到通知后已撤销了恶意应用的签名。 此次攻击影响重大，因为它针对广泛使用的密码管理器和加密钱包，使数百万用户面临风险。苹果迅速撤销签名表明了严重性，但恶意软件能够绕过 Gatekeeper 也凸显了 macOS 面临的安全挑战。 该恶意软件伪装成名为 Werkbit 的工具，利用有效的 Developer ID 绕过 Gatekeeper，并诱导用户输入 Mac 密码以加载最终载荷。它从浏览器、密码管理器（包括 1Password、Bitwarden、LastPass）以及加密钱包中窃取数据，并在 ~/Library/Caches/com.apple.crashreporter/ 中安装持久化副本。

rss · IT之家 · 7月13日 23:41

**背景**: Gatekeeper 是 macOS 的安全功能，默认在运行前验证下载的应用程序，阻止不受信任的软件。由苹果签名的 Developer ID 允许应用通过 Gatekeeper 检查。CrashStealer 通过使用窃取或获得的 Developer ID 来伪装成合法应用，从而滥用了这一机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gatekeeper_(macOS)">Gatekeeper ( macOS ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Developer_Tools">Apple Developer Tools</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#macOS`, `#password manager`, `#malware`, `#Apple`

---

<a id="item-24"></a>
## [我国团队创造钙钛矿-有机叠层太阳能电池 28.04%效率纪录](https://www.ithome.com/0/976/233.htm) ⭐️ 8.0/10

由李永舫院士和孟磊研究员带领的中国研究团队实现了钙钛矿-有机叠层太阳能电池经认证的稳态光电转换效率达 28.04%，成果发表在《自然》期刊。该器件还表现出卓越的稳定性，持续光照 625 小时后仍能保持初始效率的 90%。 这一破纪录的效率超越了此前钙钛矿-有机叠层电池的基准，使这种轻量柔性的太阳能技术更接近建筑光伏一体化、便携电子设备和空间能源等实际应用。稳定性提升解决了商业化的关键障碍。 研究团队在宽带隙钙钛矿前驱体中引入了一种光转化添加剂分子 TDB（4-[3-(三氟甲基)-3H-双吖丙啶-3-基]苄胺），实现了抑制卤化物相分离并增强器件稳定性的两阶段策略。效率由独立第三方认证。

rss · IT之家 · 7月13日 15:11

**背景**: 钙钛矿太阳能电池是一种下一代光伏技术，具有高效率与低成本制造的优势。叠层太阳能电池将两个或多个具有不同带隙的吸光层堆叠起来，以捕获更宽的太阳光谱，从而突破单结电池的肖克利-奎伊瑟极限。钙钛矿-有机叠层结合了宽带隙钙钛矿前电池和有机后电池，但历史上因光照下的卤化物相分离而存在稳定性问题。本工作引入的 TDB 添加剂作为一种动态调节剂来缓解该问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10869-x">Perovskite–organic tandem solar cells with a photo ... - Nature</a></li>
<li><a href="https://www.nature.com/articles/s41578-023-00642-1">Perovskite–organic tandem solar cells - Nature Reviews Materials</a></li>

</ul>
</details>

**标签**: `#Perovskite Solar Cells`, `#Solar Energy`, `#Photovoltaics`, `#Efficiency Record`, `#Nature`

---

<a id="item-25"></a>
## [中国电动汽车电池新国标：热失控后 2 小时不起火](https://www.36kr.com/p/3893470914870144) ⭐️ 8.0/10

两项强制性国家标准 GB 38031-2025 和 GB 18384-2025 于 2026 年 7 月 1 日实施，要求动力电池在热失控后至少 2 小时内不起火、不爆炸，取代了旧版的“起火前 5 分钟报警”要求。新标准还增加了底部撞击测试和 300 次快充循环安全测试。 这是中国有史以来最严格的电动汽车电池安全法规，使合规成本增加 15%-20%，并加速行业洗牌，挤压中小电池厂商生存空间。消费者将受益于更低的起火风险，但长期可能需要承担更高的车价。 每辆车合规成本预计增加 4000-6500 元，包括电池包结构件修改、产线升级和测试费用。头部企业如宁德时代和比亚迪已通过全部测试，预计 30%-40%的中小电芯厂将退出市场。

rss · 36氪 - 24小时热榜 · 7月13日 03:53

**背景**: 热失控是锂电池因内部短路或过热引发的连锁放热反应，导致温度不可控地急剧上升，可能引发起火或爆炸。比亚迪刀片电池是一种采用磷酸铁锂化学体系的结构创新，通过针刺测试时温度升高极小。BMS（电池管理系统）监控电压、温度和电流，确保安全运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://baike.baidu.com/item/电池热失控/67387858">电池热失控（锂电池内短路或过热致链式反应）_百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/666521979">比亚迪刀片电池技术 - 知乎专栏</a></li>
<li><a href="https://www.byd.com/cn/detail617">电动化上半场完美收官：比亚迪发布第二代刀片电池及闪充技术</a></li>

</ul>
</details>

**标签**: `#EV batteries`, `#safety standards`, `#China regulation`, `#cost analysis`, `#automotive industry`

---

<a id="item-26"></a>
## [GPUHedge 将无服务器 GPU 冷启动 p95 延迟从 117 秒降至 30 秒](https://www.reddit.com/r/MachineLearning/comments/1uvlb6h/gpuhedge_hedging_serverless_gpu_providers/) ⭐️ 8.0/10

GPUHedge 是一个开源工具，通过跨多个无服务器 GPU 提供商的投机执行来降低冷启动延迟，在基准测试中将 p95 延迟从 117 秒降至 30 秒。 冷启动延迟是无服务器 GPU 推理的主要痛点，影响用户体验和成本效率。GPUHedge 的方法通过缓解尾部延迟问题，使无服务器 GPU 更适用于延迟敏感型应用，而无需更改提供商。 该系统通过监控主提供商上的作业生命周期，并有条件地启动备份来工作；第一个通过验证器的结果获胜，失败的任务通过提供商的 API 取消。在基准测试中，在 10 秒后启动固定的 RunPod → Cerebrium 对冲，将超过 60 秒的请求从 11/36 减少到 0/36。

reddit · r/MachineLearning · /u/Putrid_Construction3 · 7月13日 19:20

**背景**: 无服务器 GPU 冷启动延迟发生在 GPU 模型在提供服务推理之前需要从头加载时，对于大型模型可能需要几十秒到几分钟。这是一个众所周知的挑战，因为无服务器平台为了节省成本不会在请求之间保持 GPU 内存热状态。对冲是分布式系统中的一种技术，即发送多个冗余请求并使用最快响应的结果，这里将其应用于不同的 GPU 提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.paralleliq.ai/blog/gpu-ops-serverless-cold-start">Serverless GPU Cold Start Latency: Causes and Solutions</a></li>
<li><a href="https://www.beam.cloud/blog/top-serverless-gpu-providers">The Top Serverless GPU Providers in 2025, Ranked by Cold Start</a></li>

</ul>
</details>

**标签**: `#serverless`, `#GPU`, `#cold-start`, `#latency`, `#hedging`

---