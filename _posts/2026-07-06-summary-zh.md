---
layout: default
title: "Horizon Summary: 2026-07-06 (ZH)"
date: 2026-07-06
lang: zh
---

> 从 306 条内容中筛选出 26 条重要资讯。

---

1. [Anthropic 发布 Claude Code 智能编码工具](#item-1) ⭐️ 9.0/10
2. [Tree-sitter：用于代码编辑器的增量解析库](#item-2) ⭐️ 9.0/10
3. [长征十号乙 7 月首飞验证全球首创海上网系回收](#item-3) ⭐️ 9.0/10
4. [Project X 不再对抗 GFW，转向俄罗斯和伊朗](#item-4) ⭐️ 9.0/10
5. [F-Droid 称 Google ADV 为恶意软件，预装在 40 亿设备上](#item-5) ⭐️ 9.0/10
6. [免费编译器书籍获社区高度赞扬](#item-6) ⭐️ 8.0/10
7. [Strix：开源 AI 渗透测试工具，自主发现漏洞](#item-7) ⭐️ 8.0/10
8. [Chrome DevTools MCP 让 AI 代理调试浏览器](#item-8) ⭐️ 8.0/10
9. [GitHub 仓库泄露主要 AI 聊天机器人的系统提示词](#item-9) ⭐️ 8.0/10
10. [.NET 代理技能：官方 AI 编码插件](#item-10) ⭐️ 8.0/10
11. [谷歌发布开源 AI 智能体开发工具包 ADK 2.0](#item-11) ⭐️ 8.0/10
12. [Langflow：用可视化工作流构建与部署 AI 智能体](#item-12) ⭐️ 8.0/10
13. [actions/checkout v7：更安全的 fork PR 处理与 ESM 迁移](#item-13) ⭐️ 8.0/10
14. [Omnigraph：支持 Git 工作流的湖仓一体图引擎](#item-14) ⭐️ 8.0/10
15. [Hyperswitch：开源可组合支付平台](#item-15) ⭐️ 8.0/10
16. [OpenAI 发布 Codex CLI：本地编程代理](#item-16) ⭐️ 8.0/10
17. [OCI 镜像格式规范持续维护](#item-17) ⭐️ 8.0/10
18. [Kubernetes MCP 服务器发布，实现 AI 驱动集群管理](#item-18) ⭐️ 8.0/10
19. [AgentsView：面向 AI 编程代理的本地优先分析工具](#item-19) ⭐️ 8.0/10
20. [索尼 2028 年起停售 PS 实体光盘引发强烈反对](#item-20) ⭐️ 8.0/10
21. [HBM 之父：AI 未来是内存中心，而非 GPU 中心](#item-21) ⭐️ 8.0/10
22. [Zero Day Clock 显示黑客 2 小时内利用漏洞](#item-22) ⭐️ 8.0/10
23. [Linux epoll 子系统高危漏洞'Bad Epoll'（CVE-2026-46242）影响 Linux 6.4 以上版本及安卓系统](#item-23) ⭐️ 8.0/10
24. [北京光电子芯片平台投产，降低进口依赖](#item-24) ⭐️ 8.0/10
25. [复旦考试改为人机对战：学生出题考 AI](#item-25) ⭐️ 8.0/10
26. [香港处理中国过半芯片进口，创历史新高](#item-26) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Code 智能编码工具](https://github.com/anthropics/claude-code) ⭐️ 9.0/10

Anthropic 发布了 Claude Code，这是一款在终端中运行的智能编码工具，允许开发者通过自然语言指令与代码库交互，自动完成常规任务、解释复杂代码和管理 Git 工作流。 Claude Code 代表了 AI 辅助软件开发的重要进步，它提供了终端原生的智能体体验，能够自主规划和执行编码任务，有望改变开发者的工作效率和工作流程。 安装方式包括 curl、Homebrew 或 WinGet，npm 安装已弃用。该工具可与终端、IDE 和 GitHub 集成，并包含用于自定义命令的插件系统。

rss · GitHub Trending - Python Daily · 7月5日 01:39

**背景**: 智能编码工具与传统 AI 编码助手不同，它们能够自主规划、编写、测试和修改代码，几乎无需人工干预。Claude 是 Anthropic 开发的一系列大型语言模型，采用宪法 AI 训练以提升伦理合规性。Claude Code 将 Claude 的能力扩展为开发者工具，可以读取代码库并在开发环境中执行命令。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/product/claude-code">Claude Code | Anthropic's agentic coding system \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding assistant`, `#agentic`, `#developer tools`, `#claude`

---

<a id="item-2"></a>
## [Tree-sitter：用于代码编辑器的增量解析库](https://github.com/tree-sitter/tree-sitter) ⭐️ 9.0/10

Tree-sitter 是一个增量解析库和解析器生成器，能够高效地构建和更新具体语法树，从而在编辑器中实现快速且健壮的代码分析。它可以在每次按键时重新解析文件，提供准确的语法高亮和代码导航。 Tree-sitter 是 Neovim 和 GitHub 代码阅读器等现代代码编辑器的基础，实现了响应迅速且准确的语法感知功能。它的增量特性降低了延迟，提高了开发者生产力，使其成为软件工程生态系统中的关键工具。 运行时库采用纯 C 编写且无依赖，可嵌入任何应用程序。Tree-sitter 提供 Rust、WebAssembly 绑定和命令行接口，支持解析多种编程语言。

rss · GitHub Trending - Rust Daily · 7月5日 01:40

**背景**: 增量解析是一种技术，它随着源文本的变化增量更新解析树，而不是从头重新解析。具体语法树（CST）表示源代码的确切语法结构，保留所有细节如括号和空白。传统解析器通常太慢，无法在编辑器中提供实时反馈，但 tree-sitter 的增量方法使其足够快，可以应对每次按键。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tree-sitter/tree-sitter">GitHub - tree-sitter/tree-sitter: An incremental parsing system for programming tools · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Parse_tree">Parse tree - Wikipedia</a></li>
<li><a href="https://tratt.net/laurie/blog/2024/structured_editing_and_incremental_parsing.html">Laurence Tratt: Structured Editing and Incremental Parsing</a></li>

</ul>
</details>

**标签**: `#parsing`, `#compiler`, `#text-editor`, `#syntax-tree`, `#tooling`

---

<a id="item-3"></a>
## [长征十号乙 7 月首飞验证全球首创海上网系回收](https://www.ithome.com/0/972/847.htm) ⭐️ 9.0/10

中国长征十号乙火箭定于 2025 年 7 月 10 日至 13 日期间从文昌商业航天发射场首飞，验证全球首创的“海上网系回收”技术。 若成功，该技术将无需着陆腿即可实现火箭回收，大幅降低发射成本，并为中国载人登月及低轨卫星互联网任务提供关键技术验证。 该火箭采用两级可重复使用设计且无着陆腿；一子级分离后释放挂钩，由 2.5 万吨级 DP 动力定位船“领航者号”上的巨型阻拦网捕获缓冲回收。同时验证 YF-100K 发动机并联和液氧甲烷二级技术。

rss · IT之家 · 7月5日 13:52

**背景**: 可重复使用火箭通常采用着陆腿垂直回收（如 SpaceX 猎鹰 9 号）。中国提出用海上网捕获火箭的方案是全新路径，可省去着陆腿的重量与复杂度。长征十号乙源自载人型长征十号甲，是载人登月技术的验证平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.10jqka.com.cn/20260705/c677957437.shtml">长征十号乙首飞锁定7月10日至7月13...</a></li>
<li><a href="https://en.wikipedia.org/wiki/YF-100">YF-100 - 维基百科，自由的百科全书</a></li>
<li><a href="https://www.thepaper.cn/newsDetail_forward_23350844">我国用于载人登月火箭的 YF-100K 发动机研制取得重大突破_澎湃号·媒体_澎湃新闻-The Paper</a></li>

</ul>
</details>

**标签**: `#space`, `#rocket`, `#reusable launch vehicle`, `#China`, `#aerospace`

---

<a id="item-4"></a>
## [Project X 不再对抗 GFW，转向俄罗斯和伊朗](https://t.me/vps_xhq/814) ⭐️ 9.0/10

Xray-core 的项目团队 Project X 宣布完全停止对抗中国 GFW，将重心转向俄罗斯和伊朗，并禁止在中国大陆内使用。 这一战略转变影响了大量依赖 Xray-core 获取互联网自由的中国用户，并表达了对中国代理生态的不满，可能影响未来翻墙工具的发展方向。 即将推出的 REALITY 服务端将限制客户端最小版本，并阻止“有问题的客户端”TLS 指纹；团队解释变更是为了规避风险以及中国用户捐款稀少。

rss · VPS信号旗播报 - Telegram Channel · 7月5日 14:45

**背景**: Xray-core 是一个开源网络代理平台，是 v2ray-core 的增强版，广泛用于突破网络审查。GFW（中国防火墙）是中国的互联网审查系统。REALITY 是一种将代理流量伪装成普通 TLS 流量的协议，有助于避免检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xtls/xray-core">GitHub - XTLS/Xray-core: Xray, Penetrates Everything. Also the best v2ray-core. Where the magic happens. An open platform for various uses. · GitHub</a></li>
<li><a href="https://objshadow.pages.dev/en/posts/how-reality-works/">How does XTLS REALITY break through the whitelist? REALITY source code analysis - ObjShadow's Blog</a></li>

</ul>
</details>

**标签**: `#Xray-core`, `#Project X`, `#GFW`, `#circumvention`, `#internet censorship`

---

<a id="item-5"></a>
## [F-Droid 称 Google ADV 为恶意软件，预装在 40 亿设备上](https://f-droid.org/2026/07/01/adv-malware.html) ⭐️ 9.0/10

F-Droid 发布博客文章，将 Google 的 Android Developer Verifier (ADV) 定性为恶意软件，称其已预装在约 40 亿台安卓设备上，并将于 9 月 30 日起在部分国家开始拦截未经 Google 批准的软件。 来自主要替代应用商店的这一声明挑战了 Google 对安卓的控制权，可能影响数十亿用户，并凸显了安全措施与软件自由之间的紧张关系。 ADV 是一个拥有 root 权限且无法移除的系统服务，其激活将首先在巴西、印尼、新加坡和泰国进行，全球推广计划于 2027 年完成。包括 EFF 和 FSF 在内的超过 70 个组织已签署公开信反对 ADV。

telegram · zaihuapd · 7月5日 00:41

**背景**: F-Droid 是一个仅提供自由开源软件 (FOSS) 应用的免费开源安卓应用仓库，是 Google Play 的替代品。Google 的 Android Developer Verifier (ADV) 是一个旨在验证开发者身份以减少恶意软件的系统，但批评者认为它赋予了 Google 对应用分发的集中控制权，并可封锁广告拦截器等合法软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://f-droid.org/2026/07/01/adv-malware.html">What We Talk About When We Talk About Malware | F-Droid - Free and Open Source Android App Repository</a></li>
<li><a href="https://techplanet.today/post/android-developer-verification-googles-controversial-security-initiative-and-its-impact-on-app-ecosystem-freedom">Android Developer Verification: Google's Controversial Security Initiative and Its Impact on App Ecosystem Freedom | TechPlanet</a></li>
<li><a href="https://en.wikipedia.org/wiki/F-Droid">F - Droid - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Android`, `#Google`, `#F-Droid`, `#malware`, `#privacy`

---

<a id="item-6"></a>
## [免费编译器书籍获社区高度赞扬](https://dthain.github.io/books/compiler/) ⭐️ 8.0/10

道格拉斯·塞恩博士编写的一本免费且广受好评的编译器和语言设计入门书籍在 Hacker News 上被推荐，获得了 264 个点赞和 44 条评论。 这本书为学习编译器（一个通常被认为困难的课题）提供了易于理解的资源，其积极反响表明它填补了学生和自学者教育材料方面的空白。 该书涵盖编译器构建和语言设计，并通过一个动手项目逐步构建一个可工作的 C 风格编译器，正如一位曾上过该教授课程的学生所提到的。

hackernews · AlexeyBrin · 7月5日 11:54 · [社区讨论](https://news.ycombinator.com/item?id=48793454)

**背景**: 编译器将高级编程语言翻译成计算机可以执行的机器代码。学习编译器设计涉及理解词法分析、解析、代码生成和优化，这是编程语言开发和系统编程的基础。

**社区讨论**: 前学生强烈推荐这本书，称赞讲师和实际项目。一些评论者提到了替代资源，如小型 C4 编译器，而一位批评者指出该书过度关注 C 语言及其特性。其他人则讨论其难度与《龙书》等经典教材的比较。

**标签**: `#compilers`, `#language-design`, `#education`, `#free-book`

---

<a id="item-7"></a>
## [Strix：开源 AI 渗透测试工具，自主发现漏洞](https://github.com/usestrix/strix) ⭐️ 8.0/10

Strix 是一款开源的 AI 驱动渗透测试工具，已在 GitHub 上发布，它通过多代理 AI 黑客自动动态分析代码并生成真实概念验证，实现自主漏洞发现和修复。 Strix 使开发者和小团队能够使用 AI 驱动的渗透测试，从而降低对昂贵人工渗透测试的依赖，并减少静态分析工具常见的误报，这具有重要的行业影响。 Strix 可与 GitHub Actions 和 CI/CD 流水线集成，自动扫描拉取请求并在生产前阻止不安全代码；它采用多代理编排，通过真实概念验证进行实际漏洞验证。

rss · GitHub Trending - Daily · 7月5日 01:33

**背景**: 渗透测试（pentesting）传统上由人类专家手动探测系统漏洞。AI 渗透测试利用机器学习模型自动化部分流程，实现更快、可扩展的安全评估。自主漏洞修复更进一步，不仅能发现缺陷还能自动修复，这正是 Strix 的目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xbow.com/blog/what-is-ai-pentesting">What Is AI Pentesting? A Practical Guide | XBOW</a></li>
<li><a href="https://www.bugcrowd.com/blog/introducing-ai-penetration-testing/">Introducing AI Penetration Testing | @Bugcrowd</a></li>
<li><a href="https://www.atera.com/blog/what-is-autonomous-vulnerability-management/">What is autonomous vulnerability management?</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Penetration Testing`, `#Open Source`, `#Vulnerability Detection`, `#Cybersecurity`

---

<a id="item-8"></a>
## [Chrome DevTools MCP 让 AI 代理调试浏览器](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools 团队发布了 chrome-devtools-mcp 这个 MCP 服务器，允许 AI 编码代理（如 Claude、Cursor）通过 Model Context Protocol 控制和检查实时的 Chrome 浏览器。 该工具将 AI 代理与浏览器 DevTools 连接起来，实现自动调试、性能分析和可靠的 Web 自动化，显著增强了 AI 辅助开发工作流程。 它使用 Puppeteer 进行自动化，并使用 Chrome DevTools 前端进行追踪和性能分析。默认收集使用统计信息，但可通过 --no-usage-statistics 标志选择退出。

rss · GitHub Trending - Daily · 7月5日 01:33

**背景**: Model Context Protocol (MCP) 是 Anthropic 于 2024 年 11 月推出的开放标准，规范了 AI 模型连接外部工具和数据的方式。该协议允许 LLM 使用实时数据并执行超出其训练范围的操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>
<li><a href="https://cloud.google.com/discover/what-is-model-context-protocol">What is Model Context Protocol (MCP)? A guide | Google Cloud</a></li>

</ul>
</details>

**标签**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#debugging`, `#automation`

---

<a id="item-9"></a>
## [GitHub 仓库泄露主要 AI 聊天机器人的系统提示词](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 8.0/10

一个名为 'system_prompts_leaks' 的 GitHub 仓库记录了来自 Claude、ChatGPT、Gemini 和 Grok 等 AI 聊天机器人的泄露系统提示词，并定期更新，包括 Claude Fable 5 和 GPT-5.5 Codex 等最新模型的提示词。 此次泄露揭示了控制 AI 行为的专有系统指令，使研究人员和竞争对手能够分析并可能利用这些规则，引发了重大的 AI 安全和知识产权问题。 该仓库包含来自 Anthropic 的 Claude Opus 4.8、Fable 5 和 Claude Design（含 48 个工具）、OpenAI 的 GPT-5.5 Codex、Google 的 Gemini 3.5 Flash 和 Grok 等的提示词，并被《华盛顿邮报》报道。

rss · GitHub Trending - Daily · 7月5日 01:33

**背景**: 系统提示词是在对话开始前设置模型角色、语气和规则的隐藏的高优先级指令，影响每一次回复。泄露它们是一种提示注入攻击，攻击者诱使模型暴露自身的指令，可能泄露敏感的操作指南。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learnprompting.org/docs/prompt_hacking/leaking">Prompt Leaking : Understanding Risks in GenAI Models</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/">LLM07:2025 System Prompt Leakage - OWASP Gen AI Security ...</a></li>
<li><a href="https://multiple.chat/ai-glossary/system-prompt">System Prompt — Definition | MultipleChat AI Glossary</a></li>

</ul>
</details>

**标签**: `#system prompts`, `#AI security`, `#prompt leak`, `#GPT`, `#Claude`

---

<a id="item-10"></a>
## [.NET 代理技能：官方 AI 编码插件](https://github.com/dotnet/skills) ⭐️ 8.0/10

微软 .NET 团队发布了官方 dotnet/skills 仓库，提供精选的插件和技能，帮助 AI 编码助手进行 .NET 和 C# 开发。 该仓库通过提供专家精心制作的可复用技能，标准化了 AI 辅助的 .NET 开发，有望提升整个 .NET 生态系统的开发效率和代码质量。 该仓库包含 12 个插件，涵盖语言服务器集成、MSBuild、NuGet、测试、升级、MAUI、AI/ML 等领域，全部遵循 Agent Skills 开放标准。

rss · GitHub Trending - Daily · 7月5日 01:33

**背景**: Agent Skills 是一种可移植、版本控制的标准，用于将 AI 代理的能力（指令、行为和工具使用）打包成可复用的工件。该标准允许技能在不同的 AI 代理和平台之间共享和使用，增强一致性和领域专业知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://github.com/HoangNguyen0403/agent-skills-standard">GitHub - HoangNguyen0403/agent-skills-standard: A collection of Agent Skills Standard and Best Practice for Programming Languages, Frameworks that help our AI Agent follow best practies on frameworks and programming laguages · GitHub</a></li>
<li><a href="https://www.f5.com/company/blog/agent-skills-an-emerging-open-standard">Agent skills: An emerging open standard | F5</a></li>

</ul>
</details>

**标签**: `#.NET`, `#C#`, `#AI coding agents`, `#agent skills`

---

<a id="item-11"></a>
## [谷歌发布开源 AI 智能体开发工具包 ADK 2.0](https://github.com/google/adk-python) ⭐️ 8.0/10

谷歌开源了智能体开发工具包（ADK）2.0 版，这是一个代码优先的 Python 框架，用于构建、评估和部署 AI 智能体。新版本引入了基于图的执行引擎 Workflow Runtime，以及用于结构化智能体间任务委托的 Task API。 作为谷歌的官方发布，ADK 可能成为 AI 智能体开发的标准工具，类似于 LangChain 或 AutoGen，但与谷歌的 Gemini 模型集成更深。其开源性质允许社区贡献并在生态系统中广泛采用。 ADK 2.0 包含从 1.x 版本的重大变更，特别是在智能体 API、事件模型和会话架构方面；2.0 的会话可以被 ADK 1.28+读取，但不兼容更旧的版本。该框架需要 Python 3.10+，可通过 pip install google-adk 安装，并提供可选扩展。

rss · GitHub Trending - Python Daily · 7月5日 01:39

**背景**: 智能体开发工具包（ADK）是谷歌推出的开源 Python 框架，用于构建能够自主执行任务或在工作流中运行的 AI 智能体。它采用代码优先的方式，允许开发者使用 Python 脚本定义智能体和工作流。该工具包支持与谷歌的 Gemini 模型集成，并提供评估和部署工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pankaj-rai.medium.com/adk-series-1-create-your-first-ai-agent-with-google-adk-bcd252b926a5">ADK Series 1: Create your first AI Agent with Google ADK | Medium</a></li>
<li><a href="https://compute.anshaj.dev/p/google-agent-development-kit">Google Agent Development Kit - by Anshaj</a></li>
<li><a href="https://mozilla-ai.github.io/any-agent/agents/frameworks/google-adk/">Google Agent Development Kit ( ADK ) | any- agent</a></li>

</ul>
</details>

**标签**: `#AI`, `#Python`, `#open-source`, `#agent development`, `#Google`

---

<a id="item-12"></a>
## [Langflow：用可视化工作流构建与部署 AI 智能体](https://github.com/langflow-ai/langflow) ⭐️ 8.0/10

Langflow 作为一个流行的 GitHub 仓库，提供了强大的可视化平台，用于构建和部署 AI 驱动的智能体与工作流，支持所有主流大语言模型和向量数据库。 该工具通过提供可视化界面和内置 API/MCP 服务器，使 AI 智能体开发更加普及，开发者无需大量编码即可将 AI 工作流集成到任何应用中。 Langflow 具有可视化构建器、交互式游乐场、多智能体编排，以及作为 API 或 MCP 服务器部署的选项，并提供 LangSmith 和 LangFuse 等可观测性集成。

rss · GitHub Trending - Python Daily · 7月5日 01:39

**背景**: Langflow 是一个开源 Python 工具，旨在简化 AI 智能体与工作流的创建。它提供拖放式界面，用于连接大语言模型、向量存储和工具，使初学者和资深开发者都能轻松使用。

**标签**: `#AI`, `#workflow`, `#agents`, `#open-source`, `#Python`

---

<a id="item-13"></a>
## [actions/checkout v7：更安全的 fork PR 处理与 ESM 迁移](https://github.com/actions/checkout) ⭐️ 8.0/10

Checkout v7 引入了更安全的 fork 拉取请求处理，默认拒绝在通过 pull_request_target 或 workflow_run 触发时检出 fork 代码，并将 action 迁移至 ESM。 此更新显著降低了 CI/CD 流水线中 'pwn request' 漏洞的风险，保护了仓库的密钥和令牌。ESM 迁移确保与更新的 @actions/* 包兼容。 如需在评估风险后选择之前的行为，用户必须设置新的输入参数 `allow-unsafe-pr-checkout: true`。此更新还包括依赖项更新和安全性修复。

rss · GitHub Trending - TypeScript Daily · 7月5日 01:41

**背景**: Pwn request 漏洞发生在由 pull_request_target 或 workflow_run 触发的工作流检出并执行来自 fork 仓库的代码时，从而使攻击者能够访问密钥和令牌。actions/checkout 是 GitHub Actions 工作流中检出仓库的标准操作。默认情况下，它只获取触发 ref 的单个提交。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.endorlabs.com/learn/pwn-request-threat-a-hidden-danger-in-github-actions">PWN Request Threat: A Hidden Danger in GitHub Actions | Blog | Endor Labs</a></li>
<li><a href="https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/">Keeping your GitHub Actions and workflows secure Part 1: Preventing...</a></li>
<li><a href="https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target">Securely using pull_request_target - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#GitHub Actions`, `#security`, `#CI/CD`, `#TypeScript`

---

<a id="item-14"></a>
## [Omnigraph：支持 Git 工作流的湖仓一体图引擎](https://github.com/ModernRelay/omnigraph) ⭐️ 8.0/10

ModernRelay 发布了 Omnigraph，这是一个开源图引擎，将湖仓一体架构、类 Git 分支和多智能体协调相结合，用于上下文组装。 Omnigraph 结合了图数据库、湖仓一体存储和版本控制工作流，使智能体能够安全地在共享图上协作，这可能彻底改变知识管理和智能体 AI 系统。 Omnigraph 使用 Lance 列式格式实现可版本控制和时间旅行存储，支持通过图遍历、向量 ANN 和全文搜索进行多模态检索，并在每次变更时强制执行 Cedar 策略。

rss · GitHub Trending - Rust Daily · 7月5日 01:40

**背景**: 湖仓一体是一种结合数据湖灵活性和数据仓库可靠性的数据架构。图数据库将关系存储为节点和边。类 Git 分支允许在隔离的副本上并行工作，然后合并。多智能体协调涉及多个 AI 智能体在共享任务上协同工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.cambridgesemantics.com/graphlakehouse/v3.2/userdoc/features.htm">Graph Lakehouse Features and Benefits</a></li>
<li><a href="https://github.com/topics/branching">branching · GitHub Topics · GitHub</a></li>
<li><a href="https://blaxel.ai/blog/agentic-ai-architecture-explained">How Agentic AI Architecture Works in Production | Blaxel Blog</a></li>

</ul>
</details>

**标签**: `#Rust`, `#graph-database`, `#lakehouse`, `#multi-agent`, `#git-workflow`

---

<a id="item-15"></a>
## [Hyperswitch：开源可组合支付平台](https://github.com/juspay/hyperswitch) ⭐️ 8.0/10

Juspay 发布了 Hyperswitch，这是一个开源、可组合的支付平台，符合 PCI 标准，并通过智能路由支持多个支付提供商。 该平台为企业提供了对其支付栈的灵活性和控制力，通过智能路由和成本可观察性减少了供应商锁定并可能降低成本。 Hyperswitch 使用 Rust 构建，提供 SaaS 和自托管选项，包括收入恢复和对账等功能，以减少支付运营开销。

rss · GitHub Trending - Rust Daily · 7月5日 01:40

**背景**: 可组合支付平台允许企业仅集成所需的支付模块，如路由、欺诈检测或令牌化，避免使用单体系统。智能路由使用机器学习根据成本、成功率等因素为每笔交易选择最佳支付网关。收入恢复功能自动重试失败的支付，以减少非自愿流失。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hellgate.io/">Composable Payment Orchestration Platform | Hellgate</a></li>
<li><a href="https://www.ranktracker.com/blog/intelligent-payment-routing-ai/">Intelligent Payment Routing : How AI Picks the Best Path</a></li>
<li><a href="https://rekovery.ai/">ReKovery — AI-powered payment retry & revenue recovery</a></li>

</ul>
</details>

**标签**: `#payments`, `#open-source`, `#fintech`, `#routing`, `#PCI compliance`

---

<a id="item-16"></a>
## [OpenAI 发布 Codex CLI：本地编程代理](https://github.com/openai/codex) ⭐️ 8.0/10

OpenAI 发布了 Codex CLI，这是一个在终端本地运行的轻量级编程代理，以 Apache-2.0 许可证开源。它能在选定目录中直接在用户机器上读取、修改和运行代码。 这为开发者提供了一个免费（需订阅 ChatGPT）的本地 AI 编程助手，相比云端方案能提升生产力和隐私性。这标志着 OpenAI 进入了竞争激烈的本地编程代理领域，可能重塑开发者工作流程。 Codex CLI 可通过 curl、PowerShell、npm 或 Homebrew 安装，需要 ChatGPT Plus/Pro/Business/Edu/Enterprise 订阅或 API 密钥。它不同于早期的 Codex 模型和云端 Codex Web。

rss · GitHub Trending - Rust Daily · 7月5日 01:40

**背景**: OpenAI Codex 最初指 2021 年针对代码微调的大型语言模型，为 GitHub Copilot 提供支持。Codex CLI 是独立的新产品，通过命令行界面本地运行，提供比 IDE 集成编程代理更轻量的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenAI_Codex_(language_model)">OpenAI Codex (language model)</a></li>
<li><a href="https://developers.openai.com/codex/cli">CLI – Codex | OpenAI Developers</a></li>

</ul>
</details>

**标签**: `#AI`, `#coding agent`, `#OpenAI`, `#CLI`, `#developer tools`

---

<a id="item-17"></a>
## [OCI 镜像格式规范持续维护](https://github.com/opencontainers/image-spec) ⭐️ 8.0/10

opencontainers/image-spec 仓库持续维护 OCI 镜像格式规范，为容器镜像标准化提供 Go 类型和验证工具。 OCI 镜像格式是一项基础标准，使 Docker 和 rkt 等容器工具之间实现互操作性，确保容器镜像在不同环境中能够一致地构建、分发和运行。 该规范定义了由清单、索引（可选）、文件系统层和配置组成的镜像。该仓库还包含 Go 类型、blob 内验证工具和 JSON Schema。

rss · GitHub Trending - Go Daily · 7月5日 01:36

**背景**: 开放容器倡议（OCI）是一个 Linux 基金会项目，由 Docker、CoreOS 等公司于 2015 年创立，旨在为容器格式和运行时创建开放标准。OCI 镜像格式规范于 2016 年从运行时规范中分离出来，并于 2017 年 7 月达到 1.0.0 版本。它与 OCI 运行时规范和 OCI 分发规范协同工作，支持容器的完整生命周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open_Container_Initiative">Open Container Initiative - Wikipedia</a></li>
<li><a href="https://opencontainers.org/">Open Container Initiative - Open Container Initiative</a></li>
<li><a href="https://github.com/opencontainers/image-spec">GitHub - opencontainers/ image - spec : OCI Image Format · GitHub</a></li>

</ul>
</details>

**标签**: `#container`, `#image-spec`, `#OCI`, `#standard`, `#container-runtime`

---

<a id="item-18"></a>
## [Kubernetes MCP 服务器发布，实现 AI 驱动集群管理](https://github.com/containers/kubernetes-mcp-server) ⭐️ 8.0/10

containers 组织发布了一个开源的 Kubernetes 和 OpenShift 模型上下文协议（MCP）服务器，使 AI 助手能够通过自然语言直接对任意资源执行 CRUD 操作、管理 Pod、查看事件以及安装 Helm Chart。 这一集成将 AI 助手与 Kubernetes 操作连接起来，允许开发者和运维人员通过对话管理集群，减少手动 kubectl 命令，加速 DevOps 工作流。这是迈向 AI 原生基础设施管理的实际一步。 该服务器支持集群内和 kubeconfig 两种认证方式，自动检测配置变化，并提供 Pod 特定的操作如 exec、logs、top 和 run。它通过 npm 和 PyPI 分发，可与任何兼容 MCP 的 AI 客户端配合使用。

rss · GitHub Trending - Go Daily · 7月5日 01:36

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，旨在使 LLM 能够与外部工具和数据源连接。Kubernetes 是流行的容器编排平台，OpenShift 是 Red Hat 的企业级 Kubernetes 发行版。该服务器允许 AI 模型通过 MCP 协议与 Kubernetes 集群交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**标签**: `#Kubernetes`, `#MCP`, `#AI`, `#OpenShift`, `#DevOps`

---

<a id="item-19"></a>
## [AgentsView：面向 AI 编程代理的本地优先分析工具](https://github.com/kenn-io/agentsview) ⭐️ 8.0/10

AgentsView 是一个新的开源工具，为包括 Claude Code 和 OpenAI Codex 在内的 20 多种 AI 编程代理提供本地优先的会话搜索、分析和令牌使用追踪。 随着开发者越来越多地依赖 AI 编程代理，跟踪成本和理解使用模式变得至关重要。AgentsView 通过提供保护隐私、支持离线的分析仪表板来填补这一空白，无需云账户。 它以一个二进制文件运行，数据存储在本地 SQLite 中，并在 localhost 上提供 Web UI。它支持 S3 兼容存储以实现集中式会话聚合，并包含用于每日成本摘要的 CLI 工具。

rss · GitHub Trending - Go Daily · 7月5日 01:36

**背景**: 本地优先软件将数据主要存储在用户设备上，支持离线访问并保护隐私。Claude Code 是 Anthropic 的 AI 编程代理，在终端中运行；OpenAI Codex 是用于代码生成的 AI 助手。AgentsView 汇总这些代理的事务日志，帮助开发者监控令牌使用情况和费用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Local-first_software">Local-first software</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://chatgpt.com/ru-RU/codex/">Codex | AI Assistant for Work and Code</a></li>

</ul>
</details>

**标签**: `#tools`, `#AI agents`, `#analytics`, `#developer tools`, `#cost tracking`

---

<a id="item-20"></a>
## [索尼 2028 年起停售 PS 实体光盘引发强烈反对](https://www.ithome.com/0/972/877.htm) ⭐️ 8.0/10

索尼宣布从 2028 年 1 月起，所有新款 PlayStation 游戏将仅以数字下载形式发行，停止生产实体光盘。这一决定在 Change.org 上引发请愿，短短四天内获得超过十万个签名。 此举标志着游戏行业向全数字化的重大转型，引发了对游戏所有权、消费者权益和市场垄断的担忧。它影响了数百万珍视拥有、交易和转售实体游戏能力的玩家。 这份名为“不要抹杀实体光盘”的请愿由加拿大游戏零售商 PnP Games 的代表发起。请愿指出，实体光盘代表真正的所有权，而数字版本仅是可被撤销的授权，并引用了玩家库中被删除内容的先例。

rss · IT之家 · 7月5日 23:53

**背景**: 实体游戏光盘是传统主机游戏的媒介，允许玩家拥有、借出、转卖或赠送副本。数字发行虽然便利，但通常仅授予游玩授权，平台持有者可以撤销该授权。索尼在 2013 年承诺玩家可以永久保留所购游戏，如今被认为已食言。

**社区讨论**: 玩家普遍反对这一决定，近 5%的请愿支持者留下了文字评论或视频声援。常见论据包括失去所有权、对数字垄断的担忧，以及实体供应链就业岗位的影响。一些批评者指出，请愿可能无法改变索尼的计划，因为该决定可能早已规划好。

**标签**: `#游戏产业`, `#数字版权`, `#索尼`, `#实体光盘`, `#玩家权益`

---

<a id="item-21"></a>
## [HBM 之父：AI 未来是内存中心，而非 GPU 中心](https://www.ithome.com/0/972/872.htm) ⭐️ 8.0/10

被誉为“HBM 之父”的韩国科学技术院教授金正浩在采访中表示，AI 的核心竞争力正从 GPU 转向内存。他预测 HBF（高带宽闪存）将在 10 年内超过 HBM 的需求，更长远来看 HBS（高带宽 SRAM）将成为主流，并设想了一种 100 层 3D 复合架构的 AI 计算机。 这标志着 AI 硬件设计的范式转变：随着 AI 从训练转向推理，内存带宽和容量成为瓶颈。如果金正浩的预测成立，内存行业可能会迎来超越 HBM 的新一波创新，可能重塑 AI 加速器和数据中心的竞争格局。 金正浩指出，即使部署 100 万块 GPU，由于数据在 HBM 和 GPU 之间的搬运，实际计算时间只占 10%-30%。他提出未来的 AI 计算机会将 HBM、HBF（基于 NAND 闪存）和 HBS（基于 SRAM）堆叠成约 100 层的 3D 架构，其中 HBF 用于存储视频、文档和代理式 AI 的长期冷数据。

rss · IT之家 · 7月5日 23:22

**背景**: HBM（高带宽内存）是一种 3D 堆叠 DRAM 技术，广泛用于 AI GPU 加速器，通过垂直互连提供高带宽。HBF（高带宽闪存）是 SK 海力士和 SanDisk 提出的较新概念，垂直堆叠 NAND 闪存以实现高容量和带宽，专门用于 AI 推理工作负载。HBS（高带宽 SRAM）是一种更超前的技术，使用比 DRAM 快 1000 倍的 SRAM，在 12 英寸晶圆上堆叠以实现巨大容量。代理式 AI（Agentic AI）是指能够以最少人工干预自主执行任务的 AI 系统，需要持久化内存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.indexbox.io/blog/sk-hynix-hbf-high-bandwidth-flash-for-ai-inference-in-2026/">SK Hynix HBF : High - Bandwidth Flash AI Memory... - IndexBox</a></li>
<li><a href="https://www.oscoo.com/news/sk-hynix-and-sandisk-unveil-high-bandwidth-flash-for-ai-inference/">SK Hynix and SanDisk Unveil High Bandwidth Flash for AI... - OSCOO</a></li>
<li><a href="https://www.kad8.com/ai/hbf-the-next-memory-layer-for-ai-accelerators/">HBF : The Next Memory Layer for AI Accelerators · KAD</a></li>

</ul>
</details>

**标签**: `#HBM`, `#AI hardware`, `#memory-centric computing`, `#HBF`, `#HBS`

---

<a id="item-22"></a>
## [Zero Day Clock 显示黑客 2 小时内利用漏洞](https://www.ithome.com/0/972/862.htm) ⭐️ 8.0/10

由 Sysdig 首席信息安全官 Sergej Epp 发起的 Zero Day Clock 项目显示，截至 2026 年 7 月，漏洞从公开披露到首次被利用的平均时间（TTE）已降至不足 2 小时，而 2025 年这一数据为 21.5 天。 防御窗口的急剧压缩迫使企业从根本上重新审视其漏洞响应和补丁管理策略，传统的数天补丁周期已不再可行。 Zero Day Clock 整合了超过 3500 起真实漏洞利用事件的数据，数据来源包括 CISA 的已知被利用漏洞目录（KEV）和 VulnCheck。该指标追踪从漏洞公开披露到首次在野外被观测到利用的时间。

rss · IT之家 · 7月5日 14:52

**背景**: 时间到利用（TTE）衡量漏洞公开披露到被攻击者利用之间的时间差。历史上这一窗口可能长达数月甚至数年，但自动化和 AI 驱动的漏洞利用开发已大幅缩短了这一时间。CISA 的 KEV 目录收录了已知被积极利用的漏洞，是优先修复的重要依据。VulnCheck 提供漏洞利用情报，帮助组织聚焦最关键威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zerodayclock.com/">Zero Day Clock</a></li>
<li><a href="https://www.cisa.gov/resources-tools/resources/known-exploited-vulnerabilities-catalog">Known Exploited Vulnerabilities Catalog | CISA</a></li>
<li><a href="https://www.vulncheck.com/">VulnCheck - Outpace Adversaries</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#vulnerability management`, `#exploit speed`, `#threat intelligence`, `#patch management`

---

<a id="item-23"></a>
## [Linux epoll 子系统高危漏洞'Bad Epoll'（CVE-2026-46242）影响 Linux 6.4 以上版本及安卓系统](https://www.ithome.com/0/972/861.htm) ⭐️ 8.0/10

该漏洞影响 Linux 6.4 及以上版本以及使用 6.6 及以上内核的安卓设备（包括 Pixel 10）。由于 epoll 是内核核心机制，无法轻易禁用，唯一的可靠防护是更新补丁内核，因此及时更新对安全至关重要。 该漏洞是 epoll 子系统中的竞争条件导致的释放后重用（UAF）漏洞，可使拥有普通用户权限的攻击者获得 root 权限。使用 Linux 6.1 内核的系统不受影响，因为漏洞是在 6.4 版本中引入的。

rss · IT之家 · 7月5日 14:44

**背景**: epoll 是 Linux 内核子系统，用于高效监控多个文件描述符的 I/O 事件，广泛应用于高性能网络服务器。释放后重用（UAF）漏洞是指程序在释放内存后仍继续访问该内存，可能导致代码执行或权限提升。该漏洞利用了 epoll 在内部处理文件描述符时的竞争条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/torvalds/linux/blob/master/fs/eventpoll.c">linux/fs/eventpoll.c at master - GitHub</a></li>
<li><a href="https://cqr.company/web-vulnerabilities/use-after-free-vulnerability/">Use - After - Free vulnerability | CQR</a></li>

</ul>
</details>

**标签**: `#Linux kernel`, `#epoll`, `#vulnerability`, `#local privilege escalation`, `#CVE-2026-46242`

---

<a id="item-24"></a>
## [北京光电子芯片平台投产，降低进口依赖](https://www.ithome.com/0/972/810.htm) ⭐️ 8.0/10

2025 年 7 月 5 日，北京信息光电子芯片平台在北京经开区正式通线投产，建成一条高速光芯片专用量产线，以降低对外进口依赖。 这一里程碑直接填补了中国在 AI 数据中心、光电共封装、卫星光通信等领域所需高速光芯片的供应链关键短板，有望提升国内自主供应能力和产业安全。 该平台由华毅瀛飞运营，已完成近 2 亿元 Pre-A 轮融资，可量产大功率分布反馈激光器、高速电吸收调制激光器、薄膜铌酸锂调制器、单行载流子光电探测器等核心器件，性能对标国际一线水平。

rss · IT之家 · 7月5日 09:48

**背景**: 高速光芯片是 AI 和数据中心中数据传输的核心器件。长期以来，中国严重依赖进口，存在供应链脆弱性。该平台集研发、中试、量产于一体，实现了这些关键器件的本土化制造。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://post.smzdm.com/p/ad7vpz7p/">功耗直降68%！ 这项 光 通信 封 革命让博通英伟达集体押注，2026...</a></li>
<li><a href="https://www.ipanqiao.com/entry/168">ipanqiao.com/entry/168</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#photonics`, `#AI infrastructure`, `#supply chain`, `#optics`

---

<a id="item-25"></a>
## [复旦考试改为人机对战：学生出题考 AI](https://www.ithome.com/0/972/809.htm) ⭐️ 8.0/10

复旦大学《数据挖掘技术》课程将传统期末考试改为全新形式：51 名学生每人设计 10 道计算题，用来考验三个 AI 模型（DeepSeek V4-Flash、MiniMax M2.7、Claude Sonnet 4.6），AI 答错越多，学生得分越高。 这一教学创新颠覆了利用 AI 作弊的传统思路，要求学生深入理解知识以找出 AI 的盲区，可能重塑人工智能时代批判性思维的评估方式。 51 名学生中仅 4 人成功让某个 AI 模型在 10 道题上得零分，最强的 Claude Sonnet 4.6 没有被任何学生完全难倒；评分公式为 60 分保底加 AI 错误奖励分（每题 1.5 至 3 分），上限 100 分。

rss · IT之家 · 7月5日 09:42

**背景**: 传统的数据挖掘考试已经过时，因为 AI 比学生更快更准确地解决标准算法题。肖仰华教授设计这种“人机对战”形式以鼓励深度理解：学生必须找出 AI 推理失败的地方，这需要掌握底层概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash - Hugging Face</a></li>
<li><a href="https://platform.minimax.io/">Overview of MiniMax AI models and their capabilities</a></li>
<li><a href="https://www.anthropic.com/news/claude-sonnet-4-6">Introducing Sonnet 4 . 6 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#education`, `#pedagogy`, `#critical thinking`, `#Fudan University`

---

<a id="item-26"></a>
## [香港处理中国过半芯片进口，创历史新高](https://thenextweb.com/news/hong-kong-china-ai-chip-trade-hub) ⭐️ 8.0/10

2026 年前五个月，香港经手了中国逾半数的芯片进口，转口至内地的芯片价值约 1240 亿美元，占中国同期芯片采购总额的 52%，创下历史新高。 这一里程碑巩固了香港作为人工智能半导体贸易关键枢纽的地位，对全球供应链和地缘政治具有影响，目前人工智能相关电子产品已占其出口的 57%至 70%。 香港凭借自由港地位、无关税、无资本管制以及发达的航空货运网络，在半导体高价值、低重量、时效性强的贸易中占据优势，但其中间人角色也使其面临中美关系紧张带来的地缘政治风险。

telegram · zaihuapd · 7月5日 02:45

**背景**: 半导体是电子产品和人工智能的关键组件，中国是主要进口国。由于独特的贸易政策，香港长期以来一直是转口枢纽。人工智能需求的激增放大了香港的作用，香港贸发局因此将 2026 年出口增长预测上调至逾 20%。

**标签**: `#semiconductors`, `#Hong Kong`, `#AI trade`, `#chip imports`, `#geopolitics`

---