---
layout: default
title: "Horizon Summary: 2026-08-14 (EN)"
date: 2026-08-14
lang: en
---

> From 326 items, 18 important content pieces were selected

---

**Technology News**
1. [AMD Memory-Mapping Flaw Exposes Protected DRAM Regions](#item-tech-news-1) ⭐️ 8.0/10
2. [Z.AI Presents GLM-5.3 With Emerging Cyber Capabilities](#item-tech-news-2) ⭐️ 7.0/10
3. [Google Introduces Gemini 3.7 Flash](#item-tech-news-3) ⭐️ 7.0/10
4. [Bluesky Introduces Protocol Services for AT Protocol](#item-tech-news-4) ⭐️ 7.0/10
5. [DeepSeek Harness Enters Developer Preview](#item-tech-news-5) ⭐️ 7.0/10
6. [Code Understanding Becomes the Bottleneck](#item-tech-news-6) ⭐️ 7.0/10
7. [Pi’s Approach to Conversation Compaction](#item-tech-news-7) ⭐️ 7.0/10
8. [Tracing Link Rot Across 657,607 Web Links](#item-tech-news-8) ⭐️ 7.0/10
9. [Journald issue reports severe filesystem write amplification](#item-tech-news-9) ⭐️ 7.0/10
10. [Anthropic Publishes Reusable Agent Skills for Claude](#item-tech-news-10) ⭐️ 7.0/10
11. [Needle 2 Targets On-Device Tool Calling in 14MB](#item-tech-news-11) ⭐️ 7.0/10
12. [Chrome DevTools MCP Connects Coding Agents to Live Browsers](#item-tech-news-12) ⭐️ 7.0/10
13. [Sandisk Targets First HBF Samples in 2027](#item-tech-news-13) ⭐️ 7.0/10
14. [X Opens More Recommendation Code and Tests Shadow-Ban Transparency Tools](#item-tech-news-14) ⭐️ 7.0/10
15. [MiniMax-Music3 Generates Songs Up to Five Minutes Long](#item-tech-news-15) ⭐️ 7.0/10
16. [LG and NVIDIA Move Broad AI Partnership Into Execution](#item-tech-news-16) ⭐️ 7.0/10
17. [Xiaohongshu Reportedly Releases 280B-Parameter dots3-note](#item-tech-news-17) ⭐️ 7.0/10

**Financial News**
1. [US Drone Import Tariffs Announced](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [AMD Memory-Mapping Flaw Exposes Protected DRAM Regions](https://www.ithome.com/0/989/793.htm) ⭐️ 8.0/10

Security researcher Christopher Domas disclosed “Skitter Creek Bath Salts,” an open-source attack and toolset that changes AMD Family 16h memory-controller address mapping at runtime to create alias addresses for protected DRAM regions. By toggling an unlocked Bank Swizzling register bit, an attacker can potentially read or modify memory associated with the AMD Platform Security Processor, System Management Mode, C6 processor state, and DRAM-resident microcode patches, then restore the original mapping with little evidence of the access. Domas tested the technique on older Jaguar- and Puma-based APUs, including Kabini, Temash, Beema, and Mullins; AMD advisory AMD-SB-7068 says relevant configuration registers in Family 15h and 16h processors may not be lockable, while Ryzen processors based on Zen and later architectures are not affected by this reported flaw. Exploitation requires existing root or administrator privileges, so it is not an initial-access method, and AMD will not issue patches because the affected processor families are no longer under security support.

rss · IT之家 · Aug 14, 08:31

**「Background」** A processor’s memory controller translates physical addresses into DRAM coordinates such as channels, banks, rows, and columns; changing that translation can make an ordinary address refer to a different physical memory location. The open-source “Skitter Creek Bath Salts” research examines this mechanism on AMD Family 15h and 16h systems, including older low-power Jaguar-era APUs, to reach protected areas associated with the PSP, SMM, C6 state, and microcode.

**「Impact」** On affected AMD Family 15h and 16h systems, an attacker who already has root or administrator access may be able to bypass hardware-isolated DRAM regions, and AMD does not plan to patch these unsupported processor families.

**「Community Discussion」** Commenters highlighted the broad attack surface created by increasingly complex DRAM controllers and noted that the technique could expose resources normally hidden from ring-0 software. They also questioned whether any newer processors are vulnerable and cautioned that possible implications for Jaguar-based game consoles remain conditional on first obtaining highly privileged access.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/skitter-creek-bath-salts">GitHub - xoreaxeaxeax/ skitter - creek - bath - salts : Unlocking...</a></li>
<li><a href="https://cyberpress.org/new-dram-scrambling-attack/">New DRAM Scrambling Attack Unlocks Protected Memory on AMD ...</a></li>

</ul>
</details>

**Tags**: `#硬件安全`, `#AMD处理器`, `#内存地址映射`, `#DRAM`, `#漏洞研究`

---

<a id="item-tech-news-2"></a>
### [Z.AI Presents GLM-5.3 With Emerging Cyber Capabilities](https://z.ai/blog/glm-5.3) ⭐️ 7.0/10

Z.AI presents GLM-5.3 as a frontier coding model with emerging capabilities in vulnerability discovery and exploitation. The company says the base model is unchanged from GLM-5.2 and attributes the reported improvement to scaled post-training and better agent environments. Its claims include finding vulnerabilities across popular open-source software, but many reported cases remain under embargo. Without source methodology, detailed benchmarks, or independent validation in the supplied material, the breadth and significance of these cybersecurity results remain uncertain.

hackernews · pella · Aug 14, 05:19 · [Discussion](https://news.ycombinator.com/item?id=49294997)

**「Background」** GLM is the model family behind Z.AI, whose public assistant was previously presented as powered by GLM-5.2. In this context, post-training means refining an existing base model for tasks such as coding and tool use, while cybersecurity capability can range from identifying possible flaws to reproducing and exploiting them in controlled environments.

**「Impact」** GLM-5.3 could reduce the cost of finding and validating vulnerabilities in widely used open-source software, increasing both defensive disclosure capacity and the remediation burden on maintainers. However, its broad vulnerability claims remain difficult to assess without public methodology, benchmark details, or independent validation.

**「Community Discussion」** Commenters were impressed by the reported coding performance, candid comparisons with stronger closed models, and a disclosure portal listing vulnerabilities across widely used software. They also noted that GLM-5.3 reportedly remains behind leading models on tasks further along the exploitation chain, while questioning local deployment economics and awaiting released weights.

<details><summary>References</summary>
<ul>
<li><a href="https://z.ai/blog/glm-5.3">GLM-5.3: Frontier Coding with Emergent Cyber Capabilities</a></li>

</ul>
</details>

**Tags**: `#coding models`, `#AI cybersecurity`, `#vulnerability discovery`, `#open source software`, `#large language models`

---

<a id="item-tech-news-3"></a>
### [Google Introduces Gemini 3.7 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/) ⭐️ 7.0/10

Google has introduced Gemini 3.7 Flash and published a Gemini API model documentation page, positioning another Flash-series model for developers. The supplied source contains almost no official technical detail, so its capabilities, compatibility constraints, benchmark results, and improvements over Gemini 3.6 Flash cannot be established from the primary material provided. Community discussion instead focuses on multimodal image-to-HTML generation, configurable reasoning levels, coding-agent benchmarks, and introductory API pricing reportedly scheduled to increase on January 1, 2027. Those comparisons are preliminary and largely anecdotal, limiting firm conclusions about the model&\#x27;s performance or value.

hackernews · thisisauserid · Aug 13, 17:23 · [Discussion](https://news.ycombinator.com/item?id=49289112)

**「Background」** Gemini Flash is Google’s model line intended for lower-latency, lower-cost workloads than its largest Gemini models, including high-volume text, multimodal, and coding tasks. Gemini 3.7 Flash follows Gemini 3.6 Flash, with Google describing substantial improvements in debugging, problem-solving, first-pass code accuracy, and production-level code generation.

**「Developer Cost Planning」** Developers can evaluate Gemini 3.7 Flash for coding and agent workloads at its introductory rate of $0.75 per million input tokens and $3.75 per million output tokens through December 31, 2026, but should account for the scheduled increase to $1.50 and $7.50 per million tokens from January 1, 2027.

**「Developer Reactions」** Early testers said Gemini 3.7 Flash performed well on vision-to-HTML work for its price but still trailed Opus 5, while others compared its reasoning-token usage and DeepSWE 1.1 results unfavorably with lower-cost Luna or Terra alternatives. Commenters also questioned the relevance of pricing scheduled to double by the end of 2026 given the rapid release cadence, noting that Gemini 3.6 Flash had reportedly arrived only three weeks earlier.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/intl/ja-jp/company-news/technology/gemini-37-flash/">Gemini 3.7 Flash を発表 - The Keyword</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/">Gemini 3.7 Flash: our most intelligent workhorse model</a></li>
<li><a href="https://www.explainx.ai/blog/gemini-3-7-flash-pricing-leak-rumor-august-2026">Gemini 3.7 Flash Launch: Pricing &amp; Benchmarks (Aug 2026 ...</a></li>

</ul>
</details>

**Tags**: `#large-language-models`, `#Gemini`, `#multimodal-AI`, `#AI-pricing`, `#coding-agents`

---

<a id="item-tech-news-4"></a>
### [Bluesky Introduces Protocol Services for AT Protocol](https://atproto.com/blog/introducing-bluesky-protocol-services) ⭐️ 7.0/10

Bluesky Protocol Services introduces infrastructure intended to support AT Protocol event-firehose consumption and downstream applications. The development appears particularly relevant to developers building services that process Bluesky events, including through the new Jetstream mentioned in the community discussion. However, the supplied item does not include the article text, so its architecture, compatibility requirements, operational limits, and differences from the original Jetstream cannot be established here.

hackernews · danabramov · Aug 14, 00:14 · [Discussion](https://news.ycombinator.com/item?id=49293324)

**「Background」** AT Protocol is the open networking protocol underlying Bluesky, and its event firehose lets downstream systems continuously receive network activity for indexing, analysis, and application features. Bluesky Protocol Services is the new brand and website for the public AT Protocol infrastructure operated by Bluesky, including services such as Jetstream that simplify consuming firehose data.

**「Developer Impact」** AT Protocol developers now have a dedicated site for discovering and accessing Bluesky-operated Jetstream instances, relays, and API endpoints used to build firehose-driven tools, feeds, moderation services, bots, and applications.

**「Community Discussion」** Commenters highlighted Jetstream&\#x27;s practical accessibility, including direct browser-based firehose consumption, while also proposing broader infrastructure uses such as downstream DNS services. Others raised concerns about Bluesky&\#x27;s outage transparency and reliability as its focus expands beyond the main app.

<details><summary>References</summary>
<ul>
<li><a href="https://atproto.com/blog/introducing-bluesky-protocol-services">Introducing Bluesky Protocol Services - AT Protocol</a></li>
<li><a href="https://docs.bsky.app/blog/jetstream">Introducing Jetstream | Bluesky</a></li>
<li><a href="https://atproto.com/blog/introducing-bluesky-protocol-services">Introducing Bluesky Protocol Services - AT Protocol</a></li>

</ul>
</details>

**Tags**: `#AT Protocol`, `#Bluesky`, `#Open Protocols`, `#Event Streaming`, `#Distributed Systems`

---

<a id="item-tech-news-5"></a>
### [DeepSeek Harness Enters Developer Preview](https://deepseek.com/harness/en/) ⭐️ 7.0/10

DeepSeek released DeepSeek Harness as an MIT-licensed developer preview for building AI agents. The framework centers execution on an append-only event stream that records prompts, reasoning, tool calls and results, subagent scheduling, and context injections for inspection in a Trajectory view. The same event stream supports resuming, forking, searching, and replaying runs, while its plugin architecture allows capabilities and UI components to be enabled, disabled, or reloaded dynamically. The authors warn that this is an early release with rough edges and likely compatibility-breaking changes, and the supplied material does not provide independent technical or performance validation.

hackernews · bjin · Aug 13, 12:58 · [Discussion](https://news.ycombinator.com/item?id=49285244)

**「Background」** An AI agent harness is the runtime layer that coordinates a model with tools, sessions, storage, sandboxes, scheduling, and user interfaces; DeepSeek Harness exposes each of these capabilities as a replaceable or recomposable plugin. Its append-only session log follows an event-stream approach, preserving execution records so a run can be inspected, resumed, forked, searched, or replayed from recorded events.

**「Impact」** Agent-harness developers can build on a source-available, plugin-based system whose models, tools, sessions, storage, scheduling, and UI can be recomposed, but the early preview’s expected breaking changes make it unsuitable for compatibility-sensitive production use.

**「Community Discussion」** Commenters highlighted trace visibility and reversible hot-loading of plugins as the most promising features, with some connecting the design to Cordis v4 and its earlier use in Koishi. Others questioned the framework&\#x27;s practical value, complexity, and plugin-heavy architecture, while an author reiterated that the release is intended to gather early feedback.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness/blob/master/README.md">deepseek-harness/README.md at master · deepseek-ai ... - GitHub</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#developer tools`, `#open source`, `#observability`, `#plugin systems`

---

<a id="item-tech-news-6"></a>
### [Code Understanding Becomes the Bottleneck](https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck) ⭐️ 7.0/10

The essay argues that as LLMs make code generation cheaper, understanding code, intent, and system architecture may become the limiting factor in software development. Engineers still need accurate mental models to judge whether generated changes preserve deeper requirements such as scalability, flexibility, and architectural coherence. Producing summaries or documentation with the same LLM does not necessarily solve the problem because those outputs can omit motivation, overemphasize mechanical changes, or reproduce incorrect assumptions. The supplied excerpt does not include the essay&\#x27;s full technical argument, so its proposed solutions and supporting evidence cannot be assessed here.

hackernews · sebg · Aug 13, 18:47 · [Discussion](https://news.ycombinator.com/item?id=49290299)

**「Background」** Software development depends on a mental model of a system&\#x27;s architecture, behavior, constraints, and intended purpose, not merely the ability to produce working code. LLM coding agents can accelerate implementation, but directing repeated agent interactions and deciding how a project should evolve still requires a rich understanding of the system.

**「Impact」** Teams adopting AI-assisted development may need to spend more engineering effort reviewing generated changes against system intent rather than treating faster code production as faster delivery.

**「Community Discussion」** Commenters broadly agree that understanding and verification matter, but several argue that the bottleneck predates LLMs and has long been central to engineering leadership, program management, and maintainable system design. Others report that LLM-generated pull-request descriptions are often overly mechanical and weak on motivation, warning that an LLM cannot independently verify its own potentially flawed account of a change.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geoffreylitt.com/2026/07/02/understanding-is-the-new-bottleneck">Understanding is the new bottleneck</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#software architecture`, `#code comprehension`, `#engineering management`, `#LLMs`

---

<a id="item-tech-news-7"></a>
### [Pi’s Approach to Conversation Compaction](https://earendil.com/posts/compaction-in-pi/) ⭐️ 7.0/10

The article examines how Pi compacts long AI-agent conversations when accumulated messages approach the model’s context limit. Compaction summarizes earlier material to free context space, allowing an agent to continue working, but it can discard intent or details needed later. The discussion places this mechanism among alternatives such as pruning low-value messages, proactively limiting context use, and managing multiple KV caches. The supplied evidence presents a practical engineering analysis rather than a new compaction breakthrough.

hackernews · tosh · Aug 13, 17:57 · [Discussion](https://news.ycombinator.com/item?id=49289654)

**「Background」** Large language models can consider only a limited amount of conversation and tool output at once, a capacity known as the context window. Coding agents such as Pi use compaction to replace older context with a shorter representation when a long-running session approaches that limit, trading detail for enough space to continue working.

**「Impact」** Pi users can continue long-running sessions beyond context limits and switch models while retaining a readable, portable plain-text summary of older work alongside recent messages.

**「Community Discussion」** Commenters generally agreed that compaction is lossy, while differing on whether selective pruning, branching and summarizing sessions, or keeping utilization below roughly 30% of the context window works best. Others described dual-KV-cache summarization and pointer-based replacement of tool results or reasoning traces, but noted that more aggressive techniques can invalidate prompt caches and increase cost.

<details><summary>References</summary>
<ul>
<li><a href="https://earendil.com/posts/compaction-in-pi/">How Compaction Works in Pi | EARENDIL</a></li>
<li><a href="https://earendil.com/posts/compaction-in-pi/">How Compaction Works in Pi | EARENDIL</a></li>
<li><a href="https://pi.dev/docs/latest/compaction">Compaction &amp; Branch Summarization · Documentation · Pi</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#context compaction`, `#context windows`, `#KV cache`, `#LLM infrastructure`

---

<a id="item-tech-news-8"></a>
### [Tracing Link Rot Across 657,607 Web Links](https://0.mk/blog/link-rot) ⭐️ 7.0/10

The reported analysis followed 657,607 links to investigate how much older web content remains accessible and how extensively link rot has erased parts of the web. Its scale makes the findings relevant to digital preservation, web infrastructure, and the long-term reliability of references in websites and software documentation. However, the supplied material does not include the study&\#x27;s methodology, date range, accessibility criteria, or results, so its conclusions cannot be assessed or quantified here. The analysis also raises a broader question about whether the &quot;old web&quot; denotes a specific historical period or a changing cultural experience.

hackernews · tdx · Aug 13, 17:49 · [Discussion](https://news.ycombinator.com/item?id=49289532)

**「Background」** Link rot is the gradual loss of access to web content as pages move, domains expire, and servers or sites disappear. Measuring it by raw URLs can exaggerate the influence of a single domain: in this analysis, one account contributed 83,398 distinct 2011 links to pelaphptutorials.com, producing a 92.5% failure rate at the URL level but 61.7% when that host was counted once.

**「Impact」** Researchers, maintainers, and readers cannot reliably use pre-2015 links as durable references, as the study found that 76.7% of 655,178 safe, crawlable records no longer returned a loading page.

**「Community Discussion」** Commenters disagreed sharply on when the old web ended, proposing milestones ranging from the public arrival of Google Search to Facebook&\#x27;s rise, while others argued that the term reflects when individuals first discovered online communities more than a fixed era. One commenter suggested that a smaller, enthusiast-driven web could re-emerge as mainstream activity becomes concentrated elsewhere.

<details><summary>References</summary>
<ul>
<li><a href="https://0.mk/blog/link-rot">Where did the old web go ? We followed 657 , 607 links to find... | 0.mk</a></li>
<li><a href="https://0.mk/blog/link-rot">Where did the old web go ? We followed 657 , 607 links to find out .</a></li>

</ul>
</details>

**Tags**: `#link rot`, `#web preservation`, `#internet history`, `#web infrastructure`

---

<a id="item-tech-news-9"></a>
### [Journald issue reports severe filesystem write amplification](https://github.com/systemd/systemd/issues/40262) ⭐️ 7.0/10

A systemd issue reports that sending a single log line through systemd-journald can cause more than 49 KB of disk writes on ext4 and more than 110 KB on btrfs. Such write amplification could affect storage performance and endurance, particularly on systems with frequent logging or write-sensitive media. The supplied material does not identify the affected systemd versions, establish reproducibility, explain the root cause, or report an upstream resolution. The measurements should therefore be treated as an issue report rather than a confirmed general characteristic of journald.

hackernews · ValdikSS · Aug 13, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49290215)

**「Background」** systemd-journald is systemd&\#x27;s logging service, storing structured messages in binary journal files when persistent storage is enabled. Write amplification occurs when the storage stack writes substantially more data than the original log payload because of journal metadata, indexing, synchronization, and filesystem-level operations; the reported case used systemd 257.9 on Debian 13 with Linux 6.12.57.

**「Impact」** Under the reported test conditions, persistent journald logging at only two lines per second sustained about 50 IOPS in a VM, potentially increasing storage load and write wear on affected ext4 and btrfs systems.

**「Community Discussion」** Commenters broadly criticized journald&\#x27;s storage and indexing behavior, highlighting uncontrolled log volume, limited filtering, and difficulty managing individual noisy services. Some recommended using journald only for routing, with persistent storage and filtering handled by tools such as rsyslog, while another noted that the reported behavior appears inconsistent with the journal format&\#x27;s append-oriented design intent.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/systemd/systemd/issues/40262">Excessive IO caused by systemd-journald · Issue #40262 · systemd/systemd</a></li>
<li><a href="https://zeli.app/en/story/49290215">systemd-journald writes 49KB+ per log line on ext4, 110KB+ on ...</a></li>

</ul>
</details>

**Tags**: `#systemd`, `#journald`, `#Linux filesystems`, `#write amplification`, `#logging`

---

<a id="item-tech-news-10"></a>
### [Anthropic Publishes Reusable Agent Skills for Claude](https://github.com/anthropics/skills) ⭐️ 7.0/10

Anthropic has published a public repository of Agent Skills, self-contained bundles of instructions, scripts, and resources that Claude loads dynamically for specialized, repeatable tasks. Each skill is organized around a SKILL.md file whose YAML frontmatter requires a lowercase, hyphenated name and a description of what the skill does and when Claude should use it. The repository includes a specification, template, and examples spanning creative work, web-app testing, MCP server generation, enterprise workflows, and document handling, with access through Claude Code plugins, paid Claude.ai plans, and the Claude API. Many examples use the Apache 2.0 license, but the production-backed DOCX, PDF, PPTX, and XLSX skills are only source-available; Anthropic also cautions that the repository is primarily educational and that behavior may differ in Claude, so critical uses require independent testing.

rss · GitHub Trending - Daily · Aug 14, 03:22

**「Background」** Agent Skills are a lightweight, open format for extending AI agents with specialized knowledge and workflows, centered on a folder containing a \`SKILL.md\` file. Anthropic&\#x27;s repository includes its Claude implementation, the specification, templates, and examples that can be used through Claude Code, Claude.ai, or the Claude API.

**「Developer impact」** Claude developers can package repeatable workflows as versioned custom skills for use through Claude Code and the API, although API use requires the Code Execution Tool.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/skills">GitHub - anthropics / skills : Public repository for Agent Skills · GitHub</a></li>
<li><a href="https://agentskills.io/">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://claude.com/blog/skills">Introducing Agent Skills | Claude by Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Claude`, `#agent skills`, `#open source`, `#developer tools`

---

<a id="item-tech-news-11"></a>
### [Needle 2 Targets On-Device Tool Calling in 14MB](https://github.com/cactus-compute/needle) ⭐️ 7.0/10

Cactus Compute has released Needle 2, an open 45M-parameter model packaged with its inference engine as a single 14MB binary for on-device tool calling, device control, and structured extraction. The project says a session uses about 28MB of RAM, with CQ2-bit quantization, a 256-token sliding window, pinned tool KV sinks, schema-derived byte-level grammar constraints, confidence scoring, and retrieval that exposes the top five relevant tools per turn. The Python package, installable as \`cactus-needle\`, supports local inference without network access after its engine is downloaded from Hugging Face, as well as Pydantic-based extraction, LoRA fine-tuning, synthetic-data generation, and export to a single \`.cact\` file. Cactus Compute reports that Needle 2 trades benchmark wins with FunctionGemma 270M, LFM2.5 230M, and Apple FM while being 5 to 70 times smaller, but the supplied material provides limited benchmark methodology, so those comparisons remain self-reported.

rss · GitHub Trending - Daily · Aug 14, 03:22

**「Background」** Tool-calling models translate natural-language requests into structured function names and arguments, allowing software to invoke APIs or device controls. Needle 2 targets constrained edge hardware by combining 2-bit quantization, which compresses model weights, with schema-constrained decoding for valid structured output and LoRA for parameter-efficient task-specific fine-tuning.

**「Impact」** Developers can add offline, schema-constrained tool calling and structured extraction to memory-limited devices using a 14MB model that reportedly holds full-session RAM use near 28MB, although its comparative performance claims remain self-reported.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/needle: 14MB foundation model for ...</a></li>
<li><a href="https://cactuscompute.com/needle">Needle 2 - The 14 MB Agentic LLM for Tiny Devices | Cactus</a></li>
<li><a href="https://huggingface.co/Cactus-Compute/needle2">Cactus-Compute/ needle 2 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#edge AI`, `#small language models`, `#model quantization`, `#tool calling`, `#open source`

---

<a id="item-tech-news-12"></a>
### [Chrome DevTools MCP Connects Coding Agents to Live Browsers](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 7.0/10

ChromeDevTools has released chrome-devtools-mcp, an MCP server and standalone CLI that lets coding agents such as Antigravity, Claude, Cursor, and Copilot control and inspect a live Chrome browser. It uses Chrome DevTools to capture traces and performance insights, inspect network requests and console messages with source-mapped stack traces, and take screenshots, while Puppeteer provides browser automation with automatic waiting for action results. The tool requires an LTS version of Node.js, npm, and the current stable Chrome or newer; only Google Chrome and Chrome for Testing are officially supported, although other Chromium-based browsers may work. Browser contents are exposed to connected MCP clients, usage statistics and update checks are enabled by default, and performance analysis may send trace URLs to the Google CrUX API, with flags or environment variables available to disable these behaviors.

rss · GitHub Trending - TypeScript Daily · Aug 14, 03:39

**「Background」** The Model Context Protocol \(MCP\) is a standard interface through which AI applications can invoke external tools and access contextual data. Chrome DevTools MCP, introduced as a public preview, applies that interface to a live Chrome session and combines DevTools inspection and performance capabilities with Puppeteer-based browser automation.

**「Impact」** Developers can give compatible coding agents direct browser-debugging and performance-analysis capabilities, but should use a dedicated Chrome profile because connected MCP clients can inspect or modify browser data and usage statistics are collected by default unless separately disabled.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/blog/chrome-devtools-mcp">Chrome DevTools (MCP) for your AI agent | Blog | Chrome for Developers</a></li>

</ul>
</details>

**Tags**: `#Chrome DevTools`, `#coding agents`, `#Model Context Protocol`, `#browser automation`

---

<a id="item-tech-news-13"></a>
### [Sandisk Targets First HBF Samples in 2027](https://www.ithome.com/0/989/796.htm) ⭐️ 7.0/10

Sandisk disclosed additional specifications and a production roadmap for high-bandwidth flash \(HBF\), following its announcement of an initial HBF standard with SK hynix. The first version is expected to offer up to 512GB using 8-layer or 16-layer stacks, with three bandwidth grades spanning roughly 0.4TB/s to 3.0TB/s; initial samples are planned for 2027 and mass production for 2028. The NAND-based technology aims to approach the read bandwidth of DRAM-based HBM at lower cost and with 8 to 16 times its capacity, although with higher latency. Sandisk says its internal AI model tests matched the token output of an eight-GPU HBM system using four GPUs with HBF, but the product has not yet been sampled and the performance claim has not been independently verified; Mizuho Securities expects HBF to complement rather than fully replace HBM, particularly in disaggregated AI inference systems.

rss · IT之家 · Aug 14, 08:42

**「Background」** High Bandwidth Memory \(HBM\) is stacked DRAM designed to provide accelerators with high throughput and low latency, while High Bandwidth Flash \(HBF\) applies a high-bandwidth architecture to denser, lower-cost NAND flash but accepts higher latency. Sandisk and SK hynix developed the first HBF specification through the Open Compute Project, defining areas including the accelerator-to-HBF interface, packaging, reliability, and software operations; it is a technical standard rather than an available commercial product.

**「Impact」** If SanDisk’s internal results hold, HBF could let AI inference systems keep much larger model weights near accelerators while using fewer GPUs, reducing server costs; however, this remains unverified before initial samples arrive in 2027 and mass production begins in 2028.

<details><summary>References</summary>
<ul>
<li><a href="https://news.skhynix.com/en/hbf-at-fms-2026/">SK hynix Unveils First HBF Standard Specifications with ...</a></li>
<li><a href="https://letsdatascience.com/news/sandisk-and-sk-hynix-publish-first-hbf-specification-ef07f241">Sandisk and SK hynix Publish First HBF Specification | Let&#x27;s ...</a></li>

</ul>
</details>

**Tags**: `#高带宽闪存`, `#AI硬件`, `#存储系统`, `#内存带宽`, `#半导体`

---

<a id="item-tech-news-14"></a>
### [X Opens More Recommendation Code and Tests Shadow-Ban Transparency Tools](https://www.ithome.com/0/989/727.htm) ⭐️ 7.0/10

X has expanded its open-source repository to include code for the For You timeline, core ranking, recommendation, and filtering mechanisms under the Apache 2.0 license. The released code is intended to show how ranking labels and other content tags can affect a post’s visibility and distribution, although some systems used to assess policy violations, including Grok-based components, have not been disclosed. X is also piloting an Under the Hood feature that lets eligible users inspect account and post labels that may affect visibility; eligibility initially requires at least 10 posts in the previous month and an account at least one year old, with access assigned randomly among test accounts. The tool will roll out gradually and may be adjusted based on public feedback, while the practical completeness of the code, its relationship to production systems, and the results of any independent audit remain unclear.

rss · IT之家 · Aug 14, 07:23

**「Background」** X’s “For You” feed uses a recommendation pipeline to select, rank, and filter posts for each user, and the company maintains a public repository describing it as the algorithm that powers that feed. “Shadow banning” is an informal term for reducing an account’s or post’s visibility through ranking or filtering without an explicit suspension, although reduced reach can also result from ordinary recommendation decisions.

**「Impact」** Eligible X users will be able to identify account or post labels affecting their visibility, while developers can inspect more of the “For You” ranking and filtering code; initially, however, the transparency tool is limited to randomly selected accounts at least one year old that posted more than 10 times in the previous month.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xai-org/x-algorithm/blob/main/phoenix/README.md">x-algorithm/phoenix/README.md at main · xai-org/x-algorithm</a></li>
<li><a href="https://github.com/xai-org/x-algorithm/tree/main/">GitHub - xai-org/x-algorithm: Algorithm powering the For You ...</a></li>
<li><a href="https://techcrunch.com/2026/08/13/x-open-sources-its-ranking-algorithm-letting-users-see-if-theyve-been-shadowbanned/">X open sources its ranking algorithm, letting users see if ...</a></li>
<li><a href="https://hypebeast.com/2026/8/x-expands-open-source-ranking-algorithm-with-new-tool">X Ranking Algorithm Open-Source Expansion and New Tool ...</a></li>

</ul>
</details>

**Tags**: `#推荐算法`, `#开源`, `#内容排名`, `#平台治理`, `#算法透明度`

---

<a id="item-tech-news-15"></a>
### [MiniMax-Music3 Generates Songs Up to Five Minutes Long](https://www.ithome.com/0/989/722.htm) ⭐️ 7.0/10

MiniMax released MiniMax-Music3, a music generation model that creates complete songs up to five minutes long from lyrics and musical descriptions. Its hierarchical autoregressive architecture combines an 8-billion-parameter Global LLM, initialized from Qwen3-8B, with a 0.6-billion-parameter Local LLM: the global model predicts the first RVQ codebook for long-range semantics and structure, while the local model predicts the remaining acoustic codebooks for fine-grained detail. Generated songs are delivered as 32 kHz, 16-bit stereo WAV files, and MiniMax claims the model can preserve themes, rhythm, vocal identity, and arrangement progression across sections including verses, choruses, bridges, instrumental breaks, and outros. However, the available information primarily reflects MiniMax&\#x27;s own claims and does not include public benchmarks, independent evaluations, training details, or clear availability information, so real-world quality remains unverified.

rss · IT之家 · Aug 14, 07:15

**「Background」** Residual vector quantization \(RVQ\) represents audio using multiple discrete codebooks: an initial codebook captures broad information, while subsequent codebooks refine acoustic detail. MiniMax-Music3 applies this division through a hierarchical autoregressive architecture, with separate global and local language models handling long-range musical structure and fine-grained sound reconstruction, respectively.

**「Impact」** Music creators and developers can generate complete songs lasting up to five minutes from lyrics and musical descriptions, although real-world quality remains uncertain without public benchmarks or independent evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MiniMax-AI/MiniMax-Music3">GitHub - MiniMax-AI/MiniMax-Music3</a></li>
<li><a href="https://github.com/MiniMax-AI/MiniMax-Music3">GitHub - MiniMax -AI/ MiniMax - Music 3 · GitHub</a></li>

</ul>
</details>

**Tags**: `#音乐生成`, `#生成式AI`, `#音频模型`, `#自回归模型`, `#MiniMax`

---

<a id="item-tech-news-16"></a>
### [LG and NVIDIA Move Broad AI Partnership Into Execution](https://www.ithome.com/0/989/696.htm) ⭐️ 7.0/10

LG and NVIDIA signed a memorandum of understanding at NVIDIA’s Santa Clara headquarters on August 13, expanding their AI collaboration across robotics, AI factories, and automotive computing. LG plans to test its wheeled CLOiD robot at its Tennessee washing-machine factory and unveil a next-generation bipedal humanoid robot in the first quarter of 2027 using NVIDIA Jetson Thor, the Isaac GR00T reference platform, and the Halos for Robotics safety stack. The company also targets a Vera Rubin-based NVIDIA DSX AI factory demonstration in the first half of 2027 and an 80 MW AI factory in Cheonan, South Korea, by the first half of 2028. In automotive technology, LG plans to develop a high-performance computing platform based on NVIDIA DRIVE Hyperion and integrate its own infotainment and vehicle software, though the announcement remains an MOU centered largely on future validation and construction milestones.

rss · IT之家 · Aug 14, 06:07

**「Background」** In this context, an “AI factory” is computing infrastructure for developing and operating AI models, distinct from the LG appliance factory where robots will be tested. NVIDIA’s Jetson Thor, Isaac GR00T, and robotics safety technologies provide the computing, model platform, and safety stack for LG’s planned humanoid, while DRIVE Hyperion serves as the basis for its proposed automotive computing platform.

**「Impact」** If the planned infrastructure is completed, LG will gain a shared NVIDIA-based computing foundation for robotics, autonomous driving, data-center technology, and GPU cloud services, though the projects remain subject to future validation and construction.

<details><summary>References</summary>
<ul>
<li><a href="https://www.prnewswire.com/news-releases/lg-to-unveil-its-next-gen-humanoid-robot-built-on-nvidia-isaac-gr00t-302851583.html">LG to Unveil Its Next-Gen Humanoid Robot, Built on NVIDIA ...</a></li>
<li><a href="https://www.ajupress.com/view/20260814110043056">LG to roll out Nvidia-powered humanoid Q1 2027 | Aju Press</a></li>
<li><a href="https://blogs.nvidia.com/blog/nvidia-and-lg-group-ai-factory/">NVIDIA and LG Group Build an AI Factory to Advance Physical ...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#机器人`, `#AI基础设施`, `#人形机器人`, `#汽车计算`

---

<a id="item-tech-news-17"></a>
### [Xiaohongshu Reportedly Releases 280B-Parameter dots3-note](https://x.com/dotsstudioai/status/2088083314855018521) ⭐️ 7.0/10

Xiaohongshu&\#x27;s dots lab reportedly released dots3-note preview, the first open-weight model in the dots3 series, through Hugging Face. The multimodal mixture-of-experts model has 280 billion total parameters but activates 16 billion per inference step, supports a 512K-token context window, and accepts text, images, video, and audio. The release also introduces TEMPO, a reinforcement-learning method intended to train long-horizon agents using self-critique and test-time value estimation, alongside the real-world agent benchmarks VibeSearchBench and VibeLifeBench. However, the available account is a Telegram relay and provides no paper, evaluation results, license terms, or deployment requirements, so the model&\#x27;s capabilities and degree of openness remain unverified.

telegram · zaihuapd · Aug 14, 08:27

**「Background」** A mixture-of-experts \(MoE\) model routes each input through only a subset of its expert components, so its activated parameter count can be much smaller than its total parameter count; for dots3-note preview, those figures are 16B and 280B, respectively. “Open-weight” means the trained weights are available for download, but it does not by itself guarantee an open-source license or unrestricted use; the project provides an FP8 weight release through Hugging Face.

**「Impact」** Developers could run or adapt an open-weight, multimodal 512K-context model with only 16B parameters active per inference step, potentially lowering compute relative to a dense 280B model. Practical accessibility remains unclear because licensing, hardware requirements, deployment details, and independent evaluations were not provided.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/studio-dots-ai/dots3-note-prev">GitHub - studio-dots-ai/dots3-note-prev: dots3 note preview</a></li>
<li><a href="https://huggingface.co/dots-studio/dots3-note-prev-fp8">dots-studio/dots3-note-prev-fp8 · Hugging Face</a></li>
<li><a href="https://ai-manual.ru/article/dots3-note-preview-lyogkij-gigant-v-mire-open-weight-moe-modelej/">dots 3 - note preview: лёгкий гигант в мире open-weight... | AiManual</a></li>

</ul>
</details>

**Tags**: `#大语言模型`, `#混合专家模型`, `#多模态AI`, `#强化学习`, `#开放权重`

---

## Financial News

<a id="item-finance-news-1"></a>
### [US Drone Import Tariffs Announced](https://www.whitehouse.gov/presidential-actions/2026/08/adjusting-imports-of-unmanned-aircraft-systems-and-unmanned-aircraft-systems-components-into-the-united-states/) ⭐️ 7.0/10

A Telegram report says the US president signed a proclamation imposing tariffs from September 3, 2026, of 100% on imported drones weighing more than 25 kilograms, thermal-imaging drones, ground stations and certain key components, and 25% on drones weighing 25 kilograms or less. It says a 25% tariff on additional components will take effect on February 9, 2027, with the commerce secretary authorized to add more components.

telegram · zaihuapd · Aug 14, 01:24

**「Background」** The White House lists the measure as an August 13, 2026 presidential proclamation, a formal action issued by the president.

**「Impact」** U.S. importers of covered drones and components, particularly those sourcing from China, will face substantially higher border taxes when the tariffs take effect.

<details><summary>References</summary>
<ul>
<li><a href="https://www.whitehouse.gov/presidential-actions/">Presidential Actions – The White House</a></li>
<li><a href="https://www.bangkokpost.com/world/3301603/trump-announces-tariffs-of-up-to-100-on-imported-drones">Trump announces tariffs of up to 100% on imported drones</a></li>

</ul>
</details>

**Tags**: `#无人机关税`, `#美国贸易政策`, `#无人机供应链`, `#进口限制`

---