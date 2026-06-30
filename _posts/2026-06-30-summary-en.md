---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 331 items, 33 important content pieces were selected

---

1. [Supreme Court: Geofence Warrants Need Constitutional Protections](#item-1) ⭐️ 9.0/10
2. [LocalAI: Open-Source AI Engine Runs Any Model Without GPU](#item-2) ⭐️ 9.0/10
3. [CXMT signs $3B DRAM supply deal with Tencent](#item-3) ⭐️ 9.0/10
4. [vLLM v0.24.0: MiniMax-M3 Support and DeepSeek-V4 Optimizations](#item-4) ⭐️ 8.0/10
5. [Rocket Lab acquires Iridium in historic $8B deal](#item-5) ⭐️ 8.0/10
6. [WATaBoy: JIT-Compiling Game Boy to WebAssembly Beats Native Interpreter](#item-6) ⭐️ 8.0/10
7. [Deep Dive into CUDA Kernel Launch Internals](#item-7) ⭐️ 8.0/10
8. [European ISPs Demand Rightsholders Pay for Overblocking Damage](#item-8) ⭐️ 8.0/10
9. [Samsung, SK Hynix, Micron Sued in US for Memory Price Fixing](#item-9) ⭐️ 8.0/10
10. [Ornith-1.0: Self-Scaffolding LLM Achieves SOTA Coding Performance](#item-10) ⭐️ 8.0/10
11. [SimpleX: First Messaging Network Without User Identifiers](#item-11) ⭐️ 8.0/10
12. [Free-for-Dev: A Curated List of Free Tiers for Developers](#item-12) ⭐️ 8.0/10
13. [openpilot: Open-Source ADAS for 300+ Cars](#item-13) ⭐️ 8.0/10
14. [LingBot-Map: Feed-Forward 3D Foundation Model for Streaming Reconstruction](#item-14) ⭐️ 8.0/10
15. [MinerU: Open-source tool converts PDFs to LLM-ready format](#item-15) ⭐️ 8.0/10
16. [ByteByteGo System Design 101: Visual Learning Hub](#item-16) ⭐️ 8.0/10
17. [12-Factor Agents: Principles for Reliable LLM Apps](#item-17) ⭐️ 8.0/10
18. [SurrealDB: Combines Document, Graph, and Real-time Web](#item-18) ⭐️ 8.0/10
19. [Google's Comprehensive Rust Course Goes Public](#item-19) ⭐️ 8.0/10
20. [GreptimeDB: Unified Database for Metrics, Logs, Traces](#item-20) ⭐️ 8.0/10
21. [Jujutsu (jj): A Powerful Git-Compatible VCS](#item-21) ⭐️ 8.0/10
22. [Study finds half of child safety features on major social platforms ineffective](#item-22) ⭐️ 8.0/10
23. [Apple supplier Tata Electronics hacked, iPhone 18 Pro specs leaked](#item-23) ⭐️ 8.0/10
24. [California partners with Anthropic for half-price Claude](#item-24) ⭐️ 8.0/10
25. [Horizon Robotics Launches HSD V2.0 with World Model and End-to-End RL](#item-25) ⭐️ 8.0/10
26. [Adblock for YouTube Chrome extension has critical RCE vulnerability](#item-26) ⭐️ 8.0/10
27. [SK Hynix announces $750B plan, speeds up chip cluster by 12 years](#item-27) ⭐️ 8.0/10
28. [AI Leaders Declare End of Prompt Engineering, Embrace Loop Engineering](#item-28) ⭐️ 8.0/10
29. [Phishing App 'MobileClaw' Steals AI Access Tokens](#item-29) ⭐️ 8.0/10
30. [Google's AI Peer-Reviewer Handles ~10K Papers at Top Conferences](#item-30) ⭐️ 8.0/10
31. [EML Trees Proven as Universal Approximators](#item-31) ⭐️ 8.0/10
32. [Samsung and SK Hynix Announce Massive AI Investment Plans](#item-32) ⭐️ 8.0/10
33. [Algorithm erroneously retracts Max Planck's 1940s papers](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Supreme Court: Geofence Warrants Need Constitutional Protections](https://www.theguardian.com/us-news/2026/jun/29/supreme-court-geofence-warrants-case-decision) ⭐️ 9.0/10

The US Supreme Court ruled 6-3 that geofence warrants, which compel tech companies to provide location data of devices in a defined area, constitute a Fourth Amendment search and thus require probable cause and a warrant. This landmark decision significantly limits law enforcement's ability to obtain bulk location data without individual suspicion, strengthening digital privacy protections for all smartphone users. The case arose from a bank robbery investigation where Google provided device locations within 150 meters of the bank; the Court held that even short-duration location data is protected under the Fourth Amendment.

hackernews · cdrnsf · Jun 29, 15:54 · [Discussion](https://news.ycombinator.com/item?id=48720924)

**Background**: A geofence warrant, also known as a reverse location warrant, is a court order that compels a company like Google to search its database for all mobile devices that were within a specific geographic area during a specific time. Law enforcement has used these warrants to identify suspects in crimes such as robberies and arsons. The Fourth Amendment protects against unreasonable searches and seizures, and the Court's ruling applies this protection to digital location data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Geofence_warrant">Geofence warrant</a></li>
<li><a href="https://grokipedia.com/page/reverse_search_warrant">Reverse search warrant</a></li>
<li><a href="https://mjlst.lib.umn.edu/2025/01/20/caught-in-the-digital-dragnet-the-controversy-over-geofence-warrants-and-privacy-rights/">Caught in the Digital Dragnet: The Controversy Over Geofence ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted the decision's implications for other surveillance technologies like Flock cameras, with some questioning whether warrantless access to such data would now be unconstitutional. Others pointed to the Paula Broadwell case as an example of identifying suspects without phone data, and linked to the full PDF of the decision. Justices Alito and Thomas dissented, with Barrett also in the minority, surprising some observers.

**Tags**: `#privacy`, `#supreme court`, `#geofence warrants`, `#digital rights`, `#law enforcement`

---

<a id="item-2"></a>
## [LocalAI: Open-Source AI Engine Runs Any Model Without GPU](https://github.com/mudler/LocalAI) ⭐️ 9.0/10

LocalAI, an open-source AI engine, has been released to run large language models, vision, voice, image, and video models on any hardware without requiring a GPU. It features a composable architecture with backends like llama.cpp and vLLM that are pulled on demand. This democratizes AI access by eliminating the GPU barrier, enabling individuals and organizations to run powerful AI models on consumer hardware or CPU-only servers. It also ensures data privacy as models run locally without sending data to external services. LocalAI is designed as a small core without bundled dependencies; backends such as llama.cpp, whisper.cpp, and stable-diffusion are containerized and pulled only when needed. It offers drop-in API compatibility with OpenAI, Anthropic, and ElevenLabs, and supports multi-user features like API key auth and role-based access.

rss · GitHub Trending - Go Daily · Jun 29, 01:45

**Background**: Large language models like GPT-4 typically require powerful GPUs for inference, limiting their deployment. LocalAI addresses this by leveraging CPU-optimized inference engines such as llama.cpp and allowing models to run on various hardware including Apple Silicon and AMD GPUs. The project also supports multiple modalities beyond text, including image generation via stable-diffusion and speech recognition via whisper.cpp.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mudler/localai">GitHub - mudler/LocalAI: LocalAI is the open-source AI engine. Run any model - LLMs, vision, voice, image, video - on any hardware. No GPU required. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#AI`, `#local-ai`, `#machine-learning`, `#LLM`

---

<a id="item-3"></a>
## [CXMT signs $3B DRAM supply deal with Tencent](https://www.reuters.com/world/china/chinas-cxmt-wins-3-billion-memory-supply-deal-with-tencent-sources-say-2026-06-29/) ⭐️ 9.0/10

Changxin Memory Technologies (CXMT) has signed a long-term DRAM supply agreement worth nearly $3 billion with Tencent, covering server memory for several years. This deal marks a major breakthrough for China's DRAM industry, as CXMT secures its first large-scale long-term order from a major internet company, boosting self-sufficiency in semiconductors and AI infrastructure. The agreement is reported to last three to five years, sources said; CXMT is also reportedly in talks with Alibaba Cloud, ByteDance, and Xiaomi for similar deals.

telegram · zaihuapd · Jun 29, 09:31

**Background**: DRAM (Dynamic Random Access Memory) is a key memory chip used in servers, PCs, and consumer electronics. Changxin Memory Technologies (CXMT) is China's leading DRAM manufacturer and is preparing for an IPO. This deal comes amid China's push for semiconductor self-reliance and rising demand for AI computing power.

<details><summary>References</summary>
<ul>
<li><a href="https://www.partgenie.ai/insights/china-s-cxmt-is-set-to-challenge-dram-incumbents-2">China’s CXMT Is Set to Challenge DRAM Incumbents</a></li>
<li><a href="https://www.scmp.com/business/china-business/article/3354223/why-chinese-dram-maker-cxmts-ipo-attracting-so-much-attention">Why is Chinese DRAM maker CXMT ’s IPO attracting so much attention?</a></li>

</ul>
</details>

**Tags**: `#DRAM`, `#半导体`, `#腾讯`, `#长鑫存储`, `#AI基础设施`

---

<a id="item-4"></a>
## [vLLM v0.24.0: MiniMax-M3 Support and DeepSeek-V4 Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.24.0) ⭐️ 8.0/10

vLLM v0.24.0 has been released, adding support for the MiniMax-M3 model and delivering major optimizations for DeepSeek-V4, along with 571 commits from 256 contributors. This release significantly expands vLLM's model ecosystem with cutting-edge models like MiniMax-M3 and DeepSeek-V4, enhancing inference performance and flexibility for the LLM community. The release includes a FlashInfer sparse index cache for DeepSeek-V4 improving TTFT by 2-4%, and enables Model Runner V2 to support quantized models by default. A new streaming parser engine unifies tool-call and reasoning parsing across models.

github · khluu · Jun 29, 19:41

**Background**: vLLM is an open-source high-throughput LLM inference engine. MiniMax-M3 is a large multimodal model with 428B parameters and 1M context window, while DeepSeek-V4 is an MoE model with up to 1.6T parameters. FlashInfer is a kernel library for efficient inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.minimax.io/models/text/m3">MiniMax M3 - Coding & Agentic Frontier, 1M Context ...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://github.com/flashinfer-ai/flashinfer">GitHub - flashinfer-ai/flashinfer: FlashInfer: Kernel Library ...</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#release`, `#optimization`, `#model support`

---

<a id="item-5"></a>
## [Rocket Lab acquires Iridium in historic $8B deal](https://investors.rocketlabcorp.com/news-releases/news-release-details/rocket-lab-acquire-iridium-historic-deal-creating-fully) ⭐️ 8.0/10

Rocket Lab announced it will acquire satellite communications company Iridium in a cash-and-stock deal valued at approximately $80 billion, expected to close by mid-2027. This acquisition creates a fully integrated space company, combining Rocket Lab's launch and satellite manufacturing capabilities with Iridium's established satellite network and user base, potentially reshaping the competitive landscape in the space industry. The deal is valued at $80 billion and will be paid in a combination of cash and stock; Iridium operates a constellation in low Earth orbit (LEO), which aligns with Rocket Lab's existing capabilities.

hackernews · everfrustrated · Jun 29, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48719485)

**Background**: Rocket Lab is a commercial space company that provides launch services with its Electron rocket and builds satellites. Iridium is a satellite communications company known for its global satellite phone and data network. This move follows a trend of vertical integration in the space sector, similar to SpaceX's model of controlling both launch and satellite operations.

**Discussion**: Community comments highlight concerns about space debris and commercialization of space, with one user questioning the long-term environmental impact. Others see the acquisition as a strategic move to guarantee launch demand, similar to SpaceX's Starlink model. Some commenters are confused about orbital compatibility, noting that Iridium satellites are not in low Earth orbit (they are actually in LEO, but at a higher altitude than typical).

**Tags**: `#space`, `#acquisition`, `#satellite`, `#rocket-lab`, `#iridium`

---

<a id="item-6"></a>
## [WATaBoy: JIT-Compiling Game Boy to WebAssembly Beats Native Interpreter](https://humphri.es/blog/WATaBoy/) ⭐️ 8.0/10

A project called WATaBoy demonstrates a just-in-time (JIT) compiler that translates Game Boy instructions into WebAssembly, achieving faster performance than a native interpreter. This approach shows that leveraging WebAssembly's JIT capabilities in browsers can outperform traditional native interpreters for emulation, opening new possibilities for high-performance emulation on constrained platforms like iOS where JIT is restricted except in browsers. The project demonstrates that despite WebAssembly's ~20% overhead over native code, the JIT approach outperforms a native interpreter because interpreter overhead can be as high as 1000%. Performance varies across browsers, with Firefox being about 25% slower than Chrome/Safari.

hackernews · energeticbark · Jun 29, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48720190)

**Background**: Game Boy emulation typically runs by interpreting each instruction in software, which is slow. Just-in-time (JIT) compilation translates frequently executed code into native machine code at runtime to speed things up. WebAssembly is a low-level binary format that runs in modern browsers at near-native speed, and it supports JIT compilation in browsers. By targeting WebAssembly, this project can run on any platform with a WebAssembly runtime, including iOS where traditional JIT is not allowed except in web browsers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly_text_format">WebAssembly text format</a></li>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters praised the project as impressive for an undergraduate and noted that the performance result is not surprising because interpreter overhead far exceeds WASM overhead. Comparisons were drawn to similar work like Dolphin+LLVM and NES static recompilation, and one commenter highlighted that Firefox is 25% slower than Chrome/Safari while another explained the motivation to bypass iOS JIT restrictions.

**Tags**: `#JIT Compilation`, `#WebAssembly`, `#Game Boy Emulation`, `#Performance`

---

<a id="item-7"></a>
## [Deep Dive into CUDA Kernel Launch Internals](https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/) ⭐️ 8.0/10

The blog post by Fergus Finn provides a detailed walkthrough of the exact CPU-to-GPU path when launching a CUDA kernel, covering doorbell registers, QMD (Queue Management Descriptor), and stream synchronization. It reveals that the process involves tens of millions of CPU instructions, multiple device files, and hundreds of ioctls. This article fills a critical gap in understanding CUDA kernel launch internals, which is valuable for GPU programmers seeking performance optimization. It demystifies the often opaque driver and hardware hand-off, enabling developers to write more efficient code. The launch process uses a memory-mapped doorbell register to signal the GPU, and the QMD is handed to the compute work distributor. The default stream implicitly handles synchronization, while explicit streams allow parallel command execution.

hackernews · mezark · Jun 29, 13:11 · [Discussion](https://news.ycombinator.com/item?id=48718863)

**Background**: CUDA is NVIDIA's parallel computing platform and programming model that enables GPU acceleration. When a CUDA kernel is launched, the CPU prepares a command descriptor (QMD) and writes it to GPU memory, then rings a doorbell register to notify the GPU. The GPU's hardware command queue picks up the descriptor and schedules execution across streaming multiprocessors. Streams in CUDA allow multiple operations to execute concurrently and require explicit synchronization for correctness.

<details><summary>References</summary>
<ul>
<li><a href="https://fergusfinn.com/blog/what-happens-when-you-run-a-gpu-kernel/">What happens when you run a CUDA kernel</a></li>

</ul>
</details>

**Discussion**: Commenters found the post highly useful, praising the explanation of doorbell registers and QMD for connecting CUDA syntax to actual GPU submission. One commenter noted that control codes are more complex (table lookup), while another speculated about the future of kernel optimization companies versus open-source libraries.

**Tags**: `#CUDA`, `#GPU programming`, `#CUDA internals`, `#performance`, `#hardware`

---

<a id="item-8"></a>
## [European ISPs Demand Rightsholders Pay for Overblocking Damage](https://torrentfreak.com/european-isps-want-rightsholders-held-accountable-for-overblocking-damage/) ⭐️ 8.0/10

European ISPs are demanding that rightsholders be held legally accountable for damages caused by overblocking legitimate content, citing a recent CEPS report that recommends such liability. This push could shift the balance of power in copyright enforcement, forcing rightsholders to be more cautious before blocking content and reducing collateral censorship of lawful material. The ISP organization cites the April CEPS report, which warns against IP-address blocking and recommends that rightsholders be held liable for overblocking. Overblocking occurs when filters or blocks mistakenly prevent access to legitimate content.

hackernews · Brajeshwar · Jun 29, 16:07 · [Discussion](https://news.ycombinator.com/item?id=48721072)

**Background**: Overblocking refers to the unintended blocking of legitimate content due to overly broad filters or court orders. In Europe, site-blocking is often used to combat piracy, but it frequently catches innocent sites. The CEPS report highlighted that rightsholders currently face no consequences for overblocking, while ISPs bear the operational burden.

<details><summary>References</summary>
<ul>
<li><a href="https://torrentfreak.com/european-isps-want-rightsholders-held-accountable-for-overblocking-damage/">European ISPs Want Rightsholders Held Accountable ... * TorrentFreak</a></li>
<li><a href="https://de.wikipedia.org/wiki/Overblocking">Overblocking – Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_filter">Internet filter - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters broadly support ISPs, with many noting that overblocking is a systemic abuse by rightsholders. Some express skepticism that accountability will actually be enforced, while others highlight broader censorship concerns and parallels with US DMCA takedowns.

**Tags**: `#internet governance`, `#copyright`, `#overblocking`, `#ISP liability`, `#censorship`

---

<a id="item-9"></a>
## [Samsung, SK Hynix, Micron Sued in US for Memory Price Fixing](https://en.sedaily.com/international/2026/06/29/samsung-sk-hynix-micron-sued-in-us-over-memory-price-fixing) ⭐️ 8.0/10

A lawsuit has been filed in the United States against Samsung, SK Hynix, and Micron, accusing them of conspiring to fix prices for memory chips including DRAM and NAND flash. If proven, this price fixing could have artificially inflated costs for consumers and businesses, affecting everything from smartphones to data centers. The lawsuit may reshape competition in the memory market and lead to significant penalties. The lawsuit follows past allegations of DRAM price fixing that resulted in fines in the 2000s. This case may focus on recent supply constraints and pricing trends during the pandemic and AI boom.

hackernews · donohoe · Jun 29, 11:58 · [Discussion](https://news.ycombinator.com/item?id=48718102)

**Background**: Memory chips, especially DRAM and NAND flash, are essential components in nearly all electronic devices. The market is dominated by a few major players, making it susceptible to coordinated pricing behavior. Price fixing is illegal under antitrust laws as it harms competition and consumers.

**Discussion**: Commenters noted that a similar lawsuit in 2022 failed due to lack of evidence of an agreement. Some argued that discontinuing older memory products like DDR3 and DDR4 is a normal market shift, not necessarily price fixing, while others pointed to the industry's history of collusion, referencing the DRAM price fixing scandal.

**Tags**: `#memory`, `#price fixing`, `#antitrust`, `#lawsuit`, `#semiconductors`

---

<a id="item-10"></a>
## [Ornith-1.0: Self-Scaffolding LLM Achieves SOTA Coding Performance](https://simonwillison.net/2026/Jun/29/ornith/#atom-everything) ⭐️ 8.0/10

DeepReinforce released Ornith-1.0, a family of self-scaffolding large language models under the MIT license, achieving state-of-the-art performance on coding benchmarks among open-source models of comparable size. This is significant for agentic coding as it introduces a self-improving training framework where the model learns to generate its own harnesses, reducing reliance on human-designed scaffolds and potentially accelerating autonomous software development. Ornith-1.0 is built on the permissively licensed Gemma 4 and Qwen 3.5 base models, with variants including 9B, 31B, 35B MoE, and 397B MoE; initial tests show it can proficiently execute multi-step tool calls in an agent harness.

rss · Simon Willison · Jun 29, 16:17

**Background**: Self-scaffolding refers to a training method where the model jointly learns to produce solution rollouts and task-specific harnesses, optimizing both through reinforcement learning. Agentic coding uses AI agents that autonomously perform multi-step software development tasks, such as code generation, debugging, and testing. Ornith-1.0's approach treats the scaffold as a learnable object, enabling the model to discover better search trajectories.

<details><summary>References</summary>
<ul>
<li><a href="https://deep-reinforce.com/ornith_1_0.html">Ornith-1.0: Self-Scaffolding LLMs for Agentic Coding | DeepReinforce Blog | Jun. 2026</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/ornith-1-0-self-learning-llm-for-coding-318c9a830bfc">Ornith 1.0 : Self Learning LLM for Coding | by Mehul Gupta | Data Science in Your Pocket | Jun, 2026 | Medium</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#agentic coding`, `#open-source`, `#coding benchmark`, `#MIT license`

---

<a id="item-11"></a>
## [SimpleX: First Messaging Network Without User Identifiers](https://github.com/simplex-chat/simplex-chat) ⭐️ 8.0/10

SimpleX Chat, the first messaging platform that operates without any user identifiers, is now available on iOS, Android, and desktop, as announced on its GitHub repository. This approach eliminates the need for phone numbers, usernames, or email addresses, setting a new standard for privacy in messaging and potentially influencing the future of secure communications. SimpleX uses multiple identifiers per messaging queue, rotated regularly, to prevent correlation across contacts. The project has undergone a security audit by Trail of Bits.

rss · GitHub Trending - Daily · Jun 29, 01:41

**Background**: Traditional messaging apps like Signal require phone numbers or usernames as identifiers. SimpleX replaces this with temporary identifiers assigned to each message queue, ensuring no persistent user identity exists.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simplex-chat/simplex-chat">GitHub - simplex-chat/simplex-chat: SimpleX - the first messaging ...</a></li>
<li><a href="https://simplex.chat/docs/protocol/simplex-chat.html">SimpleX Chat Protocol</a></li>
<li><a href="https://www.blog.brightcoding.dev/2025/09/18/simplex-chat-the-first-messaging-app-with-no-user-identifiers-privacy-by-design">SimpleX Chat: The First Messaging App with No User ... - BrightCoding</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#messaging`, `#decentralized`, `#security`, `#open-source`

---

<a id="item-12"></a>
## [Free-for-Dev: A Curated List of Free Tiers for Developers](https://github.com/ripienaar/free-for-dev) ⭐️ 8.0/10

The ripienaar/free-for-dev GitHub repository provides a community-maintained, categorized list of SaaS, PaaS, and IaaS services that offer free tiers, targeting developers and DevOps practitioners. New services are added and outdated ones are removed through pull requests from over 1,600 contributors. This resource saves developers significant time by consolidating free tier offerings from many cloud services, enabling rapid prototyping and cost-effective development. It also encourages community collaboration to keep the list accurate and up-to-date. The list only includes as-a-Service offerings, not self-hosted software, and requires free tiers to last at least a year if time-limited. It also insists on TLS being available in the free tier and does not accept services that restrict TLS to paid tiers.

rss · GitHub Trending - Daily · Jun 29, 01:41

**Background**: Many cloud services offer free tiers to attract developers, but finding and comparing them is often time-consuming. This curated list organizes such offerings into categories like analytics, CI/CD, and data services, making it easier for developers to discover useful tools. The project started on GitHub and has grown through community contributions.

**Tags**: `#DevOps`, `#free-tier`, `#SaaS`, `#PaaS`, `#IaaS`

---

<a id="item-13"></a>
## [openpilot: Open-Source ADAS for 300+ Cars](https://github.com/commaai/openpilot) ⭐️ 8.0/10

openpilot is an open-source operating system for robotics that enhances the driver assistance system on over 300 supported vehicles, offering features like Adaptive Cruise Control and Automated Lane Centering. This project democratizes advanced driver assistance by making high-end ADAS features available to a wide range of vehicles, fostering innovation through an open-source community and reducing dependency on proprietary solutions. openpilot uses machine learning trained on real-world driving data to determine safe paths, and it includes a driver monitoring system for safety. It requires a compatible device (comma four) and a car harness for installation.

rss · GitHub Trending - Daily · Jun 29, 01:41

**Background**: openpilot is developed by comma.ai and is released under the MIT license. It performs functions such as Adaptive Cruise Control (ACC), Automated Lane Centering (ALC), Forward Collision Warning (FCW), and Lane Departure Warning (LDW). The system observes ISO26262 safety guidelines and logs driving data to improve models, with user opt-in options.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Openpilot">openpilot - Wikipedia</a></li>
<li><a href="https://github.com/commaai/openpilot">GitHub - commaai/openpilot: openpilot is an operating system ... comma.ai — make driving chill comma.ai openpilot - Software Guide | CommaGuide openpilot - Wikipedia Releases · commaai/openpilot - GitHub commaai/openpilot | DeepWiki</a></li>
<li><a href="https://comma.ai/openpilot">comma.ai — make driving chill</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#open-source`, `#robotics`, `#ADAS`

---

<a id="item-14"></a>
## [LingBot-Map: Feed-Forward 3D Foundation Model for Streaming Reconstruction](https://github.com/Robbyant/lingbot-map) ⭐️ 8.0/10

The Robbyant team released LingBot-Map, an open-source feed-forward 3D foundation model for streaming 3D reconstruction that processes video frames at ~20 FPS and can handle sequences over 10,000 frames. It is accompanied by a paper, pretrained models on Hugging Face and ModelScope, and an interactive demo. LingBot-Map enables real-time 3D mapping using only a single RGB camera without LiDAR, making high-quality 3D reconstruction accessible for robotics, AR/VR, and autonomous systems. Its fully open-source release with pretrained models lowers the barrier for research and commercial applications. The model uses a Geometric Context Transformer with three context types—anchor context, pose-reference window, and trajectory memory—to handle long-range drift and ensure consistency. It employs paged KV cache attention for efficient streaming inference and builds upon the VGGT architecture, replacing bidirectional attention with causal attention.

rss · GitHub Trending - Daily · Jun 29, 01:41

**Background**: Streaming 3D reconstruction aims to recover camera poses and 3D point clouds from a video stream in real-time, requiring geometric accuracy, temporal consistency, and computational efficiency. Traditional methods often rely on iterative optimization (like SLAM) or offline batch processing. Feed-forward foundation models like LingBot-Map directly predict 3D geometry from input frames without per-scene optimization, enabling faster inference.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.14141">[2604.14141] Geometric Context Transformer for Streaming 3D ... Images LingBot-Map Builds a Full 3D Map with Just One Cheap Camera ... Geometric Context Transformer for Streaming 3D Reconstruction Robbyant LingBot-Map: Streaming 3D Reconstruction with the Geometric ...</a></li>
<li><a href="https://huggingface.co/robbyant/lingbot-map">robbyant/lingbot-map · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#3D reconstruction`, `#foundation model`, `#streaming data`, `#computer vision`

---

<a id="item-15"></a>
## [MinerU: Open-source tool converts PDFs to LLM-ready format](https://github.com/opendatalab/MinerU) ⭐️ 8.0/10

MinerU is an open-source tool that transforms PDFs and Office documents into markdown or JSON format optimized for large language model (LLM) workflows. It addresses a major bottleneck in preparing complex documents for AI agents, making it easier to integrate diverse data into agentic workflows. The tool handles complex layouts and tables via auto-detected OCR, and can be installed via pip. It is available on GitHub under opendatalab/MinerU.

rss · GitHub Trending - Daily · Jun 29, 01:41

**Background**: MinerU is a document parsing tool designed to transform unstructured documents like PDFs and Office files into structured markdown or JSON that LLMs can easily consume. This is crucial for 'agentic workflows' where AI agents autonomously process and act on information from various sources.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/opendatalab/mineru">GitHub - opendatalab/MinerU: Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows. · GitHub</a></li>
<li><a href="https://grokipedia.com/page/MinerU">MinerU</a></li>

</ul>
</details>

**Tags**: `#document parsing`, `#LLM`, `#data preprocessing`, `#open source`, `#AI tooling`

---

<a id="item-16"></a>
## [ByteByteGo System Design 101: Visual Learning Hub](https://github.com/ByteByteGoHq/system-design-101) ⭐️ 8.0/10

ByteByteGo has published a GitHub repository called system-design-101 that explains complex system design concepts using visuals and simple terms, targeting interview preparation. This repository consolidates essential system design knowledge from a reputable source, making it a valuable free resource for engineers preparing for technical interviews or seeking to understand system architecture. The repository covers topics like API design, load balancing, WebSocket, gRPC, and HTTP/2, with links to detailed ByteByteGo guides and a table of contents for easy navigation.

rss · GitHub Trending - Daily · Jun 29, 01:41

**Background**: System design interviews assess a candidate's ability to architect large-scale distributed systems. Visual explanations help simplify abstract concepts, making them easier to grasp and remember. ByteByteGo is known for its educational content on system design through blog posts and YouTube videos.

**Tags**: `#system-design`, `#interview-prep`, `#visual-learning`, `#architecture`

---

<a id="item-17"></a>
## [12-Factor Agents: Principles for Reliable LLM Apps](https://github.com/humanlayer/12-factor-agents) ⭐️ 8.0/10

The 12-Factor Agents repository, inspired by the 12-Factor App methodology, outlines twelve principles for building reliable and production-ready LLM-powered software. It provides a structured framework to address common challenges in deploying LLM agents to real users. This framework offers a practical guide for engineers to move beyond experimental prototypes and build LLM applications that are robust enough for production customers. It fills a critical gap in the AI/ML ecosystem where many agent frameworks lack proven production patterns. The 12 factors cover areas such as owning the context window, logging, and observability, emphasizing that a reliable agent is well-engineered software with LLMs used only where probabilistic reasoning adds value. The project is open-source under Apache 2.0 (code) and CC BY-SA 4.0 (content).

rss · GitHub Trending - TypeScript Daily · Jun 29, 01:51

**Background**: The original 12-Factor App is a widely adopted methodology for building software-as-a-service applications that are deployable, scalable, and maintainable. LLM agents are AI systems that use large language models to reason and take actions autonomously. Despite their promise, many agents fail in production due to unpredictable behavior and lack of structured engineering practices.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/humanlayer/12-factor-agents">GitHub - humanlayer/ 12 - factor - agents : What are the principles we can...</a></li>
<li><a href="https://www.humanlayer.dev/12-factor-agents">12 Factor Agents - Build Reliable LLM Applications</a></li>
<li><a href="https://medium.com/@adnanmasood/12-factor-agents-framework-for-reliable-llm-agents-empirical-guidelines-for-scalable-auditable-4b758e0e7979">12 Factor Agents : Framework for Reliable LLM Agents ... | Medium</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#software engineering`, `#best practices`, `#agents`, `#TypeScript`

---

<a id="item-18"></a>
## [SurrealDB: Combines Document, Graph, and Real-time Web](https://github.com/surrealdb/surrealdb) ⭐️ 8.0/10

SurrealDB is a new open-source database that combines document-oriented and graph database models with real-time web capabilities, built entirely in Rust. This multi-model approach simplifies application development by replacing separate databases for documents, graphs, and real-time updates, potentially reducing architectural complexity for modern web applications. SurrealDB supports SQL-like queries, real-time subscriptions, and runs on various platforms including Docker, with client libraries for JavaScript, Python, .NET, and PHP. It is licensed under BSL 1.1, which is not fully open source.

rss · GitHub Trending - Rust Daily · Jun 29, 01:49

**Background**: Traditional document databases store semi-structured data as documents, while graph databases excel at managing relationships between data points. SurrealDB aims to combine the flexibility of document stores with the relationship capabilities of graph databases, adding real-time synchronization for collaborative applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Document-oriented_database">Document-oriented database - Wikipedia</a></li>
<li><a href="https://www.dataversity.net/articles/graph-database-vs-document-database-different-levels-of-abstraction/">Graph Database vs. Document Database: Different Levels of ...</a></li>

</ul>
</details>

**Tags**: `#database`, `#distributed-systems`, `#realtime`, `#graph-db`, `#rust`

---

<a id="item-19"></a>
## [Google's Comprehensive Rust Course Goes Public](https://github.com/google/comprehensive-rust) ⭐️ 8.0/10

Google has open-sourced Comprehensive Rust, a multi-day Rust course developed by its Android team, now available on GitHub and as a hosted website. This course provides a high-quality, structured pathway for experienced engineers to learn Rust, reflecting Google's internal investment in Rust adoption and addressing the industry's need for Rust training. The course covers Rust from basics to advanced topics including Android, Chromium, bare-metal, and concurrency modules, and is built with mdBook, supporting multiple languages via i18n.

rss · GitHub Trending - Rust Daily · Jun 29, 01:49

**Background**: Rust is a systems programming language focused on safety and performance, widely adopted by companies like Google for systems software. Google's Android team created this course to internally train engineers with C++ or Java backgrounds, and it has been refined over two years.

**Tags**: `#Rust`, `#education`, `#Google`, `#course`, `#programming`

---

<a id="item-20"></a>
## [GreptimeDB: Unified Database for Metrics, Logs, Traces](https://github.com/GreptimeTeam/greptimedb) ⭐️ 8.0/10

GreptimeDB is an open-source unified database designed to handle metrics, logs, and traces in a single engine, aiming to replace Prometheus, Loki, and Elasticsearch for observability. This project simplifies the observability stack by consolidating three specialized tools into one, reducing operational complexity and storage costs while enabling cross-signal correlation queries using SQL and PromQL. GreptimeDB is built with Rust, stores data on object storage, and supports both SQL and PromQL for querying. It is self-described as a unified OpenTelemetry backend and is under active development with a 2026 roadmap.

rss · GitHub Trending - Rust Daily · Jun 29, 01:49

**Background**: Observability traditionally requires separate tools for metrics (Prometheus), logs (Loki), and traces (Jaeger or similar). Managing multiple systems increases complexity and cost. GreptimeDB aims to unify these signals into a single database, leveraging object storage for scalability and using Rust for performance.

**Tags**: `#observability`, `#database`, `#open-source`, `#Prometheus-replacement`, `#Rust`

---

<a id="item-21"></a>
## [Jujutsu (jj): A Powerful Git-Compatible VCS](https://github.com/jj-vcs/jj) ⭐️ 8.0/10

Jujutsu (jj) is a new version control system that is fully compatible with Git repositories and aims to provide a simpler and more powerful user experience. Jujutsu matters because it addresses common pain points in Git, such as complex commands and confusing data model, while maintaining seamless interoperability with existing Git repositories, which could significantly impact developer productivity. Jujutsu is written in Rust, uses Git repositories as its default storage backend, and stores bookmarks and other metadata separately. It introduces a revset language for selecting commits and eliminates the traditional staging area (index).

rss · GitHub Trending - Rust Daily · Jun 29, 01:49

**Background**: Version control systems (VCS) track changes to source code. Git is the most popular but has a steep learning curve due to its complex data model and command set. Jujutsu (jj), developed at Google, aims to simplify this by combining ideas from Git, Mercurial, and Sapling into a single tool, while offering full Git interoperability.

<details><summary>References</summary>
<ul>
<li><a href="https://jj-for-everyone.github.io/">Introduction - Jujutsu for everyone</a></li>
<li><a href="https://mskadu.medium.com/introducing-jujutsu-a-modern-alternative-to-git-32bb8b7fadd9">Introducing Jujutsu : A Modern Alternative to Git | Medium</a></li>
<li><a href="https://zenn.dev/kosk_t/articles/jj-introduction-guide?locale=en">Benefits and Basic Usage of Jujutsu (jj), a Git-Compatible Version ...</a></li>

</ul>
</details>

**Tags**: `#version-control`, `#git-compatible`, `#rust`, `#jujutsu`, `#development-tools`

---

<a id="item-22"></a>
## [Study finds half of child safety features on major social platforms ineffective](https://www.ithome.com/0/970/253.htm) ⭐️ 8.0/10

Researchers from New York University and Northeastern University tested 86 child safety features on Instagram, Snapchat, TikTok, and YouTube, finding that at least 50% of them failed to work as advertised. This research reveals systemic failures in social media platforms' child protection measures, which could influence public policy and increase pressure on companies to improve safety. The study simulated various scenarios including normal use, teens attempting to bypass safety features, and malicious adults targeting minors. Snapchat allowed unrestricted adult contact with children, and TikTok recommended anorexia-related content to teen accounts.

rss · IT之家 · Jun 29, 23:46

**Background**: Child safety features on social media are designed to protect minors from inappropriate contact and harmful content. However, this study indicates that many of these features are either hard to find, ineffective, or not actually implemented.

**Tags**: `#child safety`, `#social media`, `#research`, `#online privacy`, `#platform accountability`

---

<a id="item-23"></a>
## [Apple supplier Tata Electronics hacked, iPhone 18 Pro specs leaked](https://www.ithome.com/0/970/245.htm) ⭐️ 8.0/10

Ransomware group World Leaks hacked Apple's Indian supplier Tata Electronics and leaked over 200,000 files on the dark web, including component lists and supplier details for the unreleased iPhone 18 Pro series. This breach exposes Apple's highly confidential supply chain information, potentially revealing its negotiation leverage and single-source dependencies, which could impact future product secrecy and supplier relationships. The leaked files include test photos of the iPhone 18 Pro taken in early 2026 at a Tata Electronics factory, and documents marked with Apple's 'confidential' watermark. The data also covers Tesla components and references to TSMC and Qualcomm.

rss · IT之家 · Jun 29, 22:56

**Background**: Apple maintains strict secrecy over its supply chain, but suppliers like Tata Electronics have access to sensitive plans. Ransomware groups like World Leaks, which emerged in January 2025 as a rebrand of Hunters International, focus on data theft and extortion rather than encryption. India is expected to produce 26% of iPhones globally by 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ransomware.live/group/worldleaks">Group: worldleaks - ransomware.live</a></li>
<li><a href="https://blackpointcyber.com/wp-content/uploads/2025/12/World-Leaks.pdf">World Leaks Ransomware - blackpointcyber.com</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#supply chain`, `#Apple`, `#data breach`, `#ransomware`

---

<a id="item-24"></a>
## [California partners with Anthropic for half-price Claude](https://www.ithome.com/0/970/222.htm) ⭐️ 8.0/10

California Governor Gavin Newsom announced a partnership with AI company Anthropic, offering state and local government agencies a 50% discount on Claude AI tools, along with free training and expert support. This marks a major adoption of AI in the public sector at scale, potentially improving government efficiency and setting a precedent for other states. It also signals growing trust in AI despite earlier security concerns. The discount applies to all state administrative departments and city/county governments. Claude will assist with tasks like drafting documents, summarizing files, analyzing information, and daily office work.

rss · IT之家 · Jun 29, 14:23

**Background**: Claude is an AI chatbot developed by Anthropic, an AI safety company. It is trained using constitutional AI to be safe and ethical. Earlier this year, the US Department of Defense designated Anthropic as a supply chain risk, and the Department of Commerce imposed export controls on some Anthropic models over national security concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>
<li><a href="https://claude.com/">Claude</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Government`, `#Anthropic`, `#Claude`, `#Partnership`

---

<a id="item-25"></a>
## [Horizon Robotics Launches HSD V2.0 with World Model and End-to-End RL](https://www.ithome.com/0/970/186.htm) ⭐️ 8.0/10

Horizon Robotics released HSD V2.0, an assisted driving system integrating a world model with end-to-end reinforcement learning, and will start OTA updates for the iCAR V27 on June 30. This update significantly improves autonomous driving performance, with a 56% increase in zero-intervention mileage and a 167% improvement in negotiation capability, setting a new benchmark for assisted driving systems. HSD V2.0 extends the Occupancy Network (OCC) from NOA to active safety scenarios like AEB and AES, enabling the system to handle irregular obstacles without relying on traditional 'white list' recognition.

rss · IT之家 · Jun 29, 12:44

**Background**: World models in autonomous driving are AI systems that learn internal representations of the environment to predict future states and simulate scenarios, enhancing decision-making. End-to-end reinforcement learning allows agents to learn actions directly from raw sensor data through trial and error, without manual feature engineering.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2501.11260">[2501.11260] A Survey of World Models for Autonomous Driving</a></li>
<li><a href="https://en.wikipedia.org/wiki/End-to-end_reinforcement_learning">End-to-end reinforcement learning</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#world model`, `#reinforcement learning`, `#OTA update`, `#assisted driving`

---

<a id="item-26"></a>
## [Adblock for YouTube Chrome extension has critical RCE vulnerability](https://www.ithome.com/0/970/179.htm) ⭐️ 8.0/10

Security researchers discovered that the Adblock for YouTube Chrome extension, with over 11 million users, has a critical vulnerability allowing remote code execution via server-side configuration and flawed domain validation. This vulnerability can allow attackers to execute arbitrary JavaScript in users' browsers, steal sensitive data, and perform account impersonation, affecting millions of YouTube users who rely on ad blocking. The extension does not strictly validate whether the current domain is actually youtube.com; it can be tricked by URLs containing the string 'youtube.com'. Additionally, it includes a server-side configurable JavaScript library that could be abused if the server is compromised.

rss · IT之家 · Jun 29, 12:10

**Background**: Chrome extensions can have elevated permissions, allowing them to access browser data and modify web pages. Server-side configuration injection is a known attack vector where an extension fetches code from a remote server, and if that server is compromised, attackers can inject malicious code. Domain validation bypass is another common vulnerability where an extension incorrectly trusts a domain based on a substring match.

<details><summary>References</summary>
<ul>
<li><a href="https://thehackernews.com/2026/03/chrome-extension-turns-malicious-after.html?m=1">Chrome Extension Turns Malicious After Ownership Transfer, Enabling Code Injection and Data Theft</a></li>
<li><a href="https://cheatsheetseries.owasp.org/cheatsheets/Browser_Extension_Vulnerabilities_Cheat_Sheet.html">Browser Extension Vulnerabilities - OWASP Cheat Sheet Series</a></li>

</ul>
</details>

**Tags**: `#安全漏洞`, `#Chrome扩展`, `#远程代码执行`, `#广告拦截`

---

<a id="item-27"></a>
## [SK Hynix announces $750B plan, speeds up chip cluster by 12 years](https://www.ithome.com/0/970/175.htm) ⭐️ 8.0/10

SK Hynix announced a 1,100 trillion won (about $750 billion) long-term investment strategy, accelerating the completion of its Yongin semiconductor cluster from 2045 to 2033, a 12-year speedup. This massive investment signals SK Hynix's aggressive expansion to meet surging demand for DRAM and HBM memory critical for AI hardware, potentially reshaping the global memory supply chain. The plan allocates 600 trillion won for four fabs in Yongin, 100 trillion won for a NAND fab and HBM packaging in Cheongju, and 400 trillion won for front-end process facilities in southwestern Korea; overseas fabs may be considered later.

rss · IT之家 · Jun 29, 11:40

**Background**: SK Hynix is a leading semiconductor manufacturer specializing in DRAM, NAND flash, and HBM (High Bandwidth Memory). HBM uses 3D-stacked SDRAM to provide high bandwidth critical for AI accelerators. Advanced packaging techniques like CoWoS combine multiple chips into one package to improve performance and reduce power consumption. A clean room is a controlled environment essential for semiconductor fabrication to avoid particle contamination.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advanced_packaging_(semiconductors)">Advanced packaging (semiconductors) - Wikipedia</a></li>
<li><a href="https://www.abilityengineering.com/inside-semiconductor-fabrication-cleanroom/">Semiconductor Fabrication Cleanroom Essentials</a></li>

</ul>
</details>

**Tags**: `#semiconductor`, `#investment`, `#SK Hynix`, `#DRAM`, `#NAND`

---

<a id="item-28"></a>
## [AI Leaders Declare End of Prompt Engineering, Embrace Loop Engineering](https://www.36kr.com/p/3873913078732036) ⭐️ 8.0/10

Jensen Huang, Andrew Ng, and other prominent AI figures have declared that prompt engineering is obsolete, advocating instead for loop engineering—autonomous systems that iteratively prompt themselves without human intervention. A widely shared 11-page whitepaper on loop engineering has circulated, and Anthropic reportedly has over 80% of its engineers using self-improving loops. This shift marks a fundamental change in how AI systems are designed, moving from human-in-the-loop prompting to fully autonomous loops, which could dramatically increase efficiency and scalability. It signals that the industry is prioritizing agentic workflows over manual prompt crafting, potentially rendering prompt engineering skills less valuable. The term 'Loop Engineering' was coined by Google Chrome engineer Addy Osmani in June 2026, and the whitepaper summarizes contributions from Peter Steinberger, Boris Cherny, and Addy Osmani. Karpathy's AutoResearch project exemplifies the concept with a generation-execution-evaluation-improve loop.

rss · 36氪 - 24小时热榜 · Jun 29, 08:23

**Background**: Prompt engineering has been the dominant approach for interacting with large language models (LLMs), requiring humans to craft specific prompts to get desired outputs. Loop engineering automates this by designing a system where an AI agent recursively sets goals, executes tasks, verifies results, and persists memory, operating 24/7 with minimal human oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/what-is-loop-engineering-ai-agents-2026">What Is Loop Engineering? Beyond Prompt Engineering in 2026 ...</a></li>
<li><a href="https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/">Loop Engineering: The Guide for AI Agents | Lushbinary</a></li>
<li><a href="https://www.businesstoday.in/technology/artificial-intelligence/story/what-is-loop-engineering-the-ai-trend-replacing-prompt-engineering-539754-2026-06-29">What is loop engineering? The AI trend replacing prompt ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Prompt Engineering`, `#Loop Engineering`, `#Machine Learning`, `#LLM`

---

<a id="item-29"></a>
## [Phishing App 'MobileClaw' Steals AI Access Tokens](https://linux.do/t/topic/2498147) ⭐️ 8.0/10

A suspicious phishing app named MobileClaw was discovered, promoted via email, that tricks users into providing their access tokens for AI services like Codex, Claude, and OpenRouter by offering a seemingly legitimate client. Access tokens grant full control over AI service accounts and billing; this phishing campaign poses a direct threat to developers and AI users, risking data breaches and financial loss. The app's official website is a third-level domain, the sender uses a duck email address, and no legitimate company affiliation or contact information is provided, which are strong indicators of phishing.

rss · LINUX DO - 最新话题 · Jun 29, 23:18

**Background**: Access tokens are credentials used to authenticate API requests to AI services like OpenAI's Codex or Anthropic's Claude, often obtained via OAuth flow. Phishing apps trick users into authorizing token generation, granting attackers unauthorized access. OpenRouter is a unified API gateway that routes requests to multiple LLM providers, making its tokens a valuable target.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2026/04/06/ai-enabled-device-code-phishing-campaign-april-2026/">Inside an AI‑enabled device code phishing campaign ...</a></li>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>

</ul>
</details>

**Discussion**: The community warns others not to log in to the app even if installed, as it is likely a phishing attempt, though the evidence is not yet conclusive.

**Tags**: `#security`, `#phishing`, `#access-token`, `#warning`, `#AI-services`

---

<a id="item-30"></a>
## [Google's AI Peer-Reviewer Handles ~10K Papers at Top Conferences](https://www.reddit.com/r/MachineLearning/comments/1uio9rb/googles_agentic_peerreviewer_handled_10k_papers/) ⭐️ 8.0/10

Google deployed an agentic AI peer-reviewer that processed approximately 10,000 papers at ICML and STOC conferences, achieving a 34% improvement in detecting mathematical errors compared to zero-shot prompting. The results are formally documented in a research paper now available on arXiv. This marks a significant practical deployment of AI in scientific peer review at scale, potentially accelerating review processes and improving error detection. It sets a precedent for AI-assisted review in academic conferences, which could impact scientific integrity and efficiency. The AI system operates with a 30-minute turnaround per paper and uses an agentic approach, meaning it can use tools and make autonomous decisions within defined objectives. The 34% improvement is measured against zero-shot prompting, a baseline where the model is given no examples.

reddit · r/MachineLearning · /u/Justgototheeffinmoon · Jun 29, 10:05

**Background**: Agentic AI refers to AI systems that can pursue goals, use tools, and act autonomously, often within human-defined constraints. Zero-shot prompting is a prompt engineering technique where a model is given a task description without any examples, relying on its pre-trained knowledge. This research compares the agentic approach to that baseline for error detection in mathematical content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_prompting">Zero-shot prompting</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Peer Review`, `#Machine Learning`, `#Scientific Publishing`

---

<a id="item-31"></a>
## [EML Trees Proven as Universal Approximators](https://www.reddit.com/r/MachineLearning/comments/1uipl1t/eml_trees_are_universal_approximators_r/) ⭐️ 8.0/10

A new paper proves that EML trees, composed solely of the EML operator (exp(x) - ln(y)) and the constant 1, can approximate any continuous function on a compact interval to arbitrary precision, establishing them as universal approximators. This theoretical result bridges the gap between a simple algebraic structure and powerful approximation capabilities, potentially inspiring new architectures for symbolic regression or interpretable machine learning models. The proof uses explicit construction of elementary operations like polynomials and hyperbolic tangent as EML tree blocks, and handles the domain restriction of the natural logarithm via sign-based decompositions and affine maps.

reddit · r/MachineLearning · /u/JoeGermany · Jun 29, 11:16

**Background**: The EML operator, introduced by Andrzej Odrzywołek in 2026, is defined as eml(x, y) = exp(x) - ln(y). With the constant 1, it can express all elementary functions through composition. EML trees are binary trees where each internal node applies the eml function, with leaves being inputs or constants.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.21852">[2603.21852] All elementary functions from a single binary ... The EML Operator: Expressing All Elementary Functions with ... GitHub - gba3124/emltree: Compile elementary-function ... Examples of binary EML trees equivalent to few important ... EML Phylogenetic Tree - Robbobobbo The EML Weierstrass Theorem: Density of EML Trees in C([a,b])</a></li>
<li><a href="https://lilting.ch/en/articles/eml-single-operator-elementary-functions">The EML Operator: Expressing All Elementary Functions with ...</a></li>
<li><a href="https://graphicmaths.com/pure/special-functions/universal-eml-function/">GraphicMaths - A universal elementary function , EML</a></li>

</ul>
</details>

**Discussion**: The Reddit community generally views this as a high-value theoretical result. Commenters appreciate the explicit construction and connection to universal approximation theory, though some note practical limitations regarding the logarithm's domain and potential numerical stability issues.

**Tags**: `#Machine Learning`, `#Universal Approximation`, `#EML Trees`, `#Theoretical ML`

---

<a id="item-32"></a>
## [Samsung and SK Hynix Announce Massive AI Investment Plans](https://t.me/zaihuapd/42235) ⭐️ 8.0/10

Samsung plans to invest 1,000 trillion KRW ($648 billion) over ten years in AI, semiconductors, and data centers, while SK Hynix aims to double production capacity in five years and raise $29 billion through a US IPO. This is the largest investment plan in South Korean history, signaling a major shift toward AI hardware and infrastructure. It could reshape global semiconductor competition, positioning South Korea as a leader in AI chips and physical AI technologies. The announcement will be made on June 29 at a national briefing led by President Lee Jae-myung. Despite the ambitious plans, Samsung and SK Hynix shares both fell over 9% on the same day, partly due to concerns over Apple's chip demand.

telegram · zaihuapd · Jun 29, 07:00

**Background**: Physical AI refers to technologies that enable autonomous machines like robots and self-driving cars to perceive, understand, and perform complex tasks in the real world. This investment focus on 'physical AI' and AI data centers reflects a strategic bet on the next wave of AI beyond software, into embodied systems that interact with the physical environment.

<details><summary>References</summary>
<ul>
<li><a href="https://www.winzheng.jp/article/physical-ai-moment-everyone-wants">物 理 AI ... | Winzheng AI ニュース</a></li>
<li><a href="https://m.pedaily.cn/news/564774">就因为会「搬砖」了， 物 理 AI 一夜爆火|投资界</a></li>

</ul>
</details>

**Tags**: `#AI`, `#semiconductor`, `#investment`, `#Samsung`, `#SK Hynix`

---

<a id="item-33"></a>
## [Algorithm erroneously retracts Max Planck's 1940s papers](https://arstechnica.com/science/2026/06/why-did-this-journal-retract-two-1940s-papers-by-max-planck/) ⭐️ 8.0/10

Two papers by Max Planck from the 1940s were retracted and deleted from the journal Naturwissenschaften, likely due to an automated screening system misclassifying them as violating journal policies. The retractions were discovered by historian Yves Gingras and reported via Retraction Watch. This incident exposes critical flaws in automated content screening systems that lack historical context, potentially destroying important scientific records. It underscores the need for human oversight in retraction decisions, especially for older papers. The retracted papers were completely removed from the journal's website, leaving only blank pages with a notice of withdrawal, instead of the typical practice of prominently marking them as retracted. The current editor-in-chief stated he was unaware of the retractions and suggested they were likely an error by an automated detection system.

telegram · zaihuapd · Jun 29, 08:46

**Background**: Automated integrity screening tools are increasingly used by journals to detect potential misconduct such as plagiarism or fabricated content. However, these systems often fail to understand historical context and may flag older papers due to format or citation anomalies. Retraction Watch is a blog that tracks retractions and has been instrumental in uncovering such incidents. The case highlights the tension between efficiency in screening and the need for nuanced human judgment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retraction_Watch">Retraction Watch</a></li>
<li><a href="https://retractionwatch.com/">Retraction Watch – Tracking retractions as a window into the...</a></li>
<li><a href="https://cen-online.org/ai-assisted-integrity-screening-in-scientific-publishing-benefits-limits-and-trust-signals/">AI Integrity Screening in Scientific Publishing Explained</a></li>

</ul>
</details>

**Tags**: `#algorithmic bias`, `#academic publishing`, `#automated detection`, `#Max Planck`, `#science policy`

---