---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> 从 306 条内容中筛选出 28 条重要资讯。

---

1. [ZLUDA：非 NVIDIA GPU 的 CUDA 直接替代方案](#item-1) ⭐️ 9.0/10
2. [DeepSeek 以 MIT 许可证开源 DSpark 和 DeepSpec](#item-2) ⭐️ 9.0/10
3. [Linux 6.9 回归：LUKS 挂起无法擦除加密密钥](#item-3) ⭐️ 8.0/10
4. [PeerTube：去中心化、联邦制的 YouTube 替代品](#item-4) ⭐️ 8.0/10
5. [Immich 3.0：自托管照片平台重大更新](#item-5) ⭐️ 8.0/10
6. [西班牙下令将 Palantir 列入公私企业黑名单](#item-6) ⭐️ 8.0/10
7. [Strix：开源 AI 渗透测试工具发布](#item-7) ⭐️ 8.0/10
8. [Meta 开源 Astryx 设计系统，支撑内部 13,000+ 应用](#item-8) ⭐️ 8.0/10
9. [Allen AI 发布 olmOCR 工具包，用于 PDF 转文本](#item-9) ⭐️ 8.0/10
10. [VulnClaw：AI 驱动的 CLI 工具，通过自然语言自动化渗透测试](#item-10) ⭐️ 8.0/10
11. [Open WebUI：支持多种 LLM 后端的用户友好界面](#item-11) ⭐️ 8.0/10
12. [Maigret：一款可扫描 3000 多个网站查找用户名痕迹的 OSINT 工具](#item-12) ⭐️ 8.0/10
13. [Chrome DevTools MCP 服务器让 AI 代理控制浏览器](#item-13) ⭐️ 8.0/10
14. [Polars：基于 Rust 的超高速 DataFrame 库](#item-14) ⭐️ 8.0/10
15. [Awesome Rust：精选 Rust 资源列表](#item-15) ⭐️ 8.0/10
16. [Kueue：面向批处理工作负载的 Kubernetes 原生作业队列](#item-16) ⭐️ 8.0/10
17. [Meta 计算：人人都想成为云](#item-17) ⭐️ 8.0/10
18. [ECTC 2026 综述：EMIB-T、HBM4、冷却、光子互连](#item-18) ⭐️ 8.0/10
19. [铠侠-闪迪 BiCS10 332 层 3D NAND 进入出样](#item-19) ⭐️ 8.0/10
20. [特斯拉司机因 FSD 致命车祸被控过失杀人，数据显示其人为干预](#item-20) ⭐️ 8.0/10
21. [快手 AI 子公司可灵获最高 30 亿美元融资](#item-21) ⭐️ 8.0/10
22. [企业 AI 成本失控，花旗、Adobe 等限制员工使用大模型](#item-22) ⭐️ 8.0/10
23. [针对 Microsoft 365 的密码喷洒攻击利用 Azure CLI](#item-23) ⭐️ 8.0/10
24. [微软斥资 25 亿美元成立新公司助力企业 AI 落地](#item-24) ⭐️ 8.0/10
25. [Meta 进军云计算引发 AI 基础设施股暴跌](#item-25) ⭐️ 8.0/10
26. [Cloudflare 9 月起默认拦截混合用途 AI 爬虫，含谷歌](#item-26) ⭐️ 8.0/10
27. [OpenAI 提议美国政府持股 5%，或纳入 Google、Meta](#item-27) ⭐️ 8.0/10
28. [PS3 商店 2027 关闭引发紧急游戏存档](#item-28) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ZLUDA：非 NVIDIA GPU 的 CUDA 直接替代方案](https://github.com/vosen/ZLUDA) ⭐️ 9.0/10

ZLUDA 是一个开源的 CUDA 直接替代方案，允许未经修改的 CUDA 应用程序在 AMD、Intel 等非 NVIDIA GPU 上以接近原生性能运行。该项目最近新增了对 CUDA 13.1 的兼容性，并完全支持在非 NVIDIA 硬件上运行 Llama.cpp。 这打破了 NVIDIA 在 CUDA 软件上的长期垄断，为 AI/ML 和科学计算等工作负载提供了更广泛的 GPU 选择。它显著降低了供应商锁定风险，并可能加速替代 GPU 硬件的采用。 ZLUDA 通过将 CUDA API 调用转换为目标 GPU 的原生计算 API（如 AMD ROCm 或 Intel Level Zero）来实现接近原生的性能。2024 年 12 月的 v4 版本将支持范围从 AMD GPU 扩展到 Intel GPU，最新版本的目标是 CUDA 13.1。

rss · GitHub Trending - Rust Daily · 7月2日 01:47

**背景**: CUDA 是 NVIDIA 专有的并行计算平台和 API，广泛应用于深度学习、科学计算和高性能计算。在 ZLUDA 出现之前，在非 NVIDIA GPU 上运行基于 CUDA 的应用程序需要手动将代码移植到 OpenCL 或 AMD ROCm 等替代方案，这既耗时又不完整。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://itsfoss.gitlab.io/post/zluda-boasts-full-llamacpp-support-better-windows-handling-for-cuda-on-non-nvidia-gpus/">ZLUDA Boasts Full Llama.cpp Support Better Windows... :: IT'S FOSS</a></li>
<li><a href="https://www.topcpu.net/en/news/open-source-cuda-simulation-project-zluda-achieves-breakthrough-progress">Open Source CUDA Simulation Project ZLUDA Achieves Breakthrough...</a></li>
<li><a href="https://www.phoronix.com/news/ZLUDA-CUDA-13.1-Compatibility">ZLUDA Adds CUDA 13.1 Compatibility For Running... - Phoronix</a></li>

</ul>
</details>

**标签**: `#CUDA`, `#GPU`, `#Open Source`, `#Compute`

---

<a id="item-2"></a>
## [DeepSeek 以 MIT 许可证开源 DSpark 和 DeepSpec](https://www.36kr.com/p/3877109219406081) ⭐️ 9.0/10

2025 年 6 月 28 日，DeepSeek 以宽松的 MIT 许可证开源了推理加速框架 DSpark 以及用于训练和评估推测解码算法的全栈代码库 DeepSpec，同时还在 Hugging Face 上发布了增强后的模型权重 DeepSeek-V4-Pro-DSpark 和 DeepSeek-V4-Flash-DSpark。 此次发布凸显了 DeepSeek 对开源的特殊承诺，与 OpenAI、Meta 等其他主要 AI 实验室的限制性做法形成鲜明对比。通过免费提供方法论和实现，DeepSeek 赋能全球开发者社区利用尖端加速技术，可能加速推测解码的采用并促进进一步创新。 据报道，DSpark 可将 DeepSeek-V4 推理速度提升高达 85%。DeepSpec 包含三种草稿模型算法、一篇研究论文以及数据准备、训练和评估工具，全部采用 MIT 许可证，允许无限制商业使用。

rss · 36氪 - 24小时热榜 · 7月2日 01:48

**背景**: 推测解码是一种推理优化技术，通过让小模型（草稿模型）预测多个 token，然后由主模型并行验证，从而降低延迟并保持输出质量，以加速大型语言模型（LLM）。MIT 许可证是一种宽松的开源许可证，允许用户自由使用、修改和分发代码，包括用于商业用途。DeepSeek 此次发布包含了加速框架（DSpark）和完整的训练/评估流程（DeepSpec），使其他人能够在其自己的模型上实现推测解码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://venturebeat.com/orchestration/deepseek-open-sources-dspark-a-new-framework-to-speed-up-llm-inference-by-up-to-85">DeepSeek open sources DSpark, a new framework to speed up LLM ...</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSpec">GitHub - deepseek-ai/ DeepSpec : DeepSpec : a full-stack codebase for...</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>

</ul>
</details>

**社区讨论**: 社区反应极为积极，中国社交媒体用户称梁文锋为“活菩萨”和“圣人”，国际观察者如 Teortaxes 则称赞 DeepSeek 的“浩瀚的慷慨”。普遍情绪认为 DeepSeek 正在为 AI 领域的开放设定新标准，与 OpenAI 和 Meta 等更为限制性的玩家形成鲜明对比。

**标签**: `#DeepSeek`, `#open source`, `#AI`, `#LLM`, `#community`

---

<a id="item-3"></a>
## [Linux 6.9 回归：LUKS 挂起无法擦除加密密钥](https://mathstodon.xyz/@iblech/116769502749142438) ⭐️ 8.0/10

自 Linux 内核 6.9（2024 年 5 月发布）起，`cryptsetup luksSuspend` 命令在系统挂起期间不再从内存中擦除磁盘加密密钥，该回归问题是通过 NixOS 测试发现的。 此回归削弱了依赖 luksSuspend 在挂起期间保护密钥的 Linux 系统的磁盘加密安全性，尤其是使用可选 cryptsetup-suspend 插件的 Debian 用户。若不擦除密钥，拥有物理访问权限的攻击者可能从 RAM 中提取主密钥。 此回归未被注意是因为系统仍正常运行——加密密钥保留在内存中，因此恢复时不会提示输入密码。该 bug 在 Linux 6.9 中引入，影响主要被 Debian 使用的 `cryptsetup luksSuspend` 命令。

hackernews · IngoBlechschmid · 7月2日 15:25 · [社区讨论](https://news.ycombinator.com/item?id=48763035)

**背景**: LUKS（Linux 统一密钥设置）是磁盘加密的标准。当系统挂起到 RAM 时，加密主密钥通常保留在内核内存中。`luksSuspend` 命令旨在挂起时擦除该密钥，强制在恢复时重新输入密码。此功能由 Debian 通过可选插件首创，但并非官方 cryptsetup 上游的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48763035">Since Linux 6.9, LUKS suspend stopped wiping disk-encryption ...</a></li>
<li><a href="https://www.man7.org/linux//man-pages/man8/cryptsetup-luksSuspend.8.html">cryptsetup-luksSuspend (8) - Linux manual page - man7.org</a></li>
<li><a href="https://sesamedisk.com/linux-luks-suspend-regression-security/">Linux LUKS Suspend Regression: Keys Stay - Sesame Disk</a></li>

</ul>
</details>

**社区讨论**: 关于该 bug 报告的评论显示反应不一。一些用户认为这是标题党，因为该功能并非上游官方支持，而另一些用户则强调安全回归往往是无声且危险的。对于在挂起期间将密钥保留在内存中是否对普通用户构成真正威胁，存在分歧。

**标签**: `#security`, `#linux`, `#encryption`, `#regression`

---

<a id="item-4"></a>
## [PeerTube：去中心化、联邦制的 YouTube 替代品](https://github.com/Chocobozzz/PeerTube) ⭐️ 8.0/10

PeerTube 是一个开源、去中心化的视频平台，允许任何人托管自己的实例，并通过 ActivityPub 协议与其他实例连接，形成联邦网络。 它提供了一个尊重隐私、社区所有的 YouTube 替代方案，减少对单一中心化服务的依赖，让创作者对自己的内容拥有更多控制权。 PeerTube 使用 WebTorrent 进行点对点流媒体传输以降低服务器负载，并支持视频嵌入。然而，它目前缺乏内置的盈利选项，这对专业创作者来说是一个重大挑战。

hackernews · doener · 7月2日 11:17 · [社区讨论](https://news.ycombinator.com/item?id=48759634)

**背景**: 去中心化视频平台将存储和分发分布在许多节点上，而不是依赖单一服务器。联邦制意味着不同实例可以相互通信，因此一个实例上的用户可以关注另一个实例上的频道，从而形成类似电子邮件的网络。这与 YouTube 等中心化服务形成对比，后者所有内容都托管在单一公司的服务器上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Odysee">Odysee - Wikipedia</a></li>
<li><a href="https://opensource.com/article/23/3/tour-the-fediverse">A 5-minute tour of the Fediverse | Opensource.com</a></li>
<li><a href="https://www.inmotionhosting.com/blog/what-is-the-fediverse/">What is the Fediverse + 4 Great Apps | InMotion Hosting Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者对盈利问题表示担忧，一位专业 YouTuber 强调视频制作成本高昂，而 PeerTube 缺乏收入选项。其他人指出，将观众从成熟平台吸引过来很困难，不过也有人称赞它适用于开源教程和注重隐私的内容。

**标签**: `#decentralized`, `#video streaming`, `#open-source`, `#federated`, `#PeerTube`

---

<a id="item-5"></a>
## [Immich 3.0：自托管照片平台重大更新](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

开源自托管照片和视频管理解决方案 Immich 发布了 3.0 大版本，标志着该平台的一次重大更新。 作为 Google Photos 和 Apple Photos 的主要自托管替代品，此次重大更新表明以隐私为核心的照片管理功能持续改进，吸引更多用户脱离云服务。 虽然摘要未提供具体变更日志，但 3.0 版本通常会引入重大更改和新功能；用户在升级前应查看迁移指南。

hackernews · hashier · 7月2日 14:13 · [社区讨论](https://news.ycombinator.com/item?id=48761944)

**背景**: Immich 是一个高性能、开源的自托管照片和视频管理平台，旨在替代 Google Photos 等服务。它提供移动备份、相册共享和 AI 搜索等功能，同时将数据保留在用户自己的服务器上。该项目在自托管爱好者中获得了广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/immich-app/immich">GitHub - immich-app/immich: High performance self-hosted photo and ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈的积极情绪，用户称 Immich 是 Apple Photos 的“无脑替代品”，并称赞其隐私和自托管能力。然而，一些用户对 iOS 照片同步性能提出担忧，并将其与 Ente 等替代方案进行比较，强调后者的加密功能。

**标签**: `#immich`, `#self-hosted`, `#photo management`, `#open source`, `#version release`

---

<a id="item-6"></a>
## [西班牙下令将 Palantir 列入公私企业黑名单](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv) ⭐️ 8.0/10

西班牙下令将美国科技巨头 Palantir 列入黑名单，禁止公共和私营企业使用其服务，理由是安全担忧。 这一举措标志着对美国大型数据分析公司的重大监管打击，反映了欧洲对数据主权和外国技术依赖日益增长的担忧。 该黑名单影响 Palantir 的数据集成和分析软件，该软件被政府机构和公司广泛使用。此举引发了关于其动机是出于真正的安全风险还是政治考虑的辩论。

hackernews · mgh2 · 7月2日 15:02 · [社区讨论](https://news.ycombinator.com/item?id=48762725)

**背景**: Palantir Technologies 是一家以数据分析平台闻名的美国公司，情报和国防机构使用其平台。该公司曾因隐私和监控问题受到批评。西班牙的黑名单是在欧洲减少对美国科技公司依赖、加强数据保护法规的背景下出台的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Palantir">Palantir</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：一些用户称赞西班牙此举是迈向数据主权和隐私保护的一步，而另一些用户则怀疑其政治动机，指出西班牙最近与华为的合同。少数人表示强烈反对 Palantir，但也有人对西班牙安全政策的一致性表示怀疑。

**标签**: `#Palantir`, `#Spain`, `#Data Privacy`, `#Tech Policy`, `#Geopolitics`

---

<a id="item-7"></a>
## [Strix：开源 AI 渗透测试工具发布](https://github.com/usestrix/strix) ⭐️ 8.0/10

Strix，一款开源 AI 驱动的渗透测试工具，已在 GitHub 上发布，提供自主 AI 代理，能够动态发现并通过概念验证漏洞利用来确认应用漏洞。 该工具通过将 AI 与开源相结合，使高级安全测试民主化，减少对手动渗透测试和静态分析误报的依赖，可能改变开发者和安全团队发现和修复漏洞的方式。 Strix 具有多智能体编排、真实漏洞利用验证功能，并与 GitHub Actions 和 CI/CD 流水线集成，可在每个拉取请求上进行自动扫描。它采用 Apache 2.0 许可证，可通过 PyPI 获取。

rss · GitHub Trending - Daily · 7月2日 01:39

**背景**: 传统的渗透测试需要安全专家手动模拟攻击以发现漏洞。AI 驱动的工具自动化了部分流程，但许多依赖静态分析，会产生误报。Strix 使用动态分析，通过自主 AI 代理模拟真实黑客行为，运行代码并生成可工作的概念验证漏洞利用来确认发现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing ...</a></li>
<li><a href="https://docs.strix.ai/">Introduction - Strix</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI`, `#pentesting`, `#open-source`, `#vulnerability`

---

<a id="item-8"></a>
## [Meta 开源 Astryx 设计系统，支撑内部 13,000+ 应用](https://github.com/facebook/astryx) ⭐️ 8.0/10

Meta 宣布开源 Astryx，这是一套基于 React 的设计系统，在 Meta 内部经历了八年发展，支撑了 13,000+ 应用，现已以 MIT 许可证公开发布（公测版）。它提供 150+ 无障碍组件、品牌级主题、暗黑模式、模板和 CLI，底层使用 StyleX 技术实现样式。 Astryx 是迄今为止规模最大的内部设计系统开源项目之一，为开发者社区提供了一个经过实战检验、可定制且支持 AI 代理的 UI 工具包。其设计理念——内部开放、无样式锁定、对代理友好——直击企业级 UI 开发中的常见痛点。 Astryx 内部使用 StyleX 处理样式，但允许使用者通过 className 使用任何 CSS 方案（如 Tailwind、CSS modules、纯 CSS）进行覆盖。系统还包含 swizzle 功能，可将组件完整源码弹出到项目中以便深度定制，CLI 则同时面向人类和 AI 助手设计。

rss · GitHub Trending - Daily · 7月2日 01:39

**背景**: 设计系统是一组可复用的 UI 组件和规范，用于确保组织内各应用的视觉和功能一致性。StyleX 是 Meta 开发的编译时 CSS-in-JS 库，兼具 CSS-in-JS 的灵活性和静态 CSS 的性能。Astryx 内部使用 StyleX，但对使用者透明，无需额外构建插件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/facebook/astryx">GitHub - facebook/astryx: An open source design system that's fully customizable and agent ready · GitHub</a></li>
<li><a href="https://astryx.atmeta.com/">Astryx Design System</a></li>
<li><a href="https://www.opensourceforu.com/2026/06/meta-open-sources-astryx/">Meta Open-Sources Astryx: An AI-Agent-Ready React Design System - Open Source For You</a></li>

</ul>
</details>

**标签**: `#react`, `#design-system`, `#open-source`, `#meta`, `#ui`

---

<a id="item-9"></a>
## [Allen AI 发布 olmOCR 工具包，用于 PDF 转文本](https://github.com/allenai/olmocr) ⭐️ 8.0/10

Allen AI 发布了开源工具包 olmOCR，可将 PDF 和图像转换为干净、可读的纯文本或 Markdown，专为构建 LLM 训练数据集而优化。最新版本 v0.4.0 引入了使用合成数据和强化学习训练的新模型，将基准分数提升了约 4 分。 olmOCR 解决了 LLM 数据准备中的一个关键瓶颈，提供了一种高效、高质量的 PDF 线性化工具，能够保留阅读顺序、公式、表格和手写内容。这使得研究人员和公司能够更轻松地整理大规模、多样化的文本数据集，用于训练或微调语言模型。 olmOCR 基于一个 7B 参数的视觉语言模型（VLM）olmOCR-2-7B-1025-FP8，需要 GPU 支持，每百万页转换成本低于 200 美元。它还附带了一个全面的基准测试套件 olmOCR-Bench，涵盖 1,400 份文档中的 7,000 多个测试案例。

rss · GitHub Trending - Daily · 7月2日 01:39

**背景**: 大型语言模型（LLM）的训练需要大量高质量的文本数据。虽然 PDF 是此类数据的常见来源，但从中提取文本并保持结构和阅读顺序并非易事，尤其是对于复杂的布局、表格和扫描文档。olmOCR 使用视觉语言模型直接解释页面的视觉外观，避免了传统 OCR 或 PDF 解析方法的局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/allenai/olmocr">GitHub - allenai/olmocr: Toolkit for linearizing PDFs for LLM ...</a></li>
<li><a href="https://olmocr.allenai.org/">olmOCR – Open-Source OCR for Accurate Document Conversion</a></li>

</ul>
</details>

**标签**: `#PDF`, `#LLM`, `#data preprocessing`, `#toolkit`, `#OCR`

---

<a id="item-10"></a>
## [VulnClaw：AI 驱动的 CLI 工具，通过自然语言自动化渗透测试](https://github.com/Unclecheng-li/VulnClaw) ⭐️ 8.0/10

VulnClaw v0.3.2 发布，这是一款 CLI 工具，利用 AI Agent、MCP 工具链和技能编排，通过自然语言输入自动化完成从信息收集到报告生成的整个渗透测试流程。 该工具将 AI 推理与实用渗透测试相结合，是安全自动化领域的重要进步，可能降低授权安全评估和红队演练的门槛。 它支持 13 个 LLM 提供商（OpenAI、DeepSeek 等），内置 21 个渗透技能，并包含反幻觉验证机制，确保发现结果与实际工具输出一致。

rss · GitHub Trending - Daily · 7月2日 01:39

**背景**: MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，规范了 AI 系统与外部工具和数据源的连接方式。在渗透测试中，AI 代理可以编排多个工具和技能，实现复杂安全评估的自动化。VulnClaw 利用这些技术提供端到端的自动化测试体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Penetration Testing`, `#MCP`, `#Cybersecurity`, `#Automation`

---

<a id="item-11"></a>
## [Open WebUI：支持多种 LLM 后端的用户友好界面](https://github.com/open-webui/open-webui) ⭐️ 8.0/10

Open WebUI 是一个开源、自托管的 AI 平台，提供功能丰富的网页界面，用于与来自 Ollama 和任何兼容 OpenAI API 的大型语言模型进行交互。 该工具简化了本地和云端 LLM 的部署和使用，无需复杂设置即可让个人和组织访问先进的 AI，并且凭借高 GitHub 星标获得了强劲的社区支持。 它支持离线运行，包含用于 RAG（检索增强生成）的内置推理引擎，并可通过 pip、uv、Docker 或 Kubernetes 安装，提供专用的 :ollama 和 :cuda 容器镜像。

rss · GitHub Trending - Python Daily · 7月2日 01:46

**背景**: Ollama 是一个开源平台，允许用户在自己的机器上本地运行大型语言模型。OpenAI API 则通过云服务提供对 GPT-4 等模型的访问。Open WebUI 作为一个统一的前端，可以连接本地的 Ollama 模型和远程的 OpenAI 兼容 API，为用户提供灵活性和控制权。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama</a></li>
<li><a href="https://www.ollama.com/">Ollama</a></li>

</ul>
</details>

**标签**: `#AI`, `#web UI`, `#open-source`, `#LLMs`, `#tools`

---

<a id="item-12"></a>
## [Maigret：一款可扫描 3000 多个网站查找用户名痕迹的 OSINT 工具](https://github.com/soxoj/maigret) ⭐️ 8.0/10

Maigret 是一款基于 Python 的开源情报（OSINT）工具，它通过搜索超过 3000 个网站上的用户名来收集一个人的档案，无需任何 API 密钥，并提供可选的 AI 驱动的分析功能。 该工具极大地简化并扩展了基于用户名的调查过程，适用于安全研究人员、记者和执法部门，使得无需深厚技术背景即可进行 OSINT，并减少了手动检查所需的时间。 Maigret 需要 Python 3.10 或更高版本，覆盖超过 3000 个网站，并支持多种输出格式。该工具还包含一个 AI 分析演示，尝试根据收集到的数据构建人物画像。

rss · GitHub Trending - Python Daily · 7月2日 01:46

**背景**: 开源情报（OSINT）是指从公开可用来源收集和分析信息以获取情报的过程。在网络安全中，OSINT 被用于发现潜在漏洞或搜集威胁情报。像 Maigret 这样的用户名搜索工具可以帮助自动化发现个人在不同平台上的网络足迹，可用于调查、渗透测试或社会工程学评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-source_intelligence">Open - source intelligence - Wikipedia</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/threat-intelligence/open-source-intelligence-osint/">What is OSINT ( Open Source Intelligence )?</a></li>

</ul>
</details>

**标签**: `#osint`, `#python`, `#username-search`, `#github`

---

<a id="item-13"></a>
## [Chrome DevTools MCP 服务器让 AI 代理控制浏览器](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools 团队发布了官方的 MCP 服务器（chrome-devtools-mcp），允许 AI 编码代理如 Claude、Cursor 或 Copilot 通过模型上下文协议检查、调试和自动化实时 Chrome 浏览器。 这填补了 AI 驱动工作流中的关键空白，通过直接从编码代理提供可靠、细粒度的浏览器控制和调试能力。 该工具使用 Puppeteer 进行自动化，利用 Chrome DevTools 进行性能追踪，并且默认收集使用统计信息（可选择退出）。

rss · GitHub Trending - TypeScript Daily · 7月2日 01:48

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在规范化 AI 系统连接外部工具和数据源的方式。Chrome DevTools 是内置于 Chrome 浏览器的一套网页开发者工具。此 MCP 服务器让 AI 编码代理能够直接访问这些工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">GitHub - ChromeDevTools/chrome-devtools-mcp: Chrome DevTools for coding agents · GitHub</a></li>
<li><a href="https://developer.chrome.com/blog/chrome-devtools-mcp">Chrome DevTools (MCP) for your AI agent | Blog | Chrome for Developers</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#automation`, `#debugging`

---

<a id="item-14"></a>
## [Polars：基于 Rust 的超高速 DataFrame 库](https://github.com/pola-rs/polars) ⭐️ 8.0/10

Polars 是一个用 Rust 编写的超快 DataFrame 查询引擎，目前在数据工程和数据科学社区中获得了广泛采用。它提供惰性和即时执行、支持大于内存数据集的流式处理以及多线程性能。 Polars 在速度和内存效率上显著优于传统的 DataFrame 库（如 pandas），使数据从业者能够更快地处理大数据集，同时减少资源消耗。其轻量级设计和零依赖特性使其成为现代数据工作流程中极具吸引力的替代方案。 Polars 使用 Apache Arrow 列式格式实现高效数据表示，并支持 SIMD 以进一步提升速度。它提供 Python、Rust、Node.js、R 和 SQL 的前端绑定，并拥有强大的表达式 API 以支持复杂的数据操作。

rss · GitHub Trending - Rust Daily · 7月2日 01:47

**背景**: DataFrame 库是数据分析中必不可少的工具，允许用户直观地操作结构化数据。Pandas 一直是 Python 中的主导库，但在处理大数据集和性能方面存在不足。Rust 是一种系统编程语言，以其内存安全和性能著称，非常适合构建高性能数据处理工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pola.rs/">Polars — DataFrames for the new era</a></li>
<li><a href="https://github.com/pola-rs/polars">GitHub - pola-rs/polars: Extremely fast Query Engine for DataFrames, written in Rust · GitHub</a></li>
<li><a href="https://realpython.com/polars-python/">Python Polars: A Lightning-Fast DataFrame Library – Real Python</a></li>

</ul>
</details>

**标签**: `#rust`, `#dataframe`, `#data-engineering`, `#performance`, `#open-source`

---

<a id="item-15"></a>
## [Awesome Rust：精选 Rust 资源列表](https://github.com/rust-unofficial/awesome-rust) ⭐️ 8.0/10

awesome-rust 仓库托管在 rust-unofficial 下，维护着精选的 Rust 代码和资源列表，涵盖应用、库和工具。 该资源对 Rust 开发者至关重要，提供了一个组织良好、定期更新的 Rust 生态系统概览，帮助新手和有经验的开发者发现高质量的项目和库。 列表包括应用（音频、区块链、数据库等）、开发工具、库等部分，采用社区维护结构，并通过自动化 CI 检查保证质量。

rss · GitHub Trending - Rust Daily · 7月2日 01:47

**背景**: Awesome 列表是针对特定主题的精选资源集合，通常托管在 GitHub 上，以'awesome'为标志。Rust 编程语言强调安全性和性能，其生态系统发展迅速。该仓库汇集了最佳的 Rust 工具和库，使开发者更容易找到所需。

**标签**: `#Rust`, `#awesome-list`, `#resources`, `#curated`

---

<a id="item-16"></a>
## [Kueue：面向批处理工作负载的 Kubernetes 原生作业队列](https://github.com/kubernetes-sigs/kueue) ⭐️ 8.0/10

Kueue 是一组用于 Kubernetes 作业队列的 API 和控制器，支持基于优先级的调度、资源管理以及与流行批处理作业框架的集成。 它通过提供原生的作业级别队列填补了 Kubernetes 批处理领域的空白，实现了多租户环境下的公平共享和资源效率。这对 AI/ML 工作负载和高性能计算至关重要。 Kueue 支持 StrictFIFO 和 BestEffortFIFO 等策略，具备抢占、队列组（cohorts）和资源口味互换（flavor fungibility）等功能，并与 BatchJob、Kubeflow、RayJob 和 JobSet 集成。它还提供 Prometheus 指标和 AdmissionChecks。

rss · GitHub Trending - Go Daily · 7月2日 01:42

**背景**: Kubernetes 是一个容器编排平台。批处理工作负载（如训练 ML 模型）通常需要作业队列来管理资源和优先级。Kueue 来自 Kubernetes SIG-s，提供了一种与 Kubernetes 调度器协同工作的原生解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kubernetes.io/blog/2022/10/04/introducing-kueue/">Introducing Kueue | Kubernetes</a></li>
<li><a href="https://github.com/kubernetes-sigs/kueue">GitHub - kubernetes -sigs/kueue: Kubernetes -native Job Queueing</a></li>

</ul>
</details>

**标签**: `#kubernetes`, `#job-queueing`, `#batch-processing`, `#cloud-native`

---

<a id="item-17"></a>
## [Meta 计算：人人都想成为云](https://newsletter.semianalysis.com/p/meta-compute-everyone-wants-to-be) ⭐️ 8.0/10

Meta 正在打造一项名为 Meta Compute 的云业务，旨在出售过剩的 AI 计算能力并托管其 AI 模型，与 AWS、Azure 以及 CoreWeave 等新云厂商竞争。该计划包括将推荐系统规模扩大 10 倍，并将在即将发布的 ClusterMAX 排名中有所体现。 这标志着 Meta 在战略上的转变，通过其庞大的 AI 基础设施实现盈利，加剧了云市场的竞争，并可能降低 AI 计算成本。这反映了大型科技公司构建类似云的服务以从 AI 投资中获取更多价值的更广泛趋势。 Meta 的云将提供两条业务线：原始 AI 计算能力（类似新云厂商）以及对其自有 AI 模型的托管访问（类似 AWS Bedrock），由基础设施主管 Santosh Janardhan 领导。Meta 还在使用 InterFormer 等新架构将其推荐系统扩展到 LLM 规模，旨在实现 10 倍的效率提升。

rss · Semianalysis · 7月2日 22:18

**背景**: 大型科技公司最初为内部使用构建云基础设施，后来出售多余容量（例如 AWS、Google Cloud）。Meta 为其社交平台在 AI 计算方面进行了大量投资，现在寻求将这种能力外部化以盈利。ClusterMAX 是 SemiAnalysis 推出的 GPU 云评分系统，对性能、网络和定价等方面进行排名，即将发布的排名将包括 Meta 的服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://letsdatascience.com/news/meta-builds-cloud-business-to-sell-ai-compute-bc12117e">Meta Builds Cloud Business to Sell AI Compute | Let's Data ...</a></li>
<li><a href="https://newsletter.semianalysis.com/p/clustermax-20-the-industry-standard">ClusterMAX ™ 2.0: The Industry Standard GPU Cloud Rating System</a></li>
<li><a href="https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/">Meta Adaptive Ranking Model: Bending the Inference Scaling Curve to Serve LLM-Scale Models for Ads - Engineering at Meta</a></li>

</ul>
</details>

**标签**: `#cloud computing`, `#Meta`, `#infrastructure`, `#AI`, `#tech strategy`

---

<a id="item-18"></a>
## [ECTC 2026 综述：EMIB-T、HBM4、冷却、光子互连](https://newsletter.semianalysis.com/p/ectc2026) ⭐️ 8.0/10

在 ECTC 2026 上，Intel、台积电、SK 海力士、三星、美光、Marvell、Lightmatter 和微软展示了先进封装的技术路线和挑战，包括 Intel 的 EMIB-T 技术、定制 HBM、HBM4 封装挑战、微流体冷却和光子互连。 这些进展对未来 AI 和 HPC 系统至关重要，因为先进封装能够实现更高的性能、带宽和能效。所强调的挑战将塑造半导体行业的发展方向。 EMIB-T 结合了 2.5D 和 3D 封装元素，支持 HBM4 和 UCIe。微流体冷却将冷却通道直接嵌入硅中，实现显著的降温效果。光子互连利用光进行高带宽、低功耗的芯片间通信。

rss · Semianalysis · 7月2日 17:25

**背景**: 先进封装将多个芯片集成到一个封装中，以克服半导体缩放限制。EMIB（嵌入式多芯片互连桥）是 Intel 用于高密度芯片间连接的技术。HBM（高带宽存储器）是一种用于 GPU 和加速器的内存。微流体冷却通过微通道循环液体来冷却热点。光子互连使用光传输数据，在带宽和能效方面优于电互连。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kad8.com/hardware/intel-archieves-breakthroughs-new-packaging-technology/">Intel Archieves Breakthroughs New Packaging Technologies · KAD</a></li>
<li><a href="https://www.datacenterdynamics.com/en/analysis/microfluidics-cooling-inside-the-chip/">Microfluidics: Cooling inside the chip - DCD</a></li>
<li><a href="https://lightmatter.co/knowledge-hub/how-do-photonic-interconnects-work/">How Do Photonic Interconnects Work?</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#advanced packaging`, `#HBM`, `#photonic interconnects`, `#microfluidic cooling`

---

<a id="item-19"></a>
## [铠侠-闪迪 BiCS10 332 层 3D NAND 进入出样](https://www.ithome.com/0/971/973.htm) ⭐️ 8.0/10

铠侠和闪迪宣布其第 10 代 BiCS FLASH 3D NAND 开始出样，采用 332 层堆叠，首款产品为 1Tb TLC，I/O 接口速度高达 4800 MT/s。 这一里程碑展示了 NAND 闪存在密度和性能上的持续进步，相比 BiCS8 密度提升 59%，为数据中心和消费设备实现更高容量 SSD 铺平道路。 BiCS10 芯片采用 332 层单元堆叠架构，使用 CMOS 直接键合到阵列（CBA）和节距选通（OPS）技术，支持 Toggle DDR6.0 接口，数据传输速率达 4800 MT/s。

rss · IT之家 · 7月2日 23:55

**背景**: 3D NAND 闪存通过垂直堆叠存储单元来提高密度，无需缩小单元尺寸。CBA 技术将 CMOS 逻辑电路和存储阵列在单独晶圆上键合，以提升性能；OPS 则改善了高堆叠层数设计中的信号完整性。BiCS10 是铠侠和闪迪的最新一代产品，上一代 BiCS8 为 218 层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/storage/kioxia-and-sandisk-start-shipping-bics9-3d-nand-samples-hybrid-design-combining-112-layer-bics5-with-modern-cba-and-ddr6-0-interface-for-higher-performance-and-cost-efficiency">Kioxia and SanDisk start shipping BiCS9 3D NAND... | Tom's Hardware</a></li>
<li><a href="https://www.techtimes.com/articles/317071/20260524/kioxia-nand-flash-mass-production-accelerates-bics10-target-puts-samsung-sk-hynix-edge.htm">Kioxia NAND Flash Mass Production Accelerates: BiCS10 Target Puts...</a></li>
<li><a href="https://www.icgoodfind.com/cms/Article/get/article_id/18126">Kioxia Delays BiCS10 3D NAND Mass Production to 2027, Boosts...</a></li>

</ul>
</details>

**标签**: `#NAND Flash`, `#Storage Technology`, `#Semiconductors`, `#3D NAND`, `#Kioxia`

---

<a id="item-20"></a>
## [特斯拉司机因 FSD 致命车祸被控过失杀人，数据显示其人为干预](https://www.ithome.com/0/971/971.htm) ⭐️ 8.0/10

此案为半自动驾驶系统使用中的驾驶员责任确立了重要的法律先例，尤其是当驾驶员主动寻求更激进的驾驶模式时。它凸显了系统保守性感知与实际安全风险之间的张力，可能影响未来的法规制定及公众对特斯拉 FSD 的看法。 车辆数据显示，巴特勒将加速踏板踩至 100%约 6 秒，车速升至 117 公里/小时（超出住宅区限速两倍以上），且从未踩下制动踏板。特斯拉 AI 负责人证实驾驶员手动干预了 FSD，这与巴特勒自称启动系统后失去意识的说法相矛盾。

rss · IT之家 · 7月2日 23:43

**背景**: 特斯拉的 FSD（完全自动驾驶）是一种高级驾驶辅助系统，可以处理许多驾驶任务，但仍需要驾驶员主动监督。特斯拉提供多种驾驶模式（如 Sloth、Chill、Standard、Hurry、Mad Max），可调整系统的激进程度。驾驶员可随时通过踩加速或制动踏板干预 FSD，但这样做会将控制权交还给驾驶员。在此事件中，驾驶员的人为干预导致了致命车祸。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/brookecrothers/2026/06/28/tesla-autopilot-vs-fsd-explained--and-what-can-go-wrong/">Tesla FSD Explained – And What Can Go Wrong</a></li>
<li><a href="https://electrek.co/2026/06/23/tesla-fsd-katy-crash-driver-pedal/">Tesla admits FSD was on in fatal Texas crash, blames driver for 'overriding' it | Electrek</a></li>
<li><a href="https://tahaabbasi.com/blog/tesla-fsd-profiles-explained-sloth-chill-standard-hurry-mad-max-which-one-should-you-use-taha-abbasi">Tesla FSD Profiles Explained: Sloth, Chill, Standard, Hurry ...</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#FSD`, `#autonomous driving`, `#safety`, `#legal`

---

<a id="item-21"></a>
## [快手 AI 子公司可灵获最高 30 亿美元融资](https://www.ithome.com/0/971/954.htm) ⭐️ 8.0/10

快手今日公告，初始投资者同意向北京可灵注资 138.24 亿元人民币（约 20.28 亿美元），额外投资者可追加至 204.471 亿元（约 30 亿美元），投后估值 180 亿美元。 这笔巨额融资彰显了市场对快手 AI 视频生成技术的强烈信心，使可灵 AI 成为全球估值最高的独立 AI 视频初创公司之一，并计划在 12 个月内赴港上市。 初始投资包括 21 名独立投资者出资 138.24 亿元，总融资上限为 30 亿美元，约占扩大后注册资本的 16.67%。据报腾讯参与了本轮融资，投后估值 180 亿美元，较此前 200 亿美元目标有所下调。

rss · IT之家 · 7月2日 15:36

**背景**: 可灵 AI 是快手推出的 AI 视频生成平台，支持文生视频、图生视频、对口型、运镜控制等功能，于 2024 年推出，截至 2025 年 1 月年化收入超过 3 亿美元。快手在 2025 年 5 月宣布了分拆及引入外部投资者的计划。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kelingaicn.com/">可灵AI官网</a></li>
<li><a href="https://klingai.com/app">可灵 AI - 新一代 AI 创意生产力平台</a></li>

</ul>
</details>

**标签**: `#AI`, `#investment`, `#Kuaishou`, `#Keling`, `#funding`

---

<a id="item-22"></a>
## [企业 AI 成本失控，花旗、Adobe 等限制员工使用大模型](https://www.ithome.com/0/971/937.htm) ⭐️ 8.0/10

泄露的内部文件显示，包括花旗银行、Adobe、Atlassian 和亚马逊在内的多家大型企业，因按 token 计费导致月度 AI 成本暴增至三倍，正在限制员工使用高级 AI 模型，其中一家公司月支出超过 1500 万美元。 这揭示了企业快速部署 AI 的隐藏后果：按使用量计费导致成本失控，迫使企业实施严格管控。这一趋势可能减缓 AI 采用速度，并将焦点转向成本效益更高的模型选择。 花旗银行禁用了 Claude Opus 4.6/4.7 和 GPT-5.5 的访问；Atlassian 的月度 AI 成本从 500 万美元升至 1500 万美元；GitHub 正在测试按用户计费模式；Adobe 终止了 Claude 无限制访问。公司还在监控 token 用量并设置预算。

rss · IT之家 · 7月2日 14:22

**背景**: 像 GPT-5 和 Claude Opus 这样的 AI 模型按 token（文本处理单位）收费。此前，许多企业采用固定费用协议，但供应商已转向按使用量计费。这一变化使得成本难以预测，迫使企业跨员工管理 token 预算，并在非必要时限制对昂贵的旗舰模型的访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://benchlm.ai/llm-pricing">LLM API Pricing Comparison 2026 — Cost Per Token for GPT ...</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence, Performance, and Price</a></li>

</ul>
</details>

**社区讨论**: 内部员工评论反映了对失去 AI 访问权限的焦虑以及对先前宽松成本政策的不满。一些人质疑大量使用 AI 的必要性，而另一些人则认为限制是不可避免的。还提到了一种讽刺情况：埃森哲曾大力推广 AI，现在却提供成本管理服务。

**标签**: `#AI`, `#cost management`, `#enterprise`, `#large language models`, `#industry trends`

---

<a id="item-23"></a>
## [针对 Microsoft 365 的密码喷洒攻击利用 Azure CLI](https://www.ithome.com/0/971/914.htm) ⭐️ 8.0/10

安全公司 Huntress 报告称，有黑客利用 Azure CLI 和 OAuth ROPC 流程对 Microsoft 365 账户发起大规模密码喷洒攻击，在 2025 年 6 月 12 日至 26 日期间产生超过 8100 万次登录请求，至少 64 家机构的 78 个账户被入侵。 此次攻击表明，攻击者可以通过利用 ROPC 等旧版 OAuth 流程绕过多因素认证和条件访问策略，对云身份安全构成重大威胁。仅依赖多因素认证的组织如果未明确保护 Azure CLI 登录，可能面临风险。 攻击者使用之前泄露的凭据，通过 Azure CLI 进行密码喷洒，针对许多账户尝试少量常见密码以避免账户锁定。恶意流量来自归属于 LSHIY LLC 的一个 IPv6 地址段。

rss · IT之家 · 7月2日 13:46

**背景**: 密码喷洒是一种攻击技术，攻击者针对大量账户尝试少量常见密码，与针对单个账户尝试大量密码的暴力破解不同。OAuth ROPC（资源所有者密码凭据）授权类型允许应用程序直接使用用户名和密码交换访问令牌，无需交互式登录，这种方法被认为安全性较低，在现代应用中通常已弃用。Azure CLI 是用于管理 Azure 资源的命令行工具；攻击者利用它自动化认证请求，使其看起来像正常的 API 流量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth-ropc">Microsoft identity platform and OAuth 2.0 Resource... | Microsoft Learn</a></li>
<li><a href="https://www.scottbrady.io/oauth/why-the-resource-owner-password-credentials-grant-type-is-not-authentication-nor-suitable-for-modern-applications">Don't use the OAuth password grant type</a></li>
<li><a href="https://cybersecuritynews.com/microsofts-azure-password-spray-attack/">Massive Password Stealing Attack Targeting Microsoft 365 Users...</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#password spraying`, `#Microsoft 365`, `#Azure CLI`, `#OAuth ROPC`

---

<a id="item-24"></a>
## [微软斥资 25 亿美元成立新公司助力企业 AI 落地](https://www.ithome.com/0/971/911.htm) ⭐️ 8.0/10

微软宣布成立一家名为微软前沿公司的新子公司，初期注资 25 亿美元，旨在帮助企业整合来自 Anthropic、OpenAI 等多个供应商的 AI 工具。 这标志着微软企业 AI 战略的重大转变，承认客户希望灵活组合模型而非被单一供应商锁定，可能重塑企业 AI 市场格局。 新公司将与联合利华、诺和诺德等客户合作，整合微软自研 AI 工具、第三方模型及企业专有数据，确保输出归客户所有。微软商用业务总裁承认早期将 Copilot 仅绑定 OpenAI 模型是个错误。

rss · IT之家 · 7月2日 13:29

**背景**: 企业越来越多采用多模型策略，结合 Anthropic 的 Claude、OpenAI 的 GPT 以及 DeepSeek 等开源模型，以避免供应商锁定并降低成本。微软是 OpenAI 的主要投资者，也已将 Anthropic 的模型集成到 Copilot 中。此举效仿了 Palantir 和亚马逊云服务等同行的类似做法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#AI adoption`, `#enterprise AI`, `#investment`

---

<a id="item-25"></a>
## [Meta 进军云计算引发 AI 基础设施股暴跌](https://www.36kr.com/p/3878176206516225) ⭐️ 8.0/10

Meta 宣布正在搭建云计算业务，将向外部客户出售 AI 算力，导致 CoreWeave 和 Nebius 等 AI 基础设施股暴跌。 这标志着 Meta 寻求将其庞大的 AI 资本支出货币化的重大转变，可能颠覆云端 AI 算力市场并影响 CoreWeave 等竞争对手。 Meta 已签署超过 1000 亿美元的 AI 基础设施合同，包括与 CoreWeave 的 2100 亿美元和与 Nebius 的 2700 亿美元协议。其进军云业务引发了对供应过剩和合同续签的担忧。

rss · 36氪 - 24小时热榜 · 7月2日 08:34

**背景**: 亚马逊、微软和谷歌等大型科技公司拥有盈利的云业务，可以抵消其 AI 基础设施支出。Meta 此前缺乏这样的收入来源，使其巨额资本支出成为投资者担忧的问题。通过进入云服务，Meta 旨在为潜在过度投资建立安全网。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/accelerators/instinct.html">AMD Instinct ™ Accelerators</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group</a></li>

</ul>
</details>

**标签**: `#Meta`, `#cloud computing`, `#AI infrastructure`, `#stock market`, `#capital expenditure`

---

<a id="item-26"></a>
## [Cloudflare 9 月起默认拦截混合用途 AI 爬虫，含谷歌](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/) ⭐️ 8.0/10

Cloudflare 宣布自 9 月 15 日起，将默认拦截同时用于搜索索引、AI 问答和训练的“混合用途”爬虫抓取带广告的页面，并专门点名谷歌的爬虫。 该政策迫使 AI 公司要么按功能分离机器人，要么为使用发布商内容付费，可能重塑 AI 训练数据的获取方式。网站发布商获得了一个保护内容不被无偿爬取的工具。 拦截针对的是同时进行搜索索引和 AI 训练的“混合用途”爬虫；发布商仍可单独允许专门的 AI 爬虫。Cloudflare 利用其现有机器人管理系统，通过行为分析检测并拦截这些爬虫。

telegram · zaihuapd · 7月2日 05:37

**背景**: 混合用途爬虫是同时为搜索引擎建立索引和为 AI 模型训练抓取数据的机器人。此前，网站可以阻止 AI 爬虫，但无法阻止搜索爬虫，这为谷歌等公司利用搜索爬虫进行 AI 训练创造了漏洞。Cloudflare 的新默认设置通过将任何双重用途的爬虫视为对发布商变现的潜在威胁来堵住这一漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bitcoinworld.co.in/cloudflare-blocks-ai-crawlers-publishers-payment/">Cloudflare’s New Default Settings Will Block AI Crawlers From...</a></li>
<li><a href="https://www.engadget.com/2207360/cloudflare-will-filter-out-web-crawlers-that-serve-ai-companies/">Cloudflare Will Filter Out Web Crawlers That Serve AI Companies</a></li>
<li><a href="https://www.cloudflare.com/products/bot-management/">Bot Management - Cloudflare</a></li>

</ul>
</details>

**社区讨论**: Telegram 社区讨论指出，许多网站阻止了 AI 爬虫，但没有阻止谷歌搜索，导致谷歌利用这个漏洞训练其 AI。Cloudflare 的举措被视为迫使谷歌要么停止用搜索爬虫训练 AI，要么为内容付费。

**标签**: `#AI`, `#web scraping`, `#Cloudflare`, `#Google`, `#content policy`

---

<a id="item-27"></a>
## [OpenAI 提议美国政府持股 5%，或纳入 Google、Meta](https://www.bloomberg.com/news/articles/2026-07-02/openai-proposes-giving-the-us-government-a-5-stake-ft-says) ⭐️ 8.0/10

OpenAI 提议美国政府持有公司 5%的股份，并可能推广至 Google 和 Meta 等主要 AI 公司，让公众分享 AI 热潮带来的收益。 这一提议标志着 AI 治理和公共政策的重大转变，可能重塑行业监管及 AI 进步带来的财富分配。 该计划由一个政府载体统一持有 OpenAI、Anthropic、Google 和 Meta 各 5%的股份，但引发了监管、控制权和利益冲突等争议，其他公司是否接受尚不明确。

telegram · zaihuapd · 7月2日 06:02

**背景**: OpenAI 是一家领先的 AI 研究机构，开发了 ChatGPT。政府持股的提议在科技行业史无前例，反映了如何将 AI 发展与公共利益对齐的辩论。

**标签**: `#AI政策`, `#政府持股`, `#OpenAI`, `#科技监管`, `#公共利益`

---

<a id="item-28"></a>
## [PS3 商店 2027 关闭引发紧急游戏存档](http://no-intro.org/) ⭐️ 8.0/10

索尼宣布将于 2027 年 7 月永久关闭 PS3 和 PS Vita 的 PlayStation 商店，档案管理员和 RPCS3 模拟器团队正紧急备份数字游戏数据。 这次关闭可能导致从未推出实体版的数字游戏永久丢失，突显了数字所有权的脆弱性，以及游戏社区中保存工作的紧迫性。 RPCS3 团队推荐使用 no-intro.org 数据库，该数据库记录游戏的加密哈希值和文件大小等元数据，以协调备份工作并识别哪些游戏仍面临风险。

telegram · zaihuapd · 7月2日 15:04

**背景**: PS3 和 PS Vita 商店是用户购买和下载游戏的数字平台，关闭后将无法进行新的购买或重新下载。RPCS3 是一款流行的开源 PS3 模拟器，no-intro.org 是一个社区驱动的数据库，收录游戏 ROM 元数据以协助保存工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rpcs3.net/">RPCS3</a></li>
<li><a href="https://no-intro.org/">No-Intro.org</a></li>

</ul>
</details>

**标签**: `#digital preservation`, `#gaming`, `#PlayStation`, `#emulation`, `#archiving`

---