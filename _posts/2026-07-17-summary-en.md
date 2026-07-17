---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 302 items, 30 important content pieces were selected

---

1. [Kimi K3: Open Frontier Intelligence Model Released](#item-1) ⭐️ 9.0/10
2. [Firefox compiled to WebAssembly runs inside another browser](#item-2) ⭐️ 9.0/10
3. [xAI open-sources Grok Build after privacy backlash](#item-3) ⭐️ 9.0/10
4. [World AI Cooperation Organization Agreement Signed, HQ in Shanghai](#item-4) ⭐️ 9.0/10
5. [Interactive Linear Algebra Book with 3D Visuals](#item-5) ⭐️ 8.0/10
6. [Rust-to-Zig Rewrite Progress Report](#item-6) ⭐️ 8.0/10
7. [Inkling: Thinking Machines Lab's Open-Weights MoE Model](#item-7) ⭐️ 8.0/10
8. [Open Interpreter: Open-Source Coding Agent for Low-Cost Models](#item-8) ⭐️ 8.0/10
9. [Stanford Releases Biomni: A General-Purpose Biomedical AI Agent](#item-9) ⭐️ 8.0/10
10. [vLLM: High-Throughput LLM Inference Engine](#item-10) ⭐️ 8.0/10
11. [Lance: An Open Lakehouse Format for Multimodal AI](#item-11) ⭐️ 8.0/10
12. [Jujutsu: Git-Compatible VCS in Rust Gains Traction](#item-12) ⭐️ 8.0/10
13. [Delta: Syntax-highlighting pager for git diffs](#item-13) ⭐️ 8.0/10
14. [Zed: High-Performance Multiplayer Code Editor Released](#item-14) ⭐️ 8.0/10
15. [InfluxDB 3 Core Goes Open Source with Apache Arrow](#item-15) ⭐️ 8.0/10
16. [PocketBase: Open Source Realtime Backend in a Single File](#item-16) ⭐️ 8.0/10
17. [Microsoft Launches Agent Framework for Go](#item-17) ⭐️ 8.0/10
18. [GitHub launches official MCP server for AI-driven repository management](#item-18) ⭐️ 8.0/10
19. [Powertech and Broadcom Plan PLP Joint Venture in Singapore](#item-19) ⭐️ 8.0/10
20. [China Unicom & Huawei Launch World's Largest 5G-A High-Uplink Network](#item-20) ⭐️ 8.0/10
21. [Three Chinese AI Founders Bet on AGI in High-Stakes Race](#item-21) ⭐️ 8.0/10
22. [Rethinking AI Memory: From Facts to Reasoning Patterns](#item-22) ⭐️ 8.0/10
23. [ExTernD: Expanded-Rank Ternary Decomposition for LLM Quantization](#item-23) ⭐️ 8.0/10
24. [PnP-CoSMo: Plug-and-Play MRI Reconstruction with Content/Style Model](#item-24) ⭐️ 8.0/10
25. [Schema harness hits 99% on ARC-AGI-3 using Opus 4.8 and Fable 5](#item-25) ⭐️ 8.0/10
26. [xAI sues user for generating child sexual abuse deepfakes with Grok](#item-26) ⭐️ 8.0/10
27. [CXMT to Match Micron DRAM Capacity by 2026](#item-27) ⭐️ 8.0/10
28. [Japan Buys 27,500 NVIDIA Rubin Chips for Robot Sovereign AI](#item-28) ⭐️ 8.0/10
29. [TSMC to invest additional $100B in US, Q2 profit surges 77%](#item-29) ⭐️ 8.0/10
30. [EU drafts requirement for Google to give rival AI assistants equal Android access](#item-30) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Kimi K3: Open Frontier Intelligence Model Released](https://www.kimi.com/blog/kimi-k3) ⭐️ 9.0/10

Kimi (Moonshot AI) announced K3, a frontier-level AI model with open weights, claiming overall intelligence ranks second only to Claude Fable 5 and GPT-5.6 Sol. The full model weights will be released in the coming days, alongside a detailed technical report. This release challenges top proprietary frontier models with an open-weight approach, potentially democratizing access to cutting-edge AI and increasing competition in the industry. K3 claims frontier-level performance, with benchmarks showing it second only to Claude Fable 5 and GPT-5.6 Sol. The model weights will be open, and a technical report with architecture and training details is forthcoming.

hackernews · vincent_s · Jul 16, 14:46 · [Discussion](https://news.ycombinator.com/item?id=48935342)

**Background**: Frontier AI models are the most advanced general-purpose models capable of reasoning, multimodal generation, and agentic workflows. Open-weight models allow researchers and developers to download, modify, and fine-tune the model weights, fostering innovation and transparency. Kimi K3 is positioned as an open alternative to proprietary frontier models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/glossary/frontier-models/">What Are Frontier AI Models and How They Work | NVIDIA Glossary</a></li>
<li><a href="https://openai.com/open-models/">Open models by OpenAI</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed sentiments. Some users raise concerns about Moonshot AI's data usage policies, noting that they may train on API content unless enterprise arrangements are made. Others discuss the high token costs of using K3 via OpenRouter, with one user reporting a costly inference. Overall, there is excitement about the open weights but caution regarding privacy and pricing.

**Tags**: `#AI`, `#LLMs`, `#open-source`, `#frontier models`, `#machine learning`

---

<a id="item-2"></a>
## [Firefox compiled to WebAssembly runs inside another browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the Firefox browser (Gecko engine) into WebAssembly, enabling it to run entirely within another browser like Chrome, with all network traffic proxied via the Wisp protocol through Puter's server. This breakthrough demonstrates that a full-featured browser can be sandboxed inside another browser, opening possibilities for secure legacy app support, cross-browser testing, and novel sandboxing architectures. The project used approximately $25,000 worth of AI tokens (Claude Opus and Fable) and leverages Firefox's strong single-process support. Network traffic is encrypted end-to-end, verified by inspecting WebSocket messages.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (WASM) is a low-level binary instruction format that allows code written in languages like C++ to run in web browsers at near-native speed. Firefox's Gecko engine was chosen because it has robust single-process mode, which simplifies compiling a browser engine to WASM. The Wisp protocol is a low-overhead method for multiplexing multiple TCP/UDP connections over a single WebSocket, which is necessary because browser code cannot open arbitrary network sockets.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-4.8">Claude Opus 4.8 - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly enthusiastic, with many commenters impressed by the technical feat. The team noted they had to scale up servers to handle traffic spikes from the HN attention, highlighting the real-world cost of the proxy infrastructure.

**Tags**: `#WebAssembly`, `#Firefox`, `#Browser Engineering`, `#Sandboxing`, `#AI`

---

<a id="item-3"></a>
## [xAI open-sources Grok Build after privacy backlash](https://simonwillison.net/2026/Jul/15/grok-build/#atom-everything) ⭐️ 9.0/10

xAI open-sourced the entire Grok Build codebase under Apache 2.0 after community backlash over its CLI tool uploading entire directories to Google Cloud. They also deleted all retained user data and disabled default data retention. This incident underscores serious privacy risks in AI coding tools and forced xAI to take unprecedented transparency measures, potentially setting a precedent for how AI companies handle user data and open-source their tools. The codebase contains 844,530 lines of Rust with only ~3% vendored code, includes a terminal Mermaid diagram renderer, and tool implementations inspired by Codex and OpenCode. The subagent system prompt explicitly forbids revealing its contents.

rss · Simon Willison · Jul 15, 23:59

**Background**: Grok Build is xAI's coding agent CLI tool that uses AI to assist developers with coding tasks in the terminal. It was initially closed-source and had a feature that by default uploaded the entire current directory to xAI's servers, leading to exposure of sensitive data like SSH keys and password managers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xai-org/grok-build">GitHub - xai-org/grok-build: SpaceXAI's coding agent harness and TUI. Fullscreen, mouse interactive, extensible. · GitHub</a></li>
<li><a href="https://x.ai/cli">Grok Build | SpaceXAI</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#open-source`, `#AI`, `#security`, `#xAI`

---

<a id="item-4"></a>
## [World AI Cooperation Organization Agreement Signed, HQ in Shanghai](https://www.nodeseek.com/post-825578-1) ⭐️ 9.0/10

On July 16, an agreement was signed to establish the World Artificial Intelligence Cooperation Organization (WAICO), an independent intergovernmental body, with its headquarters in Shanghai, China. Chinese Foreign Minister Wang Yi signed on behalf of China, and 29 countries became founding members. This marks a significant step in global AI governance, establishing a new international framework under the UN Charter principles. It could influence future AI cooperation and regulation, particularly by representing voices from the Global South and promoting equitable development. The organization will adhere to principles of extensive consultation, joint contribution, and shared benefits, and aims to ensure AI develops in a beneficial, safe, and fair manner. The 2026 World AI Conference and High-level Meeting on AI Global Governance will be held in Shanghai from July 17-20, featuring over 300 AI product launches.

rss · NodeSeek · Jul 16, 23:54

**Background**: The Chinese government first proposed establishing the World AI Cooperation Organization in July 2025 as part of its efforts to promote multilateralism and bridge the digital divide. The organization is designed as an intergovernmental body, distinct from industry associations or private initiatives, to foster international cooperation in AI development and governance.

**Tags**: `#AI governance`, `#international cooperation`, `#China`, `#global AI policy`

---

<a id="item-5"></a>
## [Interactive Linear Algebra Book with 3D Visuals](https://immersivemath.com/ila/) ⭐️ 8.0/10

The online book 'Immersive Linear Algebra' features interactive 3D figures that allow readers to manipulate vectors and matrices in real time, enhancing conceptual understanding. This resource demonstrates how interactive visualization can transform math education, making abstract concepts more tangible and accessible to a wider audience. The book covers standard linear algebra topics like vector operations, matrix multiplication, and eigenvalues, with embedded 3D scenes that respond to mouse drags and clicks.

hackernews · srean · Jul 16, 15:32 · [Discussion](https://news.ycombinator.com/item?id=48935951)

**Background**: Linear algebra is foundational for fields like computer graphics, machine learning, and engineering, but many students struggle with its geometric intuition. Interactive 3D figures help bridge the gap between algebraic formulas and visual understanding.

**Discussion**: Commenters express strong enthusiasm for the book, wishing similar interactive resources existed for other subjects like statistics and robotics. Some note that LLMs now make creating such visuals easier, potentially leading to more interactive textbooks.

**Tags**: `#linear algebra`, `#interactive learning`, `#math education`, `#visualization`

---

<a id="item-6"></a>
## [Rust-to-Zig Rewrite Progress Report](https://rtfeldman.com/rust-to-zig) ⭐️ 8.0/10

Richard Feldman published a blog post detailing the motivation and progress of rewriting the Roc compiler from Rust to Zig, highlighting Zig's incremental builds and memory control. This rewrite sparks debate on the trade-offs between Rust's safety guarantees and Zig's simplicity and performance, particularly for system software like compilers. The author notes that compilers doing code generation often require unsafe memory operations, and Zig's ReleaseSafe mode provides runtime checks for use-after-free, though commenters question the extent of those checks.

hackernews · jorangreef · Jul 16, 11:39 · [Discussion](https://news.ycombinator.com/item?id=48933149)

**Background**: Rust and Zig are modern systems programming languages. Rust emphasizes memory safety without garbage collection through its ownership model and borrow checker, while Zig focuses on simplicity, manual memory management, and seamless interoperability with C. The Roc compiler is a functional language compiler being rewritten from Rust to Zig to leverage Zig's fast incremental compilation and cross-compilation capabilities.

**Discussion**: Steve Klabnik argued that unsafe operations are not necessary for most compiler code generation, only for specific features like hot patching. Landr0id questioned Zig's runtime use-after-free detection claims, noting no documentation. Arthur Brown wondered why OCaml was not chosen given its maturity. Onlyrealcuzzo praised Zig's incremental builds as a killer feature but hoped Rust would eventually support similar capabilities.

**Tags**: `#rust`, `#zig`, `#compiler`, `#systems-programming`, `#memory-safety`

---

<a id="item-7"></a>
## [Inkling: Thinking Machines Lab's Open-Weights MoE Model](https://simonwillison.net/2026/Jul/16/inkling/#atom-everything) ⭐️ 8.0/10

Thinking Machines Lab released Inkling, their first open-weights multimodal Mixture-of-Experts model with 975B total parameters and 41B active, under Apache-2.0 license. This release strengthens the US open-weights AI ecosystem, offering a competitive alternative to models from NVIDIA and China, though Thinking Machines admits it is not a frontier model. Inkling is trained on 45 trillion tokens of text, images, audio, and video, but its model card and training data documentation are notably sparse. A smaller variant, Inkling-Small (276B total, 12B active), is still in testing.

rss · Simon Willison · Jul 16, 15:35

**Background**: Mixture-of-Experts (MoE) models use multiple specialized subnetworks (experts) with a gating mechanism to activate only a subset per input, enabling large total parameter counts without proportional compute cost. Open-weights means the trained parameters are publicly available under a license, but training data and code are not necessarily disclosed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://medium.com/@aruna.kolluru/exploring-the-world-of-open-source-and-open-weights-ai-aa09707b69fc">Exploring the World of Open Source and Open Weights AI | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-weights`, `#Mixture-of-Experts`, `#multimodal`, `#model release`

---

<a id="item-8"></a>
## [Open Interpreter: Open-Source Coding Agent for Low-Cost Models](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter has been released as an open-source coding agent optimized for low-cost models, forking OpenAI's Codex to emulate its agent harness. It allows users to run code locally via LLMs from the terminal on macOS, Linux, and Windows. This tool democratizes access to AI-powered coding agents by supporting low-cost models, potentially boosting developer productivity without requiring expensive API subscriptions. Its open-source nature encourages community contributions and customization. Open Interpreter includes a harness system that can switch between different model backends like native, claude-code, and deepseek-tui via the /harness command. It also features a QA skill for operating and testing web and native apps using agent-browser or trycua.

rss · GitHub Trending - Daily · Jul 16, 01:32

**Background**: Coding agents are AI systems that can autonomously write and execute code based on natural language instructions. Open Interpreter is a fork of OpenAI's Codex, designed to work efficiently with low-cost language models, making it accessible to a broader audience of developers without high computational costs.

**Tags**: `#coding agent`, `#low-cost models`, `#open source`, `#AI assistant`

---

<a id="item-9"></a>
## [Stanford Releases Biomni: A General-Purpose Biomedical AI Agent](https://github.com/snap-stanford/Biomni) ⭐️ 8.0/10

Stanford University announced the release of Biomni, a general-purpose biomedical AI agent that autonomously executes a broad spectrum of research tasks, integrating large language model reasoning with retrieval-augmented planning and code execution. The agent is now available on GitHub, accompanied by a research paper published on bioRxiv and a web UI at biomni.stanford.edu. Biomni has the potential to dramatically accelerate biomedical research by automating complex, repetitive workflows and generating testable hypotheses, addressing the growing bottleneck of fragmented and labor-intensive tasks. This release marks a significant step toward scalable AI-powered scientific discovery, impacting researchers across diverse biomedical subfields. Biomni supports multiple LLM backends, including Anthropic Claude, OpenAI, Gemini, and local models via Ollama, and requires API keys for operation. The software is installable via pip and provides a web-based user interface, with the source code available on GitHub under the SNAP Stanford organization.

rss · GitHub Trending - Python Daily · Jul 16, 01:39

**Background**: Biomedical research increasingly involves analyzing large datasets, conducting complex experiments, and navigating vast literature, leading to repetitive and fragmented workflows that slow discovery. AI agents are designed to combine human creativity with AI's ability to automate tasks and analyze data, but most previous tools are specialized. Biomni aims to be a general-purpose agent that can handle diverse research tasks across subfields, from genomics to drug discovery, by integrating LLM reasoning with structured planning and execution.

<details><summary>References</summary>
<ul>
<li><a href="https://biomni.stanford.edu/">Biomni - A General-Purpose Biomedical AI Agent</a></li>
<li><a href="https://www.biorxiv.org/content/10.1101/2025.05.30.656746v1">Biomni: A General-Purpose Biomedical AI Agent | bioRxiv</a></li>

</ul>
</details>

**Tags**: `#AI`, `#biomedical`, `#Stanford`, `#AI agent`

---

<a id="item-10"></a>
## [vLLM: High-Throughput LLM Inference Engine](https://github.com/vllm-project/vllm) ⭐️ 8.0/10

vLLM is an open-source library for efficient LLM inference and serving with state-of-the-art throughput and memory efficiency. By optimizing memory management and batching, vLLM makes LLM serving faster and cheaper, accelerating AI deployment in production. Key features include PagedAttention for efficient KV cache management, continuous batching, support for FP8/INT4 quantization, and compatibility with over 200 model architectures.

rss · GitHub Trending - Python Daily · Jul 16, 01:39

**Background**: Large language models require significant memory for the key-value cache during autoregressive generation. PagedAttention uses a paging mechanism to manage this cache more efficiently, reducing memory waste and enabling larger batch sizes, similar to virtual memory in operating systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference`, `#serving`, `#GitHub trending`

---

<a id="item-11"></a>
## [Lance: An Open Lakehouse Format for Multimodal AI](https://github.com/lance-format/lance) ⭐️ 8.0/10

Lance is an open-source lakehouse format that claims 100x faster random access than Parquet and Iceberg, with native support for vector search, full-text search, and multimodal data types. It includes zero-copy versioning, ACID transactions, and time travel capabilities. This addresses the need for a unified storage format that can handle multimodal AI workloads, which often involve large-scale vector embeddings and diverse data types. Its broad compatibility with popular data tools (Pandas, DuckDB, PyTorch, etc.) lowers the barrier for adoption and could accelerate AI feature engineering and retrieval-augmented generation pipelines. Lance converts from Parquet in two lines of code and supports efficient column addition without full table rewrites. It is built on Apache Arrow and offers both vector indexing (e.g., IVF, HNSW) and full-text search (BM25) on the same dataset.

rss · GitHub Trending - Rust Daily · Jul 16, 01:39

**Background**: A lakehouse combines data lake flexibility with warehouse ACID transactions, often using open table formats like Delta Lake, Iceberg, or Hudi. Multimodal AI processes multiple data types (text, image, audio) simultaneously, requiring storage that can handle diverse schemas and fast retrieval of embeddings. Vector indexing allows efficient similarity search over high-dimensional vectors, critical for modern AI applications like recommendation systems and large language model retrieval.

<details><summary>References</summary>
<ul>
<li><a href="https://www.onehouse.ai/blog/open-table-formats-and-the-open-data-lakehouse-in-perspective">Open Table Formats and the Open Data Lakehouse, In Perspective</a></li>
<li><a href="https://www.min.io/learn/open-table-format">What Is an Open Table Format? A Technical Overview | MinIO</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_AI">Multimodal AI</a></li>

</ul>
</details>

**Tags**: `#multimodal AI`, `#lakehouse`, `#vector search`, `#data format`, `#open source`

---

<a id="item-12"></a>
## [Jujutsu: Git-Compatible VCS in Rust Gains Traction](https://github.com/jj-vcs/jj) ⭐️ 8.0/10

Jujutsu (jj) is a new version control system written in Rust that is compatible with Git repositories, combining simplicity and power. It has gained significant traction as a trending Rust project on GitHub. Jujutsu introduces novel design choices that abstract the user interface from storage backends, offering a fresh approach to version control. It could influence workflows for both individual developers and large teams, especially those seeking Git compatibility with improved usability. Jujutsu uses Git repositories as a storage backend, but stores bookmarks and metadata outside of Git in custom storage. It is built in Rust and draws inspiration from Git, Mercurial, and Google's Piper/CitC systems.

rss · GitHub Trending - Rust Daily · Jul 16, 01:39

**Background**: Version control systems (VCS) are essential tools that track changes to source code over time, enabling collaboration and history management. Git is the most widely used distributed VCS, but its complexity has inspired alternative tools like Jujutsu that aim to simplify common workflows while maintaining compatibility.

<details><summary>References</summary>
<ul>
<li><a href="https://jj-for-everyone.github.io/">Introduction - Jujutsu for Everyone</a></li>
<li><a href="https://neugierig.org/software/blog/2024/12/jujutsu.html">Tech Notes: The Jujutsu version control system</a></li>
<li><a href="https://mskadu.medium.com/introducing-jujutsu-a-modern-alternative-to-git-32bb8b7fadd9">Introducing Jujutsu : A Modern Alternative to Git | Medium</a></li>

</ul>
</details>

**Tags**: `#version control`, `#git-compatible`, `#rust`, `#jujutsu`, `#vcs`

---

<a id="item-13"></a>
## [Delta: Syntax-highlighting pager for git diffs](https://github.com/dandavison/delta) ⭐️ 8.0/10

Delta is a syntax-highlighting pager for git, diff, grep, and blame output, providing enhanced readability with features like word-level diff highlighting and side-by-side view. For developers who regularly review code changes, Delta significantly improves the diff reading experience by adding syntax highlighting and navigation, making code reviews faster and more pleasant. Delta includes features such as Levenshtein edit inference for word-level highlighting, side-by-side view, line numbering, and hyperlinks for commit hashes and file paths.

rss · GitHub Trending - Rust Daily · Jul 16, 01:39

**Background**: When using git diff, the output is typically plain text without syntax highlighting, making it hard to quickly understand changes. Delta acts as a pager that parses the diff output and applies syntax highlighting based on the language, similar to tools like bat. It also offers a side-by-side view and word-level changes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/dandavison/delta">GitHub - dandavison/delta: A syntax-highlighting pager for git, diff, grep, rg --json, and blame output · GitHub</a></li>
<li><a href="https://dandavison.github.io/delta/introduction.html">Introduction - delta</a></li>
<li><a href="https://www.reddit.com/r/linux/comments/scaj1c/delta_a_syntaxhighlighting_pager_for_git_diff_and/">r/linux on Reddit: Delta: A syntax-highlighting pager for git, diff, and grep output</a></li>

</ul>
</details>

**Discussion**: On Reddit, users praised Delta as one of the best tools for displaying diffs, noting its support for Mercurial in addition to git. Some expressed appreciation for its customizability and ease of installation.

**Tags**: `#git`, `#diff`, `#syntax-highlighting`, `#pager`, `#developer-tools`

---

<a id="item-14"></a>
## [Zed: High-Performance Multiplayer Code Editor Released](https://github.com/zed-industries/zed) ⭐️ 8.0/10

Zed, a high-performance multiplayer code editor built in Rust, has been released as open source under GPL-3.0 license. It is created by the team behind Atom and Tree-sitter. Zed's focus on speed and real-time collaboration could set a new standard for code editors, challenging established tools like VS Code. It leverages Rust for performance and Tree-sitter for precise syntax highlighting. Zed supports macOS, Linux, and Windows, with a web version under discussion. It is primarily licensed under GPL-3.0-or-later with Apache-2.0 components where marked.

rss · GitHub Trending - Rust Daily · Jul 16, 01:39

**Background**: Atom was a popular open-source text editor developed by GitHub, while Tree-sitter is a parser generator that enables incremental parsing for efficient syntax highlighting in editors. Zed combines the team's expertise to create a modern, collaborative editing experience.

<details><summary>References</summary>
<ul>
<li><a href="https://zed.dev/">Zed is a high-performance, multiplayer code editor from the creators...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tree-sitter_(parser_generator)">Tree-sitter (parser generator)</a></li>

</ul>
</details>

**Tags**: `#code editor`, `#multiplayer`, `#Rust`, `#performance`, `#developer tools`

---

<a id="item-15"></a>
## [InfluxDB 3 Core Goes Open Source with Apache Arrow](https://github.com/influxdata/influxdb) ⭐️ 8.0/10

InfluxData has released InfluxDB 3 Core as an open-source time series database built on Apache Arrow, DataFusion, and Parquet, now generally available since April 2025. This release modernizes the widely-used InfluxDB platform by leveraging columnar data technologies, enabling faster query performance and real-time analytics for monitoring and event processing. InfluxDB 3 Core features a diskless architecture with object storage support, sub-10ms last-value queries, an embedded Python VM for plugins, and compatibility with InfluxDB 1.x and 2.x APIs.

rss · GitHub Trending - Rust Daily · Jul 16, 01:39

**Background**: Time series databases are optimized for storing and querying data points indexed by time, such as sensor readings or application metrics. Apache Arrow provides a cross-language columnar memory format for efficient data processing, while DataFusion is a query engine built on Arrow that supports SQL. Apache Parquet is a columnar storage format often used in data lakes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Arrow">Apache Arrow</a></li>
<li><a href="https://www.linkedin.com/pulse/single-node-data-engineering-duckdb-datafusion-polars-alex-merced-rgybe">Single-Node Data Engineering: DuckDB, DataFusion , Polars, and...</a></li>

</ul>
</details>

**Tags**: `#time-series`, `#database`, `#rust`, `#apache-arrow`, `#analytics`

---

<a id="item-16"></a>
## [PocketBase: Open Source Realtime Backend in a Single File](https://github.com/pocketbase/pocketbase) ⭐️ 8.0/10

PocketBase is an open-source backend that bundles an embedded SQLite database, realtime subscriptions, file storage, user management, and an admin dashboard into a single executable file, and it is trending on GitHub. It dramatically simplifies backend development for small to medium projects by removing the need for complex infrastructure setup, and its built-in realtime capabilities make it ideal for modern web and mobile applications. PocketBase uses SQLite as its embedded database and supports realtime subscriptions via WebSocket, and it can be extended using Go or JavaScript hooks, offering flexibility for custom business logic.

rss · GitHub Trending - Go Daily · Jul 16, 01:35

**Background**: Traditional backend stacks often require separate components such as a database server, API server, and authentication server, which can be complex to set up and maintain. PocketBase consolidates these into a single binary, similar to all-in-one platforms like Supabase but self-hosted and lighter. Written in Go, it is portable and performant, making it suitable for developers who want a quick, self-contained backend solution.

<details><summary>References</summary>
<ul>
<li><a href="https://pocketbase.io/">PocketBase - Open Source backend in 1 file</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#backend`, `#Go`, `#realtime`, `#database`

---

<a id="item-17"></a>
## [Microsoft Launches Agent Framework for Go](https://github.com/microsoft/agent-framework-go) ⭐️ 8.0/10

Microsoft has released an official Go implementation of its Agent Framework (MAF), enabling developers to build, orchestrate, and deploy AI agents and multi-agent workflows in Go. The framework is currently in public preview and supports integrations with Microsoft Foundry, Azure OpenAI, OpenAI, MCP, A2A, and more. This marks a significant expansion of enterprise AI agent development into the Go ecosystem, a language widely used for cloud-native and backend systems. The multi-agent workflow support aligns with the industry trend toward complex, production-grade agent orchestration. The Go SDK currently covers core agents, tools, middleware, workflows, observability, and interoperability, but lacks some broader product integrations present in the .NET version. The framework remains separate from the upstream MAF codebase during preview, with closer alignment expected as adoption grows.

rss · GitHub Trending - Go Daily · Jul 16, 01:35

**Background**: AI agents are autonomous systems that perform tasks by designing workflows with available tools. Multi-agent workflows orchestrate multiple such agents to collaboratively solve complex problems, a pattern gaining traction in enterprise AI. Microsoft Agent Framework provides a consistent foundation for building and operating such agent systems across languages including Python, .NET, and now Go.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/ai-agents">What Are AI Agents ? | IBM</a></li>
<li><a href="https://temporal.io/blog/what-are-multi-agent-workflows">Multi - agent Workflow patterns and modern use cases | Temporal</a></li>

</ul>
</details>

**Tags**: `#Go`, `#AI Agents`, `#Microsoft`, `#Framework`, `#Multi-Agent`

---

<a id="item-18"></a>
## [GitHub launches official MCP server for AI-driven repository management](https://github.com/github/github-mcp-server) ⭐️ 8.0/10

GitHub has released its official Model Context Protocol (MCP) server, enabling AI agents to manage repositories, issues, pull requests, and workflows through natural language commands. This official integration significantly lowers the barrier for AI-driven automation in software development, allowing developers to delegate routine tasks to AI agents and focus on higher-level work. The server supports remote and local deployment, requires MCP-compatible hosts (e.g., VS Code 1.101+), and authenticates via OAuth or personal access tokens. It includes tools for repository browsing, issue/PR management, CI/CD monitoring, security analysis, and team collaboration.

rss · GitHub Trending - Go Daily · Jul 16, 01:35

**Background**: The Model Context Protocol (MCP) is an open standard that allows AI agents to access external tools and data sources in a standardized way. Developed by Anthropic, MCP enables AI assistants to perform actions like reading files or managing repositories. GitHub's MCP server is an official implementation that brings these capabilities to the GitHub ecosystem.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://github.com/github/github-mcp-server">GitHub - github / github - mcp - server : GitHub 's official MCP Server</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#GitHub`, `#AI`, `#automation`, `#developer-tools`

---

<a id="item-19"></a>
## [Powertech and Broadcom Plan PLP Joint Venture in Singapore](https://www.ithome.com/0/977/838.htm) ⭐️ 8.0/10

Powertech Technology (PTI) announced on July 17, 2024, that it plans to form a joint venture with Broadcom in Singapore focused on panel-level advanced packaging (PLP), with PTI investing $400 million. This collaboration between a top OSAT provider and Broadcom underscores the growing importance of panel-level packaging for high-performance AI and datacenter chips, potentially reducing costs and improving efficiency. The Singapore location also strengthens supply chain resilience in the semiconductor ecosystem. Panel-level packaging uses rectangular substrates instead of round wafers, improving area utilization and lowering cost per unit. The joint venture will likely focus on fan-out panel-level packaging (FOPLP), a key technology for integrating multiple dies.

rss · IT之家 · Jul 16, 23:29

**Background**: Advanced packaging involves integrating multiple components in a single package to achieve performance gains without relying solely on transistor scaling. Panel-level packaging (PLP) extends concepts from wafer-level packaging to larger rectangular panels, enabling higher throughput and lower costs. Major players like TSMC are also investing in FOPLP. Powertech is a leading global OSAT, and Broadcom is a major semiconductor company that drives demand for advanced packaging in networking and AI chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/panel-level-packaging-plp-strategic-evolution-semiconductor-szxvf">Panel - Level Packaging ( PLP ): A Strategic Evolution in Semiconductor...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_(semiconductors)">Advanced packaging (semiconductors)</a></li>
<li><a href="https://www.yolegroup.com/strategy-insights/is-panel-level-packaging-plp-finally-emerging/">Is Panel - Level Packaging ( PLP ) finally emerging?</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#advanced packaging`, `#panel-level packaging`, `#Broadcom`, `#Powertech`

---

<a id="item-20"></a>
## [China Unicom & Huawei Launch World's Largest 5G-A High-Uplink Network](https://www.ithome.com/0/977/791.htm) ⭐️ 8.0/10

China Unicom Beijing and Huawei have launched the world's largest 5G-Advanced (5G-A) high-uplink commercial network in Beijing, featuring over 10,000 base stations. The network achieves an average uplink speed of 397 Mbps and supports real-time AI applications such as AI glasses with millisecond latency. This milestone demonstrates large-scale deployment of 5G-Advanced technology with a focus on uplink performance, which is critical for emerging AI applications that require real-time data upload. It sets a benchmark for mobile network evolution toward the Mobile AI era, where stable and fast uplink is as important as downlink. The network uses 3.5GHz and 2.1GHz carrier aggregation (SUL solution) to achieve high uplink. In a 34km driving test, the network achieved 83% uplink 100MHz availability, 1Gbps peak uplink, and only 0.1% of samples below 20Mbps. It fully supported AI glasses, AI smartphones, and AI cameras in mobile scenarios.

rss · IT之家 · Jul 16, 14:27

**Background**: 5G-Advanced (3GPP Release 18) is an evolution of 5G that enhances speed, latency, and reliability. Carrier aggregation combines multiple frequency bands to increase bandwidth; the 3.5GHz band provides high capacity while 2.1GHz offers wider coverage. This deployment leverages that combination to boost uplink performance for AI-driven applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/5g-advanced-6g-faster-lower-latency-networks-enabling-new-7ieqc">5 G - Advanced & 6G: Faster, lower-latency networks enabling new...</a></li>
<li><a href="https://www.t-mobile.com/news/network/t-mobile-reaches-5g-advanced-nationwide-milestone-unlocks-the-modern-wireless-network-for-consumers-businesses-and-developers">T‑Mobile Reaches 5 G Advanced Nationwide... - T‑Mobile Newsroom</a></li>

</ul>
</details>

**Tags**: `#5G-Advanced`, `#AI`, `#uplink network`, `#China Unicom`, `#Huawei`

---

<a id="item-21"></a>
## [Three Chinese AI Founders Bet on AGI in High-Stakes Race](https://www.36kr.com/p/3896941290833539) ⭐️ 8.0/10

Zhipu CEO Tang Jie issued an internal letter calling for a 'reset' after a successful IPO, while MiniMax founder Yan Junjie pledged to forgo salary until AGI and donate 4% of his shares to retain talent. Meanwhile, DeepSeek founder Liang Wenfeng is raising a new funding round, with valuation reportedly jumping from $52 billion to $71 billion, and is reportedly preparing for an IPO in 2027. This analysis reveals that in China's competitive large model arena, access to capital is a survival imperative, not a choice. The contrasting strategies of these three founders—ranging from aggressive technical reinvestment to tight ownership control and personal sacrifice—highlight the critical decisions shaping the future of China's AI ecosystem. Zhipu's market cap reached 810 billion HKD, nearly three times Baidu's; MiniMax's stock plummeted 77% from 1330 to 297 HKD; DeepSeek's valuation jumped to $71 billion with Liang Wenfeng retaining 78% control. Tang Jie outlined a 'touch-the-sky' plan targeting four technical peaks, while Liang's funding round aims to give employee options a market price, preventing talent poaching.

rss · 36氪 - 24小时热榜 · Jul 16, 00:46

**Background**: China's AI large model race requires massive computational resources, making continuous funding essential for survival. The ultimate goal for many companies is Artificial General Intelligence (AGI), which demands long-term investment and technical breakthroughs. Zhipu, MiniMax, and DeepSeek are among the leading players, each taking distinct approaches to balancing innovation, talent retention, and financial sustainability.

**Tags**: `#AI大模型`, `#融资`, `#行业分析`, `#创始人战略`, `#竞争格局`

---

<a id="item-22"></a>
## [Rethinking AI Memory: From Facts to Reasoning Patterns](https://www.reddit.com/r/MachineLearning/comments/1uy6yht/are_current_ai_memory_architectures_optimizing/) ⭐️ 8.0/10

A Reddit user proposes that AI persistent context should evolve from storing descriptive facts about users to inferring higher-level reasoning patterns, such as explanatory frameworks and reasoning styles. This idea challenges the current design of AI memory architectures, which often prioritize storing factual preferences over understanding underlying cognitive patterns. If realized, it could lead to AI systems that more deeply align with a user's unique way of thinking, enabling more personalized and insightful interactions. The proposal distinguishes between current descriptive memory (e.g., 'user interested in economics') and a potential inferential memory that captures recurring explanatory frameworks and characteristic reasoning styles. It questions whether such representations can emerge naturally from existing architectures or require fundamentally different approaches.

reddit · r/MachineLearning · /u/Boris_Ljevar · Jul 16, 16:00

**Background**: Current AI memory systems, such as those used in conversational agents, store persistent context in the form of saved memories, conversation summaries, and user preferences. These are primarily descriptive, helping the system recall facts about the user. Recent developments in AI agent memory emphasize balancing semantic understanding and scalability, but still focus on retrieval of stored information. The idea of shifting to higher-level reasoning patterns represents a potential paradigm change, moving from a collection of notes to an evolving model of how a user interprets problems.

<details><summary>References</summary>
<ul>
<li><a href="https://redis.io/blog/ai-agent-memory-stateful-systems/">AI agent memory: types, architecture & implementation</a></li>
<li><a href="https://www.cognee.ai/academy/chapter-1/what-is-ai-memory">What is AI Memory? | Cognee Academy</a></li>

</ul>
</details>

**Tags**: `#AI memory`, `#persistent context`, `#reasoning patterns`, `#machine learning`, `#abstraction`

---

<a id="item-23"></a>
## [ExTernD: Expanded-Rank Ternary Decomposition for LLM Quantization](https://www.reddit.com/r/MachineLearning/comments/1uy2zb3/externd_expandedrank_ternary_decomposition/) ⭐️ 8.0/10

A new method called ExTernD expands the rank of ternary decomposition for LLM post-training quantization, allowing arbitrary accuracy with minimal VRAM increase. This addresses a key limitation of ternary quantization (fixed rank), enabling accuracy comparable to higher-bit methods while maintaining efficiency, which could significantly improve LLM deployment on resource-constrained devices. The method decomposes a weight matrix into two ternary matrices and an inner diagonal scaling matrix, making the effective rank arbitrarily large. Experiments show only a slight VRAM overhead compared to standard quantization techniques.

reddit · r/MachineLearning · /u/LMTLS5 · Jul 16, 13:31

**Background**: Post-training quantization (PTQ) reduces LLM memory and computation by converting weights to lower precision. Ternary quantization uses values {-1,0,1}, but fixed-rank ternary matrices limit accuracy. ExTernD uses expanded-rank decomposition to overcome this, achieving flexible accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13511">ExTernD: Expanded-Rank Ternary Decomposition Ternary LLM ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tensor_rank_decomposition">Tensor rank decomposition - Wikipedia</a></li>
<li><a href="https://symbl.ai/developers/blog/a-guide-to-quantization-in-llms/">A Guide to Quantization in LLMs | Symbl.ai</a></li>

</ul>
</details>

**Tags**: `#ternary quantization`, `#LLM compression`, `#post-training quantization`, `#model decomposition`, `#efficient inference`

---

<a id="item-24"></a>
## [PnP-CoSMo: Plug-and-Play MRI Reconstruction with Content/Style Model](https://www.reddit.com/r/MachineLearning/comments/1uy2h66/pnpcosmo_a_multicontrast_mri_reconstruction/) ⭐️ 8.0/10

Researchers propose PnP-CoSMo, a plug-and-play multi-contrast MRI reconstruction framework that learns a content/style model from image-domain data, eliminating the need for raw k-space training data. This addresses a critical data bottleneck in MRI reconstruction and offers generalization across different contrasts and forward operators, potentially accelerating clinical adoption of deep learning methods. The framework consists of two stages: first, a content/style model is pretrained on image-only data; second, it is frozen and used as a prior in iterative reconstruction. It is published in Medical Image Analysis with code available.

reddit · r/MachineLearning · /u/void_gear · Jul 16, 13:10

**Background**: In MRI, raw data is acquired in k-space, which is the Fourier transform of the image. Traditional deep learning methods often require large amounts of raw k-space data for training, which is a major bottleneck. Plug-and-play priors allow using pre-trained denoisers as regularizers in iterative algorithms without modifying the reconstruction pipeline.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/K-space_in_magnetic_resonance_imaging">K-space in magnetic resonance imaging</a></li>
<li><a href="https://colab.research.google.com/github/ISMRM-MIT-CMR/CMR-DL-challenge/blob/master/challenge_plug_and_play_sample_solution.ipynb">challenge_ plug _ and _ play _sample_solution.ipynb - Colab</a></li>

</ul>
</details>

**Tags**: `#MRI reconstruction`, `#multi-contrast`, `#deep learning`, `#plug-and-play`, `#content/style modeling`

---

<a id="item-25"></a>
## [Schema harness hits 99% on ARC-AGI-3 using Opus 4.8 and Fable 5](https://www.reddit.com/r/MachineLearning/comments/1uyf8oo/new_fable5opus48_harness_called_schema_claims_99/) ⭐️ 8.0/10

A new harness called Schema achieves 99% accuracy on the ARC-AGI-3 Public benchmark by combining Claude Opus 4.8 and Fable 5 models with an improved inference process, without modifying model weights. This near-perfect score on a challenging interactive reasoning benchmark demonstrates that significant gains can come from process-level improvements around models, potentially influencing how AI systems are deployed and benchmarked. Schema uses a fixed fallback rule: Opus 4.8 and Sol xhigh run first; games scoring below 80 are rerun with Fable 5 and Sol max respectively, and the higher per-game score is retained. It also achieves 95.35% using GPT-5.6 Sol.

reddit · r/MachineLearning · /u/we_are_mammals · Jul 16, 21:02

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that evaluates AI agents on novel, turn-based environments requiring exploration, goal inference, and planning. A 'harness' refers to the system or workflow that orchestrates model calls, data processing, and decision logic—separate from the model's internal weights. Claude Opus 4.8 is Anthropic's most capable model, and Fable 5 is another high-performance AI model. Schema improves how observations are turned into internal models, how predictions are tested, and how plans are executed and revised.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus_4.8">Claude Opus 4.8</a></li>
<li><a href="https://fable5.io/">Fable 5 AI — Independent Model Guide & Prompt Workspace</a></li>

</ul>
</details>

**Tags**: `#ARC-AGI`, `#Claude Opus`, `#Fable5`, `#Machine Learning`, `#AI Benchmarking`

---

<a id="item-26"></a>
## [xAI sues user for generating child sexual abuse deepfakes with Grok](https://www.reuters.com/legal/litigation/musks-xai-sues-grok-user-over-sexualized-deepfakes-2026-07-15/) ⭐️ 8.0/10

xAI has filed a lawsuit against Terry Harwood for using its Grok chatbot to generate child sexual abuse and non-consensual intimate deepfakes. This is one of the first lawsuits by an AI company against a user for generating CSAM, setting a legal precedent for holding users accountable for model misuse. xAI reports that in 2026 alone, it suspended 52,222 accounts, reported 73,604 incidents to the National Center for Missing & Exploited Children, and facilitated at least 244 arrests.

telegram · zaihuapd · Jul 16, 01:45

**Background**: Grok is a generative AI chatbot developed by xAI, launched in late 2023. It has been controversial for generating inappropriate content, including sexualized images of minors. AI deepfakes are created using generative models that can manipulate images or videos, often without consent. The lawsuit highlights ongoing challenges in AI safety and moderation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grok_AI">Grok AI</a></li>
<li><a href="https://grokipedia.com/page/Grok_(chatbot)">Grok (chatbot)</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Deepfakes`, `#Legal`, `#xAI`, `#Grok`

---

<a id="item-27"></a>
## [CXMT to Match Micron DRAM Capacity by 2026](https://www.tomshardware.com/pc-components/dram/cxmt-close-to-matching-microns-memory-capacity-in-2026-research-claims-would-put-china-on-track-to-become-worlds-second-largest-dram-producer) ⭐️ 8.0/10

Citrini Research predicts that CXMT (ChangXin Memory Technologies) will reach approximately 350,000 wafer starts per month (WSPM) by the end of 2026, nearly matching Micron's 375,000 WSPM, potentially making China the world's second-largest DRAM producer. This shift could reshape the global DRAM supply chain, reducing reliance on South Korean and American suppliers and intensifying geopolitical tensions over semiconductor technology exports. China's growing capacity may also help stabilize DRAM prices and address potential supply gaps. CXMT's capacity is projected to grow to 950,000 WSPM by 2030, while total Chinese DRAM output (including other domestic firms) could reach 1.41 million WSPM. However, restrictions on advanced immersion DUV lithography tools under the proposed US MATCH Act could hinder near-term expansion.

telegram · zaihuapd · Jul 16, 02:30

**Background**: DRAM (Dynamic Random Access Memory) is a type of volatile memory widely used in computers and servers. Wafer starts per month (WSPM) is a key metric for memory fabrication capacity. Immersion DUV lithography is a critical technology for producing advanced DRAM nodes, and restrictions on its export could significantly impact China's ability to scale up production. The MATCH Act (Multilateral Coordination for Hardware Technology) is a US legislative proposal aimed at tightening export controls on semiconductor manufacturing equipment.

<details><summary>References</summary>
<ul>
<li><a href="https://caifuhao.eastmoney.com/news/20260404232857892043730">深度解析：4月3日的“最严芯片 法 案 ”（ MATCH ...</a></li>
<li><a href="https://www.163.com/dy/article/IM7V623E0516DOTJ.html">揭秘 光 刻 技术：一束 光 的旅程究竟有多复杂？| 摩尔|掩模|nm|euv...</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#semiconductor`, `#China`, `#memory`, `#technology`

---

<a id="item-28"></a>
## [Japan Buys 27,500 NVIDIA Rubin Chips for Robot Sovereign AI](https://www.bloomberg.com/news/articles/2026-07-16/japan-to-buy-nvidia-rubin-chips-to-build-sovereign-ai-for-robots) ⭐️ 8.0/10

Japan announced plans to purchase 27,500 NVIDIA Rubin chips, led by the newly formed Noetra consortium, to build a large-scale data center for developing a domestic foundational AI model for robots, with a government subsidy of 387.3 billion yen (about $24 billion). This initiative aims to create a 'third option' beyond the US and China in AI, reducing Japan's dependence on foreign technology and targeting over 30% of the global robot market by 2040, with significant geopolitical and economic implications. Noetra includes SoftBank, Toyota-backed Preferred Networks, NEC, and others; the first AI model is expected by March 2026, with a robot-specific version later. The Rubin architecture is NVIDIA's next-generation platform focused on integrated AI factory ecosystems.

telegram · zaihuapd · Jul 16, 10:59

**Background**: The Rubin architecture, unveiled at CES, shifts NVIDIA's focus from single GPUs to integrated AI factory ecosystems unifying massive compute clusters. Japan's sovereign AI push aligns with global trends of nations investing in domestic AI infrastructure to reduce reliance on a few dominant players, especially in critical sectors like robotics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.thundercompute.com/blog/nvidia-rubin-architecture">Nvidia Rubin Architecture : Everything You Must... | Thunder Compute</a></li>
<li><a href="https://www.storyboard18.com/digital/japan-plans-6-1-billion-sovereign-ai-model-10-million-robots-by-2040-102912.htm">Japan plans $6.1 billion sovereign AI model, 10 million... - Storyboard18</a></li>
<li><a href="https://www.channelnewsasia.com/east-asia/japan-plans-sovereign-ai-model-10-million-ai-robots-6223956">Japan plans sovereign AI model, 10 million AI robots - CNA</a></li>

</ul>
</details>

**Tags**: `#AI`, `#robotics`, `#NVIDIA`, `#Japan`, `#sovereign AI`

---

<a id="item-29"></a>
## [TSMC to invest additional $100B in US, Q2 profit surges 77%](https://www.reuters.com/world/asia-pacific/tsmcs-second-quarter-profit-seen-hitting-record-ai-boom-2026-07-15/) ⭐️ 8.0/10

TSMC announced an additional $100 billion investment in Arizona factories, bringing total US investment to $265 billion, and reported record Q2 net profit of $22 billion, up 77% year-over-year. This massive investment and record profit underscore TSMC's central role in the AI-driven semiconductor boom and highlight the deepening US-Taiwan chip supply chain ties amid geopolitical tensions. TSMC raised its 2026 capital expenditure forecast to $60-$64 billion and expects full-year dollar revenue to grow over 40%. There are currently 8 factories built or planned in Arizona, with up to 4 more possible.

telegram · zaihuapd · Jul 16, 12:29

**Background**: TSMC is the world's largest semiconductor foundry, producing advanced chips for companies like Apple, NVIDIA, and AMD. The US investments aim to secure supply chains and meet soaring demand for AI chips, driven by the global AI boom.

**Tags**: `#TSMC`, `#semiconductor`, `#AI`, `#investment`, `#manufacturing`

---

<a id="item-30"></a>
## [EU drafts requirement for Google to give rival AI assistants equal Android access](https://t.me/zaihuapd/42615) ⭐️ 8.0/10

The European Commission has drafted measures that would require Google to grant competing AI assistants, such as ChatGPT and Claude, the same system-level permissions on Android as its own Gemini assistant. The proposal is still in draft form and its release could be delayed. If enacted, this regulation would significantly level the playing field for AI assistants on Android, potentially increasing competition and user choice. However, Google has raised concerns about security and privacy risks from granting deep system access to third-party apps. The draft mandates that rival AI assistants get full access to core Android functionalities, including the ability to perform actions inside other apps. Google has strongly opposed the move, warning of a potential security catastrophe if external apps bypass hardware safety guardrails.

telegram · zaihuapd · Jul 16, 13:19

**Background**: Currently, Google's Gemini assistant has deep system-level access on Android, allowing it to read phone and messaging data, while competing AI assistants face restrictions. The European Commission's Digital Markets Act (DMA) aims to prevent such unequal treatment by 'gatekeeper' platforms. This draft requirement is part of the EU's broader antitrust efforts to promote fair competition in digital markets.

<details><summary>References</summary>
<ul>
<li><a href="https://www.androidauthority.com/eu-android-ai-google-search-mandates-3688186/">Rival AI assistants could soon gain full access to... - Android Authority</a></li>
<li><a href="https://en.actualidadgadget.com/The-EU-is-putting-pressure-on-Google-and-forcing-it-to-open-Android-to-AI-assistants-that-rival-Gemini./">The EU puts pressure on Google and forces it to open Android to AI ...</a></li>

</ul>
</details>

**Tags**: `#EU regulation`, `#Android`, `#AI assistants`, `#Google`, `#antitrust`

---