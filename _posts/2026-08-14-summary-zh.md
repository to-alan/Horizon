---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 316 条内容中筛选出 24 条重要资讯。

---

**科技新闻**
1. [GLM-5.3 展示新兴网络安全能力](#item-tech-news-1) ⭐️ 8.0/10
2. [英伟达量产 200G/lane CPO 交换机](#item-tech-news-2) ⭐️ 8.0/10
3. [小红书开源 dots3-note 多模态 MoE 模型](#item-tech-news-3) ⭐️ 8.0/10
4. [PostgreSQL 修复 to\_char 高危堆缓冲区溢出漏洞](#item-tech-news-4) ⭐️ 8.0/10
5. [Qwen3.8-27B-FP8 引发本地推理关注](#item-tech-news-5) ⭐️ 7.0/10
6. [RustDesk 为 Wayland 带来真正的无人值守远程访问](#item-tech-news-6) ⭐️ 7.0/10
7. [Google 探索用同态加密实现私密 AI 推理](#item-tech-news-7) ⭐️ 7.0/10
8. [Firefox 成为最后支持完整 uBlock Origin 的主流浏览器](#item-tech-news-8) ⭐️ 7.0/10
9. [Anthropic 发布 Claude Agent Skills 公共仓库](#item-tech-news-9) ⭐️ 7.0/10
10. [Needle 2 面向微型设备运行工具调用](#item-tech-news-10) ⭐️ 7.0/10
11. [NVIDIA NeMo 开源 LLM 路由工具 Switchyard](#item-tech-news-11) ⭐️ 7.0/10
12. [Chrome DevTools MCP 为编码代理开放浏览器调试](#item-tech-news-12) ⭐️ 7.0/10
13. [Apify MCP Server 让 AI 代理调用数千种网页数据工具](#item-tech-news-13) ⭐️ 7.0/10
14. [DeepSeek 发布开源 Agent 框架 Harness](#item-tech-news-14) ⭐️ 7.0/10
15. [福特斥资 20 亿美元改造工厂生产 Fathom](#item-tech-news-15) ⭐️ 7.0/10
16. [法国否决 15 岁以下未成年人社媒禁令](#item-tech-news-16) ⭐️ 7.0/10
17. [Doom 渲染器被编译为 210 亿参数 Transformer](#item-tech-news-17) ⭐️ 7.0/10
18. [Vivodyne 用 AI 与机器人规模化测试人体组织](#item-tech-news-18) ⭐️ 7.0/10
19. [法院限谷歌一周内简化第三方应用商店安装](#item-tech-news-19) ⭐️ 7.0/10
20. [苹果据报为中国市场训练专属大模型](#item-tech-news-20) ⭐️ 7.0/10

**科技博客**
1. [vLLM 的 DSpark 自适应验证](#item-tech-blog-1) ⭐️ 8.0/10

**财经新闻**
1. [伯克希尔增持 Alphabet](#item-finance-news-1) ⭐️ 7.0/10
2. [美国加强审查预测市场](#item-finance-news-2) ⭐️ 7.0/10
3. [Uber 与小马智行拟在欧洲部署 2000 辆无人驾驶出租车](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [GLM-5.3 展示新兴网络安全能力](https://z.ai/blog/glm-5.3) ⭐️ 8.0/10

Z.AI 将 GLM-5.3 描述为前沿编程模型，并重点展示其在安全研究、漏洞发现和攻防代理测试方面的能力。该条目称，模型可能支持大规模漏洞扫描、漏洞利用适配以及攻击代理与防御代理之间的对抗，但未提供可供独立核验的原始正文、基准数据或完整实验方法。社区用户报告称，它在 Claude Code 工具框架中完成了 WordPress 插件零日漏洞、远程代码执行和 Linux 6.8 内核漏洞利用适配等任务；这些均属于个人陈述，不能单独证明模型能力或漏洞有效性。若相关表现得到复现，持续下降的自动化扫描成本可能扩大开源软件漏洞发现规模，同时也会提高对负责任披露、访问控制和滥用防范的要求。

hackernews · pella · 8月14日 05:19 · [社区讨论](https://news.ycombinator.com/item?id=49294997)

**「背景」** GLM 是 Z.ai 使用的大语言模型系列，其现有产品页面此前将 Z.ai 助手描述为由 GLM-5.2 驱动，可用于编程、网站构建和长周期任务。所谓“涌现式网络安全能力”，通常指模型未经逐项专门设计便表现出漏洞发现、利用代码调整或攻防代理协作等能力，但这些表现仍需通过可复现测试和独立验证来确认。

**「社区讨论」** 评论者普遍认为 GLM-5.3 的编码与安全研究表现接近领先模型，并提到 Z.AI 似乎正扫描开源及流行软件、通过其漏洞披露平台处理大量高危或严重问题。讨论同时保留明显疑虑，包括相关案例缺少独立验证、与其他模型的基准比较并不完整，以及价格、额度重置和本地量化部署仍会影响实际采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.3">GLM-5.3: Frontier Coding with Emergent Cyber Capabilities</a></li>

</ul>
</details>

**标签**: `#AI coding models`, `#cybersecurity`, `#vulnerability research`, `#AI agents`

---

<a id="item-tech-news-2"></a>
### [英伟达量产 200G/lane CPO 交换机](https://www.ithome.com/0/989/970.htm) ⭐️ 8.0/10

英伟达于 8 月 14 日宣布全面投产面向大规模 AI 训练与推理集群的 Spectrum-X Ethernet Photonics，并称其为全球首款量产的 200G/lane 共封装光学（CPO）以太网交换机系统。该系统将硅光子引擎与交换 ASIC 封装在多芯片模块中，并以外置激光源统一供光；英伟达宣称，与传统可插拔光模块方案相比，其激光器数量降至四分之一、功耗降至五分之一，AI 应用无中断运行时间延长 5 倍，平均事件间隔时间提高 10 倍。产品包括 2U 液冷 SN6810，提供 128 个 800Gb/s 端口和 102.4Tb/s 交换能力，以及 5U SN6800，采用 4 颗 ASIC，提供 409.6Tb/s 交换能力，可支持 512 个 800Gb/s 端口或超过 2000 个 200Gb/s 端口。供应链由台积电提供硅光子技术、SPIL 负责芯片级封装与测试、Lumentum 和 TFC 供应激光器组件、富士康开发整机，英伟达负责出货前最终测试；不过上述量产领先地位及功耗、可靠性数据主要来自厂商公告，报道未提供独立验证、实际部署规模或第三方实测结果。

rss · IT之家 · 8月14日 22:53

**「技术背景」** 共封装光学（CPO）把光学引擎与交换 ASIC 集成在同一封装或紧邻位置，相比前面板可插拔光模块可缩短高速电信号路径，主要用于降低高带宽互连的功耗和信号损耗。200G/lane 表示每条物理通道可承载每秒 200 吉比特的数据，多条通道可组合为 800Gb/s 等端口；英伟达披露的架构包含 512 条支持 200G 的通道，并面向大规模 AI 集群网络。

**「实际影响」** 大规模 AI 集群运营方将可采用量产的 200G/lane CPO 交换机，以更低的网络功耗和更高的端口密度扩展 GPU 互连，但英伟达宣称的 5 倍能效和 10 倍可靠性提升仍缺少独立实测验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/scaling-power-efficient-ai-factories-with-nvidia-spectrum-x-ethernet-photonics/">Scaling Power-Efficient AI Factories with NVIDIA Spectrum-X Ethernet Photonics | NVIDIA Technical Blog</a></li>
<li><a href="https://www.nvidia.com/en-us/networking/products/silicon-photonics/">Silicon Photonics Networking for Agentic AI | NVIDIA</a></li>

</ul>
</details>

**标签**: `#共封装光学`, `#硅光子`, `#数据中心网络`, `#AI基础设施`, `#以太网交换机`

---

<a id="item-tech-news-3"></a>
### [小红书开源 dots3-note 多模态 MoE 模型](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 8.0/10

小红书 dots 实验室发布 dots3-note preview，这是 dots3 系列首个开放权重模型。该模型采用总参数量 280B、单次激活参数量 16B 的混合专家（MoE）架构，支持最长 512K 上下文，并可处理文本、图像、视频和音频输入。模型还引入 TEMPO 强化学习方法，通过自批判和测试时价值估计训练长程智能体，同时发布 VibeSearchBench 和 VibeLifeBench 两个面向真实场景的智能体基准，权重已在 Hugging Face 开源。现有信息尚未包含完整训练细节、评测结果或独立验证，因此其实际性能和技术影响仍有待进一步评估。

telegram · zaihuapd · 8月14日 08:27

**「背景」** 混合专家（MoE）模型通常只为每个输入调用部分专家参数，因此“总参数 280B、激活参数 16B”表示模型容量很大，但单次推理并不会使用全部权重；不过，部署时通常仍需存储完整模型。dots3-note preview 的官方代码库列出了 Transformers、SGLang、vLLM、Hugging Face 和 ModelScope 等相关入口，并确认其上下文长度最高为 512K tokens。

**「影响」** 开发者现在可以基于开放权重直接评估和集成这一 280B/16B MoE 模型，但其智能体能力能否用于生产仍取决于独立基准复现、实际部署支持以及长期运行轨迹等证据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/studio-dots-ai/dots3-note-prev">GitHub - studio-dots-ai/ dots 3 - note -prev: dots 3 note preview · GitHub</a></li>
<li><a href="https://www.remio.ai/post/rednote-opens-dots3-note-preview-but-its-agent-claims-still-need-proof">RedNote Opens dots 3 note Preview, but Its Agent Claims Still Need...</a></li>
<li><a href="https://github.com/studio-dots-ai/dots3-note-prev">GitHub - studio-dots-ai/ dots 3 - note -prev: dots 3 note preview · GitHub</a></li>

</ul>
</details>

**标签**: `#开放权重模型`, `#混合专家模型`, `#多模态 AI`, `#长上下文`, `#智能体基准`

---

<a id="item-tech-news-4"></a>
### [PostgreSQL 修复 to\_char 高危堆缓冲区溢出漏洞](https://www.postgresql.org/support/security/CVE-2026-14669/) ⭐️ 8.0/10

PostgreSQL 项目披露并修复了高危漏洞 CVE-2026-14669，该漏洞位于 \`to\_char\(timestamptz\)\` 处理超长 POSIX 时区缩写的过程，可能造成堆缓冲区溢出。能够设置时区的低权限数据库用户可能利用该漏洞，以 PostgreSQL 服务进程的操作系统权限执行任意代码；漏洞 CVSS 评分为 8.8，但不属于无需认证即可利用的漏洞。受影响版本包括 PostgreSQL 18.5、17.11、16.15、15.19 和 14.24 之前的版本，其中 18.5 因回归问题未正式发布，PostgreSQL 18 系列用户应升级至 18.6，其他系列应分别升级至 17.11、16.15、15.19 或 14.24。此次小版本升级无需转储数据库或运行 \`pg\_upgrade\`，更新程序文件并重启服务即可完成更新。

telegram · zaihuapd · 8月14日 14:35

**「背景」** PostgreSQL 的 to\_char\(timestamptz\) 用于按指定格式输出带时区的时间戳，而 POSIX 时区字符串可包含自定义时区缩写。堆缓冲区溢出意味着程序向堆内存中已分配缓冲区的边界之外写入数据，可能破坏进程内存并被利用来执行代码；在此漏洞中，代码将以运行数据库服务的操作系统用户身份执行。

**「运维影响」** 运行受影响 PostgreSQL 版本的组织应尽快升级并重启服务，尤其需要关注允许低权限用户设置时区的数据库环境，因为攻击成功后可能获得数据库服务进程的操作系统权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/support/security/CVE-2026-14669/">PostgreSQL : CVE-2026-14669: PostgreSQL to _ char heap buffer...</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#数据库安全`, `#远程代码执行`, `#缓冲区溢出`, `#漏洞修复`

---

<a id="item-tech-news-5"></a>
### [Qwen3.8-27B-FP8 引发本地推理关注](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) ⭐️ 7.0/10

Qwen3.8-27B-FP8 作为一款面向本地推理的 27B 参数 FP8 模型，因可在个人设备上运行而受到关注。早期用户反馈称，它在部分私有推理任务和图形生成任务中表现出较强能力，但可能消耗更多推理令牌、产生较高延迟，并存在显存效率方面的疑问。现有材料没有提供官方规格、发布日期、标准化基准或可复现的横向对比，因此尚不足以判断其相对其他本地模型的整体优势。用户还报告了思考文本风格、关闭思考模式以及聊天模板和工具调用兼容性方面的问题。

hackernews · erdaltoprak · 8月14日 15:00 · [社区讨论](https://news.ycombinator.com/item?id=49299605)

**「背景」** FP8 是一种以 8 位浮点数表示模型权重的量化方式，通常能在降低显存占用的同时，尽量保持接近 BF16 原始模型的性能；该模型采用块大小为 128 的细粒度 FP8 量化。模型文件可通过 Hugging Face Transformers、vLLM 和 SGLang 等推理框架运行，因此适合在本地硬件上部署，也可通过 Qwen Cloud 使用托管服务。

**「影响」** 本地 AI 用户可在约 17GB RAM/VRAM 的设备上运行 Qwen 3.8 27B，并获得视觉、推理和最高 256K 上下文能力。

**「社区讨论」** 一名用户称该模型通过了其私有基准，但令牌用量约为 Gemma 4 的 5 倍，并在启用 MTP 时耗时 12 分 30 秒；另一名用户认为它生成的骑车鹈鹕图形结构出色，但自行车缺少链条。讨论中也有人担忧显存效率、简略且省词的思考轨迹，以及 Ollama 中关闭思考模式和默认 Jinja 模板可能影响工具调用与 KV 缓存命中率的问题，但这些均属于尚未独立验证的个人观察。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B-FP8">Qwen/Qwen3.8-27B-FP8 · Hugging Face</a></li>
<li><a href="https://unsloth.ai/docs/models/qwen3.8">Qwen 3 . 8 - How to Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**标签**: `#large-language-models`, `#local-ai`, `#model-inference`, `#FP8`, `#Qwen`

---

<a id="item-tech-news-6"></a>
### [RustDesk 为 Wayland 带来真正的无人值守远程访问](https://rustdesk.com/blog/unattended-remote-access-wayland/) ⭐️ 7.0/10

RustDesk 宣布支持在 Wayland 环境下进行真正的无人值守远程访问，从而可以在没有本地用户确认或操作的情况下远程管理 Linux 系统。Wayland 长期以来给远程桌面软件的屏幕捕获、输入控制和后台连接带来限制，因此这项变化解决了 RustDesk 用户在 Linux 主机管理中的一个重要实际障碍。现有材料没有提供具体的实现方式、支持的发行版或版本要求，因此这些兼容性细节仍需以 RustDesk 的正式文档为准。

hackernews · rustdesk · 8月14日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=49300759)

**「背景」** RustDesk 是一款开源远程桌面软件，而 Wayland 是现代 Linux 桌面广泛采用的显示系统。由于 Wayland 对屏幕捕获和输入控制施加了更严格的安全限制，远程桌面通常需要远端用户逐次批准会话；所谓“无人值守访问”则允许在远端无人操作时建立连接。\[tool-1-1\]

**「实际影响」** RustDesk 用户现在可在无需本地用户交互的情况下，远程管理采用 Wayland 的 Linux 系统。

**「社区讨论」** 部分用户表示该功能及时解决了自己刚遇到的 Wayland 使用障碍，也有人询问 RustDesk 与 VNC、通过 SSH 和 Tailscale 使用 Remmina 等方案在性能、用途与信任模型上的差异。另有评论指出，RustDesk 自托管连接的加密支持仍存在问题，但这只是社区提出的未经核实的担忧，不能直接视为此次 Wayland 更新的结论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustdesk.com/blog/unattended-remote-access-wayland/">Unattended Remote Access on Wayland with RustDesk — RustDesk</a></li>

</ul>
</details>

**标签**: `#RustDesk`, `#Wayland`, `#remote desktop`, `#Linux`, `#open source`

---

<a id="item-tech-news-7"></a>
### [Google 探索用同态加密实现私密 AI 推理](https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/) ⭐️ 7.0/10

Google 提出利用同态加密实现私密 AI 推理，使系统能够直接处理加密数据，而无需先将其解密。该技术有望减少云端推理过程中用户数据暴露的风险，并影响隐私保护机器学习和 AI 基础设施的部署方式。不过，现有材料未提供具体实现细节、性能测试或资源消耗数据，因此尚不足以验证其已达到可大规模商用的“实用”程度。同态加密通常会引入显著计算开销，这仍是判断该方案现实可行性的关键限制。

hackernews · u1hcw9nx · 8月14日 15:43 · [社区讨论](https://news.ycombinator.com/item?id=49300314)

**「背景」** 同态加密允许服务器直接对密文执行计算，并让数据在处理过程中保持加密，因此可用于减少云端 AI 推理对明文输入的接触。Google 的 HEIR（Homomorphic Encryption Intermediate Representation）是一个开源编译器工具链和开发平台，可将原本处理未加密数据的预训练 AI 模型转换为处理加密输入的形式。

**「实际影响」** 如果 Google 的方案达到可部署的性能，云端服务可在不直接解密用户输入的情况下完成 AI 推理，从而为隐私敏感型应用提供新的部署选项。当前材料未给出具体性能或资源开销数据，因此尚无法判断它能否超越同态加密通常面临的高计算成本，立即形成商业可行性。

**「社区讨论」** 评论者认可私密云端 AI 的潜在价值，但有人援引相关研究经验，认为同态加密推理可能产生约 1000 倍量级的开销，并质疑其能源成本和商业可行性。另一些评论者主张本地推理更能保障隐私，同时以 Google 既有产品和服务的隐私做法为由，对其可信度持保留态度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/">How Google is Making Private AI Practical with Homomorphic ...</a></li>
<li><a href="https://blog.google/security/how-google-is-making-private-ai-practical-with-homomorphic-encryption/">How Google is Making Private AI Practical with Homomorphic ...</a></li>

</ul>
</details>

**标签**: `#Homomorphic Encryption`, `#Privacy-Preserving ML`, `#AI Inference`, `#Cloud Security`

---

<a id="item-tech-news-8"></a>
### [Firefox 成为最后支持完整 uBlock Origin 的主流浏览器](https://www.pcworld.com/article/3212428/firefox-is-now-the-last-major-browser-that-still-supports-ublock-origin.html) ⭐️ 7.0/10

据该条目称，在其他主流浏览器转向 Manifest V3 并收紧扩展 API 后，Firefox 已成为最后仍支持完整版 uBlock Origin 的主流浏览器。相关限制削弱了内容拦截扩展动态过滤网络请求的能力，使其难以维持 uBlock Origin 的完整功能。此事不仅影响广告拦截，也凸显浏览器平台规则对隐私工具、开源扩展及其维护者的直接制约。由于未提供原文内容，具体浏览器范围、兼容状态及功能差异无法从现有材料中进一步核实。

hackernews · DemiGuru · 8月14日 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49303202)

**「背景」** uBlock Origin 是一款开源内容拦截扩展，其完整功能依赖浏览器提供的扩展 API；Manifest V3 改变了扩展处理网络请求等能力，因而限制了传统拦截方式。面向 Chrome 的 uBlock Origin Lite 是为 Manifest V3 单独开发的版本，与完整的 uBlock Origin 相比存在明显功能限制。

**「实际影响」** Chrome 用户在 Manifest V3 迁移后只能使用功能受限的 uBO Lite，而 Firefox 用户仍可使用完整的 uBlock Origin；不过“Firefox 是唯一仍支持它的主流浏览器”这一说法并不严谨，因为现有资料也列出 Brave、Edge 和 Opera 的支持。

**「社区讨论」** 评论者普遍批评 Manifest V3 削弱用户控制权，并有人表示相关限制促使其停止维护广告过滤工具；另有评论指出，Chrome 仍可加载自行构建的未打包扩展，但操作成本很高。也有评论强调 Firefox 会审核 uBlock Origin 等推荐扩展的更新代码，不过该说法在现有材料中未获独立验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ublockorigin.com/">uBlock Origin - Free, open-source ad blocker extension</a></li>
<li><a href="https://winaero.com/google-ends-support-for-original-ublock-origin/">Google ends support for original uBlock Origin</a></li>
<li><a href="https://ublockorigin.com/">uBlock Origin - Free, open-source ad blocker extension</a></li>

</ul>
</details>

**标签**: `#Firefox`, `#uBlock Origin`, `#Browser Extensions`, `#Manifest V3`, `#Web Privacy`

---

<a id="item-tech-news-9"></a>
### [Anthropic 发布 Claude Agent Skills 公共仓库](https://github.com/anthropics/skills) ⭐️ 7.0/10

Anthropic 发布了 Agent Skills 公共仓库，展示 Claude 如何动态加载由指令、脚本和资源组成的文件夹，以可重复地完成文档处理、网页测试、MCP 服务器生成、品牌传播等专业任务。每项技能独立存放，并通过带 YAML frontmatter 的 SKILL.md 定义；必填字段只有使用小写连字符格式的唯一 name，以及说明功能和适用时机的 description。仓库提供技能示例、规范和模板，并可通过 Claude Code 插件市场安装；Claude.ai 付费套餐已提供这些示例技能，Claude API 也支持预构建技能和自定义技能。许多示例采用 Apache 2.0 许可证，但 docx、pdf、pptx 和 xlsx 文档技能仅为源码可用而非开源；Anthropic 同时强调所有技能主要用于演示和教育，实际行为可能不同，关键任务采用前应在自身环境中充分测试。

rss · GitHub Trending - Daily · 8月14日 03:22

**「背景」** Agent Skills 是一种用于扩展 AI 智能体能力的轻量开放格式，其基本单元是包含 \`SKILL.md\` 的目录，可封装专门知识、操作流程及相关资源。该规范采用渐进式披露机制：启动时只加载所有技能的名称和描述等元数据，智能体在任务需要时再读取更详细的指令和资源。

**「影响」** 代理开发者可按公开的 Agent Skills 格式封装可复用工作流，并在 Claude 及逐渐采用该标准的其他代理产品间共享，但文档处理技能仅为源码可用而非开源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/specification">The complete format specification for Agent Skills .</a></li>
<li><a href="https://agentskills.io/">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Claude`, `#agent skills`, `#open source`, `#developer tools`

---

<a id="item-tech-news-10"></a>
### [Needle 2 面向微型设备运行工具调用](https://github.com/cactus-compute/needle) ⭐️ 7.0/10

Cactus Compute 发布了 Needle 2，这是一款面向手机、可穿戴设备、智能家居和机器人的开放式 4500 万参数模型，主要用于工具调用、设备操作和结构化信息提取。其权重与推理引擎被压缩为单个 14MB 二进制文件，采用 CQ2-bit 量化，并通过 256-token 滑动窗口及固定工具 KV 缓存，将官方所称的完整会话内存维持在约 28MB。模型基于 Simple Attention Network，结合 Hadamard MLP、GQA 注意力、engram 键值记忆和多通道超连接；解码过程使用由工具模式编译而成的字节级语法，以约束 JSON 输出，同时提供置信度门控和每轮最多选择五个工具的检索机制。配套 Python 包可通过 pip 安装，支持离线推理、Pydantic 结构化提取、LoRA 微调、数据合成和单文件 .cact 导出，但其与 FunctionGemma 270M、LFM2.5 230M 和 Apple FM 的性能比较主要来自项目方宣传，现有材料不足以核验基准方法及结果。

rss · GitHub Trending - Daily · 8月14日 03:22

**「背景」** 工具调用模型并非直接完成外部操作，而是根据预先声明的函数及参数模式生成结构化调用，再由宿主程序执行；受约束解码可将输出限制为符合模式的 JSON。Needle 2 通过训练阶段纳入的 2 位量化压缩参数、激活和 KV 缓存，并支持用 LoRA 在冻结基础模型的前提下进行低成本适配，以满足端侧设备对存储和内存的严格限制。

**「影响」** 需要在内存和存储受限设备上离线执行工具调用的开发者，可以用该工具包部署并定制一个约 14MB 的模型，但实际任务准确率和置信度校准效果仍需独立测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/needle: 14MB foundation model for tiny devices; phones, wearables, smart home, and robots. · GitHub</a></li>
<li><a href="https://cactuscompute.com/needle">Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus</a></li>

</ul>
</details>

**标签**: `#on-device AI`, `#small language models`, `#model quantization`, `#tool calling`, `#open source`

---

<a id="item-tech-news-11"></a>
### [NVIDIA NeMo 开源 LLM 路由工具 Switchyard](https://github.com/NVIDIA-NeMo/Switchyard) ⭐️ 7.0/10

NVIDIA NeMo 的 Switchyard 是一个用 Rust 编写的开源代理和库，可在不同模型及供应商之间路由 LLM 请求，同时转换 OpenAI Chat、OpenAI Responses 与 Anthropic Messages 格式。它可将 Claude Code、Codex CLI 和 OpenClaw 等代理接入 vLLM、NVIDIA NIM、Ollama、OpenRouter 或其他 OpenAI 兼容端点，并提供随机分流、LLM 分类、阶段路由、升级路由和自定义算法。Switchyard 还通过 Prometheus 记录请求、错误、延迟、令牌用量和路由开销指标，既能作为独立代理运行，也能通过 switchyard-libsy 嵌入 Rust 应用。该项目目前仍处于 pre-alpha 阶段，API 和算法预计会在 v1.0 前显著变化，官方明确标注其为实验性软件且不适合生产环境；现有材料也未提供可靠性、采用规模或基准测试结果。

rss · GitHub Trending - Daily · 8月14日 03:22

**「背景」** OpenAI Chat Completions、OpenAI Responses 与 Anthropic Messages 是不同的模型调用接口格式，客户端通常需要分别适配；Switchyard 在客户端与模型后端之间进行协议转换，使既有代理和 API 客户端可以继续使用原生接口。模型路由则根据请求内容、对话信号或固定流量比例选择后端，常用于跨模型测试以及成本与性能优化。

**「影响」** LLM 应用开发者可在尽量保持现有客户端 API 不变的情况下试验多模型分流、A/B 测试及成本与性能优化，但当前仅适合评估和实验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvidia-nemo.github.io/Switchyard/">Switchyard</a></li>

</ul>
</details>

**标签**: `#LLM infrastructure`, `#API compatibility`, `#model routing`, `#Rust`, `#open source`

---

<a id="item-tech-news-12"></a>
### [Chrome DevTools MCP 为编码代理开放浏览器调试](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 7.0/10

ChromeDevTools 推出的 chrome-devtools-mcp 通过模型上下文协议（MCP），让 Antigravity、Claude、Cursor 和 Copilot 等编码代理控制并检查实时 Chrome 浏览器，同时提供可脱离 MCP 使用的独立 CLI。它结合 Chrome DevTools 记录性能追踪并提取优化建议，可分析网络请求、截图和带源码映射堆栈的控制台消息，还借助 Puppeteer 执行浏览器操作并自动等待结果。该工具要求 Node.js LTS、npm 以及当前稳定版或更新版本的 Chrome，官方仅保证支持 Google Chrome 和 Chrome for Testing；其他 Chromium 浏览器可能可用，但不受保证。服务器默认收集工具调用成功率、延迟和环境信息等使用统计，并检查 npm 更新；性能功能还可能向 Google CrUX API 发送追踪 URL，这些行为可分别通过 --no-usage-statistics、CHROME\_DEVTOOLS\_MCP\_NO\_UPDATE\_CHECKS 和 --no-performance-crux 禁用。MCP 客户端能够查看、调试和修改浏览器及 DevTools 中的数据，因此不应在受控浏览器实例中暴露不希望共享的敏感或个人信息。

rss · GitHub Trending - TypeScript Daily · 8月14日 03:39

**「背景」** 模型上下文协议（MCP）是一种让 AI 客户端以结构化方式调用外部工具和访问上下文的接口规范。chrome-devtools-mcp 将这一接口连接到实时 Chrome 实例，使 Claude、Cursor、Copilot 等编码代理能够使用浏览器检查、调试和自动化能力。

**「实际影响」** 编码代理可直接利用实时浏览器状态完成自动化、调试和性能分析，但团队需要明确隔离敏感会话，并按隐私政策配置遥测与 CrUX 数据访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">GitHub - ChromeDevTools / chrome - devtools - mcp : Chrome...</a></li>

</ul>
</details>

**标签**: `#Chrome DevTools`, `#coding agents`, `#Model Context Protocol`, `#browser automation`, `#developer tools`

---

<a id="item-tech-news-13"></a>
### [Apify MCP Server 让 AI 代理调用数千种网页数据工具](https://github.com/apify/apify-mcp-server) ⭐️ 7.0/10

Apify MCP Server 通过模型上下文协议（MCP）让 AI 代理调用 Apify Store 中的数千种现成 Actor，用于抓取社交媒体、搜索引擎、地图、电商平台及其他网站的数据。项目推荐使用托管端点 https://mcp.apify.com，支持 OAuth，也可通过 Bearer 令牌连接 Claude.ai、Claude Code、Cursor、Visual Studio Code 及其他兼容 MCP 的客户端。该托管服务采用 Streamable HTTP 传输，并提供本地 stdio 模式不具备的 Actor 结果输出模式推断功能；旧版 https://mcp.apify.com/sse 端点已移除，客户端需要删除配置中的/sse 后缀。服务器还支持通过 AGI 代币、直接 x402 或 Skyfire 进行代理付费，但具体可用方式取决于 Actor 和支付方案。

rss · GitHub Trending - TypeScript Daily · 8月14日 03:39

**「背景」** 模型上下文协议（MCP）是一种让 AI 助手以标准化方式连接外部工具与数据源的协议；在这里，MCP 服务器把 Apify Actor 暴露为可调用工具。Apify Actor 是运行在 Apify 平台上的网页抓取、数据提取或自动化程序，因此兼容的 AI 客户端可以借此执行 Facebook 帖子抓取等具体任务。

**「实际影响」** 仍使用旧版 \`/sse\` 端点的 MCP 客户端必须改用不带该后缀的 \`https://mcp.apify.com\` 和 Streamable HTTP；需要结构化 Actor 结果输出模式推断的用户也必须使用托管服务，因为本地 stdio 模式尚不支持该功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apify/apify-mcp-server">GitHub - apify / apify - mcp - server : The Apify MCP server enables...</a></li>

</ul>
</details>

**标签**: `#Model Context Protocol`, `#AI Agents`, `#Web Scraping`, `#Data Extraction`

---

<a id="item-tech-news-14"></a>
### [DeepSeek 发布开源 Agent 框架 Harness](https://sspai.com/post/113434) ⭐️ 7.0/10

8 月 13 日，深度求索发布采用 MIT 许可证的 DeepSeek Harness 开发者预览版及配套插件生态，并同步开源 DeepSeek-V4-Pro-0813。该框架基于 Cordis 插件系统，以“一切皆插件”为理念，将模型、工具、Skills、会话、沙箱、存储、运行循环、调度和 UI 均设计为可配置、替换和扩展的插件，无需修改核心代码。Harness 提供 Standard、Code、Minimal 和 Creator 四种运行模式，分别面向完整编程工具链、通过 TypeScript 编排多步工具调用、最小化环境验证，以及插件与 Agent 预设的构建调试；安装 Node.js 后可运行“npx @deepseek-ai/dsh web”启动本地 Web UI。配套的 DeepSeek-V4-Pro-0813 采用 MoE 架构，总参数量 1.6 万亿、每 token 激活约 490 亿参数，支持最高 100 万 token 上下文，API 最大输出长度为 38.4 万 token，并兼容 JSON Output、Tool Calls、Responses API 和 Anthropic API。Harness 目前仍是开发者预览版，现有材料未提供其代码成熟度、实测效果或插件生态采用情况。

rss · 少数派 · 8月14日 00:52

**「背景」** DeepSeek 将 Agent 概括为“Model + Harness”：模型负责推理与决策，Harness 则提供环境感知、工具调用和持续执行机制，使模型能在任务过程中反复行动与修正。插件化设计旨在把这些运行能力从框架核心中解耦，方便开发者按场景组合组件或开发新的 Agent 预设。

**「影响」** Agent 开发者可在 MIT 许可证下组合或替换完整运行栈，并将 DeepSeek-V4-Pro-0813 下载到本地部署，但生产使用仍需评估预览版框架的稳定性与生态成熟度。

**标签**: `#AI Agent`, `#DeepSeek`, `#开源框架`, `#插件架构`, `#开发者工具`

---

<a id="item-tech-news-15"></a>
### [福特斥资 20 亿美元改造工厂生产 Fathom](https://www.ithome.com/0/989/967.htm) ⭐️ 7.0/10

福特投入 20 亿美元改造肯塔基州路易斯维尔装配厂，计划于 2027 年第一季度试制纯电中型皮卡 Fathom，并在同年晚些时候启动面向消费者的生产。Fathom 预计售价低于 3 万美元，将成为福特首款采用全新通用平台的电动车型。新“通用生产系统”以三条支线分别组装前部、后部以及集成座椅和内饰的结构电池组，并通过大型一体式铝铸件减少零部件，最终合并三个总成。工厂还把 Wi-Fi 接入点增至 1080 个，以支持软件质量检测；福特预计新体系可使装配速度较该厂此前车型提高 15%，但这些成本、效率和商业目标仍有待量产验证。

rss · IT之家 · 8月14日 15:55

**「技术背景」** 传统移动装配线让车辆沿单一路径依次完成各工序，是福特沿用一个多世纪的大规模汽车生产模式。大型一体式铸件可用单个铝制总成替代多个零件，结构电池组则同时承担储能和车身承载功能，两者都有助于减少零件及装配步骤。

**「实际影响」** 若项目按计划落地，路易斯维尔工厂将于 2027 年以三分支装配体系生产售价低于 3 万美元的纯电皮卡，并有望将装配速度提高 15%；但该车型尚未量产，成本、产能和盈利目标仍待验证。

**标签**: `#电动汽车`, `#汽车制造`, `#工业自动化`, `#结构电池`, `#福特`

---

<a id="item-tech-news-16"></a>
### [法国否决 15 岁以下未成年人社媒禁令](https://www.ithome.com/0/989/940.htm) ⭐️ 7.0/10

法国宪法委员会当地时间 8 月 14 日否决了禁止 15 岁以下未成年人使用社交媒体的法案，认定其对表达和通信自由构成“不成比例的侵犯”。委员会指出，禁令可能覆盖尚未证实会危害未成年人健康和安全的网络服务，且未考虑未成年人的年龄、家庭状况和成熟程度，也未设置家长基于儿童利益调整限制的机制。该法案还可能迫使包括成年人在内的所有用户证明年龄，但没有为年龄验证的方式和范围提供充分法律保障，因而存在侵犯隐私权的风险。法国议会此前于 7 月 21 日通过该法案，原计划从 9 月起实施，这也是总统马克龙推动的未成年人网络保护措施之一。

rss · IT之家 · 8月14日 13:57

**「政策背景」** 法国议会于 7 月 21 日最终通过这项法案，原计划从同年 9 月起禁止 15 岁以下未成年人使用社交媒体，该措施由法国总统马克龙推动。此类禁令通常需要平台核验用户年龄，因此未成年人网络保护目标会与全体用户的隐私及表达、通信自由产生冲突。

**「影响」** 该裁决阻止了这项禁令按原计划实施，社交媒体平台也无需依据该法案部署面向所有用户的年龄证明机制。

**标签**: `#平台监管`, `#年龄验证`, `#隐私保护`, `#未成年人网络安全`, `#数字权利`

---

<a id="item-tech-news-17"></a>
### [Doom 渲染器被编译为 210 亿参数 Transformer](https://www.reddit.com/r/MachineLearning/comments/1voazhm/i_compiled_dooms_renderer_into_a_21bparameter/) ⭐️ 7.0/10

作者没有进行任何训练，而是用自制编译器把 Doom 的渲染计算图直接转换为一个 210 亿参数 Transformer 的权重。生成结果是无需 trust\_remote\_code 即可由 Hugging Face Transformers 加载的标准检查点；模型接收表示场景数据的提示，并输出移动光标、绘制像素等命令组成的令牌序列，机械执行后即可得到 E1M1 画面。加载检查点、生成渲染结果并解析输出的宿主程序仅有 43 行 Python，但定义待编译计算图的 Python 代码要长得多。渲染一帧需要 3,614 个提示令牌和 53,747 个生成令牌，在 B200 上耗时略超 40 分钟，作者将其概括为每天约 35 帧，而原版 Doom 在 486 上可达到每秒 35 帧。

reddit · r/MachineLearning · /u/notforrob · 8月14日 15:50

**「背景」** 通常，Transformer 的权重通过训练从数据中学习，而这个项目将传统程序的计算过程直接编码进权重，把模型当作可编程计算载体。其输出不是最终图像，而是一系列可由外部宿主程序解释执行的像素绘制指令。

**「影响」** 该项目提供了一个可加载的检查点和具体宿主代码，展示常规计算图能够在无需训练或自定义加载逻辑的条件下被编译进 Transformer，但其极低的渲染速度使 Doom 实例主要具有概念验证价值。

**标签**: `#transformers`, `#compilers`, `#Doom`, `#Hugging Face`, `#computation graphs`

---

<a id="item-tech-news-18"></a>
### [Vivodyne 用 AI 与机器人规模化测试人体组织](https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete) ⭐️ 7.0/10

Vivodyne 在旧金山南部部署衣柜大小的机器人实验室，用于培养人体组织，并由 AI 设计受控实验，以预测新药的疗效与安全性。该公司目前拥有 12 个被称为“蜂巢”的实验室，宣称每年可测试超过 300 万个人体组织样本，容量约为美国全部临床试验总和的两倍。报道指出，约 90%的临床试验即使此前通过动物测试仍会失败，因此这类人体组织实验可能帮助药物研发降低对动物测试的依赖。不过，“淘汰动物测试”仍是推测性目标，现有材料未提供预测准确率、技术细节、同行评议或独立验证结果。

telegram · zaihuapd · 8月14日 01:48

**「背景」** 动物实验通常属于药物进入人体临床试验前的临床前研究，而培养的人体组织可用于观察更接近人类生物学的药物反应，但不能等同于完整的人体试验。Vivodyne 所称的“生物数据中心”将人体组织培养、机器人自动化与 AI 实验设计结合起来，以高通量生成药物反应数据；其“每年 300 多万”指组织实验容量，并非 300 多万次人体临床试验。

**「实际影响」** 如果 Vivodyne 的人体组织平台能够在独立研究中验证其预测能力，药企可能获得更贴近人体反应的大规模临床前筛选方式，并降低对动物测试的依赖；目前公开信息主要来自公司及其支持方，尚不足以证明它已经能够取代动物实验或显著降低临床失败率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fastcompany.com/91589344/the-worlds-largest-biological-datacenter-could-help-make-animal-testing-obsolete">The world&#x27;s largest &#x27;biological datacenter&#x27; could help... - Fast Company ...</a></li>
<li><a href="https://www.helena.org/projects/vivodyne/">Vivodyne | Helena</a></li>
<li><a href="https://hlth.com/insights/news/vivodyne-raises-40m-to-transform-drug-development-with-ai-powered-human-tissue-testing-2025-06-03">Vivodyne Raises $40M to Transform Drug Development with...</a></li>
<li><a href="https://www.businesswire.com/news/home/20250528498236/en/Vivodyne-to-Replace-Animal-Testing-With-$40-Million-Funding-to-Reverse-95-Clinical-Trial-Failure-Rate">Vivodyne to Replace Animal Testing With $40 Million Funding to...</a></li>

</ul>
</details>

**标签**: `#人工智能`, `#生物技术`, `#药物研发`, `#自动化实验室`

---

<a id="item-tech-news-19"></a>
### [法院限谷歌一周内简化第三方应用商店安装](https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/) ⭐️ 7.0/10

美国地区法官 James Donato 在 Epic 诉谷歌反垄断案的后续命令中，要求谷歌简化 Android 竞品应用商店的安装流程。谷歌须在一周内删除多余步骤和警告弹窗，使安装第三方应用市场像安装普通 Android 应用一样直接。法院认为，先要求用户“查看”、之后才显示“安装”等多步操作属于蓄意设置的“反竞争摩擦”，可能吓退普通用户。该命令建立在此前陪审团认定谷歌在 Android 应用分发领域构成非法垄断的裁决之上，但现有转述未提供裁决文本、具体改动范围或谷歌回应。

telegram · zaihuapd · 8月14日 09:55

**「背景」** Epic Games 诉谷歌案聚焦 Android 应用分发与应用内支付市场的竞争问题，陪审团此前认定谷歌在相关市场实施了非法垄断。法院原有禁令已要求谷歌在结构上向竞争性应用商店开放，此次后续命令则针对仍然存在的搜索提示、额外确认页面和安装警告等具体操作障碍。

**「直接影响」** Android 用户安装第三方应用商店时将减少额外警告和操作步骤，而竞争性应用商店也将更容易触达普通用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://budgyapp.com/judge-donato-google-rival-app-store-friction-order/">Google Ordered to Ease Rival App Store Installs in One Week</a></li>
<li><a href="https://www.mobilemarketingreads.com/judge-orders-google-to-remove-barriers-to-rival-app-store-installs-on-google-play/">Judge orders Google to remove barriers to rival app store installs on...</a></li>
<li><a href="https://www.androidauthority.com/google-play-store-remove-third-party-app-store-friction-3698697/">Google ordered to remove Android app store warning screens</a></li>

</ul>
</details>

**标签**: `#Android`, `#应用商店`, `#反垄断`, `#Google Play`, `#Epic Games`

---

<a id="item-tech-news-20"></a>
### [苹果据报为中国市场训练专属大模型](https://www.reuters.com/business/retail-consumer/apple-trains-its-own-ai-model-china-market-with-alibabas-support-sources-say-2026-08-14/) ⭐️ 7.0/10

据路透社援引知情人士消息，苹果已在阿里巴巴支持下为中国市场训练一款专属大语言模型，改变此前依赖第三方模型的策略。报道称，Apple Intelligence 预计将在未来数月通过 iOS 更新在中国上线，使苹果能够更直接地控制在华 AI 体验。消息人士还称，中国国家互联网信息办公室已于上月完成该生成式 AI 服务的备案；若最终获准落地，苹果可能成为首家获北京批准、在华提供自有 AI 模型的外国公司。不过，报道未披露模型能力、技术架构、兼容设备及确切上线时间，相关信息主要来自匿名消息源。

telegram · zaihuapd · 8月14日 14:47

**「背景」** Apple Intelligence 是苹果面向 iPhone 等设备推出的生成式 AI 功能，但自 2024 年 9 月 iPhone 16 发布以来，其在中国市场的推出一直以获得监管批准为前提。此前中国版 iPhone 尚未提供该功能，这一缺口被认为是影响苹果在华市场竞争力的因素之一。

**「影响」** 若报道所述模型获批并上线，中国大陆的 iPhone 用户将可通过后续 iOS 更新使用由苹果主导、阿里巴巴支持的本地化 Apple Intelligence；但具体上线时间、设备兼容范围和模型能力尚未公布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.investing.com/news/stock-market-news/apple-trains-own-ai-model-for-china-with-alibaba-support-reuters-reports-4859693">Apple trains own AI model for China with Alibaba support, Reuters ...</a></li>
<li><a href="https://favtutor.com/apple-china-ai-model-alibaba/">Apple Trained Its Own AI Model for China , 22 Months After Promising...</a></li>
<li><a href="https://www.techrepublic.com/article/news-apple-china-ai-model-alibaba-intelligence-apac/">Apple Intelligence in China : Alibaba Backs a Custom AI Model</a></li>

</ul>
</details>

**标签**: `#Apple Intelligence`, `#大语言模型`, `#阿里巴巴`, `#中国AI监管`, `#iOS`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [vLLM 的 DSpark 自适应验证](https://vllm.ai/blog/2026-08-14-dspark-adaptive-verification) ⭐️ 8.0/10

rss · vLLM Blog · 8月14日 00:00

**「背景」** 推测解码用额外计算换取更少的解码步数，但在高并发、GPU 计算饱和时，被拒绝的草稿 token 会直接拖累吞吐。作者指出，7-token 草稿块的末位存活率低于 10%，首位却超过 70%，且最佳草稿长度会随负载和接受率变化，固定配置无法兼顾不同并发。

**「方案」** DSpark 为每个草稿位置生成置信度，调度器将其累乘为存活概率，再从所有请求中全局选择概率最高的 B 个槽位，因此高置信请求的较深位置也可能优先于低置信请求的首位。B 通过最大化预期产出 token 与步骤耗时之比确定：收益包含采样请求的奖励 token 和所选槽位的累计存活概率，耗时则来自启动时对不同形状各运行五次并取中位数得到的查表模型。预算计算在 CPU 上利用滞后一拍的双缓冲置信度与 GPU 并行，而实际分配基于当前置信度在 GPU 上完成，并由 PyTorch 经 torch.compile 降为 Triton。为支持可变验证长度，方案还引入 varlen decode CUDA Graph，并把图填充造成的阶梯成本纳入预算决策。在 8×B300、DeepSeek-V4-Pro-0813、并发 1 至 256 的单一测试配置中，作者报告该方法始终位于吞吐与交互性的 Pareto 前沿：低并发近似长草稿，高并发自动收缩；但它目前依赖特定注意力后端，且不支持 eager 模式、LoRA、流水线并行和输出 logprobs。

**「启示」** 作者的核心结论是，推测解码不应使用静态长度，而应结合 token 存活概率与真实执行成本逐步分配验证预算。这样才能在负载变化时保留收益，并减少针对具体部署反复调参的需要。

**标签**: `#speculative decoding`, `#GPU inference`, `#adaptive scheduling`, `#CUDA graphs`, `#performance profiling`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [伯克希尔增持 Alphabet](https://www.cnbc.com/2026/08/14/berkshire-hathaway-boosts-alphabet-to-a-top-three-holding-ups-delta-and-housing-bets.html) ⭐️ 7.0/10

伯克希尔·哈撒韦第二季度将 Alphabet 持仓增加 83%，截至 6 月底持有约 1.06 亿股、价值 379 亿美元，使其成为公司第三大美国上市股票持仓。同期伯克希尔净买入近 200 亿美元股票，结束连续 14 个季度净卖出。

rss · CNBC Finance · 8月14日 21:06

**「背景」** 伯克希尔此前连续 14 个季度净卖出股票，并曾在新冠疫情初期卖出所持航空股。

**「影响」** 伯克希尔股东对科技、航空和住宅建筑行业的投资敞口随这些增持而扩大，相关行业的股价波动将更直接影响其股票组合价值。

**标签**: `#Berkshire Hathaway`, `#Alphabet`, `#institutional investing`, `#airlines`, `#homebuilders`

---

<a id="item-finance-news-2"></a>
### [美国加强审查预测市场](https://www.cnbc.com/2026/08/14/prediction-markets-scrutiny-mounts-from-regulators-and-banks.html) ⭐️ 7.0/10

知情人士称，美国商品期货交易委员会正内部审查押注特定词语是否出现的“提及合约”，但审查范围尚不明确；与此同时，华盛顿州法院下令叫停 Kalshi 的相关合约及体育、选举等市场，使该州成为继密歇根、内华达和马萨诸塞之后第四个限制 Kalshi 的州。

rss · CNBC Finance · 8月14日 19:21

**「背景」** “提及市场”让交易者押注某个词是否会出现在演讲、财报电话会或电视节目中，批评者认为掌握发言内容的人可能轻易操纵结果。

**「影响」** 华盛顿州的 Kalshi 用户将无法交易该平台的词语提及、体育、选举等多类事件合约，因为州法院已下令禁止这些市场在当地运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/08/13/business/kalshi-washington-state-ruling.html">Kalshi Ordered to Cease Most Operations in Washington State</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#CFTC regulation`, `#event contracts`, `#state gambling laws`, `#market manipulation`

---

<a id="item-finance-news-3"></a>
### [Uber 与小马智行拟在欧洲部署 2000 辆无人驾驶出租车](https://www.cnbc.com/2026/08/14/uber-partners-with-chinas-ponyai-for-2000-robotaxis-in-europe.html) ⭐️ 7.0/10

Uber 与小马智行宣布，计划在欧洲部署 2000 辆无人驾驶出租车，将服务从克罗地亚萨格勒布扩展至另外四座尚未公布的城市，并把合作拓展至中东；两家公司未披露具体时间表。

rss · CNBC Finance · 8月14日 01:02

**「背景」** 两家公司今年 3 月底已在萨格勒布推出商业服务，并称其为欧洲首个此类项目；作为行业参照，Waymo 目前在全球运营约 5000 辆车，主要位于美国。

**标签**: `#autonomous vehicles`, `#ride hailing`, `#European markets`, `#strategic partnerships`, `#transportation technology`

---