---
layout: default
title: "Horizon Summary: 2026-07-14 (EN)"
date: 2026-07-14
lang: en
---

> From 298 items, 27 important content pieces were selected

---

1. [Cursor 0day: Full Disclosure After 6 Months of Silence](#item-1) ⭐️ 9.0/10
2. [Rust Rewrite of PostgreSQL Passes All 46k+ Regression Tests](#item-2) ⭐️ 9.0/10
3. [Ollama Expands Local LLM Support with New Models](#item-3) ⭐️ 9.0/10
4. [Fields Medal 2026 Winners Leaked; Two Chinese Mathematicians Named](#item-4) ⭐️ 9.0/10
5. [Bonsai 27B: 27B-Parameter AI Model Runs on a Phone](#item-5) ⭐️ 8.0/10
6. [AI agents worsen coordination in large software projects](#item-6) ⭐️ 8.0/10
7. [How to stop Claude from overusing 'load-bearing' phrases](#item-7) ⭐️ 8.0/10
8. [Are We Offloading Too Much Thinking to AI?](#item-8) ⭐️ 8.0/10
9. [Linux Input Latency Measured: X11 vs Wayland, VRR, DXVK](#item-9) ⭐️ 8.0/10
10. [Lobste.rs Migrates from MariaDB to SQLite, Cuts Costs](#item-10) ⭐️ 8.0/10
11. [Friction Builds Shared Understanding in Software Projects](#item-11) ⭐️ 8.0/10
12. [Manim: Animation Engine for Explanatory Math Videos](#item-12) ⭐️ 8.0/10
13. [HeyGen releases HyperFrames: open-source HTML-to-video tool for AI agents](#item-13) ⭐️ 8.0/10
14. [Nushell: A Modern Shell in Rust Gains Traction](#item-14) ⭐️ 8.0/10
15. [InfluxDB 3 Core: Open Source Time Series Database with Apache Arrow](#item-15) ⭐️ 8.0/10
16. [Plano: AI-Native Proxy for Agentic Apps](#item-16) ⭐️ 8.0/10
17. [Samsung Flex Titanium: Titanium Alloy Reinforces Foldable Screens](#item-17) ⭐️ 8.0/10
18. [IBM Warns AI Infrastructure Boom Squeezes Enterprise Software Spending](#item-18) ⭐️ 8.0/10
19. [DeepSeek seeks $71B valuation in new funding round](#item-19) ⭐️ 8.0/10
20. [Stepfun unveils world's first AI agent-native OS and smartphone](#item-20) ⭐️ 8.0/10
21. [New LLM Coordination Benchmark Reveals Major Gaps](#item-21) ⭐️ 8.0/10
22. [Cloudflare Precursor Continuously Monitors Mouse Movements to Detect AI Bots](#item-22) ⭐️ 8.0/10
23. [DeepSeek Raises Over $7.4B in First Round, Uses LP to Keep Founder Control](#item-23) ⭐️ 8.0/10
24. [Amap Debuts ABot-WorldStudio with 'Spacetime Portals' for 3D World Generation](#item-24) ⭐️ 8.0/10
25. [Telegram's t.me domain frozen by registry](#item-25) ⭐️ 8.0/10
26. [DeepMind CEO Urges US-Led Global AI Regulatory Body](#item-26) ⭐️ 8.0/10
27. [Anthropic Launches Claude for Teachers for US K-12 Educators](#item-27) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Cursor 0day: Full Disclosure After 6 Months of Silence](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) ⭐️ 9.0/10

MindGard discovered a critical 0day vulnerability in the Cursor editor that allows arbitrary code execution via a malicious git.exe in the project folder, and after over six months of unaddressed reporting, they have published full details. This vulnerability threatens users of a popular AI coding assistant, especially on Windows, and the failure to patch after six months raises serious concerns about vendor security practices and the effectiveness of responsible disclosure. The exploit requires an attacker to place a malicious git.exe in the user's project folder; Cursor would then execute it without prompting. The vulnerability was reported on December 15, 2025 via HackerOne, initially marked informative, then reproduced, but never fixed.

hackernews · Synthetic7346 · Jul 14, 17:58 · [Discussion](https://news.ycombinator.com/item?id=48910676)

**Background**: A zero-day (0day) vulnerability is a security flaw unknown to the vendor, with no patch available. Full disclosure is the practice of publicly revealing all details of a vulnerability after a vendor fails to fix it, aiming to pressure action and inform users. The Cursor editor is an AI-powered code editor that can execute commands on behalf of the user.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-day_vulnerability">Zero-day vulnerability - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Full_disclosure_(computer_security)">Full disclosure (computer security) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community opinions are divided: some argue the vulnerability is overblown because it requires a malicious exe already on the system, while others emphasize the principle of not executing untrusted binaries without prompting, especially for an AI agent. Many express frustration with Cursor's lack of response for over six months.

**Tags**: `#security`, `#vulnerability`, `#cursor`, `#full disclosure`, `#0day`

---

<a id="item-2"></a>
## [Rust Rewrite of PostgreSQL Passes All 46k+ Regression Tests](https://github.com/malisper/pgrust) ⭐️ 9.0/10

The pgrust project, a complete rewrite of PostgreSQL in Rust, has achieved full compatibility by passing over 46,000 regression tests matching Postgres 18.3 output. The project is now available as a Docker image and WebAssembly demo. This milestone demonstrates that a Rust-based database can achieve binary-level compatibility with PostgreSQL, opening the door to safer, more performant alternatives. It could lower the barrier for experimenting with deep server changes using Rust's memory safety and AI-assisted programming. pgrust is disk compatible with Postgres 18.3 and can boot from an existing data directory. An upcoming version is reported to be 50% faster on transactional workloads and ~300x faster on analytical workloads compared to Postgres.

rss · GitHub Trending - Rust Daily · Jul 14, 01:40

**Background**: PostgreSQL is a widely used open-source relational database management system, originally written in C. Rewriting core database components in Rust, a systems programming language focused on safety and concurrency, has been a growing trend to improve reliability and performance while maintaining compatibility.

**Tags**: `#Rust`, `#PostgreSQL`, `#database`, `#systems programming`, `#rewrite`

---

<a id="item-3"></a>
## [Ollama Expands Local LLM Support with New Models](https://github.com/ollama/ollama) ⭐️ 9.0/10

Ollama has added support for Kimi-K2.6, GLM-5.1, MiniMax, DeepSeek, Qwen, Gemma, and other models, enabling local execution of state-of-the-art large language models. This expands the ecosystem of locally-run LLMs, giving developers and researchers more options for privacy, customization, and offline use, while reducing reliance on cloud APIs. Ollama provides a REST API, Python and JavaScript libraries, and one-command installations for macOS, Windows, Linux, and Docker, simplifying model management and integration.

rss · GitHub Trending - Go Daily · Jul 14, 01:35

**Background**: Ollama is an open-source platform that allows users to run large language models locally on their own hardware. It leverages llama.cpp as a backend for efficient inference, and supports a wide range of models including those from Chinese AI companies like Moonshot AI (Kimi) and Z.ai (GLM).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kimi_K2.6">Kimi K2.6</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM-5.1">GLM-5.1</a></li>
<li><a href="https://en.wikipedia.org/wiki/MiniMax_Group">MiniMax Group - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#Large Language Models`, `#Open Source`, `#Local LLM`, `#Developer Tools`

---

<a id="item-4"></a>
## [Fields Medal 2026 Winners Leaked; Two Chinese Mathematicians Named](https://www.36kr.com/p/3895047930100996) ⭐️ 9.0/10

The official ICM 2026 website inadvertently revealed the list of Fields Medal recipients in its source code, naming Chinese mathematicians Deng Yu and Wang Hong as awardees. If confirmed, Wang Hong would become the first Chinese woman and only the third female mathematician ever to win the Fields Medal; Deng Yu would also be the first Chinese national to receive the award, marking a historic milestone for Chinese mathematics. The leak was discovered on July 13, 2026, in the schedule source code of the ICM 2026 website, which has since been fixed. Both Deng Yu and Wang Hong are alumni of Peking University's School of Mathematical Sciences, class of 2007.

rss · 36氪 - 24小时热榜 · Jul 14, 08:53

**Background**: The Fields Medal is the highest honor in mathematics, awarded every four years to mathematicians under age 40. Wang Hong reportedly solved the Kakeya conjecture, a century-old problem about geometric measure theory, while Deng Yu solved Hilbert's sixth problem, which seeks to axiomatize physics. Only two people of Chinese descent, Shing-Tung Yau and Terence Tao, have previously won the medal.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/International_Congress_of_Mathematicians">International Congress of Mathematicians - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kakeya_conjecture">Kakeya conjecture</a></li>
<li><a href="https://www.mathunion.org/icm/icm-2026">ICM 2026 - International Congress of Mathematicians in ...</a></li>

</ul>
</details>

**Tags**: `#Fields Medal`, `#Mathematics`, `#Chinese Mathematicians`, `#Leak`, `#Awards`

---

<a id="item-5"></a>
## [Bonsai 27B: 27B-Parameter AI Model Runs on a Phone](https://prismml.com/news/bonsai-27b) ⭐️ 8.0/10

PrismML released Bonsai 27B, a quantized version of Qwen 3.6 27B that retains 90% intelligence while fitting in 12GB memory, enabling native on-phone inference. This breakthrough makes advanced AI models accessible on consumer devices without compromising too much on intelligence, potentially transforming on-device AI applications. The model uses quantization to compress from ~50GB to ~4GB (or up to 12GB for higher quality), and demonstrates strong performance in tool calling and vision tasks.

hackernews · xenova · Jul 14, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48910545)

**Background**: Quantization reduces the precision of model weights (e.g., from 16-bit to 4-bit), drastically shrinking model size with minimal accuracy loss. Bonsai 27B is based on Qwen 3.6 27B, a large language model from Alibaba Cloud. On-device AI inference allows privacy and offline use.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_compression">Model compression - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2411.02530v1">A Comprehensive Study on Quantization Techniques for Large ...</a></li>

</ul>
</details>

**Discussion**: Comments compare Bonsai 27B to Google's Gemma 4 4-bit QAT version, with users questioning tool-calling performance and noting recipe errors in the demo. Some users had issues running the models on LM Studio.

**Tags**: `#AI`, `#model compression`, `#quantization`, `#on-device ML`

---

<a id="item-6"></a>
## [AI agents worsen coordination in large software projects](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/) ⭐️ 8.0/10

Armin Ronacher's essay 'The Tower Keeps Rising' argues that while AI agents boost individual coding speed, they worsen coordination challenges in large software projects, leading to a loss of shared understanding without immediate failure. This analysis highlights a critical, often overlooked cost of AI-assisted programming: it can silently increase software complexity and fragility, threatening the sustainability of large codebases. The essay draws a parallel to the Lisp Curse, where powerful tools discourage collaboration; unlike the biblical Tower of Babel, construction continues after shared language is lost, making the problem less visible.

hackernews · cdrnsf · Jul 14, 16:57 · [Discussion](https://news.ycombinator.com/item?id=48909785)

**Background**: The Lisp Curse, as described by Rudolf Winestock, refers to Lisp's extreme power allowing individual developers to accomplish so much alone that they avoid collaboration, leading to fragmented libraries and poor documentation. In large software projects, productivity is limited not just by code output but by how well team members coordinate their understanding. AI agents that generate code quickly can widen this gap by enabling individuals to build without consulting others, increasing the risk of integration failures.

<details><summary>References</summary>
<ul>
<li><a href="http://www.winestockwebdesign.com/Essays/Lisp_Curse.html">The Lisp Curse - Winestock Webdesign</a></li>
<li><a href="https://www.freshcodeit.com/blog/myths-of-lisp-curse">What is the Curse of Lisp: Challenges and Opportunities</a></li>

</ul>
</details>

**Discussion**: Commenters largely agreed with the essay's premise. One noted a Tetris analogy for composability, while another explicitly connected it to the Lisp Curse. A third appreciated the nuanced observation that failure is not immediate, making the problem insidious.

**Tags**: `#software engineering`, `#AI-assisted programming`, `#composability`, `#coordination`, `#software complexity`

---

<a id="item-7"></a>
## [How to stop Claude from overusing 'load-bearing' phrases](https://jola.dev/posts/how-to-stop-claude-from-saying-load-bearing) ⭐️ 8.0/10

A blog post details how to get Claude to stop overusing phrases like 'load-bearing', sparking a community discussion about LLM output biases. With 405 points and 468 comments, this issue highlights how model quirks become glaring when scaled across millions of generated outputs. The post suggests using a global CLAUDE.md configuration to mitigate unwanted phrasing, and community members have tracked additional fixated words like 'projection', 'strand', and 'frontier'.

hackernews · shintoist · Jul 14, 11:46 · [Discussion](https://news.ycombinator.com/item?id=48905248)

**Background**: Claude is a large language model developed by Anthropic, known for its constitutional AI approach. LLMs can develop output biases, often overusing certain words or phrases due to training data or fine-tuning. When deployed at scale, these biases become amplified and more noticeable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="https://claude.com/">Claude</a></li>
<li><a href="https://claude.com/product/overview">The AI for Problem Solvers | Claude by Anthropic</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed feelings: some find claudisms less bothersome in direct coding interactions but jarring in prose that appears human-written. Others noted that the scalability of LLM biases makes them stand out more than individual human quirks. Solutions like a global CLAUDE.md to modify behavior were also shared.

**Tags**: `#LLM`, `#AI behavior`, `#Claude`, `#tone`, `#community discussion`

---

<a id="item-8"></a>
## [Are We Offloading Too Much Thinking to AI?](https://www.artfish.ai/p/offloading-thinking-to-ai) ⭐️ 8.0/10

An article explores whether over-reliance on AI for cognitive tasks is eroding human critical thinking, sparking a community debate about the risks and trade-offs. As AI tools become ubiquitous, the erosion of critical thinking could have long-term impacts on skill development, especially for junior professionals and the broader workforce. The discussion highlights real-world examples, such as junior developers unable to explain AI-generated code, and fears of a future where AI approval is mandatory for decisions.

hackernews · yenniejun111 · Jul 14, 15:18 · [Discussion](https://news.ycombinator.com/item?id=48908178)

**Background**: Cognitive offloading refers to using external tools to reduce cognitive demand, a concept studied in psychology. Historical examples include calculators and the internet, but AI now handles higher-level reasoning, raising concerns about deeper reliance and loss of understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cognitive_offloading">Cognitive offloading</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1364661316300985">Cognitive Offloading - ScienceDirect</a></li>
<li><a href="https://www.computer.org/publications/tech-news/trends/cognitive-offloading">Cognitive Offloading: How AI is Quietly Eroding Our Critical ...</a></li>

</ul>
</details>

**Discussion**: The community is divided: some argue heavy AI use still leaves the user in control, while others point to cases where individuals blindly trust AI without understanding, and fear a future of enforced AI deference.

**Tags**: `#AI ethics`, `#critical thinking`, `#cognitive offloading`, `#LLM impact`, `#software engineering`

---

<a id="item-9"></a>
## [Linux Input Latency Measured: X11 vs Wayland, VRR, DXVK](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/) ⭐️ 8.0/10

A detailed empirical study measured input latency across Linux display servers and technologies, finding that native Wayland games have the lowest latency while XWayland adds about 3ms overhead. This analysis helps Linux gamers and developers make informed choices about display servers and configurations, and demonstrates that the Linux ecosystem can self-improve through open measurement. The tests used a 500Hz display for precise timing; XWayland showed higher latency than native Wayland, and VRR (Variable Refresh Rate) did not add significant extra latency. DXVK, a DirectX-to-Vulkan translation layer, performed competitively with native D3D.

hackernews · hoechst · Jul 14, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48909424)

**Background**: X11 and Wayland are display servers on Linux: X11 is legacy, Wayland modern. VRR syncs monitor refresh to GPU frame rate. DXVK translates Direct3D calls to Vulkan for running Windows games on Linux.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Variable_refresh_rate">Variable refresh rate - Wikipedia</a></li>
<li><a href="https://github.com/doitsujin/dxvk">GitHub - doitsujin/dxvk: Vulkan-based implementation of D3D8 ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the thoroughness and importance of the measurements, though some noted the 500Hz display might mask frame-time issues. There was curiosity about Hyprland (Wayland compositor) and speculation that XWayland latency explains perceptions of Wayland being slow.

**Tags**: `#Linux`, `#input latency`, `#Wayland`, `#X11`, `#gaming`

---

<a id="item-10"></a>
## [Lobste.rs Migrates from MariaDB to SQLite, Cuts Costs](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything) ⭐️ 8.0/10

Lobste.rs has completed its migration from MariaDB to SQLite, resulting in lower CPU and memory usage, a snappier site, and halving VPS costs. The change is now considered the permanent architecture. This migration demonstrates SQLite's viability for production Rails applications handling moderate traffic, challenging the assumption that larger databases require separate database servers. It provides a real-world case study for cost reduction and operational simplicity. The Lobsters Rails application now runs on a single VPS with a primary SQLite database file of about 3.8GB, plus a 1.1GB cache database, a 218MB queue database, and a 555MB rack_attack database. The migration PR added 735 lines and removed 593 lines across 30 commits and 188 files.

rss · Simon Willison · Jul 14, 19:44

**Background**: SQLite is a lightweight, embedded SQL database engine that stores data in a single file, requiring no separate server process. It is often used for mobile apps and small-scale applications, but recent improvements have made it viable for production web services. Lobste.rs, a community-driven link aggregation site similar to Hacker News, originally used MariaDB (a MySQL fork) and had been planning a migration since 2018.

**Tags**: `#SQLite`, `#Rails`, `#database migration`, `#web development`, `#lobste.rs`

---

<a id="item-11"></a>
## [Friction Builds Shared Understanding in Software Projects](https://simonwillison.net/2026/Jul/14/armin-ronacher/#atom-everything) ⭐️ 8.0/10

Armin Ronacher argues that the shared language of a software project—built through code review, conversations, and friction—is at risk of being bypassed by AI agents, potentially leading to a loss of deep understanding among developers. This insight highlights a critical risk in the increasing use of AI coding agents: they may accelerate individual productivity at the expense of team-level coherence and shared mental models, which are essential for maintaining complex systems over time. Ronacher specifically notes that friction—such as the need to read others' code, ask questions, and coordinate across teams—synchronizes people by transferring understanding, and that not all of this slowness is waste.

rss · Simon Willison · Jul 14, 18:04

**Background**: In software engineering, an invariant is a condition that must always hold true during the execution of a program, such as a class invariant that ensures object consistency. Tacit knowledge refers to the unspoken, experience-based understanding that team members develop through collaboration and friction. Ronacher's argument connects these concepts by suggesting that the friction of code review and conversation is how tacit knowledge about invariants and system boundaries is shared and maintained within a team.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Invariant-based_programming">Invariant-based programming - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0950584913000591">Acquiring and sharing tacit knowledge in software development ...</a></li>

</ul>
</details>

**Tags**: `#software engineering`, `#shared understanding`, `#AI agents`, `#software development practices`, `#code review`

---

<a id="item-12"></a>
## [Manim: Animation Engine for Explanatory Math Videos](https://github.com/3b1b/manim) ⭐️ 8.0/10

Manim is an animation engine created by Grant Sanderson (3Blue1Brown) for programmatically generating explanatory math videos. The GitHub repository contains the original version, while a community-maintained fork exists for improved stability and contributions. Manim has become a key tool in math education and science communication, enabling creators to produce high-quality, precise animations that were previously difficult to create. Its open-source nature and active community have fostered widespread adoption, inspiring many to create their own educational content. There are two main versions: the original 3b1b/manim (installed via pip as 'manimgl') and the community edition (ManimCommunity/manim) forked in 2020. Manim requires Python 3.7+, FFmpeg, OpenGL, and optionally LaTeX and Pango.

rss · GitHub Trending - Python Daily · Jul 14, 01:39

**Background**: Manim stands for Mathematical Animation Engine. It was developed to create the animations seen on the popular YouTube channel 3Blue1Brown, which explains mathematical concepts with intuitive visuals. The tool allows users to write Python scripts that define scenes and objects, which are then rendered into animations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/3b1b/manim">GitHub - 3b1b/manim: Animation engine for explanatory math ...</a></li>
<li><a href="https://www.manim.community/">Manim Community</a></li>
<li><a href="https://www.3blue1brown.com/lessons/manim-demo/">How I animate 3Blue1Brown | A Manim demo with B... | 3Blue1Brown</a></li>

</ul>
</details>

**Tags**: `#animation`, `#math`, `#python`, `#education`, `#open-source`

---

<a id="item-13"></a>
## [HeyGen releases HyperFrames: open-source HTML-to-video tool for AI agents](https://github.com/heygen-com/hyperframes) ⭐️ 8.0/10

HeyGen has open-sourced HyperFrames, a framework that converts HTML, CSS, and animations into deterministic MP4 videos, specifically designed for AI coding agents. It includes 20 skills that teach agents how to plan, write, and render videos from natural language prompts. This lowers the barrier for AI agents to generate dynamic, branded videos programmatically, enabling automated video production in workflows like marketing, onboarding, and social media. As an open-source alternative to Remotion with no per-render fees, it could accelerate adoption of HTML-based video generation. HyperFrames uses headless Chrome and FFmpeg for rendering, supports adapter-based animation (GSAP, CSS, Lottie, Three.js, etc.), and requires Node.js version 22 or later. It is licensed under Apache 2.0 and does not require a build step for compositions.

rss · GitHub Trending - TypeScript Daily · Jul 14, 01:41

**Background**: Traditional video creation often requires manual editing or complex programming. HyperFrames builds on the concept of rendering web content as video, similar to Remotion but focused on AI agent workflows. It allows developers to define videos using familiar HTML/CSS, making it accessible to web developers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/heygen-com/hyperframes">GitHub - heygen-com/hyperframes: Write HTML. Render video. Built for agents. · GitHub</a></li>
<li><a href="https://hyperframes.heygen.com/introduction">Introduction - HyperFrames - HeyGen</a></li>
<li><a href="https://www.heygen.com/agent">AI Video Agent | Create and Automate Videos with AI | HeyGen</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#HTML`, `#open-source`, `#AI agents`, `#TypeScript`

---

<a id="item-14"></a>
## [Nushell: A Modern Shell in Rust Gains Traction](https://github.com/nushell/nushell) ⭐️ 8.0/10

Nushell, an open-source shell written in Rust, has reached a minimum-viable-product level and is being used as a daily driver by many developers, offering a structured data pipeline approach. Nushell represents a significant shift in command-line interface design by treating data as structured objects rather than plain text, enabling more powerful and intuitive workflows for developers and system administrators. Nushell supports pipelines that pass structured data, has a plugin system, and integrates with existing shell commands. It is available via package managers like Homebrew and winget, and includes a built-in help system and a book for learning.

rss · GitHub Trending - Rust Daily · Jul 14, 01:40

**Background**: Traditional Unix shells (like Bash and Zsh) treat all data as text strings, which requires manual parsing for complex operations. Nushell introduces a typed data model where commands operate on structured values, reducing errors and simplifying scripting. Rust was chosen for its performance and memory safety, contributing to Nushell's reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nushelle_de_Silva">Nushelle de Silva</a></li>

</ul>
</details>

**Tags**: `#shell`, `#rust`, `#developer-tools`, `#nushell`

---

<a id="item-15"></a>
## [InfluxDB 3 Core: Open Source Time Series Database with Apache Arrow](https://github.com/influxdata/influxdb) ⭐️ 8.0/10

InfluxData has released InfluxDB 3 Core as a generally available open source time series database, built on Apache Arrow, DataFusion, and Parquet, with a diskless architecture and sub-10ms query performance. This release marks a major architectural shift for InfluxDB, making it competitive with modern cloud-native databases for real-time analytics and monitoring, and it provides a free, open source alternative to the proprietary InfluxDB 3.0 Cloud. InfluxDB 3 Core supports SQL, InfluxQL, and Flight SQL for queries, uses Line Protocol for writes, and stores data in Apache Parquet on object storage or local disk, with an embedded Python VM for plugins and triggers.

rss · GitHub Trending - Rust Daily · Jul 14, 01:40

**Background**: Apache Arrow is a language-agnostic columnar memory format for efficient data interchange. DataFusion is an extensible query engine written in Rust that uses Arrow as its in-memory format. Apache Parquet is a columnar storage format optimized for compression and analytic queries. InfluxDB 3 Core combines these technologies to provide high-performance time series data handling.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Arrow">Apache Arrow</a></li>
<li><a href="https://datafusion.apache.org/">Apache DataFusion — Apache DataFusion documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Parquet">Apache Parquet</a></li>

</ul>
</details>

**Tags**: `#time series database`, `#influxdb`, `#open source`, `#apache arrow`, `#datafusion`

---

<a id="item-16"></a>
## [Plano: AI-Native Proxy for Agentic Apps](https://github.com/katanemo/plano) ⭐️ 8.0/10

Katanemo released Plano, an open-source AI-native proxy and data plane for agentic applications, offering built-in orchestration, safety, observability, and smart LLM routing. It is built in Rust and leverages Envoy for high performance. Plano simplifies production deployment of agentic AI systems by centralizing common infrastructure like routing, safety, and observability, letting developers focus on agent logic. It addresses a critical gap in the agentic AI stack as enterprises move from demos to production. Plano supports any language or AI framework, provides zero-code capture of Agentic Signals and OTEL traces, and includes Filter Chains for moderation and memory hooks. It is built on Envoy by its core contributors and backed by LLM research.

rss · GitHub Trending - Rust Daily · Jul 14, 01:40

**Background**: Agentic AI refers to systems that can act autonomously to achieve goals, often combining LLMs, multi-agent systems, and workflow orchestration. An AI proxy acts as a traffic manager between AI tools and external systems, handling routing, monitoring, and control. The data plane is the part of the network that processes and forwards data, while the control plane configures it. Plano unifies these concepts for agentic applications.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/katanemo/plano">GitHub - katanemo/plano: Plano is an AI-native proxy and data ...</a></li>
<li><a href="https://www.forbes.com/councils/forbestechcouncil/2026/02/24/what-is-an-ai-proxy-how-it-works-and-key-use-cases/">What Is An AI Proxy? How It Works And Key Use Cases - Forbes</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained - MIT Sloan</a></li>

</ul>
</details>

**Tags**: `#AI proxy`, `#agentic apps`, `#Rust`, `#LLM routing`, `#observability`

---

<a id="item-17"></a>
## [Samsung Flex Titanium: Titanium Alloy Reinforces Foldable Screens](https://www.ithome.com/0/976/778.htm) ⭐️ 8.0/10

Samsung has announced Flex Titanium, a new foldable display technology that uses a titanium alloy film and titanium plate to improve durability, reduce creases, and enhance viewing experience. It will debut in the next-generation Galaxy Z Fold device. This innovation directly addresses two key pain points of foldable phones: screen creasing and durability concerns. By leveraging titanium's strength, Samsung could set a new standard for foldable display quality and accelerate mainstream adoption. The titanium alloy film below the OLED panel is 20 times stiffer than polymer films and only about one-third the thickness of a human hair, while the titanium plate features micro-patterned holes to balance flexibility and support. The display also uses a high-resolution architecture and next-gen organic materials for better image quality and energy efficiency.

rss · IT之家 · Jul 14, 23:37

**Background**: Foldable phones rely on flexible displays that can bend repeatedly, but this creates a visible crease along the fold and raises concerns about long-term durability. Titanium is known for its high strength and toughness but is difficult to work into thin, flexible structures. Samsung's solution uses two titanium-based components — a film and a plate — to reinforce the display while maintaining thinness and flexibility.

<details><summary>References</summary>
<ul>
<li><a href="https://news.samsung.com/global/samsung-introduces-flex-titanium-technology-to-advance-foldable-displays">Samsung Introduces Flex Titanium Technology To Advance ...</a></li>
<li><a href="https://www.pcmag.com/news/samsung-teases-new-screen-substrate-for-its-next-foldable-titanium">Samsung Teases New Screen Substrate for Its Next Foldable ...</a></li>
<li><a href="https://www.androidauthority.com/samsung-flex-titanium-3687554/">Samsung details the secrets of foldable screen Flex Titanium tech</a></li>

</ul>
</details>

**Tags**: `#Foldable Phones`, `#Titanium`, `#Display Technology`, `#Samsung`, `#Galaxy Z Fold`

---

<a id="item-18"></a>
## [IBM Warns AI Infrastructure Boom Squeezes Enterprise Software Spending](https://www.ithome.com/0/976/722.htm) ⭐️ 8.0/10

IBM warned that enterprises are redirecting capital expenditure from software to AI infrastructure, causing IBM shares to plunge about 20% and dragging down other software stocks. The company expects Q2 revenue of ~$17.2 billion, below analyst estimates of $17.86 billion. This marks a clear signal that the AI infrastructure boom is cannibalizing enterprise software budgets, threatening the software industry's growth. Long-term shifts could fundamentally alter spending patterns across tech sectors. IBM CEO Arvind Krishna said customers shifted capital spending to servers, storage, and memory to lock in supply before price hikes. The company acknowledged it failed to adjust quickly, losing large orders. Adjusted EPS is expected at $2.93, below the $3.02 consensus.

rss · IT之家 · Jul 14, 12:36

**Background**: Enterprise software spending has historically been a stable revenue source for tech companies. However, the rise of generative AI has driven massive investment in data centers, GPUs, and networking gear, diverting funds from traditional software licenses. IBM's warning highlights the tension between AI infrastructure and software budgets.

**Tags**: `#AI`, `#infrastructure`, `#enterprise software`, `#spending`, `#IBM`

---

<a id="item-19"></a>
## [DeepSeek seeks $71B valuation in new funding round](https://www.ithome.com/0/976/713.htm) ⭐️ 8.0/10

DeepSeek is reportedly in preliminary talks with new investors for a funding round at a $71 billion pre-money valuation, just months after its first external raise. This valuation reflects DeepSeek's rapid growth and strategic importance in AI, as it plans to use the funds for large-scale data centers and AI chip acquisitions, potentially reshaping the competitive landscape. The previous round closed in May 2025, raising about $7 billion at a $52 billion post-money valuation, with founder Liang Wenfeng contributing $3 billion of that amount.

rss · IT之家 · Jul 14, 11:46

**Background**: DeepSeek is a Chinese AI startup focused on large language models. The rapid succession of funding rounds highlights intense capital needs for AI infrastructure, where companies spend billions on computing power and chips.

**Tags**: `#AI funding`, `#DeepSeek`, `#startup`, `#data center`, `#AI chips`

---

<a id="item-20"></a>
## [Stepfun unveils world's first AI agent-native OS and smartphone](https://www.36kr.com/p/3894202301250819) ⭐️ 8.0/10

Stepfun (阶跃星辰) launched Step AOS, the world's first agent-native operating system, along with the personal AI agent Amoo and the STEPX Neo smartphone, which integrates with major Chinese apps like Alipay, Meituan, and Didi. This marks a paradigm shift from app-based to intent-based smartphone interaction, potentially redefining the role of mobile devices and accelerating the adoption of AI agents in everyday life. Step AOS features dual-domain memory (user and agent), edge-cloud collaboration for task execution, and all operations are auditable and reversible for security. The company plans to build ecosystem over 100 days with community input.

rss · 36氪 - 24小时热榜 · Jul 14, 01:17

**Background**: An AI agent is an autonomous software entity that can understand, plan, and execute tasks on behalf of users. An agent-native operating system is built from the ground up to host and manage AI agents as first-class processes, unlike traditional OSes designed for human interaction. Edge-cloud collaboration means simple tasks run on-device for low latency, while complex tasks are offloaded to the cloud for deeper reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://zglg.work/en/ai/news/2026-07-13-step-launches-world-s-first-agent-native-os-rebuilt-from-scratch-for-ai-agent">Step Launches World's First Agent-Native OS, Rebuilt from ...</a></li>
<li><a href="https://www.ai-market-watch.com/news/step-ai-launches-worlds-first-agentic-native-os-step-aos-and-personal-ai-agent-a-3w5kon">Step AI unveils world's first agentic-native OS, Step AOS ...</a></li>
<li><a href="https://eu.36kr.com/en/p/3894202301250819">World's First AI Agent Smartphone Launch: Seamlessly ...</a></li>

</ul>
</details>

**Tags**: `#AI agent`, `#smartphone`, `#operating system`, `#Stepfun`, `#Chinese tech`

---

<a id="item-21"></a>
## [New LLM Coordination Benchmark Reveals Major Gaps](https://www.reddit.com/r/MachineLearning/comments/1uwc6ni/new_llm_coordination_benchmark_benchmarking/) ⭐️ 8.0/10

Researchers introduced the ALM benchmark to evaluate LLMs on open-ended multi-agent coordination tasks; they found that while most models average only ~6% normalized return, Gemini 3.1 Pro achieves performance comparable to a trained MARL agent on the hardest setting. This benchmark highlights that coordination is a distinct bottleneck beyond individual task competence, and the surprising success of Gemini 3.1 Pro suggests that advanced reasoning models can bridge the gap with specialized MARL algorithms, potentially enabling more capable multi-agent AI systems. The benchmark, named ALM, involves agents exploring, communicating, trading resources, crafting tools, building structures, and fighting mobs in a long-horizon open-ended world; communication was found to be the most impactful factor in ablation studies.

reddit · r/MachineLearning · /u/ktessera · Jul 14, 15:37

**Background**: Multi-agent reinforcement learning (MARL) is a subfield of RL that studies multiple learning agents coexisting in a shared environment. Traditional single-agent tasks differ from multi-agent coordination because agents must communicate and deduce others' intentions. The ALM benchmark provides a challenging testbed for evaluating whether LLMs can handle such coordination without explicit training.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning">Multi-agent reinforcement learning - Wikipedia</a></li>
<li><a href="https://deepmind.google/models/gemini/pro/">Gemini 3.1 Pro - Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmark`, `#multi-agent`, `#coordination`, `#AI research`

---

<a id="item-22"></a>
## [Cloudflare Precursor Continuously Monitors Mouse Movements to Detect AI Bots](https://blog.cloudflare.com/introducing-precursor/) ⭐️ 8.0/10

Cloudflare announced Precursor, a continuous behavior verification engine that monitors mouse movements, keystroke patterns, and other signals throughout a user session to distinguish humans from bots or AI agents. This addresses the growing challenge of AI-powered bots that can bypass single-point challenges like CAPTCHAs, by providing persistent verification across the entire user journey, enhancing web security without disrupting user experience. Precursor is a client-side JavaScript that dynamically collects behavioral signals and works with Cloudflare's Bot Management; it is currently available for free testing to enterprise Bot Management users, with a full release planned later this year.

telegram · zaihuapd · Jul 14, 09:44

**Background**: Traditional bot detection uses single-point challenges like CAPTCHAs or Turnstile at login or checkout. However, advanced AI bots can mimic human behavior for brief moments. Precursor continuously analyzes subtle human physiological traits—such as natural mouse arcs and micro-delays—that are hard for machines to fake, providing session-long verification.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/introducing-precursor/">Introducing Precursor: detecting agentic behavior with ...</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-challenges/precursor/">Precursor · Cloudflare challenges docs</a></li>
<li><a href="https://securityboulevard.com/2026/07/cloudflare-precursor-extends-bot-detection-beyond-browser-checks/">Cloudflare Precursor Extends Bot Detection Beyond Browser ...</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#Bot Detection`, `#Security`, `#Behavior Analysis`, `#AI Agents`

---

<a id="item-23"></a>
## [DeepSeek Raises Over $7.4B in First Round, Uses LP to Keep Founder Control](https://t.me/zaihuapd/42557) ⭐️ 8.0/10

DeepSeek completed its first funding round raising over 50 billion yuan (approximately $7.4 billion), using a limited partnership structure where investors contribute to a fund managed by CEO Liang Wenfeng instead of directly investing in DeepSeek, with a five-year lock-up period and no voting rights. This massive funding round underscores strong industry confidence in DeepSeek as a leading AI company, while the unconventional structure sets a precedent for Chinese startups seeking to maintain founder control despite large capital inflows. Founder Liang Wenfeng personally invested 20 billion yuan in this round. Tencent is considering an investment of 10 billion yuan, and CATL plans to invest 5 billion yuan, potentially becoming the largest external investors.

telegram · zaihuapd · Jul 14, 11:06

**Background**: A limited partnership (LP) structure separates management (general partner) from passive investors (limited partners), who contribute capital but have no management control. This structure allows founders to retain decision-making power while raising external funds, similar to dual-class share structures used by some tech companies. DeepSeek's approach further restricts investor rights with a five-year lock-up and no voting rights, ensuring founder control remains intact.

<details><summary>References</summary>
<ul>
<li><a href="https://corporatefinanceinstitute.com/resources/management/limited-partnership/">Limited Partnership - Overview, Characteristics, Examples</a></li>
<li><a href="https://www.investopedia.com/terms/l/limitedpartnership.asp">Limited Partnership (LP): What It Is, Pros and Cons, How to ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#funding`, `#DeepSeek`, `#startup`

---

<a id="item-24"></a>
## [Amap Debuts ABot-WorldStudio with 'Spacetime Portals' for 3D World Generation](https://www.ithome.com/0/976/538.htm) ⭐️ 8.0/10

Amap, under Alibaba, has officially released ABot-WorldStudio, a general world model workshop that generates interactive 3D worlds from text or images. It features 'spacetime portals' allowing users to jump between connected 3D scenes, and supports long-duration local inference on a single RTX 5090 for over an hour without degradation. This product unifies interactive video generation with 3D Gaussian Splatting (3DGS) scene generation for the first time, enabling novel applications in embodied AI simulation, game development, film production, and education. Its open-source foundation models and local deployment capability lower the barrier for researchers and developers. ABot-WorldStudio outputs native 3DGS assets with realistic geometric structures and photographic visual fidelity. It can be deployed on a single RTX 5090 with no limit on inference duration; official tests show continuous inference exceeding one hour without crash or quality decay.

telegram · zaihuapd · Jul 14, 12:22

**Background**: 3D Gaussian Splatting (3DGS) is a rasterization technique for real-time radiance field rendering, popularized in 2023 for creating photorealistic 3D scenes from sparse 2D images. World models are AI systems that can simulate interactive environments, often used in robotics and content generation. ABot-WorldStudio combines these two areas.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ithome.com/0/976/538.htm">内置“任意门”，高德发布通用世界模型工坊 ABot-WorldStudio - IT之家</a></li>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#world model`, `#open source`, `#AI world`, `#interactive simulation`

---

<a id="item-25"></a>
## [Telegram's t.me domain frozen by registry](https://t.me/zaihuapd/42559) ⭐️ 8.0/10

Telegram's short domain t.me was placed under serverHold status by the registry on July 13, preventing normal DNS resolution and affecting short link services. This disruption impacts millions of Telegram users who rely on t.me links for sharing channels, groups, and bots, and raises concerns about platform reliability and centralization risks. Whois records show the domain is now subject to multiple restrictions including serverHold, clientDeleteProhibited, clientTransferProhibited, and clientRenewProhibited, with GoDaddy as the registrar and validity until May 2035.

telegram · zaihuapd · Jul 14, 12:48

**Background**: A domain registry is the organization that manages a top-level domain (TLD) like .com, while a registrar sells domains to the public. serverHold is a registry-level suspension that typically prevents domain resolution, often due to policy violations or legal actions. The registry, not the registrar, imposes serverHold, making it a more severe and less common status.

<details><summary>References</summary>
<ul>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/10717/46/why-was-my-domain-suspended-with-a-serverhold-or-clienthold-status/">Why was my domain suspended with a serverHold or clientHold ...</a></li>
<li><a href="https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en">EPP Status Codes | What Do They Mean, and Why Should I Know?</a></li>
<li><a href="https://www.godaddy.com/help/what-is-the-difference-between-a-registry-registrar-and-registrant-8039">What is the difference between a registry, registrar and ...</a></li>

</ul>
</details>

**Tags**: `#Telegram`, `#domain`, `#DNS`, `#registry`, `#outage`

---

<a id="item-26"></a>
## [DeepMind CEO Urges US-Led Global AI Regulatory Body](https://www.theverge.com/tech/965270/google-deepmind-demis-hassabis-global-ai-watchdog) ⭐️ 8.0/10

Demis Hassabis, CEO of Google DeepMind, proposed the creation of a US-led global AI regulatory body that would review frontier AI models before deployment and coordinate industry-wide pauses if risks are deemed too high, aiming to have the body operational by the end of the year. This proposal addresses the urgent need for international AI governance as systems become more powerful and AGI may be only a few years away, potentially setting a precedent for global cooperation on AI safety and regulation. Hassabis stated that he has been in discussions with the Trump administration, other AI labs, and European officials for months, receiving very positive feedback. The proposed body would consist of independent experts and representatives from the open-source community.

telegram · zaihuapd · Jul 14, 14:29

**Background**: Artificial general intelligence (AGI) is a hypothetical type of AI that matches or surpasses human cognitive abilities across virtually all tasks. Frontier models are the most advanced AI models at a given moment, trained on massive datasets to deliver state-of-the-art performance. As these models become more capable, concerns about their potential risks have grown, prompting calls for regulatory oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Artificial_general_intelligence">Artificial general intelligence - Wikipedia</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work - NVIDIA</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#DeepMind`, `#Demis Hassabis`, `#global governance`, `#AI safety`

---

<a id="item-27"></a>
## [Anthropic Launches Claude for Teachers for US K-12 Educators](https://www.anthropic.com/news/claude-for-teachers) ⭐️ 8.0/10

On July 14, 2026, Anthropic launched Claude for Teachers, offering verified US K-12 educators free access to advanced Claude features, including teaching skill libraries aligned with all 50 states' academic standards. This initiative integrates AI into K-12 education with strong privacy protections and curriculum alignment, potentially transforming lesson planning and personalized learning for millions of teachers and students. Teacher data is not used for model training by default, and student information is protected under FERPA-compliant data handling protocols. Teachers must register by June 30, 2027 to receive a full year of free access.

telegram · zaihuapd · Jul 14, 15:37

**Background**: Claude is a series of large language models developed by Anthropic, known for its 'constitutional AI' approach to improve ethical compliance. FERPA is a US federal law that protects the privacy of student education records, granting parents and eligible students rights over disclosure. This launch aims to provide AI tools to educators while addressing privacy and curriculum concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/FERPA">FERPA</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI)</a></li>
<li><a href="http://studentprivacy.ed.gov/ferpa">FERPA | Protecting Student Privacy - ed</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Education`, `#Anthropic`, `#Claude`, `#EdTech`

---