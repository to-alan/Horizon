---
layout: default
title: "Horizon Summary: 2026-07-09 (EN)"
date: 2026-07-09
lang: en
---

> From 309 items, 33 important content pieces were selected

---

1. [TypeScript 7.0 Delivers Up to 11.9x Speed Boost](#item-1) ⭐️ 10.0/10
2. [OpenAI Launches GPT-Live Voice Assistant with GPT-5.5 Delegation](#item-2) ⭐️ 9.0/10
3. [Microsoft Ports TypeScript to Go for 10x Performance Boost](#item-3) ⭐️ 9.0/10
4. [Temporal: Open-source durable execution platform for reliable workflows](#item-4) ⭐️ 9.0/10
5. [MoWorld: First Real-Time World Model at 50FPS on Domestic NPUs](#item-5) ⭐️ 9.0/10
6. [Critical Linux KVM Vulnerability CVE-2026-53359 Allows VM Escape After 16 Years](#item-6) ⭐️ 9.0/10
7. [Agentic Safety Triggers Bypass Textual Guardrails in LLM Agents](#item-7) ⭐️ 9.0/10
8. [Decoding obfuscated bash script on Uniqlo t-shirt](#item-8) ⭐️ 8.0/10
9. [Bun Rewrites from Zig to Rust: Smaller, Faster, Safer](#item-9) ⭐️ 8.0/10
10. [Mistral Releases Robostral Navigate: Map-Less AI Navigation](#item-10) ⭐️ 8.0/10
11. [Cloudflare Meerkat: Leaderless Async Consensus](#item-11) ⭐️ 8.0/10
12. [EU Revives Private Message Scanning Rules](#item-12) ⭐️ 8.0/10
13. [GitHub Repository Tracks Leaked AI System Prompts](#item-13) ⭐️ 8.0/10
14. [.NET Agent Skills Repository Launched for AI Coding Agents](#item-14) ⭐️ 8.0/10
15. [Kyutai Releases Pocket TTS: CPU-Friendly Open-Source TTS](#item-15) ⭐️ 8.0/10
16. [Agent Skills Repository Released by Anthropic](#item-16) ⭐️ 8.0/10
17. [n8n: Open-Source AI Workflow Automation Platform](#item-17) ⭐️ 8.0/10
18. [Dynamo: Open-source datacenter-scale inference serving](#item-18) ⭐️ 8.0/10
19. [uv: Fast Python Package Manager in Rust](#item-19) ⭐️ 8.0/10
20. [Microsoft's windows-rs: Rust bindings for Windows APIs](#item-20) ⭐️ 8.0/10
21. [Tencent Open-Sources WeKnora: RAG, Agent, Wiki Platform](#item-21) ⭐️ 8.0/10
22. [SOPS: Simple & Flexible Secrets Management Tool](#item-22) ⭐️ 8.0/10
23. [LocalAI: Open-source AI engine runs models on any hardware, no GPU required](#item-23) ⭐️ 8.0/10
24. [Meta developing 'super sensing' glasses with always-on recording](#item-24) ⭐️ 8.0/10
25. [SpaceXAI Launches Grok 4.5: Programming AI Co-Trained with Cursor](#item-25) ⭐️ 8.0/10
26. [Anthropic to Surpass $1B Profit, Secretly Files for IPO](#item-26) ⭐️ 8.0/10
27. [Sony faces €4B class-action over physical disc phase-out](#item-27) ⭐️ 8.0/10
28. [Cloudflare and OpenAI Pilot Using Network Signals for AI Search](#item-28) ⭐️ 8.0/10
29. [LingBot-Video: 13B Sparse MoE Video Diffusion World Model Open-Sourced](#item-29) ⭐️ 8.0/10
30. [DeepSeek Develops Own AI Inference Chip to Reduce Supplier Reliance](#item-30) ⭐️ 8.0/10
31. [Alibaba Bans Employees from Using Claude](#item-31) ⭐️ 8.0/10
32. [Android Remote Root Exploit 'IonStack' Threatens All Versions](#item-32) ⭐️ 8.0/10
33. [Smartphone apps identified via leaked EM signals with 99% accuracy](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 Delivers Up to 11.9x Speed Boost](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 10.0/10

Microsoft announced TypeScript 7.0, a major version upgrade that introduces a new compiler architecture yielding up to 11.9 times faster performance on large codebases like VS Code. This dramatic speed improvement addresses one of TypeScript's longstanding pain points—slow compilation on large projects—making it more viable for very large codebases and improving developer productivity. Benchmarks show VS Code compilation dropped from 125.7 seconds in TypeScript 6 to 10.6 seconds, while other projects like Sentry and Bluesky saw 8.9x and 8.7x speedups respectively.

hackernews · DanRosenwasser · Jul 8, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48833715)

**Background**: TypeScript is a statically typed superset of JavaScript that compiles to plain JavaScript. The compiler, traditionally written in TypeScript itself, can become a bottleneck for large projects. This update likely involves a rewrite in a lower-level language or significant architectural changes to achieve such gains.

**Discussion**: The community overwhelmingly praised the announcement, with commenters highlighting the massive speed improvements and congratulating the team. Some noted that Node.js native type stripping reduces reliance on tsc, but the performance gains still make TypeScript 7 attractive.

**Tags**: `#TypeScript`, `#performance`, `#compiler`, `#Microsoft`, `#programming languages`

---

<a id="item-2"></a>
## [OpenAI Launches GPT-Live Voice Assistant with GPT-5.5 Delegation](https://openai.com/index/introducing-gpt-live/) ⭐️ 9.0/10

OpenAI launched GPT-Live on July 27, 2026, a full-duplex voice assistant capable of delegating complex queries to GPT-5.5 in the background for extended, natural conversations. GPT-Live bridges the gap between voice interfaces and frontier AI models, enabling users to have seamless, intelligent conversations without sacrificing reasoning capability. This could transform daily interactions with AI for tasks like brainstorming, research, and personal assistance. GPT-Live uses a full-duplex architecture for simultaneous listening and speaking, with natural backchannels like 'mhmm' and 'yeah'. Delegation to GPT-5.5 occurs automatically for tasks requiring web search, deep reasoning, or agentic steps, while the voice layer maintains continuous interaction.

hackernews · logickkk1 · Jul 8, 17:03 · [Discussion](https://news.ycombinator.com/item?id=48834405)

**Background**: GPT-5.5 (codename 'Spud') is OpenAI's most capable large language model, released on April 23, 2026, offering faster and more complex reasoning. Previous ChatGPT voice modes used older models, limiting their intelligence. GPT-Live addresses this by pairing a real-time voice layer with GPT-5.5's background processing.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT-Live | OpenAI</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.5">GPT-5.5 - Wikipedia</a></li>
<li><a href="https://mer.vin/2026/07/gpt-live-explained-full-duplex-chatgpt-voice-with-gpt-5-5-delegation/">GPT-Live Explained: Full-Duplex ChatGPT Voice With GPT-5.5 ...</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some users praise the delegation feature for enabling productive hour-long conversations, while others express concerns about social replacement, lack of tool integration, and potential societal harm. A bug was reported where the assistant interrupts and laughs at unintended moments.

**Tags**: `#OpenAI`, `#GPT Live`, `#voice assistant`, `#AI`, `#GPT-5.5`

---

<a id="item-3"></a>
## [Microsoft Ports TypeScript to Go for 10x Performance Boost](https://github.com/microsoft/typescript-go) ⭐️ 9.0/10

Microsoft has announced a native port of the TypeScript compiler to Go, with preview builds available on npm as @typescript/native-preview and a preview VS Code extension. The port aims to deliver a 10x performance improvement over the current TypeScript compiler. This port promises to significantly speed up TypeScript development workflows, especially for large codebases, and could lead to faster editor experiences and build times. It marks a major shift in TypeScript's implementation strategy, potentially influencing the broader JavaScript ecosystem. The preview build supports most core features like parsing, type checking, and declaration emit, but the Language Server Protocol (LSP) is still in progress and the API is not yet ready. The final version, expected to ship as TypeScript 7.0, will eventually merge back into the main TypeScript repository.

rss · GitHub Trending - Go Daily · Jul 8, 01:35

**Background**: TypeScript is a popular typed superset of JavaScript that compiles to plain JavaScript. The current compiler is written in TypeScript itself, which can be slow for large projects. By rewriting the compiler in Go, a compiled language known for high performance and efficient concurrency, Microsoft aims to achieve substantial speedups.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/typescript-go">GitHub - microsoft/typescript-go: Staging repo for development of native port of TypeScript · GitHub</a></li>
<li><a href="https://devblogs.microsoft.com/typescript/typescript-native-port/">A 10x Faster TypeScript - TypeScript</a></li>
<li><a href="https://www.reddit.com/r/ProgrammingLanguages/comments/1j9osva/typescript_compiler_is_being_ported_to_go/">r/ProgrammingLanguages on Reddit: TypeScript compiler is being ported to Go</a></li>

</ul>
</details>

**Tags**: `#TypeScript`, `#Go`, `#performance`, `#compiler`, `#port`

---

<a id="item-4"></a>
## [Temporal: Open-source durable execution platform for reliable workflows](https://github.com/temporalio/temporal) ⭐️ 9.0/10

Temporal is an open-source durable execution platform that enables developers to build scalable and reliable distributed systems through workflow orchestration. It automatically handles failures and retries, ensuring resilient execution of application logic. Temporal addresses critical challenges in building distributed systems, such as managing state across failures and ensuring reliability without sacrificing productivity. Its adoption by major companies highlights its significance in the microservices ecosystem. Temporal originated as a fork of Uber's Cadence and is developed by Temporal Technologies. It provides a server that executes Workflows, with SDKs available for Go and Java, and includes a web UI for monitoring.

rss · GitHub Trending - Go Daily · Jul 8, 01:35

**Background**: Durable execution platforms like Temporal ensure that long-running workflows survive crashes and failures by persisting their state. They decouple application logic from infrastructure, allowing developers to focus on business rules while the platform handles retries and state recovery. Temporal is a mature technology widely used in industry.

<details><summary>References</summary>
<ul>
<li><a href="https://temporal.io/">Durable Execution Solutions | Temporal</a></li>
<li><a href="https://temporal.io/blog/what-is-durable-execution">The definitive guide to Durable Execution | Temporal</a></li>
<li><a href="https://medium.com/@surajsub_68985/temporal-revolutionizing-workflow-orchestration-in-microservices-architectures-f8265afa4dc0">Temporal : Revolutionizing Workflow Orchestration in Microservices Architectures — Part 1 | by Suraj Subramanian | Medium</a></li>

</ul>
</details>

**Tags**: `#workflow orchestration`, `#distributed systems`, `#Go`, `#microservices`, `#reliability`

---

<a id="item-5"></a>
## [MoWorld: First Real-Time World Model at 50FPS on Domestic NPUs](https://www.36kr.com/p/3886462577094915) ⭐️ 9.0/10

Chinese team Moxin Technology and Zhejiang University released MoWorld, the first real-time interactive world model achieving over 50FPS inference on domestic NPUs (Huawei Ascend 910C), with training and deployment fully on domestic hardware. This breakthrough solves the real-time bottleneck for world models, enabling applications in gaming, robotics, autonomous driving, and digital twins at 70% lower cost than GPU solutions, marking a key step toward commercialization. MoWorld is a 14B-parameter MoE model running on Huawei Ascend 910C CloudMatrix384 NPU, featuring 2000-frame long-sequence training and inference, and supporting full 6-DOF camera control at 1080P resolution.

rss · 36氪 - 24小时热榜 · Jul 8, 04:09

**Background**: World models are AI systems that learn environment dynamics from video and interaction data, but previous models struggled with real-time inference (typically 5-10FPS). NPUs (Neural Processing Units) are specialized chips for AI acceleration; domestic NPUs like Huawei Ascend aim to reduce reliance on NVIDIA GPUs. MoWorld introduces the 'Flash World Model' concept for real-time deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.13678">[2510.13678] FlashWorld: High-quality 3D Scene Generation within Seconds</a></li>
<li><a href="https://www.techpowerup.com/321033/arm-china-develops-npu-accelerator-for-ai-targeting-domestic-cpus">Arm China Develops NPU Accelerator for AI, Targeting Domestic ...</a></li>
<li><a href="https://grokipedia.com/page/4D_world_model">4D world model</a></li>

</ul>
</details>

**Tags**: `#world model`, `#real-time interaction`, `#NPU`, `#AI`, `#domestic hardware`

---

<a id="item-6"></a>
## [Critical Linux KVM Vulnerability CVE-2026-53359 Allows VM Escape After 16 Years](https://t.me/vps_xhq/815) ⭐️ 9.0/10

A critical use-after-free vulnerability in Linux KVM's shadow MMU, CVE-2026-53359 (Januscape), was disclosed allowing guest-to-host VM escape and root code execution on the host. Patches have been merged into the Linux kernel mainline as of mid-June 2026. This vulnerability poses a severe threat to public cloud and multi-tenant environments relying on KVM for workload isolation, as any guest with root privileges can escape to the host. Its 16-year undetected presence highlights the challenge of auditing legacy kernel code. The flaw affects both Intel and AMD x86 systems and is especially dangerous when nested virtualization is enabled. On systems like RHEL and CloudLinux with world-writable /dev/kvm, local unprivileged users can trigger the exploit without running a production VM.

rss · VPS信号旗播报 - Telegram Channel · Jul 8, 02:23

**Background**: KVM (Kernel-based Virtual Machine) is a Linux kernel module that enables the host to act as a hypervisor. The shadow MMU manages guest memory translations; a use-after-free bug in this code allows a malicious VM to corrupt host kernel memory, breaking isolation.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudlinux.com/januscape-cve-2026-53359-mitigation-and-kernel-update-on-cloudlinux/">Januscape (CVE-2026-53359): Mitigation and Kernel Update on CloudLinux - CloudLinux</a></li>
<li><a href="https://dailysecurityreview.com/resources/cve-2026-53359-januscape-16-year-kvm-flaw-enables-vm-escape/">CVE-2026-53359 Januscape: 16-Year KVM Flaw Enables VM Escape</a></li>
<li><a href="https://thecybersecguru.com/news/cve-2026-53359-januscape-kvm-guest-to-host-escape/">CVE-2026-53359 Januscape: 16-Year-Old KVM Escape Bug Explained | The CyberSec Guru</a></li>

</ul>
</details>

**Tags**: `#Linux kernel`, `#KVM`, `#vulnerability`, `#VM escape`, `#security`

---

<a id="item-7"></a>
## [Agentic Safety Triggers Bypass Textual Guardrails in LLM Agents](https://www.reddit.com/r/MachineLearning/comments/1ur1fnz/agentic_safety_triggers_arent_textual_safety/) ⭐️ 9.0/10

Researchers demonstrated that LLM agents using Model Context Protocol (MCP) tool access are vulnerable to attacks embedded in tool-call sequences, which evade traditional text-based safety guardrails. Even state-of-the-art safety tuning like DPO and SafeDPO only raises refusal rates to 48%, while base models refuse less than 35% of these attacks. This finding exposes a fundamental blind spot in current LLM safety alignment methods, which treat attack detection as a text classification problem. As AI agents gain real-world tool access, this vulnerability could lead to serious security breaches, necessitating new safety paradigms that account for agentic actions. The attacks exploit known CVEs by crafting tool-call sequences that appear as ordinary text requests. The study tested models with 1B–14B parameters using MCP filesystem IO, and found that training-free methods achieved roughly 3x the baseline refusal rate without fine-tuning.

reddit · r/MachineLearning · /u/mlsandwich · Jul 8, 18:36

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic to standardize how AI systems connect to external tools and data sources. Direct Preference Optimization (DPO) is a preference-tuning method for LLMs that avoids explicit reward models, and SafeDPO extends it with enhanced safety constraints. Traditional guardrails operate on text input, but agentic systems execute tool calls that can carry attack sequences not evident in the text.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2305.18290">[2305.18290] Direct Preference Optimization: Your Language ... Direct Preference Optimization (DPO) of LLMs: A Paradigm Shift Direct Preference Optimization (DPO): An In-depth Analysis [2510.05703] Provably Convergent Primal-Dual DPO for ... Preference Tuning LLMs with Direct Preference Optimization ... Direct preference optimization - Microsoft Foundry</a></li>
<li><a href="https://arxiv.org/abs/2505.20065">[2505.20065] SafeDPO: A Simple Approach to Direct Preference Optimization with Enhanced Safety</a></li>

</ul>
</details>

**Tags**: `#LLM safety`, `#AI agents`, `#MCP`, `#adversarial attacks`, `#security vulnerabilities`

---

<a id="item-8"></a>
## [Decoding obfuscated bash script on Uniqlo t-shirt](https://tris.sherliker.net/blog/obfuscated-self-evaluating-bash-script-by-cdn-akamai-being-supplied-to-consumers-via-retail-stores/) ⭐️ 8.0/10

A blog post decodes an obfuscated, self-evaluating bash script printed on a Uniqlo x Akamai t-shirt, revealing its inner workings and syntax errors. This unique blend of programming puzzles and fashion design has sparked high community engagement, highlighting the cultural intersection of code and consumer products. The script uses Bash eval for self-evaluation and contains deliberate obfuscation techniques, but also includes syntax errors that make it non-functional. The font is Roboto Mono, but the typesetting is non-monospace, likely due to optical kerning in InDesign.

hackernews · speerer · Jul 8, 08:46 · [Discussion](https://news.ycombinator.com/item?id=48829312)

**Background**: Bash obfuscation involves making scripts hard to read by using techniques like variable substitution, eval, and encoding. Tools like Bashfuscator exist for generating such scripts. Self-evaluating scripts use eval to execute code constructed during runtime, often for puzzles or security contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Bashfuscator/Bashfuscator">GitHub - Bashfuscator/Bashfuscator: A fully configurable and ...</a></li>
<li><a href="https://earthly.dev/blog/safely-using-bash-eval/">Bash eval: Understanding and (Safely) Using the Power of Dynamic Code Evaluation - Earthly Blog</a></li>

</ul>
</details>

**Discussion**: Commenters noted the irony of a shirt with a syntax error, suggested similar works like Martin Kleppe's Quine Clock, analyzed the font typesetting issues, and shared a video from the designer explaining the intentional OCR-difficult design.

**Tags**: `#bash`, `#obfuscation`, `#uniqlo`, `#script`, `#community-discussion`

---

<a id="item-9"></a>
## [Bun Rewrites from Zig to Rust: Smaller, Faster, Safer](https://bun.com/blog/bun-in-rust) ⭐️ 8.0/10

The Bun JavaScript runtime has been rewritten from Zig to Rust, yielding a 20% smaller binary, 5% performance improvement, and fixing long-standing memory leaks. This demonstrates that a switch to Rust can bring tangible improvements in performance, stability, and binary size for a high-profile runtime, potentially influencing language choices in systems programming. The binary size reduction came from combining the Rust rewrite, ICU changes, and identical code folding. The 5% performance gain is modest but the stability improvements from fixing memory leaks are significant.

hackernews · afturner · Jul 8, 21:49 · [Discussion](https://news.ycombinator.com/item?id=48837877)

**Background**: Bun is a fast all-in-one JavaScript runtime, bundler, and package manager, originally written in Zig. Zig is a system programming language designed as an improvement to C, with manual memory management and a focus on simplicity. However, Zig's explicitness and lack of abstractions can lead to verbose code and potential memory issues. Rust is a memory-safe systems language with zero-cost abstractions, making it attractive for performance-critical applications.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**Discussion**: The community discussed the negative implications for Zig, noting that a naive rewrite to Rust fixed memory leaks and improved stability. Others debated the high cost of AI-assisted rewriting, estimating over $25k in API costs, and questioned its efficiency versus hiring engineers. Some appreciated the disciplined approach to ensuring correctness.

**Tags**: `#Rust`, `#Zig`, `#Bun`, `#performance`, `#rewrite`

---

<a id="item-10"></a>
## [Mistral Releases Robostral Navigate: Map-Less AI Navigation](https://mistral.ai/news/robostral-navigate/) ⭐️ 8.0/10

Mistral AI released Robostral Navigate, an 8-billion-parameter model that enables robots to navigate complex environments using only a single RGB camera and natural language instructions, achieving 76.6% on the R2R-CE benchmark. This marks Mistral's first formal product in embodied AI, extending their reach from language models into physical systems, and demonstrates a major milestone in map-less navigation, which could significantly lower the hardware requirements for autonomous robots. Robostral Navigate is an 8B parameter model that requires no depth sensors, LiDAR, or multiple cameras—only a single RGB camera and natural language commands. It achieves state-of-the-art results on the R2R-CE benchmark, but the model is not openly available.

hackernews · ottomengis · Jul 8, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48832212)

**Background**: Traditional robot navigation often relies on pre-mapped environments or expensive sensor arrays like LiDAR. Map-less navigation, where a robot explores and follows directions without a prior map, has long been a challenge, especially indoors. Models like Robostral Navigate use vision and language to overcome this, but privacy concerns about such technology have been raised, as it could enable stalking or surveillance.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate: single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://www.siliconreport.com/mistral-ai-releases-robostral-navigate-a-single-camera-robotics-model-95dac18d">Mistral AI Releases Robostral Navigate, a Single-Camera ...</a></li>
<li><a href="https://theaidude.net/blog/mistral-robostral-navigate-8b-single-camera-robotics-model-launch">Mistral Robostral Navigate: One Camera, 8B Params</a></li>

</ul>
</details>

**Discussion**: Commenters are impressed by the map-less capability, noting the historic 'kidnapped robot' problem. Some expressed excitement for hobbyist applications, but noted the model is not openly available. Others raised privacy concerns similar to Stanford's PIGEON model, which was withheld due to stalking risks.

**Tags**: `#robotics`, `#AI`, `#navigation`, `#Mistral`, `#deep learning`

---

<a id="item-11"></a>
## [Cloudflare Meerkat: Leaderless Async Consensus](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare Research has introduced Meerkat, a globally distributed consensus service that implements the QuePaxa algorithm, achieving the first production deployment of an asynchronous consensus protocol. Meerkat represents a significant step forward in distributed consensus, as it operates without relying on timeouts, making it more resilient to network instability and suitable for global-scale systems. Based on QuePaxa, Meerkat is a crash fault-tolerant, asynchronous consensus algorithm that uses hedging and adaptive leader selection to maintain performance under adverse conditions.

hackernews · bobnamob · Jul 8, 13:18 · [Discussion](https://news.ycombinator.com/item?id=48831565)

**Background**: Classic consensus algorithms like Paxos and Raft are partially synchronous, relying on timeouts and assuming bounded message delays. Asynchronous consensus algorithms like QuePaxa do not require timeouts, providing liveness even under unpredictable network conditions, but they have traditionally been too slow for practical use. Meerkat aims to demonstrate that asynchronous consensus can be efficient enough for production systems.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/meerkat-introduction/">Introducing Meerkat: an experiment in global consensus</a></li>
<li><a href="https://github.com/dedis/quepaxa">GitHub - dedis/quepaxa: This is the code repository for ...</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus QuePaxa: Escaping the Tyranny of Timeouts in Consensus QuePaxa: Escaping the tyranny of timeouts in consensus QuePaxa: Escaping the Tyranny of Timeouts in Consensus PasinduTennage/quepaxa-fork-for-internal - GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Meerkat's leaderless nature makes direct comparison to Raft misleading, as Raft is designed specifically for strong leadership. Others pointed out the trade-off of requiring global consensus for every read, which may limit use cases. However, some praised the potential of an asynchronous algorithm for messy networks, while cautioning that it is not yet in production.

**Tags**: `#distributed-systems`, `#consensus`, `#cloudflare`, `#asynchronous`, `#QuePaxa`

---

<a id="item-12"></a>
## [EU Revives Private Message Scanning Rules](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/) ⭐️ 8.0/10

The European Union is one step away from reviving the so-called 'Chat Control 1.0' rules, which would allow service providers to voluntarily scan non-end-to-end encrypted messages for child sexual abuse material (CSAM). A procedural vote has been scheduled to advance the regulation. This development reopens the debate on privacy and encryption in the EU, as it could set a precedent for allowing scanning of private communications. It also highlights the distinction between voluntary scanning of non-E2EE messages and the more controversial mandatory scanning and E2EE bans proposed in Chat Control 2.0. Chat Control 1.0 only permits scanning of messages that are not protected by end-to-end encryption, such as those in transit where the provider holds the keys. It does not mandate scanning—providers may choose to implement it. This is distinct from Chat Control 2.0, which would require scanning and could effectively ban end-to-end encryption.

hackernews · ggirelli · Jul 8, 16:53 · [Discussion](https://news.ycombinator.com/item?id=48834296)

**Background**: Chat Control refers to a set of proposed EU regulations aimed at combating child sexual abuse material (CSAM) online. The initial proposal (Chat Control 1.0) from May 2022 allows voluntary scanning of non-E2EE communications. A more controversial version (Chat Control 2.0) would mandate client-side scanning of all communications, including E2EE, which critics say would undermine encryption and privacy. Client-side scanning is a technique where content is scanned on the user's device before encryption or sending.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://www.internetsociety.org/resources/doc/2020/fact-sheet-client-side-scanning/">Fact Sheet: Client-Side Scanning - Internet Society</a></li>
<li><a href="https://cointelegraph.com/news/eu-to-again-vote-to-extend-chat-control-rules">EU Again Set For Vote on ‘Chat Control’ - Cointelegraph</a></li>

</ul>
</details>

**Discussion**: Commenters emphasized the importance of distinguishing between Chat Control 1.0 and 2.0. One user noted that 1.0 only allows providers to scan non-E2EE messages, which is already expected (e.g., Facebook scanning messages). Another warned that client-side scanning, pushed by organizations like the Internet Watch Foundation, remains a concern. A user also provided a link for EU citizens to contact representatives.

**Tags**: `#privacy`, `#EU`, `#encryption`, `#surveillance`, `#policy`

---

<a id="item-13"></a>
## [GitHub Repository Tracks Leaked AI System Prompts](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 8.0/10

A GitHub repository, asgeirtj/system_prompts_leaks, systematically collects and updates leaked system prompts from major AI models such as Claude, ChatGPT, Gemini, Grok, and others, and has been featured by The Washington Post. This repository provides unprecedented transparency into the hidden instructions that govern AI behavior, enabling researchers, developers, and the public to understand and audit how AI models are programmed behind the scenes. The repo includes prompts from models like Claude Fable 5, Opus 4.8, GPT-5.5 Codex, Gemini 3.5 Flash, and Google Antigravity, along with diffs between versions, such as Claude Opus 4.8 to Fable 5.

rss · GitHub Trending - Daily · Jul 8, 01:32

**Background**: System prompts are foundational instructions that define an AI model's behavior, tone, and reasoning approach. They are typically hidden from users and set by developers to control how the AI responds. Leaked prompts reveal these hidden rules, allowing comparison and analysis of different models' design choices.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@david.p.lemon79/system-prompts-explained-how-ai-models-actually-work-behind-the-scenes-2265f14e3eba">System Prompts Explained: How AI Models Actually ... - Medium</a></li>
<li><a href="https://blog.promptlayer.com/system-prompt-vs-user-prompt-a-comprehensive-guide-for-ai-prompts/">System Prompt vs User Prompt in AI: What's the difference?</a></li>

</ul>
</details>

**Tags**: `#AI`, `#system prompts`, `#AI safety`, `#transparency`, `#open source`

---

<a id="item-14"></a>
## [.NET Agent Skills Repository Launched for AI Coding Agents](https://github.com/dotnet/skills) ⭐️ 8.0/10

The .NET team has launched the dotnet/skills repository, a curated set of skills and plugins for AI coding agents to assist with .NET and C# development. The repository includes a dashboard for accuracy scoring and follows the open Agent Skills standard. This official initiative enhances AI tooling for .NET developers, enabling coding agents to more accurately handle .NET-specific tasks such as project upgrades, testing, and debugging. It fosters ecosystem integration by providing a standardized way to extend AI agent capabilities. The repository contains 12 plugins covering areas like C# language server integration, MSBuild, NuGet, .NET MAUI, AI/ML, and test migration. Each plugin follows the Agent Skills format, which uses a SKILL.md file for instructions and can include scripts and other resources.

rss · GitHub Trending - Daily · Jul 8, 01:32

**Background**: Agent Skills is a lightweight, open format for extending AI agent capabilities with specialized knowledge and workflows. A skill is a folder containing a SKILL.md file with metadata and instructions. The .NET team's curated skills aim to improve the accuracy and efficiency of coding agents when working with .NET technologies.

<details><summary>References</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills</a></li>
<li><a href="https://devblogs.microsoft.com/dotnet/extend-your-coding-agent-with-dotnet-skills/">Extend your coding agent with .NET Skills - .NET Blog</a></li>

</ul>
</details>

**Tags**: `#.NET`, `#C#`, `#AI agents`, `#coding agents`, `#skills`

---

<a id="item-15"></a>
## [Kyutai Releases Pocket TTS: CPU-Friendly Open-Source TTS](https://github.com/kyutai-labs/pocket-tts) ⭐️ 8.0/10

Kyutai Labs has released Pocket TTS, a lightweight text-to-speech model with 100 million parameters that runs efficiently on CPUs without requiring a GPU. It supports Python APIs, CLI, and browser inference, along with voice cloning and multi-language support. This significantly lowers the barrier to deploying TTS on edge devices and personal computers, enabling offline, low-latency speech synthesis without expensive hardware. It also promotes open-source accessibility in AI voice generation. The model achieves approximately 200ms first-chunk latency and runs 6x faster than real-time on a MacBook Air M4 using only 2 CPU cores. It supports English, French, German, Portuguese, Italian, and Spanish, with additional languages planned.

rss · GitHub Trending - Daily · Jul 8, 01:32

**Background**: Traditional text-to-speech models often require powerful GPUs or cloud APIs, limiting their use in offline or resource-constrained environments. Pocket TTS is designed specifically for CPU inference, making it suitable for laptops, mobile devices, and browser-based applications.

**Tags**: `#TTS`, `#machine-learning`, `#CPU-inference`, `#open-source`, `#AI`

---

<a id="item-16"></a>
## [Agent Skills Repository Released by Anthropic](https://github.com/anthropics/skills) ⭐️ 8.0/10

Anthropic has released a public GitHub repository (anthropics/skills) containing open-source skills for Claude, including task-specific instructions and scripts that Claude can load dynamically to improve performance on specialized tasks. This release democratizes access to advanced AI agent capabilities, enabling developers and users to customize Claude with repeatable workflows for creative, technical, and enterprise tasks. It also establishes an open standard (Agent Skills) that is gaining adoption across multiple AI platforms, including OpenAI and Cursor. The repository contains demonstration skills across creative, technical, and enterprise domains, with each skill in a self-contained folder with a SKILL.md file. Notably, it includes the source-available document editing skills (docx, pdf, pptx, xlsx) that power Claude's production document capabilities, licensed under a source-available license rather than open source.

rss · GitHub Trending - Python Daily · Jul 8, 01:38

**Background**: Agent Skills is an open standard that allows AI agents to dynamically load task-specific instructions and scripts, improving their reliability for real-world tasks. The standard was initially developed by Anthropic for Claude, but has since been adopted by other AI tools like OpenAI's ChatGPT and Codex CLI, Cursor, and Gemini CLI. The skills.sh index serves as a registry for discovering skills.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/skills">GitHub - anthropics/skills: Public repository for Agent Skills</a></li>
<li><a href="https://inference.sh/blog/skills/agent-skills-overview">Agent Skills: The Open Standard for AI Capabilities | blog | inference.sh</a></li>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub</a></li>

</ul>
</details>

**Tags**: `#Agent Skills`, `#Claude`, `#Anthropic`, `#AI Tooling`, `#GitHub`

---

<a id="item-17"></a>
## [n8n: Open-Source AI Workflow Automation Platform](https://github.com/n8n-io/n8n) ⭐️ 8.0/10

n8n now offers over 1500 integrations and native AI agent capabilities for building and deploying AI workflows, combining visual building with custom code. This provides an open-source, self-hostable alternative to proprietary automation tools, enabling developers to integrate AI into workflows with full control over data and infrastructure. n8n is licensed under the Sustainable Use License (fair-code), meaning source code is visible and self-hostable, but commercial use may be restricted. It supports connecting to multiple AI models including OpenAI, Anthropic, Google, and open-source models.

rss · GitHub Trending - TypeScript Daily · Jul 8, 01:41

**Background**: n8n is a fair-code workflow automation platform that competes with tools like Zapier and Make. The fair-code license allows access and modification of source code but prohibits certain commercial uses such as offering the software as a paid service. This model aims to balance openness with sustainability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fair_License">Fair License - Wikipedia</a></li>
<li><a href="https://faircode.io/">Fair-code</a></li>

</ul>
</details>

**Tags**: `#workflow automation`, `#AI agents`, `#open-source`, `#integration`, `#fair-code`

---

<a id="item-18"></a>
## [Dynamo: Open-source datacenter-scale inference serving](https://github.com/ai-dynamo/dynamo) ⭐️ 8.0/10

Dynamo, an open-source datacenter-scale distributed inference serving framework, has been released on GitHub. It orchestrates multiple inference engines like vLLM to coordinate multi-node inference with features such as disaggregated serving and intelligent routing. As large language models and multimodal AI scale to multiple GPUs and nodes, efficient distributed inference becomes critical. Dynamo provides a unified orchestration layer that maximizes throughput and minimizes latency, potentially reducing infrastructure costs for AI deployments. Dynamo is built in Rust for performance and Python for extensibility, and it integrates with inference engines like vLLM, SGLang, and TensorRT-LLM without replacing them. It includes KV-aware routing, multi-token prediction, and disaggregated prefill/decode, and offers prebuilt recipes for models like Nemotron 3 Ultra.

rss · GitHub Trending - Rust Daily · Jul 8, 01:39

**Background**: Distributed inference serving involves deploying large AI models across multiple GPUs or nodes, requiring coordination for parallel processing and resource management. Traditional frameworks often focus on single-node or simple multi-node setups, but datacenter-scale workloads demand advanced orchestration. Dynamo addresses this by acting as an orchestration layer above existing inference engines.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/v0.8.0/serving/distributed_serving.html">Distributed Inference and Serving — vLLM</a></li>

</ul>
</details>

**Tags**: `#distributed inference`, `#AI infrastructure`, `#Rust`, `#deep learning`, `#serving framework`

---

<a id="item-19"></a>
## [uv: Fast Python Package Manager in Rust](https://github.com/astral-sh/uv) ⭐️ 8.0/10

Astral has released uv, an extremely fast Python package and project manager written in Rust, claiming to be 10-100x faster than pip and capable of replacing multiple tools like pip, poetry, pyenv, and virtualenv. uv significantly improves Python dependency management performance through Rust implementation, potentially reducing developer wait times and improving CI/CD pipelines, while its all-in-one approach simplifies toolchain complexity. uv offers a pip-compatible interface, universal lockfile, script execution with inline dependencies, Python version management, Cargo-style workspaces, and a global cache for disk-space efficiency. It is installable via a standalone script or pip, and supports macOS, Linux, and Windows.

rss · GitHub Trending - Rust Daily · Jul 8, 01:39

**Background**: Python package management has traditionally used pip for installing packages, but performance bottlenecks and fragmented tooling (e.g., poetry for dependency resolution, pyenv for version management) have spurred innovation. Rust is a systems programming language known for performance and safety, making it a popular choice for reimplementing developer tools.

**Tags**: `#Python`, `#Rust`, `#package manager`, `#developer tools`

---

<a id="item-20"></a>
## [Microsoft's windows-rs: Rust bindings for Windows APIs](https://github.com/microsoft/windows-rs) ⭐️ 8.0/10

Microsoft has released windows-rs, a family of Rust crates that provide bindings to Windows APIs, enabling Rust developers to call past, present, and future Windows functionality directly from Rust. This project significantly reduces the friction for Rust developers targeting Windows, making it easier to build systems applications and libraries that leverage native Windows APIs. It strengthens Rust's position in systems programming on Windows. The crate family includes focused crates for error handling, strings, COM/WinRT support, collections, and more, allowing developers to depend only on what they need. The broader windows and windows-sys crates provide access to the entire Windows API surface via per-namespace features.

rss · GitHub Trending - Rust Daily · Jul 8, 01:39

**Background**: In programming, a crate is a Rust package or library. Foreign Function Interface (FFI) allows code in one language to call functions written in another. windows-rs uses FFI to bind Rust to Windows APIs, which are typically exposed as C-style functions. This enables Rust to leverage the vast Windows ecosystem without writing separate C/C++ wrappers.

<details><summary>References</summary>
<ul>
<li><a href="https://doc.rust-lang.org/book/ch07-01-packages-and-crates.html">Packages and Crates - The Rust Programming Language</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foreign_function_interface">Foreign function interface - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#Windows`, `#FFI`, `#Microsoft`, `#Systems Programming`

---

<a id="item-21"></a>
## [Tencent Open-Sources WeKnora: RAG, Agent, Wiki Platform](https://github.com/Tencent/WeKnora) ⭐️ 8.0/10

Tencent has open-sourced WeKnora, a platform that converts raw documents into a queryable RAG system, an autonomous reasoning ReAct agent, and a self-maintaining wiki knowledge base. As an enterprise-grade framework from a major tech company, WeKnora provides a unified, open-source solution for knowledge management that combines retrieval, reasoning, and automatic knowledge base maintenance, potentially reducing the cost and complexity of building custom AI-powered knowledge systems. WeKnora supports ingestion from Feishu, Notion, and Yuque, handles 10+ document formats, integrates 20+ LLM providers, offers multi-tenant RBAC, and can be fully self-hosted.

rss · GitHub Trending - Go Daily · Jul 8, 01:35

**Background**: RAG (Retrieval-Augmented Generation) enhances LLMs by retrieving relevant documents before generating answers. The ReAct pattern (Reasoning + Acting) enables agents to use tools and perform multi-step reasoning. The self-maintaining wiki concept, popularized by Andrej Karpathy, uses LLMs to continually structure and update a knowledge base from raw sources.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent/WeKnora">WeKnora - GitHub</a></li>
<li><a href="https://weknora.online/">WeKnora - LLM-powered Document Understanding & RAG Framework</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#RAG`, `#Open Source`, `#Knowledge Management`, `#AI Platform`

---

<a id="item-22"></a>
## [SOPS: Simple & Flexible Secrets Management Tool](https://github.com/getsops/sops) ⭐️ 8.0/10

SOPS is an open-source editor for encrypted files that supports YAML, JSON, ENV, INI, and binary formats, and integrates with multiple key management systems including AWS KMS, GCP KMS, Azure Key Vault, HuaweiCloud KMS, age, and PGP. SOPS simplifies secret management in DevOps workflows by allowing teams to encrypt secrets directly in configuration files, ensuring security without sacrificing convenience. Its support for multiple backends makes it flexible for diverse cloud environments. SOPS was originally created at Mozilla in 2015 and is now a CNCF Sandbox project. It is licensed under Mozilla Public License Version 2.0 and uses age as a recommended encryption tool.

rss · GitHub Trending - Go Daily · Jul 8, 01:35

**Background**: Secret management is critical in modern application development to avoid storing sensitive information like API keys and passwords in plaintext. SOPS provides a way to encrypt these secrets while keeping them in version control, using key management services from major cloud providers or open-source tools like age and PGP.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/FiloSottile/age">GitHub - FiloSottile/age: A simple, modern and secure ...</a></li>
<li><a href="https://support.huaweicloud.com/intl/en-us/bestpractice-dew/dew_06_0003.html">Overview_Using KMS to Encrypt and Decrypt Data for Cloud ...</a></li>

</ul>
</details>

**Tags**: `#secrets-management`, `#encryption`, `#DevOps`, `#security-tools`

---

<a id="item-23"></a>
## [LocalAI: Open-source AI engine runs models on any hardware, no GPU required](https://github.com/mudler/LocalAI) ⭐️ 8.0/10

LocalAI is an open-source AI engine that enables running various AI models—LLMs, vision, voice, image, video—on any hardware without requiring a GPU. It provides a composable, privacy-first platform with drop-in API compatibility for OpenAI, Anthropic, and ElevenLabs. This project significantly lowers the barrier to running AI models locally, promoting privacy and accessibility for users without high-end hardware. It challenges the reliance on cloud-based AI services and accelerates edge computing adoption. LocalAI uses a modular architecture where backends like llama.cpp, vLLM, and whisper.cpp are pulled on demand, so users only install what they need. It supports multiple hardware platforms including NVIDIA, AMD, Intel, Apple Silicon, Vulkan, and CPU-only, with multi-user authentication and built-in AI agents.

rss · GitHub Trending - Go Daily · Jul 8, 01:35

**Background**: Most AI models require powerful GPUs for efficient inference, making local deployment difficult for many users. Traditional cloud APIs centralize data processing, raising privacy concerns. LocalAI addresses these issues by leveraging optimized inference engines that run on CPUs and various accelerators, enabling private, offline AI usage.

**Tags**: `#AI`, `#open-source`, `#local inference`, `#edge computing`, `#Go`

---

<a id="item-24"></a>
## [Meta developing 'super sensing' glasses with always-on recording](https://www.ithome.com/0/974/288.htm) ⭐️ 8.0/10

Meta is developing a prototype AI smart glasses internally called 'super sensing' that can continuously record audio and automatically take photos every few seconds, without lighting the LED recording indicator. This raises significant privacy concerns as bystanders may not know they are being recorded. It represents a step towards always-on wearable AI but could face regulatory and public backlash. The LED indicator would remain off during AI functions, only lighting for active photo/video saving. Meta also discusses not storing raw data but extracting metadata for AI queries to reduce privacy risks.

rss · IT之家 · Jul 8, 23:36

**Background**: Meta already sells Ray-Ban Meta smart glasses with camera and audio capabilities. Previous privacy issues include facial recognition code discovery and third-party LED removal services, highlighting ongoing concerns about covert recording.

**Tags**: `#smart glasses`, `#AI`, `#privacy`, `#Meta`, `#wearable tech`

---

<a id="item-25"></a>
## [SpaceXAI Launches Grok 4.5: Programming AI Co-Trained with Cursor](https://www.ithome.com/0/974/278.htm) ⭐️ 8.0/10

SpaceXAI has released Grok 4.5, its first programming-focused AI model, co-trained with the AI code editor Cursor. The model claims to double efficiency and halve costs compared to leading competitors. This development could significantly reduce the cost and time required for software engineering tasks, making advanced AI-assisted coding more accessible. It also highlights the trend of specialized AI models for agentic programming tasks. Grok 4.5 was trained on tens of thousands of NVIDIA GB300 GPUs, achieves 80 tokens per second output, and uses half the tokens per task compared to similar models. Pricing is set at $2 per million input tokens and $6 per million output tokens.

rss · IT之家 · Jul 8, 22:51

**Background**: Cursor is an AI-native code editor that uses natural language to generate, edit, and debug code. NVIDIA GB300 is a high-performance GPU designed for AI training and inference. Agent tasks in programming AI involve multi-step software engineering using various tools and skills.

<details><summary>References</summary>
<ul>
<li><a href="https://builtin.com/articles/what-is-cursor-ai">What Is Cursor? AI Code Editor Explained | Built In</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/gb300-nvl72/">NVIDIA GB300 NVL72</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_agent">AI agent - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Large Language Models`, `#Code Generation`, `#Software Engineering`, `#Grok`

---

<a id="item-26"></a>
## [Anthropic to Surpass $1B Profit, Secretly Files for IPO](https://www.ithome.com/0/974/275.htm) ⭐️ 8.0/10

SemiAnalysis reports that Anthropic is projected to exceed $1 billion in profit in Q3 2026 and secretly filed for IPO on June 1, 2026. This marks a major milestone for AI labs, as Anthropic's profitability and IPO could force OpenAI to disclose its finances and accelerate capital raising for AI infrastructure. The combined ARR of Anthropic and OpenAI has reached nearly $100 billion, with Anthropic's Claude Code driving strong B2B growth. SemiAnalysis estimates a potential $6 trillion market cap if execution continues.

rss · IT之家 · Jul 8, 22:30

**Background**: SemiAnalysis is an independent research firm specializing in AI and semiconductors. Their Tokenomics model analyzes AI economics by SKU and customer tier. Anthropic is an AI company founded by former OpenAI employees, focused on safe AI development.

<details><summary>References</summary>
<ul>
<li><a href="https://semianalysis.com/about/">About – SemiAnalysis</a></li>
<li><a href="https://finance.biggo.com/news/KPbYnp0BvthpMgHBApty">29-Year-Old Founder Builds AI Research Empire SemiAnalysis ...</a></li>
<li><a href="https://www.cloudzero.com/blog/claude-code-pricing/">Claude Code Pricing In 2026: Plans, Token Costs, And Costs</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#financial performance`, `#Claude Code`

---

<a id="item-27"></a>
## [Sony faces €4B class-action over physical disc phase-out](https://www.ithome.com/0/974/246.htm) ⭐️ 8.0/10

A Dutch consumer organization, Stichting Massaschade & Consument, has filed a class-action lawsuit against Sony for over €400 million, representing 1.7 million Dutch players, over Sony's announced plan to stop producing physical game discs by 2028. This lawsuit challenges Sony's move toward a digital-only future, alleging monopolistic control over game pricing and ownership, which could set a precedent for digital distribution practices and consumer rights across the gaming industry. The lawsuit argues that without physical discs, Sony would have monopoly power over first-party game pricing and ownership, since digital games are only licenses, not actual ownership. This is Sony's second legal battle over digital market dominance, following an $8 million settlement in California two months ago.

rss · IT之家 · Jul 8, 13:17

**Background**: Physical game discs allow players to buy, sell, and trade used games, fostering a competitive secondary market. Digital-only distribution removes this option, locking players into the platform holder's store and pricing. Consumer groups argue this limits freedom and could lead to higher prices, as seen in other digital marketplaces.

**Tags**: `#Sony`, `#lawsuit`, `#digital-only`, `#gaming`, `#consumer rights`

---

<a id="item-28"></a>
## [Cloudflare and OpenAI Pilot Using Network Signals for AI Search](https://www.ithome.com/0/974/235.htm) ⭐️ 8.0/10

Cloudflare and OpenAI have launched a research pilot where Cloudflare shares real-time network signals—such as content freshness, traffic quality, and page changes—from its network covering over 20% of global web traffic, aiming to improve AI search indexing and answer accuracy. This partnership leverages unique real-world web data from Cloudflare's global network to address key challenges in AI search, such as timeliness and content quality, potentially leading to more accurate and up-to-date answers for users. It could also set a precedent for how internet infrastructure companies collaborate with AI firms. The pilot focuses on signal-driven crawling and indexing techniques, using Cloudflare's visibility into page changes and traffic patterns to guide OpenAI's search index. OpenAI contributes its advanced models, large-scale search systems, and real user query data for testing.

rss · IT之家 · Jul 8, 12:39

**Background**: AI search engines rely on crawling the web to index content for answering queries. Traditional crawling may miss timely updates or prioritize low-quality content. Signal-driven crawling uses network-level indicators like content freshness and traffic quality to guide indexing, potentially leading to more accurate and up-to-date AI responses. Cloudflare's network, handling over 20% of global internet traffic, provides a unique vantage point for such signals.

<details><summary>References</summary>
<ul>
<li><a href="https://rallies.ai/news/cloudflare-launches-openai-pilot-using-signals-from-20-of-web-traffic">Cloudflare Launches OpenAI Pilot Using Signals from 20% of ...</a></li>
<li><a href="https://seekingalpha.com/news/4612227-cloudflare-openai-team-up-to-launch-research-pilot-for-ai-search-indexing">Cloudflare, OpenAI launch research pilot for AI search indexing</a></li>

</ul>
</details>

**Tags**: `#Cloudflare`, `#OpenAI`, `#AI search`, `#network insights`, `#indexing`

---

<a id="item-29"></a>
## [LingBot-Video: 13B Sparse MoE Video Diffusion World Model Open-Sourced](https://www.reddit.com/r/MachineLearning/comments/1ur0bxq/lingbotvideo_sparsemoe_video_diffusion/) ⭐️ 8.0/10

LingBot-Video is a 13 billion parameter sparse Mixture-of-Experts (MoE) video diffusion transformer, with only 1.4B active parameters, post-trained using reinforcement learning with six rewards including physical plausibility, and released as an open-source action-conditioned world model for robotics. This model pushes the boundary between video generation and world modeling by using RL with a VLM-judged physics reward, and its open-source release enables broader research into scalable, physically-plausible video prediction for robotics and simulation. The model uses a single-stream diffusion transformer with DeepSeek-V3-style sparse MoE (128 experts, top-8 routing, 1.4B active out of 13B total), and includes an action-to-video mode that predicts robot rollouts from action and hand-pose conditions, with code and weights available on GitHub and Hugging Face.

reddit · r/MachineLearning · /u/Savings-Display5123 · Jul 8, 17:58

**Background**: Sparse Mixture-of-Experts (MoE) is a neural network architecture where only a subset of parameters (experts) is activated per input, enabling large total capacity with lower computational cost. DeepSeek-V3 popularized this approach with 671B total parameters and 37B active per token. Video diffusion transformers generate videos by iteratively denoising random noise conditioned on text or other inputs. Reinforcement learning (RL) post-training optimizes models for specific rewards; here, a Vision-Language Model (VLM) grades physical plausibility. World models aim to simulate environment dynamics for planning, distinct from text-to-video generation which only produces plausible videos without interactive control.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2412.19437">[2412.19437] DeepSeek-V3 Technical Report - arXiv.org GitHub - deepseek-ai/DeepSeek-V3 Model Architecture Overview | deepseek-ai/DeepSeek-V3 | DeepWiki deepseek-ai/DeepSeek-V3.2 · Hugging Face GitHub - RushilJ2603/DeepSeek-V3-Sparse-MoE-Architecture ...</a></li>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance ...</a></li>
<li><a href="https://arxiv.org/abs/2505.02018">[2505.02018] R-Bench: Graduate-level Multi-disciplinary ... RBench: Graduate-level Multi-disciplinary Benchmarks for LLM ... [2505.16770] RBench-V: A Primary Assessment for Visual ... README.md · R-Bench/R-Bench at main - Hugging Face R-Bench/R-Bench-V · Datasets at Hugging Face GitHub - rbenchmark/benchmarks: Collections of Benchmarks of ... RBench-V: A Primary Assessment for Visual Reasoning Models ...</a></li>

</ul>
</details>

**Discussion**: The post author invites critical discussion, questioning whether a VLM is a defensible physics judge (risk of reward hacking) and where the line lies between video generation and world modeling, as the model lacks closed-loop robot results despite achieving top average on RBench.

**Tags**: `#sparse MoE`, `#video diffusion`, `#world model`, `#reinforcement learning`, `#robotics`

---

<a id="item-30"></a>
## [DeepSeek Develops Own AI Inference Chip to Reduce Supplier Reliance](https://t.me/zaihuapd/42423) ⭐️ 8.0/10

DeepSeek, a Chinese AI company, has begun developing its own AI inference chip, aiming to reduce dependence on Nvidia and Huawei for chip supply, according to three sources. The project started about a year ago and is still in early stages, with the company recruiting chip design engineers. This move could reshape the AI chip supply chain amid US export restrictions, potentially giving DeepSeek greater control over its inference costs and hardware roadmap. If successful, it may inspire other Chinese AI firms to pursue self-developed chips, accelerating the trend toward homegrown semiconductor solutions in China. The chip is focused on inference—the phase where trained models generate responses for users—rather than training. DeepSeek has begun contacting chip design, foundry, and memory companies, and has been privately recruiting chip design engineers in recent months.

telegram · zaihuapd · Jul 8, 05:20

**Background**: DeepSeek previously relied on Nvidia H800 and Huawei Ascend chips, but US export controls have restricted access to advanced Nvidia GPUs. AI inference chips, unlike training chips, optimize for cost-per-token, latency, and power efficiency, making them attractive for large-scale deployment. The market for inference chips is expected to grow significantly, reaching 60-70% of the AI accelerator market by 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://www.granitefirm.com/blog/us/2025/08/24/ai-inference-chips/">AI inference chips vs. training chips - Andy Lin's Long-term ...</a></li>
<li><a href="https://www.naddod.com/ai-insights/inference-chip-guide-the-foundation-of-scalable-ai-applications">Inference Chip Guide: The Foundation of Scalable AI ...</a></li>
<li><a href="https://www.techpowerup.com/gpu-specs/h800-pcie-80-gb.c4181">NVIDIA H800 PCIe 80 GB Specs | TechPowerUp GPU Database</a></li>

</ul>
</details>

**Tags**: `#AI`, `#semiconductor`, `#DeepSeek`, `#chip design`, `#geopolitics`

---

<a id="item-31"></a>
## [Alibaba Bans Employees from Using Claude](https://t.me/zaihuapd/42424) ⭐️ 8.0/10

Alibaba has ordered all employees to uninstall Anthropic's Claude and related products, including Sonnet, Opus, Fable models and Claude Code, effective July 10, 2026. This marks a major escalation in AI corporate tensions, as a top Chinese tech firm bans a leading US AI model over alleged account abuse, highlighting growing security and competitive pressures in the AI industry. The ban follows Anthropic's accusation that Alibaba used about 25,000 fake accounts to interact with Claude over 28 million times between April 22 and June 5, 2026, leading to tightened security measures.

telegram · zaihuapd · Jul 8, 06:09

**Background**: Claude is a family of large language models developed by Anthropic, a US AI company, with models like Sonnet, Opus, and Fable offering varying capabilities. Model distillation is a technique where a smaller model learns from a larger one, often using large volumes of queries. Alibaba had previously reimbursed employees for using external AI models like Claude, GPT, and Gemini, but this policy has now been reversed.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/jonmarkman/2026/06/26/anthropic-says-alibaba-used-25000-fake-accounts-to-distill-claude/">Anthropic Says Alibaba Used 25,000 Fake Accounts To Distill ...</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/overview">Models overview - Claude Platform Docs</a></li>
<li><a href="https://code.claude.com/docs/en/sub-agents">Create custom subagents - Claude Code Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Alibaba`, `#Claude`, `#Anthropic`, `#Ban`

---

<a id="item-32"></a>
## [Android Remote Root Exploit 'IonStack' Threatens All Versions](https://www.coolapk.com/feed/72700258?s=ZGQ2MTVlZjYxMDYyNTM3ZzZhNGUzOThjega1640) ⭐️ 8.0/10

Security researchers at Nebula Security have disclosed 'IonStack', the first public proof-of-concept exploit chain that grants full remote root access to Android devices up to version 17 by clicking a single malicious URL. This exploit chain demonstrates a critical remote code execution path that bypasses Android's sandbox and achieves persistent root access, affecting billions of devices and posing an immediate security threat. The chain combines a Mozilla Firefox browser vulnerability (affecting version 151.0.2 and earlier) with a 15-year-old Linux kernel bug, and after exploitation, attackers gain persistent root access via ADB. The Linux kernel has been patched, but full exploit details are withheld to give vendors time to respond.

telegram · zaihuapd · Jul 8, 13:01

**Background**: Android devices typically run on a Linux kernel, and system security relies on sandboxing via SELinux and application isolation. Root access gives full control over the device, which standard Android does not allow without unlocking the bootloader. This exploit chain achieves root without user interaction beyond clicking a link, representing a severe escalation.

<details><summary>References</summary>
<ul>
<li><a href="https://cybersecuritynews.com/android-17-root-1-click/">First-Ever 1- Click Android 17 Exploit Allows Attackers to ...</a></li>
<li><a href="https://cyberpress.org/ionstack-attack-full-control-android/">IonStack Attack Lets Hackers Gain Full Control of Android ...</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Security`, `#Vulnerability`, `#Root`, `#Linux kernel`

---

<a id="item-33"></a>
## [Smartphone apps identified via leaked EM signals with 99% accuracy](https://www.scmp.com/news/china/science/article/3359688/chinese-researchers-find-peephole-any-smartphone-its-leaked-radio-signal) ⭐️ 8.0/10

Researchers from People's Public Security University of China have developed a non-contact forensic technique that identifies smartphone applications by analyzing leaked low-frequency electromagnetic signals, achieving up to 99.07% accuracy on iPhone 15 Pro, Xiaomi 15 Pro, and OPPO Reno 13. This technique poses significant privacy and security risks as it works even when the device is offline, in airplane mode, encrypted, or locked, potentially enabling covert surveillance or forensic evidence gathering without physical access. The method analyzes electromagnetic emissions in the low-frequency band, requires no access to the device's operating system or stored data, and can distinguish specific operations within apps (e.g., WeChat video call, Douyin browsing). The study was published on May 22, 2026 in the peer-reviewed journal Radio Engineering.

telegram · zaihuapd · Jul 8, 16:05

**Background**: Side-channel attacks exploit physical emissions such as electromagnetic radiation, power consumption, or timing to extract sensitive information from electronic devices. Electromagnetic (EM) side-channel attacks are non-invasive and can be performed remotely using probes and oscilloscopes. This research extends EM attacks to identify running applications on smartphones by matching unique EM signatures of each app or operation.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ckhq.net/html/6c1af61946e47994a7d682373d5f7757.html">中国科研团队研发非接触式智能手机应用识别技术，准确率达99.07%</a></li>
<li><a href="https://www.msn.cn/zh-cn/技术/硬件和设备/手机关机也没用-中国科学家发现新型电磁-透视术-让隐私无处遁形/ar-AA27u7GB">手机关机也没用？中国科学家发现新型电磁“透视术”让隐私无处遁形</a></li>

</ul>
</details>

**Tags**: `#security`, `#privacy`, `#electromagnetic emissions`, `#smartphone`, `#research`

---