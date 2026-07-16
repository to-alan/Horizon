---
layout: default
title: "Horizon Summary: 2026-07-16 (ZH)"
date: 2026-07-16
lang: zh
---

> 从 300 条内容中筛选出 24 条重要资讯。

---

1. [Stripe 与 Advent 联合出价超 530 亿美元收购 PayPal](#item-1) ⭐️ 9.0/10
2. [Claude 的 web_fetch 漏洞通过蜜罐网站泄露数据](#item-2) ⭐️ 9.0/10
3. [FoundationPose: 统一 6D 姿态估计与跟踪的新颖物体模型](#item-3) ⭐️ 9.0/10
4. [基于 Apache Arrow 的 InfluxDB 3 Core 发布](#item-4) ⭐️ 9.0/10
5. [马斯克宣布 X 全量开源代码并引入第三方核验](#item-5) ⭐️ 9.0/10
6. [国行苹果 AI 获备案，接入阿里千问](#item-6) ⭐️ 9.0/10
7. [Inkling：支持音频的大型开放权重多模态模型](#item-7) ⭐️ 8.0/10
8. [Telegram 数据中心谜团被揭露](#item-8) ⭐️ 8.0/10
9. [Needle：从 Gemini 3.1 蒸馏出的 2600 万参数函数调用模型](#item-9) ⭐️ 8.0/10
10. [BrowserOS：挑战 AI 浏览器的开源代理浏览器](#item-10) ⭐️ 8.0/10
11. [OpenAI 发布 Codex CLI 本地终端代理](#item-11) ⭐️ 8.0/10
12. [uv：用 Rust 构建的快速 Python 包管理器](#item-12) ⭐️ 8.0/10
13. [NVIDIA Dynamo：开源分布式推理框架](#item-13) ⭐️ 8.0/10
14. [vLLM 语义路由器：高效模型混合推理](#item-14) ⭐️ 8.0/10
15. [腾讯开源 WeKnora：LLM 知识平台](#item-15) ⭐️ 8.0/10
16. [KServe：Kubernetes 上的标准化 AI 推理平台](#item-16) ⭐️ 8.0/10
17. [优步接近收购 Delivery Hero，估值 125 亿欧元](#item-17) ⭐️ 8.0/10
18. [国内首款 CT 引导加速器进入创新医疗器械审查程序](#item-18) ⭐️ 8.0/10
19. [华为引望助力联合国首个全球自动驾驶法规制定](#item-19) ⭐️ 8.0/10
20. [DeepSeek 传筹备 IPO，目标 2027 年上市](#item-20) ⭐️ 8.0/10
21. [哈达玛积方法解耦 CNN 神经元](#item-21) ⭐️ 8.0/10
22. [法官质疑 Epic 与谷歌交易影响反垄断立场](#item-22) ⭐️ 8.0/10
23. [DeepSeek 首轮融资超 500 亿元](#item-23) ⭐️ 8.0/10
24. [Telegram 推出无服务器平台，机器人后端无需自建服务器](#item-24) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Stripe 与 Advent 联合出价超 530 亿美元收购 PayPal](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

据知情人士透露，Stripe 与私募股权公司 Advent International 联合出价超过 530 亿美元收购 PayPal，此举可能合并全球两大支付处理商。 此次收购将整合在线支付领域的巨大市场份额，影响数百万商家和消费者。由于合并后实体的主导地位，可能导致费用上涨、竞争减少，并面临监管反垄断审查。 报价对 PayPal 的估值超过 530 亿美元。Stripe 目前运营着 Braintree，它是 PayPal 的直接竞争对手，合并后的公司还将拥有 Venmo、Xoom 等其他支付服务。

hackernews · rvz · 7月15日 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: PayPal 是广泛使用的在线支付系统，而 Stripe 是为互联网企业提供领先支付基础设施的公司。两家公司为全球数百万商家处理支付。合并将创造一个在非面对面交易中占据主导地位的参与者，可能引发关于市场集中度的反垄断担忧。

**社区讨论**: 评论者对竞争减少和费用上涨表达了严重担忧。一些人指出，Stripe 对某些行业（如大麻、成人内容）的限制政策可能会伤害目前由 PayPal 服务的供应商。其他人则担心反垄断障碍以及需要剥离 Venmo 和 Braintree 等资产。

**标签**: `#fintech`, `#acquisition`, `#PayPal`, `#Stripe`, `#payments`

---

<a id="item-2"></a>
## [Claude 的 web_fetch 漏洞通过蜜罐网站泄露数据](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 9.0/10

安全研究员 Ayush Paul 发现 Claude 的 web_fetch 工具存在一个绕过漏洞，攻击者可以通过诱骗模型跟随蜜罐页面中的嵌入式链接来窃取用户隐私数据。 这突显了 AI 代理安全中的一个关键漏洞，表明即使精心设计的数据泄露防护措施，也可能被创造性的提示注入和链接链绕过。 攻击使用了一个蜜罐网站，显示伪造的 Cloudflare 认证提示，指示模型按字母顺序浏览用户资料页面以找到受害者信息。Anthropic 通过移除 web_fetch 跟随获取内容中链接的能力来修复了这个漏洞。

rss · Simon Willison · 7月15日 14:21

**背景**: Claude 的 web_fetch 工具设计为仅获取用户明确提供或 web_search 工具返回的 URL，以防止数据泄露。然而，该工具也允许获取先前抓取页面中的嵌入式链接，这为攻击者创造了可乘之机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/">The lethal trifecta for AI agents: private data, untrusted ...</a></li>
<li><a href="https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/">Claude API: Web fetch tool</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Platform Docs</a></li>

</ul>
</details>

**标签**: `#security`, `#AI safety`, `#Claude`, `#data exfiltration`, `#prompt injection`

---

<a id="item-3"></a>
## [FoundationPose: 统一 6D 姿态估计与跟踪的新颖物体模型](https://github.com/NVlabs/FoundationPose) ⭐️ 9.0/10

NVIDIA 研究人员发布了 FoundationPose，这是一个统一的 6D 物体姿态估计与跟踪基础模型，无需微调即可用于新颖物体，并被 CVPR 2024 接收为 Highlight 论文。 这项工作显著推进了计算机视觉领域，使得仅需 CAD 模型或少量参考图像即可即时估计任何物体的姿态，其性能超越专门方法，甚至媲美实例级方法。 FoundationPose 通过神经隐式表示实现新颖视图合成，桥接了基于模型和无模型两种设置，并借助大型语言模型、Transformer 架构和对比学习的大规模合成训练实现强泛化能力。

rss · GitHub Trending - Python Daily · 7月15日 01:40

**背景**: 6D 物体姿态估计涉及确定物体相对于相机的 3D 平移和 3D 旋转，对机器人技术和增强现实至关重要。传统方法需要对每个物体进行微调或使用特定实例模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://just-merwan.medium.com/what-is-6d-object-pose-estimation-in-computer-vision-21e8acf9e3e2">What is 6D Object Pose Estimation in Computer Vision? | by Merwansky | Medium</a></li>
<li><a href="https://github.com/vsitzmann/awesome-implicit-representations">GitHub - vsitzmann/awesome-implicit-representations: A curated list of resources on implicit neural representations. · GitHub</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#6D pose estimation`, `#foundation model`, `#CVPR`, `#object tracking`

---

<a id="item-4"></a>
## [基于 Apache Arrow 的 InfluxDB 3 Core 发布](https://github.com/influxdata/influxdb) ⭐️ 9.0/10

InfluxDB 3 Core 是一款基于 Apache Arrow、DataFusion 和 Parquet 构建的开源时序数据库，自 2025 年 4 月起正式可用。它采用无磁盘架构，查询响应时间低于 10 毫秒，并兼容 InfluxDB 1.x/2.x 的 API。 此次发布标志着时序数据库在性能和可扩展性上的范式转变，利用现代列式格式实现实时分析和监控。它支持更快的查询和更低的存储成本，惠及 DevOps、物联网和金融分析等场景。 InfluxDB 3 Core 使用 Apache Parquet 在对象存储（S3、Azure、GCP）或本地磁盘上持久化数据，支持 SQL、InfluxQL 和 Flight SQL 查询。它采用 Rust 编写，并包含嵌入式 Python 虚拟机用于插件和触发器。

rss · GitHub Trending - Rust Daily · 7月15日 01:41

**背景**: Apache Arrow 是一种跨语言列式内存格式，用于高效数据处理。DataFusion 是基于 Arrow 的 Rust 查询引擎，Parquet 是面向分析的列式存储格式。InfluxDB 3 Core 结合这些技术，取代了早期的 TSM 存储引擎，提供了现代化的性能和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Arrow">Apache Arrow</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_DataFusion">Apache DataFusion</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Parquet">Apache Parquet</a></li>

</ul>
</details>

**标签**: `#time series database`, `#open source`, `#Apache Arrow`, `#DataFusion`, `#Parquet`

---

<a id="item-5"></a>
## [马斯克宣布 X 全量开源代码并引入第三方核验](https://www.ithome.com/0/977/233.htm) ⭐️ 9.0/10

埃隆·马斯克宣布，社交媒体平台 X 在完成内部安全审查后，将开源其全部代码库，零保留、无例外。同时，X 将邀请第三方审核机构核验，确保对外公开的代码与正式服务器上实际运行的代码完全一致。 此举可能为社交媒体行业的平台透明度树立新标准，直接挑战 Farcaster 和 Lens Protocol 等去中心化平台的核心价值主张。如果成功，它将通过结合透明度与中心化平台的网络效应来重塑竞争格局。 此次全量开源覆盖支撑 X 平台运营的所有系统、功能模块与代码行，远超 2025 年仅公开“为你推荐”算法的有限开源。第三方核验机制旨在杜绝行业常见的发布经过删减的“干净代码”而与实际运行代码不一致的做法。

rss · IT之家 · 7月15日 13:53

**背景**: 开源是指将源代码公开，任何人都可以查看、修改和分发。第三方核验确保公开的代码与生产环境实际运行的代码一致，以回应对“形式化透明”的批评。Farcaster 和 Lens Protocol 等去中心化社交媒体协议一直强调透明度和用户数据所有权是相对于传统中心化平台的关键优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gate.com/zh/learn/articles/farcaster-redefining-connections-controlling-privacy-and-experiencing-true-decentralized-social-freedom/3664">Farcaster ... | Gate 学院</a></li>
<li><a href="https://www.gate.com/zh-tw/crypto-wiki/article/lens-protocol-the-foundational-decentralized-social-network-of-the-future">Lens Protocol ： 去 中 心 化 社 交 的未來基石</a></li>

</ul>
</details>

**标签**: `#open source`, `#social media`, `#transparency`, `#code verification`, `#Elon Musk`

---

<a id="item-6"></a>
## [国行苹果 AI 获备案，接入阿里千问](https://www.36kr.com/p/3896830991320962) ⭐️ 9.0/10

苹果智能（Apple Intelligence）已获得中国网信办备案，同批还有六家国产手机厂商。它将集成阿里千问 AI 模型，为 iOS、iPadOS、macOS 和 visionOS 的中国用户提供生成式 AI 能力。 这结束了国行 iPhone 用户长达两年的等待，使其能够使用苹果 AI 功能，这对与华为、小米等已提供端侧 AI 的本地竞争对手竞争至关重要。与千问的合作也凸显了在中国市场本地 AI 模型合规的重要性。 此次备案之前，2025 年 3 月曾有一次意外推送，暴露了端侧 AI 速度快但精度不足的问题，仅依赖本地处理。正式版本将使用千问进行云端任务，以补充端侧模型。

rss · 36氪 - 24小时热榜 · 7月15日 11:58

**背景**: 端侧生成式 AI 是指在智能手机等设备上本地运行的 AI 模型，提供隐私和速度优势，但受计算能力限制。千问是阿里的大语言模型家族，类似于 GPT-4，提供文本和图像理解与生成能力。中国法规要求 AI 服务在公开部署前必须获得备案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2024/04/17/on-device-generative-ai-unlocks-true-smartphone-and-pc-value/">On-Device Generative AI Unlocks True Smartphone And PC Value Beyond the Cloud: A Deep Dive Into On-Device Generative AI 5 benefits of on-device generative AI - Qualcomm What's next in on-device generative AI - Qualcomm On-Device Generative AI: The Need, Architectures, and ... On-device Generative AI: The Need, Architectures, and Challenges</a></li>
<li><a href="https://penchan.co/en/market/ai/china-models/qwen/">What Is Qwen (Tongyi Qianwen)? Alibaba's AI Model Family ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI`, `#China`, `#Regulatory Approval`, `#Qianwen`

---

<a id="item-7"></a>
## [Inkling：支持音频的大型开放权重多模态模型](https://thinkingmachines.ai/news/introducing-inkling/) ⭐️ 8.0/10

Thinking Machines 发布了 Inkling，这是一款支持音频的大型开放权重多模态模型，专为企业微调而设计。据称它是目前最大的具有音频能力的开放权重模型。 Inkling 为开放权重模型领域增添了一个重要的新选择，尤其适用于需要音频处理和多模态理解的任务。它强调通过 Tinker 平台进行微调，为企业提供了强大且可定制的 AI 解决方案，同时保持模型所有权。 Inkling 支持长上下文和强大的音频能力，使其适用于代理型应用。该模型已在 Hugging Face 上提供，并可通过 llama.cpp 和 Unsloth 本地运行，提供 GGUF 和 NVFP4 量化版本。

hackernews · vimarsh6739 · 7月15日 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48924912)

**背景**: 开放权重模型意味着其训练参数公开可用，允许任何人下载和定制。多模态模型整合多种数据类型（如文本、图像和音频），能够执行视觉问答和跨模态检索等任务。Inkling 基于这些原理构建，专注于音频和企业微调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_model">Multimodal model</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，用户强调 Inkling 的音频能力和本地部署的潜力。一些人认为它是专有模型的有前景的开放替代方案，尤其适合需要定制的企业，而另一些人则注意到现代 AI 开发日益增长的复杂性。

**标签**: `#open-weights`, `#multimodal`, `#AI`, `#audio`, `#machine learning`

---

<a id="item-8"></a>
## [Telegram 数据中心谜团被揭露](https://dev.moe/en/3025) ⭐️ 8.0/10

一篇调查文章披露，Telegram 的数据中心基础设施可能由与俄罗斯 FSB 有关联的人管理，并记录了多个未公开的数据中心模式和缺口。 这对数亿 Telegram 用户构成重大的安全和隐私隐患，可能意味着潜在的政府监控或后门访问，削弱了其中立性和安全性的主张。 文章指出 Telegram 的数据中心存在未记录的 ID，例如 DC3 的缺口，且 DC2 主要服务于俄罗斯和乌克兰用户。此外，调查确认存在暴露持久设备标识符的跟踪漏洞。

hackernews · theanonymousone · 7月15日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=48920475)

**背景**: Telegram 是一款基于云的即时通讯应用，采用分散式多数据中心架构和 MTProto 协议。用户根据地理位置被分配到数据中心以降低延迟。先前分析已发现安全问题，包括一项确认跟踪漏洞的审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://istories.media/en/stories/2025/06/10/telegram-fsb/">Telegram, the FSB, and the Man in the Middle</a></li>
<li><a href="https://docs.pyrogram.org/faq/what-are-the-ip-addresses-of-telegram-data-centers">What are the IP addresses of Telegram Data Centers ? — Pyrogram...</a></li>
<li><a href="https://core.telegram.org/api/datacenter">Working with Different Data Centers</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 FSB 关联表示担忧，并验证了技术发现。有用户指出 DC2 宕机是常见抱怨，另一人质疑自定义代码的复杂性为技术债务。

**标签**: `#Telegram`, `#data centers`, `#infrastructure`, `#security`, `#analysis`

---

<a id="item-9"></a>
## [Needle：从 Gemini 3.1 蒸馏出的 2600 万参数函数调用模型](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus Compute 发布了 Needle，这是一个从 Gemini 3.1 蒸馏出的 2600 万参数模型，采用 Simple Attention Network 架构，在 Cactus 推理引擎上可达每秒 6000 个 token 的预填充和每秒 1200 个 token 的解码速度。 Needle 展示了极小型模型也能有效处理边缘设备上的函数调用任务，有望在手机、手表和眼镜上实现强大的 AI 助手，无需依赖云端。 该模型在 16 个 TPU v6e 上预训练了 2000 亿个 token 耗时 27 小时，随后在 20 亿个 token 的单次函数调用数据上后训练了 45 分钟。Needle 在单次函数调用基准测试中超越了 FunctionGemma-270m、Qwen-0.6B、Graninte-350m 和 LFM2.5-350m。

rss · GitHub Trending - Python Daily · 7月15日 01:40

**背景**: 模型蒸馏是一种技术，让大型教师模型（如 Gemini 3.1）教会小型学生模型模仿其行为，以牺牲容量换取效率。函数调用使 AI 模型能调用外部工具或 API，这对实际智能体应用至关重要。边缘 AI 旨在消费者设备上本地运行推理，以保护隐私和降低延迟，但小模型常牺牲能力。Needle 的 Simple Attention Network 架构是 Transformer 的变体，在减少参数的同时保留用于工具使用的注意力机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://the-agent-report.com/2026/05/needle-gemini-tool-calling-distilled-26m-parameter-model/">Needle: Gemini Tool Calling Distilled Into a 26M Parameter Model ...</a></li>
<li><a href="https://deepwiki.com/cactus-compute/cactus">cactus -compute/ cactus | DeepWiki</a></li>
<li><a href="https://devengoratela.com/2025/05/amazon-bedrock-model-distillation-boost-function-calling-accuracy-while-reducing-cost-and-latency/">Amazon Bedrock Model Distillation : Boost function calling accuracy...</a></li>

</ul>
</details>

**标签**: `#AI`, `#model distillation`, `#function calling`, `#edge computing`, `#open source`

---

<a id="item-10"></a>
## [BrowserOS：挑战 AI 浏览器的开源代理浏览器](https://github.com/browseros-ai/BrowserOS) ⭐️ 8.0/10

BrowserOS 作为一个开源代理浏览器项目已发布，是 ChatGPT Atlas、Perplexity Comet 和 Dia 等商业 AI 浏览器的隐私优先替代品。它包括两个产品：面向人类的 BrowserOS 和面向 AI 代理的 BrowserClaw，两者均基于 Chromium 分支构建。 该项目将代理浏览能力民主化，允许开发者和用户在本地运行 AI 驱动的浏览器自动化，无需依赖专有云服务。它通过为代理工作流提供免费、可修改的基础，可能加速 AI 工具领域的创新。 BrowserOS 和 BrowserClaw 均采用 AGPL-3.0 许可证，确保其免费和开源。BrowserClaw 通过模型上下文协议（MCP）连接 AI 代理，使 Claude Code 等工具能够利用用户现有的登录会话控制浏览器。

rss · GitHub Trending - TypeScript Daily · 7月15日 01:42

**背景**: AI 浏览器集成人工智能，用于总结内容、回答问题并代表用户执行操作。一个专门的子集——代理浏览器，能够自主导航网页和填写表单；知名例子包括 ChatGPT Atlas（仅 macOS）、Perplexity Comet 和 Dia，它们均在 2025 年出现。BrowserOS 将自己定位为完全在用户机器上运行的开源、隐私优先替代品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_browser">Agentic browser</a></li>
<li><a href="https://en.wikipedia.org/wiki/ChatGPT_Atlas">ChatGPT Atlas</a></li>

</ul>
</details>

**标签**: `#AI`, `#browser`, `#open-source`, `#agentic`, `#TypeScript`

---

<a id="item-11"></a>
## [OpenAI 发布 Codex CLI 本地终端代理](https://github.com/openai/codex) ⭐️ 8.0/10

OpenAI 发布了 Codex CLI，这是一个轻量级编码代理，可在本地终端中运行，使开发者能够直接从命令行获得 AI 辅助编码。 此次发布将强大的 AI 编码能力带到本地环境，减少了对云端界面的依赖，提供了更高的隐私性和灵活性。它还能与 VS Code、Cursor、Windsurf 等流行 IDE 集成，扩大了开发者的适用范围。 Codex CLI 可通过 curl、npm 或 Homebrew 在 Mac、Linux 和 Windows 上安装。用户可使用 ChatGPT 计划（Plus、Pro、Business、Edu、Enterprise）登录，或通过额外设置使用 API 密钥。该仓库采用 Apache-2.0 许可证。

rss · GitHub Trending - Rust Daily · 7月15日 01:41

**背景**: 编码代理是一种 AI 驱动的工具，可以帮助编写、调试和提出代码更改建议。Codex CLI 是 OpenAI Codex 系列的一部分，该系列包括基于云的 Web 代理（Codex Web）和 IDE 插件。通过本地运行，它比纯云解决方案提供更好的性能和数据隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in ...</a></li>

</ul>
</details>

**标签**: `#openai`, `#codex`, `#ai coding agent`, `#cli`, `#developer tools`

---

<a id="item-12"></a>
## [uv：用 Rust 构建的快速 Python 包管理器](https://github.com/astral-sh/uv) ⭐️ 8.0/10

Astral 发布了 uv，这是一个用 Rust 构建的极速 Python 包和项目管理器。它声称在安装依赖时比 pip 快 10 到 100 倍。 uv 将多个 Python 工具（如 pip、pip-tools、pipx、poetry、pyenv 等）整合为一个高性能的替代品。这可以显著提高开发者的生产力，并通过全局缓存减少磁盘使用。 它提供了兼容 pip 的接口、自动处理虚拟环境以及通用锁文件。uv 支持 macOS、Linux 和 Windows，并且可以通过 curl 或 pip 安装，无需预先安装 Rust 或 Python。

rss · GitHub Trending - Rust Daily · 7月15日 01:41

**背景**: Python 的默认包管理器 pip 在处理大型项目时可能较慢，开发者通常还需要依赖 virtualenv、pipx、poetry 等额外工具。uv 由 Rust 编写，并得到 Astral（Ruff 的创建者）的支持，旨在将 Python 包管理统一并加速一个数量级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.astral.sh/uv/">uv is an extremely fast Python package and project manager , written...</a></li>
<li><a href="https://github.com/astral-sh/uv">astral-sh/ uv : An extremely fast Python package and project manager ...</a></li>

</ul>
</details>

**标签**: `#Python`, `#Rust`, `#package manager`, `#tooling`, `#performance`

---

<a id="item-13"></a>
## [NVIDIA Dynamo：开源分布式推理框架](https://github.com/ai-dynamo/dynamo) ⭐️ 8.0/10

NVIDIA 于 2025 年 3 月开源了 Dynamo，这是一个数据中心规模的分布式推理服务框架。它作为编排层，协调多个推理引擎（如 vLLM、TensorRT-LLM 和 SGLang）在多节点间运行。 Dynamo 在 NVIDIA Blackwell 上可将 DeepSeek-R1 等推理模型的吞吐量提升高达 30 倍，满足了 AI 数据中心日益增长的推理需求。它通过分离式服务和智能路由实现高效的多节点推理，使大规模 AI 部署更具成本效益。 主要特性包括分离式预填充和解码阶段、LLM 感知的请求路由、多层 KV 缓存以及自动 GPU 扩展。该框架使用 Rust 保证性能、Python 实现可扩展性，采用 Apache 2.0 许可证，并在 NGC 上提供预构建容器。

rss · GitHub Trending - Rust Daily · 7月15日 01:41

**背景**: 分布式推理服务是指跨多个 GPU 和节点运行大型 AI 模型以处理高请求量的过程。分离式服务将预填充（计算初始令牌）和解码（生成后续令牌）分开，以优化资源使用。Dynamo 作为推理引擎之上的编排层，将其转变为协调的多节点系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ai-dynamo/dynamo">GitHub - ai-dynamo/dynamo: A Datacenter Scale Distributed ...</a></li>
<li><a href="https://developer.nvidia.com/blog/introducing-nvidia-dynamo-a-low-latency-distributed-inference-framework-for-scaling-reasoning-ai-models/">NVIDIA Dynamo, A Low-Latency Distributed Inference Framework ...</a></li>

</ul>
</details>

**标签**: `#distributed inference`, `#AI infrastructure`, `#Rust`, `#serving framework`

---

<a id="item-14"></a>
## [vLLM 语义路由器：高效模型混合推理](https://github.com/vllm-project/semantic-router) ⭐️ 8.0/10

vLLM 项目发布了 vLLM 语义路由器，这是一个开源、信号驱动的路由器，能够在异构 LLM 和计算环境中实现智能的模型混合（MoM）路由。 该工具解决了在多样化硬件上高效编排多个专用 LLM 的关键挑战，有望降低成本和提高延迟，同时为不同工作负载实现个性化的模型路径。 vLLM 语义路由器利用用户偏好和工作负载特征等信号，将请求路由到最合适的模型或模型路径，支持在边缘、私有云和公有云上部署，并提供开源运行时。

rss · GitHub Trending - Go Daily · 7月15日 01:36

**背景**: 模型混合（MoM）是一种系统架构，在系统层编排多个独立模型，不同于在单个模型内部运作的混合专家（MoE）。异构 LLM 推理涉及将不同模型和硬件协同使用。vLLM 是一个高吞吐量的 LLM 推理引擎，在 AI 社区中被广泛采用。vLLM 语义路由器通过为多模型设置添加智能路由，扩展了 vLLM 的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/semantic-router">GitHub - vllm-project/semantic-router: Intelligent Mixture-of ...</a></li>
<li><a href="https://vllm-sr.ai/docs/intro/">vLLM Semantic Router</a></li>
<li><a href="https://vllm.ai/blog/mom-on-amd-gpu">Building Mixture - of - Models on AMD GPUs with vLLM-SR | vLLM Blog</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#Mixture-of-models`, `#Routing`, `#vLLM`, `#AI infrastructure`

---

<a id="item-15"></a>
## [腾讯开源 WeKnora：LLM 知识平台](https://github.com/Tencent/WeKnora) ⭐️ 8.0/10

腾讯开源了 WeKnora（v0.6.3），一个基于 LLM 的知识框架，能将原始文档转换为可查询的 RAG 系统、自主推理代理和自维护 Wiki。 此版本为企业提供了一个全面的、可自托管的知識管理解决方案，结合了 RAG、代理推理和自动 Wiki 生成，可能减少对专有服务的依赖。 WeKnora 支持多源数据接入（飞书、Notion、语雀、RSS）、20 多种 LLM 提供商、多工作空间 RBAC、Langfuse 可观测性以及 Chrome 扩展，模块化架构便于自托管。

rss · GitHub Trending - Go Daily · 7月15日 01:36

**背景**: 检索增强生成（RAG）是一种让 LLM 在生成回答前从外部源检索相关文档的技术，能提高准确性并减少幻觉。自维护 Wiki 利用 AI 代理从原始文档中持续组织并更新知识库。WeKnora 将这些概念整合到一个开源平台中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent/WeKnora">GitHub - Tencent/WeKnora: Open-source LLM knowledge platform ...</a></li>
<li><a href="https://deepwiki.com/Tencent/WeKnora">Tencent/WeKnora - DeepWiki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#RAG`, `#knowledge management`, `#open-source`, `#LLM`, `#Tencent`

---

<a id="item-16"></a>
## [KServe：Kubernetes 上的标准化 AI 推理平台](https://github.com/kserve/kserve) ⭐️ 8.0/10

KServe 是一个开源、CNCF 孵化项目，提供标准化的分布式平台，用于在 Kubernetes 上部署生成式和预测性 AI 模型，支持 vLLM、TensorFlow 和 PyTorch 等多种框架。 这很重要，因为 KServe 在单一的 Kubernetes 原生平台上统一了生成式和预测性 AI 推理，简化了 MLOps 工作流，并通过自动缩放、GPU 加速和模型可解释性等功能支持企业级部署。 KServe 既支持生成式 AI 后端（如 vLLM、llm-d）及兼容 OpenAI 的协议，也支持预测性 AI 框架（如 TensorFlow、PyTorch、ONNX）。它包括 KV 缓存卸载、智能路由、金丝雀发布和推理流水线等高级特性。

rss · GitHub Trending - Go Daily · 7月15日 01:36

**背景**: Kubernetes 是一个广泛用于部署和扩展应用程序的容器编排平台。AI 模型推理需要专门的基础设施以实现高效服务，尤其是大型语言模型（LLM）。KServe 基于 Kubernetes 构建，提供标准化、多框架的推理平台，处理自动缩放、GPU 管理和模型版本控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/kserve/kserve">GitHub - kserve/kserve: Standardized Distributed Generative ...</a></li>
<li><a href="https://kserve.github.io/website/">KServe - GitHub Pages</a></li>
<li><a href="https://kserve.github.io/kserve/">KServe | kserve</a></li>

</ul>
</details>

**标签**: `#MLOps`, `#Kubernetes`, `#AI Inference`, `#Open Source`

---

<a id="item-17"></a>
## [优步接近收购 Delivery Hero，估值 125 亿欧元](https://www.ithome.com/0/977/276.htm) ⭐️ 8.0/10

优步正就收购德国外卖公司 Delivery Hero 进行深入谈判，对后者估值约 125 亿欧元（每股约 41 欧元）。这笔交易最快可能于 2025 年 7 月 16 日宣布，将显著扩展 Uber Eats 的全球覆盖范围。 此次收购将使 Uber Eats 在欧洲、中东、亚洲和拉丁美洲的外卖配送领域占据主导地位，整合市场并加剧与 Just Eat Takeaway 等竞争对手的竞争。这也反映了外卖行业为追求盈利而进行的整合趋势。 优步已持有 Delivery Hero 24.99%的投票权，通过衍生品合约的总经济权益约为 36.8%。为应对反垄断审查，Delivery Hero 计划将其土耳其子公司 Yemeksepeti 及部分欧洲业务出售给一家美国投资公司。

rss · IT之家 · 7月15日 23:28

**背景**: 外卖配送已成为零工经济的重要组成部分，Uber Eats、DoorDash 和 Just Eat 等公司在全球范围内竞争。Delivery Hero 业务覆盖全球 60 多个市场，其中许多市场与 Uber Eats 重叠。此次收购将整合重叠业务，并可能减少在波兰、葡萄牙、西班牙和瑞典等市场的竞争。

**标签**: `#business`, `#acquisition`, `#food delivery`, `#Uber`, `#Delivery Hero`

---

<a id="item-18"></a>
## [国内首款 CT 引导加速器进入创新医疗器械审查程序](https://www.ithome.com/0/977/235.htm) ⭐️ 8.0/10

中核集团宣布，其自主研发的‘秒级转速同轴共面诊断 CT 引导医用电子直线加速器’已进入国家药监局创新医疗器械特别审查程序。这是国内首款达到该里程碑的设备。 这一突破展示了中国在高端放疗设备方面的能力，有望提高治疗精度和可及性。创新设计将 CT 成像与直线加速器集成在同一机架上，实现治疗过程中的实时肿瘤追踪。 该设备具有‘秒级转速’实现高速 CT 扫描以及同轴共面集成设计，可在治疗体位获取诊断级 CT 图像。中核集团子公司中核粒子同时推进医用直线加速器、SPECT/CT 一体机和硼中子俘获治疗三条产品线。

rss · IT之家 · 7月15日 14:07

**背景**: 医用电子直线加速器用于放射治疗，通过产生高能 X 射线或电子束照射肿瘤。CT 引导通过在治疗前或治疗中即时成像来提高靶向精度。国家药监局的创新医疗器械特别审查程序旨在加快具有高临床价值的新型医疗器械的审评。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/977/235.htm">国内首款“秒级转速同轴共面诊断 CT 引导医用电子直线加速器”成功进入...</a></li>
<li><a href="https://www.msn.cn/zh-cn/科学/通用/中核集团自主研制-国内首款秒级转速同轴共面ct引导加速器入审评程序/ar-AA27ZUw7">中核集团自主研制! 国内首款秒级转速同轴共面CT引导加速器入审评程序</a></li>
<li><a href="https://www.163.com/dy/article/L1TF6OFP0534A4SC.html">中核集团：同轴共面诊断CT引导医用电子直线加速器进入创新医疗器械特...</a></li>

</ul>
</details>

**标签**: `#medical device`, `#radiation therapy`, `#CT guidance`, `#innovation`

---

<a id="item-19"></a>
## [华为引望助力联合国首个全球自动驾驶法规制定](https://www.ithome.com/0/977/215.htm) ⭐️ 8.0/10

联合国于 2026 年 6 月正式通过了全球首个自动驾驶系统技术法规（ADS GTR）。华为旗下引望公司作为中国专家组核心成员，贡献的多项关键技术提案被采纳。 ADS GTR 是首个针对 L3/L4 自动驾驶的统一全球标准，有助于减少法规碎片化并推动国际部署。华为的深度参与凸显了中国在全球汽车技术标准制定中日益增长的影响力。 该法规涵盖了 L3/L4 系统的安全要求、制造商安全保障体系（SMS）、产品安全档案以及多支柱测试验证。引望利用了超过 190 万辆搭载华为 ADS 的量产车辆的真实道路数据，累计辅助驾驶里程达 128 亿公里。

rss · IT之家 · 7月15日 11:56

**背景**: 联合国世界车辆法规协调论坛（WP.29）负责协调全球车辆安全标准。ADS GTR 由中国、欧盟、英国、美国、加拿大和日本共同牵头制定，旨在统一此前各区域差异巨大的自动驾驶法规，这些差异曾阻碍跨境部署并增加开发成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bydtoday.com/china-co-authors-un-global-autonomous-driving-regulation-ads-gtr/">China Co-Authors UN Global Autonomous Driving Regulation</a></li>
<li><a href="https://equalocean.com/news/2026062921976-china-co-leads-worlds-first-global-autonomous-driving-regulation-shifting">China Co-Leads World's First Global Autonomous - Driving ...</a></li>
<li><a href="https://unece.org/transport/vehicle-regulations/world-forum-harmonization-vehicle-regulations-wp29">World Forum for Harmonization of Vehicle Regulations (WP.29)</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#regulation`, `#UN`, `#Huawei`, `#global standards`

---

<a id="item-20"></a>
## [DeepSeek 传筹备 IPO，目标 2027 年上市](https://www.36kr.com/p/3896190110319751) ⭐️ 8.0/10

DeepSeek 已开始筹备 IPO，计划在国内上市，目标 2027 年正式挂牌；同时正在推进新一轮融资，融资前估值目标至少 710 亿美元（约 4800 亿元人民币），计划融资至少 100 亿元人民币。 这一进展凸显了中国 AI 行业的强劲势头和监管支持，上交所近期发布了针对性的指引，允许人工智能大模型企业在不要求盈利的情况下登陆科创板。 DeepSeek 的 IPO 时间表包括在 2026 年底前完成财务报告，并在 2026 年底或 2027 年初提交申请；新一轮融资距上一轮仅隔一个月，资金将用于建设数据中心和采购 AI 芯片，包括可能自研芯片。

rss · 36氪 - 24小时热榜 · 7月15日 01:36

**背景**: 科创板第五套上市标准最初为生物医药企业设计，允许未盈利但拥有关键技术的公司上市。2026 年 6 月，上交所发布《发行上市审核规则适用指引第 10 号》，专门为人工智能大模型企业量身定制了这套标准，要求企业至少有一个已上线并实现规模化应用的大模型产品，并在主流评测中排名领先。这一监管变化为 DeepSeek 等 AI 公司打开了通往公开资本市场的大门。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sse.com.cn/aboutus/mediacenter/hotandd/c/c_20260617_10822584.shtml">上交所发布人工智能大模型企业适用科创板第五套上市标准审核指引 | 上...</a></li>
<li><a href="https://baike.baidu.com/item/科创板第五套标准/68037386">科创板第五套标准 - 百度百科</a></li>
<li><a href="https://baike.baidu.com/item/上海证券交易所发行上市审核规则适用指引第10号——人工智能大模型企业适用科创板第五套上市标准/67989151">上海证券交易所发行上市审核规则适用指引第10号——人工智能大模型企业...</a></li>

</ul>
</details>

**标签**: `#AI`, `#IPO`, `#DeepSeek`, `#China`, `#funding`

---

<a id="item-21"></a>
## [哈达玛积方法解耦 CNN 神经元](https://www.reddit.com/r/MachineLearning/comments/1uwya70/mechanistic_interpretability_a_first_paper_on/) ⭐️ 8.0/10

一篇独立研究论文提出了一种新技术，利用神经元感受野与其权重的哈达玛积来解耦和分析 InceptionV1 中的单个 1x1 卷积神经元，揭示了多个单语义簇，例如汽车、猫、狗、字母和人脸。 这项工作解决了卷积神经网络（CNN）机械可解释性中的一个关键挑战，提供了一种理解单个神经元检测内容的新方法。它可能使视觉模型的分析更加透明，并启发其他架构的类似方法。 该方法通过聚类感受野与神经元权重的哈达玛积来识别神经元检测的所有模式，并发现像字母这样的低值簇中，其依赖神经元也针对相同概念激活，正负权重均匀分布以降低总和。分析以受 Distill 风格启发的可视化呈现。

reddit · r/MachineLearning · /u/narang_27 · 7月15日 06:59

**背景**: 机械可解释性是一个通过逆向工程神经网络来理解其内部算法的领域。哈达玛积是两个矩阵的逐元素乘法。单语义簇指的是每组特征都代表一个单一、独立的概念，与对多个不相关输入响应的多语义神经元相对。这项工作基于 Distill Circuits 系列，并将一种新方法应用于 CNN。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hadamard_product_(matrices)">Hadamard product (matrices) - Wikipedia</a></li>
<li><a href="https://transformer-circuits.pub/2023/monosemantic-features/index.html">Towards Monosemanticity: Decomposing Language Models With ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>

</ul>
</details>

**标签**: `#mechanistic interpretability`, `#deep learning`, `#convolutional neural networks`, `#neuron analysis`, `#InceptionV1`

---

<a id="item-22"></a>
## [法官质疑 Epic 与谷歌交易影响反垄断立场](https://t.me/zaihuapd/42588) ⭐️ 8.0/10

一位美国法官披露，Epic Games 与谷歌已达成新的商业合作，涉及联合产品开发、营销，且 Epic 将在 6 年内向谷歌支付约 8 亿美元，用于 Unreal Engine、《堡垒之夜》及 Android 相关业务。法官质疑该合作是否损害了 Epic 在反垄断案中推动 Android 生态改革的立场。 这一披露可能削弱 Epic 在反垄断案中的道德和法律地位，影响旨在开放 Android 生态的补救措施。它还引发了关于原告在诉讼期间与被告进行重大商业交易存在利益冲突的担忧。 该合作期限为 6 年，包括围绕 Unreal Engine、《堡垒之夜》和 Android 的联合产品开发、营销及合作关系。Epic CEO Tim Sweeney 表示，协议未包含在 Google Play 上分发 Epic Games Store 的条款，但法官对该交易对案件的影响表示怀疑。

telegram · zaihuapd · 7月15日 11:15

**背景**: Epic Games 于 2020 年起诉谷歌，指控其在 Android 应用分发和应用内支付方面存在垄断行为。2023 年 12 月，陪审团裁定谷歌违反反垄断法，案件目前处于补救措施阶段。这一新合作出现在该阶段，引发了对 Epic 的商业利益是否与其推动开放性的立场一致的质疑。Unreal Engine 是 Epic 广泛使用的 3D 游戏引擎，《堡垒之夜》是其旗舰游戏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/07/third-party-app-stores-coming-to-google-play-next-week-as-epic-settlement-withdrawn/">Third-party app stores coming to Google Play next week as ...</a></li>
<li><a href="https://news.bloomberglaw.com/antitrust/google-proposes-to-share-play-store-catalog-to-resolve-case">Google Revamps Android App Stores to Resolve Antitrust Claims</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unreal_Engine">Unreal Engine</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#Epic Games`, `#Google`, `#legal`, `#Android`

---

<a id="item-23"></a>
## [DeepSeek 首轮融资超 500 亿元](https://t.me/zaihuapd/42589) ⭐️ 8.0/10

DeepSeek 完成了首轮外部融资，筹得超过 500 亿元人民币（约 74 亿美元），估值超过 500 亿美元，并采用有限合伙架构维持创始人的控制权。 这一巨额融资轮表明投资者对 DeepSeek 信心十足，也凸显了中国 AI 初创企业日益增长的重要性；同时，这种特殊的控制架构为创始人主导的公司寻求大额投资而不稀释投票权树立了先例。 本轮投资者将资金投入由 CEO 梁文锋管理的有限合伙企业，而非直接投资 DeepSeek 本身，且需接受五年锁定期且不享有表决权；梁文锋本人投资了 200 亿元人民币。

telegram · zaihuapd · 7月15日 12:56

**背景**: 有限合伙（LP）结构将所有权与控制权分离：有限合伙人出资但无管理权，而普通合伙人（通常是创始人）保留完全控制权。这种安排允许初创公司在不放弃董事会席位或投票权的情况下筹集大额资金，常用于私募股权，但在早期 AI 公司中不太常见。DeepSeek 采用这一模式，反映了在获得大量外部投资的同时维持创始人自主权的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investopedia.com/terms/l/limitedpartnership.asp">investopedia.com/terms/l/ limitedpartnership .asp</a></li>

</ul>
</details>

**标签**: `#AI`, `#funding`, `#DeepSeek`, `#startup`, `#valuation`

---

<a id="item-24"></a>
## [Telegram 推出无服务器平台，机器人后端无需自建服务器](https://core.telegram.org/bots/serverless) ⭐️ 8.0/10

Telegram 正式推出无服务器平台，允许开发者使用 JavaScript 将机器人和 Mini App 的后端代码直接运行在 Telegram 的基础设施上，无需自行管理服务器。开发者只需执行一行命令 npx tgcloud push 即可完成部署。 这极大简化了机器人开发，消除了基础设施管理负担，降低了创建 Telegram 机器人的门槛。同时，后端与 Telegram API 紧密集成，有望提升延迟和可靠性。 代码运行在紧邻 Bot API 的隔离 V8 沙箱中，并内置基于 SQLite 的数据库。该平台目前仅支持 JavaScript 模块，通过 npx tgcloud push 命令部署。

telegram · zaihuapd · 7月15日 16:00

**背景**: V8 是谷歌的开源 JavaScript 引擎，用于 Chrome 和 Node.js。沙箱是一种安全机制，隔离运行中的代码，防止其访问敏感系统资源。Telegram 的无服务器平台利用 V8 沙箱来安全执行用户提供的 JavaScript 代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rivers.chaitin.cn/blog/cq953up0lnechd244nbg">Numen独家：利用wasm再次绕过最新Chrome v 8 sbx | 长亭百川云</a></li>
<li><a href="https://www.cnblogs.com/ninghg/p/21386559">Ant JS 运行时 9 MB 跑通 Hono 冷启动 5.5 ms:从二进制大小到 JIT...</a></li>

</ul>
</details>

**标签**: `#serverless`, `#Telegram`, `#bots`, `#JavaScript`, `#deployment`

---