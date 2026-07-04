---
layout: default
title: "Horizon Summary: 2026-07-04 (ZH)"
date: 2026-07-04
lang: zh
---

> 从 322 条内容中筛选出 33 条重要资讯。

---

1. [ZLUDA：在非 NVIDIA GPU 上以接近原生性能运行 CUDA 应用](#item-1) ⭐️ 9.0/10
2. [全球首例自主 AI Agent 勒索攻击曝光](#item-2) ⭐️ 9.0/10
3. [紫光同创发布国内首款亿门级 FinFET FPGA](#item-3) ⭐️ 9.0/10
4. [CDD 仅通过对数概率即可恢复微调数据](#item-4) ⭐️ 9.0/10
5. [欧洲议会间谍软件调查员遭飞马间谍软件入侵](#item-5) ⭐️ 8.0/10
6. [本地 SOTA 大模型指南：高昂成本与实用限制](#item-6) ⭐️ 8.0/10
7. [Wordgard：ProseMirror 创建者推出的新富文本编辑器](#item-7) ⭐️ 8.0/10
8. [Superpowers：编码智能体的新方法论](#item-8) ⭐️ 8.0/10
9. [Chrome DevTools MCP 服务器让 AI 代理控制浏览器](#item-9) ⭐️ 8.0/10
10. [OpenAI Codex 插件 (用于 Claude Code)](#item-10) ⭐️ 8.0/10
11. [Hugging Face Transformers：领先的开源机器学习库](#item-11) ⭐️ 8.0/10
12. [Anthropic 发布 Claude Code：终端中的智能编码工具](#item-12) ⭐️ 8.0/10
13. [Meta 开源 Astryx 设计系统，含 150+ 组件](#item-13) ⭐️ 8.0/10
14. [微软推出'Skills'仓库，为 AI 编码代理提供落地能力](#item-14) ⭐️ 8.0/10
15. [MCP Apps 协议让 AI 聊天机器人支持交互式 UI](#item-15) ⭐️ 8.0/10
16. [uv：基于 Rust 的超快速 Python 包管理器](#item-16) ⭐️ 8.0/10
17. [Tree-sitter：编程工具的增量解析库](#item-17) ⭐️ 8.0/10
18. [Rolldown：基于 Rust 的 JavaScript/TypeScript 打包器，兼容 Rollup API](#item-18) ⭐️ 8.0/10
19. [Helix：基于 Rust 的后现代模态文本编辑器](#item-19) ⭐️ 8.0/10
20. [ttl：一款基于 Rust 的现代 traceroute 替代工具](#item-20) ⭐️ 8.0/10
21. [wgpu：安全、跨平台的 Rust 图形 API](#item-21) ⭐️ 8.0/10
22. [FFF：面向 AI 代理和开发者的快速文件搜索 SDK](#item-22) ⭐️ 8.0/10
23. [Ollama：本地运行开源大语言模型](#item-23) ⭐️ 8.0/10
24. [桥水研究：前沿 AI 模型金融判断准确率未达 80%](#item-24) ⭐️ 8.0/10
25. [生数科技发布 Vidu S1：支持实时视频通话与语音控制](#item-25) ⭐️ 8.0/10
26. [京东物流在京启动国内首个 L4 自动驾驶重卡载货示范](#item-26) ⭐️ 8.0/10
27. [阿里因隐藏后门全面禁用 Anthropic 产品](#item-27) ⭐️ 8.0/10
28. [百度 AI 芯片昆仑芯冲刺 500 亿美元港股 IPO](#item-28) ⭐️ 8.0/10
29. [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](#item-29) ⭐️ 8.0/10
30. [原生低秩分解提升 Transformer 训练效率](#item-30) ⭐️ 8.0/10
31. [Anthropic 指控阿里巴巴发动大规模蒸馏攻击窃取 Claude 能力](#item-31) ⭐️ 8.0/10
32. [NASA 发射 LINK 航天器救援 Swift 望远镜](#item-32) ⭐️ 8.0/10
33. [腾讯玄武实验室阿图因 AI 在 CyberGym 测试中超越 Mythos](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ZLUDA：在非 NVIDIA GPU 上以接近原生性能运行 CUDA 应用](https://github.com/vosen/ZLUDA) ⭐️ 9.0/10

ZLUDA 是一个开源的、可直接替代 NVIDIA CUDA 的方案，允许未经修改的 CUDA 应用在 AMD 和 Intel GPU 上以接近原生性能运行。该项目使用 Rust 编写，主要通过 ROCm 支持 AMD GPU，并曾支持 Intel GPU。 ZLUDA 打破了 NVIDIA 对 CUDA 的硬件锁定，使 GPU 计算和 AI/ML 工作负载能够在更便宜或更易获得的非 NVIDIA 硬件上运行。这可能使 GPU 计算更加普及，并减少对单一供应商的依赖。 ZLUDA 通过在运行时将 CUDA 内核翻译为 AMD 的 ROCm 或 Intel 的 oneAPI 来实现接近原生性能。它采用 MIT 许可证，在 GitHub 上开源，并通过 Discord 社区提供支持。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: CUDA 是 NVIDIA 的并行计算平台和编程模型，广泛应用于人工智能、机器学习和科学计算。它是专有的，仅能在 NVIDIA GPU 上运行，形成了供应商锁定。ZLUDA 是一个逆向工程兼容层，将 CUDA 指令翻译为 AMD 或 Intel GPU 指令，使得为 CUDA 编写的应用无需修改即可在非 NVIDIA 硬件上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/ZLUDA">ZLUDA</a></li>

</ul>
</details>

**标签**: `#CUDA`, `#GPU`, `#ZLUDA`, `#open-source`, `#Rust`

---

<a id="item-2"></a>
## [全球首例自主 AI Agent 勒索攻击曝光](https://www.ithome.com/0/972/424.htm) ⭐️ 9.0/10

安全厂商 Sysdig 首次记录了一起完全由 AI 智能体（命名为 JADEPUFFER）自主执行的勒索软件攻击案例，该攻击利用已知的 Langflow 漏洞（CVE-2025-3248）完成整个攻击链，无需人工干预。 这一事件标志着网络安全领域的范式转变，证明 AI 智能体能够自主编排多步骤攻击，降低了勒索软件部署的技术门槛，迫使防御者重新思考检测和响应策略。 JADEPUFFER 执行了超过 600 个攻击载荷，能在 31 秒内自主从失败中恢复，并利用 MySQL 的 AES_ENCRYPT()函数加密了 Nacos 中全部 1342 条配置数据，但未保存加密密钥，导致赎金无法支付。

rss · IT之家 · 7月3日 11:57

**背景**: Langflow 是一个用于构建 AI 智能体工作流的开源工具。CVE-2025-3248 是 Langflow 1.3.0 之前版本中的一个严重远程代码执行漏洞，允许未认证的攻击者执行任意 Python 代码。AI 智能体是能够利用大语言模型和外部工具自主规划和执行任务的软件实体。本次攻击展示了 AI 智能体如何将多个已知漏洞和错误配置（如 MinIO 默认凭据）串联起来，实现完整的系统入侵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/horizon3ai_unsafe-at-any-speed-abusing-python-exec-activity-7315844970278539264-yK3v">CVE - 2025 - 3248 : Langflow vulnerability found by Horizon3.ai | LinkedIn</a></li>
<li><a href="https://wiki.archlinux.org/title/MinIO">MinIO - ArchWiki</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#ransomware`, `#cybersecurity`, `#autonomous attack`, `#vulnerability exploitation`

---

<a id="item-3"></a>
## [紫光同创发布国内首款亿门级 FinFET FPGA](https://www.ithome.com/0/972/407.htm) ⭐️ 9.0/10

紫光同创在 2026 慕尼黑上海电子展上发布 Titan-3 系列，这是国内第一款自主研发的亿门级高端 FPGA 产品，采用 FinFET 工艺制造。 这一突破填补了中国在高性能可编程芯片领域的空白，减少了对国外 FPGA 供应商的依赖，为通信、数据中心、人工智能和航空航天等国内应用提供了支撑。 Titan-3 系列包括 PG3T1300 和 PG3T1500 等型号，支持片上大容量 HRM+DRM 架构、高速 DDR4 存储接口、多速率 EMAC 硬核、PCIe Gen4 和高速 SerDes 接口。同时发布了配套的 PG3T1300 加速卡，配备 4 路 25G 光口和 PCIe 4.0 x8 接口。

rss · IT之家 · 7月3日 10:48

**背景**: FPGA（现场可编程门阵列）是一种可编程逻辑芯片，广泛应用于通信、数据中心、视频处理和航空航天等领域。FinFET（鳍式场效应晶体管）是一种先进的晶体管技术，可提升性能和能效。中国一直在努力实现半导体自给自足，而高端 FPGA 曾是国内供应链的一个显著短板。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/electronics-engineering/high-speed-serdes-serializer-deserializer-interfaces/">High - Speed SerDes (Serializer-Deserializer) Interfaces</a></li>
<li><a href="https://www.youtube.com/watch?v=gUsHwi4M4xE">EEVblog #496 - What Is An FPGA ? - YouTube</a></li>

</ul>
</details>

**标签**: `#FPGA`, `#semiconductor`, `#China technology`, `#FinFET`, `#hardware`

---

<a id="item-4"></a>
## [CDD 仅通过对数概率即可恢复微调数据](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 9.0/10

对比解码差异分析(CDD)是一种新方法，仅需访问对数概率(logits)即可从大型语言模型中逐字恢复微调数据，无需模型权重或激活值。 这推进了 AI 安全性与可解释性，仅通过灰盒访问即可实现白盒级别的模型差异分析，性能优于之前的白盒方法(如激活差异透镜)。 CDD 在四个模型家族(1B 至 32B 参数)的 20 个有机体×模型对中的 19 对上达到了 4+/5 的逐字恢复分数，而 ADL 尽管需要完整权重访问，分数从未超过 3/5。

reddit · r/MachineLearning · /u/CebulkaZapiekana · 7月3日 19:01

**背景**: 模型差异分析旨在识别微调后模型的变化。对比解码是一种通过比较两个模型的对数概率来改进生成的技术。CDD 在基模型和微调模型之间应用对比解码，以提取微调数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2210.15097">[2210.15097] Contrastive Decoding: Open-ended Text Generation as Optimization</a></li>
<li><a href="https://www.lesswrong.com/w/model-diffing">Model Diffing — LessWrong</a></li>
<li><a href="https://www.emergentmind.com/topics/contrastive-decoding">Contrastive Decoding in Language Models</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#LLMs`, `#interpretability`, `#AI safety`, `#finetuning`

---

<a id="item-5"></a>
## [欧洲议会间谍软件调查员遭飞马间谍软件入侵](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

经公民实验室法证分析确认，欧洲议会负责调查间谍软件的委员会的一名成员遭到飞马间谍软件入侵。入侵发生在 2022 年 10 月和 2023 年 3 月。 这一事件凸显了国家支持的间谍活动胆敢针对负责调查间谍软件滥用的机构，威胁到民主监督和欧洲议会程序的完整性。 首次感染与一起针对欧洲流亡俄语和白俄罗斯语记者的已知飞马行动重合，表明某飞马客户有权在多个欧盟国家进行间谍活动。该手机中同时包含个人医疗信息和政府机密文件。

hackernews · ledoge · 7月3日 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列 NSO 集团开发的间谍软件，标榜用于反恐，但常被政府用于监视记者、活动家和反对派人士。公民实验室是多伦多大学的一个网络安全研究小组，广泛记录了飞马入侵事件。欧洲议会一直在调查包括飞马在内的间谍软件在欧盟内部的使用情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_Project_(investigation)">Pegasus Project (investigation) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了希腊更广泛的飞马丑闻，有证据表明总理办公室策划了此事。一些人认为，这次攻击应被视为欧盟成员国的攻击，而非针对欧洲议会的外部攻击，突显了滥用飞马的政府的共谋行为。

**标签**: `#cybersecurity`, `#Pegasus`, `#espionage`, `#European Parliament`, `#spyware`

---

<a id="item-6"></a>
## [本地 SOTA 大模型指南：高昂成本与实用限制](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob 在 GitHub 上发布了一份指南，详细说明了如何在本地运行最先进的大语言模型，但社区评论指出推荐的硬件配置成本高达 4 万至 5.5 万美元，并且通过量化和专家剪枝等方式显著降低了模型质量。 该指南及其社区讨论表明，对于大多数个人来说，在本地运行顶级大语言模型的成本仍然高得令人望而却步，而且质量往往低于云服务，这与本地部署更具成本效益的普遍认知相悖。 该指南推荐的配置包含 4 块单价 12,000 美元的 GPU，总价超过 5 万美元，并使用经过 REAP 剪枝和 Int8-mix NVFP4 量化的 GLM-5.2 模型，参数约 594B。另外提到一种更经济的选择：使用两块 RTX 3090，共 48GB 显存，运行 Qwen3.6-27B。

hackernews · livestyle · 7月3日 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: SOTA（最先进）在 AI 中指的是在特定基准上当前性能最好的模型。本地大语言模型推理是指在个人硬件上运行大语言模型，而不是依赖云 API，这需要大量的 GPU 显存和计算能力。该指南旨在帮助用户在家中获得接近云质量的推理体验，但顶级模型的硬件需求极高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://maddevs.io/glossary/state-of-the-art-models/">What Is SOTA in AI? State-of-the-Art Models | Machine Learning Glossary</a></li>
<li><a href="https://grokipedia.com/page/Pre-built_PCs_for_Local_LLM_Inference">Pre-built PCs for Local LLM Inference</a></li>

</ul>
</details>

**社区讨论**: 社区评论者对指南中高端配置的实用性表示严重怀疑，指出其成本（4 万至 5.5 万美元）足以支付多年的云订阅费用。还有人强调，经过剪枝和量化的模型往往会降低质量，并且存在模型被植入后门的安全隐患。少数人提出了更经济的选择，例如 128GB 统一内存配置或双 RTX 3090。

**标签**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#community discussion`

---

<a id="item-7"></a>
## [Wordgard：ProseMirror 创建者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 8.0/10

Wordgard 是由 ProseMirror 的作者 Marijn Haverbeke 开发的一款新的浏览器内富文本编辑器系统。它采用语义化的内容编辑方式，可精确控制文档结构。 此次发布意义重大，因为它出自 ProseMirror（一个广泛使用的编辑器框架）的创建者之手，并引入了一种可能影响未来编辑器开发的不同架构。现在，构建自定义编辑器的开发者有了一个提供更好类型安全和更简洁 API 设计的新选择。 Wordgard 不是一个自由格式的 HTML 编辑器，而是专注于语义化的内容类型，与 ProseMirror 类似但存在显著的概念差异。没有从 ProseMirror 直接升级的路径，因此迁移需要大量重构。

hackernews · indy · 7月3日 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个经过实战检验的开源富文本编辑器框架，以其灵活性和高性能著称，但学习曲线陡峭，并被用于许多编辑器（如 Tiptap）的底层。Wordgard 由其创建者宣布为一个新系统，它共享一些概念但旨在解决类型安全和 API 复杂性等限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wordgard.net/">Wordgard</a></li>
<li><a href="https://code.haverbeke.berlin/wordgard/wordgard">wordgard / wordgard : The Wordgard rich text editor</a></li>
<li><a href="https://news.ycombinator.com/item?id=48772573">Wordgard : The new in-browser rich - text editor from... | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论包括对于创建新编辑器动机的疑问，一些用户指出缺乏升级路径以及移动端可能存在的不稳定。其他人则称赞其设计，并看到与自己定制的解决方案的相似之处而感到受到验证，而有些人则对缺乏富文本编辑的 Web 标准感到沮丧。

**标签**: `#rich-text editor`, `#web development`, `#prosemirror`, `#javascript`, `#open source`

---

<a id="item-8"></a>
## [Superpowers：编码智能体的新方法论](https://github.com/obra/superpowers) ⭐️ 8.0/10

名为 'obra/superpowers' 的 GitHub 仓库为编码智能体提出了一套完整的软件开发方法论与智能体技能框架，强调设计先行和子智能体驱动的开发模式。 该框架可能标准化 AI 智能体在软件开发中的辅助方式，有望提升代码质量并减少人工监督。其可组合技能的方法可能加速企业采用 AI 辅助编码。 Superpowers 支持多种工具，包括 Claude Code、Antigravity、Codex 和 Cursor，并且作为插件在 Anthropic 官方市场中提供。它自动执行规格提取、计划创建和子智能体任务执行等任务。

rss · GitHub Trending - Daily · 7月3日 01:32

**背景**: 编码智能体是指能够根据自然语言指令自主编写、编辑和调试代码的 AI 工具，例如 Anthropic 的 Claude Code、Google 的 Antigravity 和 OpenAI 的 Codex。这些智能体通常协助开发者，但往往需要仔细的提示工程以避免错误。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://antigravity.google/?ref=producthunt">Google Antigravity - Build the new way</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#software development methodology`, `#agentic framework`, `#coding agents`

---

<a id="item-9"></a>
## [Chrome DevTools MCP 服务器让 AI 代理控制浏览器](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools 团队发布了 'chrome-devtools-mcp'，这是一个 MCP 服务器，允许 Claude、Cursor 和 Copilot 等 AI 编码助手控制和检查实时 Chrome 浏览器，以实现自动化和调试。 这个官方工具通过模型上下文协议 (MCP) 连接了 Chrome DevTools 和 AI 编码代理，使得 AI 助手能够直接进行可靠的自动化、深入的调试和性能分析，从而可能显著提高开发者的生产力。 该工具使用 Puppeteer 进行浏览器自动化，并使用 Chrome DevTools 进行性能追踪；它默认收集使用统计信息，但允许通过标志选择退出，并且性能工具可能会向 Google CrUX API 发送跟踪 URL，除非禁用。

rss · GitHub Trending - Daily · 7月3日 01:32

**背景**: 模型上下文协议 (MCP) 是 Anthropic 于 2024 年 11 月推出的开放标准，它标准化了 AI 应用程序连接到外部工具和数据源的方式。MCP 就像 AI 应用的“USB-C 端口”，允许它们通过统一接口与各种系统交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://docs.anthropic.com/en/docs/mcp">Model Context Protocol ( MCP ) - Anthropic</a></li>

</ul>
</details>

**标签**: `#Chrome DevTools`, `#MCP`, `#AI coding agents`, `#automation`, `#debugging`

---

<a id="item-10"></a>
## [OpenAI Codex 插件 (用于 Claude Code)](https://github.com/openai/codex-plugin-cc) ⭐️ 8.0/10

该插件将 OpenAI Codex 的代码审查与任务委派功能集成到 Claude Code 中。

rss · GitHub Trending - Daily · 7月3日 01:32

**标签**: `#AI`, `#code review`, `#plugin`, `#developer tools`, `#OpenAI`

---

<a id="item-11"></a>
## [Hugging Face Transformers：领先的开源机器学习库](https://github.com/huggingface/transformers) ⭐️ 8.0/10

Hugging Face Transformers 是一个用于文本、视觉、音频和多模态任务训练与推理的先进开源库，在 Hugging Face Hub 上托管了超过 100,000 个预训练模型。 它已成为研究界和工业界应用 Transformer 模型的事实标准，极大地降低了使用前沿 AI 的门槛。其广泛采用加速了自然语言处理、计算机视觉、语音处理和多模态 AI 领域的创新。 该库支持超过 100,000 个预训练模型检查点，并能与 Datasets、Spaces 等 Hugging Face 工具无缝集成。它提供了统一的 API，支持 PyTorch、TensorFlow 和 JAX，从而实现灵活的训练和推理。

rss · GitHub Trending - Python Daily · 7月3日 01:38

**背景**: Transformer 架构于 2017 年由论文《Attention Is All You Need》提出，通过使用自注意力机制并行处理序列，取代了循环神经网络。该架构已成为现代 AI 的基础，支撑着 GPT、BERT、ViT 等模型。Hugging Face Transformers 提供了一个用户友好的接口，可以轻松加载、微调和部署这些模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@raiyanmd17357/transformer-architecture-in-machine-learning-800b4691264b">“ Transformer Architecture in Machine Learning ” | Medium</a></li>
<li><a href="https://introml.mit.edu/notes/transformers.html">9 Transformers – 6.390 - Intro to Machine Learning</a></li>
<li><a href="https://medium.com/@jude.ananth/advancements-in-multimodal-machine-learning-the-future-of-ai-3552c7f19888">Advancements in Multimodal Machine Learning : The... | Medium</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#NLP`, `#transformers`, `#deep learning`, `#open source`

---

<a id="item-12"></a>
## [Anthropic 发布 Claude Code：终端中的智能编码工具](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 发布了 Claude Code，这是一个直接在终端中运行的智能编码工具，允许开发者通过自然语言命令执行任务、解释代码和管理 git 工作流。 此次发布标志着将大型语言模型集成到开发者工作流程中的重要一步，通过自动化日常编码任务，可能提升生产力。它使 Anthropic 成为新兴的智能 AI 编码助手领域的关键参与者。 Claude Code 支持多种安装方式，包括 curl、Homebrew 和 Winget，而 npm 包已弃用。它提供插件以扩展功能，并收集使用数据以改进产品，同时设有隐私保护措施。

rss · GitHub Trending - Python Daily · 7月3日 01:38

**背景**: Claude 是 Anthropic 开发的一系列大型语言模型，采用宪法 AI 技术进行训练，以提高伦理合规性。智能 AI（Agentic AI）指的是能够自主追求目标并使用工具的系统，Claude Code 通过在终端环境中协助编码任务，体现了这一概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI coding assistant`, `#developer tools`, `#Claude`, `#agentic`, `#natural language programming`

---

<a id="item-13"></a>
## [Meta 开源 Astryx 设计系统，含 150+ 组件](https://github.com/facebook/astryx) ⭐️ 8.0/10

Meta 开源了 Astryx，这是一个完全可定制的 React 应用设计系统，包含 150 多个无障碍组件、品牌级主题、暗色模式、CLI 以及 AI 就绪工具。 作为 Meta 内部最常用、支撑超过 13,000 个应用的设计系统，Astryx 提供了一个成熟且经过生产验证的基础，能够显著提升 React 项目的开发效率和一致性。其面向 AI 代理的设计也顺应了 AI 辅助开发日益增长的趋势。 Astryx 基于 React 和 Meta 自有的 StyleX CSS-in-JS 库构建，但开发者可以通过 className 使用任何 CSS 方案覆盖样式。它还提供了 swizzle 机制，可以将完整组件源码弹出到项目中进行深度定制。

rss · GitHub Trending - TypeScript Daily · 7月3日 01:40

**背景**: 设计系统是一套可复用的 UI 组件、指南和工具，帮助团队高效构建一致的用户界面。Astryx 在 Meta 内部历经八年开发，现以 MIT 许可证开源，利用 StyleX 实现编译时 CSS 优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/stylex">Stylex</a></li>

</ul>
</details>

**标签**: `#design-system`, `#react`, `#open-source`, `#meta`, `#ui-components`

---

<a id="item-14"></a>
## [微软推出'Skills'仓库，为 AI 编码代理提供落地能力](https://github.com/microsoft/skills) ⭐️ 8.0/10

微软在 GitHub 上发布了一个名为'skills'的新开源仓库，提供了使用 MCP 服务器、自定义代理和 AGENTS.md 模板构建落地编码代理的框架，包含了超过 175 个针对 Azure SDK 和 Microsoft AI Foundry 的预构建技能。 该仓库通过提供领域特定的上下文和激活模式，解决了编码代理的一个关键局限，使 AI 代理在现实软件开发任务中更加可靠和有效，特别是在微软生态系统内。 这些技能可以通过简单的 npx 命令（npx skills add microsoft/skills）安装到代理目录中，例如用于 GitHub Copilot 的.github/skills/目录，并且该仓库正处于积极开发中，有持续的添加和改进，如'正在进行中'的提示所示。

rss · GitHub Trending - TypeScript Daily · 7月3日 01:40

**背景**: 编码代理（如 GitHub Copilot）利用大语言模型辅助代码生成和软件任务，但它们通常缺乏关于项目 SDK、API 和内部代码库的领域特定上下文，导致生成泛化或不正确的建议。落地（Grounding）是指将代理行为锚定在实际项目代码和文档中以提高准确性。MCP（模型上下文协议）服务器提供了一种标准化的方式，将外部工具和数据源暴露给 AI 代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mcpservers.org/">Awesome MCP Servers</a></li>
<li><a href="https://bitoai.my/product/grounded-coding/">Grounded coding with AI Architect | Bito</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#AI Agents`, `#MCP`, `#SDK`, `#GitHub`

---

<a id="item-15"></a>
## [MCP Apps 协议让 AI 聊天机器人支持交互式 UI](https://github.com/modelcontextprotocol/ext-apps) ⭐️ 8.0/10

Anthropic、OpenAI 及 MCP 社区联合发布了 MCP Apps 协议的官方规范与 SDK，该协议允许 MCP 服务器提供交互式 UI（如图表、表单、仪表板），并直接在 Claude 和 ChatGPT 等 AI 聊天机器人中渲染。 这为在 AI 聊天机器人中嵌入丰富的用户界面提供了标准化方案，使得超出纯文本的更复杂、更交互式的对话成为可能，是推动 AI 实际应用和 MCP 生态发展的重要一步。 MCP Apps 基于模型上下文协议 (MCP) 构建，使用标准 Web 技术（HTML、CSS、JavaScript）进行 UI 渲染。其 SDK 已发布在 npm 上（@modelcontextprotocol/ext-apps），且该协议已获得 Claude 和 ChatGPT 等兼容聊天客户端的支持。

rss · GitHub Trending - TypeScript Daily · 7月3日 01:40

**背景**: 模型上下文协议 (MCP) 是 Anthropic 于 2024 年 11 月推出的开放标准，旨在规范 AI 系统与外部工具和数据源的集成方式。MCP Apps 是 MCP 的第一个官方扩展（SEP-1865），旨在允许 MCP 服务器直接将交互式 UI 组件交付到聊天界面中，从而大幅扩展 AI 助手的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://serpapi.com/blog/mcp-apps-with-fastmcp-interactive-ui/">MCP Apps with FastMCP: Turning Tool Output Into Interactive UI</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#MCP`, `#UI`, `#AI Chatbots`, `#Protocol`, `#Specification`

---

<a id="item-16"></a>
## [uv：基于 Rust 的超快速 Python 包管理器](https://github.com/astral-sh/uv) ⭐️ 8.0/10

Astral 发布了用 Rust 编写的 Python 包和项目管理工具 uv，声称比 pip 快 10-100 倍，并取代了 pip、poetry、pyenv 等多个现有工具。 uv 解决了 Python 包管理中长期存在的瓶颈，特别是安装速度和工具碎片化问题，有望显著提升开发效率。其背后是 Ruff 的创建者 Astral，这增强了可信度，并表明用 Rust 替换 Python 工具的趋势正在增长。 uv 通过 Rust 实现和全局依赖缓存实现高速，可通过 curl 或 pip 安装，无需预装 Rust 或 Python。它还提供兼容 pip 的接口以方便迁移，并支持类似 Cargo 的工作区以应对大规模项目。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: Python 的包管理传统上涉及多个工具，如用于安装包的 pip、用于依赖管理的 poetry、用于 Python 版本管理的 pyenv 等。这些工具本身通常用 Python 编写，导致性能开销。uv 是更广泛的用 Rust 重写 Python 核心基础设施运动的一部分，此前已有 Ruff（快速 linter）、PyO3/maturin 等成功案例。

**标签**: `#Rust`, `#Python`, `#package manager`, `#developer tools`

---

<a id="item-17"></a>
## [Tree-sitter：编程工具的增量解析库](https://github.com/tree-sitter/tree-sitter) ⭐️ 8.0/10

Tree-sitter 是一个增量解析系统，能够为源代码文件构建具体语法树，并在每次按键编辑时高效地更新树结构。它被广泛应用于 Neovim、Atom、Emacs 等文本编辑器，用于语法高亮和代码分析。 通过在每次编辑时进行快速而稳健的解析，tree-sitter 显著提升了语法高亮、代码折叠、语义导航等 IDE 功能的响应速度和准确性。这使其成为现代开发者工具的基础构件。 运行时库采用纯 C 语言编写，无依赖，便于嵌入任何应用。它提供了 Rust 和 WebAssembly 的绑定，以及用于从语法文件生成解析器的命令行接口。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: 增量解析是一种仅重新解析文件中发生变化的部分，而非整个文件的技术，从而能在大型代码库中实现实时更新。具体语法树（CST）精确保留源文本中所有的句法细节，而抽象语法树（AST）可能会省略某些标记。Tree-sitter 结合了这些概念，生成精确的语法树，并能够以最小的延迟进行增量更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Concrete_syntax_tree">Concrete syntax tree</a></li>
<li><a href="https://stackoverflow.com/questions/1888854/what-is-the-difference-between-an-abstract-syntax-tree-and-a-concrete-syntax-tre">parsing - What is the difference between an Abstract Syntax Tree and...</a></li>
<li><a href="https://offlinetools.org/a/json-formatter/incremental-parsing-for-responsive-json-formatting">Incremental Parsing for Responsive JSON Formatting | Offline Tools</a></li>

</ul>
</details>

**标签**: `#parsing`, `#syntax tree`, `#programming tools`, `#incremental parsing`

---

<a id="item-18"></a>
## [Rolldown：基于 Rust 的 JavaScript/TypeScript 打包器，兼容 Rollup API](https://github.com/rolldown/rolldown) ⭐️ 8.0/10

Rolldown 是一个用 Rust 编写的全新 JavaScript/TypeScript 打包器，提供与 Rollup 兼容的 API 和插件接口。它旨在成为 Vite 未来的打包器。 Rolldown 结合了 Rust 的性能和 Rollup 熟悉的 API，可能为大规模 JavaScript/TypeScript 项目提供显著更快的构建速度。它作为 Vite 未来打包器的采用可能重塑工具链生态。 Rolldown 由 VoidZero Inc. 开发，并作为 npm 包发布。它支持多种平台，包括 macOS、Linux、Windows 以及通过 WASM 支持 WebAssembly。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: 打包器是一种将多个 JavaScript 或 TypeScript 模块合并成单个文件以便在浏览器中使用的工具。Rollup 是流行的打包器，以其摇树优化和插件生态闻名；esbuild 是用 Go 编写的快速打包器。Rolldown 旨在结合两者优点：Rollup 的 API 和 Rust 的速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rollupjs.org/">Rollup</a></li>

</ul>
</details>

**标签**: `#rust`, `#bundler`, `#javascript`, `#typescript`, `#performance`

---

<a id="item-19"></a>
## [Helix：基于 Rust 的后现代模态文本编辑器](https://github.com/helix-editor/helix) ⭐️ 8.0/10

Helix 是一款用 Rust 编写的后现代模态文本编辑器，受 Kakoune 和 Neovim 启发，凭借其速度、内置语言服务器支持和 tree-sitter 集成，在开发者社区中获得了广泛关注。 Helix 代表了新一代基于终端的编辑器，将模态编辑的效率与多选、原生 LSP 支持等现代功能相结合，对 Vim 和 Neovim 等成熟编辑器构成了挑战。 Helix 使用 tree-sitter 进行增量语法高亮和代码编辑，并将 Kakoune 的多选作为核心范式。它主要基于终端，但计划探索使用 wgpu 的自定义 GUI 渲染器。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: 模态编辑器是一种具有插入、导航和执行命令等不同模式的文本编辑器，由 Vim 普及。多选允许同时编辑多个光标位置，提高生产力。Tree-sitter 是一个用于快速增量解析的解析器生成工具，支持智能语法高亮和代码导航。语言服务器协议（LSP）为自动补全和诊断等语言特定功能提供了标准化接口。Helix 将这些功能全部打包到一个 Rust 二进制文件中，以实现高性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://helix-editor.com/">Helix</a></li>
<li><a href="https://grokipedia.com/page/Helix_text_editor">Helix (text editor)</a></li>
<li><a href="https://phoenixnap.com/glossary/modal-editor">What Is a Modal Editor ? | phoenixNAP IT Glossary</a></li>

</ul>
</details>

**标签**: `#text editor`, `#rust`, `#modal editor`, `#open source`

---

<a id="item-20"></a>
## [ttl：一款基于 Rust 的现代 traceroute 替代工具](https://github.com/lance0/ttl) ⭐️ 8.0/10

ttl 是一款用 Rust 编写的新型网络诊断工具，提供实时 TUI、逐跳统计、ASN/GeoIP 查询、ECMP 检测、MPLS 标签解析等众多高级功能。它旨在成为经典 mtr 工具的更好替代品。 该工具将路径 MTU 发现、NAT 检测、路由抖动告警等功能集成到一个快速、可脚本化的应用中，从而实现了网络诊断的现代化。它有益于网络工程师、系统管理员以及任何需要详细网络路径分析的人。 ttl 支持巴黎/都柏林 traceroute 以枚举 ECMP 路径，支持二分查找路径 MTU 发现，通过源端口重写检测 NAT，并从 ICMP 扩展中解析 MPLS 标签。它提供可脚本化的输出格式（JSON、CSV、文本）以及带有 Prometheus 导出器的守护进程模式。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: Traceroute 是一种经典的网络诊断工具，用于追踪数据包到目的地所经过的路径，显示每一跳的 IP 地址和延迟。传统 traceroute 缺乏 ECMP 检测（识别负载均衡路径）和 MPLS 标签解析（解码 MPLS 网络中的标签）等功能。ttl 使用以性能和安全性著称的系统编程语言 Rust 构建，集成了这些高级功能，并提供了实时可视化以及来自 ASN 和 GeoIP 等外部数据库的丰富信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lance0/ttl">GitHub - lance0/ttl: Fast, modern traceroute with real-time TUI, per-hop...</a></li>
<li><a href="https://ru.wikipedia.org/wiki/MPLS">MPLS — Википедия</a></li>

</ul>
</details>

**标签**: `#Rust`, `#networking`, `#traceroute`, `#CLI`, `#tool`

---

<a id="item-21"></a>
## [wgpu：安全、跨平台的 Rust 图形 API](https://github.com/gfx-rs/wgpu) ⭐️ 8.0/10

wgpu 是一个成熟的纯 Rust 实现，遵循 WebGPU 标准，原生支持 Vulkan、Metal、D3D12 和 OpenGL，并在浏览器中支持 WebGL2 和 WebGPU。它已被 Firefox、Servo 和 Deno 等重大项目采用。 wgpu 为 Rust 开发者提供了一个安全且现代的图形 API，无需不安全代码即可实现跨平台 GPU 计算和渲染。它被关键浏览器和运行时采用，使其成为 WebGPU 在 Web 和原生应用未来发展的基石。 该 API 与 WebGPU 规范镜像，但专为 Rust 定制，提供零成本抽象并与 Rust 生态系统无缝集成。wgpu 还通过 wgpu-native 提供 C 绑定，以供 C++ 等其他语言使用。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: WebGPU 是由 W3C 标准化的下一代图形 API，旨在取代 WebGL，为 Web 提供底层 GPU 访问。Rust 是一种注重安全性和性能的系统编程语言。wgpu 连接了这两个生态系统，使 Rust 开发者能够编写跨多种硬件后端运行且完全安全的 GPU 代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU - Wikipedia</a></li>
<li><a href="https://www.w3.org/TR/webgpu/">WebGPU - W3C</a></li>
<li><a href="https://en.wikipedia.org/wiki/Graphics_processing_unit">Graphics processing unit - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Rust`, `#graphics`, `#WebGPU`, `#cross-platform`, `#API`

---

<a id="item-22"></a>
## [FFF：面向 AI 代理和开发者的快速文件搜索 SDK](https://github.com/dmtrKovalenko/fff) ⭐️ 8.0/10

一款名为 'fff' 的新型文件搜索 SDK 已发布，提供容错路径和内容搜索、基于频率和最近访问的排序以及后台监视器。它声称在长时间运行的进程中比 ripgrep 和 fzf 更快。 该工具弥合了传统 CLI 文件搜索工具与 AI 代理需求之间的差距，提供了可集成多种语言和 MCP 服务器的库。它能显著提升开发者在代码导航中的生产力以及 AI 代理的效率。 FFF 支持 Rust、C、Python、Bun、NodeJS，并为 Claude Code 等 AI 代理提供 MCP 服务器。它使用 SIMD 加速的模糊匹配和 Smith-Waterman 评分进行内容搜索。

rss · GitHub Trending - Rust Daily · 7月3日 01:39

**背景**: 传统的文件搜索工具如 ripgrep 和 fzf 针对单次搜索优化，但重复搜索时有开销。频率-最近访问排序结合了使用频率和最近访问时间，优先显示常用文件；而容错搜索算法如 Smith-Waterman 允许即使在输入错误时也能匹配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/dmtrKovalenko/fff">dmtrKovalenko/fff: The fastest and the most accurate file search SDK...</a></li>
<li><a href="https://www.aitoolnet.com/fff">fff - Fast, resident-memory file search for AI agents - Aitoolnet</a></li>

</ul>
</details>

**标签**: `#file-search`, `#SDK`, `#Rust`, `#AI-agents`, `#developer-tools`

---

<a id="item-23"></a>
## [Ollama：本地运行开源大语言模型](https://github.com/ollama/ollama) ⭐️ 8.0/10

Ollama 是一个广受欢迎的开源工具，它允许用户在本地计算机上直接运行 DeepSeek、Qwen 和 Gemma 等大语言模型，并提供命令行界面、REST API 以及与编码助手的集成。 通过支持在本地运行强大的 AI 模型，Ollama 普及了先进 AI 的访问，减少了云服务依赖，并增强了数据隐私，这对于寻求经济高效且私密的 AI 推理的开发者与研究人员而言意义重大。 Ollama 利用 llama.cpp 作为主要后端实现高效推理，并提供官方的 Python 和 JavaScript 库。它还通过简单的 'ollama launch' 命令与 Claude Code 和 Copilot CLI 等工具集成。

rss · GitHub Trending - Go Daily · 7月3日 01:35

**背景**: 大语言模型通常通过云端 API 访问，这可能成本高昂并引发隐私问题。Ollama 通过允许用户在自有硬件上本地运行开放权重模型解决了这一问题。DeepSeek 和 Qwen 等模型因其竞争性性能和低成本而广受欢迎的开源替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLM`, `#open-source`, `#local-inference`, `#Go`

---

<a id="item-24"></a>
## [桥水研究：前沿 AI 模型金融判断准确率未达 80%](https://www.ithome.com/0/972/445.htm) ⭐️ 8.0/10

桥水基金旗下 AIA Labs 与 Thinking Machines Lab 测试了 GPT、Claude、Gemini 等前沿 AI 模型在基础金融判断任务上的表现，发现即使使用专家提示词，准确率也仅有 50-70%。而基于开源 Qwen3-235B 微调的模型达到了 84.7% 的准确率，推理成本仅为前沿模型的约十四分之一。 这项研究挑战了前沿 AI 模型在专业金融任务上更优的假设，表明微调的开源模型能以极低成本超越它们。它强调了专有数据和领域特定微调的价值，对受监管行业中的 AI 部署具有启示意义。 微调模型基于 Qwen3-235B，使用 Tinker 平台和 CISPO 损失函数、非对称裁剪、同策略蒸馏等技术。该模型相比最佳前沿模型（78.2%）错误率降低了 29.8%，推理成本仅约为其十四分之一。

rss · IT之家 · 7月3日 13:51

**背景**: GPT-4、Claude 等前沿 AI 模型是在海量数据上训练的大型语言模型，但未经微调时在专业任务上常表现不佳。微调是利用标注数据将预训练模型适配到特定领域的过程。金融判断任务需要复制专家直觉，难以形式化，因此成为具有挑战性的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/tinker/">Tinker - Thinking Machines Lab</a></li>
<li><a href="https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/CISPO.html">Clipped Importance Sampling Policy Optimization ( CISPO ) — swift...</a></li>
<li><a href="https://langdb.ai/app/models/deepinfra/qwen3-235b-a22b-2507">qwen 3 - 235 b -a22b-2507 by deepinfra | AI Model Pricing... | LangDB</a></li>

</ul>
</details>

**标签**: `#AI`, `#Finance`, `#Fine-tuning`, `#Open-source`, `#Large Language Models`

---

<a id="item-25"></a>
## [生数科技发布 Vidu S1：支持实时视频通话与语音控制](https://www.ithome.com/0/972/436.htm) ⭐️ 8.0/10

生数科技发布了 Vidu S1 模型，支持实时视频通话和语音控制视频走向，采用自回归扩散模型技术。用户可以通过语音指令与数字角色进行无限时长连续互动。 这标志着交互式 AI 的重要进步，将实时视频生成与语音控制相结合，实现动态持续的互动。可能对虚拟助手、直播、数字人等领域产生深远影响。 Vidu S1 支持 540P 分辨率、25 FPS 帧率（最高 42FPS），可基于真人、动漫、宠物等形象创建交互角色并个性化音色。它采用自回归扩散模型，基于历史画面和语音指令逐帧生成视频。

rss · IT之家 · 7月3日 13:00

**背景**: 自回归扩散模型结合了自回归生成与扩散过程。自回归模型逐步生成数据，依赖之前输出；扩散模型是一种通过学习逆转加噪过程来生成的模型。Vidu S1 将两者结合，实现实时连续视频生成并响应语音指令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cloud.tencent.com/developer/article/2508274">爆火Block Diffusion引发LLM...</a></li>
<li><a href="https://www.dongaigc.com/a/autoregressive-diffusion-pytorch">Autoregressive Diffusion: 基于PyTorch的 自 回 归 扩 散 模 型 实现 - 懂AI</a></li>

</ul>
</details>

**标签**: `#AI`, `#real-time video`, `#voice control`, `#diffusion model`, `#interactive AI`

---

<a id="item-26"></a>
## [京东物流在京启动国内首个 L4 自动驾驶重卡载货示范](https://www.ithome.com/0/972/419.htm) ⭐️ 8.0/10

2025 年 7 月 3 日，京东物流联合中国重汽和嬴彻科技，正式启动国内快递行业首个 L4 级自动驾驶重卡载货示范，在 31 公里路线上满载 43 吨货物运行。 这一里程碑将自动驾驶卡车从测试推向实际物流应用，打通了末端与长途干线自动化之间的衔接，有望降低运输成本并提升货运效率。 车辆搭载嬴彻科技全栈自研的 L4 级自动驾驶系统，融合激光雷达、毫米波雷达与多目视觉感知。系统构建了“车端自主决策+云端实时监控+远程应急处置”三级安全保障，主驾配备安全员。

rss · IT之家 · 7月3日 11:25

**背景**: L4 级自动驾驶意味着车辆可在特定条件下无需人工干预完成所有驾驶任务，但限于规定的运行设计域。北京高级别自动驾驶示范区提供了超过 100 平方公里的智能道路基础设施。京东物流此前已在无人配送车、无人机等领域深耕，此次扩展至重型卡车。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Inceptio_Technology">Inceptio Technology - Wikipedia</a></li>
<li><a href="https://english.beijing.gov.cn/investinginbeijing/WhyBeijing/DistrictsParks/Economic_Area/Key_industrial_parks/202501/t20250110_3985832.html">Beijing High - Level Autonomous Driving Demonstration Zone</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#logistics`, `#L4 autonomous truck`, `#JD Logistics`, `#freight`

---

<a id="item-27"></a>
## [阿里因隐藏后门全面禁用 Anthropic 产品](https://www.36kr.com/p/3879721635361032) ⭐️ 8.0/10

阿里巴巴内部下发通知，自 7 月 10 日起全面禁用所有 Anthropic 产品，包括 Claude、Claude Code、Sonnet、Opus 和 Fable。此前 Claude Code 被曝存在隐藏后门，可悄然检测中国用户并篡改系统提示词。 这标志着中国科技公司对外国 AI 工具信任的重大转变，阿里从鼓励使用外部模型转向安全优先。该事件可能促使其他中国企业重新评估对非本土闭源 AI 工具的依赖。 该后门自 Claude Code 2.1.91 版本（2026 年 4 月）起存在，它检查系统时区和代理设置是否关联中国实体，然后悄悄用不可见的 Unicode 字符修改系统提示词以回传数据。Anthropic 承认了该问题并于 7 月 2 日回滚了变更。

rss · 36氪 - 24小时热榜 · 7月3日 10:15

**背景**: Claude Code 是一个拥有文件系统和 Shell 执行权限的 AI 编码代理，因此是开发环境中的敏感工具。该后门利用隐写术将指纹数据隐藏在看似正常的提示词中，引发了严重的安全和信任问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digg.com/tech/misirerb">It reportedly detects local timezone settings when proxies are enabled</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/72518">[BUG] Anthropic embedded spyware in Claude Code · Issue #72518...</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/anthropic-tried-to-spy-on-chinese-claude-users-through-hidden-code-now-faces-backlash-2938754-2026-07-02">Anthropic tried to spy on Chinese Claude users through hidden code ...</a></li>

</ul>
</details>

**标签**: `#security`, `#AI`, `#Anthropic`, `#Claude`, `#Alibaba`

---

<a id="item-28"></a>
## [百度 AI 芯片昆仑芯冲刺 500 亿美元港股 IPO](https://www.36kr.com/p/3879603134312449) ⭐️ 8.0/10

百度旗下 AI 芯片公司昆仑芯正在推进港股 IPO，目标估值约 500 亿美元，并要求潜在基石投资者承诺采购价值为其认购额 3 至 7 倍的芯片。 此次 IPO 可能使昆仑芯估值超过母公司百度，标志着中国 AI 硬件领域的重要里程碑，并反映出在美国出口限制背景下国产 AI 加速器需求的激增。 昆仑芯主力产品为 2024 年上市的 P800，面向数据中心推理场景，随后是 2026 年初的 M100 和 2027 年的 M300 用于大规模训练。公司在 2025 年中国 AI 加速器服务器市场占有 11.6%份额，与寒武纪并列国产厂商第三位。

rss · 36氪 - 24小时热榜 · 7月3日 09:29

**背景**: 昆仑芯前身为百度 2011 年创立的内部 AI 芯片团队，2021 年独立为子公司，当时估值约 130 亿元。公司开发面向云到边缘场景的 AI 加速器，利用百度的生态系统包括飞桨深度学习框架。其芯片用于百度的搜索、云和自动驾驶业务，以及中国移动等外部客户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kunlunxin">Kunlunxin - Wikipedia</a></li>
<li><a href="https://www.zdnet.com/article/baidu-creates-kunlun-silicon-for-ai/">Baidu creates Kunlun silicon for AI | ZDNET</a></li>

</ul>
</details>

**标签**: `#IPO`, `#AI chips`, `#Baidu`, `#Kunlun Chip`, `#semiconductor`

---

<a id="item-29"></a>
## [华为 Mate 80 Pro 游戏能效超越骁龙 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

极客湾的评测显示，华为 Mate 80 Pro 系列搭载麒麟 9030 芯片，在原生鸿蒙优化下，游戏能效超越骁龙 8 Gen3。 这表明华为的软硬件协同优化可以克服制程劣势，可能重塑移动芯片格局，并为用户提供不牺牲性能的更长续航。 Mate 80 Pro Max 运行《原神》60 帧时整机功耗仅 4.9W，《王者荣耀》120 帧时约 3W，而 CPU 多核能效介于骁龙 8 Gen2 和 8 Gen3 之间。

telegram · bilibili 排行榜-全站 · 7月3日 13:27

**背景**: 麒麟 9030 系列据信采用 7nm 工艺，拥有 9 核 CPU 和马良 935 GPU，晶体管规模约 150 亿。华为的“软硬芯云”一体化是一种系统级优化，协同操作系统、硬件、芯片和云端资源，提升实际性能超越纸面规格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.zol.com.cn/article/10921163.html">华为 麒 麟 9030 系列发布 性能追赶国际主流但存制程差距-中关村在线</a></li>
<li><a href="https://post.smzdm.com/p/adozp02z/">麒 麟 9030 芯 片 性能显著提升_CPU_什么值得买</a></li>
<li><a href="http://www.fengsung.com/n-251230145203716.html">fengsung.com/n-251230145203716.html</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile processors`, `#energy efficiency`

---

<a id="item-30"></a>
## [原生低秩分解提升 Transformer 训练效率](https://www.reddit.com/r/MachineLearning/comments/1umtiqk/training_transformers_where_every_layer_w_vu%E1%B5%80/) ⭐️ 8.0/10

一种称为原生分解权重（NFW）的新方法从初始化开始就将 Transformer 中的每个线性层替换为低秩分解 W = V·U^T，从头训练，无需事后压缩或适配器。 NFW 以更少的参数实现了比稠密基线更好的困惑度，揭示了由语料库决定的最优秩，能防止记忆化并提高泛化能力，有望引领更参数高效的模型设计。 在 WikiText-2 上使用隐藏维度 2048 的 4 层 Transformer，秩为 32 的 NFW 实现了验证集困惑度 5.617，而稠密基线为 6.219，且参数更少、结合 dropout 时保持稳定；最优秩 r*受欠拟合和记忆化阈值的约束。

reddit · r/MachineLearning · /u/MrAddams_LibraLogic · 7月3日 23:33 · [社区讨论](https://www.reddit.com/r/MachineLearning/comments/1umtiqk/training_transformers_where_every_layer_w_vuᵀ/)

**背景**: 低秩分解将一个大权重矩阵分解为两个较小的矩阵，从而减少参数。LoRA 仅在预训练模型的微调中应用此方法，而 NFW 从一开始就使用低秩结构，使其成为固有属性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2602.12429">Stabilizing Native Low-Rank LLM Pretraining</a></li>
<li><a href="https://proceedings.mlsys.org/paper_files/paper/2023/file/c2db3ef0b1ad4c5ec7c3a0a0c6f6c832-Paper-mlsys2023.pdf">Cuttlefish: Low - rank Model Training without All The Tuning</a></li>

</ul>
</details>

**标签**: `#transformers`, `#low-rank factorization`, `#efficient deep learning`, `#parameter efficiency`, `#machine learning research`

---

<a id="item-31"></a>
## [Anthropic 指控阿里巴巴发动大规模蒸馏攻击窃取 Claude 能力](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic 指控阿里巴巴通过 2.5 万个欺诈账户，在 2026 年 4 月 22 日至 6 月 5 日期间发动了针对其 Claude AI 模型的最大规模蒸馏攻击，非法提取模型能力。 这一指控凸显了 AI API 中的关键安全漏洞，并加剧了领先 AI 公司之间的知识产权争夺，可能影响未来关于模型保护的法规。 Anthropic 报告称，这些欺诈账户与 Claude 进行了超过 2880 万次交互，且攻击与阿里巴巴的 AI 实验室 Qwen 有关联。

telegram · zaihuapd · 7月3日 06:21

**背景**: 模型蒸馏是一种技术，通过让较弱模型学习更强模型的输出来高效复制能力。蒸馏攻击则指未经授权使用该技术窃取专有模型。Anthropic 此前已发布过检测此类攻击的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks : What They Are and Why... | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Model Distillation`, `#Intellectual Property`, `#Anthropic`, `#Alibaba`

---

<a id="item-32"></a>
## [NASA 发射 LINK 航天器救援 Swift 望远镜](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

NASA 于 2025 年 7 月 3 日发射 LINK 航天器，与老化的 Swift 伽马射线暴天文台会合，并将其轨道提升约 240 公里，防止其今年晚些时候坠入地球大气层烧毁。 这次任务是私人航天器首次尝试捕获并提升美国政府卫星的轨道，展示了在轨服务能力，有助于减少太空垃圾并延长宝贵科学仪器的寿命。 LINK 将使用机械臂抓住 Swift，并在数月内缓慢提升其高度。Swift 于 2004 年发射，已在轨运行超过 20 年，由于太阳活动增加，其轨道衰减速度加快。

telegram · zaihuapd · 7月3日 15:43

**背景**: 在轨卫星服务包括在太空中为卫星加油、提升轨道或维修。Swift 是一台伽马射线暴观测站，取得了重大发现。如果不进行干预，它将于 2025 年 10 月左右坠入地球大气层。LINK 航天器由一家私人公司建造，代表了商业太空服务的新时代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift... - NASA</a></li>
<li><a href="https://en.wikipedia.org/wiki/On-orbit_satellite_servicing">On-orbit satellite servicing</a></li>

</ul>
</details>

**标签**: `#space`, `#NASA`, `#satellite rescue`, `#astronomy`, `#space technology`

---

<a id="item-33"></a>
## [腾讯玄武实验室阿图因 AI 在 CyberGym 测试中超越 Mythos](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

腾讯玄武实验室宣布，其研发的阿图因 AI 在加州大学伯克利分校主导的 CyberGym 网络安全基准测试中获得 84.0%的得分，超过 Anthropic 的 Claude Mythos Preview。该工具基于可本地部署的开源模型 GLM-5.1 构建，消耗的预算不到 Mythos 的 0.1%。 这表明在开源 AI 应用于现实网络安全领域取得了重大突破，以极低的成本超越专有模型。它展示了可访问的 AI 能够发现其他系统遗漏的关键漏洞，有望提升整个行业的软件安全性。 阿图因 AI 在 curl、gnark、OpenSSL、Python cryptography、Java bc-java 等重要项目中发现了多个高危逻辑漏洞，评分最高达 9.3。在伯克利 BVI 真实世界漏洞榜单中，其严重漏洞严重程度排名第 1，总数排名第 5。

telegram · zaihuapd · 7月3日 16:12

**背景**: CyberGym 是一个大规模网络安全评估框架，基于 188 个开源项目中的 1507 个真实漏洞，旨在评估 AI 代理的漏洞分析能力。GLM-5.1 是由 Z.ai（原智谱 AI）开发的开源大语言模型，自 2025 年 7 月起以 MIT 许可证发布，具有强大的编码能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cybergym.io/cybergym/">CyberGym : Evaluating AI Agents' Real-World Cybersecurity...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.1">GLM 5.1</a></li>
<li><a href="https://www.xugj520.cn/archives/cybergym-ai-cybersecurity-test.html">CyberGym 揭示AI 网 络 安 全 真实水平：1507个漏洞挑战下仅12...</a></li>

</ul>
</details>

**标签**: `#AI安全`, `#网络安全`, `#基准测试`, `#开源模型`, `#漏洞挖掘`

---