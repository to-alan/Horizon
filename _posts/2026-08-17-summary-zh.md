---
layout: default
title: "Horizon Summary: 2026-08-17 (ZH)"
date: 2026-08-17
lang: zh
---

> 从 273 条内容中筛选出 15 条重要资讯。

---

**科技新闻**
1. [xAI 开放 Grok-1 权重](#item-tech-news-1) ⭐️ 9.0/10
2. [DuckDB v2.0 预览](#item-tech-news-2) ⭐️ 8.0/10
3. [Copilot Autofix 与 Snowflake Jira 入侵](#item-tech-news-3) ⭐️ 8.0/10
4. [英伟达称 OpenAI 规划 12GW 算力](#item-tech-news-4) ⭐️ 8.0/10
5. [英伟达据称支持 OpenAI 数据中心融资](#item-tech-news-5) ⭐️ 8.0/10
6. [Qwen3.8 27B 评分 52](#item-tech-news-6) ⭐️ 7.0/10
7. [亚马逊书籍追踪曝光](#item-tech-news-7) ⭐️ 7.0/10
8. [Needle 2](#item-tech-news-8) ⭐️ 7.0/10
9. [TimesFM 2.5 发布](#item-tech-news-9) ⭐️ 7.0/10
10. [Rayhunter 发布](#item-tech-news-10) ⭐️ 7.0/10
11. [vLLM Semantic Router 发布](#item-tech-news-11) ⭐️ 7.0/10
12. [GitHub 大规模宕机调查中](#item-tech-news-12) ⭐️ 7.0/10
13. [声波驱动微型船和飞行器](#item-tech-news-13) ⭐️ 7.0/10
14. [苹果调整广告授权规则](#item-tech-news-14) ⭐️ 7.0/10

**科技博客**
1. [分布式层级卸载](#item-tech-blog-1) ⭐️ 8.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [xAI 开放 Grok-1 权重](https://github.com/xai-org/grok-1) ⭐️ 9.0/10

xAI 在 GitHub 仓库 xai-org/grok-1 发布了 Grok-1 开放权重模型的支持代码，仓库提供用于加载和运行模型的 JAX 示例实现。用户需要先下载 checkpoint，将 ckpt-0 目录放入 checkpoints，然后安装 requirements.txt 并运行 python run.py，脚本会加载 checkpoint 并对测试输入进行采样。Grok-1 标称为 314B 参数的 Mixture of 8 Experts（MoE）模型，每个 token 使用 2 个专家，包含 64 层、查询 48 个注意力头、键和值 8 个注意力头、6,144 维嵌入、SentencePiece 131,072 token 词表，最大上下文长度为 8,192 token。仓库说明该示例需要足够 GPU 内存，且 MoE 层实现并不高效，其设计目标是避免自定义 kernel 以验证模型正确性；代码和 Grok-1 权重以 Apache 2.0 许可发布。

rss · GitHub Trending - Python Daily · 8月17日 05:54

**「背景」** 开放权重模型通常允许用户下载模型参数并在自己的基础设施上运行或改造，但实际可用性仍受硬件、推理框架和许可条款限制。MoE 模型通过多个专家子网络分担计算，推理时通常只激活部分专家，因此参数规模和每个 token 的实际计算量不是同一概念。

**「影响」** 具备大规模 GPU 资源的研究者和工程团队现在可以直接检查、加载并实验 Grok-1 权重，但普通开发者很可能受限于 314B 参数规模和示例实现效率。

**标签**: `#artificial-intelligence`, `#machine-learning`, `#large-language-models`, `#open-source`, `#model-release`

---

<a id="item-tech-news-2"></a>
### [DuckDB v2.0 预览](https://duckdb.org/2026/08/17/duckdb-20-highlights) ⭐️ 8.0/10

这篇条目预告了 DuckDB v2.0，引发了对其在嵌入式分析、本地分析处理和数据管道中的角色的讨论。由于未提供正文，具体发布内容和改动细节无法从来源确认，但社区评论显示，用户关注的重点包括把 DuckDB 作为运行时工件来管理、空间分析、dbt 集成以及超出内存的数据处理能力。也有人借机提出了对缺少增量物化视图的长期期待，以及对近半年约 10,000 次提交背后是否大量使用 AI 辅助开发的疑问。整体上，这个预览被视为 DuckDB 继续扩展到更大规模、更广场景使用的信号。

hackernews · ibotty · 8月17日 13:46 · [社区讨论](https://news.ycombinator.com/item?id=49330781)

**「背景」** DuckDB 是一个面向分析查询的数据库项目，这次文章预告的是 v2.0，代号 Cyanoptera。按预告内容，2.0 的意义在于它不是单纯修补，而是把服务器模式、触发器、VARIANT 类型、异步 I/O、新 SQL 解析器和新存储格式一起纳入了这一版的讨论范围。

**「社区讨论」** 评论区整体非常积极，许多使用者表示 DuckDB 已经在多个项目和环境中降低了资源需求，并能在低配硬件上处理大于内存的数据。争议主要集中在功能优先级和开发节奏上，尤其是增量物化视图是否会成为下一步重点，以及快速提交增长是否意味着较多 AI 参与。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://prismix.dev/news/4f5a33c12fbb">A Preview of DuckDB v2.0 | Prismix</a></li>

</ul>
</details>

**标签**: `#duckdb`, `#databases`, `#analytics`, `#data-engineering`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [Copilot Autofix 与 Snowflake Jira 入侵](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug) ⭐️ 8.0/10

Wiz 发布的一篇分析称，GitHub Copilot Autofix 生成的代码在一个 GitHub Actions 工作流中引入了漏洞，最终帮助攻击者入侵了 Snowflake 的 Jira。这个案例的关键点不是 AI 本身“自动被攻破”，而是 AI 生成的变更进入了 CI/CD 流程后，没有被足够严格地审查和静态分析。它说明自动化修复工具如果直接修改工作流、脚本或模板，可能把原本的维护任务变成可被利用的注入面。对依赖 GitHub Actions 和类似流水线的团队来说，这类事件强调了人工审查、静态检测和最小权限配置仍然是必要控制。

hackernews · galnagli · 8月17日 14:18 · [社区讨论](https://news.ycombinator.com/item?id=49331423)

**「背景」** GitHub Actions 是 GitHub 的 CI/CD 自动化系统，工作流里如果把外部输入直接拼进 \`run:\` 命令，就可能出现脚本注入；这类问题在处理 issue 标题、分支名或其他不可信文本时尤其敏感。GitHub Copilot Autofix 则是 GitHub 的 AI 辅助修复功能，这篇 Wiz 报告讨论的是它参与了 Snowflake 相关工作流修复背景下的安全问题，而 Jira 是常见的缺陷和工单管理系统。

**「影响」** 对使用 AI 辅助改写 CI/CD 工作流的开发团队来说，这类变更不能视为低风险，必须像普通代码一样经过审查和安全扫描。

**「讨论」** 评论区的共识是，这类问题更像是人类把关不足，而不是 AI 生成代码天然安全或不安全；有人直接建议在 GitHub Actions 中加入静态分析工具。也有人质疑标题把 Copilot 与具体漏洞的关联说得过满，指出相关 PR 中被提到的 Copilot 贡献未必就是漏洞本身的直接来源。

**标签**: `#AI-assisted coding`, `#GitHub Actions`, `#supply chain security`, `#DevSecOps`, `#cloud security`

---

<a id="item-tech-news-4"></a>
### [英伟达称 OpenAI 规划 12GW 算力](https://www.ithome.com/0/990/834.htm) ⭐️ 8.0/10

IT 之家报道称，英伟达 CEO 黄仁勋在 8 月 17 日的官方博客中表示，OpenAI 已承诺在 2030 年前大规模部署约 12GW 的英伟达 AI 基础设施。黄仁勋同时提到，如果英伟达将 PORTS-Pike 合作从首期 4.25GW 继续扩大，总规模有望增至约 16GW。按这一规模估算，到 2030 年相关业务机会约为 6000 亿美元。黄仁勋还称，建设 AI 工厂需要芯片、封装、内存、网络以及土地、电力和建筑外壳等完整资源，并宣布英伟达与 SB Energy 在美国俄亥俄州朴次茅斯的 PORTS-Pike 科技园区锁定 LPS 容量，OpenAI 将作为承租方在当地建设并运营一座采用英伟达 DSX AI 工厂平台的“世界级 AI 工厂”。

rss · IT之家 · 8月17日 13:55

**「背景」** 这里的 GW 指的是算力基础设施的大规模功率与容量投入，通常对应数据中心、供电和服务器集群的整体部署规模。英伟达的 DSX AI 工厂平台则是围绕 GPU、CPU、网络和基础设施软件组织起来的整套 AI 基础设施方案。

**「影响」** 如果报道中的计划落实，OpenAI 将成为英伟达超大规模 AI 基础设施的长期大客户，并推动美国本土数据中心、电力和园区容量的锁定。

**标签**: `#AI infrastructure`, `#Nvidia`, `#OpenAI`, `#data centers`, `#semiconductors`

---

<a id="item-tech-news-5"></a>
### [英伟达据称支持 OpenAI 数据中心融资](https://www.36kr.com/p/3943003260583049) ⭐️ 8.0/10

据 The Information 报道，英伟达正洽谈向软银旗下 SB Energy 投资最多 30 亿美元，约合人民币 202 亿元，同时即将与 OpenAI 敲定约 1000 亿美元、约合人民币 6740 亿元的信贷担保协议，用于支持 OpenAI 租用美国俄亥俄州大型数据中心。SB Energy 是俄亥俄州 10GW 巨型数据中心园区的开发建设方，OpenAI 是主要承租方，英伟达则可能同时成为开发商投资者和承租方信用支持方。报道称，英伟达的担保规模已从此前《华尔街日报》提到的约 2500 亿美元下调，交易被拆分为两个阶段，其中 1000 亿美元用于第一阶段，且英伟达希望把自身信用支持限制在项目融资总额的 25%以内。英伟达还据称已同意向电力基础设施开发商 Lancium 投资 20 亿美元，后续最高可达 30 亿美元，Lancium 在得克萨斯州开发约 4GW 电力资源，其中 1.2GW 用于 OpenAI 的“星际之门”园区。

rss · 36氪 - 24小时热榜 · 8月17日 03:30

**「背景」** 大型 AI 模型训练和推理需要大量 GPU、数据中心容量和稳定电力，吉瓦级园区的瓶颈已从芯片供给扩展到土地、电网接入、能源和项目融资。OpenAI、软银和 SB Energy 今年 1 月已宣布合作并合计向 SB Energy 投资 10 亿美元，以推进“星际之门”项目下的数据中心建设。

**「影响」** 如果这些交易按报道落地，英伟达将通过资本投入和信用担保更深介入 OpenAI 相关 AI 基础设施建设，并可能提前锁定长期 GPU 需求。

**标签**: `#AI infrastructure`, `#Nvidia`, `#OpenAI`, `#data centers`, `#financing`

---

<a id="item-tech-news-6"></a>
### [Qwen3.8 27B 评分 52](https://artificialanalysis.ai/models/qwen3-8-27b) ⭐️ 7.0/10

Hacker News 讨论称，Qwen3.8 27B 在 Artificial Analysis 上拿到 52 分，引发了它是否能以 27B 规模接近更大模型能力的讨论。这个条目本身没有提供方法细节或独立验证，只给出了分数和模型名称，因此更像是一次基准分数更新而不是完整技术发布说明。其意义在于，它把“中等参数规模”模型的上限再次推高，也让人重新关注小模型在推理、工具调用和日常使用中的实际可用性。

hackernews · anana\_ · 8月17日 17:25 · [社区讨论](https://news.ycombinator.com/item?id=49334544)

**「背景」** Artificial Analysis 的 Intelligence Index 是一个综合基准，用来衡量模型在推理、知识、数学和编码等任务上的表现。Qwen3.8 27B 是一个支持文本和图像输入、输出文本、上下文窗口为 256k tokens 的模型。它在该指数上获得 52 分，因此被视为明显高于同类模型的平均水平。

**「社区讨论」** 评论区普遍认为这次分数很夸张：有人拿它和 Qwen3.6 27B、DeepSeek V4 Flash 0731 以及 Opus 4.6 做对比，认为它在同级别和更大模型里都显得异常强。也有实际使用者表示它在高推理档位下表现出很强的“agentic”倾向，善于目标跟踪和工具调用，但仍打算继续做更全面的测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/qwen3-8-27b">Qwen3.8 27B - Intelligence, Performance &amp; Price Analysis</a></li>
<li><a href="https://dataconomy.com/ai-models/qwen3-8-27b/">Qwen3.8 27B - Dataconomy</a></li>

</ul>
</details>

**标签**: `#AI models`, `#benchmarks`, `#Qwen`, `#open source AI`, `#model efficiency`

---

<a id="item-tech-news-7"></a>
### [亚马逊书籍追踪曝光](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 7.0/10

404 Media 用一枚放进珍贵书籍中的 Apple AirTag 追踪了一批约 1,000 本的订单，最终发现货件被送到了亚马逊拉斯维加斯 LAS8 仓库内的 VGT3 区域。报道与随附材料称，这个团队会为提高扫描效率先切掉书脊，因此原书在处理过程中被销毁，随后扫描得到的数据被用于训练亚马逊的 Nova 模型。亚马逊发言人则表示，公司是通过正常商业渠道采购书籍，用于改进产品。此事之所以重要，是因为它把外界长期怀疑的“为 AI 训练批量购买并拆解纸书”的做法，变成了可追踪的具体实例，并再次引发对训练数据来源和纸本原件损毁的争议。

rss · Simon Willison · 8月17日 15:21

**「背景」** 大型语言模型训练需要海量文本数据，纸质书对 AI 公司有吸引力，因为其中不少内容未完整出现在公开互联网语料中。此前 Anthropic 也因购书、切书脊并扫描用于训练而卷入作者诉讼，2025 年 6 月的相关裁决讨论了这种“破坏性扫描”在合理使用框架下的地位。

**「影响」** 这则报道使 Amazon 通过大批采购、切脊扫描并销毁稀有图书来训练 Nova 的说法更具可验证性，直接加剧了书商、作者和版权方对 AI 训练数据来源与原书灭失的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2025/Jun/24/anthropic-training/">Anthropic wins a major fair use victory for AI — but it’s still in trouble for stealing books</a></li>
<li><a href="https://dallasexpress.com/national/the-vanishing-page-ai-firms-scan-then-destroy-rare-book-editions/">The Vanishing Page: AI Firms Scan Then Destroy Rare Book Editions</a></li>
<li><a href="https://techcrunch.com/2026/08/17/amazon-once-an-online-bookseller-is-destroying-rare-books-to-train-ai-models/">Amazon, which started off selling books, is destroying rare ...</a></li>

</ul>
</details>

**标签**: `#ai-training`, `#data-sourcing`, `#amazon`, `#investigative-reporting`, `#copyright`

---

<a id="item-tech-news-8"></a>
### [Needle 2](https://github.com/cactus-compute/needle) ⭐️ 7.0/10

cactus-compute/needle 发布了 Needle 2，这是一个面向工具调用、设备端推理和结构化抽取的开源 45M 参数模型。项目称整个模型被压缩为单个 14MB 二进制文件，运行完整会话大约占用 28MB 内存，并采用 Cactus Quants 的 CQ2-bit 压缩和自研引擎封装。仓库本身提供 Python 包，支持推理、LoRA 微调和导出，安装后可直接描述工具并从 Python 调用，离线部署说明也已经给出。项目还声称它在部分小模型基准上能与 FunctionGemma 270M、LFM2.5 230M 和 Apple FM 互有胜负，同时体积小得多。

rss · GitHub Trending - Daily · 8月17日 05:40

**「背景」** 工具调用模型会根据输入选择外部函数或 API，并返回结构化结果，这类能力常用于助手、自动化和设备控制。端侧推理则强调在手机、穿戴设备、智能家居和机器人这类资源受限环境中本地运行模型，通常对体积、内存和离线能力要求很高。

**「影响」** 如果这些体积和内存数字在实际场景中成立，Needle 2 会让受限硬件上的本地工具调用和结构化抽取更容易落地。

**标签**: `#edge-ai`, `#small-language-models`, `#on-device-inference`, `#tool-calling`, `#model-compression`

---

<a id="item-tech-news-9"></a>
### [TimesFM 2.5 发布](https://github.com/google-research/timesfm) ⭐️ 7.0/10

Google Research 的 TimesFM 是一个用于时间序列预测的预训练基础模型，这个仓库集中发布了论文、模型检查点和安装方式。当前最新模型版本是 TimesFM 2.5，相比 2.0 采用 2 亿参数、支持最长 16k 上下文，并通过可选的 3000 万参数 quantile head 提供最长 1k 预测跨度的连续分位数预测。项目说明还提到 2.5 版本移除了 \`frequency\` 指示器，并新增了一些预测标志；同时提供 PyPI 安装、Torch/Flax/XReg 变体，以及本地可编辑安装。仓库明确说明这是开源版本，不是 Google 官方支持产品。

rss · GitHub Trending - Python Daily · 8月17日 05:54

**「背景」** 时间序列基础模型试图用一个预训练模型覆盖多种预测任务，类似语言模型在文本上的做法。TimesFM 对应的论文是《A decoder-only foundation model for time-series forecasting》，并在 Google Research 博客中作过介绍。

**「影响」** 对于做需求、指标和传感器预测的开发者，这个仓库提供了可直接试用的预训练模型、旧版本回退路径和分位数预测能力，降低了从零训练的门槛。

**标签**: `#machine learning`, `#time series forecasting`, `#foundation models`, `#Google Research`, `#open source`

---

<a id="item-tech-news-10"></a>
### [Rayhunter 发布](https://github.com/EFForg/rayhunter) ⭐️ 7.0/10

EFF 发布了 Rayhunter，这是一个用 Rust 编写的开源工具，用于在支持的移动热点设备上检测 IMSI catcher，也就是 cell-site simulator 或 stingray。项目最初是为廉价的 Orbic RC400L 设计的，但在社区贡献下，也已支持部分其他设备。官方强调它尽量降低误报，并把安装和使用设计得尽可能简单，以便非技术用户也能上手。项目同时给出了安装指南、社区支持入口和法律免责声明，提醒用户在美国以外地区先评估当地法律风险。

rss · GitHub Trending - Rust Daily · 8月17日 05:55

**「背景」** IMSI catcher 是一种通过伪装成基站来诱导手机连接的设备，常被用于监听或定位移动终端。Rayhunter 的目标是帮助用户在无线网络环境中识别这类可疑设备，从而提升隐私和通信安全。

**「影响」** 这为使用受支持移动热点的隐私敏感用户和安全研究者提供了一个可部署的开源检测工具。

**标签**: `#rust`, `#open-source`, `#security`, `#privacy`, `#wireless`

---

<a id="item-tech-news-11"></a>
### [vLLM Semantic Router 发布](https://github.com/vllm-project/semantic-router) ⭐️ 7.0/10

vLLM Semantic Router 是一个面向异构 LLM 推理的可编程 Mixture-of-Models 路由器，项目页把它描述为“让你的 Mixture-of-Models 可编程”。它会根据请求信号、用户偏好和应用策略，选择或组合合适的模型路径，用于在不同模型、不同算力和不同部署位置之间进行路由。项目方称这有助于在不把路由逻辑硬编码进应用的情况下，改善质量、成本、延迟、隐私和安全。仓库还提供了文档、在线 Playground、博客、论文与安装脚本入口，说明它既面向使用者也面向贡献者。

rss · GitHub Trending - Go Daily · 8月17日 05:46

**「背景」** “Mixture-of-Models”指在同一应用或服务中按任务、成本、延迟、隐私或安全需求组合使用多个大语言模型，而不是把所有请求固定交给单一模型。语义路由层的作用是在应用和模型服务之间根据请求信号、用户偏好和策略做选择或编排，vLLM Semantic Router 将这一能力定位为面向异构 LLM 基础设施的可编程组件。

**「影响」** 对运营混合模型和混合基础设施的团队来说，它把模型选择与策略执行抽象成独立的路由层，便于统一管理异构推理路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/semantic-router">GitHub - vllm-project/semantic-router: A programmable Mixture ...</a></li>

</ul>
</details>

**标签**: `#llm-inference`, `#model-routing`, `#open-source`, `#ai-infrastructure`

---

<a id="item-tech-news-12"></a>
### [GitHub 大规模宕机调查中](https://www.ithome.com/0/990/842.htm) ⭐️ 7.0/10

据 IT 之家 8 月 17 日报道，GitHub 突发大规模宕机，Pull Requests、Issues、Webhooks、Actions 等核心功能受到不同程度影响，官方仍在调查且尚未确认根本原因。GitHub 仪表板显示，官方从 UTC 13:40（北京时间 21:40）开始注意到部分服务性能故障报告，UTC 13:45（北京时间 21:45）起 Webhooks、Pull Request、Issue 等功能出现不同程度宕机。到 UTC 14:04（北京时间 22:04），网页和 API 流量错误率约达 20%，归档文件下载和原始存储库下载错误率约为 50%。第三方故障统计网站 Downdetector 显示，GitHub 无法正常访问的报告从北京时间 9:24 左右开始明显增加。

rss · IT之家 · 8月17日 14:46

**「背景」** GitHub 是广泛使用的代码托管和协作平台，Pull Request、Issue、Webhook、Actions 和 API 是许多开发团队日常评审、跟踪、自动化构建与集成流程的基础组件。此类平台级故障通常会同时影响人工协作流程和依赖 GitHub 事件、下载或 API 的自动化系统。

**「影响」** 受影响的开发者和组织可能会遇到代码评审、问题跟踪、CI/CD 触发、API 调用以及源码或归档下载失败或延迟。

**标签**: `#GitHub`, `#outage`, `#developer-tools`, `#cloud-infrastructure`

---

<a id="item-tech-news-13"></a>
### [声波驱动微型船和飞行器](https://www.ithome.com/0/990/837.htm) ⭐️ 7.0/10

EPFL 微型生物机器人系统实验室开发出一种全新的声波推进方案，用 3D 打印腔体把声音直接转化为推力，做出了无需电机、齿轮或磁性零件的微型船和飞行器。相关成果发表在《Science Advances》上，核心机制是声学共振：特定频率的声音进入中空腔体后，会让内部空气振动并从开口形成定向喷流，从而推动装置前进。研究团队在微型船上实现了用不同可听频率分别激活共振器，并完成前进、转向、绕障和自主导航。飞行器则使用超声波工作，其中一款仅重 150 微克，叶片式版本最高转速可达 13000rpm，但当前实验尺度仍然很小，升高不到 5 毫米。

rss · IT之家 · 8月17日 14:13

**「背景」** 声学共振指的是气体或结构在特定频率下被强烈激发，从而放大振动和气流效应。微型机器人领域一直在寻找比电机、齿轮和磁驱动更轻、更易缩小的推进方式，因此把结构本身设计成“会动的推进器”具有研究价值。

**「影响」** 这项工作为极微型机器人提供了一种不依赖机械传动和磁部件的新型推进路径，尤其适合继续向更小尺寸和多自由度控制扩展。

**标签**: `#micro-robotics`, `#acoustic propulsion`, `#robotics research`, `#Science Advances`

---

<a id="item-tech-news-14"></a>
### [苹果调整广告授权规则](https://www.reuters.com/business/retail-consumer/apple-change-app-data-consent-rules-german-regulator-says-2026-08-17/) ⭐️ 7.0/10

苹果将调整 iPhone 和 iPad 上与应用广告数据授权相关的规则，以回应德国监管机构对其 App 追踪透明度框架（ATT）的竞争担忧。德国方面认为，ATT 对苹果自家应用更有利，涉嫌违反竞争规则，因此要求第三方授权弹窗必须保持中立，并去除劝阻性措辞和符号。苹果需在裁决送达后四个月内落实这些变更，相关承诺有效期为七年。报道还提到，法国和意大利此前已分别就此对苹果罚款 1.5 亿欧元和 9860 万欧元。

telegram · zaihuapd · 8月17日 12:50

**「背景」** App Tracking Transparency 是苹果用于控制应用是否可跟踪用户并用于定向广告的隐私框架，通常会在首次授权时向用户展示提示。此类授权弹窗的措辞和视觉设计会直接影响用户是否同意，因此也常成为隐私与平台竞争监管的焦点。

**「影响」** 受影响的第三方应用和广告技术公司将需要按德国要求调整授权界面设计，而苹果也要接受更严格的竞争合规约束。

**标签**: `#Apple`, `#privacy`, `#app-store`, `#adtech`, `#regulation`

---

## 科技博客

<a id="item-tech-blog-1"></a>
### [分布式层级卸载](https://vllm.ai/blog/2026-08-17-distributed-layerwise-offload) ⭐️ 8.0/10

rss · vLLM Blog · 8月17日 00:00

**「背景」** 这篇文章讨论的是：当视频/扩散模型大到单卡 HBM 装不下时，单纯把权重放到主机内存也会被另一道墙挡住，因为纯 DP 会让每个 rank 都保留一份完整模型，主机内存和冷启动 RSS 都会按设备数线性膨胀。作者以 Cosmos3-Super 这类 64B 以上模型为例，说明既要压住 HBM 占用，又要避免 host RAM 随 dp\_size 爆炸。

**「方案」** 他们把问题拆成四层协作：先用 meta device 加 mmap，把参数变成指向共享 page cache 的视图，避免加载时生成 dp\_size 份私有副本；再把权重按 rank 切成 1/dp\_size，运行时用 AllGather 在通信流上重建当前层，从而把主机驻留权重从“每卡一整份”降到“全局一整份”。随后用固定双缓冲把设备侧只限制为两个最大 block 的槽位，并把 H2D 与 AllGather 和计算重叠起来，所以 HBM 里始终只有两层权重，而不是整个模型。最后利用 AllGather 本身与请求无关这一点，让每个 DP rank 同时处理不同请求，实测在 4 路并发下吞吐达到单请求 HSDP 的约 3.3 倍；作者也指出，Ascend 上 cgroup 看不到 /dev/davinci\_manager 里的 pinned shard，因此必须把可见内存和物理 RAM 分开理解。文章给出多组验证：冷启动峰值、主机内存、HBM、正确性哈希都被逐项测过，但这些结果仍然依赖具体的 vLLM-Omni 版本、拓扑和硬件配置。

**「启示」** 作者的核心结论是，超大 DiT 的可扩展性不只取决于“能不能分片”，还取决于加载、驻留和并发这三件事是否一起设计。把共享 page cache、按层重建和请求并发放在同一条执行链上，才能把 200B 级模型推进到可部署区间。

**标签**: `#model-serving`, `#memory-management`, `#distributed-systems`, `#allgather`, `#diffusion-models`

---