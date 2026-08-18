---
layout: default
title: "Horizon Summary: 2026-08-18 (EN)"
date: 2026-08-18
lang: en
---

> From 278 items, 12 important content pieces were selected

---

**Technology News**
1. [Mojo Compiler and Toolchain Open Sourced](#item-tech-news-1) ⭐️ 8.0/10
2. [GitLab Patches Critical GraphQL Vulnerabilities](#item-tech-news-2) ⭐️ 8.0/10
3. [Linux 7.3 VRAM Pressure Improvement](#item-tech-news-3) ⭐️ 7.0/10
4. [Qwen 3.8 27B Reaches Benchmark Score 52](#item-tech-news-4) ⭐️ 7.0/10
5. [Anthropic Releases Claude Security Reference Harness](#item-tech-news-5) ⭐️ 7.0/10
6. [Needle 2 for Tiny Devices](#item-tech-news-6) ⭐️ 7.0/10
7. [FFF Targets Fast Repeated File Search](#item-tech-news-7) ⭐️ 7.0/10
8. [Apple Revises EU App Store Terms](#item-tech-news-8) ⭐️ 7.0/10
9. [Gas Plants for Data Centers Raise Emissions Concerns](#item-tech-news-9) ⭐️ 7.0/10
10. [Apple Says App Store Rules Are Hurting Services](#item-tech-news-10) ⭐️ 7.0/10
11. [WeCom 5.0.10 Opens CLI and MCP Access](#item-tech-news-11) ⭐️ 7.0/10

**Financial News**
1. [Jeanie Buss Opposes Lakers Stake Sale](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Mojo Compiler and Toolchain Open Sourced](https://simonwillison.net/2026/Aug/18/mojo-is-now-open-source/) ⭐️ 8.0/10

Mojo has released its compiler and toolchain as open source under the Apache 2 license, following its 1.0 release the previous week. Simon Willison notes that this fulfills a promise dating back to Mojo&\#x27;s May 2023 launch. The language was originally presented as a planned superset of Python, but Modular&\#x27;s direction changed around August 2025, with project guidance saying Mojo may or may not become fully Python-compatible. Mojo is now positioned as its own Python-inspired language focused on making GPU programming easier, rather than as a language guaranteed to run existing Python code unchanged.

rss · Simon Willison · Aug 18, 21:39

**「Background」** Mojo is a systems programming language developed by Modular with Python-like syntax and features aimed at high-performance workloads, including static typing and ownership concepts associated with systems languages. It was originally presented as Python-adjacent and potentially compatible with existing Python code, but the source item says its current direction is as a separate language optimized for GPU programming rather than a guaranteed full Python superset.

**「Impact」** Developers interested in Mojo can now inspect, use, and build on its compiler and toolchain under Apache 2, while accounting for its limited and evolving Python compatibility.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo ( programming language ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#programming-languages`, `#open-source`, `#AI-infrastructure`, `#Python`, `#compiler-toolchains`

---

<a id="item-tech-news-2"></a>
### [GitLab Patches Critical GraphQL Vulnerabilities](https://www.ithome.com/0/991/362.htm) ⭐️ 8.0/10

GitLab released emergency security updates on August 17, 2026 for two vulnerabilities in GitLab Community Edition and Enterprise Edition. The critical flaw, CVE-2026-19478 with a CVSS score of 9.4, reportedly lets unauthenticated attackers remotely modify or permanently delete public project and user data through a GraphQL fallback field resolution defect involving the @gl\_introduced directive. The second issue, CVE-2026-19650 with a CVSS score of 7.1, is a CSRF vulnerability in the GraphQL multiplex query processor that can allow GraphQL mutation operations through GET requests under specific conditions and requires user interaction. Both vulnerabilities affect GitLab CE/EE versions from 18.2 up to before 18.11.11, 19.0 up to before 19.0.8, 19.1 up to before 19.1.6, and 19.2 up to before 19.2.4, with fixes released in 18.11.11, 19.0.8, 19.1.6, and 19.2.4. GitLab said the update includes no new database migrations, multi-node deployments do not need downtime, both reports came through HackerOne, and it has not seen evidence of in-the-wild exploitation.

rss · IT之家 · Aug 18, 15:52

**「Background」** GitLab CE and EE are the community and enterprise editions of GitLab, and security patch releases apply especially to self-managed installations that operators maintain themselves. GraphQL APIs use queries to read data and mutations to change data, so flaws in directive handling, request validation, or CSRF protections can turn a single crafted request into an unauthorized state-changing action.

**「Impact」** Self-hosted GitLab operators running affected CE/EE versions should upgrade immediately to 18.11.11, 19.0.8, 19.1.6, or 19.2.4 because public technical details and a PoC are reportedly already available.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/">GitLab Critical Patch Release: 19.2.4, 19.1.6, 19.0.8, 18.11.11</a></li>
<li><a href="https://nvd.nist.gov/vuln/detail/CVE-2026-19650">NVD - CVE-2026-19650</a></li>

</ul>
</details>

**Tags**: `#security`, `#GitLab`, `#vulnerability`, `#GraphQL`, `#DevOps`

---

<a id="item-tech-news-3"></a>
### [Linux 7.3 VRAM Pressure Improvement](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 7.0/10

The linked article discusses a Linux 7.3 change intended to improve behavior and performance when GPU VRAM is exhausted. The improvement is about GPU memory pressure and overcommit handling, where data may need to move or be reclaimed when workloads exceed available VRAM. This matters for graphics, gaming, and GPU compute workloads because running out of VRAM can otherwise cause severe slowdowns or poor responsiveness. The supplied item does not include the article text, so specific implementation details, benchmark numbers, affected drivers, and upstream status cannot be verified here.

hackernews · flaburgan · Aug 18, 07:51 · [Discussion](https://news.ycombinator.com/item?id=49342719)

**「Background」** VRAM is a GPU’s dedicated memory, used for textures, buffers, model data, and other graphics or compute workloads; when allocations exceed physical VRAM, drivers may page data between VRAM and system memory. The source article frames VRAM overcommit as something that should primarily affect performance rather than stability, because GPU drivers have long supported overcommitting VRAM in principle.

**「Impact」** Users running GPU workloads that exceed available VRAM may see better performance or responsiveness once the relevant Linux 7.3 change is available in their kernel and supported driver stack.

**「Community」** Commenters broadly welcomed the improvement and praised the article, while raising practical questions about driver support, especially Nvidia, and whether applications should provide stronger hints to the kernel about which allocations should remain in VRAM. Some discussion also connected the issue to broader memory-pressure behavior, including system freezes when ordinary RAM is exhausted.

<details><summary>References</summary>
<ul>
<li><a href="https://pixelcluster.dev/VRAM-Overcommit/">VRAM Management Part 2: Beyond the... | pixelcluster &#x27;s GPU blog</a></li>

</ul>
</details>

**Tags**: `#linux kernel`, `#GPU memory`, `#performance`, `#memory management`, `#hardware`

---

<a id="item-tech-news-4"></a>
### [Qwen 3.8 27B Reaches Benchmark Score 52](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 7.0/10

Simon Willison highlighted that Qwen 3.8 27B reportedly scored 52 on the Artificial Analysis Intelligence Index. The score matches GPT-5.6 Luna \(max\) and is one point behind GLM-5.2 \(max\) and DeepSeek V4 Pro 0813 \(max\), according to the source item. Willison notes the comparison is notable because GLM-5.2 is listed as 753B parameters, DeepSeek V4 Pro 0813 as 1.7T parameters, and Luna’s size is unknown but presumed much larger than 27B. The item is brief and benchmark-focused, so it does not provide additional technical details about evaluation conditions, architecture, licensing, or independent validation.

rss · Simon Willison · Aug 17, 23:58

**「Background」** Qwen is a family of large language models associated with Alibaba’s AI work, and parameter count is commonly used as a rough indicator of model scale. The Artificial Analysis Intelligence Index is a benchmark aggregation used to compare model performance, but benchmark scores should be interpreted alongside methodology, task mix, inference settings, and real-world workload results.

**「Impact」** AI practitioners evaluating open or smaller models may treat Qwen 3.8 27B as a candidate for efficiency-focused testing against much larger systems, while waiting for workload-specific validation.

**Tags**: `#ai`, `#llms`, `#benchmarks`, `#qwen`, `#open-models`

---

<a id="item-tech-news-5"></a>
### [Anthropic Releases Claude Security Reference Harness](https://github.com/anthropics/defending-code-reference-harness) ⭐️ 7.0/10

Anthropic published the open-source \`anthropics/defending-code-reference-harness\` repository as a reference implementation for autonomous vulnerability discovery and remediation with Claude. The repo packages Claude Code skills for \`/quickstart\`, \`/threat-model\`, \`/vuln-scan\`, \`/triage\`, \`/patch\`, and \`/customize\`, plus an autonomous \`harness/\` pipeline that follows recon, find, verify, report, and patch stages. The included harness is configured for C/C++ memory vulnerability discovery using Docker and ASAN, while its prompts, sandboxing approach, and pipeline shape are intended to be customized for other languages, detectors, or vulnerability classes. Anthropic says the repository is not maintained and is not accepting contributions, and distinguishes it from the hosted Claude Security product, which provides managed scanning, false-positive reduction, lifecycle triage, fix validation, and rapid fix generation.

rss · GitHub Trending - Python Daily · Aug 18, 02:26

**「Background」** Claude Code skills are reusable command-style workflows that guide Claude through tasks such as threat modeling, scanning, triage, and patching inside a codebase. The harness reflects Anthropic’s stated learnings from working with security teams since launching Claude Mythos Preview and is accompanied by a blog post, cookbook, and documentation on pipeline design, prompting, threat modeling, sandboxing, and patch verification.

**「Impact」** Security teams and developers can use the repo as a starting point for building Claude-based vulnerability scanning and remediation pipelines, but autonomous runs execute target code and are designed to require gVisor sandboxing unless explicitly overridden.

**Tags**: `#AI security`, `#vulnerability scanning`, `#code remediation`, `#threat modeling`, `#open source`

---

<a id="item-tech-news-6"></a>
### [Needle 2 for Tiny Devices](https://github.com/cactus-compute/needle) ⭐️ 7.0/10

Needle 2 is an open 45M-parameter model packaged as a single 14MB binary for tool calling, device use, and structured extraction on tiny devices such as phones, wearables, smart home hardware, and robots. The project says it runs a full session in about 28MB of RAM, uses a 256-token sliding window with tools pinned as KV sinks, and returns structured tool calls with a confidence score. This repository is the Python package for inference, LoRA fine-tuning, and export, installable with \`pip install cactus-needle\`, while the engine is fetched once from Hugging Face and then cached for offline use. The README also says tuned models are merged back into a single \`.cact\` artifact and that the decoding path is constrained by schemas and a byte-level grammar.

rss · GitHub Trending - Python Daily · Aug 18, 02:26

**「Background」** Tool calling lets a model choose a predefined function or API and fill its arguments, while structured extraction constrains model output into a schema such as JSON for downstream software. Needle 2 is positioned in the edge AI category, where models must fit tight storage, memory, and offline constraints on devices such as phones, wearables, smart home hardware, and robots.

**「Impact」** Developers building local agents or extraction pipelines for constrained devices now have a self-contained model/runtime aimed at on-device tool use without separate model files or network inference.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/needle: 14MB foundation model for ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#edge-computing`, `#machine-learning`, `#open-source`

---

<a id="item-tech-news-7"></a>
### [FFF Targets Fast Repeated File Search](https://github.com/dmtrKovalenko/fff) ⭐️ 7.0/10

dmtrKovalenko/fff is a Rust-based file search toolkit and SDK aimed at AI agents, Neovim, Rust, C, Python, Bun, and Node.js integrations. The project claims typo-resistant path and content search, frequency-ranked file access, a background watcher, and a lightweight in-memory content index designed to outperform command-line tools such as ripgrep and fzf in long-running processes that search repeatedly. It includes an MCP server for clients such as Claude Code, Codex, OpenCode, Cursor, and Cline, with tools including ffgrep, fffind, and fff-multi-grep, plus installation paths via shell scripts and Homebrew. The README also describes a Pi agent extension with tools-and-ui, tools-only, and override modes, runtime commands such as /fff-health and /fff-rescan, and environment variables for frecency and history databases.

rss · GitHub Trending - Rust Daily · Aug 18, 02:27

**「Background」** File-search tools such as ripgrep and fzf are commonly used by developers and coding agents to locate paths or code text, but they are typically invoked as separate command-line searches. FFF is positioned as a library and long-running service instead, keeping search state such as an in-memory index, file-change watcher, and usage-based ranking available across repeated queries. It also grew out of an earlier Neovim-focused workflow before being packaged for agent and editor integrations.

**「Impact」** Developers building AI coding agents, editor integrations, or other long-running search workflows can use fff as a library or MCP server to avoid repeated external grep/find invocations and keep search state in memory.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/dmtrKovalenko/fff">GitHub - dmtrKovalenko / fff : The fastest and the most accurate file ...</a></li>

</ul>
</details>

**Tags**: `#developer tools`, `#search indexing`, `#AI agents`, `#Rust`, `#Neovim`

---

<a id="item-tech-news-8"></a>
### [Apple Revises EU App Store Terms](https://www.ithome.com/0/991/366.htm) ⭐️ 7.0/10

Apple announced on August 18 that it is changing its app commercial terms in the European Union after working with the European Commission, with the new terms available for developers to sign now and taking effect on October 1. The changes put all developers distributing apps in the EU under one set of terms and replace the previous per-install Core Technology Fee for certain larger developers with a 5% Core Technology Commission on in-app digital transactions in apps distributed outside the App Store. Apple also removed the initial acquisition fee and store services fee, and set updated commission rates of 26% for App Store apps using Apple In-App Purchase, 20% for App Store apps using alternative payment processing, 15% for App Store apps that send users outside the app to buy, and 5% for apps distributed through alternative marketplaces or the web, with lower 15% or 10% rates for qualifying programs and some subscriptions. Developers in the EU may now offer Apple In-App Purchase and alternative payment options together, but must choose and keep their payment configuration for 12 months, while child-safety rules restrict external purchase links and require parental controls for some under-18 users. Apple is also expanding eligibility to operate alternative app marketplaces or distribute apps through the web in the EU, while continuing to require notarization for apps distributed outside the App Store.

rss · IT之家 · Aug 18, 16:03

**「Context」** The EU&\#x27;s Digital Markets Act has pushed Apple to allow alternatives to its traditional App Store distribution and payment model in the European Union. Apple previously introduced EU-specific terms that included a per-install Core Technology Fee, but its latest revision replaces that structure with a 5% Core Technology Commission on certain digital transactions for apps distributed outside the App Store.

**「Impact」** Developers distributing iOS apps in the EU need to reassess payment, distribution, eligibility, and commission economics before the October 1 effective date.

<details><summary>References</summary>
<ul>
<li><a href="https://thenextweb.com/news/apple-eu-app-store-fees-dma-core-technology-commission">Apple overhauls EU App Store fees to settle its DMA dispute</a></li>
<li><a href="https://www.theverge.com/tech/981504/apple-app-store-eu-rules-core-technology-commission">Apple squashes EU beef with new App Store rules | The Verge</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#App Store`, `#EU regulation`, `#mobile development`, `#platform policy`

---

<a id="item-tech-news-9"></a>
### [Gas Plants for Data Centers Raise Emissions Concerns](https://www.ithome.com/0/991/345.htm) ⭐️ 7.0/10

Bloomberg reported that developers are increasingly building dedicated natural-gas power plants to supply rapidly expanding U.S. data centers, a shift that could make major technology companies&\#x27; climate goals harder to meet. BloombergNEF tracked 99 proposed gas plants and estimated that, if run at typical industry utilization rates, they could emit about 318 million metric tons of carbon dioxide per year. Compared with U.S. Energy Information Administration data showing about 1.485 billion tons of emissions from the U.S. electricity sector last year, those data-center-related plants could raise sector emissions by roughly 20%, or by about one-third if operated at full capacity. The report cites grid strain, reliability concerns, paused approvals in some areas, and multi-year waits for regulated grid connections as reasons developers are seeking direct power supplies. It also says Amazon is developing a 32.4-square-kilometer project in Pecos County, Texas, while Chevron is building a gas plant for Microsoft about 48 kilometers away to power an 8.1-square-kilometer data center campus; together, the two projects could exceed 10 GW of generation capacity and emit up to 45 million tons of CO2 equivalent annually, though Amazon and Microsoft said their climate targets have not changed.

rss · IT之家 · Aug 18, 14:49

**「Background」** Data centers require large, reliable power supplies for servers, cooling, networking, and increasingly AI workloads, which can make grid interconnection delays a major constraint on new projects. Natural-gas power plants can be built or contracted to provide dedicated electricity more quickly than many grid upgrades or low-carbon alternatives, but they emit carbon dioxide when operating and can conflict with corporate net-zero commitments.

**「Impact」** Data center operators and major cloud companies may face higher emissions and harder-to-meet climate targets if planned gas plants become the fastest route around constrained U.S. grid connections.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bloomberg.com/news/articles/2026-08-18/data-center-gas-plants-to-boost-us-power-emissions-by-20">Data Center Gas Plants to Boost US Power Emissions by 20%</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#energy infrastructure`, `#carbon emissions`, `#big tech`, `#AI infrastructure`

---

<a id="item-tech-news-10"></a>
### [Apple Says App Store Rules Are Hurting Services](https://www.ithome.com/0/991/342.htm) ⭐️ 7.0/10

Apple has for the first time acknowledged that antitrust pressure and App Store rule changes are beginning to affect its services business, which exceeds $100 billion and is a key source of high-margin profit. Its latest services revenue and margin both missed Wall Street expectations, with June-quarter services revenue of $30.7 billion below the expected $31.4 billion and gross margin at 75.6%, according to the report. Apple warned in a regulatory filing that it may receive no commission when consumers buy digital content through alternative payment systems, and CFO Kevan Parekh said recent App Store rule changes have affected services. Sensor Tower said U.S. App Store consumer spending fell 6% year over year in the second quarter after rising 9% a year earlier, while Appfigures estimated Apple’s U.S. App Store commission revenue has fallen 18% so far this year. Courts and regulators in the U.S., Europe, South Korea, Brazil and other markets have pushed Apple to loosen control over app payments or distribution, threatening the company’s model of charging commissions of up to 30% on in-app digital purchases and subscriptions.

rss · IT之家 · Aug 18, 14:30

**「Background」** Apple’s services segment includes App Store commissions, subscriptions, payments, warranties, licensing, and other recurring revenue streams, and it has become important because its margins are typically much higher than hardware sales. The App Store model historically let Apple control iPhone app distribution and charge developers up to 30% on many digital purchases, but court rulings and laws such as Europe’s Digital Markets Act have pushed the company to allow alternative payment or distribution options in some markets.

**「Impact」** Apple faces measurable pressure on App Store commissions as alternative payment and distribution rules take effect, with reported U.S. App Store consumer spending down 6% in the quarter and U.S. commission revenue down 18% since the start of the year.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/08/18/apple-admits-it-may-not-make-any-commission-from-alternative-app-stores/">Apple admits it may not make any commission from alternative app stores</a></li>
<li><a href="https://appleinsider.com/articles/26/08/18/apples-app-store-revenue-in-danger-of-being-regulated-away">Apple&#x27;s App Store revenue in danger of being regulated away</a></li>
<li><a href="https://www.macrumors.com/2026/08/18/apple-app-store-revenue-falling/">Apple &#x27;s US App Store Commission Revenue Down 18... - MacRumors</a></li>
<li><a href="https://www.pymnts.com/apple/2026/apple-says-antitrust-issues-are-hurting-services-business/">PYMNTS | Apple Says Antitrust Issues Are Hurting Services Business</a></li>

</ul>
</details>

**Tags**: `#苹果`, `#App Store`, `#反垄断监管`, `#服务业务`, `#移动支付`

---

<a id="item-tech-news-11"></a>
### [WeCom 5.0.10 Opens CLI and MCP Access](https://mp.weixin.qq.com/s/uJf57P15-FQL_u6jLHiGYA) ⭐️ 7.0/10

WeCom 5.0.10 has opened CLI and MCP capabilities to all enterprises, allowing WorkBuddy, DeepSeek Harness, and internally built agents to call 10 core office modules directly. The release matters because it gives mainstream AI agents a governed way to interact with enterprise collaboration and workflow systems rather than operating outside official platform controls. The integration supports separation between human and AI permissions, human approval for sensitive actions, time-limited authorization, and full auditing. According to the source, AI agents can also read documents and spreadsheets, analyze data, and generate proposal PPTs or business dashboards.

telegram · zaihuapd · Aug 18, 06:22

**「Background」** WeCom, also known as Enterprise WeChat, is Tencent&\#x27;s workplace collaboration platform for organizations using WeChat-linked communications and office workflows. MCP, or Model Context Protocol, is commonly used to let AI agents connect to external tools and data sources through standardized interfaces, while CLI access provides command-line automation hooks. WorkBuddy is Tencent&\#x27;s office-focused AI agent product that can generate reports, decks, spreadsheets, and other deliverables through multi-agent collaboration.

**「Impact」** Enterprises using WeCom can connect agents to office workflows while retaining permission isolation, approval gates, temporary authorization, and audit trails.

<details><summary>References</summary>
<ul>
<li><a href="https://www.workbuddy.ai/">WorkBuddy - AI Agent for Everyday Office Work</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#enterprise software`, `#AI agents`, `#workflow automation`, `#product announcement`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Jeanie Buss Opposes Lakers Stake Sale](https://www.cnbc.com/2026/08/17/jeanie-buss-opposes-sale-family-stake.html) ⭐️ 7.0/10

Los Angeles Lakers governor Jeanie Buss is opposing a potential sale of her family&\#x27;s stake to Bob Iger and Joshua Kushner, with her lawyer saying any vote to sell the JAB Trust&\#x27;s 17.8% ownership interest would be void without required approval.

rss · CNBC Finance · Aug 18, 21:29

**「Background」** A 2017 court order says the family trust&\#x27;s co-trustees must take reasonable steps to keep Jeanie Buss as the Lakers&\#x27; controlling owner, according to a supporting report.

**「Impact」** The dispute could delay or block Iger and Kushner from increasing their overall Lakers ownership share to about 83%, as ESPN reported the family stake sale would have done.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inkl.com/news/three-big-questions-circling-the-lakers-amid-potential-sale-of-buss-familys-remaining-stake">Three Big Questions Circling the Lakers Amid Potential</a></li>

</ul>
</details>

**Tags**: `#NBA`, `#mergers-and-acquisitions`, `#sports-business`, `#corporate-governance`, `#team-ownership`

---