---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 303 items, 32 important content pieces were selected

---

1. [Anna's Archive Offers $200k Bounty for All Google Books Scans](#item-1) ⭐️ 9.0/10
2. [YouTube Private Videos Leaked via Prompt Injection](#item-2) ⭐️ 9.0/10
3. [Microsoft Agent Governance Toolkit for Secure AI Agents](#item-3) ⭐️ 9.0/10
4. [World's first sub-10ms neural dynamical system chip based on phase-change memristors](#item-4) ⭐️ 9.0/10
5. [Chinese astronomers find strongest evidence for intermediate-mass black hole in Milky Way](#item-5) ⭐️ 9.0/10
6. [First Synthetic Cell with Complete Lifecycle Created](#item-6) ⭐️ 9.0/10
7. [Better Models: Worse Tool Calling](#item-7) ⭐️ 8.0/10
8. [actions/checkout v7: Safer fork PR handling and ESM migration](#item-8) ⭐️ 8.0/10
9. [Chrome DevTools MCP brings DevTools to AI coding agents](#item-9) ⭐️ 8.0/10
10. [Meta Open-Sources Astryx Design System](#item-10) ⭐️ 8.0/10
11. [Harvard's CS249r Book: Open-Source ML Systems](#item-11) ⭐️ 8.0/10
12. [Anthropic Releases Claude Code: Open-Source Agentic Coding Tool](#item-12) ⭐️ 8.0/10
13. [TencentCloud Releases CubeSandbox for AI Agent Security](#item-13) ⭐️ 8.0/10
14. [NVlabs Releases ProtoMotions3 for Humanoid Simulation & Learning](#item-14) ⭐️ 8.0/10
15. [Hugging Face Launches Low-Latency Speech-to-Speech Pipeline](#item-15) ⭐️ 8.0/10
16. [Vue 2 Reaches End of Life, Urging Upgrade to Vue 3](#item-16) ⭐️ 8.0/10
17. [Alibaba Releases Page Agent for Natural Language Web Control](#item-17) ⭐️ 8.0/10
18. [Bun: A fast all-in-one JavaScript runtime and toolkit](#item-18) ⭐️ 8.0/10
19. [NVIDIA OpenShell: Sandboxed Runtime for Autonomous AI Agents](#item-19) ⭐️ 8.0/10
20. [Prometheus Monitoring System GitHub Repository Overview](#item-20) ⭐️ 8.0/10
21. [Nuclei: Fast, Community-Powered Vulnerability Scanner](#item-21) ⭐️ 8.0/10
22. [Google Releases Open-Source Go ADK for AI Agents](#item-22) ⭐️ 8.0/10
23. [Micron's SCAs lock high memory prices until 2030, no drop before 2031](#item-23) ⭐️ 8.0/10
24. [China proposes banning unauthorized bypass of state technical measures](#item-24) ⭐️ 8.0/10
25. [AI Data Centers' Indirect Water Use Far Exceeds Reported Amounts](#item-25) ⭐️ 8.0/10
26. [Tesla Robotaxi Launches in Miami Without Safety Drivers](#item-26) ⭐️ 8.0/10
27. [Immune Cells Use Neurotransmitters to Communicate](#item-27) ⭐️ 8.0/10
28. [Anthropic Enters Drug R&D, Targets Neglected Diseases](#item-28) ⭐️ 8.0/10
29. [BaryGraph redefines relationships as embedded documents](#item-29) ⭐️ 8.0/10
30. [Google Bans AI Jailbreaking and Prediction Markets in Chrome Extensions](#item-30) ⭐️ 8.0/10
31. [iOS 27 Introduces Trust Insights On-Device Fraud Detection](#item-31) ⭐️ 8.0/10
32. [South Korea to invest 800 trillion KRW in semiconductor cluster, aiming to double DRAM output](#item-32) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anna's Archive Offers $200k Bounty for All Google Books Scans](https://software.annas-archive.gl/AnnaArchivist/annas-archive/-/work_items/234) ⭐️ 9.0/10

Anna's Archive has announced a $200,000 bounty to compile all Google Books scans by 2025, aiming to aggregate the entire collection into its open access repository. This initiative could dramatically expand access to millions of digitized books that are currently behind paywalls or unavailable, potentially reshaping digital preservation and open access movements. It also raises significant legal and ethical questions about copyright and piracy, affecting authors, publishers, and readers worldwide. The bounty is intended to fund efforts to scrape, download, or otherwise aggregate Google Books scans, which are not all publicly accessible. Anna's Archive does not host files directly but links to third-party sources, a model that has faced legal challenges for copyright infringement.

hackernews · Cider9986 · Jul 4, 16:51 · [Discussion](https://news.ycombinator.com/item?id=48786838)

**Background**: Anna's Archive is an open-source search engine for shadow libraries, launched in 2022 after crackdowns on Z-Library. It aggregates records from Z-Library, Sci-Hub, and Library Genesis, aiming to catalog all books in existence. Google Books is a large-scale project that scans books from libraries and publishers, but many scans are only available in preview mode or through paywalls. Shadow libraries like Anna's Archive provide free access to such materials, often without authorization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anna's_Archive">Anna's Archive</a></li>
<li><a href="https://en.wikipedia.org/wiki/Shadow_library">Shadow library</a></li>

</ul>
</details>

**Discussion**: Community members expressed strong support for Anna's Archive, sharing personal stories of accessing rare or out-of-print books that improved their lives. Some users highlighted alternative projects like SourceLibrary and discussed challenges such as cloudflare blocks and internet censorship. Overall sentiment was positive, with many viewing the bounty as a vital step for cultural preservation.

**Tags**: `#digital preservation`, `#open access`, `#annas-archive`, `#google-books`, `#piracy`

---

<a id="item-2"></a>
## [YouTube Private Videos Leaked via Prompt Injection](https://javoriuski.com/post/youtube) ⭐️ 9.0/10

A security researcher discovered that attackers can leak YouTube creators' private or unlisted videos by exploiting prompt injection in YouTube Studio's AI-powered comment summarization feature, which treats malicious comments as system instructions. This vulnerability exposes private content that creators intended to keep confidential, potentially leading to severe privacy breaches. It highlights the growing security risks of AI integrations in widely-used platforms. The attack requires the creator to click a suggested AI prompt in YouTube Studio's comment tab, which then triggers the injection. The researcher reported the issue to Google but it was initially closed as 'won't fix' before being reopened.

hackernews · javxfps · Jul 4, 16:45 · [Discussion](https://news.ycombinator.com/item?id=48786781)

**Background**: Prompt injection is a security vulnerability where attackers craft inputs that trick AI language models into ignoring their intended instructions and following attacker commands instead. In this case, YouTube's AI comment summarizer was manipulated to include attacker-controlled content, which could include links or instructions that leak private video titles or other sensitive information.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>
<li><a href="https://owasp.org/www-community/attacks/PromptInjection">Prompt Injection - OWASP Foundation</a></li>
<li><a href="https://blog.cyberdesserts.com/prompt-injection-attacks/">Prompt Injection Attacks: Examples and Defences</a></li>

</ul>
</details>

**Discussion**: Community reactions included appreciation for the clear write-up, with one user noting the article's quality compared to typical disclosures. A former Google employee explained why the bug might have been mishandled internally. Another user attempted to reproduce the exploit but was unsuccessful with their limited setup.

**Tags**: `#security`, `#YouTube`, `#prompt injection`, `#vulnerability`, `#infosec`

---

<a id="item-3"></a>
## [Microsoft Agent Governance Toolkit for Secure AI Agents](https://github.com/microsoft/agent-governance-toolkit) ⭐️ 9.0/10

Microsoft has released the Agent Governance Toolkit, an open-source toolkit that provides policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. It claims to cover all 10 items of the OWASP Agentic Top 10 security risks. As AI agents become more autonomous in production, governance and security are critical to prevent abuse and failures. This toolkit provides a standardized approach to enforce security policies, making it easier for developers to deploy agents safely. The toolkit supports multiple package managers including PyPI, npm, and NuGet, and is licensed under MIT. It is compliant with the OWASP Agentic Top 10 and the AARM (Agentic AI Risk Management) framework.

rss · GitHub Trending - Python Daily · Jul 4, 01:39

**Background**: The OWASP Agentic Top 10 is a globally peer-reviewed framework that identifies critical security risks for autonomous AI agents, such as identity and privilege abuse. AI agents are autonomous programs that can perform tasks on behalf of users, and securing them is increasingly important as they are deployed in enterprise environments.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/OWASP_Top_10_for_Agentic_Applications_2026">OWASP Top 10 for Agentic Applications 2026</a></li>
<li><a href="https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/">OWASP Top 10 for Agentic Applications for 2026</a></li>
<li><a href="https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/">OWASP Top 10 for Agentic Applications - The Benchmark for ...</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#agent security`, `#zero-trust`, `#OWASP agentic top 10`, `#Microsoft`

---

<a id="item-4"></a>
## [World's first sub-10ms neural dynamical system chip based on phase-change memristors](https://www.ithome.com/0/972/680.htm) ⭐️ 9.0/10

A Chinese research team has developed the world's first sub-10-millisecond neural dynamical system chip using phase-change memristors, achieving a single-step iteration latency of 2.12 ms. The work was published in Science on July 5, 2026. This breakthrough solves a 50-year-old latency bottleneck in neural dynamical systems, enabling real-time high-fidelity brain modeling and advancing brain-computer interfaces. Compared to NVIDIA A100 GPUs, the chip achieves up to 478x speedup in brain cortex reconstruction tasks. The chip is manufactured in a 40nm process, with in-memory computing and step-size drift array occupying only 0.28 mm². It operates at 50 MHz with a 9-stage pipeline, delivering 2.12 ms per iteration while reducing power consumption by 11.75–24.73× compared to state-of-the-art ASICs.

rss · IT之家 · Jul 4, 23:07

**Background**: Neural dynamical systems combine neural networks with differential equations to model continuous physical processes, but have long suffered from high latency in hardware implementation. Phase-change memristors are non-volatile memory devices that can store and compute simultaneously, enabling in-memory computing. The key challenge was achieving controllable in-memory computation with phase-change memristors due to conductance drift and multi-level characteristics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Phase-change_memory">Phase-change memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/In-memory_computing">In-memory computing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dynamical_neuroscience">Dynamical neuroscience - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#neuromorphic computing`, `#phase-change memristors`, `#neural dynamics`, `#hardware`, `#research breakthrough`

---

<a id="item-5"></a>
## [Chinese astronomers find strongest evidence for intermediate-mass black hole in Milky Way](https://www.ithome.com/0/972/672.htm) ⭐️ 9.0/10

A team led by Dr. Zheng Xiaochen from Beijing Planetarium used numerical simulations to provide the strongest dynamical evidence yet for an intermediate-mass black hole (IMBH) lurking near the center of the Milky Way, as published in The Astrophysical Journal on June 29, 2025. This finding fills a crucial missing link in black hole evolution, bridging stellar-mass and supermassive black holes, and could reshape our understanding of galactic formation and dynamics. The team simulated three groups of young stars near Sagittarius A* and found that only a gravitational source about 10,000 solar masses could explain their orbits. The candidate IMBH may reside within the IRS 13 star cluster.

rss · IT之家 · Jul 4, 15:02

**Background**: Black holes come in three main types: stellar-mass (up to ~100 solar masses), supermassive (millions to billions solar masses), and intermediate-mass (100 to 100,000 solar masses), which are thought to be the missing link between the two extremes. IMBHs are extremely rare and hard to detect; only a few candidates have been proposed. The study used the open-source N-body code PeTar on high-performance computing platforms to simulate stellar dynamics over millions of years.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lwang-astro/PeTar">GitHub - lwang-astro/PeTar: PeTar is a high-performance N-body code for modelling the evolution of star clusters and tidal streams, including the effect of galactic potential, dynamics of binary and hierarchical system, single and binary stellar evolution. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Intermediate-mass_black_hole">Intermediate-mass black hole</a></li>
<li><a href="https://science.nasa.gov/universe/black-holes/types/">Black Hole Types - NASA Science</a></li>

</ul>
</details>

**Tags**: `#astrophysics`, `#black holes`, `#Milky Way`, `#numerical simulation`, `#astronomy`

---

<a id="item-6"></a>
## [First Synthetic Cell with Complete Lifecycle Created](https://www.ithome.com/0/972/615.htm) ⭐️ 9.0/10

Researchers at the University of Minnesota have created SpudCell, the first synthetic cell built entirely from non-living chemical components that can grow, divide, and pass DNA to offspring. This breakthrough demonstrates that core life processes can be engineered chemically without relying on natural organisms, opening new possibilities for programmable bioengineering in drug manufacturing, materials science, and industrial chemistry. SpudCell's genome is only 90 kilobase pairs (kbp) across seven plasmids, with 36 purified enzymes and a lipid membrane, yet it can grow via fusion with nutrient-carrying liposomes and divide using membrane protein stress rather than a cytoskeleton.

rss · IT之家 · Jul 4, 09:36

**Background**: Synthetic biology aims to construct artificial cells from scratch using bottom-up approaches, assembling non-living molecules into cell-like systems. Previous minimal genome estimates suggested at least 113 kbp were necessary for a living cell, but SpudCell operates with 90 kbp. This work contrasts with top-down methods that simplify existing organisms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpudCell">SpudCell - Wikipedia</a></li>
<li><a href="https://biotic.org/research/spudcell/">Biotic | SpudCell</a></li>
<li><a href="https://www.science.org/content/article/lab-created-spudcell-marks-major-step-toward-building-life-scratch">Lab-created ‘SpudCell’ marks ‘stunning’ step toward building life from scratch | Science | AAAS</a></li>

</ul>
</details>

**Tags**: `#synthetic biology`, `#artificial cells`, `#synthetic genomics`, `#bottom-up biology`, `#biotechnology`

---

<a id="item-7"></a>
## [Better Models: Worse Tool Calling](https://simonwillison.net/2026/Jul/4/better-models-worse-tools/#atom-everything) ⭐️ 8.0/10

Newer Anthropic Claude models (Opus 4.8 and Sonnet 5) have been observed to invent extra fields in tool call arguments, causing third-party coding harnesses like Pi to reject valid edits and request retries. This regression in tool-calling reliability undermines the promise of increasingly capable AI coding assistants and forces developers to choose between model performance and tool compatibility. The issue appears specifically in Anthropic's latest flagship models (Opus 4.8 and Sonnet 5) but not in older models, suggesting that reinforcement learning training optimized for Claude Code's built-in edit tool may inadvertently degrade performance on custom tool schemas.

rss · Simon Willison · Jul 4, 22:53

**Background**: Tool calling is a key capability for LLMs used in coding assistants, allowing models to invoke functions with specific parameters. Third-party tools like Pi define their own tool schemas, which the model must adhere to exactly. The introduction of model-specific built-in tools (e.g., Claude's search-replace editor, OpenAI's apply_patch) can create a mismatch when models over-learn those proprietary patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://machinelearningmastery.com/mastering-llm-tool-calling-the-complete-framework-for-connecting-models-to-the-real-world/">Mastering LLM Tool Calling: The Complete Framework for ...</a></li>
<li><a href="https://www.braincuber.com/blog/reliable-tool-calling-ai-agents-schema-validation-recovery">Reliable Tool Calling for AI Agents: Fix Bad Calls</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#tool use`, `#Anthropic Claude`, `#software engineering`, `#AI reliability`

---

<a id="item-8"></a>
## [actions/checkout v7: Safer fork PR handling and ESM migration](https://github.com/actions/checkout) ⭐️ 8.0/10

GitHub's actions/checkout v7 now refuses to check out fork pull request code by default when triggered by pull_request_target or workflow_run, and has migrated the action codebase to ECMAScript Modules (ESM) for improved security and maintainability. This update addresses the common 'pwn request' vulnerability in GitHub Actions, which allowed attackers to gain write-level access by submitting malicious pull requests. The ESM migration modernizes the codebase and enables better dependency management. To opt in to the legacy behavior after reviewing the risks, set allow-unsafe-pr-checkout: true. The action also includes updated dependencies and security fixes, and continues to require a minimum Actions Runner version as specified in previous versions.

rss · GitHub Trending - Daily · Jul 4, 01:33

**Background**: The pull_request_target trigger runs workflows in the context of the base repository with access to secrets, making it a common target for 'pwn request' attacks. A pwn request is an attack where a malicious contributor submits a pull request whose code is executed in a privileged workflow, potentially exfiltrating secrets or gaining unauthorized access. actions/checkout is the most widely used GitHub Action for checking out repository code in CI/CD pipelines.

<details><summary>References</summary>
<ul>
<li><a href="https://www.endorlabs.com/learn/pwn-request-threat-a-hidden-danger-in-github-actions">PWN Request Threat: A Hidden Danger in GitHub Actions</a></li>
<li><a href="https://www.stepsecurity.io/blog/github-actions-pwn-request-vulnerability">GitHub Actions Pwn Request Vulnerability - StepSecurity</a></li>
<li><a href="https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows">Events that trigger workflows - GitHub Docs</a></li>

</ul>
</details>

**Tags**: `#GitHub Actions`, `#CI/CD`, `#security`, `#open source`, `#ESM`

---

<a id="item-9"></a>
## [Chrome DevTools MCP brings DevTools to AI coding agents](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Google has released chrome-devtools-mcp, an open-source MCP server that allows AI coding agents to control and inspect a live Chrome browser using Chrome DevTools. This integration bridges AI coding assistants with powerful browser debugging and automation capabilities, potentially improving the reliability and depth of AI-driven web development workflows. The tool uses Puppeteer for reliable automation and Chrome DevTools for performance tracing and network analysis; it collects usage statistics by default but allows opt-out via a flag.

rss · GitHub Trending - Daily · Jul 4, 01:33

**Background**: The Model Context Protocol (MCP) is an open standard that enables seamless integration between LLM applications and external tools. It standardizes how AI agents interact with data sources and services, reducing custom integration work. By acting as an MCP server, chrome-devtools-mcp gives AI assistants direct access to Chrome DevTools features.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://github.com/modelcontextprotocol">Model Context Protocol · GitHub</a></li>
<li><a href="https://cloud.google.com/discover/what-is-model-context-protocol">What is Model Context Protocol (MCP)? A guide | Google Cloud</a></li>

</ul>
</details>

**Tags**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#browser automation`, `#debugging`

---

<a id="item-10"></a>
## [Meta Open-Sources Astryx Design System](https://github.com/facebook/astryx) ⭐️ 8.0/10

Meta has open-sourced Astryx, a fully customizable design system with over 150 accessible React components built on StyleX, now available in beta. This release provides the development community with a mature, internally proven design system used in 13,000+ apps at Meta, offering high customization and agent-ready features that align with modern AI-assisted workflows. Astryx is built with React and StyleX but allows style overrides via className with any CSS method, includes a CLI for scaffolding and templating, and is designed for both human developers and AI agents.

rss · GitHub Trending - Daily · Jul 4, 01:33

**Background**: StyleX is a zero-runtime CSS-in-JS library developed by Meta that compiles styles at build time for performance. Astryx originated as Meta's internal design system over eight years and is now open-sourced to the community.

<details><summary>References</summary>
<ul>
<li><a href="https://stylexjs.com/docs/learn/">Introduction | StyleX | The styling system that powers Meta.</a></li>

</ul>
</details>

**Tags**: `#design system`, `#open source`, `#React`, `#StyleX`, `#UI components`

---

<a id="item-11"></a>
## [Harvard's CS249r Book: Open-Source ML Systems](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

Harvard's CS249r course has released an open-source book titled 'Machine Learning Systems: Principles and Practices of Engineering Artificially Intelligent Systems' on GitHub. This book provides a comprehensive, principled approach to engineering ML systems, filling a gap in educational resources for AI system design. Its multi-language support and active development make it accessible to a global audience. The repository includes tools like TinyTorch, Labs, Kits, and MLSys·im, and is licensed under CC-BY-NC-SA 4.0. It is actively maintained with automated validation workflows.

rss · GitHub Trending - Daily · Jul 4, 01:33

**Background**: Machine Learning Systems engineering focuses on the design, deployment, and maintenance of ML models in production, covering data pipelines, model serving, and monitoring. This area is often underemphasized compared to model development. Harvard's CS249r course addresses this by teaching both theory and practical skills needed to build robust AI systems.

**Tags**: `#machine learning`, `#systems engineering`, `#education`, `#AI`, `#book`

---

<a id="item-12"></a>
## [Anthropic Releases Claude Code: Open-Source Agentic Coding Tool](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic has open-sourced Claude Code, an agentic coding tool that operates directly in the terminal, allowing developers to understand codebases and execute tasks via natural language commands. This release lowers the barrier for developers to integrate an advanced AI coding agent into their workflow, potentially increasing productivity and code quality. As an open-source tool from a leading AI company, it could set new standards for agentic coding assistants. Claude Code supports installation via curl, Homebrew, WinGet, and NPM (deprecated), and includes plugins for extended functionality. It operates in the terminal, IDE, or via GitHub @claude tag, and collects usage data for feedback.

rss · GitHub Trending - Daily · Jul 4, 01:33

**Background**: Agentic coding tools are AI-powered systems that understand an entire codebase, plan implementations, and autonomously execute tasks like writing features, debugging, and refactoring. Claude Code is one such tool from Anthropic, designed to act in the terminal without leaving the developer's environment.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/blog/introduction-to-agentic-coding">Introduction to agentic coding | Claude by Anthropic</a></li>
<li><a href="https://code.claude.com/">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**Tags**: `#AI coding`, `#agentic tool`, `#terminal`, `#GitHub`, `#open source`

---

<a id="item-13"></a>
## [TencentCloud Releases CubeSandbox for AI Agent Security](https://github.com/TencentCloud/CubeSandbox) ⭐️ 8.0/10

TencentCloud has open-sourced CubeSandbox, an instant, concurrent, secure, and lightweight sandbox service for AI agents. Built on RustVMM and KVM, it can create a hardware-isolated sandbox in under 60ms with less than 5MB memory overhead. This provides a high-performance, hardware-level isolated execution environment for AI agents, addressing critical security and concurrency needs. It is compatible with the E2B SDK, making it easy to integrate into existing AI agent workflows, and is recognized in the CNCF landscape as an AI-native workload runtime. CubeSandbox supports both single-node deployment and scaling to multi-node clusters. Version 0.4.0 introduces CubeEgress, an egress gateway for credential injection, domain filtering, and access auditing, allowing agents to call external APIs without exposing keys inside the sandbox.

rss · GitHub Trending - Daily · Jul 4, 01:33

**Background**: AI agents often need to execute untrusted code or access external resources, posing security risks. A sandbox provides a secure, isolated environment to run such code without affecting the host system. Traditional sandboxes may be slow or insecure; CubeSandbox uses microVM technology (RustVMM and KVM) to achieve hardware-level isolation with fast startup and low overhead, making it suitable for production AI agent systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/TencentCloud/CubeSandbox">GitHub - TencentCloud/ CubeSandbox : Instant, Concurrent, Secure...</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor ...</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Sandbox`, `#Security`, `#Tencent Cloud`, `#Open Source`

---

<a id="item-14"></a>
## [NVlabs Releases ProtoMotions3 for Humanoid Simulation & Learning](https://github.com/NVlabs/ProtoMotions) ⭐️ 8.0/10

NVlabs has released ProtoMotions3, a GPU-accelerated simulation and learning framework for training physically simulated digital humans and humanoid robots, built on Newton physics and IsaacLab. This framework bridges animation, robotics, and reinforcement learning communities by providing a fast, scalable platform for humanoid research, with the ability to train motion skills from the entire AMASS dataset (40+ hours) in just 12 hours on 4 A100 GPUs. ProtoMotions3 is modular, extensible, and community-driven under the Apache-2.0 license, and integrates with text-to-motion generation via Kimodo to train physics-based policies for both the SOMA character and the Unitree G1 robot.

rss · GitHub Trending - Python Daily · Jul 4, 01:39

**Background**: ProtoMotions3 leverages the Newton physics engine, an open-source GPU-accelerated and differentiable simulation engine developed by NVIDIA, Google DeepMind, and Disney Research, and IsaacLab, a GPU-accelerated framework for robotics research. These technologies enable large-scale parallel simulation and reinforcement learning for humanoid agents.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVlabs/ProtoMotions">GitHub - NVlabs/ProtoMotions: ProtoMotions is a GPU ...</a></li>
<li><a href="https://developer.nvidia.com/newton-physics">Newton Physics Engine | NVIDIA Developer</a></li>
<li><a href="https://github.com/isaac-sim/IsaacLab">GitHub - isaac-sim/IsaacLab: Unified framework for robot ...</a></li>

</ul>
</details>

**Tags**: `#simulation`, `#robotics`, `#GPU`, `#humanoid`, `#framework`

---

<a id="item-15"></a>
## [Hugging Face Launches Low-Latency Speech-to-Speech Pipeline](https://github.com/huggingface/speech-to-speech) ⭐️ 8.0/10

Hugging Face has released a modular, low-latency speech-to-speech pipeline that allows developers to build voice agents using open-source models, exposed through an OpenAI Realtime-compatible WebSocket API. This tool democratizes voice agent development by enabling fully local, open-source stacks, reducing dependency on proprietary APIs and lowering costs for developers and startups. The pipeline consists of Voice Activity Detection (VAD), Speech-to-Text (STT), a Large Language Model (LLM), and Text-to-Speech (TTS), with every component being swappable; it is already used in production for thousands of Reachy Mini robots.

rss · GitHub Trending - Python Daily · Jul 4, 01:39

**Background**: Voice activity detection (VAD) distinguishes speech from silence or noise, while speech-to-text (STT) converts audio to text, and text-to-speech (TTS) generates speech from text. The OpenAI Realtime API enables low-latency, bidirectional audio interactions with AI models, and this pipeline provides an open-source alternative to that API.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Voice_activity_detection">Voice activity detection - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/tutorial/realtime-api-openai">OpenAI Realtime API : A Guide With Examples | DataCamp</a></li>

</ul>
</details>

**Tags**: `#speech-to-speech`, `#voice-agent`, `#open-source`, `#Hugging Face`, `#pipeline`

---

<a id="item-16"></a>
## [Vue 2 Reaches End of Life, Urging Upgrade to Vue 3](https://github.com/vuejs/vue) ⭐️ 8.0/10

The Vue 2 repository is now inactive as Vue 2 reached end of life on December 31, 2023. The project strongly recommends upgrading to Vue 3 and points to a migration guide. This marks a major milestone for the Vue ecosystem, as thousands of existing projects using Vue 2 must now plan migration or seek extended support. Teams that cannot upgrade immediately can turn to commercial support like HeroDevs' Never-Ending Support (NES). Vue 2 will no longer receive new features, updates, or fixes, but remains available on existing distribution channels. The migration guide and HeroDevs NES provide options for staying secure without upgrading.

rss · GitHub Trending - TypeScript Daily · Jul 4, 01:41

**Background**: Vue.js is a progressive JavaScript framework for building user interfaces. Vue 2 was widely adopted, but Vue 3 introduced breaking changes, better performance, and improved TypeScript support, making migration non-trivial but beneficial.

<details><summary>References</summary>
<ul>
<li><a href="https://www.herodevs.com/support/nes-vue">Vue 2 - Never-Ending Support (NES) | HeroDevs</a></li>
<li><a href="https://v2.vuejs.org/lts/">Vue 2 LTS, EOL & Extended Support Vue 2 Has Reached End of Life Vue - endoflife.date Vue.js Latest Version - Support Lifecycle & EOL Vue 2 Has Reached End of Life - GitHub</a></li>

</ul>
</details>

**Tags**: `#Vue`, `#JavaScript`, `#Framework`, `#End of Life`, `#Upgrade`

---

<a id="item-17"></a>
## [Alibaba Releases Page Agent for Natural Language Web Control](https://github.com/alibaba/page-agent) ⭐️ 8.0/10

Alibaba has open-sourced Page Agent, a JavaScript library that allows users to control web interfaces using natural language commands directly in the browser. This simplifies web automation and accessibility, enabling developers to integrate AI-powered copilots, smart form filling, and voice-controlled interfaces without backend changes or browser extensions. Page Agent works by text-based DOM manipulation, avoiding the need for screenshots or multimodal LLMs, and supports optional Chrome extension for multi-page tasks and an MCP Server for external control.

rss · GitHub Trending - TypeScript Daily · Jul 4, 01:41

**Background**: GUI agents that automate web tasks typically require browser extensions, Python scripts, or headless browsers. Page Agent is a lightweight in-page JavaScript solution that runs entirely within the user's tab, using only a text map of the DOM for the LLM to understand the page structure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.remio.ai/post/alibaba-releases-page-agent-open-source-javascript-library-for-natural-language-webpage-dom-control">Alibaba Releases Page Agent Open Source JavaScript Library for...</a></li>
<li><a href="https://openapps.pro/apps/page-agent">Page Agent : Natural Language GUI Automation for Web Apps</a></li>

</ul>
</details>

**Tags**: `#natural language`, `#browser automation`, `#GUI agent`, `#TypeScript`, `#Alibaba`

---

<a id="item-18"></a>
## [Bun: A fast all-in-one JavaScript runtime and toolkit](https://github.com/oven-sh/bun) ⭐️ 8.0/10

Bun is a new JavaScript runtime, bundler, test runner, and package manager combined into a single executable, offering significant performance improvements over existing tools like Node.js. Bun simplifies the JavaScript development toolchain by replacing multiple tools with one fast alternative, reducing complexity and startup times, which could improve developer productivity and adoption in the ecosystem. Bun is written in Rust and uses Apple's JavaScriptCore engine instead of V8, enabling faster startup and lower memory usage. It supports TypeScript and JSX out of the box and can be used as a drop-in replacement for Node.js in most projects.

rss · GitHub Trending - Rust Daily · Jul 4, 01:39

**Background**: JavaScript runtimes like Node.js and Deno execute JavaScript code outside a browser. Node.js, built on Chrome's V8 engine, is widely used but has slower startup and higher memory usage. Bun aims to solve this by using JavaScriptCore and a more integrated approach, bundling common developer tools into one binary.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>

</ul>
</details>

**Tags**: `#JavaScript`, `#runtime`, `#bundler`, `#package-manager`, `#Rust`

---

<a id="item-19"></a>
## [NVIDIA OpenShell: Sandboxed Runtime for Autonomous AI Agents](https://github.com/NVIDIA/OpenShell) ⭐️ 8.0/10

NVIDIA has released OpenShell, an open-source sandboxed runtime for autonomous AI agents, announced as an alpha on GitHub. It enforces declarative YAML policies to prevent unauthorized file access, data exfiltration, and uncontrolled network activity. OpenShell addresses critical safety and privacy concerns in deploying AI agents by providing kernel-level isolation, enabling safer adoption in enterprise environments. As a major player like NVIDIA enters this space, it signals standardization of secure agent runtimes. OpenShell supports macOS, Windows with WSL 2, and Linux, with Docker, Podman, or MicroVM-backed sandboxes. It includes agent skills for troubleshooting and policy generation, and a Helm chart for Kubernetes deployment is available experimentally.

rss · GitHub Trending - Rust Daily · Jul 4, 01:39

**Background**: Autonomous AI agents require isolated environments to safely execute code and access resources. Sandboxed runtimes like OpenShell provide security boundaries enforced through policies, preventing malicious or erroneous actions. NVIDIA's offering leverages kernel-level isolation and declarative YAML configuration, similar to container security models but tailored for agent workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVIDIA/OpenShell">GitHub - NVIDIA/OpenShell: OpenShell is the safe, private ...</a></li>
<li><a href="https://docs.nvidia.com/openshell/home">NVIDIA OpenShell Developer Guide</a></li>
<li><a href="https://grokipedia.com/page/NVIDIA_OpenShell">NVIDIA OpenShell</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#security`, `#sandbox`, `#NVIDIA`, `#runtime`

---

<a id="item-20"></a>
## [Prometheus Monitoring System GitHub Repository Overview](https://github.com/prometheus/prometheus) ⭐️ 8.0/10

The Prometheus GitHub repository provides the source code, documentation, and installation instructions for the Prometheus monitoring system and time series database, a CNCF graduated project. Prometheus is a critical infrastructure component for observability in cloud-native environments, widely adopted for its multi-dimensional data model and powerful PromQL query language. The repository includes CI/CD badges, Docker images on Quay and Docker Hub, Go Report Card, and security scorecards, reflecting high code quality and active maintenance.

rss · GitHub Trending - Go Daily · Jul 4, 01:36

**Background**: Prometheus is an open-source systems monitoring and alerting toolkit originally built at SoundCloud and later donated to the Cloud Native Computing Foundation. It features a multi-dimensional time series data model, a flexible query language (PromQL), and a pull-based metric collection approach. Prometheus is often used in conjunction with Grafana for visualization and Alertmanager for alerting.

**Tags**: `#monitoring`, `#time-series`, `#prometheus`, `#observability`, `#devops`

---

<a id="item-21"></a>
## [Nuclei: Fast, Community-Powered Vulnerability Scanner](https://github.com/projectdiscovery/nuclei) ⭐️ 8.0/10

Nuclei is a high-performance vulnerability scanner that uses a simple YAML-based DSL to define custom detection templates, and it is powered by a global community of security professionals. Nuclei enables security teams to quickly identify and remediate vulnerabilities across applications, APIs, networks, and cloud configurations with zero false positives by simulating real-world exploitation steps. It supports multiple protocols including TCP, DNS, HTTP, SSL, WHOIS, and JavaScript, and integrates seamlessly into CI/CD pipelines for automated vulnerability detection and regression testing.

rss · GitHub Trending - Go Daily · Jul 4, 01:36

**Background**: Vulnerability scanners traditionally rely on hard-coded checks, which are difficult to customize and maintain. Nuclei introduces a flexible YAML-based template system that allows anyone to write and share detection rules for emerging threats, fostering rapid community collaboration.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/projectdiscovery/nuclei">projectdiscovery/ nuclei : Nuclei is a fast, customizable vulnerability ...</a></li>
<li><a href="https://projectdiscovery.io/nuclei">Nuclei Community-powered vulnerability scanning — ProjectDiscovery</a></li>
<li><a href="https://github.com/VBPush/nuclei_-">GitHub - VBPush/nuclei_-: Fast and customizable vulnerability ...</a></li>

</ul>
</details>

**Tags**: `#vulnerability scanning`, `#security`, `#open source`, `#Go`, `#DevSecOps`

---

<a id="item-22"></a>
## [Google Releases Open-Source Go ADK for AI Agents](https://github.com/google/adk-go) ⭐️ 8.0/10

Google has open-sourced ADK Go, a code-first toolkit for building, evaluating, and deploying AI agents in Go. Version 2.0 introduces graph-based workflow agents, parallel and loop execution primitives, and human-in-the-loop tool confirmation. This release brings enterprise-grade AI agent development to the Go ecosystem, leveraging Go's concurrency and performance for cloud-native applications. It provides a model-agnostic, deployment-agnostic framework that competes with Python and Java agent frameworks, expanding options for developers. ADK Go is optimized for Gemini but supports any model, and is deployable anywhere including Google Cloud Run. It includes pre-built tools, custom function integration, and modular multi-agent system design. The package is available via `go get google.golang.org/adk/v2` under Apache 2.0 license.

rss · GitHub Trending - Go Daily · Jul 4, 01:36

**Background**: AI agent development kits provide frameworks for building autonomous software agents that can plan, use tools, and execute tasks. Google's ADK family (Python, Java, Go, TypeScript) unifies agent development with code-first principles. Go's strengths in performance and concurrency make it suitable for high-throughput agent applications, especially in cloud-native environments.

<details><summary>References</summary>
<ul>
<li><a href="https://adk.dev/get-started/go/">Go - Agent Development Kit (ADK)</a></li>
<li><a href="https://adk.dev/">Agent Development Kit (ADK)</a></li>
<li><a href="https://github.com/google/adk-go">GitHub - google/adk-go: An open-source, code-first Go toolkit ...</a></li>

</ul>
</details>

**Tags**: `#Go`, `#AI Agents`, `#Google`, `#Open Source`, `#Toolkit`

---

<a id="item-23"></a>
## [Micron's SCAs lock high memory prices until 2030, no drop before 2031](https://www.v2ex.com/t/1224905) ⭐️ 8.0/10

Micron has signed 16 Strategic Customer Agreements (SCAs) covering 2026 to 2030, which set a floor price at historically high gross margins, effectively locking in elevated memory prices for at least five years. This suggests consumers should not expect significant memory price drops until at least 2031. This development breaks the traditional cyclical pattern of memory pricing, where prices typically fall after supply increases. Consumers and businesses may face persistently high costs for DRAM and NAND, impacting PC upgrades, server deployments, and the entire hardware ecosystem. The SCAs include a pricing band with both a floor and a ceiling, protecting buyers from further price spikes while guaranteeing Micron a minimum profit margin. The agreements span multiple market segments including data center, consumer, and automotive, with General Motors recently signing one as well.

rss · V2EX-最热主题 · Jul 4, 03:53

**Background**: Memory prices have historically been cyclical, driven by supply-demand imbalances. When demand weakens or supply expands, prices often fall sharply. Micron's SCAs represent a shift toward long-term fixed pricing, which reduces volatility for both suppliers and large customers but eliminates the usual downturn phase that benefits consumers.

<details><summary>References</summary>
<ul>
<li><a href="https://investors.micron.com/news-releases/news-release-details/micron-and-general-motors-sign-strategic-agreement-secure-supply">Micron and General Motors Sign Strategic Agreement to Secure ...</a></li>

</ul>
</details>

**Tags**: `#memory`, `#pricing`, `#Micron`, `#hardware`, `#supply chain`

---

<a id="item-24"></a>
## [China proposes banning unauthorized bypass of state technical measures](https://www.nodeseek.com/post-807594-1) ⭐️ 8.0/10

China's Cyberspace Administration released a revised draft of the Internet Information Service Management Measures for public comment, explicitly prohibiting activities that 'illegally penetrate or bypass technical measures of relevant state agencies,' with fines ranging from 100,000 to 5 million yuan. This regulation directly targets VPNs, circumvention tools, and other methods used to bypass China's internet censorship, imposing severe penalties on violators. It signals a further tightening of internet controls and could significantly impact both domestic users and foreign companies operating in China. Compared to the current regulations, the revised draft simplifies 'bad information' to 'speculating on major policy decisions,' and penalties include both fines and business suspension. Violations with serious circumstances can incur fines up to 5 million yuan.

rss · NodeSeek · Jul 4, 23:11

**Background**: China has long maintained a system of internet censorship known as the 'Great Firewall,' using technical measures to block access to foreign websites and services. 'Technical measures' refer to methods like IP blocking, DNS poisoning, and DPI used to control internet traffic. The term 'bypassing' typically refers to using VPNs, proxies, or other tools to access blocked content, which has been increasingly criminalized in recent years.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cac.gov.cn/2026-07/03/c_1784822399677167.htm">国家互联网信息办公室关于《互联网信息服务管理办法（修订草案征求意...</a></li>
<li><a href="https://wenku.baidu.com/view/830e9eedfeb069dc5022aaea998fcc22bcd14326.html">互联网信息服务管理办法 (2025版) - 百度文库</a></li>
<li><a href="https://www.clausiuspress.com/assets/default/article/2024/10/01/article_1727797305.pdf">Definition of technical measures to circumvent the ...</a></li>

</ul>
</details>

**Tags**: `#internet regulation`, `#China`, `#censorship`, `#cybersecurity`

---

<a id="item-25"></a>
## [AI Data Centers' Indirect Water Use Far Exceeds Reported Amounts](https://www.ithome.com/0/972/689.htm) ⭐️ 8.0/10

A new analysis reveals that AI data centers' indirect water consumption from power generation is roughly 12 times their direct on-site water use, yet most tech giants only report direct use, with only Meta including indirect use in their sustainability reports. This hidden water footprint raises concerns about resource competition in water-scarce regions, especially as data center expansion accelerates. The lack of complete disclosure could undermine sustainability efforts and public trust. The analysis by Lawrence Berkeley National Laboratory found that indirect water use for U.S. data centers historically averages 12 times direct use. Tech giants like Google, Amazon, and Microsoft only report direct water use, while Meta reports both, with indirect use over 20 times direct in 2024.

rss · IT之家 · Jul 4, 23:50

**Background**: Data centers require significant water for cooling servers, but the electricity they consume also requires water for power plant cooling and other processes. Power plants using coal or nuclear consume more water than natural gas, while renewable sources like solar and wind use minimal water. Many tech giants purchase renewable energy certificates to offset their electricity use, but these do not account for local water impacts.

<details><summary>References</summary>
<ul>
<li><a href="https://www.eia.gov/todayinenergy/detail.php?id=56820">U.S. electric power sector continues water efficiency gains ...</a></li>
<li><a href="https://www.publicpower.org/periodical/article/how-much-water-our-electricity-uses">How Much Water Our Electricity Uses - Public Power</a></li>
<li><a href="https://en.wikipedia.org/wiki/Renewable_Energy_Certificate_(United_States)">Renewable Energy Certificate (United States)</a></li>

</ul>
</details>

**Tags**: `#AI data centers`, `#water consumption`, `#sustainability`, `#tech giants`, `#environmental impact`

---

<a id="item-26"></a>
## [Tesla Robotaxi Launches in Miami Without Safety Drivers](https://www.ithome.com/0/972/678.htm) ⭐️ 8.0/10

Tesla's Robotaxi service has expanded to a small area in western Miami, operating without in-car safety drivers. This follows similar launches in Dallas and Houston earlier this year. This expansion demonstrates Tesla's progress in deploying fully autonomous ride-hailing without safety drivers, intensifying competition with Waymo and Zoox in the Miami market. It also validates Tesla's approach of using consumer vehicles with FSD software for robotaxi operations. Tesla avoided Miami's busy downtown area for the initial launch, similar to its strategy in Texas cities. The company's Robotaxi fleet size reached 200 vehicles as of January 2026, and testing without safety drivers is ongoing.

rss · IT之家 · Jul 4, 22:51

**Background**: Tesla Robotaxi is a ride-hailing service that uses Tesla vehicles equipped with Full Self-Driving (FSD) software. The service launched in a limited capacity in Austin, Texas, on June 22, 2025. In Austin, vehicles operate without a safety driver when not on highways, while in the Bay Area, a safety supervisor is required in the driver's seat. Competitors like Waymo and Zoox are also operating autonomous ride-hailing services in various cities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Robotaxi">Tesla Robotaxi - Wikipedia</a></li>
<li><a href="https://www.tesla.com/robotaxi">Robotaxi - Tesla</a></li>

</ul>
</details>

**Discussion**: Some users on X (formerly Twitter) shared that they have already ridden in the unsupervised Robotaxi in Miami. The general sentiment appears positive, with users reporting successful autonomous rides without safety drivers, though the sample is limited.

**Tags**: `#Tesla`, `#Robotaxi`, `#autonomous driving`, `#Waymo`, `#Miami`

---

<a id="item-27"></a>
## [Immune Cells Use Neurotransmitters to Communicate](https://www.ithome.com/0/972/656.htm) ⭐️ 8.0/10

German researchers have demonstrated for the first time in real time that human neutrophils, a type of immune cell, can take up, store, and release catecholamine neurotransmitters (including dopamine and adrenaline) similarly to neurons, using fluorescent carbon nanotube sensors. This discovery reveals a direct signaling pathway between the immune and nervous systems, fundamentally changing our understanding of inflammation regulation and potentially opening new therapeutic targets for inflammatory diseases. The team used highly sensitive fluorescent carbon nanotube sensors to visualize neurotransmitter release from single living cells, and confirmed the mechanism in healthy volunteers under induced inflammation. Released catecholamines inhibit neutrophil overactivity while promoting blood coagulation, linking immune and vascular systems.

rss · IT之家 · Jul 4, 13:19

**Background**: Catecholamines (e.g., dopamine, adrenaline) are neurotransmitters and hormones traditionally associated with the nervous and endocrine systems, mediating 'fight-or-flight' responses. Neutrophils are the most abundant white blood cells and the first responders to infection. Fluorescent carbon nanotube sensors are novel nanoscale probes that emit near-infrared light upon binding specific molecules, allowing real-time tracking of cellular processes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Catecholamine">Catecholamine - Wikipedia</a></li>
<li><a href="https://www.medicalnewstoday.com/articles/catecholamines">Catecholamines: What are they, and how do they function?</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/full/10.1002/anie.202112372">Biosensing with Fluorescent Carbon Nanotubes</a></li>

</ul>
</details>

**Tags**: `#immunology`, `#neuroscience`, `#neuroimmunology`, `#cell signaling`

---

<a id="item-28"></a>
## [Anthropic Enters Drug R&D, Targets Neglected Diseases](https://www.ithome.com/0/972/606.htm) ⭐️ 8.0/10

Anthropic launched Claude Science, a new AI workbench for scientists, and announced its own drug discovery program targeting neglected diseases, marking a rare direct entry by a leading AI firm into pharmaceutical R&D. This move could accelerate drug discovery for diseases that lack commercial incentives, while demonstrating AI's potential beyond providing tools to actually driving scientific breakthroughs. It also signals increased competition in AI-driven biotech. Claude Science integrates research tools and datasets, and was shown to detect a virus contamination in minutes that a UCSF research team missed for a year. The platform also analyzed 100 rare genetic diseases in under an hour, identifying 32 candidates for further screening.

rss · IT之家 · Jul 4, 08:36

**Background**: AI is increasingly used in drug discovery to accelerate candidate identification and optimization, but no fully AI-designed drug has yet passed all clinical trials. Neglected diseases are conditions that lack sufficient R&D investment from large pharma due to limited profitability, creating a public health gap.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science , an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/solutions/life-sciences">Life sciences | Claude by Anthropic</a></li>
<li><a href="https://huntscreens.com/products/claude-science">Claude Science : AI-Powered Research Environment for Scientists</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#AI drug discovery`, `#Claude Science`, `#neglected diseases`, `#AI in science`

---

<a id="item-29"></a>
## [BaryGraph redefines relationships as embedded documents](https://www.reddit.com/r/MachineLearning/comments/1un3lsf/barygraph_knowledge_graph_where_every/) ⭐️ 8.0/10

BaryGraph introduces BaryEdges, where every relationship in a knowledge graph is a first-class embedded document with its own vector, instead of a simple edge between nodes. It also constructs MetaBary triads by recursively stacking BaryEdges to capture structural bridges between distant concepts. This approach could significantly improve cross-domain retrieval in RAG systems by surfacing connections that flat vector search misses, potentially enabling more intelligent knowledge discovery. It challenges the conventional node-edge model of knowledge graphs and offers a new paradigm for representing relational information. BaryGraph runs locally using MongoDB Community, mongot, and nomic-embed-text, processing the full English Wiktionary (6.6M documents) in 8–14 hours on a single workstation with 8–16GB VRAM. The preprint and benchmark CSVs are available on Zenodo at the provided DOI.

reddit · r/MachineLearning · /u/adseipsum · Jul 4, 08:24

**Background**: Traditional knowledge graphs represent relationships as edges connecting nodes, and retrieval relies on vector similarity between node embeddings. BaryGraph reifies relationships as independent documents (BaryEdges) with their own embeddings, allowing them to be retrieved and linked hierarchically through MetaBary triads.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mongodb/mongot">GitHub - mongodb/mongot: MongoDB Search</a></li>

</ul>
</details>

**Tags**: `#knowledge graphs`, `#embeddings`, `#RAG`, `#machine learning`, `#semantic search`

---

<a id="item-30"></a>
## [Google Bans AI Jailbreaking and Prediction Markets in Chrome Extensions](https://developer.chrome.com/blog/cws-policy-updates-2026) ⭐️ 8.0/10

On July 1, 2026, Google announced updated Chrome Web Store developer policies that will take effect on August 1, 2026, banning excessive data collection, prediction markets with real money, and extensions designed for AI jailbreaking. This policy shift strengthens user privacy and AI safety by restricting data misuse and preventing unregulated gambling or manipulation of AI services. Developers must now ensure their extensions collect only strictly necessary data and avoid prohibited functionalities. Extensions may only collect data that is 'strictly necessary' for their stated purpose and must prominently disclose all data collection; if data handling changes after installation, developers must notify users. Prediction markets enabling real-money trading on event outcomes and extensions that bypass AI safety guardrails are explicitly forbidden.

telegram · zaihuapd · Jul 4, 06:30

**Background**: AI jailbreaking refers to techniques that circumvent the safety measures of AI models, such as causing a chatbot to ignore its restrictions. Prediction markets are exchanges where participants trade contracts based on the outcomes of future events, like elections or sports. The Chrome Web Store policies govern how extensions are distributed and must comply with developer program rules to ensure security and privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prediction_market">Prediction market - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/ai-jailbreaking-what-why-matters-how-stay-safe-simple-mehul-patel-2xdpc">AI Jailbreaking : What It Is, Why It Matters, and How to Stay Safe...</a></li>
<li><a href="https://developer.chrome.com/docs/extensions/get-started">Extensions / Get started | Chrome for Developers</a></li>

</ul>
</details>

**Tags**: `#chrome extensions`, `#privacy`, `#ai safety`, `#policy`, `#chrome web store`

---

<a id="item-31"></a>
## [iOS 27 Introduces Trust Insights On-Device Fraud Detection](https://www.cultofmac.com/news/ios-27-trust-insights-feature) ⭐️ 8.0/10

Apple announced Trust Insights, a new on-device fraud detection framework in iOS 27 that analyzes user behavior patterns, timing, context, and sensor data to identify potential scam coaching, and can trigger warnings, delays, or additional authentication before payments. This feature addresses social engineering scams that trick users into performing actions themselves, which are notoriously hard to detect automatically, while preserving privacy by processing data entirely on-device. It could significantly reduce financial fraud on iOS without compromising user privacy. Trust Insights does not read messages, emails, or photos; raw data is immediately discarded and only a single output value is sent to servers. The feature can be turned off but includes a cooling-off period before changes take effect, preventing scammers from tricking users into disabling it during a call.

telegram · zaihuapd · Jul 4, 14:30

**Background**: Social engineering scams, such as fake tech support or bank impersonation, often involve scammers coercing victims into transferring money or changing account settings while on the phone. Traditional fraud detection relies on server-side analysis of transactions, but struggles when the victim is willingly performing actions under instruction. Trust Insights uses on-device AI to detect behavioral anomalies that indicate coercion, without exposing private communication content.

<details><summary>References</summary>
<ul>
<li><a href="https://9to5mac.com/2026/07/02/ios-27-helps-apps-detect-when-a-user-may-be-getting-scammed-in-real-time/">iOS 27 helps apps detect when a user may be getting... - 9to5Mac</a></li>
<li><a href="https://applemagazine.com/ios-27-trust-insights/">iOS 27 Trust Insights Helps Apps Detect Scam... - AppleMagazine</a></li>
<li><a href="https://hoploninfosec.com/ios-27-trust-insights-scam-detection-framework">iOS 27 Trust Insights: Apple's New Scam Shield</a></li>

</ul>
</details>

**Tags**: `#iOS`, `#fraud detection`, `#privacy`, `#Apple`, `#security`

---

<a id="item-32"></a>
## [South Korea to invest 800 trillion KRW in semiconductor cluster, aiming to double DRAM output](https://t.me/zaihuapd/42357) ⭐️ 8.0/10

South Korea's Minister of Trade, Industry and Energy announced a national semiconductor cluster plan, which includes building a second semiconductor base in the southwestern region and attracting 800 trillion KRW investment for four memory fabs, with a goal to double DRAM production within five years. This massive government-led investment signals South Korea's determination to maintain its lead in global memory chip market, especially as competitors like China and the US ramp up semiconductor self-sufficiency. The plan could reshape the global DRAM supply chain and intensify competition. The investment of 800 trillion KRW (about 3.52 trillion RMB) will be used to build four memory wafer fabs, and the government will additionally inject 30 trillion KRW over 15 years. The minister predicted the global memory market could grow more than fourfold in five years.

telegram · zaihuapd · Jul 4, 15:15

**Background**: South Korea is a global leader in DRAM and NAND flash memory, with companies like Samsung and SK Hynix dominating the market. The semiconductor industry is a cornerstone of South Korea's economy, accounting for a significant share of exports. This cluster plan is part of the government's broader strategy to secure technological independence and respond to global supply chain uncertainties.

**Tags**: `#semiconductor`, `#DRAM`, `#South Korea`, `#investment`, `#industrial policy`

---