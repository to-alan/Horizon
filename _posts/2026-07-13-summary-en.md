---
layout: default
title: "Horizon Summary: 2026-07-13 (EN)"
date: 2026-07-13
lang: en
---

> From 290 items, 26 important content pieces were selected

---

1. [PostgreSQL rewritten in Rust passes all regression tests](#item-1) ⭐️ 9.0/10
2. [Cpp2Rust: Automatic C++ to Safe Rust Translation](#item-2) ⭐️ 9.0/10
3. [Ruff: Blazing Fast Python Linter and Formatter in Rust](#item-3) ⭐️ 9.0/10
4. [Build and Ship Mac/iOS Apps Without Xcode GUI](#item-4) ⭐️ 8.0/10
5. [Apple SpeechAnalyzer API Benchmark: Faster but Less Accurate Than Whisper](#item-5) ⭐️ 8.0/10
6. [Deep Dive into Sega CD Silpheed's Engineering](#item-6) ⭐️ 8.0/10
7. [Samsung Health threatens data deletion if users opt out of AI training](#item-7) ⭐️ 8.0/10
8. [Open Data Preserved Climate.gov After Shutdown](#item-8) ⭐️ 8.0/10
9. [Pydantic Releases Pydantic AI Agent Framework](#item-9) ⭐️ 8.0/10
10. [Public APIs Repository: Curated Free API List](#item-10) ⭐️ 8.0/10
11. [Microsoft releases TRELLIS.2 for fast 3D generation](#item-11) ⭐️ 8.0/10
12. [ComfyUI: A Powerful Modular Graph Interface for Diffusion Models](#item-12) ⭐️ 8.0/10
13. [Google Releases Open-Source Gemini CLI Tool for Terminal](#item-13) ⭐️ 8.0/10
14. [OpenAI Releases Codex CLI: Lightweight Coding Agent for Terminal](#item-14) ⭐️ 8.0/10
15. [Microsoft Releases MXC Sandboxed Code Execution System](#item-15) ⭐️ 8.0/10
16. [Screenpipe: Local AI Memory Recorder for Agents](#item-16) ⭐️ 8.0/10
17. [InfluxDB 3 Core Released as Open Source Time Series Database](#item-17) ⭐️ 8.0/10
18. [Tailscale Open-Sources Core VPN Daemon and CLI](#item-18) ⭐️ 8.0/10
19. [Cloudflared: Cloudflare Tunnel Client](#item-19) ⭐️ 8.0/10
20. [Kubescape: Open-Source Kubernetes Security Platform](#item-20) ⭐️ 8.0/10
21. [SOPS: Versatile Secrets Management Tool Now Under CNCF](#item-21) ⭐️ 8.0/10
22. [Telegram's t.me Domain Suspended by Registry](#item-22) ⭐️ 8.0/10
23. [CrashStealer malware targets Mac, steals from 14 password managers](#item-23) ⭐️ 8.0/10
24. [Chinese Team Sets 28.04% Efficiency Record for Perovskite-Organic Tandem Solar Cells](#item-24) ⭐️ 8.0/10
25. [China's New EV Battery Safety Standard: No Fire for 2 Hours After Thermal Runaway](#item-25) ⭐️ 8.0/10
26. [GPUHedge reduces serverless GPU cold start p95 latency from 117s to 30s](#item-26) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PostgreSQL rewritten in Rust passes all regression tests](https://github.com/malisper/pgrust) ⭐️ 9.0/10

The open-source project pgrust has achieved a milestone by passing 100% of PostgreSQL 18.3 regression tests, covering over 46,000 queries. The project is a complete rewrite of PostgreSQL in Rust, aiming for compatibility and performance improvements. This demonstrates the feasibility of rewriting a complex, production-grade database in a memory-safe language like Rust, potentially improving reliability and security. If pgrust matures, it could offer a modern alternative to PostgreSQL with better performance and easier extensibility. pgrust is disk-compatible with PostgreSQL 18.3 and can boot from an existing data directory. An upcoming unreleased version already shows significant performance gains: 50% faster on transaction workloads and ~300x faster on analytical workloads compared to stock PostgreSQL.

rss · GitHub Trending - Daily · Jul 13, 01:33

**Background**: PostgreSQL is a widely used open-source relational database with a large test suite called regression tests that ensure compatibility and correctness. pgrust rewrites PostgreSQL in Rust, a systems programming language known for memory safety and performance, aiming to keep PostgreSQL's behavior while enabling deeper server changes and better performance.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now passing 100% of the Postgres regression tests · GitHub</a></li>
<li><a href="https://pgrust.com/">pgrust — postgres, rewritten in rust</a></li>

</ul>
</details>

**Tags**: `#rust`, `#postgresql`, `#database`, `#reimplementation`, `#systems-programming`

---

<a id="item-2"></a>
## [Cpp2Rust: Automatic C++ to Safe Rust Translation](https://github.com/Cpp2Rust/cpp2rust) ⭐️ 9.0/10

Cpp2Rust, a tool that automatically translates C++ code to safe Rust using Clang's AST, has been introduced, with its algorithm published at PLDI 2026. This tool could significantly lower the barrier for migrating C++ codebases to Rust, promoting safer systems programming and enabling gradual migration from C++ to Rust. Cpp2Rust uses a reference counting model by default to produce fully safe Rust, and also offers an unsafe mode for debugging. It relies on a runtime library (libcc2rs) to handle C pointer semantics via a Ptr<T> type.

rss · GitHub Trending - Rust Daily · Jul 13, 01:41

**Background**: Clang's AST (Abstract Syntax Tree) is a tree representation of C++ source code used by the Clang compiler for analysis and transformation. PLDI (Programming Language Design and Implementation) is a premier conference in programming languages research. Reference counting is a memory management technique used in Rust's Rc and Arc types to share ownership without garbage collection.

<details><summary>References</summary>
<ul>
<li><a href="https://clang.llvm.org/docs/IntroductionToTheClangAST.html">Introduction to the Clang AST — Clang 23.0.0git documentation</a></li>
<li><a href="https://pldi26.sigplan.org/">Pldi 2026</a></li>
<li><a href="https://chomsky.hashnode.dev/rc-and-arc-in-rust-explained-for-beginners-part-1">Rust Rc vs Arc: Beginner's Guide</a></li>

</ul>
</details>

**Tags**: `#C++`, `#Rust`, `#automatic translation`, `#safe programming`, `#PLDI`

---

<a id="item-3"></a>
## [Ruff: Blazing Fast Python Linter and Formatter in Rust](https://github.com/astral-sh/ruff) ⭐️ 9.0/10

Ruff is an extremely fast Python linter and code formatter written in Rust, claiming 10-100x speedup over existing tools like Flake8 and Black. Ruff significantly improves Python development workflows by integrating linting, formatting, and import sorting into a single, highly performant tool, reducing CI times and developer friction. Ruff offers drop-in parity with Flake8, isort, and Black, includes over 900 built-in rules, and supports caching and automatic fixes.

rss · GitHub Trending - Rust Daily · Jul 13, 01:41

**Background**: Python linting and formatting tools help enforce code quality and style but can be slow. Ruff uses Rust's performance to deliver dramatic speed improvements while supporting the same rules as popular tools like Flake8 and Black.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://docs.astral.sh/ruff/formatter/">The Ruff Formatter - Astral Docs</a></li>
<li><a href="https://docs.astral.sh/ruff/">Ruff - Astral Docs</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Rust`, `#linter`, `#formatter`, `#tooling`

---

<a id="item-4"></a>
## [Build and Ship Mac/iOS Apps Without Xcode GUI](https://scottwillsey.com/building-and-shipping-mac-and-ios-apps-without-ever-opening-xcode/) ⭐️ 8.0/10

A detailed guide demonstrates how to build, sign, notarize, and upload Mac and iOS apps to App Store Connect entirely via command-line tools like xcodebuild and altool, bypassing Xcode's GUI completely. This approach enables fully automated CI/CD pipelines for Apple platform development, reduces dependency on Xcode's heavy GUI, and empowers developers who prefer terminal workflows or work in headless environments. The workflow uses xcodebuild for building, altool for uploading, and standard signing and notarization commands; it requires installing Xcode command-line tools and setting up App Store Connect API keys.

hackernews · speckx · Jul 13, 18:22 · [Discussion](https://news.ycombinator.com/item?id=48896665)

**Background**: Xcode is Apple's integrated development environment, but many core tasks like compiling, signing, and uploading can be performed via command-line tools included in the Xcode Command Line Tools package. Tools like xcodebuild and altool allow developers to automate builds and releases without opening the GUI, which is especially useful for continuous integration and deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/library/archive/technotes/tn2339/_index.html">Technical Note TN2339: Building from the Command Line with Xcode...</a></li>
<li><a href="https://keith.github.io/xcode-man-pages/altool.1.html">altool (1) - GitHub Pages</a></li>
<li><a href="https://github.com/fastlane/fastlane">GitHub - fastlane/fastlane: 🚀 The easiest way to automate building and releasing your iOS and Android apps</a></li>

</ul>
</details>

**Discussion**: Commenters shared related open-source projects like strudel (a CLI for building/signing/notarizing), xtool (build iOS apps from Linux), and Axiom (toolkit for LLM-assisted development). Some raised security concerns about running the automation agent on a Mac without sandboxing, referencing a recent incident where xAI uploaded a user's home directory.

**Tags**: `#iOS development`, `#macOS`, `#Xcode alternatives`, `#command-line tools`, `#CI/CD`

---

<a id="item-5"></a>
## [Apple SpeechAnalyzer API Benchmark: Faster but Less Accurate Than Whisper](https://get-inscribe.com/blog/apple-speech-api-benchmark.html) ⭐️ 8.0/10

Apple's new SpeechAnalyzer API, introduced at WWDC 2025, has been benchmarked against OpenAI's Whisper-Large-V2 and Whisper Small, showing it runs approximately three times faster than Whisper Small while being the most accurate on-device speech engine tested. This benchmark highlights Apple's push for on-device speech recognition, potentially threatening third-party apps that simply wrap Whisper by offering native, faster, and more private transcription on macOS and iOS. It also signals a shift toward real-time, locally processed ASR, which could improve user experience across Apple's ecosystem. The API beats every Whisper model shipped, including Whisper Small, on both clean and noisy subsets of LibriSpeech, while running three times faster than Whisper Small. However, it is slightly less accurate than Whisper-Large-V2, according to the benchmark on a math lecture.

hackernews · get-inscribe · Jul 13, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48894752)

**Background**: Whisper is an open-source automatic speech recognition (ASR) model developed by OpenAI, known for its robustness to accents and noise, but it is typically run on cloud servers or powerful desktops. Apple's SpeechAnalyzer API is designed for on-device processing, offering lower latency and better privacy. The benchmark compares speed and accuracy on LibriSpeech and real-world recordings.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48894752">Apple's new SpeechAnalyzer API, benchmarked against Whisper and its predecessor | Hacker News</a></li>
<li><a href="https://www.callstack.com/blog/on-device-speech-transcription-with-apple-speechanalyzer">On-Device Speech Transcription with Apple SpeechAnalyzer and AI SDK</a></li>
<li><a href="https://www.argmaxinc.com/blog/apple-and-argmax">Apple SpeechAnalyzer and Argmax WhisperKit - Argmax</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Whisper may not be the state-of-the-art baseline, suggesting models like Nvidia's Nemotron and Parakeet, Mistral's Voxtral, and Cohere Transcribe. Some expressed concern that Apple might obsolete paid Whisper-wrapper apps with a native recorder GUI, while others praised the API's speed for live transcription and shared integrations into projects like Handy.computer.

**Tags**: `#Apple`, `#Speech Recognition`, `#Whisper`, `#Benchmark`, `#Machine Learning`

---

<a id="item-6"></a>
## [Deep Dive into Sega CD Silpheed's Engineering](https://fabiensanglard.net/silpheed/index.html) ⭐️ 8.0/10

Fabien Sanglard published a detailed technical analysis of the Sega CD game Silpheed, explaining how developers used FMV and real-time 3D tricks to create a cinematic experience. This analysis reveals the innovative engineering behind one of the Sega CD's most impressive titles, showing how developers maximized limited hardware for groundbreaking visuals. The article details how Silpheed used full-motion video backgrounds with real-time sprite overlays, creating a pseudo-3D look that fooled players into thinking it was polygon-based.

hackernews · ibobev · Jul 13, 14:52 · [Discussion](https://news.ycombinator.com/item?id=48893639)

**Background**: The Sega CD was an add-on for the Sega Genesis that brought CD-ROM capabilities but had limited 3D hardware. Silpheed, developed by Game Arts, is a notable title that used FMV creatively. Fabien Sanglard is known for in-depth retro game engineering analyses.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Silpheed">Silpheed - Wikipedia</a></li>
<li><a href="https://racketboy.com/retro/sega-cd-101-a-beginners-guide">Sega CD 101: A Beginner’s Guide – RetroGaming with Racketboy</a></li>
<li><a href="https://jsgroth.dev/blog/posts/sega-cd-pcm-overview/">Sega CD PCM Chip - An Overview | jsgroth's blog</a></li>

</ul>
</details>

**Discussion**: Comments include technical corrections about the Sega CD's audio setup and appreciation for the game's techniques. Some users shared demoscene examples showing similar capabilities.

**Tags**: `#game development`, `#retro computing`, `#Sega CD`, `#technical analysis`, `#Fabien Sanglard`

---

<a id="item-7"></a>
## [Samsung Health threatens data deletion if users opt out of AI training](https://neow.in/cWsyMTV3) ⭐️ 8.0/10

Samsung Health has updated its terms to require users to consent to their health data being used for AI training, or else the app will delete their data and limit functionality. This raises significant privacy concerns, as it forces users to choose between losing their health data or allowing Samsung to use sensitive information for AI training, potentially setting a precedent for other health apps. The data categories targeted include sleep, medications, medical records, and cycle tracking details; refusal not only deletes data but also disables key features, effectively making the device less usable.

hackernews · bundie · Jul 13, 20:01 · [Discussion](https://news.ycombinator.com/item?id=48897991)

**Background**: AI training on health data can improve diagnostics and personalized care, but it also raises ethical and privacy issues. Companies like Samsung often collect user data to train models, but forcing consent with data deletion is a controversial approach that may violate user trust and regulatory norms.

<details><summary>References</summary>
<ul>
<li><a href="https://www.coursera.org/specializations/artificial-intelligence-for-healthcare">Artificial Intelligence for Healthcare | Coursera</a></li>
<li><a href="https://online.stanford.edu/artificial-intelligence/ai-healthcare-professionals">AI for Healthcare Professionals - Stanford Online</a></li>

</ul>
</details>

**Discussion**: Comments are largely critical, with users expressing frustration over the coercive approach and comparing it to other companies' practices. Some sarcastically suggest that data deletion might be a benefit, while others highlight the app's poor functionality and data export issues.

**Tags**: `#privacy`, `#AI`, `#data deletion`, `#Samsung Health`, `#ethics`

---

<a id="item-8"></a>
## [Open Data Preserved Climate.gov After Shutdown](https://werd.io/climate-gov-was-destroyed-open-data-saved-it/) ⭐️ 8.0/10

Climate.gov was taken down, but open data activists archived its datasets, preserving public access to vital climate information. This event underscores the importance of open data and data permanence for government transparency, scientific research, and public accountability. The archived site relies on donations to remain operational, and dynamic backend services were not fully preserved, limiting some functionality.

hackernews · benwerd · Jul 13, 19:57 · [Discussion](https://news.ycombinator.com/item?id=48897945)

**Background**: Open data refers to data that is freely available for anyone to access, use, and share. Data permanence is the concept that digital data should persist indefinitely, protected from deletion or loss. Government websites can be removed due to policy changes, but open data initiatives and grassroots archiving efforts can help ensure continued access.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_remanence">Data remanence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Digital_permanence">Digital permanence - Wikipedia</a></li>
<li><a href="https://opendatahandbook.org/glossary/en/terms/data-preservation/">Data preservation</a></li>

</ul>
</details>

**Discussion**: Commenters raised concerns about the long-term viability of donation-based archiving, with one noting that government data should be public domain. Others suggested using distributed systems like IPFS for static government content, while some questioned the accuracy of the claim that such preservation relies solely on donations.

**Tags**: `#open data`, `#climate`, `#government`, `#data preservation`

---

<a id="item-9"></a>
## [Pydantic Releases Pydantic AI Agent Framework](https://github.com/pydantic/pydantic-ai) ⭐️ 8.0/10

Pydantic has announced pydantic-ai, a Python agent framework for building production-grade GenAI applications and workflows, leveraging Pydantic validation and modern Python type hints. As a framework built by the team behind Pydantic—which is already the validation layer for many major LLM SDKs—pydantic-ai could become a standard for building reliable, type-safe AI agents in Python. The framework supports dozens of model providers including OpenAI, Anthropic, Gemini, and DeepSeek, and integrates seamlessly with Pydantic Logfire for observability and debugging.

rss · GitHub Trending - Python Daily · Jul 13, 01:40

**Background**: Pydantic is a popular Python library for data validation using type hints. The team previously created FastAPI, a widely used web framework. The new agent framework aims to bring the same ergonomic design to GenAI development.

<details><summary>References</summary>
<ul>
<li><a href="https://pydantic.dev/docs/ai/overview/">Pydantic AI | Pydantic Docs</a></li>
<li><a href="https://github.com/pydantic/pydantic-ai">GitHub - pydantic/pydantic-ai: AI Agent Framework, the Pydantic way · GitHub</a></li>

</ul>
</details>

**Tags**: `#python`, `#ai`, `#agent-framework`, `#pydantic`, `#llm`

---

<a id="item-10"></a>
## [Public APIs Repository: Curated Free API List](https://github.com/public-apis/public-apis) ⭐️ 8.0/10

The public-apis repository on GitHub, a community-curated list of free APIs, continues to be actively maintained and updated with new APIs across many domains. This repository is a vital resource for developers, saving time in discovering free APIs for prototyping and learning. Its community-driven nature ensures diversity and reliability. The repository is also sponsored by APILayer, which features its own APIs at the top of the page, though the main list remains community-curated. It includes APIs from categories like animals, music, and finance.

rss · GitHub Trending - Python Daily · Jul 13, 01:40

**Background**: APIs (Application Programming Interfaces) allow different software applications to communicate. A curated list like public-apis helps developers quickly find free APIs without searching multiple sources. The repository has over 300,000 stars on GitHub, reflecting its popularity and trust.

**Tags**: `#APIs`, `#open-source`, `#developer tools`, `#resources`

---

<a id="item-11"></a>
## [Microsoft releases TRELLIS.2 for fast 3D generation](https://github.com/microsoft/TRELLIS.2) ⭐️ 8.0/10

Microsoft has released TRELLIS.2, a 4-billion-parameter 3D generative model that uses a novel O-Voxel representation to produce high-quality 3D assets from images at resolutions up to 1536³ in about one minute. This model significantly advances image-to-3D generation by enabling arbitrary topology handling, full PBR materials, and extremely fast inference, making 3D asset creation more accessible for gaming, VR, and design industries. TRELLIS.2 uses a 'field-free' sparse voxel structure called O-Voxel, which allows it to model open surfaces, non-manifold geometry, and internal structures without lossy conversion, and it supports attributes like base color, roughness, metallic, and opacity.

rss · GitHub Trending - Python Daily · Jul 13, 01:40

**Background**: 3D generation typically relies on representations like NeRFs, 3D Gaussians, or meshes, often requiring separate optimization or rendering steps. This work builds on structured latent representations that unify different output formats, enabling scalable and versatile generation as shown in prior research.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.01506">[2412.01506] Structured 3D Latents for Scalable and Versatile 3D Generation</a></li>
<li><a href="https://openaccess.thecvf.com/content/CVPR2025/papers/Xiang_Structured_3D_Latents_for_Scalable_and_Versatile_3D_Generation_CVPR_2025_paper.pdf">Structured 3D Latents for Scalable and Versatile 3D Generation</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#machine learning`, `#computer vision`, `#Microsoft`, `#generative AI`

---

<a id="item-12"></a>
## [ComfyUI: A Powerful Modular Graph Interface for Diffusion Models](https://github.com/Comfy-Org/ComfyUI) ⭐️ 8.0/10

ComfyUI is a widely-used open-source node-based graph interface for diffusion models, enabling powerful AI-driven content creation without coding. It democratizes complex AI workflows, giving creatives total control over every parameter and output, and serves as a key tool in the open-source AI ecosystem. ComfyUI natively supports the latest open-source models and provides API nodes for closed-source models; it is available on Windows, Linux, and macOS via desktop app, portable install, or cloud.

rss · GitHub Trending - Python Daily · Jul 13, 01:40

**Background**: Diffusion models are a class of generative AI that create images, videos, and audio by iteratively denoising random noise. Traditionally, running these models required command-line or script-based interfaces. ComfyUI provides a visual node graph that represents each step of the generation pipeline, making complex workflows easier to design, share, and reproduce without any coding.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Comfy-Org/ComfyUI">Comfy-Org/ComfyUI: The most powerful and modular diffusion model ...</a></li>
<li><a href="https://opensourceai.tech/tool/comfyui.html">ComfyUI — Node - graph control over image pipelines | Open-Source AI</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#AI`, `#GUI`, `#backend`, `#modular`

---

<a id="item-13"></a>
## [Google Releases Open-Source Gemini CLI Tool for Terminal](https://github.com/google-gemini/gemini-cli) ⭐️ 8.0/10

Google has released an open-source CLI tool called Gemini CLI, allowing developers to interact with Gemini AI models directly from the terminal. It is available via npm, Homebrew, and other package managers. This tool provides a lightweight, terminal-first interface for developers to leverage Gemini's powerful AI capabilities, including a 1M token context window and built-in tools, potentially accelerating AI integration in development workflows. Gemini CLI offers a free tier with 60 requests per minute and 1,000 requests per day, access to Gemini 3 models, and supports MCP for extensibility. It is licensed under Apache 2.0.

rss · GitHub Trending - TypeScript Daily · Jul 13, 01:42

**Background**: Gemini CLI is a command-line interface for Google's Gemini AI models, which are large language models capable of reasoning and processing large contexts. The CLI provides built-in tools like Google Search grounding, file operations, and shell commands, making it a versatile agent for developers.

**Tags**: `#AI`, `#CLI`, `#Google Gemini`, `#Open Source`

---

<a id="item-14"></a>
## [OpenAI Releases Codex CLI: Lightweight Coding Agent for Terminal](https://github.com/openai/codex) ⭐️ 8.0/10

OpenAI has released Codex CLI, a lightweight coding agent that runs locally in the terminal, available for macOS, Linux, and Windows. This tool brings AI-assisted coding directly to the developer's terminal without requiring an IDE or cloud dependency, potentially streamlining workflows for many developers. Codex CLI can be installed via curl, npm, or Homebrew, and requires signing in with a ChatGPT account or using an API key. It is licensed under Apache-2.0.

rss · GitHub Trending - Rust Daily · Jul 13, 01:41

**Background**: Codex is OpenAI's AI system that translates natural language into code. Previously available as a cloud-based service or IDE plugin, Codex CLI now offers a local terminal-based version.

**Tags**: `#AI`, `#coding agent`, `#OpenAI`, `#developer tools`, `#terminal`

---

<a id="item-15"></a>
## [Microsoft Releases MXC Sandboxed Code Execution System](https://github.com/microsoft/mxc) ⭐️ 8.0/10

Microsoft has open-sourced MXC (Microsoft eXecution Container), a policy-driven sandboxed code execution system for running untrusted code across Windows, Linux, and macOS with multiple containment backends such as process containers, VMs, and OS sandboxes. MXC addresses critical needs in AI safety and untrusted code containment by providing a unified, cross-platform sandboxing layer that can isolate model outputs, plugins, and tools. It is particularly relevant as AI agents and code generation tools require secure execution environments. MXC uses a JSON-based configuration schema to define execution parameters and security policies, and includes a TypeScript SDK with one-shot and state-aware APIs. The current early preview has known overly permissive policies and should not be treated as a security boundary.

rss · GitHub Trending - Rust Daily · Jul 13, 01:41

**Background**: Sandboxed code execution involves running untrusted programs in isolated environments to prevent them from harming the host system. MXC builds on Microsoft's existing sandbox technologies like Windows Sandbox and adds cross-platform support with a policy-driven approach. It is designed for scenarios such as executing output from large language models or running third-party plugins safely.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/mxc">GitHub - microsoft / mxc : Policy-driven, layered isolation and...</a></li>
<li><a href="https://devlery.com/en/blog/microsoft-mxc-agent-sandbox">Microsoft MXC Preview Is an OS Sandbox for Windows AI... - Devlery</a></li>

</ul>
</details>

**Tags**: `#sandbox`, `#security`, `#AI safety`, `#microsoft`, `#code execution`

---

<a id="item-16"></a>
## [Screenpipe: Local AI Memory Recorder for Agents](https://github.com/screenpipe/screenpipe) ⭐️ 8.0/10

Screenpipe, a YC-backed tool, now offers a source-available license and claims its AI PII model outperforms Google, Microsoft, and OpenAI on computer recording data, running at 9ms on consumer devices. This enables private, local recording of all user activity for AI agents, potentially transforming productivity and automation workflows without compromising privacy. It integrates with OpenClaw and Hermes agent and over 100 apps, and the desktop app is available for download with auto-updates.

rss · GitHub Trending - Rust Daily · Jul 13, 01:41

**Background**: Screenpipe is a local-first tool that continuously records screen and audio to create searchable memory for AI agents. It is part of a growing ecosystem of personal AI assistants like OpenClaw and Hermes agent, which aim to run on user devices and leverage captured data for automation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>
<li><a href="https://github.com/openclaw/openclaw">GitHub - openclaw/openclaw: Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞</a></li>
<li><a href="https://hermes-agent.nousresearch.com/">Hermes Agent — The Agent That Grows With You</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Privacy`, `#Screen Recording`, `#Automation`, `#Memory`

---

<a id="item-17"></a>
## [InfluxDB 3 Core Released as Open Source Time Series Database](https://github.com/influxdata/influxdb) ⭐️ 8.0/10

InfluxData has released InfluxDB 3 Core, an open-source time series database built on Apache Arrow, DataFusion, and Parquet, achieving general availability since April 2025. It offers fast query response times under 10ms for last-value queries and supports SQL and InfluxQL. This release marks a significant evolution of a widely-used time series database, leveraging modern columnar formats to improve performance and scalability. It offers a free, open-source alternative to proprietary solutions for real-time analytics and monitoring. InfluxDB 3 Core features a diskless architecture with object storage support, an embedded Python VM for plugins, and compatibility with InfluxDB 1.x and 2.x APIs. It uses Apache Parquet for persistence and runs on a single binary.

rss · GitHub Trending - Rust Daily · Jul 13, 01:41

**Background**: Apache Arrow provides a language-independent columnar memory format for efficient data analytics. DataFusion is an extensible query engine in Rust using Arrow's format. Apache Parquet is a column-oriented storage format. InfluxDB is a popular time series database, and v3 Core represents a major architectural shift.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Apache_Arrow">Apache Arrow - Wikipedia</a></li>
<li><a href="https://github.com/apache/datafusion">GitHub - apache/datafusion: Apache DataFusion SQL Query Engine · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apache_Parquet">Apache Parquet - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#InfluxDB`, `#time series database`, `#Apache Arrow`, `#DataFusion`, `#open source`

---

<a id="item-18"></a>
## [Tailscale Open-Sources Core VPN Daemon and CLI](https://github.com/tailscale/tailscale) ⭐️ 8.0/10

Tailscale has made its core `tailscaled` daemon and `tailscale` CLI tool open source, available in the tailscale/tailscale GitHub repository. This move allows the community to inspect, audit, and contribute to the underlying VPN technology, increasing trust and fostering wider adoption of secure networking based on WireGuard. The repository includes the daemon and CLI for Linux, Windows, macOS, and partial support for FreeBSD and OpenBSD, but does not contain the mobile GUI code for iOS and Android.

rss · GitHub Trending - Go Daily · Jul 13, 01:37

**Background**: Tailscale is a VPN service that simplifies secure networking by leveraging WireGuard, a modern and efficient VPN protocol. The open-source release of its core components allows users to understand and customize their VPN setup. This repository contains the majority of Tailscale's open source code, making it a key resource for transparency and community development.

**Tags**: `#networking`, `#VPN`, `#WireGuard`, `#security`, `#Go`

---

<a id="item-19"></a>
## [Cloudflared: Cloudflare Tunnel Client](https://github.com/cloudflare/cloudflared) ⭐️ 8.0/10

Cloudflared is the command-line client for Cloudflare Tunnel, a daemon that proxies traffic from Cloudflare's network to your origins without exposing firewall ports. It supports Layer 4 traffic (TCP) for protocols like SSH and RDP. This tool enables secure, outbound-only connections to origins, eliminating the need for public IP addresses or open ports. It is widely adopted by developers and DevOps for exposing local services securely via Cloudflare's global network. Cloudflared can be installed via standalone binaries, Docker, Debian/RPM packages, or Homebrew. It also supports accessing Tunnel origins for TCP traffic at Layer 4 without HTTP/WebSocket, useful for SSH and RDP.

rss · GitHub Trending - Go Daily · Jul 13, 01:37

**Background**: A tunneling daemon creates a secure, encrypted connection between two networks, often used to expose internal services to the internet without opening firewall ports. Cloudflare Tunnel uses an outbound-only connection, meaning the daemon initiates a link to Cloudflare's edge, which then routes traffic to the origin. This approach enhances security by keeping the origin's network closed and reducing attack surface.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/tunnel/">Cloudflare Tunnel</a></li>
<li><a href="https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/">Cloudflare Tunnel · Cloudflare One docs</a></li>

</ul>
</details>

**Tags**: `#networking`, `#tunneling`, `#cloudflare`, `#security`, `#devops`

---

<a id="item-20"></a>
## [Kubescape: Open-Source Kubernetes Security Platform](https://github.com/kubescape/kubescape) ⭐️ 8.0/10

Kubescape is a CNCF incubating project that provides comprehensive Kubernetes security, including risk analysis, compliance scanning, and misconfiguration detection across IDE, CI/CD, and clusters. This project addresses critical security needs in Kubernetes environments, helping DevOps and security teams save time and resources by automating security checks throughout the development lifecycle. Kubescape supports hardening, posture management, and runtime security, and is available as an open-source tool with badges indicating CNCF incubation status and OpenSSF Best Practices compliance.

rss · GitHub Trending - Go Daily · Jul 13, 01:37

**Background**: Kubernetes is a container orchestration platform that manages containerized applications. Security in Kubernetes is complex due to its dynamic nature and many components. Kubescape helps users identify vulnerabilities and misconfigurations early in development and at runtime.

**Tags**: `#Kubernetes`, `#Security`, `#Open Source`, `#DevOps`, `#Go`

---

<a id="item-21"></a>
## [SOPS: Versatile Secrets Management Tool Now Under CNCF](https://github.com/getsops/sops) ⭐️ 8.0/10

SOPS (Secrets OPerationS) is a mature, open-source tool for encrypting and managing secrets in files, supporting multiple formats and key management backends. It was originally created at Mozilla in 2015 and accepted as a CNCF Sandbox project in 2023. SOPS simplifies secret management for DevOps and security teams by allowing encryption of configuration files with keys managed by cloud KMS or offline tools like age and PGP. Its broad backend support and integration with CI/CD pipelines make it a critical component in secure software delivery. SOPS supports encryption and decryption of YAML, JSON, ENV, INI, and binary files, and can use AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud KMS, age, and PGP as key management backends. It is written in Go and licensed under MPL 2.0.

rss · GitHub Trending - Go Daily · Jul 13, 01:37

**Background**: Secrets management involves securely storing and accessing sensitive data like passwords, API keys, and certificates. SOPS enables users to encrypt such data directly within configuration files, allowing them to be committed to version control without exposing plaintext secrets. The tool's ability to leverage various cloud and offline key management systems provides flexibility across different deployment environments.

<details><summary>References</summary>
<ul>
<li><a href="https://support.huaweicloud.com/intl/en-us/usermanual-dew/dew_01_0094.html">Using KMS for Encryption_Data Encryption Workshop-Huawei Cloud</a></li>

</ul>
</details>

**Tags**: `#secrets management`, `#encryption`, `#devops`, `#security`, `#Go`

---

<a id="item-22"></a>
## [Telegram's t.me Domain Suspended by Registry](https://www.nodeseek.com/post-820652-1) ⭐️ 8.0/10

Telegram's short-link domain t.me has been suspended at the registry level, with WHOIS now showing a 'serverHold' status that completely blocks DNS resolution. All t.me links are currently inaccessible, breaking link sharing functionality. This disruption affects millions of Telegram users worldwide who rely on t.me links for sharing channels, groups, and bots. The incident highlights the risks of centralized domain control and the fragility of internet infrastructure even for major platforms. The 'serverHold' status is a registry-level suspension that disables the entire DNS zone, meaning the domain cannot be resolved by any DNS server. The Telegram app itself remains operational, but all t.me links are broken until the suspension is lifted.

rss · NodeSeek · Jul 13, 23:40

**Background**: In the domain name system, a 'serverHold' status is a registry-imposed hold that prevents a domain from being used for any services. This is different from 'clientHold' which is set by the registrar. When a domain is placed on serverHold, its DNS records are not published, causing all associated services like websites and email to stop working. This can occur for various reasons including legal issues, non-compliance, or expiration.

<details><summary>References</summary>
<ul>
<li><a href="https://www.namecheap.com/support/knowledgebase/article.aspx/10717/46/why-was-my-domain-suspended-with-a-serverhold-or-clienthold-status/">Why was my domain suspended with a serverHold or clientHold ...</a></li>
<li><a href="https://sidebysidedomains.com/blog/serverhold-domain-status.html">"ServerHold" Domain Status Explained: Causes & Solutions ...</a></li>

</ul>
</details>

**Tags**: `#telegram`, `#domain`, `#dns`, `#internet infrastructure`, `#service disruption`

---

<a id="item-23"></a>
## [CrashStealer malware targets Mac, steals from 14 password managers](https://www.ithome.com/0/976/263.htm) ⭐️ 8.0/10

Jamf Threat Labs disclosed CrashStealer malware that targets macOS users, stealing credentials from 14 password managers and 80 cryptocurrency wallet extensions. Apple has revoked the malicious app's signature after being notified. This attack is significant because it targets widely used password managers and crypto wallets, putting millions of users at risk. Apple's swift revocation of the signature shows the severity, but the malware's ability to bypass Gatekeeper highlights ongoing security challenges for macOS. The malware, disguised as a tool called Werkbit, used a valid Developer ID to bypass Gatekeeper and prompted users for their Mac password to load the final payload. It harvested data from browsers, password managers including 1Password, Bitwarden, LastPass, and crypto wallets, and installed persistence in ~/Library/Caches/com.apple.crashreporter/.

rss · IT之家 · Jul 13, 23:41

**Background**: Gatekeeper is a macOS security feature that verifies downloaded apps before running, blocking untrusted software by default. A Developer ID signed by Apple allows apps to pass Gatekeeper checks. CrashStealer abused this by using a stolen or acquired Developer ID to appear legitimate.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gatekeeper_(macOS)">Gatekeeper ( macOS ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_Developer_Tools">Apple Developer Tools</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#macOS`, `#password manager`, `#malware`, `#Apple`

---

<a id="item-24"></a>
## [Chinese Team Sets 28.04% Efficiency Record for Perovskite-Organic Tandem Solar Cells](https://www.ithome.com/0/976/233.htm) ⭐️ 8.0/10

A Chinese research team led by Li Yongfang and Meng Lei achieved a certified steady-state photoelectric conversion efficiency of 28.04% for perovskite-organic tandem solar cells, published in Nature. The device also demonstrated outstanding stability, retaining 90% of initial efficiency after 625 hours of continuous illumination. This record-breaking efficiency surpasses previous benchmarks for perovskite-organic tandem cells, bringing this lightweight and flexible solar technology closer to practical applications such as building-integrated photovoltaics, portable electronics, and space power. The improved stability addresses a critical barrier to commercialization. The team introduced a photo-transformable additive molecule TDB (4-[3-(trifluoromethyl)-3H-diazirin-3-yl]benzylamine) into the wide-bandgap perovskite precursor, enabling a two-stage strategy that suppresses halide segregation and enhances device stability. The efficiency was certified by an independent third party.

rss · IT之家 · Jul 13, 15:11

**Background**: Perovskite solar cells are a next-generation photovoltaic technology offering high efficiency and low-cost fabrication. Tandem solar cells stack two or more light-absorbing layers with different bandgaps to capture a broader spectrum of sunlight, overcoming the Shockley-Queisser limit of single-junction cells. The perovskite-organic tandem combines a wide-bandgap perovskite front cell with an organic back cell, but has historically suffered from instability due to halide segregation under light. The TDB additive introduced in this work serves as a dynamic regulator to mitigate this issue.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41586-026-10869-x">Perovskite–organic tandem solar cells with a photo ... - Nature</a></li>
<li><a href="https://www.nature.com/articles/s41578-023-00642-1">Perovskite–organic tandem solar cells - Nature Reviews Materials</a></li>

</ul>
</details>

**Tags**: `#Perovskite Solar Cells`, `#Solar Energy`, `#Photovoltaics`, `#Efficiency Record`, `#Nature`

---

<a id="item-25"></a>
## [China's New EV Battery Safety Standard: No Fire for 2 Hours After Thermal Runaway](https://www.36kr.com/p/3893470914870144) ⭐️ 8.0/10

Two mandatory national standards GB 38031-2025 and GB 18384-2025 took effect on July 1, 2026, requiring EV batteries to not catch fire or explode for at least 2 hours after thermal runaway, replacing the old 5-minute warning rule. The new standards also add bottom impact tests and 300 fast-charge cycle safety tests. This is the strictest EV battery safety regulation in China's history, raising compliance costs by 15-20% and accelerating industry consolidation by squeezing smaller battery makers. Consumers will benefit from lower fire risks, but may face higher vehicle prices in the long run. Compliance costs per vehicle are estimated to increase by 4,000-6,500 RMB, with battery pack modifications, production line upgrades, and testing expenses. Leading companies like CATL and BYD have already passed all tests, while 30-40% of smaller cell makers are expected to exit the market.

rss · 36氪 - 24小时热榜 · Jul 13, 03:53

**Background**: Thermal runaway is a chain reaction inside a lithium battery caused by internal short circuits or overheating, leading to uncontrollable temperature rise and potential fire or explosion. BYD's blade battery is a structural innovation using LFP chemistry that passes nail penetration tests with minimal temperature rise. BMS (Battery Management System) monitors voltage, temperature, and current to ensure safe operation.

<details><summary>References</summary>
<ul>
<li><a href="https://baike.baidu.com/item/电池热失控/67387858">电池热失控（锂电池内短路或过热致链式反应）_百度百科</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/666521979">比亚迪刀片电池技术 - 知乎专栏</a></li>
<li><a href="https://www.byd.com/cn/detail617">电动化上半场完美收官：比亚迪发布第二代刀片电池及闪充技术</a></li>

</ul>
</details>

**Tags**: `#EV batteries`, `#safety standards`, `#China regulation`, `#cost analysis`, `#automotive industry`

---

<a id="item-26"></a>
## [GPUHedge reduces serverless GPU cold start p95 latency from 117s to 30s](https://www.reddit.com/r/MachineLearning/comments/1uvlb6h/gpuhedge_hedging_serverless_gpu_providers/) ⭐️ 8.0/10

GPUHedge is an open-source tool that uses speculative execution across multiple serverless GPU providers to reduce cold start latency, dropping p95 latency from 117 seconds to 30 seconds in benchmarks. Cold start latency is a major pain point for serverless GPU inference, affecting user experience and cost efficiency. GPUHedge's approach could make serverless GPUs more viable for latency-sensitive applications by mitigating the tail latency problem without requiring provider changes. The system works by monitoring the job lifecycle on a primary provider and conditionally launching a backup; the first result passing a validator wins and the losing job is cancelled via the provider's API. In the benchmark, a fixed RunPod → Cerebrium hedge after 10 seconds reduced requests over 60 seconds from 11/36 to 0/36.

reddit · r/MachineLearning · /u/Putrid_Construction3 · Jul 13, 19:20

**Background**: Serverless GPU cold start latency occurs when a GPU model needs to be loaded from scratch before serving inference, which can take tens of seconds to several minutes for large models. This is a known challenge because serverless platforms do not keep GPU memory warm between requests to save costs. Hedging is a technique from distributed systems where multiple redundant requests are sent and the fastest response is used, here applied across different GPU providers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.paralleliq.ai/blog/gpu-ops-serverless-cold-start">Serverless GPU Cold Start Latency: Causes and Solutions</a></li>
<li><a href="https://www.beam.cloud/blog/top-serverless-gpu-providers">The Top Serverless GPU Providers in 2025, Ranked by Cold Start</a></li>

</ul>
</details>

**Tags**: `#serverless`, `#GPU`, `#cold-start`, `#latency`, `#hedging`

---