---
layout: default
title: "Horizon Summary: 2026-07-09 (ZH)"
date: 2026-07-09
lang: zh
---

> 从 309 条内容中筛选出 33 条重要资讯。

---

1. [TypeScript 7.0 性能提升最高达 11.9 倍](#item-1) ⭐️ 10.0/10
2. [OpenAI 推出 GPT-Live 语音助手，可委托 GPT-5.5 处理](#item-2) ⭐️ 9.0/10
3. [微软将 TypeScript 移植到 Go 语言，性能提升 10 倍](#item-3) ⭐️ 9.0/10
4. [Temporal：开源持久执行平台，用于可靠的工作流](#item-4) ⭐️ 9.0/10
5. [MoWorld：全球首个基于国产 NPU 的 50FPS 实时世界模型](#item-5) ⭐️ 9.0/10
6. [Linux 内核 KVM 高危漏洞 CVE-2026-53359 潜伏 16 年可逃逸虚拟机](#item-6) ⭐️ 9.0/10
7. [智能体安全触发器绕过 LLM 智能体的文本护栏](#item-7) ⭐️ 9.0/10
8. [解码优衣库 T 恤上的混淆 bash 脚本](#item-8) ⭐️ 8.0/10
9. [Bun 从 Zig 重写为 Rust：更小、更快、更安全](#item-9) ⭐️ 8.0/10
10. [Mistral 发布 Robostral Navigate：无地图 AI 导航](#item-10) ⭐️ 8.0/10
11. [Cloudflare Meerkat：无领导异步共识算法](#item-11) ⭐️ 8.0/10
12. [欧盟重振私密信息扫描规则](#item-12) ⭐️ 8.0/10
13. [GitHub 仓库追踪泄露的 AI 系统提示词](#item-13) ⭐️ 8.0/10
14. [.NET 代理技能仓库发布，助力 AI 编码代理](#item-14) ⭐️ 8.0/10
15. [Kyutai 发布 Pocket TTS：面向 CPU 的开源轻量级 TTS](#item-15) ⭐️ 8.0/10
16. [Anthropic 发布 Claude Agent Skills 开源仓库](#item-16) ⭐️ 8.0/10
17. [n8n：开源 AI 工作流自动化平台](#item-17) ⭐️ 8.0/10
18. [Dynamo：开源数据中心级推理服务框架](#item-18) ⭐️ 8.0/10
19. [uv：用 Rust 编写的快速 Python 包管理器](#item-19) ⭐️ 8.0/10
20. [微软 windows-rs：Rust 的 Windows API 绑定](#item-20) ⭐️ 8.0/10
21. [腾讯开源 WeKnora：集成 RAG、自主代理与维基的知识平台](#item-21) ⭐️ 8.0/10
22. [SOPS：一个简单灵活的密钥管理工具](#item-22) ⭐️ 8.0/10
23. [LocalAI：开源 AI 引擎，无需 GPU 即可在任何硬件上运行模型](#item-23) ⭐️ 8.0/10
24. [Meta 研发‘超级感知’智能眼镜，可持续录音自动拍照](#item-24) ⭐️ 8.0/10
25. [SpaceXAI 发布 Grok 4.5：与 Cursor 联合训练的编程 AI 模型](#item-25) ⭐️ 8.0/10
26. [Anthropic 利润超 10 亿美元，秘密提交 IPO](#item-26) ⭐️ 8.0/10
27. [索尼因停售实体游戏光盘面临 40 亿欧元集体诉讼](#item-27) ⭐️ 8.0/10
28. [Cloudflare 与 OpenAI 启动试点，利用网络信号优化 AI 搜索](#item-28) ⭐️ 8.0/10
29. [LingBot-Video：开源 13B 稀疏 MoE 视频扩散世界模型](#item-29) ⭐️ 8.0/10
30. [DeepSeek 自主研发 AI 推理芯片以减少供应商依赖](#item-30) ⭐️ 8.0/10
31. [阿里巴巴下令全员卸载 Claude](#item-31) ⭐️ 8.0/10
32. [安卓远程 Root 漏洞链'IonStack'威胁所有版本](#item-32) ⭐️ 8.0/10
33. [通过泄漏电磁信号识别手机应用，准确率高达 99%](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 性能提升最高达 11.9 倍](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 10.0/10

微软发布了 TypeScript 7.0 重大版本更新，通过全新的编译器架构，在大型代码库（如 VS Code）上实现了最高 11.9 倍的性能提升。 这一显著的性能提升解决了 TypeScript 长期以来的痛点——大型项目编译速度慢，使其更适合超大型代码库，并提高了开发效率。 基准测试显示，VS Code 的编译时间从 TypeScript 6 的 125.7 秒降至 10.6 秒，而 Sentry 和 Bluesky 等项目分别获得了 8.9 倍和 8.7 倍的加速。

hackernews · DanRosenwasser · 7月8日 16:06 · [社区讨论](https://news.ycombinator.com/item?id=48833715)

**背景**: TypeScript 是一种静态类型化的 JavaScript 超集，可编译为纯 JavaScript。传统上，编译器本身用 TypeScript 编写，可能成为大型项目的瓶颈。此次更新可能涉及用低级语言重写或架构上的重大改变以实现如此大的性能提升。

**社区讨论**: 社区对此公告给予了压倒性的好评，评论者强调了巨大的速度提升并向团队表示祝贺。一些人指出，Node.js 的原生类型剥离减少了对 tsc 的依赖，但性能提升仍使 TypeScript 7 具有吸引力。

**标签**: `#TypeScript`, `#performance`, `#compiler`, `#Microsoft`, `#programming languages`

---

<a id="item-2"></a>
## [OpenAI 推出 GPT-Live 语音助手，可委托 GPT-5.5 处理](https://openai.com/index/introducing-gpt-live/) ⭐️ 9.0/10

OpenAI 于 2026 年 7 月 27 日发布 GPT-Live，这是一款全双工语音助手，可在后台将复杂查询委托给 GPT-5.5，实现长时间自然对话。 GPT-Live 弥合了语音界面与前沿 AI 模型之间的差距，使用户能够在不牺牲推理能力的情况下进行无缝智能对话。这可能改变用户日常与 AI 互动的方式，用于头脑风暴、研究及个人助理等任务。 GPT-Live 采用全双工架构，可同时收听和说话，并带有自然的回馈如“嗯”“对”。对于需要网络搜索、深度推理或代理步骤的任务，它会自动委托给 GPT-5.5，同时语音层保持连续交互。

hackernews · logickkk1 · 7月8日 17:03 · [社区讨论](https://news.ycombinator.com/item?id=48834405)

**背景**: GPT-5.5（代号“Spud”）是 OpenAI 于 2026 年 4 月 23 日发布的最强大语言模型，提供更快更复杂的推理能力。之前的 ChatGPT 语音模式使用较旧模型，智能受限。GPT-Live 通过将实时语音层与 GPT-5.5 的后台处理相结合来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT-Live | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>
<li><a href="https://mer.vin/2026/07/gpt-live-explained-full-duplex-chatgpt-voice-with-gpt-5-5-delegation/">GPT-Live Explained: Full-Duplex ChatGPT Voice With GPT-5.5 ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户称赞委托功能可实现高效的一小时长对话，而另一些人则担忧社交替代、缺乏工具集成及潜在的社会危害。有用户报告了一个 bug，助手会在不恰当的时候打断并发出笑声。

**标签**: `#OpenAI`, `#GPT Live`, `#voice assistant`, `#AI`, `#GPT-5.5`

---

<a id="item-3"></a>
## [微软将 TypeScript 移植到 Go 语言，性能提升 10 倍](https://github.com/microsoft/typescript-go) ⭐️ 9.0/10

此移植有望显著加速 TypeScript 开发流程，特别是对于大型代码库，并能带来更快的编辑器和构建体验。这标志着 TypeScript 实现策略的重大转变，可能影响整个 JavaScript 生态系统。 预览版支持大部分核心功能，如解析、类型检查和声明生成，但语言服务器协议仍在开发中，API 尚未就绪。最终版本预计作为 TypeScript 7.0 发布，并最终合并回主 TypeScript 仓库。

rss · GitHub Trending - Go Daily · 7月8日 01:35

**背景**: TypeScript 是一种流行的类型化 JavaScript 超集，可编译为普通 JavaScript。当前编译器本身用 TypeScript 编写，对于大型项目可能较慢。通过用 Go（一种以高性能和高效并发著称的编译语言）重写编译器，微软旨在实现大幅提速。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/typescript-go">GitHub - microsoft/typescript-go: Staging repo for development of native port of TypeScript · GitHub</a></li>
<li><a href="https://devblogs.microsoft.com/typescript/typescript-native-port/">A 10x Faster TypeScript - TypeScript</a></li>
<li><a href="https://www.reddit.com/r/ProgrammingLanguages/comments/1j9osva/typescript_compiler_is_being_ported_to_go/">r/ProgrammingLanguages on Reddit: TypeScript compiler is being ported to Go</a></li>

</ul>
</details>

**标签**: `#TypeScript`, `#Go`, `#performance`, `#compiler`, `#port`

---

<a id="item-4"></a>
## [Temporal：开源持久执行平台，用于可靠的工作流](https://github.com/temporalio/temporal) ⭐️ 9.0/10

Temporal 是一个开源持久执行平台，通过工作流编排帮助开发者构建可扩展且可靠的分布式系统。它能自动处理故障和重试，确保应用逻辑的弹性执行。 Temporal 解决了构建分布式系统中的关键挑战，例如在故障间管理状态以及在不牺牲生产力的前提下确保可靠性。各大公司的采用凸显了其在微服务生态系统中的重要性。 Temporal 最初是 Uber 的 Cadence 的一个分支，由 Temporal Technologies 开发。它提供一个执行工作流的服务器，并有 Go 和 Java 的 SDK，以及用于监控的 Web UI。

rss · GitHub Trending - Go Daily · 7月8日 01:35

**背景**: 像 Temporal 这样的持久执行平台通过持久化状态，确保长期运行的工作流能够在崩溃和故障中存活。它们将应用逻辑与基础设施解耦，让开发者专注于业务规则，而平台处理重试和状态恢复。Temporal 是一项成熟的技术，在工业界被广泛使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://temporal.io/">Durable Execution Solutions | Temporal</a></li>
<li><a href="https://temporal.io/blog/what-is-durable-execution">The definitive guide to Durable Execution | Temporal</a></li>
<li><a href="https://medium.com/@surajsub_68985/temporal-revolutionizing-workflow-orchestration-in-microservices-architectures-f8265afa4dc0">Temporal : Revolutionizing Workflow Orchestration in Microservices Architectures — Part 1 | by Suraj Subramanian | Medium</a></li>

</ul>
</details>

**标签**: `#workflow orchestration`, `#distributed systems`, `#Go`, `#microservices`, `#reliability`

---

<a id="item-5"></a>
## [MoWorld：全球首个基于国产 NPU 的 50FPS 实时世界模型](https://www.36kr.com/p/3886462577094915) ⭐️ 9.0/10

中国魔芯科技联合浙江大学发布了 MoWorld，这是首个在国产 NPU（华为 Ascend 910C）上实现超过 50FPS 推理的实时交互世界模型，训练和部署全栈基于国产硬件。 该突破解决了世界模型的实时性瓶颈，以比 GPU 方案降低 70%的成本支持游戏、机器人、自动驾驶和数字孪生等应用，标志着世界模型迈向商业化的关键一步。 MoWorld 是一个 140 亿参数的 MoE 模型，运行在华为 Ascend 910C CloudMatrix384 NPU 上，支持 2000 帧长序列训练与推理，并可在 1080P 分辨率下实现完整的 6 自由度相机控制。

rss · 36氪 - 24小时热榜 · 7月8日 04:09

**背景**: 世界模型是从视频和交互数据学习环境动态的 AI 系统，但此前模型难以实现实时推理（通常 5-10FPS）。NPU（神经网络处理器）是专门用于 AI 加速的芯片，国产 NPU（如华为昇腾）旨在减少对英伟达 GPU 的依赖。MoWorld 提出了“Flash World Model”概念以实现实时部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.13678">[2510.13678] FlashWorld: High-quality 3D Scene Generation within Seconds</a></li>
<li><a href="https://www.techpowerup.com/321033/arm-china-develops-npu-accelerator-for-ai-targeting-domestic-cpus">Arm China Develops NPU Accelerator for AI, Targeting Domestic ...</a></li>
<li><a href="https://grokipedia.com/page/4D_world_model">4D world model</a></li>

</ul>
</details>

**标签**: `#world model`, `#real-time interaction`, `#NPU`, `#AI`, `#domestic hardware`

---

<a id="item-6"></a>
## [Linux 内核 KVM 高危漏洞 CVE-2026-53359 潜伏 16 年可逃逸虚拟机](https://t.me/vps_xhq/815) ⭐️ 9.0/10

Linux 内核 KVM 影子 MMU 中一个关键的释放后重用漏洞（CVE-2026-53359，代号 Januscape）被公开，允许从虚拟机逃逸到宿主机并以 root 权限执行任意代码。2026 年 6 月中旬，修复补丁已合并到 Linux 主线内核。 该漏洞对依赖 KVM 实现工作负载隔离的公有云和多租户环境构成严重威胁，因为任何拥有 root 权限的虚拟机都可以逃逸到宿主机。其隐藏 16 年未被发现凸显了审查遗留内核代码的挑战。 该漏洞同时影响 Intel 和 AMD x86 系统，在开启嵌套虚拟化时尤其危险。在 RHEL 和 CloudLinux 等将/dev/kvm 设置为全局可读写的系统上，普通本地用户无需运行业务虚拟机即可触发利用。

rss · VPS信号旗播报 - Telegram Channel · 7月8日 02:23

**背景**: KVM（基于内核的虚拟机）是 Linux 内核模块，使宿主机充当虚拟机监控器。影子 MMU 用于管理客户机内存转换；该代码中的释放后重用漏洞允许恶意虚拟机破坏宿主机内核内存，打破隔离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudlinux.com/januscape-cve-2026-53359-mitigation-and-kernel-update-on-cloudlinux/">Januscape (CVE-2026-53359): Mitigation and Kernel Update on CloudLinux - CloudLinux</a></li>
<li><a href="https://dailysecurityreview.com/resources/cve-2026-53359-januscape-16-year-kvm-flaw-enables-vm-escape/">CVE-2026-53359 Januscape: 16-Year KVM Flaw Enables VM Escape</a></li>
<li><a href="https://thecybersecguru.com/news/cve-2026-53359-januscape-kvm-guest-to-host-escape/">CVE-2026-53359 Januscape: 16-Year-Old KVM Escape Bug Explained | The CyberSec Guru</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#KVM`, `#vulnerability`, `#VM escape`, `#security`

---

<a id="item-7"></a>
## [智能体安全触发器绕过 LLM 智能体的文本护栏](https://www.reddit.com/r/MachineLearning/comments/1ur1fnz/agentic_safety_triggers_arent_textual_safety/) ⭐️ 9.0/10

研究人员证明，使用 MCP 工具访问的 LLM 智能体容易受到嵌入在工具调用序列中的攻击，这些攻击能够绕过传统的基于文本的安全护栏。即使是最先进的 DPO 和 SafeDPO 安全调优，也只能将拒绝率提高到 48%，而基础模型拒绝此类攻击的比例低于 35%。 这一发现暴露了当前 LLM 安全对齐方法的一个根本盲点，这些方法将攻击检测视为文本分类问题。随着 AI 智能体获得真实的工具访问权限，这一漏洞可能导致严重的安全漏洞，需要新的安全范式来考虑智能体行为。 攻击通过构造工具调用序列来利用已知的 CVE，这些序列表现为普通的文本请求。该研究测试了使用 MCP 文件系统 IO 的 1B–14B 参数模型，发现无需微调的方法实现了大约 3 倍于基线的拒绝率。

reddit · r/MachineLearning · /u/mlsandwich · 7月8日 18:36

**背景**: MCP 是 Anthropic 推出的开放标准，用于标准化 AI 系统与外部工具和数据源的连接方式。DPO 是一种避免显式奖励模型的 LLM 偏好调优方法，SafeDPO 则通过增强安全约束对其进行了扩展。传统护栏基于文本输入运作，但智能体系统执行的工具调用可能携带文本中不明显的攻击序列。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2305.18290">[2305.18290] Direct Preference Optimization: Your Language ... Direct Preference Optimization (DPO) of LLMs: A Paradigm Shift Direct Preference Optimization (DPO): An In-depth Analysis [2510.05703] Provably Convergent Primal-Dual DPO for ... Preference Tuning LLMs with Direct Preference Optimization ... Direct preference optimization - Microsoft Foundry</a></li>
<li><a href="https://arxiv.org/abs/2505.20065">[2505.20065] SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#AI agents`, `#MCP`, `#adversarial attacks`, `#security vulnerabilities`

---

<a id="item-8"></a>
## [解码优衣库 T 恤上的混淆 bash 脚本](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/) ⭐️ 8.0/10

一篇博客文章解码了印在优衣库与 Akamai 联名 T 恤上的一个混淆自求值 bash 脚本，揭示了其内部机制和语法错误。 这种编程谜题与时尚设计的独特结合引发了社区高度参与，凸显了代码与消费品之间的文化交融。 该脚本使用 Bash 的 eval 进行自我求值，并采用了刻意的混淆技术，但其中也存在语法错误导致无法运行。字体是 Roboto Mono，但排版并非等宽，可能是由于 InDesign 中的光学字距调整所致。

hackernews · speerer · 7月8日 08:46 · [社区讨论](https://news.ycombinator.com/item?id=48829312)

**背景**: Bash 混淆通过使用变量替换、eval 和编码等技术使脚本难以阅读。存在像 Bashfuscator 这样的工具来生成此类脚本。自求值脚本使用 eval 执行运行时构建的代码，常用于谜题或安全场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Bashfuscator/Bashfuscator">GitHub - Bashfuscator/Bashfuscator: A fully configurable and ...</a></li>
<li><a href="https://earthly.dev/blog/safely-using-bash-eval/">Bash eval: Understanding and (Safely) Using the Power of Dynamic Code Evaluation - Earthly Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了带有语法错误的 T 恤的讽刺意味，推荐了类似作品如 Martin Kleppe 的 Quine Clock，分析了字体排版问题，并分享了设计师解释故意使 OCR 困难的视频。

**标签**: `#bash`, `#obfuscation`, `#uniqlo`, `#script`, `#community-discussion`

---

<a id="item-9"></a>
## [Bun 从 Zig 重写为 Rust：更小、更快、更安全](https://bun.com/blog/bun-in-rust) ⭐️ 8.0/10

Bun JavaScript 运行时已从 Zig 重写为 Rust，二进制体积缩小了 20%，性能提升了 5%，并修复了长期存在的内存泄漏问题。 这表明对于备受关注的运行时，切换到 Rust 可以带来性能、稳定性和二进制体积方面的切实改进，可能影响系统编程中的语言选择。 二进制体积缩小源于 Rust 重写、ICU 变更以及相同代码折叠的结合。5% 的性能提升虽不大，但修复内存泄漏带来的稳定性改进意义重大。

hackernews · afturner · 7月8日 21:49 · [社区讨论](https://news.ycombinator.com/item?id=48837877)

**背景**: Bun 是一个快速的一体化 JavaScript 运行时、打包器和包管理器，最初使用 Zig 编写。Zig 是一种系统编程语言，旨在改进 C 语言，注重手动内存管理和简洁性。然而，Zig 的显式性和缺乏抽象可能导致代码冗长和潜在内存问题。Rust 是一种内存安全的系统语言，具有零成本抽象，因此对性能关键型应用具有吸引力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**社区讨论**: 社区讨论了这对 Zig 的负面影响，指出简单地重写为 Rust 就修复了内存泄漏并提高了稳定性。其他人则争论 AI 辅助重写的高昂成本，估计 API 费用超过 2.5 万美元，并质疑其与雇佣工程师相比的效率。也有人对确保正确性的严谨方法表示赞赏。

**标签**: `#Rust`, `#Zig`, `#Bun`, `#performance`, `#rewrite`

---

<a id="item-10"></a>
## [Mistral 发布 Robostral Navigate：无地图 AI 导航](https://mistral.ai/news/robostral-navigate/) ⭐️ 8.0/10

Mistral AI 发布了 Robostral Navigate，这是一个 80 亿参数的模型，仅使用单个 RGB 摄像头和自然语言指令就能让机器人在复杂环境中导航，在 R2R-CE 基准测试中达到了 76.6% 的成绩。 这标志着 Mistral 在具身 AI 领域的首个正式产品，将其从语言模型扩展到物理系统，并在无地图导航方面展示了重要里程碑，可能大幅降低自主机器人的硬件要求。 Robostral Navigate 是一个 80 亿参数的模型，不需要深度传感器、LiDAR 或多摄像头——仅需一个 RGB 摄像头和自然语言指令。它在 R2R-CE 基准测试上达到了最先进的结果，但该模型并未公开发布。

hackernews · ottomengis · 7月8日 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48832212)

**背景**: 传统机器人导航通常依赖预建地图或昂贵的传感器阵列如 LiDAR。无地图导航是指机器人在没有预先地图的情况下探索并遵循指令，这一直是个挑战，尤其是在室内。像 Robostral Navigate 这样的模型利用视觉和语言来克服这一难题，但此类技术也引发了隐私担忧，因为它可能被用于跟踪或监视。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate: single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://www.siliconreport.com/mistral-ai-releases-robostral-navigate-a-single-camera-robotics-model-95dac18d">Mistral AI Releases Robostral Navigate, a Single-Camera ...</a></li>
<li><a href="https://theaidude.net/blog/mistral-robostral-navigate-8b-single-camera-robotics-model-launch">Mistral Robostral Navigate: One Camera, 8B Params</a></li>

</ul>
</details>

**社区讨论**: 评论者对无地图能力印象深刻，提到了历史性的‘绑架机器人’问题。一些人表达了将其用于爱好者项目的兴奋，但指出该模型并未开源。另一些人则提出了隐私担忧，类似于斯坦福的 PIGEON 模型因跟踪风险而被保留。

**标签**: `#robotics`, `#AI`, `#navigation`, `#Mistral`, `#deep learning`

---

<a id="item-11"></a>
## [Cloudflare Meerkat：无领导异步共识算法](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare Research 推出了 Meerkat，一种全球分布式共识服务，实现了 QuePaxa 算法，成为首个异步共识协议的生产部署。 Meerkat 代表了分布式共识的重要进步，因为它不依赖超时机制，对网络不稳定性更有弹性，适用于全球规模系统。 基于 QuePaxa，Meerkat 是一种崩溃容错的异步共识算法，通过 hedging 和自适应领导者选择在恶劣条件下保持性能。

hackernews · bobnamob · 7月8日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=48831565)

**背景**: 传统的共识算法如 Paxos 和 Raft 是部分同步的，依赖超时机制并假设消息延迟有界。异步共识算法如 QuePaxa 不需要超时，即使在不可预测的网络条件下也能保证活性，但传统上它们太慢而无法实际使用。Meerkat 旨在证明异步共识可以足够高效地用于生产系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/meerkat-introduction/">Introducing Meerkat: an experiment in global consensus</a></li>
<li><a href="https://github.com/dedis/quepaxa">GitHub - dedis/quepaxa: This is the code repository for ...</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus QuePaxa: Escaping the Tyranny of Timeouts in Consensus QuePaxa: Escaping the tyranny of timeouts in consensus QuePaxa: Escaping the Tyranny of Timeouts in Consensus PasinduTennage/quepaxa-fork-for-internal - GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Meerkat 的无领导特性使其与 Raft 的直接比较具有误导性，因为 Raft 专为强势领导而设计。其他人则指出，每次读取都需要全局共识的权衡可能会限制使用场景。不过，也有人称赞异步算法在复杂网络中的潜力，同时提醒它尚未投入生产。

**标签**: `#distributed-systems`, `#consensus`, `#cloudflare`, `#asynchronous`, `#QuePaxa`

---

<a id="item-12"></a>
## [欧盟重振私密信息扫描规则](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/) ⭐️ 8.0/10

欧盟距离重启所谓的“Chat Control 1.0”规则仅一步之遥，该规则允许服务提供商自愿扫描非端到端加密的私密信息，以查找儿童性虐待材料。已安排程序性投票推进该法规。 这一进展重新引发了欧盟关于隐私和加密的辩论，因为它可能为允许扫描私密通信开创先例。同时，它也凸显了非端到端加密消息的自愿扫描与 Chat Control 2.0 中更具争议的强制性扫描和端到端加密禁令之间的区别。 Chat Control 1.0 仅允许扫描未受端到端加密保护的消息，例如传输中的消息（此时服务商持有密钥）。它并不强制扫描——服务商可选择实施。这与 Chat Control 2.0 不同，后者将强制要求扫描并可能实质上禁止端到端加密。

hackernews · ggirelli · 7月8日 16:53 · [社区讨论](https://news.ycombinator.com/item?id=48834296)

**背景**: Chat Control 指欧盟为打击网络儿童性虐待材料而提出的一系列法规。2022 年 5 月的初始提案（Chat Control 1.0）允许自愿扫描非端到端加密的通信。更具争议的版本（Chat Control 2.0）将强制对所有通信（包括端到端加密）进行客户端扫描，批评者认为这将破坏加密和隐私。客户端扫描是一种在用户设备上、在加密或发送之前对内容进行扫描的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.internetsociety.org/resources/doc/2020/fact-sheet-client-side-scanning/">Fact Sheet: Client-Side Scanning - Internet Society</a></li>
<li><a href="https://cointelegraph.com/news/eu-to-again-vote-to-extend-chat-control-rules">EU Again Set For Vote on ‘Chat Control’ - Cointelegraph</a></li>

</ul>
</details>

**社区讨论**: 评论者强调区分 Chat Control 1.0 和 2.0 的重要性。一位用户指出，1.0 仅允许服务商扫描非端到端加密的消息，这已是预期行为（例如 Facebook 扫描消息）。另一位用户警告说，互联网观察基金会等组织推动的客户端扫描仍然是令人担忧的问题。还有用户提供了供欧盟公民联系代表的链接。

**标签**: `#privacy`, `#EU`, `#encryption`, `#surveillance`, `#policy`

---

<a id="item-13"></a>
## [GitHub 仓库追踪泄露的 AI 系统提示词](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 8.0/10

一个名为 asgeirtj/system_prompts_leaks 的 GitHub 仓库系统性地收集并更新来自 Claude、ChatGPT、Gemini、Grok 等主要 AI 模型的泄露系统提示词，并已被《华盛顿邮报》报道。 该仓库为 AI 行为背后的隐藏指令提供了前所未有的透明度，使研究人员、开发者和公众能够理解并审核 AI 模型在后台是如何被编程的。 该仓库包含来自 Claude Fable 5、Opus 4.8、GPT-5.5 Codex、Gemini 3.5 Flash 和 Google Antigravity 等模型的提示词，并提供版本之间的差异对比，例如从 Claude Opus 4.8 到 Fable 5 的变更。

rss · GitHub Trending - Daily · 7月8日 01:32

**背景**: 系统提示词是定义 AI 模型行为、语气和推理方式的基础指令。它们通常对用户隐藏，由开发者设定以控制 AI 的响应方式。泄露的提示词揭示了这些隐藏规则，使得比较和分析不同模型的设计选择成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@david.p.lemon79/system-prompts-explained-how-ai-models-actually-work-behind-the-scenes-2265f14e3eba">System Prompts Explained: How AI Models Actually ... - Medium</a></li>
<li><a href="https://blog.promptlayer.com/system-prompt-vs-user-prompt-a-comprehensive-guide-for-ai-prompts/">System Prompt vs User Prompt in AI: What's the difference?</a></li>

</ul>
</details>

**标签**: `#AI`, `#system prompts`, `#AI safety`, `#transparency`, `#open source`

---

<a id="item-14"></a>
## [.NET 代理技能仓库发布，助力 AI 编码代理](https://github.com/dotnet/skills) ⭐️ 8.0/10

.NET 团队推出了 dotnet/skills 仓库，为 AI 编码代理提供精选的技能和插件，以辅助 .NET 和 C# 开发。该仓库包含一个用于准确性评分的仪表盘，并遵循开放的 Agent Skills 标准。 这项官方举措增强了 .NET 开发者的 AI 工具，使编码代理能够更准确地处理 .NET 特定任务，如项目升级、测试和调试。它通过提供标准化的方式来扩展 AI 代理能力，促进了生态系统的集成。 该仓库包含 12 个插件，涵盖 C# 语言服务器集成、MSBuild、NuGet、.NET MAUI、AI/ML 和测试迁移等领域。每个插件都遵循 Agent Skills 格式，该格式使用 SKILL.md 文件提供指令，并可包含脚本和其他资源。

rss · GitHub Trending - Daily · 7月8日 01:32

**背景**: Agent Skills 是一种轻量级、开放的格式，用于通过专门知识和工作流扩展 AI 代理能力。一个技能是一个包含 SKILL.md 文件的文件夹，其中包含元数据和指令。.NET 团队的精选技能旨在提高编码代理在处理 .NET 技术时的准确性和效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills</a></li>
<li><a href="https://devblogs.microsoft.com/dotnet/extend-your-coding-agent-with-dotnet-skills/">Extend your coding agent with .NET Skills - .NET Blog</a></li>

</ul>
</details>

**标签**: `#.NET`, `#C#`, `#AI agents`, `#coding agents`, `#skills`

---

<a id="item-15"></a>
## [Kyutai 发布 Pocket TTS：面向 CPU 的开源轻量级 TTS](https://github.com/kyutai-labs/pocket-tts) ⭐️ 8.0/10

Kyutai Labs 发布了 Pocket TTS，这是一个仅 1 亿参数的轻量级文本转语音模型，无需 GPU 即可在 CPU 上高效运行。它支持 Python API、命令行和浏览器推理，并具备语音克隆和多语言支持。 这大大降低了在边缘设备和个人电脑上部署 TTS 的门槛，实现了无需昂贵硬件的离线、低延迟语音合成。同时推动了 AI 语音生成领域的开源可及性。 该模型首块音频延迟约 200 毫秒，在 MacBook Air M4 上仅用 2 个 CPU 核心即可达到 6 倍实时速度。支持英语、法语、德语、葡萄牙语、意大利语和西班牙语，并计划增加更多语言。

rss · GitHub Trending - Daily · 7月8日 01:32

**背景**: 传统的文本转语音模型通常需要强大的 GPU 或云 API，限制了其在离线或资源受限环境中的使用。Pocket TTS 专门为 CPU 推理设计，适用于笔记本电脑、移动设备和基于浏览器的应用。

**标签**: `#TTS`, `#machine-learning`, `#CPU-inference`, `#open-source`, `#AI`

---

<a id="item-16"></a>
## [Anthropic 发布 Claude Agent Skills 开源仓库](https://github.com/anthropics/skills) ⭐️ 8.0/10

Anthropic 发布了一个公开的 GitHub 仓库 (anthropics/skills)，其中包含 Claude 的开源技能，包括任务特定的指令和脚本，Claude 可以动态加载这些内容以提升在专业任务上的表现。 这一发布降低了高级 AI 代理功能的使用门槛，使开发者和用户能够通过可重复的工作流程为 Claude 定制技能，涵盖创意、技术及企业任务。同时，它建立了一个开放标准（Agent Skills），该标准正在被多个 AI 平台（包括 OpenAI 和 Cursor）采用。 该仓库包含跨创意、技术和企业领域的演示技能，每个技能都放在独立的文件夹中并包含一个 SKILL.md 文件。值得注意的是，仓库中还包含了 Claude 生产级文档能力背后的文档编辑技能（docx、pdf、pptx、xlsx），这些技能采用源码可用许可而非开源许可。

rss · GitHub Trending - Python Daily · 7月8日 01:38

**背景**: Agent Skills 是一个开放标准，允许 AI 代理动态加载任务特定的指令和脚本，从而提高其在真实任务中的可靠性。该标准最初由 Anthropic 为 Claude 开发，但后来已被其他 AI 工具如 OpenAI 的 ChatGPT 和 Codex CLI、Cursor 以及 Gemini CLI 采用。skills.sh 索引作为发现技能的注册中心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/skills">GitHub - anthropics/skills: Public repository for Agent Skills</a></li>
<li><a href="https://inference.sh/blog/skills/agent-skills-overview">Agent Skills: The Open Standard for AI Capabilities | blog | inference.sh</a></li>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub</a></li>

</ul>
</details>

**标签**: `#Agent Skills`, `#Claude`, `#Anthropic`, `#AI Tooling`, `#GitHub`

---

<a id="item-17"></a>
## [n8n：开源 AI 工作流自动化平台](https://github.com/n8n-io/n8n) ⭐️ 8.0/10

n8n 现已支持超过 1500 个集成和原生 AI 代理功能，用于构建和部署 AI 工作流，结合了可视化构建与自定义代码。 这提供了一个开源、可自行托管的替代方案，让开发者能够在完全掌控数据和基础设施的情况下将 AI 集成到工作流中。 n8n 采用 Sustainable Use License（公平代码）许可，源代码可见且可自行托管，但商业使用可能受限。它支持连接多种 AI 模型，包括 OpenAI、Anthropic、Google 以及开源模型。

rss · GitHub Trending - TypeScript Daily · 7月8日 01:41

**背景**: n8n 是一款公平代码工作流自动化平台，与 Zapier 和 Make 等工具竞争。公平代码许可证允许访问和修改源代码，但禁止某些商业用途，如将软件作为付费服务提供。该模式旨在平衡开放性与可持续性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fair_License">Fair License - Wikipedia</a></li>
<li><a href="https://faircode.io/">Fair-code</a></li>

</ul>
</details>

**标签**: `#workflow automation`, `#AI agents`, `#open-source`, `#integration`, `#fair-code`

---

<a id="item-18"></a>
## [Dynamo：开源数据中心级推理服务框架](https://github.com/ai-dynamo/dynamo) ⭐️ 8.0/10

Dynamo 是一个开源的数据中心级分布式推理服务框架，已在 GitHub 上发布。它协调多个推理引擎（如 vLLM），通过分离式服务和智能路由等功能实现多节点推理的协同。 随着大语言模型和多模态 AI 扩展到多 GPU 和多节点，高效的分布式推理变得至关重要。Dynamo 提供了统一的编排层，可以最大化吞吐量并最小化延迟，可能降低 AI 部署的基础设施成本。 Dynamo 使用 Rust 实现性能关键部分，Python 实现可扩展性，与 vLLM、SGLang 和 TensorRT-LLM 等推理引擎集成而不替代它们。它包含 KV 感知路由、多令牌预测和分离式预填充/解码，并为 Nemotron 3 Ultra 等模型提供了预构建的 recipes。

rss · GitHub Trending - Rust Daily · 7月8日 01:39

**背景**: 分布式推理服务涉及在多个 GPU 或节点上部署大型 AI 模型，需要协调并行处理和资源管理。传统框架通常专注于单节点或简单的多节点设置，但数据中心级工作负载需要高级编排。Dynamo 通过充当现有推理引擎之上的编排层来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/v0.8.0/serving/distributed_serving.html">Distributed Inference and Serving — vLLM</a></li>

</ul>
</details>

**标签**: `#distributed inference`, `#AI infrastructure`, `#Rust`, `#deep learning`, `#serving framework`

---

<a id="item-19"></a>
## [uv：用 Rust 编写的快速 Python 包管理器](https://github.com/astral-sh/uv) ⭐️ 8.0/10

Astral 发布了 uv，这是一个用 Rust 编写的极速 Python 包和项目管理器，声称比 pip 快 10-100 倍，并能替代 pip、poetry、pyenv、virtualenv 等多种工具。 uv 通过 Rust 实现大幅提升了 Python 依赖管理的性能，有望减少开发者的等待时间并改进 CI/CD 流水线，同时其一体化方案简化了工具链的复杂性。 uv 提供与 pip 兼容的接口、通用锁文件、支持内联依赖的脚本执行、Python 版本管理、Cargo 风格的工作区以及全局缓存以节省磁盘空间。可以通过独立脚本或 pip 安装，支持 macOS、Linux 和 Windows。

rss · GitHub Trending - Rust Daily · 7月8日 01:39

**背景**: Python 包管理传统上使用 pip 安装包，但性能瓶颈和工具碎片化（例如 poetry 用于依赖解析，pyenv 用于版本管理）催生了创新。Rust 是一种以性能和安全著称的系统编程语言，成为重新实现开发者工具的热门选择。

**标签**: `#Python`, `#Rust`, `#package manager`, `#developer tools`

---

<a id="item-20"></a>
## [微软 windows-rs：Rust 的 Windows API 绑定](https://github.com/microsoft/windows-rs) ⭐️ 8.0/10

微软发布了 windows-rs，这是一组 Rust crate，为 Windows API 提供绑定，使 Rust 开发者能直接从 Rust 调用过去、现在和未来的 Windows 功能。 该项目大大降低了 Rust 开发者在 Windows 上开发的障碍，使构建利用原生 Windows API 的系统应用和库更加容易。它巩固了 Rust 在 Windows 系统编程中的地位。 该 crate 系列包括用于错误处理、字符串、COM/WinRT 支持、集合等的专注 crate，允许开发者仅依赖所需部分。更广泛的 windows 和 windows-sys crate 通过按命名空间的功能提供对整个 Windows API 的访问。

rss · GitHub Trending - Rust Daily · 7月8日 01:39

**背景**: 在编程中，crate 是 Rust 的包或库。外部函数接口（FFI）允许一种语言编写的代码调用另一种语言编写的函数。windows-rs 使用 FFI 将 Rust 绑定到 Windows API，这些 API 通常以 C 风格函数暴露。这使得 Rust 无需编写单独的 C/C++包装器即可利用庞大的 Windows 生态系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html">Packages and Crates - The Rust Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foreign_function_interface">Foreign function interface - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Windows`, `#FFI`, `#Microsoft`, `#Systems Programming`

---

<a id="item-21"></a>
## [腾讯开源 WeKnora：集成 RAG、自主代理与维基的知识平台](https://github.com/Tencent/WeKnora) ⭐️ 8.0/10

腾讯开源了 WeKnora，该平台能将原始文档转化为可查询的 RAG 系统、自主推理的 ReAct 代理以及自我维护的维基知识库。 作为一家大型科技公司的企业级框架，WeKnora 提供了一个集检索、推理与知识库自动维护于一体的开源知识管理方案，有望降低构建自定义 AI 知识系统的成本与复杂度。 WeKnora 支持从飞书、Notion 和语雀等源导入数据，处理 10 余种文档格式，集成 20 多种 LLM 提供商，提供多租户 RBAC 权限管理，并支持完全自托管。

rss · GitHub Trending - Go Daily · 7月8日 01:35

**背景**: RAG（检索增强生成）通过在生成答案前检索相关文本来增强大语言模型。ReAct 模式（推理+行动）使代理能够使用工具并执行多步推理。由 Andrej Karpathy 推广的自我维护维基概念，利用 LLM 持续从原始源构建和更新结构化知识库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent/WeKnora">WeKnora - GitHub</a></li>
<li><a href="https://weknora.online/">WeKnora - LLM-powered Document Understanding & RAG Framework</a></li>

</ul>
</details>

**标签**: `#LLM`, `#RAG`, `#Open Source`, `#Knowledge Management`, `#AI Platform`

---

<a id="item-22"></a>
## [SOPS：一个简单灵活的密钥管理工具](https://github.com/getsops/sops) ⭐️ 8.0/10

SOPS 是一个开源加密文件编辑器，支持 YAML、JSON、ENV、INI 和二进制格式，并集成多种密钥管理系统，包括 AWS KMS、GCP KMS、Azure Key Vault、华为云 KMS、age 和 PGP。 SOPS 简化了 DevOps 工作流中的密钥管理，允许团队直接在配置文件中加密密钥，既确保安全又不牺牲便利性。其对多种后端的支持使其适用于各种云环境。 SOPS 最初于 2015 年在 Mozilla 创建，现已成为 CNCF 沙箱项目。它基于 Mozilla 公共许可证 2.0 版，并推荐使用 age 作为加密工具。

rss · GitHub Trending - Go Daily · 7月8日 01:35

**背景**: 在现代化应用开发中，密钥管理至关重要，以避免将 API 密钥和密码等敏感信息以明文形式存储。SOPS 提供了一种加密这些密钥的方法，同时将其保留在版本控制中，利用主要云提供商或开源工具（如 age 和 PGP）的密钥管理服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/FiloSottile/age">GitHub - FiloSottile/age: A simple, modern and secure ...</a></li>
<li><a href="https://support.huaweicloud.com/intl/en-us/bestpractice-dew/dew_06_0003.html">Overview_Using KMS to Encrypt and Decrypt Data for Cloud ...</a></li>

</ul>
</details>

**标签**: `#secrets-management`, `#encryption`, `#DevOps`, `#security-tools`

---

<a id="item-23"></a>
## [LocalAI：开源 AI 引擎，无需 GPU 即可在任何硬件上运行模型](https://github.com/mudler/LocalAI) ⭐️ 8.0/10

LocalAI 是一个开源 AI 引擎，可以在无需 GPU 的情况下，在任何硬件上运行各种 AI 模型，包括大语言模型、视觉、语音、图像和视频模型。它提供了可组合、优先保护隐私的平台，并兼容 OpenAI、Anthropic 和 ElevenLabs 的 API。 该项目大幅降低了本地运行 AI 模型的门槛，为没有高端硬件的用户提供了隐私保护和可及性。它挑战了对云端 AI 服务的依赖，并加速了边缘计算的普及。 LocalAI 采用模块化架构，像 llama.cpp、vLLM 和 whisper.cpp 这样的后端按需拉取，用户只需安装需要的组件。它支持多种硬件平台，包括 NVIDIA、AMD、Intel、Apple Silicon、Vulkan 以及仅 CPU 环境，并具备多用户身份验证和内置 AI 代理功能。

rss · GitHub Trending - Go Daily · 7月8日 01:35

**背景**: 大多数 AI 模型需要强大的 GPU 才能高效推理，这使得许多用户难以本地部署。传统的云端 API 集中处理数据，引发了隐私问题。LocalAI 通过利用优化的推理引擎在 CPU 和各种加速器上运行，解决了这些问题，实现了私密、离线的 AI 使用。

**标签**: `#AI`, `#open-source`, `#local inference`, `#edge computing`, `#Go`

---

<a id="item-24"></a>
## [Meta 研发‘超级感知’智能眼镜，可持续录音自动拍照](https://www.ithome.com/0/974/288.htm) ⭐️ 8.0/10

Meta 正在开发一款内部称为‘超级感知’的 AI 智能眼镜原型，该设备可以持续录音并每隔几秒自动拍照，且不会点亮镜框上的 LED 录制指示灯。 这引发了严重的隐私担忧，因为旁观者可能不知道他们正在被记录。这标志着向全天候可穿戴人工智能迈出了一步，但可能面临监管和公众的强烈反对。 在 AI 功能使用期间，LED 指示灯会保持熄灭，仅在用户主动保存照片或视频时才会亮起。Meta 还讨论不存储原始数据，而是提取元数据供 AI 查询，以减少隐私风险。

rss · IT之家 · 7月8日 23:36

**背景**: Meta 已经在销售具备摄像头和音频功能的 Ray-Ban Meta 智能眼镜。之前的隐私问题包括人脸识别代码被发现以及第三方提供的 LED 指示灯移除服务，突显了人们对秘密录制的持续担忧。

**标签**: `#smart glasses`, `#AI`, `#privacy`, `#Meta`, `#wearable tech`

---

<a id="item-25"></a>
## [SpaceXAI 发布 Grok 4.5：与 Cursor 联合训练的编程 AI 模型](https://www.ithome.com/0/974/278.htm) ⭐️ 8.0/10

SpaceXAI 发布了其首个专注编程的 AI 模型 Grok 4.5，该模型与 AI 代码编辑器 Cursor 联合训练。据称相比领先竞品，效率提升一倍，成本降低一半。 这一进展可能显著降低软件工程任务的成本和时间，使先进的 AI 辅助编程更加普及。它也突显了针对代理编程任务的专用 AI 模型趋势。 Grok 4.5 在数万个 NVIDIA GB300 GPU 上训练，输出速度达到每秒 80 个 token，每个任务消耗的 token 仅为同类模型的一半。定价为每百万输入 token 2 美元，每百万输出 token 6 美元。

rss · IT之家 · 7月8日 22:51

**背景**: Cursor 是一个 AI 原生代码编辑器，利用自然语言进行代码生成、编辑和调试。NVIDIA GB300 是为 AI 训练和推理设计的高性能 GPU。编程 AI 中的代理任务涉及使用多种工具和技能进行多步骤软件工程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://builtin.com/articles/what-is-cursor-ai">What Is Cursor? AI Code Editor Explained | Built In</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">NVIDIA GB300 NVL72</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#Large Language Models`, `#Code Generation`, `#Software Engineering`, `#Grok`

---

<a id="item-26"></a>
## [Anthropic 利润超 10 亿美元，秘密提交 IPO](https://www.ithome.com/0/974/275.htm) ⭐️ 8.0/10

SemiAnalysis 报告称，Anthropic 预计在 2026 年第三季度利润超过 10 亿美元，并于 2026 年 6 月 1 日秘密提交了 IPO 申请。 这标志着 AI 实验室的重要里程碑，Anthropic 的盈利能力和 IPO 可能迫使 OpenAI 公开财务状况并加速筹集 AI 基础设施所需资金。 Anthropic 和 OpenAI 的合计年经常性收入（ARR）已接近 1000 亿美元，Anthropic 的 Claude Code 推动了 B2B 业务的强劲增长。SemiAnalysis 估计，如果执行顺利，其市值可能达到 6 万亿美元。

rss · IT之家 · 7月8日 22:30

**背景**: SemiAnalysis 是一家专注于 AI 和半导体的独立研究公司。其 Tokenomics 模型按 SKU 和客户层级分析 AI 经济性。Anthropic 是由前 OpenAI 员工创立的 AI 公司，专注于安全 AI 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://semianalysis.com/about/">About – SemiAnalysis</a></li>
<li><a href="https://finance.biggo.com/news/KPbYnp0BvthpMgHBApty">29-Year-Old Founder Builds AI Research Empire SemiAnalysis ...</a></li>
<li><a href="https://www.cloudzero.com/blog/claude-code-pricing/">Claude Code Pricing In 2026: Plans, Token Costs, And Costs</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#financial performance`, `#Claude Code`

---

<a id="item-27"></a>
## [索尼因停售实体游戏光盘面临 40 亿欧元集体诉讼](https://www.ithome.com/0/974/246.htm) ⭐️ 8.0/10

荷兰消费者组织 Stichting Massaschade & Consument 已对索尼提起集体诉讼，索赔超过 4 亿欧元，代表 170 万荷兰玩家，反对索尼计划在 2028 年前停止生产实体游戏光盘。 此次诉讼挑战了索尼向纯数字化的转型，指控其在游戏定价和所有权方面形成垄断，可能为整个游戏行业的数字分发实践和消费者权益树立先例。 该诉讼称，没有实体光盘后，索尼将对第一方游戏定价和所有权拥有垄断权，因为数字版游戏仅为使用许可而非实际拥有。这是索尼因数字市场主导地位面临的第二起法律纠纷，两个月前刚在加州以 800 万美元达成和解。

rss · IT之家 · 7月8日 13:17

**背景**: 实体游戏光盘允许玩家购买、出售和交易二手游戏，促进了竞争性的二级市场。纯数字发行消除了这一选择，将玩家锁定在平台运营商的商店和定价体系中。消费者组织认为这限制了自由，可能导致价格上涨，如同其他数字市场中看到的那样。

**标签**: `#Sony`, `#lawsuit`, `#digital-only`, `#gaming`, `#consumer rights`

---

<a id="item-28"></a>
## [Cloudflare 与 OpenAI 启动试点，利用网络信号优化 AI 搜索](https://www.ithome.com/0/974/235.htm) ⭐️ 8.0/10

Cloudflare 与 OpenAI 启动了一项研究试点，Cloudflare 从其承载全球超过 20%网络流量的网络中分享实时网络信号（包括内容时效性、流量质量和页面变动），旨在提升 AI 搜索索引和回答的准确性。 此次合作利用 Cloudflare 全球网络的独特真实网页数据，解决 AI 搜索在时效性和内容质量方面的关键挑战，有望为用户提供更准确、更新的答案，并可能为互联网基础设施公司与 AI 企业的合作树立先例。 试点项目聚焦于信号驱动的爬取和索引技术，利用 Cloudflare 对页面变动和流量模式的洞察来指导 OpenAI 的搜索索引。OpenAI 贡献其先进模型、大规模搜索系统以及真实用户查询数据用于测试。

rss · IT之家 · 7月8日 12:39

**背景**: AI 搜索引擎依赖爬取网页来索引内容以回答查询。传统的爬取可能遗漏实时更新或优先处理低质量内容。信号驱动的爬取利用网络层面的指标（如内容新鲜度和流量质量）来指导索引，有望使 AI 回答更准确、更新。Cloudflare 的网络承载全球超过 20%的互联网流量，为获取这些信号提供了独特的视角。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rallies.ai/news/cloudflare-launches-openai-pilot-using-signals-from-20-of-web-traffic">Cloudflare Launches OpenAI Pilot Using Signals from 20% of ...</a></li>
<li><a href="https://seekingalpha.com/news/4612227-cloudflare-openai-team-up-to-launch-research-pilot-for-ai-search-indexing">Cloudflare, OpenAI launch research pilot for AI search indexing</a></li>

</ul>
</details>

**标签**: `#Cloudflare`, `#OpenAI`, `#AI search`, `#network insights`, `#indexing`

---

<a id="item-29"></a>
## [LingBot-Video：开源 13B 稀疏 MoE 视频扩散世界模型](https://www.reddit.com/r/MachineLearning/comments/1ur0bxq/lingbotvideo_sparsemoe_video_diffusion/) ⭐️ 8.0/10

LingBot-Video 是一个拥有 130 亿参数的稀疏混合专家（MoE）视频扩散变压器，仅有 14 亿活跃参数，通过包含物理合理性在内的六项奖励的强化学习进行后训练，并以开源形式发布，作为机器人学的动作条件世界模型。 该模型通过使用带有 VLM 判断物理奖励的强化学习，推动了视频生成与世界模型之间的界限，其开源发布使更广泛的研究能够探索用于机器人学和仿真的可扩展、物理合理的视频预测。 该模型采用单流扩散变压器，使用 DeepSeek-V3 风格的稀疏 MoE（128 个专家，top-8 路由，130 亿总参数中 14 亿活跃），并包含一个动作到视频模式，可根据动作和手部姿势条件预测机器人 rollout，代码和权重已在 GitHub 和 Hugging Face 上开源。

reddit · r/MachineLearning · /u/Savings-Display5123 · 7月8日 17:58

**背景**: 稀疏混合专家（MoE）是一种神经网络架构，每个输入仅激活部分参数（专家），从而实现大总容量和较低的计算成本。DeepSeek-V3 以 671B 总参数和每 token 37B 活跃参数推广了这种方法。视频扩散变压器通过迭代去噪随机噪声，以文本或其他输入为条件生成视频。强化学习（RL）后训练针对特定奖励优化模型；在这里，视觉语言模型（VLM）评估物理合理性。世界模型旨在模拟环境动态以进行规划，与仅生成合理视频而无交互控制的文本到视频生成不同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.19437">[2412.19437] DeepSeek-V3 Technical Report - arXiv.org GitHub - deepseek-ai/DeepSeek-V3 Model Architecture Overview | deepseek-ai/DeepSeek-V3 | DeepWiki deepseek-ai/DeepSeek-V3.2 · Hugging Face GitHub - RushilJ2603/DeepSeek-V3-Sparse-MoE-Architecture ...</a></li>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance ...</a></li>
<li><a href="https://arxiv.org/abs/2505.02018">[2505.02018] R-Bench: Graduate-level Multi-disciplinary ... RBench: Graduate-level Multi-disciplinary Benchmarks for LLM ... [2505.16770] RBench-V: A Primary Assessment for Visual ... README.md · R-Bench/R-Bench at main - Hugging Face R-Bench/R-Bench-V · Datasets at Hugging Face GitHub - rbenchmark/benchmarks: Collections of Benchmarks of ... RBench-V: A Primary Assessment for Visual Reasoning Models ...</a></li>

</ul>
</details>

**社区讨论**: 帖子作者邀请批判性讨论，质疑 VLM 是否是可靠的物理判断者（存在奖励作弊风险），以及视频生成与世界模型之间的界限在哪里，因为该模型尽管在 RBench 上获得了平均最高分，但缺乏闭环机器人结果。

**标签**: `#sparse MoE`, `#video diffusion`, `#world model`, `#reinforcement learning`, `#robotics`

---

<a id="item-30"></a>
## [DeepSeek 自主研发 AI 推理芯片以减少供应商依赖](https://t.me/zaihuapd/42423) ⭐️ 8.0/10

据三位知情人士透露，中国 AI 公司 DeepSeek 已开始自主研发 AI 推理芯片，旨在减少对英伟达和华为芯片的依赖。该项目启动约一年，目前仍处于早期阶段，公司正在招聘芯片设计工程师。 此举可能在美国出口管制背景下重塑 AI 芯片供应链，使 DeepSeek 更好地控制推理成本和硬件路线图。如果成功，可能激励其他中国 AI 公司自主研发芯片，加速中国本土半导体解决方案的进程。 该芯片专注于推理阶段，即已训练好的模型为用户生成回答的环节，而非训练阶段。DeepSeek 已开始与芯片设计、代工和存储公司接洽，并在近几个月私下大量招募芯片设计工程师。

telegram · zaihuapd · 7月8日 05:20

**背景**: DeepSeek 此前依赖英伟达 H800 和华为昇腾芯片，但美国出口管制限制了先进英伟达 GPU 的获取。与训练芯片不同，AI 推理芯片优化的是每 token 成本、延迟和能效，因此对于大规模部署具有吸引力。推理芯片市场预计将大幅增长，到 2026 年将占 AI 加速器市场的 60-70%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.granitefirm.com/blog/us/2025/08/24/ai-inference-chips/">AI inference chips vs. training chips - Andy Lin's Long-term ...</a></li>
<li><a href="https://www.naddod.com/ai-insights/inference-chip-guide-the-foundation-of-scalable-ai-applications">Inference Chip Guide: The Foundation of Scalable AI ...</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/h800-pcie-80-gb.c4181">NVIDIA H800 PCIe 80 GB Specs | TechPowerUp GPU Database</a></li>

</ul>
</details>

**标签**: `#AI`, `#semiconductor`, `#DeepSeek`, `#chip design`, `#geopolitics`

---

<a id="item-31"></a>
## [阿里巴巴下令全员卸载 Claude](https://t.me/zaihuapd/42424) ⭐️ 8.0/10

阿里巴巴已下令所有员工卸载 Anthropic 旗下的 Claude 及相关产品，包括 Sonnet、Opus、Fable 模型和 Claude Code，该禁令将于 2026 年 7 月 10 日生效。 这标志着 AI 企业紧张局势的重大升级，一家中国顶级科技公司因涉嫌账户滥用而禁用领先的美国 AI 模型，凸显了 AI 行业日益增长的安全和竞争压力。 此前 Anthropic 指控阿里巴巴在 2026 年 4 月 22 日至 6 月 5 日期间使用约 2.5 万个虚假账户与 Claude 交互超过 2800 万次，随后加强了风控策略，禁令正是在此背景下发布。

telegram · zaihuapd · 7月8日 06:09

**背景**: Claude 是 Anthropic 公司开发的一系列大语言模型，包括 Sonnet、Opus、Fable 等不同能力的版本。模型蒸馏是一种通过大量查询让小型模型学习大型模型能力的技术。阿里巴巴此前曾报销员工使用 Claude、GPT、Gemini 等外部模型的费用，但该政策现已逆转。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>
<li><a href="https://code.claude.com/docs/en/sub-agents">Create custom subagents - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#Alibaba`, `#Claude`, `#Anthropic`, `#Ban`

---

<a id="item-32"></a>
## [安卓远程 Root 漏洞链'IonStack'威胁所有版本](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

Nebula Security 的安全研究人员公开了'IonStack'——首个公开的概念验证漏洞链，通过点击一个恶意链接即可远程获得 Android 17 及以下版本设备的完全 Root 权限。 该漏洞链展示了绕过 Android 沙箱并实现持久 Root 访问的远程代码执行路径，影响数十亿设备，构成直接安全威胁。 该漏洞链结合了 Mozilla Firefox 浏览器漏洞（影响 151.0.2 及更早版本）和一个存在 15 年的 Linux 内核漏洞，利用后攻击者可通过 ADB 获得持久 Root 权限。Linux 内核已修复，但完整漏洞细节暂未公开以便厂商响应。

telegram · zaihuapd · 7月8日 13:01

**背景**: Android 设备通常运行在 Linux 内核上，系统安全依赖于通过 SELinux 和应用程序隔离实现的沙箱机制。Root 访问权限可完全控制设备，标准 Android 系统不允许在未解锁引导加载程序的情况下获得此权限。该漏洞链仅通过点击链接即实现 Root，属于严重权限提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://cyberpress.org/ionstack-attack-full-control-android/">IonStack Attack Lets Hackers Gain Full Control of Android ...</a></li>

</ul>
</details>

**标签**: `#Android`, `#Security`, `#Vulnerability`, `#Root`, `#Linux kernel`

---

<a id="item-33"></a>
## [通过泄漏电磁信号识别手机应用，准确率高达 99%](https://www.scmp.com/news/china/science/article/3359688/chinese-researchers-find-peephole-any-smartphone-its-leaked-radio-signal) ⭐️ 8.0/10

中国人民公安大学的研究人员开发了一种非接触式取证技术，通过分析手机运行时泄漏的低频电磁信号来识别正在使用的应用程序，在 iPhone 15 Pro、小米 15 Pro 和 OPPO Reno 13 上测试准确率高达 99.07%。 该技术即使设备处于离线、飞行模式、加密或锁定状态也能工作，带来了重大的隐私和安全风险，可能被用于隐蔽监视或在无需物理接触的情况下收集取证证据。 该方法分析低频电磁辐射，无需访问设备的操作系统或存储数据，并能区分应用内的具体操作（如微信视频通话、抖音浏览）。该研究于 2026 年 5 月 22 日发表在同行评审期刊《无线电工程》上。

telegram · zaihuapd · 7月8日 16:05

**背景**: 侧信道攻击利用电子设备运行时产生的物理泄漏，如电磁辐射、功耗或时间延迟，来窃取敏感信息。电磁侧信道攻击是非侵入性的，可以使用探头和示波器远程实施。这项研究将电磁攻击扩展到识别智能手机上正在运行的应用程序，通过匹配每个应用或操作的独特电磁特征来实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ckhq.net/html/6c1af61946e47994a7d682373d5f7757.html">中国科研团队研发非接触式智能手机应用识别技术，准确率达99.07%</a></li>
<li><a href="https://www.msn.cn/zh-cn/技术/硬件和设备/手机关机也没用-中国科学家发现新型电磁-透视术-让隐私无处遁形/ar-AA27u7GB">手机关机也没用？中国科学家发现新型电磁“透视术”让隐私无处遁形</a></li>

</ul>
</details>

**标签**: `#security`, `#privacy`, `#electromagnetic emissions`, `#smartphone`, `#research`

---