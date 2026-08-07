---
layout: default
title: "Horizon Summary: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
---

> 从 312 条内容中筛选出 23 条重要资讯。

---

1. [Visual Studio Code 的开源开发仓库](#item-1) ⭐️ 9.0/10
2. [OpenAI 改进 GPT-5.6 Sol 并扩大 Luna 免费访问](#item-2) ⭐️ 8.0/10
3. [Datasette 1.0a38 修复 SQL 注入数据泄露漏洞](#item-3) ⭐️ 8.0/10
4. [Datasette 0.65.3 回移 SQL 注入修复](#item-4) ⭐️ 8.0/10
5. [Cloudflare Computer 为智能体提供持久化虚拟计算机](#item-5) ⭐️ 8.0/10
6. [Uber 开源 ADR 保护企业 AI 代理](#item-6) ⭐️ 8.0/10
7. [AWS 发布人工智能代理开发工具包](#item-7) ⭐️ 8.0/10
8. [LangChain 推出面向内部异步编码代理的 Open SWE](#item-8) ⭐️ 8.0/10
9. [Promptfoo 将大语言模型评估与红队测试融入开发流程](#item-9) ⭐️ 8.0/10
10. [PSE-CZ 提升超导量子门速度与保真度](#item-10) ⭐️ 8.0/10
11. [IntelliJ IDEA 智能感知进入 VS Code 与 Cursor。](#item-11) ⭐️ 8.0/10
12. [台积电研发高性能单层 MoS2 顶栅极晶体管](#item-12) ⭐️ 8.0/10
13. [TONTOU 攻击绕过 AMD 与 Intel 处理器的 Spectre v2 缓解措施](#item-13) ⭐️ 8.0/10
14. [八家多晶硅企业承诺不低于成本销售。](#item-14) ⭐️ 8.0/10
15. [OpenAI 发布 Agent Plugins 1.0.0 规范](#item-15) ⭐️ 8.0/10
16. [AI 设计出可杀死大肠杆菌的噬菌体基因组。](#item-16) ⭐️ 8.0/10
17. [谷歌核心研究者创办 Discovery Loop，探索自动化科学研究](#item-17) ⭐️ 8.0/10
18. [双向扩散模型用往返一致性识别推演误差](#item-18) ⭐️ 8.0/10
19. [将重复 LLM 轨迹合成为确定性 NLP 流水线。](#item-19) ⭐️ 8.0/10
20. [BESIII 报告迄今最有力的胶球证据。](#item-20) ⭐️ 8.0/10
21. [DeepSeek 以 2080 万美元入股宇树科技上海 IPO](#item-21) ⭐️ 8.0/10
22. [Suno 为 AI 生成歌曲增加防护措施。](#item-22) ⭐️ 8.0/10
23. [阿里巴巴拟向大型 Qwen 用户收取收入分成。](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Visual Studio Code 的开源开发仓库](https://github.com/microsoft/vscode) ⭐️ 9.0/10

microsoft/vscode 仓库是 Microsoft 与社区共同开发 Code - OSS 的公开代码库。所提供的材料介绍了仓库和项目结构，但没有报告具体的新版本、突破或有日期的变更。 该仓库支撑着软件行业广泛使用的开发环境之一，并影响代码编辑、调试、导航和基于扩展的工作流程。其公开开发模式还让开发者能够了解路线图、迭代计划、问题和贡献流程。 Code - OSS 采用 MIT 许可证，而 Visual Studio Code 发行版加入了 Microsoft 特定的定制内容和扩展，并采用传统的 Microsoft 产品许可证。Visual Studio Code 每月更新，支持 Windows、macOS 和 Linux，并提供用于获取每日版本的 Insiders 构建版。

rss · GitHub Trending - TypeScript Daily · 8月7日 04:03

**背景**: Code - OSS 是 Visual Studio Code 发行版所基于的开源仓库。两者关系密切，但 Visual Studio Code 包含 Microsoft 特定的附加内容，因此更准确的说法是它建立在开源代码之上，而不是与该仓库完全相同。VS Code 还通过独立的扩展宿主进程支持扩展，有助于将扩展活动与主编辑器隔离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/vscode/wiki/Differences-between-the-repository-and-Visual-Studio-Code">Differences between the repository and Visual Studio Code</a></li>
<li><a href="https://code.visualstudio.com/docs/supporting/FAQ">Visual Studio Code FAQ</a></li>
<li><a href="https://code.visualstudio.com/api/advanced-topics/extension-host">Extension Host | Visual Studio Code Extension API</a></li>

</ul>
</details>

**标签**: `#Visual Studio Code`, `#TypeScript`, `#Developer Tools`, `#Open Source`, `#Microsoft`

---

<a id="item-2"></a>
## [OpenAI 改进 GPT-5.6 Sol 并扩大 Luna 免费访问](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/) ⭐️ 8.0/10

OpenAI 更新了面向 ChatGPT Plus 和 Pro 用户的 GPT-5.6 Sol，提供更可靠的事实性回答、更聚焦的回复，以及用于控制推理深度的选项。免费用户将默认使用 GPT-5.6 Luna，并获得处理复杂任务的 Think 按钮；从下周开始还可进行无限文本对话。 向免费用户更广泛提供具备推理能力的模型和无限文本聊天，可能显著扩大高质量 AI 助手的可及性。此次更新也让模型选择与推理深度成为日常 ChatGPT 体验的一部分，并会影响用户对付费层级价值和透明度的看法。 OpenAI 表示，在其内部涉及金融、医疗和法律的事实性问题评测中，GPT-5.6 Luna 相比 GPT-5.5 Instant 的事实错误减少约 62%，GPT-5.6 Sol 则减少约 68%。公司还为 18 岁以下用户增加了更强的训练和系统级保护，包括限制浪漫角色扮演、规避年龄限制及不当内容。

hackernews · tedsanders · 8月6日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=49199357)

**背景**: GPT-5.6 是一个模型系列，包含 Sol、Terra 和 Luna 三个版本，分别面向不同的能力、速度与成本取舍。OpenAI 将 Sol 定位为旗舰版本，而 Luna 则是速度最快、成本最低的版本。推理控制允许用户为困难提示请求更多计算量，通常以更慢的响应速度换取更深入的问题解决能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>
<li><a href="https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt">GPT-5.6 in ChatGPT - OpenAI Help Center</a></li>
<li><a href="https://developers.openai.com/api/docs/models/gpt-5.6-luna">GPT-5.6 Luna Model | OpenAI API</a></li>

</ul>
</details>

**社区讨论**: 评论者总体欢迎向免费用户开放推理能力，其中一人认为，这对社会的影响可能超过新的付费模型或编程代理。主要批评集中在界面透明度：有用户称付费方案的默认设置可能隐藏了更高推理强度的 Sol 选项，因此质疑这是疏忽还是暗黑模式。也有人认为将 Luna 设为免费默认模型只是正常的产品分层，而非所谓的仓促之举；另有评论者反对让用户自行决定推理深度。

**标签**: `#OpenAI`, `#ChatGPT`, `#AI Models`, `#Reasoning Models`, `#AI Accessibility`

---

<a id="item-3"></a>
## [Datasette 1.0a38 修复 SQL 注入数据泄露漏洞](https://simonwillison.net/2026/Aug/6/datasette/#atom-everything) ⭐️ 8.0/10

Datasette 1.0a38 修复了一个 SQL 注入漏洞，该漏洞影响通过 Datasette 权限系统在同一数据库中同时提供公共表和私有表的实例。拥有公共表访问权限的用户可能绕过 execute-sql 限制并读取私有表数据；Datasette 0.65.3 也包含此修复。 受影响的管理员可能会将原本应保持私有的数据未经授权地暴露出去，因此混合可见性部署应立即升级或调整配置。该漏洞也说明，当公共数据和私有数据共用一个 SQLite 数据库时，必须一致地执行数据库、表和查询权限。 同时提供公共表和私有表的管理员应禁用该数据库的 execute-sql 权限，以阻止用户在那里执行原始 SQL 查询。官方称这种配置可能较为少见，而且该漏洞提供的是私有表的只读访问权限，并不能修改数据。

rss · Simon Willison · 8月6日 18:24

**背景**: 除非配置身份验证和权限限制，否则 Datasette 通常允许访问者浏览数据并执行只读 SQL 查询。其权限系统可以控制对数据库、表和查询的访问；SQL 注入则是攻击者设法将恶意 SQL 代码插入数据库查询的一类漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/stable/authentication.html">Authentication and permissions - Datasette documentation</a></li>
<li><a href="https://docs.datasette.io/en/latest//authentication.html">Authentication and permissions - Datasette documentation</a></li>
<li><a href="https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL+Injection/SQLite+Injection.md">PayloadsAllTheThings/ SQL Injection / SQLite Injection .md at master...</a></li>

</ul>
</details>

**标签**: `#Datasette`, `#SQL Injection`, `#Security`, `#SQLite`, `#Access Control`

---

<a id="item-4"></a>
## [Datasette 0.65.3 回移 SQL 注入修复](https://simonwillison.net/2026/Aug/6/datasette-2/#atom-everything) ⭐️ 8.0/10

Datasette 0.65.3 将 1.0a38 alpha 版本中的 SQL 注入安全修复回移到稳定的 0.65 系列。该修复针对同一数据库同时提供公开表和私有表、并通过 Datasette 权限系统控制访问的实例。 SQL 注入可能让攻击者通过构造输入修改数据库查询，因此这一回移修复对继续使用稳定版 Datasette 的用户十分重要。受影响部署的管理员无需迁移到 1.0 alpha 系列即可获得该安全修复。 该版本明确为 Datasette 0.65.3，对应修复最初在 1.0a38 中引入。该漏洞与单个数据库中公开表和私有表混合提供、并使用 Datasette 权限配置控制访问有关，因此具体部署方式决定了是否受到影响。

rss · Simon Willison · 8月6日 18:22

**背景**: Datasette 是一个用于探索和发布数据的开源多功能工具。SQL 注入是一类安全问题，攻击者的不可信输入可能被当作 SQL 查询的一部分执行；Datasette 权限系统用于控制表的访问，包括区分公开数据和私有数据的配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://minifeed.net/items/5XWTPPQjis77">datasette 1 . 0 a 38 | Simon Willison's Weblog | minifeed</a></li>
<li><a href="https://datasette.io/">Datasette : An open source multi-tool for exploring and publishing data</a></li>
<li><a href="https://owasp.org/www-community/attacks/SQL_Injection">SQL Injection - OWASP Foundation</a></li>

</ul>
</details>

**标签**: `#Datasette`, `#SQL injection`, `#Security`, `#Database`, `#Open source`

---

<a id="item-5"></a>
## [Cloudflare Computer 为智能体提供持久化虚拟计算机](https://github.com/cloudflare/computer) ⭐️ 8.0/10

Cloudflare 发布了 Cloudflare Computer，这是一个仅供预览的开源运行时，将智能体的虚拟文件系统权威地存储在 Durable Object 内的 SQLite 中。统一的 `workspace.runtime.exec` 接口支持容器、隔离 shell 和隔离 JavaScript 后端，并会在首次使用时延迟连接后端。 该项目为人工智能智能体提供了持久化工作区，并在完整 Linux 容器与轻量级 Workers 隔离环境之间提供一致的执行抽象。这可能通过在 Workers 生态中结合持久化状态、沙箱执行和可插拔后端，简化智能体基础设施的构建。 容器后端通过真实的 FUSE 挂载公开由 SQLite 支持的状态，`computerd` 则通过 capnweb RPC 同步变更；隔离 JavaScript 后端还提供由工作区支持的 `node:fs/promises`，以及受信任的 `ws:git` 和 `ws:artifacts` 模块。该软件包明确不适合生产环境，因为其 API 尚不稳定，仓库中的 `docs/` 描述的是未来方向，而不是当前实现。

rss · GitHub Trending - Daily · 8月7日 03:45

**背景**: Durable Object 是 Cloudflare 的一种执行单元，可以将状态保存在接近代码的位置；其 SQLite 存储提供基于本地 SQL 的持久化，不必让每次操作都跨越网络。FUSE 是 Linux 的一种机制，允许用户空间进程提供文件系统挂载，因此容器后端可以让虚拟工作区表现为普通文件系统。Dynamic Workers 能在隔离的 Workers 环境中运行运行时提供的代码，对于某些工作负载而言可以作为比容器更轻量的选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/sqlite-in-durable-objects/">Zero-latency SQLite storage in every Durable Object</a></li>
<li><a href="https://docs.kernel.org/filesystems/fuse/">FUSE (Filesystem in Userspace) Technical Documentation — The Linux Kernel documentation</a></li>
<li><a href="https://developers.cloudflare.com/dynamic-workers/">Dynamic Workers - Cloudflare Docs</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Cloudflare Workers`, `#Durable Objects`, `#serverless`, `#virtual filesystem`

---

<a id="item-6"></a>
## [Uber 开源 ADR 保护企业 AI 代理](https://github.com/uber/ADR) ⭐️ 8.0/10

Uber 发布了 ADR（Agentic AI Detection and Response），这是一个已在 Uber 生产环境部署的平台，其配套论文已被 MLSys 2026 接收。开源仓库包含 ADR Sensor、ADR-Bench 和 ADR Detector，用于代理可观测性、安全评估和威胁检测。 ADR 为企业提供了一种面向生产环境的方法，用于监控代理意图、工具调用和执行轨迹，并测试和检测员工端及客户端 AI 代理的不安全行为。该项目为快速发展的 AI 安全生态补充了实用基础设施，尤其适用于通过 MCP 与企业工具交互的代理。 ADR-Bench 包含 303 个任务、133 个 MCP 服务器，并覆盖全部 17 种代理攻击技术；ADR Detector 先进行高召回率分流，再对可疑会话执行更深入的代理推理。当前开源版本不包含用于阻止不安全操作的 ADR Prevention，也不包含离线红队测试引擎 ADR Explorer。

rss · GitHub Trending - Python Daily · 8月7日 03:59

**背景**: AI 代理是能够通过决策和使用工具来完成任务的软件系统，因此其安全风险超出了传统聊天机器人的范围。可观测性会记录代理活动和执行上下文，帮助组织了解代理做了什么以及为什么这样做。MCP 即 Model Context Protocol，是 ADR 用于代理与企业服务交互的工具集成协议；ADR-Bench 则在这些真实条件下评估安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/uber/ADR">GitHub - uber/ADR: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber. · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2605.17380">[2605.17380] ADR: An Agentic Detection System for Enterprise Agentic AI Security</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#AI security`, `#threat detection`, `#observability`, `#enterprise systems`

---

<a id="item-7"></a>
## [AWS 发布人工智能代理开发工具包](https://github.com/aws/agent-toolkit-for-aws) ⭐️ 8.0/10

AWS 发布了面向生产环境的 Agent Toolkit for AWS，这是一个采用 Apache-2.0 许可的工具包，包含 AWS 官方支持的 MCP 服务器、技能、插件和安全防护机制。它支持 Claude Code、Codex、Cursor 和 Kiro 等人工智能编程代理，并提供核心 AWS 开发、基于 Bedrock 的代理、数据分析以及 DevSecOps 工作流插件。 该工具包让人工智能编程代理能够更直接地使用 AWS 专属的应用程序接口、文档、基础设施模式和运维流程，从而可能减少错误并提高云开发的一致性。AWS 官方支持以及对多种常用代理的兼容性，可能会加快人工智能辅助应用部署和管理的普及。 用户可以通过 AWS 命令行界面的`aws configure agent-toolkit`配置工具包，也可以安装`aws-core`、`aws-agents`和`aws-data-analytics`等代理专用插件；每个插件都可以捆绑 AWS MCP 服务器配置和代理技能。现有资料展示了广泛的集成范围，但对于具体的防护机制、权限模型和运维边界，技术细节仍然有限。

rss · GitHub Trending - Python Daily · 8月7日 03:59

**背景**: 模型上下文协议（MCP）规定了人工智能代理如何通过 MCP 服务器与外部工具和服务交互。在该工具包中，这些服务器把编程代理连接到 AWS 功能，技能则提供可重复使用的 AWS 专属知识和工作流。插件会将这些组件打包，便于在受支持的编程环境中安装。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/aws/agent-toolkit-for-aws">GitHub - aws/agent-toolkit-for-aws: Official, AWS-supported MCP servers, skills, and plugins to help AI agents build on AWS · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/">Agent Toolkit for AWS - For Kiro, Claude Code, Codex, & MCP-Compatible Agents</a></li>

</ul>
</details>

**标签**: `#AWS`, `#AI Agents`, `#MCP`, `#Cloud Development`, `#Developer Tools`

---

<a id="item-8"></a>
## [LangChain 推出面向内部异步编码代理的 Open SWE](https://github.com/langchain-ai/open-swe) ⭐️ 8.0/10

LangChain 发布了 Open SWE，这是一个采用 MIT 许可证的开源框架，用于构建组织专属的异步编码代理。该框架基于 LangGraph 和 Deep Agents，支持云端沙箱、Slack 与 Linear 调用、子代理编排以及自动创建拉取请求。 Open SWE 让更多团队能够采用工程组织内部编码代理的模式，并根据自身的集成、权限、上下文和安全边界进行定制。其云原生异步模型可以让代理并行处理多个开发任务，同时工程师继续使用现有工具。 该框架通过组合 Deep Agents 构建，而不是分叉现有代理或从零开始，因此可以持续引入上游改进，同时支持定制编排、工具和中间件。示例包含 HTTP 请求、网址获取、Linear 评论和 Slack 线程回复等工具，但现有信息没有提供采用规模或生产性能数据。

rss · GitHub Trending - Python Daily · 8月7日 03:59

**背景**: LangGraph 是一个用于构建有状态代理的底层编排框架，也就是能够在多个步骤或交互之间保存并管理状态的系统。Open SWE 将这一基础与 Deep Agents 结合，用于协调编码任务、工具和子代理。异步编码代理可以在云端运行任务，不要求工程师持续保持本地会话，并可将完成的工作以拉取请求的形式返回。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/langchain-ai/langgraph">GitHub - langchain- ai / langgraph : Build resilient agents . · GitHub</a></li>
<li><a href="https://blog.langchain.com/introducing-open-swe-an-open-source-asynchronous-coding-agent/">Introducing Open SWE: An Open-Source Asynchronous Coding Agent</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#LangChain`, `#LangGraph`, `#Developer tools`, `#Open source`

---

<a id="item-9"></a>
## [Promptfoo 将大语言模型评估与红队测试融入开发流程](https://github.com/promptfoo/promptfoo) ⭐️ 8.0/10

Promptfoo 是一个用于评估和红队测试大语言模型提示词、智能体与 RAG 应用的开源命令行工具和程序库。该仓库说明 Promptfoo 现已加入 OpenAI，但仍以 MIT 许可证开源，并支持自动化评估、模型对比、漏洞扫描和 CI/CD 集成。 它为开发团队提供了一种实用方法，可以跨模型衡量提示词和应用行为，并将安全检查纳入日常工程流程。随着 RAG 系统越来越普及，团队需要同时评估检索相关性、回答准确性和事实依据，而不能只依赖通用模型基准测试。 通过 npm 和 npx 使用时，快速入门要求 Node.js >=22.22.0，并推荐使用 Node.js 24 LTS；用户也可以通过 Homebrew 和 pip 安装。大多数模型提供商都需要 API 密钥，工具通过声明式配置以及 `promptfoo eval` 和 `promptfoo view` 等命令运行并查看评估结果。

rss · GitHub Trending - TypeScript Daily · 8月7日 04:03

**背景**: 大语言模型评估通过预先定义的测试和指标，衡量模型或应用在特定任务上的表现；基准测试通常用于比较不同系统的结果。RAG 将信息检索与文本生成结合起来，因此评估时既要关注是否检索到相关信息，也要关注生成答案是否准确并有信息依据。红队测试通过对系统进行对抗性测试，在部署前发现提示词注入等安全弱点和其他失效情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.evidentlyai.com/llm-guide/llm-benchmarks">30 LLM evaluation benchmarks and how they work</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators">Retrieval-Augmented Generation (RAG) Evaluators for ...</a></li>
<li><a href="https://arxiv.org/abs/2405.07437">[2405.07437] Evaluation of Retrieval-Augmented Generation: A ... Evaluation of Retrieval-Augmented Generation: A Survey Evaluating Retrieval Augmented Generation: A Comprehensive ... Testing RAG Applications: Evaluation Best Practices & Metrics A complete guide to RAG evaluation: metrics, testing and best ...</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#AI red teaming`, `#RAG`, `#prompt engineering`, `#developer tools`

---

<a id="item-10"></a>
## [PSE-CZ 提升超导量子门速度与保真度](https://www.ithome.com/0/986/894.htm) ⭐️ 8.0/10

中国科学技术大学与本源量子联合团队提出并在“本源悟空”超导量子计算机上验证了参数空间扩展受控相位门方案，即 PSE-CZ。针对 20 对两比特量子门的测试显示，在 30 至 40 纳秒的门长下，PSE-CZ 能够降低相干误差，性能优于传统 CZ 门。 这项成果针对超导量子计算中的核心控制难题，即缩短两比特量子门时间往往会损害保真度。更快且更高保真的量子门有望提升量子线路可靠性，并可能将这一方法推广到超导、离子阱和固态自旋等量子计算平台。 团队称，PSE-CZ 通过抑制短时畸变引起的相干误差，使量子门性能更加接近退相干极限。相关成果发表于《物理评论快报》，但目前公布的是在特定设备上的实验测量结果，并不意味着所有量子计算平台都能获得相同性能。

rss · IT之家 · 8月7日 03:29

**背景**: 超导量子比特是利用超导电路实现的量子信息单元，量子门则用于操控量子比特的状态。两比特量子门同时作用于一对量子比特，是量子算法建立量子比特相互作用的重要操作。退相干是量子系统受环境和控制因素影响而失去相干性的过程，相干误差则是量子门运行过程中可能累积的系统性误差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/596392090">超导量子比特（二）：主要特征介绍 - 知乎</a></li>

</ul>
</details>

**标签**: `#量子计算`, `#超导量子比特`, `#量子门保真度`, `#量子控制`, `#科研突破`

---

<a id="item-11"></a>
## [IntelliJ IDEA 智能感知进入 VS Code 与 Cursor。](https://www.ithome.com/0/986/866.htm) ⭐️ 8.0/10

JetBrains 发布了面向 VS Code 系编辑器的预览版 Java & Kotlin by IntelliJ IDEA 扩展，首批支持 VS Code 和 Cursor。该扩展将 IntelliJ IDEA 驱动的代码补全、导航、代码分析、重构辅助，以及 Java、Kotlin 和混合语言项目支持带入这些编辑器。 此次发布让偏好 VS Code 或 Cursor 的开发者，无需切换到完整的 IntelliJ IDEA 应用，也可能获得其成熟的 Java 和 Kotlin 语言工具能力。它可能改变大型 Java/Kotlin 代码库团队的编辑器选择，但实际采用情况仍取决于预览版稳定性、兼容性以及后续订阅要求。 该扩展可导入带有 Maven、Gradle 或 Bazel 构建文件的项目，并定位于大型项目和单体仓库场景。JetBrains 表示其代码分析和快速修复功能与 Red Hat、Oracle 的 Java 扩展存在重叠，建议测试时禁用后两者；预览结束后需订阅 IntelliJ IDEA Ultimate，而预览版本每两周更新一次并刷新 30 天评估期。

rss · IT之家 · 8月7日 03:07

**背景**: IntelliJ IDEA 是 JetBrains 的集成开发环境，并为 Kotlin 提供一流支持，包括编码辅助、重构、调试和分析工具。VS Code 系编辑器通过可安装扩展获得语言支持；Open VSX 是 Eclipse 的开源扩展注册中心，定位为 Visual Studio Marketplace 的替代方案。Maven、Gradle 和 Bazel 都是描述项目及其依赖如何构建的构建系统，因此导入这些配置是准确分析 Java 和 Kotlin 项目的关键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.jetbrains.com/help/idea/get-started-with-kotlin.html">Get started with Kotlin | IntelliJ IDEA Documentation</a></li>
<li><a href="https://open-vsx.org/">Open VSX Registry</a></li>
<li><a href="https://bazel.build/start/java?hl=zh-cn">Bazel 教程： 构 建 Java 项 目</a></li>

</ul>
</details>

**标签**: `#JetBrains`, `#IntelliJ IDEA`, `#VS Code`, `#Java`, `#Kotlin`

---

<a id="item-12"></a>
## [台积电研发高性能单层 MoS2 顶栅极晶体管](https://www.ithome.com/0/986/861.htm) ⭐️ 8.0/10

台积电与阳明交通大学研究团队研发出高性能单层 MoS2 顶栅极晶体管，相关成果已发表于《自然·电子学》。该器件被认为可能成为支持 1 纳米以下后硅芯片微缩的基础组件。 当硅基技术逐渐接近物理极限时，单层 MoS2 可能帮助晶体管继续微缩，从而为手机、电脑和未来的人工智能设备带来更高速度与更低功耗。该成果还与新兴的 CFET 架构以及围绕二维材料发展的半导体设备生态有关。 报道没有给出具体性能指标、制造良率或商业化时间表，因此目前仍属于科研成果展示，不能视为已经具备量产条件。文章将 MoS2 与约 0.7 纳米的 A7 制程及 CFET 时代联系起来，但接触、电路加工和大规模集成仍是重要的实际挑战。

rss · IT之家 · 8月7日 02:58

**背景**: 二维半导体的厚度可以达到原子级，有助于在晶体管尺寸缩小时增强栅极对沟道的控制，并减轻短沟道效应。MoS2 是一种正在用于研究传统硅技术之外先进制程的二维半导体。顶栅极晶体管将栅极置于沟道上方，通过栅极控制 MoS2 层中的电流；CFET 则通过堆叠互补类型的晶体管来提高逻辑电路密度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s44287-024-00045-6">Transistor engineering based on 2D materials in the post ...</a></li>
<li><a href="https://edatechsupport.com/portfolio/cfet/">CFET - Eda Tech Support</a></li>

</ul>
</details>

**标签**: `#semiconductors`, `#2D-materials`, `#MoS2`, `#transistors`, `#TSMC`

---

<a id="item-13"></a>
## [TONTOU 攻击绕过 AMD 与 Intel 处理器的 Spectre v2 缓解措施](https://www.ithome.com/0/986/852.htm) ⭐️ 8.0/10

麻省理工学院研究人员 Daniël Trujillo 和 Mengjia Yan 披露了 TONTOU，这是一种可在分支预测器状态被中和后、再次使用前重新污染该状态的时间窗口攻击。在运行 Linux 6.14.0-37-generic 的 AMD Zen 2 系统上，该攻击以每秒 5.47 字节、91.97% 的准确率泄露任意内核内存，其中包括 /etc/shadow 的内容。 这项研究质疑了广泛部署的 Spectre v2 防御措施所依赖的一个关键假设，即攻击者无法在预测器状态清理后、再次使用前影响该状态。虽然已演示的数据提取速度较慢且需要在目标系统上执行本地代码，但它扩大了受影响 AMD 和 Intel 处理器上 Linux 系统的安全风险。 TONTOU 使用中断注入：无特权进程安排定时器中断，使其在内核执行期间触发，并利用中断处理程序在中和后的时间窗口内污染微架构状态。在测试系统上定位并提取 /etc/shadow 的十次尝试中有五次成功，每次尝试平均耗时约 18 分钟。

rss · IT之家 · 8月7日 02:40

**背景**: Spectre v2 也称为分支目标注入，它利用间接分支预测，让处理器在分支结果确认前沿着受攻击者影响的目标进行推测执行。推测执行可能在微架构中留下可测量的痕迹，攻击者可以通过侧信道从中推断数据。Intel eIBRS 和 AMD Safe RET 都旨在限制或隔离这种预测器行为，而 TONTOU 论文认为，近期 AMD 和 Intel 处理器仍存在可被利用的中和到使用时间窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://people.csail.mit.edu/mengjia/data/2026.USENIX.TONTOU.pdf">: On the Exploitability of Time-of-Neutralization to Time-of ...</a></li>
<li><a href="https://www.bleepingcomputer.com/news/security/new-tontou-cpu-attack-bypasses-spectre-v2-fixes-leaks-linux-password-hashes/">New TONTOU CPU attack bypasses Spectre v2 fixes, leaks Linux ...</a></li>
<li><a href="https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/technical-documentation/indirect-branch-restricted-speculation.html">Indirect Branch Restricted Speculation - Intel</a></li>

</ul>
</details>

**标签**: `#CPU Security`, `#Spectre v2`, `#Side-Channel Attacks`, `#Linux Security`, `#AMD and Intel`

---

<a id="item-14"></a>
## [八家多晶硅企业承诺不低于成本销售。](https://www.ithome.com/0/986/836.htm) ⭐️ 8.0/10

8 月 6 日，八家中国主要多晶硅企业在上海签署反内卷倡议书，距国家市场监督管理总局 7 月 31 日开展光伏行业价格合规指导仅一周。企业承诺，光伏产品销售价格及招投标报价不得低于按照统一的《光伏行业成本核算模型通则》核算的成本。 签约企业合计占中国多晶硅有效产能超过 90%，其一致承诺可能实质影响光伏上游供应链的价格纪律和竞争格局。此举将行业自律与监管监督、产能调整相结合，可能缓解破坏性价格竞争，并推动竞争转向质量和效率。 企业表示，低于完全成本价销售必须立即停止并纠正，并将接受市场监管部门检查；发现疑似低价销售违法行为时，应向行业协会和市场监管总局反映或举报。倡议还要求落实新的能耗标准，并主动出清高耗能落后产能。

rss · IT之家 · 8月7日 01:51

**背景**: 多晶硅是光伏产业链上游的核心材料，可用于制造硅片，硅片再进一步加工为电池和组件。《光伏行业成本核算模型通则》于 7 月 27 日发布，旨在为光伏产业链建立统一的成本核算标尺。该标准覆盖硅料、硅片、电池和组件等环节，并区分现金成本、生产成本和完全成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.ithome.com/html/982073.htm">m.ithome.com/html/982073.htm</a></li>
<li><a href="https://baike.baidu.com/item/光伏行业成本核算模型通则/68368424">光伏行业成本核算模型通则 - 百度百科</a></li>
<li><a href="https://www.pvmeng.com/2026/07/27/75155/">中国光伏行业协会关于《光伏行业成本核算模型通则》：光伏行业成本核...</a></li>

</ul>
</details>

**标签**: `#光伏产业`, `#多晶硅`, `#反内卷`, `#行业监管`, `#产能出清`

---

<a id="item-15"></a>
## [OpenAI 发布 Agent Plugins 1.0.0 规范](https://www.ithome.com/0/986/816.htm) ⭐️ 8.0/10

2026 年 8 月 7 日，OpenAI 发布了 Agent Plugins 规范 1.0.0，这是一个面向 AI 智能体组件的开放、厂商中立打包标准。该规范统一了 Agent Skills 和 MCP Servers 等组件的可移植格式，使兼容客户端能够按照相同规则发现并加载它们。 该标准有望减少重复打包和适配工作，让同一套智能体能力更容易在 ChatGPT、Codex 及其他兼容工具之间复用。它在建立共享互操作层的同时，将分发、权限和用户体验交给各客户端自行处理，可能推动智能体软件分发生态发展。 插件目录必须包含 plugin.json 清单文件，skills/ 用于存放 Agent Skills，mcp.json 则描述使用 stdio、Streamable HTTP 或传统 HTTP+SSE 传输方式的 MCP 服务器。该规范只统一插件中可移植的部分，客户端专属扩展、钩子、安装流程、权限和其他运行时行为仍由各客户端决定。

rss · IT之家 · 8月7日 01:33

**背景**: Agent Skills 是一种轻量、开放的目录格式，用于向 AI 智能体提供专业知识和工作流程，核心通常包括包含元数据与说明的 SKILL.md 文件。MCP，即模型上下文协议，是一种开放协议，通过标准化交互方式连接 AI 模型与外部数据源、工具和 API。Agent Plugins 将这类可复用能力放入可预测的目录结构中，供兼容客户端识别和加载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/agentplugins/agent-plugins-spec">GitHub - agentplugins/ agent - plugins -spec: Agent Plugins ...</a></li>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://blog.csdn.net/zgpeace/article/details/156002083">一文搞懂 MCP：从入门到实战（含本地项目 MCP Server 示例）</a></li>

</ul>
</details>

**标签**: `#AI智能体`, `#OpenAI`, `#插件标准`, `#互操作性`, `#MCP`

---

<a id="item-16"></a>
## [AI 设计出可杀死大肠杆菌的噬菌体基因组。](https://www.ithome.com/0/986/809.htm) ⭐️ 8.0/10

斯坦福团队利用 Evo1 和 Evo2 基因组语言模型生成完整噬菌体基因组设计，并在实验室中合成了从中筛选出的 302 个候选方案。据报道，其中 16 个设计产生了能够杀死大肠杆菌的噬菌体。 这一结果表明，生成式 AI 可能已从设计单个生物分子迈向生成可在实验中发挥功能的基因组规模系统。它未来或可扩展噬菌体疗法的设计空间，用于应对抗生素难以有效治疗的细菌感染，包括耐药性感染。 报道中的噬菌体基因组长度约为 5400 个碱基对，远小于最小活细胞约 50 万个碱基对的基因组。Evo1 和 Evo2 使用病毒、细菌、植物和人类的遗传序列训练，随后针对噬菌体生成进行微调；目前报道的验证范围仅限于实验室中杀死大肠杆菌的活性。

rss · IT之家 · 8月7日 01:18

**背景**: 噬菌体是感染特定细菌宿主而非人体细胞的病毒。噬菌体疗法利用这类靶向细菌的病毒治疗细菌感染，并因抗微生物药物耐药性扩散而再次受到关注。基因组语言模型会学习类似 DNA 序列中的统计规律，并像文本语言模型生成文字一样生成新序列，但其生物功能仍必须通过合成和实验室测试来验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1883681460155838483">Evo2：跨生命领域的基因组“造物主”模型 - 知乎</a></li>
<li><a href="https://www.maltsci.com/zh/topic/how-does-phage-therapy-treat-bacterial-infections/">噬 菌 体 疗 法 如 何 治 疗 细 菌 感 染 ？ | MaltSci 麦伴科研</a></li>

</ul>
</details>

**标签**: `#生成式AI`, `#合成生物学`, `#噬菌体疗法`, `#抗生素耐药`, `#生物安全`

---

<a id="item-17"></a>
## [谷歌核心研究者创办 Discovery Loop，探索自动化科学研究](https://www.36kr.com/p/3927691611895943) ⭐️ 8.0/10

8 月 5 日，谷歌宣布重大人工智能部门调整：Demis Hassabis 转任 Google DeepMind 董事长并出任 Alphabet 首席科学家，Jeff Dean、Sanjay Ghemawat、Oriol Vinyals 和 Quoc Le 则共同创办公益型机构 Discovery Loop。该机构希望让人工智能提出实验、编写并运行所需代码或工具、评估结果，再根据结果进入下一轮研究。 Discovery Loop 汇集了曾参与塑造谷歌核心基础设施和现代机器学习的研究者，使自动化研究获得了极具影响力的创始团队。若这种方法能够奏效，人工智能代理可能加速机器学习、科学研究、生物、芯片设计等结果可以可靠衡量的领域中的实验过程。 谷歌将成为 Discovery Loop 的创始投资者和云合作伙伴，并在其第一年提供算力；但该机构刚刚成立，尚未开始大规模招聘，据报道甚至还没有正式办公场所。Jeff Dean 表示，这种方法成立需要两个条件：任务能够反复试验，结果能够被可靠评价。

rss · 36氪 - 24小时热榜 · 8月6日 08:19

**背景**: 研究循环是一种工作流：人工智能代理提出行动方案、执行方案、观察结果，再决定下一步做什么。Discovery Loop 将其描述为科学方法的自动化，并希望把这种方式从单次模型实验扩展到更广泛的科学和工程研究。谷歌的 Pathways 体现了其在大规模机器学习架构方面的探索，而 AutoML-Zero 则代表了更早期的机器学习算法设计自动化尝试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.discoveryloop.com/">Discovery Loop — Continuous Exploration</a></li>
<li><a href="https://blog.google/innovation-and-ai/products/introducing-pathways-next-generation-ai-architecture/">Introducing Pathways: A next-generation AI architecture</a></li>
<li><a href="https://research.google/blog/automl-zero-evolving-code-that-learns/">AutoML - Zero : Evolving Code that Learns</a></li>

</ul>
</details>

**标签**: `#AI research`, `#AI agents`, `#scientific discovery`, `#Google DeepMind`, `#machine learning systems`

---

<a id="item-18"></a>
## [双向扩散模型用往返一致性识别推演误差](https://www.reddit.com/r/MachineLearning/comments/1vh2gn1/roundtrip_consistency_bidirectional_diffusion/) ⭐️ 8.0/10

作者提出了一个单一条件潜在扩散模型，通过方向标记沿时间正向或反向预测动力系统。在测试时，模型先向前推演再向后回推，与起始状态之间的差异被用作原本不可观测的长期推演误差的自监督估计。 自回归生成和预测系统会在多步推演中累积微小误差，而部署环境通常没有真实的未来状态可供质量核验。若该方法有效，这种无需测量的可信度信号可在不依赖集成模型、部署阶段留出数据或控制方程的情况下，识别不可靠的视频生成和科学数字孪生推演。 论文报告称，在一个网络中联合训练正向和反向动力学，在两个方向上都优于两个分别专用的模型。该误差信号需要额外执行一次反向推演，且它是代理指标而非直接的真实误差，因此其可靠性取决于往返不一致性是否能在目标领域和目标时间跨度内持续与实际误差相关。

reddit · r/MachineLearning · /u/Clean-Hovercraft5825 · 8月6日 12:10

**背景**: 扩散模型是一类生成模型，它们学习逆转逐步加入噪声的过程；潜在扩散则在压缩后的表示中执行这一过程，而不是直接处理原始像素或物理场。自回归推演会将模型自身的输出反复作为下一步预测的输入，因此偏差可能不断累积，且不会由观测数据自动纠正。CelebV-HQ 是一个高质量人脸视频数据集，包含 35,666 个视频片段，分辨率至少为 512×512，因此适合用于长期视频生成实验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.00675v1">Round-Trip Consistency: Bidirectional Diffusion Models Can ...</a></li>
<li><a href="https://github.com/alexscheinker/round-trip-consistency">GitHub - alexscheinker/round-trip-consistency: Bidirectional ...</a></li>
<li><a href="https://github.com/CelebV-HQ/CelebV-HQ">GitHub - CelebV-HQ/CelebV-HQ: [ECCV 2022] CelebV-HQ: A Large ...</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#self-supervised learning`, `#time-series forecasting`, `#scientific machine learning`, `#error estimation`

---

<a id="item-19"></a>
## [将重复 LLM 轨迹合成为确定性 NLP 流水线。](https://www.reddit.com/r/MachineLearning/comments/1vhapso/can_recurring_llm_traces_be_synthesized_into/) ⭐️ 8.0/10

一项提案探索以由正则表达式、确定性解析器和传统 ML/NLP 算子组成的类型化 DAG，自动替换重复出现的前沿模型任务。该方案会把重复 LLM 轨迹聚类为工作负载家族，从 41 种原子任务类型中合成候选流水线，在按时间和组别分离的留出集上验证，并将不确定或分布外输入回退给原始模型。 对于边界清晰且重复的抽取工作负载，经验证的确定性或混合流水线有望降低推理成本和延迟，并使行为更易于检查和测试。回退门控是该思路的核心：它为陌生案例保留 LLM 的广泛覆盖能力，而非宣称合成流水线能够在所有场景泛化。 该方案明确指出，生成的图并不是被恢复出的潜在推理轨迹，而是在有限输入分布上被假定与原行为等价的合成程序。主要技术风险包括：仅凭输入输出契约导致的问题不确定性、为每个类型化节点选择合适实现，以及确保不确定性校准确实能识别错误和分布漂移。

reddit · r/MachineLearning · /u/Ok_Philosophy_4031 · 8月6日 17:24

**背景**: LLM 追踪会记录应用中的模型调用及相关执行上下文，因此能够揭示重复出现的输入到输出工作负载模式。在年报示例中，命名实体识别用于找出实体提及，规范化和实体链接则力图在关系抽取生成结构化客户—供应商记录之前，将这些提及统一到一致的实体。DAG，即有向无环图，表示由无循环的有序操作构成的流水线；类型化契约限制一个算子的输出可以如何作为另一个算子的输入。校准衡量模型声明的置信度是否与实际正确率相符，因此分布外门控可以对超出已验证工作域的案例弃答或升级处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://orq.ai/blog/llm-tracing">LLM Tracing Explained: Definition & Best Practices</a></li>
<li><a href="https://www.geeksforgeeks.org/nlp/relationship-extraction-in-nlp/">Relationship Extraction in NLP - GeeksforGeeks</a></li>
<li><a href="https://www.mdpi.com/2504-4990/8/7/179">Calibration, Architecture, and Distribution Shift in ... - MDPI</a></li>

</ul>
</details>

**标签**: `#LLM Systems`, `#NLP Pipelines`, `#Program Synthesis`, `#Uncertainty Estimation`, `#Inference Optimization`

---

<a id="item-20"></a>
## [BESIII 报告迄今最有力的胶球证据。](https://mp.weixin.qq.com/s/pvyNR1lN7QPx3IrpB3WtUg) ⭐️ 8.0/10

BESIII 国际合作组于 8 月 6 日宣布，经过 15 年研究，已为 X(2370)主要由胶子构成建立了完整证据链。该结果建立在 2011 年发现 X(2370)以及 2024 年测得其量子数的基础上，并新增观测到与胶球相符的衰变模式和味单态性质。 若胶球得到确认，将成为对量子色动力学这一描述强相互作用的标准模型理论的重要检验，因为它主要由传递强相互作用的胶子构成，而非由价夸克构成。这一结果有望帮助澄清在量子色动力学微扰方法难以适用的区域中，夸克和胶子如何形成强子。 BESIII 测得 X(2370)的自旋宇称量子数为 J^PC = 0^-+，这与最轻赝标量胶球的理论预期及相应质量范围相符。由于胶子态可能与普通介子发生混合，胶球鉴定在技术上十分困难，因此该宣布依赖多个观测量形成的证据链，而非单一质量峰。

telegram · zaihuapd · 8月6日 07:31

**背景**: 胶子是量子色动力学（QCD）中传递强相互作用的粒子。QCD 预言，胶子本身携带色荷，因此能够在不含价夸克的情况下彼此束缚形成胶球。此类粒子已被寻找数十年，但由于它们可能具有与常规介子相似的量子数并与之混合，实验上很难区分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ihep.ac.cn/xwdt2022/rd/202608/t20260805_8259263.html">BESIII实验首次认证胶球的存在--中国科学院高能物理研究所</a></li>
<li><a href="https://www.nju.edu.cn/info/1067/416761.htm">BESIII实验 X ( 2370 ) 粒 子 成果论文入 选 美国《物理评论快报》 2024...</a></li>
<li><a href="https://baike.baidu.com/item/胶球/4669361">胶球 - 百度百科</a></li>

</ul>
</details>

**标签**: `#particle-physics`, `#quantum-chromodynamics`, `#glueball`, `#BESIII`, `#experimental-physics`

---

<a id="item-21"></a>
## [DeepSeek 以 2080 万美元入股宇树科技上海 IPO](https://www.reuters.com/world/asia-pacific/deepseek-invests-208-million-unitrees-shanghai-ipo-2026-08-06/) ⭐️ 8.0/10

DeepSeek 将以 1.408 亿元人民币（约 2080 万美元）参与宇树科技上海 IPO 战略配售，获得 93.3399 万股，占战略配售股份总数的 2.31%。双方还将共同开发面向人形机器人的 AI 模型，并在相关模型、服务、技术方案和机器人采购方面优先选择对方。 这项投资将重要的 AI 模型开发者与人形机器人制造商连接起来，正值具身智能从实验室研究走向工业应用。双方合作可能加快机器人“大脑”的开发，为 DeepSeek 提供更多物理世界数据，并帮助宇树将先进模型应用到真实机器人中。 合作重点是让人形机器人理解陌生环境并可靠执行指令，而交易所文件规定的是双方的优先选择安排，并非排他性合作。物理世界训练数据具有重要价值，因为单纯的视觉输入无法完整反映抓握打滑、柔性材料和物体操作等真实交互。

telegram · zaihuapd · 8月6日 14:23

**背景**: 具身智能是指通过机器人等物理实体感知环境并采取行动的 AI 系统，而不是只在软件中运行。人形机器人需要将视觉理解、语言指令、运动控制和周围环境反馈连接起来的模型。IPO 是公司首次向公众发行股票，战略配售则是向与公司长期业务目标相关的特定投资者配售股份。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.precedenceresearch.com/insights/embodied-intelligence-ai-humanoid-robots">Embodied Intelligence and AI Humanoid Robots</a></li>
<li><a href="https://www.linkedin.com/posts/shaip_physicalai-robotics-aitraining-activity-7458119902197866496-bsxy">Multimodal AI Training Data for Physical Systems | LinkedIn</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#具身智能`, `#人形机器人`, `#AI模型`, `#战略投资`

---

<a id="item-22"></a>
## [Suno 为 AI 生成歌曲增加防护措施。](https://techcrunch.com/2026/08/06/amid-legal-battles-suno-says-it-will-start-watermarking-songs/) ⭐️ 8.0/10

Suno 表示将为生成歌曲加入音频水印和指纹识别、限制下载，并修订社区准则。该公司还与 Musixmatch 签约使用其 Sentinal 系统进行版权检测，以应对版权诉讼及与数据泄露有关的风险。 这些措施可能提高用户利用 Suno 生成歌曲仿冒他人或通过刷量获利的难度，并为平台和权利人提供更多识别内容的工具。这也反映出主要生成式音乐服务正在应对围绕训练数据和生成内容滥用的法律与治理压力。 Suno 尚未披露计划采用的水印技术，因此目前无法评估其抵抗剪辑、重新编码或移除的能力。水印是在音频中嵌入信息，而音频指纹通过匹配音频特征识别作品，两者可在溯源与检测中发挥互补作用。

telegram · zaihuapd · 8月6日 15:03

**背景**: 音频水印通常用于在音频中嵌入信号或元数据，以便日后核验其来源或使用情况。音频指纹则从录音中提取可识别特征，并与参考素材进行比对，以识别匹配的音频。这些技术与 AI 音乐有关，因为生成歌曲可能被上传到其他服务，平台需要追溯来源或检测可能侵权的内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://icode.best/i/864298414249085">22、数字水印与音频指纹技术在音频识别中的应用-爱代码爱编程</a></li>
<li><a href="https://post.smzdm.com/p/arzw4v87/">AI音乐侵权怎么追责？指纹、水印、溯源三大技术路线全解析</a></li>

</ul>
</details>

**标签**: `#AI音乐`, `#版权治理`, `#生成式AI`, `#内容安全`, `#数据泄露`

---

<a id="item-23"></a>
## [阿里巴巴拟向大型 Qwen 用户收取收入分成。](https://www.reuters.com/business/retail-consumer/alibaba-plans-charge-big-users-its-next-open-source-ai-model-sources-say-2026-08-07/) ⭐️ 8.0/10

Reuters 报道称，阿里巴巴计划在预计于下周发布的新一代开源 Qwen 模型中，要求大型商业用户支付收入分成。此举可能改变此前的模式：用户可在自有数据中心免费部署 Qwen，而阿里巴巴主要对其云平台上的托管使用收费。 即使模型权重仍可获取，收入分成要求也可能提高大型企业和服务商自行部署 Qwen 的成本与合规复杂度。这也表明，中国 AI 公司可能正在转向带有商业限制的开放权重许可，以在与美国 AI 厂商竞争时建立可持续的收入模式。 知情人士称，具体收入分成比例以及“大型用户”的认定门槛尚未最终确定。该方案与月之暗面 Kimi K3 的许可证类似：年收入超过 2000 万美元的服务商必须达成商业协议，据报道分成比例最高可达 30%。

telegram · zaihuapd · 8月7日 01:29

**背景**: 开放权重 AI 模型会提供已训练的模型参数，开发者可以下载后在自己的基础设施上运行，并针对特定用途进行适配。这不同于使用托管 AI API：后者由提供商运营基础设施，通常按使用量收费。开放权重发布仍然可以附带许可证条件，例如针对特定用户的限制或商业条款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/986/830.htm">消息称阿里计划向下一代千问 Qwen ...</a></li>
<li><a href="https://www.infoq.cn/article/jZ394NO5PIZIqNVbN4mD">普通人跑不起 K 3 ！ Kimi 开源，Anthropic... - InfoQ</a></li>
<li><a href="https://linux.do/t/topic/2716860">阿里巴巴计划对 Qwen 开 源 大 模 型 大 用 户 收 费 - 前沿快讯 - LINUX DO</a></li>

</ul>
</details>

**标签**: `#Qwen`, `#开源模型许可`, `#AI 商业模式`, `#阿里巴巴`, `#企业 AI`

---