---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 306 items, 28 important content pieces were selected

---

1. [ZLUDA: CUDA Drop-In Replacement for Non-NVIDIA GPUs](#item-1) ⭐️ 9.0/10
2. [DeepSeek Open-Sources DSpark and DeepSpec Under MIT License](#item-2) ⭐️ 9.0/10
3. [Linux 6.9 regression: LUKS suspend fails to wipe encryption keys](#item-3) ⭐️ 8.0/10
4. [PeerTube: A Decentralized, Federated Alternative to YouTube](#item-4) ⭐️ 8.0/10
5. [Immich 3.0: Major Update to Self-Hosted Photo Platform](#item-5) ⭐️ 8.0/10
6. [Spain Orders Blacklist of Palantir from Public and Private Companies](#item-6) ⭐️ 8.0/10
7. [Strix: Open-Source AI Pentesting Tool Launches](#item-7) ⭐️ 8.0/10
8. [Meta Open-Sources Astryx Design System for 13,000+ Apps](#item-8) ⭐️ 8.0/10
9. [Allen AI Releases olmOCR Toolkit for PDF-to-Text Conversion](#item-9) ⭐️ 8.0/10
10. [VulnClaw: AI-Driven CLI Tool Automates Pen Testing via Natural Language](#item-10) ⭐️ 8.0/10
11. [Open WebUI: A User-Friendly Interface for Multiple LLM Backends](#item-11) ⭐️ 8.0/10
12. [Maigret: OSINT Tool Scans 3000+ Sites for Username Traces](#item-12) ⭐️ 8.0/10
13. [Chrome DevTools MCP Server Enables AI Agents to Control Chrome](#item-13) ⭐️ 8.0/10
14. [Polars: Blazingly Fast DataFrame Library in Rust](#item-14) ⭐️ 8.0/10
15. [Awesome Rust: Curated List of Rust Resources](#item-15) ⭐️ 8.0/10
16. [Kueue: Kubernetes-native Job Queueing for Batch Workloads](#item-16) ⭐️ 8.0/10
17. [Meta Compute: Everyone Wants To Be A Cloud](#item-17) ⭐️ 8.0/10
18. [ECTC 2026 Roundup: EMIB-T, HBM4, Cooling, Photonic Interconnects](#item-18) ⭐️ 8.0/10
19. [Kioxia-SanDisk BiCS10 332-layer NAND enters sampling](#item-19) ⭐️ 8.0/10
20. [Tesla driver charged with homicide after fatal FSD crash, data shows override](#item-20) ⭐️ 8.0/10
21. [Kuaishou's AI arm Keling secures up to $3B funding](#item-21) ⭐️ 8.0/10
22. [Enterprise AI costs spiral out of control; Citigroup, Adobe reportedly restrict model access](#item-22) ⭐️ 8.0/10
23. [Password spraying attack targets Microsoft 365 via Azure CLI](#item-23) ⭐️ 8.0/10
24. [Microsoft invests $2.5B in new company for enterprise AI integration](#item-24) ⭐️ 8.0/10
25. [Meta's cloud move triggers AI infrastructure stock sell-off](#item-25) ⭐️ 8.0/10
26. [Cloudflare to Block Mixed-Use AI Crawlers, Including Google, from September](#item-26) ⭐️ 8.0/10
27. [OpenAI Proposes US Government 5% Stake, May Include Google, Meta](#item-27) ⭐️ 8.0/10
28. [PS3 Store Closure 2027 Spurs Emergency Game Archiving](#item-28) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ZLUDA: CUDA Drop-In Replacement for Non-NVIDIA GPUs](https://github.com/vosen/ZLUDA) ⭐️ 9.0/10

ZLUDA is an open-source drop-in replacement for CUDA that allows unmodified CUDA applications to run on AMD, Intel, and other non-NVIDIA GPUs with near-native performance. The project recently added CUDA 13.1 compatibility and full support for Llama.cpp on non-NVIDIA hardware. This breaks NVIDIA's long-standing monopoly on CUDA software, enabling broader GPU choice for compute workloads like AI/ML and scientific computing. It significantly reduces vendor lock-in and can accelerate adoption of alternative GPU hardware. ZLUDA achieves near-native performance by translating CUDA API calls to the target GPU's native compute API (e.g., AMD ROCm or Intel Level Zero). The December 2024 v4 release expanded support beyond AMD to include Intel GPUs, and the latest version targets CUDA 13.1.

rss · GitHub Trending - Rust Daily · Jul 2, 01:47

**Background**: CUDA is NVIDIA's proprietary parallel computing platform and API for GPU programming, widely used in deep learning, scientific computing, and high-performance computing. Until ZLUDA, running CUDA-based applications on non-NVIDIA GPUs required manual code porting to alternatives like OpenCL or AMD's ROCm, which is time-consuming and often incomplete.

<details><summary>References</summary>
<ul>
<li><a href="https://itsfoss.gitlab.io/post/zluda-boasts-full-llamacpp-support-better-windows-handling-for-cuda-on-non-nvidia-gpus/">ZLUDA Boasts Full Llama.cpp Support Better Windows... :: IT'S FOSS</a></li>
<li><a href="https://www.topcpu.net/en/news/open-source-cuda-simulation-project-zluda-achieves-breakthrough-progress">Open Source CUDA Simulation Project ZLUDA Achieves Breakthrough...</a></li>
<li><a href="https://www.phoronix.com/news/ZLUDA-CUDA-13.1-Compatibility">ZLUDA Adds CUDA 13.1 Compatibility For Running... - Phoronix</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#GPU`, `#Open Source`, `#Compute`

---

<a id="item-2"></a>
## [DeepSeek Open-Sources DSpark and DeepSpec Under MIT License](https://www.36kr.com/p/3877109219406081) ⭐️ 9.0/10

On June 28, 2025, DeepSeek open-sourced DSpark, an inference acceleration framework, and DeepSpec, a full-stack codebase for training and evaluating speculative decoding algorithms, all under the permissive MIT license. Additionally, they released the boosted model weights DeepSeek-V4-Pro-DSpark and DeepSeek-V4-Flash-DSpark on Hugging Face. This release underscores DeepSeek's exceptional commitment to open source, starkly contrasting with the restrictive practices of other major AI labs like OpenAI and Meta. By freely providing both methodology and implementation, DeepSeek empowers the global developer community to leverage cutting-edge acceleration techniques, potentially accelerating the adoption of speculative decoding and fostering further innovation. DSpark can speed up DeepSeek-V4 inference by up to 85%, according to reports. DeepSpec includes three draft model algorithms, a research paper, and utilities for data preparation, training, and evaluation, all under the MIT license for unrestricted commercial use.

rss · 36氪 - 24小时热榜 · Jul 2, 01:48

**Background**: Speculative decoding is an inference optimization technique that accelerates large language models (LLMs) by having a small draft model predict multiple tokens, which the main model then verifies in parallel, reducing latency while preserving output quality. The MIT license is a permissive open-source license that allows users to freely use, modify, and distribute the code, including for commercial purposes. DeepSeek's release includes both the acceleration framework (DSpark) and the full training/evaluation pipeline (DeepSpec), enabling others to implement speculative decoding on their own models.

<details><summary>References</summary>
<ul>
<li><a href="https://venturebeat.com/orchestration/deepseek-open-sources-dspark-a-new-framework-to-speed-up-llm-inference-by-up-to-85">DeepSeek open sources DSpark, a new framework to speed up LLM ...</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSpec">GitHub - deepseek-ai/ DeepSpec : DeepSpec : a full-stack codebase for...</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-speculative-decoding-for-reducing-latency-in-ai-inference/">An Introduction to Speculative Decoding for Reducing Latency in AI Inference | NVIDIA Technical Blog</a></li>

</ul>
</details>

**Discussion**: The community reaction has been overwhelmingly positive, with Chinese social media users calling Liang Wenfeng a 'living Buddha' and 'saint,' and international observers like Teortaxes praising DeepSeek's 'vast goodwill.' The general sentiment is that DeepSeek is setting a new standard for openness in AI, contrasting sharply with more restrictive players like OpenAI and Meta.

**Tags**: `#DeepSeek`, `#open source`, `#AI`, `#LLM`, `#community`

---

<a id="item-3"></a>
## [Linux 6.9 regression: LUKS suspend fails to wipe encryption keys](https://mathstodon.xyz/@iblech/116769502749142438) ⭐️ 8.0/10

Since Linux kernel 6.9 (released May 2024), the `cryptsetup luksSuspend` command no longer wipes disk-encryption keys from memory during system suspend, a regression discovered via NixOS tests. This regression weakens the security of disk encryption on Linux systems that rely on luksSuspend to protect keys during suspend, especially for Debian users who use the optional cryptsetup-suspend addon. Without key wiping, an attacker with physical access could extract the master key from RAM. The regression went unnoticed because the system still functions normally — encryption keys remain in memory so resume does not prompt for a passphrase. The bug was introduced in Linux 6.9 and affects the `cryptsetup luksSuspend` command, which is an extension primarily used by Debian.

hackernews · IngoBlechschmid · Jul 2, 15:25 · [Discussion](https://news.ycombinator.com/item?id=48763035)

**Background**: LUKS (Linux Unified Key Setup) is a standard for disk encryption. When a system suspends to RAM, the encryption master key typically remains in kernel memory. The `luksSuspend` command was designed to wipe that key on suspend, forcing re-entry of the passphrase on resume. This feature was pioneered by Debian via an optional addon but is not part of the official cryptsetup upstream.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48763035">Since Linux 6.9, LUKS suspend stopped wiping disk-encryption ...</a></li>
<li><a href="https://www.man7.org/linux//man-pages/man8/cryptsetup-luksSuspend.8.html">cryptsetup-luksSuspend (8) - Linux manual page - man7.org</a></li>
<li><a href="https://sesamedisk.com/linux-luks-suspend-regression-security/">Linux LUKS Suspend Regression: Keys Stay - Sesame Disk</a></li>

</ul>
</details>

**Discussion**: Comments on the bug report show mixed reactions. Some users dismiss it as clickbait since the feature is not officially supported upstream, while others emphasize that security regressions are often silent and dangerous. There is disagreement on whether keeping the key in memory during suspend is a real threat for typical users.

**Tags**: `#security`, `#linux`, `#encryption`, `#regression`

---

<a id="item-4"></a>
## [PeerTube: A Decentralized, Federated Alternative to YouTube](https://github.com/Chocobozzz/PeerTube) ⭐️ 8.0/10

PeerTube is an open-source, decentralized video platform that allows anyone to host their own instance and connect with others via the ActivityPub protocol to form a federated network. It provides a privacy-respecting, community-owned alternative to YouTube, reducing dependence on a single centralized service and giving creators more control over their content. PeerTube uses WebTorrent for peer-to-peer streaming to reduce server load and supports video embedding. However, it currently lacks built-in monetization options, which is a significant challenge for professional creators.

hackernews · doener · Jul 2, 11:17 · [Discussion](https://news.ycombinator.com/item?id=48759634)

**Background**: Decentralized video platforms distribute storage and delivery across many nodes instead of relying on a central server. Federation means that different instances can communicate, so users on one instance can follow channels on another, creating a network similar to email. This contrasts with centralized services like YouTube, where all content is hosted on a single company's servers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Odysee">Odysee - Wikipedia</a></li>
<li><a href="https://opensource.com/article/23/3/tour-the-fediverse">A 5-minute tour of the Fediverse | Opensource.com</a></li>
<li><a href="https://www.inmotionhosting.com/blog/what-is-the-fediverse/">What is the Fediverse + 4 Great Apps | InMotion Hosting Blog</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about monetization, with a professional YouTuber highlighting the high cost of video production and the lack of revenue options on PeerTube. Others noted the difficulty of attracting audiences away from established platforms, though some praised its use for open-source tutorials and privacy-focused content.

**Tags**: `#decentralized`, `#video streaming`, `#open-source`, `#federated`, `#PeerTube`

---

<a id="item-5"></a>
## [Immich 3.0: Major Update to Self-Hosted Photo Platform](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

Immich 3.0, a major version release of the open-source self-hosted photo and video management solution, has been announced as a significant update to the platform. As a leading self-hosted alternative to Google Photos and Apple Photos, this major release signals continued improvement in privacy-focused photo management, attracting more users away from cloud services. While specific changelog details were not provided in the summary, version 3.0 typically introduces breaking changes and new features; users should review migration notes before upgrading.

hackernews · hashier · Jul 2, 14:13 · [Discussion](https://news.ycombinator.com/item?id=48761944)

**Background**: Immich is a high-performance, open-source self-hosted photo and video management platform designed to be a drop-in replacement for services like Google Photos. It offers features such as mobile backup, album sharing, and AI-powered search, all while keeping data on the user's own server. The project has gained significant popularity among self-hosting enthusiasts.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/immich-app/immich">GitHub - immich-app/immich: High performance self-hosted photo and ...</a></li>

</ul>
</details>

**Discussion**: Community comments express strong positive sentiment, with users calling Immich a 'no-brainer replacement' for Apple Photos and praising its privacy and self-hosting capabilities. However, some users raise concerns about iOS photo sync performance and compare it with alternatives like Ente, highlighting the encryption features of the latter.

**Tags**: `#immich`, `#self-hosted`, `#photo management`, `#open source`, `#version release`

---

<a id="item-6"></a>
## [Spain Orders Blacklist of Palantir from Public and Private Companies](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv) ⭐️ 8.0/10

Spain has ordered a blacklist of US tech giant Palantir, prohibiting its use by both public and private companies due to security concerns. This action represents a significant regulatory crackdown on a major US data analytics company, reflecting growing European concerns over data sovereignty and foreign tech dependency. The blacklist affects Palantir's data integration and analytics software, which is widely used by government agencies and corporations. The move has sparked debate about whether it is motivated by genuine security risks or political considerations.

hackernews · mgh2 · Jul 2, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48762725)

**Background**: Palantir Technologies is an American company known for its data analytics platforms used by intelligence and defense agencies. It has faced criticism over privacy and surveillance issues. Spain's blacklist comes amid broader European efforts to reduce reliance on US tech firms and strengthen data protection regulations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Palantir">Palantir</a></li>

</ul>
</details>

**Discussion**: Community comments are divided: some users applaud Spain's move as a step toward data sovereignty and privacy protection, while others suspect political motives, noting Spain's recent contracts with Huawei. A few express strong opposition to Palantir, but there is also skepticism about the consistency of Spain's security policies.

**Tags**: `#Palantir`, `#Spain`, `#Data Privacy`, `#Tech Policy`, `#Geopolitics`

---

<a id="item-7"></a>
## [Strix: Open-Source AI Pentesting Tool Launches](https://github.com/usestrix/strix) ⭐️ 8.0/10

Strix, an open-source AI-powered penetration testing tool, has been released on GitHub, offering autonomous AI agents that dynamically find and validate application vulnerabilities with proof-of-concept exploits. This tool democratizes advanced security testing by combining AI with open-source, reducing reliance on manual pentesting and static analysis false positives, potentially transforming how developers and security teams identify and fix vulnerabilities. Strix features multi-agent orchestration, real exploit validation, and integrates with GitHub Actions and CI/CD pipelines for automated scanning on every pull request. It is licensed under Apache 2.0 and available via PyPI.

rss · GitHub Trending - Daily · Jul 2, 01:39

**Background**: Penetration testing traditionally involves manual effort by security experts to simulate attacks and find vulnerabilities. AI-powered tools automate parts of this process, but many rely on static analysis that produces false positives. Strix uses dynamic analysis with autonomous AI agents that behave like real hackers, running code and generating working proof-of-concept exploits to validate findings.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/usestrix/strix">GitHub - usestrix/strix: Open-source AI penetration testing ...</a></li>
<li><a href="https://docs.strix.ai/">Introduction - Strix</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI`, `#pentesting`, `#open-source`, `#vulnerability`

---

<a id="item-8"></a>
## [Meta Open-Sources Astryx Design System for 13,000+ Apps](https://github.com/facebook/astryx) ⭐️ 8.0/10

Meta has open-sourced Astryx, a React-based design system that was used internally across 13,000+ apps over eight years, now available in public beta under the MIT license. It ships over 150 accessible components, brand-level theming, dark mode, templates, and a CLI, all built with StyleX for styling. Astryx is one of the largest internal design systems ever open-sourced, offering a battle-tested, customizable, and AI-agent-ready UI toolkit for the broader developer community. Its design philosophy — open internals, no styling lock-in, and agent-friendly APIs — addresses common pain points in enterprise UI development. Astryx uses StyleX for styling internally but allows consumers to override with any CSS approach (Tailwind, CSS modules, plain CSS) via className. The system also includes a swizzle feature to eject component source into the project for deep customization, and a CLI designed for both humans and AI assistants.

rss · GitHub Trending - Daily · Jul 2, 01:39

**Background**: A design system is a collection of reusable UI components and guidelines that ensure visual and functional consistency across an organization's applications. StyleX is a compile-time CSS-in-JS library developed by Meta, offering the ergonomics of CSS-in-JS with static CSS performance. Astryx leverages StyleX internally but abstracts it from consumers, avoiding build plugin dependencies.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/facebook/astryx">GitHub - facebook/astryx: An open source design system that's fully customizable and agent ready · GitHub</a></li>
<li><a href="https://astryx.atmeta.com/">Astryx Design System</a></li>
<li><a href="https://www.opensourceforu.com/2026/06/meta-open-sources-astryx/">Meta Open-Sources Astryx: An AI-Agent-Ready React Design System - Open Source For You</a></li>

</ul>
</details>

**Tags**: `#react`, `#design-system`, `#open-source`, `#meta`, `#ui`

---

<a id="item-9"></a>
## [Allen AI Releases olmOCR Toolkit for PDF-to-Text Conversion](https://github.com/allenai/olmocr) ⭐️ 8.0/10

Allen AI has released olmOCR, an open-source toolkit that converts PDFs and images into clean, readable plain text or Markdown, optimized for creating LLM training datasets. The latest version v0.4.0 introduces a new model trained with synthetic data and reinforcement learning, boosting benchmark scores by about 4 points. olmOCR addresses a critical bottleneck in LLM data preparation by providing an efficient, high-quality PDF linearization tool that preserves reading order, equations, tables, and handwriting. This enables researchers and companies to more easily curate large-scale, diverse text datasets for training or fine-tuning language models. olmOCR is built on a 7B parameter vision-language model (VLM) called olmOCR-2-7B-1025-FP8, requires a GPU, and costs less than $200 per million pages converted. It also ships a comprehensive benchmark suite, olmOCR-Bench, covering over 7,000 test cases across 1,400 documents.

rss · GitHub Trending - Daily · Jul 2, 01:39

**Background**: Large language models (LLMs) require massive amounts of high-quality text data for training. While PDFs are a common source of such data, extracting text from PDFs while preserving structure and reading order is non-trivial, especially for complex layouts, tables, and scanned documents. olmOCR uses a vision-language model to directly interpret the visual appearance of pages, avoiding the limitations of traditional OCR or PDF parsing approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/allenai/olmocr">GitHub - allenai/olmocr: Toolkit for linearizing PDFs for LLM ...</a></li>
<li><a href="https://olmocr.allenai.org/">olmOCR – Open-Source OCR for Accurate Document Conversion</a></li>

</ul>
</details>

**Tags**: `#PDF`, `#LLM`, `#data preprocessing`, `#toolkit`, `#OCR`

---

<a id="item-10"></a>
## [VulnClaw: AI-Driven CLI Tool Automates Pen Testing via Natural Language](https://github.com/Unclecheng-li/VulnClaw) ⭐️ 8.0/10

VulnClaw v0.3.2 is released, a CLI tool that uses AI Agent, MCP toolchain, and skill orchestration to automate the entire penetration testing pipeline from information gathering to report generation using natural language input. This tool represents a significant advancement in security automation by bridging AI reasoning with practical penetration testing, potentially lowering the barrier for authorized security assessments and red team operations. It supports 13 LLM providers (OpenAI, DeepSeek, etc.), 21 built-in penetration skills, and includes anti-hallucination gates that verify findings against actual tool outputs.

rss · GitHub Trending - Daily · Jul 2, 01:39

**Background**: MCP (Model Context Protocol) is an open standard introduced by Anthropic in November 2024 that standardizes how AI systems connect to external tools and data sources. In penetration testing, AI agents can orchestrate multiple tools and skills to automate complex security assessments. VulnClaw leverages these technologies to provide an end-to-end automated testing experience.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Penetration Testing`, `#MCP`, `#Cybersecurity`, `#Automation`

---

<a id="item-11"></a>
## [Open WebUI: A User-Friendly Interface for Multiple LLM Backends](https://github.com/open-webui/open-webui) ⭐️ 8.0/10

Open WebUI is an open-source, self-hosted AI platform that provides a feature-rich web interface for interacting with large language models from Ollama and any OpenAI-compatible API. This tool simplifies the deployment and use of both local and cloud LLMs, making advanced AI accessible to individuals and organizations without complex setup, and it has gained strong community traction with high GitHub stars. It supports offline operation, includes a built-in inference engine for RAG (Retrieval-Augmented Generation), and can be installed via pip, uv, Docker, or Kubernetes with dedicated :ollama and :cuda container images.

rss · GitHub Trending - Python Daily · Jul 2, 01:46

**Background**: Ollama is an open-source platform that enables users to run large language models locally on their own machines. OpenAI API provides access to models like GPT-4 via cloud services. Open WebUI acts as a unified frontend to connect to both local Ollama models and remote OpenAI-compatible APIs, giving users flexibility and control.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama</a></li>
<li><a href="https://www.ollama.com/">Ollama</a></li>

</ul>
</details>

**Tags**: `#AI`, `#web UI`, `#open-source`, `#LLMs`, `#tools`

---

<a id="item-12"></a>
## [Maigret: OSINT Tool Scans 3000+ Sites for Username Traces](https://github.com/soxoj/maigret) ⭐️ 8.0/10

Maigret is a Python-based open-source intelligence (OSINT) tool that collects a dossier on a person by searching their username across over 3000 websites, requiring no API keys and offering optional AI-powered profiling. This tool significantly simplifies and scales the process of username-based investigations for security researchers, journalists, and law enforcement, making OSINT accessible without deep technical expertise and reducing the time needed for manual checks. Maigret requires Python 3.10 or later, covers more than 3000 sites, and can output results in multiple formats. The tool also includes an AI profiling demo that attempts to build a persona from collected data.

rss · GitHub Trending - Python Daily · Jul 2, 01:46

**Background**: Open-source intelligence (OSINT) refers to the collection and analysis of information from publicly available sources for intelligence purposes. In cybersecurity, OSINT is used to discover potential vulnerabilities or gather threat intelligence. Username search tools like Maigret help automate the discovery of a person's online presence across various platforms, which can be used for investigations, penetration testing, or social engineering assessments.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-source_intelligence">Open - source intelligence - Wikipedia</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/threat-intelligence/open-source-intelligence-osint/">What is OSINT ( Open Source Intelligence )?</a></li>

</ul>
</details>

**Tags**: `#osint`, `#python`, `#username-search`, `#github`

---

<a id="item-13"></a>
## [Chrome DevTools MCP Server Enables AI Agents to Control Chrome](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

The Chrome DevTools team released an official MCP server (chrome-devtools-mcp) that lets AI coding agents like Claude, Cursor, or Copilot inspect, debug, and automate a live Chrome browser via the Model Context Protocol. This bridges a critical gap in AI-driven workflows by providing reliable, fine-grained browser control for automation and debugging, directly from coding agents. The tool uses Puppeteer for automation and Chrome DevTools for performance tracing, and it collects usage statistics by default (opt-out available).

rss · GitHub Trending - TypeScript Daily · Jul 2, 01:48

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 that standardizes how AI systems connect to external tools and data sources. Chrome DevTools is a set of web developer tools built directly into the Chrome browser. This MCP server gives AI coding agents direct access to those tools.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">GitHub - ChromeDevTools/chrome-devtools-mcp: Chrome DevTools for coding agents · GitHub</a></li>
<li><a href="https://developer.chrome.com/blog/chrome-devtools-mcp">Chrome DevTools (MCP) for your AI agent | Blog | Chrome for Developers</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#automation`, `#debugging`

---

<a id="item-14"></a>
## [Polars: Blazingly Fast DataFrame Library in Rust](https://github.com/pola-rs/polars) ⭐️ 8.0/10

Polars is an extremely fast DataFrame query engine written in Rust, now gaining widespread adoption in data engineering and data science communities. It offers lazy and eager execution, streaming for larger-than-RAM datasets, and multi-threaded performance. Polars significantly outperforms traditional DataFrame libraries like pandas in speed and memory efficiency, enabling data practitioners to process large datasets faster and with less resource usage. Its lightweight design and zero required dependencies make it an attractive alternative for modern data workflows. Polars uses Apache Arrow columnar format for efficient data representation and supports SIMD for additional speed. It provides front-end bindings for Python, Rust, Node.js, R, and SQL, and offers a powerful expression API for complex data manipulations.

rss · GitHub Trending - Rust Daily · Jul 2, 01:47

**Background**: DataFrame libraries are essential for data analysis, allowing users to manipulate structured data intuitively. Pandas has been the dominant library in Python, but it struggles with large datasets and performance. Rust is a systems programming language known for its memory safety and performance, making it well-suited for building high-performance data tools.

<details><summary>References</summary>
<ul>
<li><a href="https://pola.rs/">Polars — DataFrames for the new era</a></li>
<li><a href="https://github.com/pola-rs/polars">GitHub - pola-rs/polars: Extremely fast Query Engine for DataFrames, written in Rust · GitHub</a></li>
<li><a href="https://realpython.com/polars-python/">Python Polars: A Lightning-Fast DataFrame Library – Real Python</a></li>

</ul>
</details>

**Tags**: `#rust`, `#dataframe`, `#data-engineering`, `#performance`, `#open-source`

---

<a id="item-15"></a>
## [Awesome Rust: Curated List of Rust Resources](https://github.com/rust-unofficial/awesome-rust) ⭐️ 8.0/10

The awesome-rust repository, hosted under rust-unofficial, maintains a curated list of Rust code and resources, covering applications, libraries, and tools. This resource is essential for Rust developers, providing a well-organized, regularly updated snapshot of the Rust ecosystem, which helps newcomers and experienced developers discover high-quality projects and libraries. The list includes sections for applications (audio, blockchain, databases, etc.), development tools, libraries, and more, with a community-maintained structure and automated CI checks for quality.

rss · GitHub Trending - Rust Daily · Jul 2, 01:47

**Background**: Awesome lists are curated collections of resources on specific topics, commonly hosted on GitHub under the 'awesome' banner. The Rust programming language emphasizes safety and performance, and its ecosystem has grown rapidly. This repository aggregates the best Rust tools and libraries, making it easier for developers to find what they need.

**Tags**: `#Rust`, `#awesome-list`, `#resources`, `#curated`

---

<a id="item-16"></a>
## [Kueue: Kubernetes-native Job Queueing for Batch Workloads](https://github.com/kubernetes-sigs/kueue) ⭐️ 8.0/10

Kueue is a set of APIs and a controller for job queueing in Kubernetes, supporting priority-based scheduling, resource management, and integrations with popular batch job frameworks. It fills a gap in Kubernetes batch processing by providing native job-level queueing, enabling fair sharing and resource efficiency for multi-tenant environments. This is crucial for AI/ML workloads and high-performance computing. Kueue supports strategies like StrictFIFO and BestEffortFIFO, features like preemption, cohorts, and flavor fungibility, and integrates with BatchJob, Kubeflow, RayJob, and JobSet. It also provides Prometheus metrics and AdmissionChecks.

rss · GitHub Trending - Go Daily · Jul 2, 01:42

**Background**: Kubernetes is a container orchestration platform. Batch workloads, like training ML models, often need job queueing to manage resources and priorities. Kueue, from the Kubernetes SIG-s, provides a native solution that works with the Kubernetes scheduler.

<details><summary>References</summary>
<ul>
<li><a href="https://kubernetes.io/blog/2022/10/04/introducing-kueue/">Introducing Kueue | Kubernetes</a></li>
<li><a href="https://github.com/kubernetes-sigs/kueue">GitHub - kubernetes -sigs/kueue: Kubernetes -native Job Queueing</a></li>

</ul>
</details>

**Tags**: `#kubernetes`, `#job-queueing`, `#batch-processing`, `#cloud-native`

---

<a id="item-17"></a>
## [Meta Compute: Everyone Wants To Be A Cloud](https://newsletter.semianalysis.com/p/meta-compute-everyone-wants-to-be) ⭐️ 8.0/10

Meta is building a cloud business, internally called Meta Compute, to sell excess AI computing capacity and host its AI models, competing with AWS, Azure, and neoclouds like CoreWeave. The initiative includes scaling recommendation systems by 10x and will be featured in the upcoming ClusterMAX ranking. This marks a strategic shift for Meta as it monetizes its massive AI infrastructure, intensifying competition in the cloud market and potentially lowering AI compute costs. It reflects a broader trend of large tech companies building cloud-like services to capture more value from AI investments. Meta's cloud will offer two tracks: raw AI compute capacity (similar to neoclouds) and hosted access to its own AI models (similar to AWS Bedrock), led by infrastructure chief Santosh Janardhan. Meta is also scaling its recommendation systems to LLM-scale using new architectures like InterFormer, aiming for a 10x improvement in efficiency.

rss · Semianalysis · Jul 2, 22:18

**Background**: Major tech companies originally built cloud infrastructure for internal use and later sold excess capacity (e.g., AWS, Google Cloud). Meta has invested heavily in AI compute for its social platforms, and now seeks to monetize that capacity externally. ClusterMAX is a rating system by SemiAnalysis that ranks GPU cloud providers across performance, networking, and pricing, and upcoming rankings will include Meta's offerings.

<details><summary>References</summary>
<ul>
<li><a href="https://letsdatascience.com/news/meta-builds-cloud-business-to-sell-ai-compute-bc12117e">Meta Builds Cloud Business to Sell AI Compute | Let's Data ...</a></li>
<li><a href="https://newsletter.semianalysis.com/p/clustermax-20-the-industry-standard">ClusterMAX ™ 2.0: The Industry Standard GPU Cloud Rating System</a></li>
<li><a href="https://engineering.fb.com/2026/03/31/ml-applications/meta-adaptive-ranking-model-bending-the-inference-scaling-curve-to-serve-llm-scale-models-for-ads/">Meta Adaptive Ranking Model: Bending the Inference Scaling Curve to Serve LLM-Scale Models for Ads - Engineering at Meta</a></li>

</ul>
</details>

**Tags**: `#cloud computing`, `#Meta`, `#infrastructure`, `#AI`, `#tech strategy`

---

<a id="item-18"></a>
## [ECTC 2026 Roundup: EMIB-T, HBM4, Cooling, Photonic Interconnects](https://newsletter.semianalysis.com/p/ectc2026) ⭐️ 8.0/10

At ECTC 2026, Intel, TSMC, SK Hynix, Samsung, Micron, Marvell, Lightmatter, and Microsoft presented roadmaps and challenges for advanced packaging, including Intel's EMIB-T technology, custom HBM, HBM4 packaging challenges, microfluidic cooling, and photonic interconnects. These developments are critical for future AI and HPC systems, as advanced packaging enables higher performance, bandwidth, and energy efficiency. The challenges highlighted will shape the direction of the semiconductor industry. EMIB-T combines 2.5D and 3D packaging elements to support HBM4 and UCIe. Microfluidic cooling embeds coolant channels directly into silicon, achieving significant temperature reduction. Photonic interconnects use light for high-bandwidth, low-power chip-to-chip communication.

rss · Semianalysis · Jul 2, 17:25

**Background**: Advanced packaging integrates multiple chips into a single package to overcome semiconductor scaling limits. EMIB (Embedded Multi-die Interconnect Bridge) is Intel's technology for high-density inter-die connections. HBM (High Bandwidth Memory) is a type of memory used in GPUs and accelerators. Microfluidic cooling circulates liquid through microscopic channels to cool hot spots. Photonic interconnects transmit data using light, offering advantages over electrical interconnects in bandwidth and power efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kad8.com/hardware/intel-archieves-breakthroughs-new-packaging-technology/">Intel Archieves Breakthroughs New Packaging Technologies · KAD</a></li>
<li><a href="https://www.datacenterdynamics.com/en/analysis/microfluidics-cooling-inside-the-chip/">Microfluidics: Cooling inside the chip - DCD</a></li>
<li><a href="https://lightmatter.co/knowledge-hub/how-do-photonic-interconnects-work/">How Do Photonic Interconnects Work?</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#advanced packaging`, `#HBM`, `#photonic interconnects`, `#microfluidic cooling`

---

<a id="item-19"></a>
## [Kioxia-SanDisk BiCS10 332-layer NAND enters sampling](https://www.ithome.com/0/971/973.htm) ⭐️ 8.0/10

Kioxia and SanDisk have announced sampling of their 10th-generation BiCS FLASH 3D NAND, featuring 332 layers and a 1Tb TLC product with I/O speeds up to 4800 MT/s. This milestone demonstrates continued advancement in NAND flash density and performance, with a 59% density increase over BiCS8, enabling higher capacity SSDs for data centers and consumer devices. The BiCS10 chip uses a 332-layer cell stacking architecture, CMOS Directly Bonded to Array (CBA) and Offset Pitch Strapping (OPS) technologies, and supports Toggle DDR6.0 interface with 4800 MT/s data rate.

rss · IT之家 · Jul 2, 23:55

**Background**: 3D NAND flash stacks memory cells vertically to increase density without shrinking cell size. CBA technology bonds the CMOS logic and memory array on separate wafers for better performance, while OPS improves signal integrity in high-layer-count designs. BiCS10 is the latest generation from Kioxia and SanDisk, following BiCS8 with 218 layers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/storage/kioxia-and-sandisk-start-shipping-bics9-3d-nand-samples-hybrid-design-combining-112-layer-bics5-with-modern-cba-and-ddr6-0-interface-for-higher-performance-and-cost-efficiency">Kioxia and SanDisk start shipping BiCS9 3D NAND... | Tom's Hardware</a></li>
<li><a href="https://www.techtimes.com/articles/317071/20260524/kioxia-nand-flash-mass-production-accelerates-bics10-target-puts-samsung-sk-hynix-edge.htm">Kioxia NAND Flash Mass Production Accelerates: BiCS10 Target Puts...</a></li>
<li><a href="https://www.icgoodfind.com/cms/Article/get/article_id/18126">Kioxia Delays BiCS10 3D NAND Mass Production to 2027, Boosts...</a></li>

</ul>
</details>

**Tags**: `#NAND Flash`, `#Storage Technology`, `#Semiconductors`, `#3D NAND`, `#Kioxia`

---

<a id="item-20"></a>
## [Tesla driver charged with homicide after fatal FSD crash, data shows override](https://www.ithome.com/0/971/971.htm) ⭐️ 8.0/10

Michael Butler, 44, was arrested and charged with negligent homicide after his Tesla Model 3 crashed into a Texas home while using Full Self-Driving (FSD), killing 76-year-old Martha Avila. Police found that before the crash, Butler searched online for less conservative FSD behavior, and vehicle data showed he manually overrode FSD by fully depressing the accelerator. This case sets a critical legal precedent for driver responsibility when using semi-autonomous systems, especially when drivers actively seek more aggressive driving modes. It highlights the tension between perceived system conservatism and real-world safety risks, potentially influencing future regulations and public perception of Tesla's FSD. Vehicle data showed Butler pressed the accelerator pedal to 100% for about six seconds, accelerating to 117 km/h (over double the residential speed limit) with no brake application. Tesla's AI head confirmed the driver manually overrode FSD, contradicting Butler's claim that he lost consciousness after activating the system.

rss · IT之家 · Jul 2, 23:43

**Background**: Tesla's Full Self-Driving (FSD) is an advanced driver-assistance system that can handle many driving tasks but still requires active driver supervision. Tesla offers multiple driving profiles (e.g., Sloth, Chill, Standard, Hurry, Mad Max) that adjust the system's assertiveness. Drivers can override FSD at any time by applying the accelerator or brake, but doing so transfers control back to the driver. In this incident, the driver's override led to a fatal crash.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/brookecrothers/2026/06/28/tesla-autopilot-vs-fsd-explained--and-what-can-go-wrong/">Tesla FSD Explained – And What Can Go Wrong</a></li>
<li><a href="https://electrek.co/2026/06/23/tesla-fsd-katy-crash-driver-pedal/">Tesla admits FSD was on in fatal Texas crash, blames driver for 'overriding' it | Electrek</a></li>
<li><a href="https://tahaabbasi.com/blog/tesla-fsd-profiles-explained-sloth-chill-standard-hurry-mad-max-which-one-should-you-use-taha-abbasi">Tesla FSD Profiles Explained: Sloth, Chill, Standard, Hurry ...</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#FSD`, `#autonomous driving`, `#safety`, `#legal`

---

<a id="item-21"></a>
## [Kuaishou's AI arm Keling secures up to $3B funding](https://www.ithome.com/0/971/954.htm) ⭐️ 8.0/10

Kuaishou announced that initial investors have agreed to inject 13.824 billion yuan ($2.028 billion) into its AI subsidiary Beijing Keling, with additional investors allowed to bring total funding up to 20.4471 billion yuan ($3 billion), valuing the company at $18 billion post-money. This massive funding round underscores strong market confidence in Kuaishou's AI video generation technology, and positions Keling as one of the most valuable independent AI video startups globally, with plans to list in Hong Kong within 12 months. The initial investment includes 21 independent investors contributing 13.824 billion yuan, and the total funding cap is set at $3 billion for approximately 16.67% of the expanded registered capital. Tencent is reportedly among the investors, and the post-money valuation of $18 billion is down from an earlier target of $20 billion.

rss · IT之家 · Jul 2, 15:36

**Background**: Keling is Kuaishou's AI video generation platform that supports text-to-video, image-to-video, lip-sync, and camera control. It was launched in 2024 and achieved an annualized revenue of over $300 million as of January 2025. Kuaishou announced a potential spin-off and external fundraising plan in May 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://kelingaicn.com/">可灵AI官网</a></li>
<li><a href="https://klingai.com/app">可灵 AI - 新一代 AI 创意生产力平台</a></li>

</ul>
</details>

**Tags**: `#AI`, `#investment`, `#Kuaishou`, `#Keling`, `#funding`

---

<a id="item-22"></a>
## [Enterprise AI costs spiral out of control; Citigroup, Adobe reportedly restrict model access](https://www.ithome.com/0/971/937.htm) ⭐️ 8.0/10

Leaked internal documents reveal that multiple large enterprises, including Citigroup, Adobe, Atlassian, and Amazon, are restricting employee access to advanced AI models due to per-token pricing causing monthly AI costs to triple, with one company spending over $15 million per month. This reveals a hidden consequence of rapid enterprise AI deployment: usage-based pricing leads to runaway costs, forcing companies to implement strict governance. This trend may slow down AI adoption and shift focus to cost-efficient model selection. Citigroup disabled access to Claude Opus 4.6/4.7 and GPT-5.5; Atlassian's AI costs rose from $5M to $15M monthly; GitHub is testing per-user billing; Adobe ended unlimited Claude access. Companies are also monitoring token usage and setting budgets.

rss · IT之家 · Jul 2, 14:22

**Background**: AI models like GPT-5 and Claude Opus charge per token, which is a unit of text processed. Previously, many enterprises had flat-fee agreements, but providers have shifted to pay-per-use pricing. This change has made costs unpredictable, forcing companies to manage token budgets across employees and restrict access to expensive flagship models unless necessary.

<details><summary>References</summary>
<ul>
<li><a href="https://benchlm.ai/llm-pricing">LLM API Pricing Comparison 2026 — Cost Per Token for GPT ...</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence, Performance, and Price</a></li>

</ul>
</details>

**Discussion**: Internal employee comments reflect anxiety about losing AI access and resentment over previous permissive cost policies. Some question the necessity of heavy AI usage, while others see the restrictions as inevitable. There is also irony noted in Accenture, which promoted AI adoption now offering cost management services.

**Tags**: `#AI`, `#cost management`, `#enterprise`, `#large language models`, `#industry trends`

---

<a id="item-23"></a>
## [Password spraying attack targets Microsoft 365 via Azure CLI](https://www.ithome.com/0/971/914.htm) ⭐️ 8.0/10

Security firm Huntress reported a massive password spraying attack against Microsoft 365 accounts, using Azure CLI and the OAuth ROPC flow, generating over 81 million login attempts between June 12-26, 2025, and compromising at least 78 accounts across 64 organizations. This attack demonstrates how adversaries can bypass multi-factor authentication (MFA) and conditional access policies by exploiting legacy OAuth flows like ROPC, posing a significant threat to cloud identity security. Organizations relying solely on MFA may be vulnerable if Azure CLI sign-ins are not explicitly protected. The attackers used previously leaked credentials to perform password spraying via Azure CLI, targeting a small set of common passwords across many accounts to avoid account lockout. The malicious traffic originated from an IPv6 address block belonging to LSHIY LLC.

rss · IT之家 · Jul 2, 13:46

**Background**: Password spraying is a technique where attackers try a few commonly used passwords against many accounts, differing from brute-force attacks that target a single account with many passwords. The OAuth ROPC (Resource Owner Password Credentials) grant type allows an application to exchange a username and password directly for an access token without interactive login, a method considered less secure and often deprecated for modern applications. Azure CLI is a command-line tool for managing Azure resources; attackers exploited it to automate authentication requests that appear as normal API traffic.

<details><summary>References</summary>
<ul>
<li><a href="https://learn.microsoft.com/en-us/entra/identity-platform/v2-oauth-ropc">Microsoft identity platform and OAuth 2.0 Resource... | Microsoft Learn</a></li>
<li><a href="https://www.scottbrady.io/oauth/why-the-resource-owner-password-credentials-grant-type-is-not-authentication-nor-suitable-for-modern-applications">Don't use the OAuth password grant type</a></li>
<li><a href="https://cybersecuritynews.com/microsofts-azure-password-spray-attack/">Massive Password Stealing Attack Targeting Microsoft 365 Users...</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#password spraying`, `#Microsoft 365`, `#Azure CLI`, `#OAuth ROPC`

---

<a id="item-24"></a>
## [Microsoft invests $2.5B in new company for enterprise AI integration](https://www.ithome.com/0/971/911.htm) ⭐️ 8.0/10

Microsoft announced the formation of Microsoft Frontier Company, a new subsidiary with $2.5 billion in initial funding, to help enterprises integrate AI tools from multiple vendors including Anthropic and OpenAI. This signals a major shift in Microsoft's enterprise AI strategy, acknowledging that customers want flexibility to mix and match models rather than being locked into a single provider, which could reshape the enterprise AI market. The new company will work with clients like Unilever and Novo Nordisk to combine Microsoft's own AI tools with third-party models and proprietary data, ensuring that output belongs to the client. Microsoft's commercial business president admitted an earlier mistake in tying Copilot exclusively to OpenAI models.

rss · IT之家 · Jul 2, 13:29

**Background**: Enterprises are increasingly adopting a multi-model approach, combining models like Anthropic's Claude, OpenAI's GPT, and open-source options such as DeepSeek to avoid vendor lock-in and reduce costs. Microsoft, a major investor in OpenAI, has also integrated Anthropic's models into Copilot. This move mirrors similar initiatives by Palantir and Amazon Web Services.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#AI adoption`, `#enterprise AI`, `#investment`

---

<a id="item-25"></a>
## [Meta's cloud move triggers AI infrastructure stock sell-off](https://www.36kr.com/p/3878176206516225) ⭐️ 8.0/10

Meta announced it is building a cloud computing business to sell AI compute power to external customers, causing a sharp drop in AI infrastructure stocks like CoreWeave and Nebius. This marks a major shift for Meta as it seeks to monetize its massive AI capital expenditure, potentially disrupting the cloud AI compute market and affecting competitors like CoreWeave. Meta has signed over $100 billion in AI infrastructure contracts, including a $210 billion deal with CoreWeave and $270 billion with Nebius. Its cloud entry raises concerns about oversupply and contract renewals.

rss · 36氪 - 24小时热榜 · Jul 2, 08:34

**Background**: Major tech companies like Amazon, Microsoft, and Google have profitable cloud businesses that offset their AI infrastructure spending. Meta lacked such a revenue stream, making its large capital expenditures a concern for investors. By entering cloud services, Meta aims to create a safety net for potential overinvestment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/accelerators/instinct.html">AMD Instinct ™ Accelerators</a></li>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group</a></li>

</ul>
</details>

**Tags**: `#Meta`, `#cloud computing`, `#AI infrastructure`, `#stock market`, `#capital expenditure`

---

<a id="item-26"></a>
## [Cloudflare to Block Mixed-Use AI Crawlers, Including Google, from September](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/) ⭐️ 8.0/10

Cloudflare announced that starting September 15, it will by default block 'mixed-use' crawlers that simultaneously scrape for search indexing, AI queries, and training on pages with ads. Google's crawler is explicitly called out as an example of such abuse. This policy pressures AI companies to either separate their bots by function or pay publishers for content, potentially reshaping how AI training data is sourced. Web publishers gain a tool to protect their content from uncompensated scraping. The block applies to 'mixed-use' crawlers that combine search indexing with AI training; publishers can still allow dedicated AI crawlers if they choose. Cloudflare uses its existing Bot Management system to detect and block these crawlers based on behavioral analysis.

telegram · zaihuapd · Jul 2, 05:37

**Background**: Mixed-use crawlers are bots that index websites for search engines while simultaneously scraping data for AI model training. Previously, websites could block AI crawlers but not search crawlers, creating a loophole that allowed companies like Google to use their search crawler for AI training. Cloudflare's new default setting closes this loophole by treating any crawler with dual purposes as a potential threat to publisher monetization.

<details><summary>References</summary>
<ul>
<li><a href="https://bitcoinworld.co.in/cloudflare-blocks-ai-crawlers-publishers-payment/">Cloudflare’s New Default Settings Will Block AI Crawlers From...</a></li>
<li><a href="https://www.engadget.com/2207360/cloudflare-will-filter-out-web-crawlers-that-serve-ai-companies/">Cloudflare Will Filter Out Web Crawlers That Serve AI Companies</a></li>
<li><a href="https://www.cloudflare.com/products/bot-management/">Bot Management - Cloudflare</a></li>

</ul>
</details>

**Discussion**: The Telegram community discussion highlights that many websites block AI crawlers but not Google Search, allowing Google to exploit this loophole to train its AI. Cloudflare's move is seen as a way to force Google to either stop using search crawlers for AI or pay for the content.

**Tags**: `#AI`, `#web scraping`, `#Cloudflare`, `#Google`, `#content policy`

---

<a id="item-27"></a>
## [OpenAI Proposes US Government 5% Stake, May Include Google, Meta](https://www.bloomberg.com/news/articles/2026-07-02/openai-proposes-giving-the-us-government-a-5-stake-ft-says) ⭐️ 8.0/10

OpenAI has proposed that the US government take a 5% stake in the company, and possibly in other major AI firms like Google and Meta, to let the public share in AI profits. This proposal marks a significant shift in AI governance and public policy, potentially reshaping industry regulation and wealth distribution from AI advancements. The plan involves a government vehicle holding 5% stakes in OpenAI, Anthropic, Google, and Meta, but raises concerns about regulatory control, conflicts of interest, and acceptance by other companies.

telegram · zaihuapd · Jul 2, 06:02

**Background**: OpenAI is a leading AI research organization that developed ChatGPT. The proposal to involve government ownership is unprecedented in the tech industry, reflecting debates on how to align AI development with public interest.

**Tags**: `#AI政策`, `#政府持股`, `#OpenAI`, `#科技监管`, `#公共利益`

---

<a id="item-28"></a>
## [PS3 Store Closure 2027 Spurs Emergency Game Archiving](http://no-intro.org/) ⭐️ 8.0/10

Sony announced the permanent closure of the PS3 and PS Vita PlayStation Stores by July 2027, prompting archivists and the RPCS3 emulator team to urgently backup digital game data. This closure threatens the permanent loss of digital-only games that never had physical releases, highlighting the fragility of digital ownership and the urgent need for preservation efforts in the gaming community. The RPCS3 team recommends using the no-intro.org database, which catalogs game metadata like cryptographic hashes and file sizes, to coordinate backup efforts and identify which games are still at risk.

telegram · zaihuapd · Jul 2, 15:04

**Background**: The PS3 and PS Vita stores are digital storefronts where users purchase and download games; after closure, no new purchases or re-downloads will be possible. RPCS3 is a popular open-source PS3 emulator, and no-intro.org is a community-driven database that catalogs ROM metadata to aid preservation.

<details><summary>References</summary>
<ul>
<li><a href="https://rpcs3.net/">RPCS3</a></li>
<li><a href="https://no-intro.org/">No-Intro.org</a></li>

</ul>
</details>

**Tags**: `#digital preservation`, `#gaming`, `#PlayStation`, `#emulation`, `#archiving`

---