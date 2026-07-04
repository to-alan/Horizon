---
layout: default
title: "Horizon Summary: 2026-07-04 (EN)"
date: 2026-07-04
lang: en
---

> From 322 items, 33 important content pieces were selected

---

1. [ZLUDA: Run CUDA Apps on Non-NVIDIA GPUs with Near-Native Performance](#item-1) ⭐️ 9.0/10
2. [First Fully Autonomous AI Agent Ransomware Attack Discovered](#item-2) ⭐️ 9.0/10
3. [Unisplendour Titan-3: China's first billion-gate FPGA with FinFET](#item-3) ⭐️ 9.0/10
4. [CDD recovers finetuning data from LLM logits alone](#item-4) ⭐️ 9.0/10
5. [European Parliament Spyware Investigator Hacked with Pegasus](#item-5) ⭐️ 8.0/10
6. [Local SOTA LLM Guide Highlights High Costs and Limitations](#item-6) ⭐️ 8.0/10
7. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-7) ⭐️ 8.0/10
8. [Superpowers: A New Methodology for Coding Agents](#item-8) ⭐️ 8.0/10
9. [Chrome DevTools MCP Server Enables AI Agents to Control Browsers](#item-9) ⭐️ 8.0/10
10. [openai/codex-plugin-cc](#item-10) ⭐️ 8.0/10
11. [Hugging Face Transformers: Leading Open-Source ML Library](#item-11) ⭐️ 8.0/10
12. [Anthropic Launches Claude Code: Agentic Coding Tool in Terminal](#item-12) ⭐️ 8.0/10
13. [Meta Open Sources Astryx Design System with 150+ Components](#item-13) ⭐️ 8.0/10
14. [Microsoft Launches 'Skills' Repository for Grounded AI Coding Agents](#item-14) ⭐️ 8.0/10
15. [MCP Apps Protocol Enables Interactive UIs in AI Chatbots](#item-15) ⭐️ 8.0/10
16. [uv: A Rust-Powered, Ultra-Fast Python Package Manager](#item-16) ⭐️ 8.0/10
17. [Tree-sitter: Incremental Parsing Library for Programming Tools](#item-17) ⭐️ 8.0/10
18. [Rolldown: New Rust-based JS/TS Bundler with Rollup API](#item-18) ⭐️ 8.0/10
19. [Helix: A Post-Modern Modal Text Editor in Rust](#item-19) ⭐️ 8.0/10
20. [ttl: A Modern Rust-Based Traceroute Alternative](#item-20) ⭐️ 8.0/10
21. [wgpu: Safe, Cross-Platform Rust Graphics API](#item-21) ⭐️ 8.0/10
22. [FFF: Fast File Search SDK for AI Agents and Developers](#item-22) ⭐️ 8.0/10
23. [Ollama: Run Open-Source LLMs Locally](#item-23) ⭐️ 8.0/10
24. [Bridgewater Study: Frontier AI Models Fail 80% Financial Accuracy Threshold](#item-24) ⭐️ 8.0/10
25. [Vidu S1: Real-Time Video Chat with Voice Control via Autoregressive Diffusion](#item-25) ⭐️ 8.0/10
26. [JD Logistics Launches China's First L4 Autonomous Heavy Truck Demo](#item-26) ⭐️ 8.0/10
27. [Alibaba Bans All Anthropic Products After Hidden Backdoor Found](#item-27) ⭐️ 8.0/10
28. [Baidu's AI chip unit Kunlun Chip targets $50B Hong Kong IPO](#item-28) ⭐️ 8.0/10
29. [Huawei Mate 80 Pro gaming efficiency surpasses Snapdragon 8 Gen3](#item-29) ⭐️ 8.0/10
30. [Native low-rank factorization improves transformer training efficiency](#item-30) ⭐️ 8.0/10
31. [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](#item-31) ⭐️ 8.0/10
32. [NASA Launches LINK Spacecraft to Rescue Swift Telescope](#item-32) ⭐️ 8.0/10
33. [Tencent Xuanwu Lab's Atuin AI surpasses Mythos in CyberGym test](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ZLUDA: Run CUDA Apps on Non-NVIDIA GPUs with Near-Native Performance](https://github.com/vosen/ZLUDA) ⭐️ 9.0/10

ZLUDA is an open-source drop-in replacement for NVIDIA's CUDA that allows unmodified CUDA applications to run on AMD and Intel GPUs with near-native performance. The project is written in Rust and targets primarily AMD GPUs through ROCm, with historical support for Intel GPUs. ZLUDA breaks NVIDIA's hardware lock-in for CUDA, enabling GPU computing and AI/ML workloads to run on cheaper or more available non-NVIDIA hardware. This could democratize access to GPU computing and reduce vendor dependency. ZLUDA achieves near-native performance by translating CUDA kernels to AMD's ROCm or Intel's oneAPI at runtime. It is licensed under the MIT license and available on GitHub, with active development and community support on Discord.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: CUDA is NVIDIA's parallel computing platform and programming model, widely used in AI, machine learning, and scientific computing. It is proprietary and only runs on NVIDIA GPUs, creating vendor lock-in. ZLUDA is a reverse-engineered compatibility layer that translates CUDA instructions to AMD or Intel GPU instructions, allowing applications written for CUDA to work on non-NVIDIA hardware without modification.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/ZLUDA">ZLUDA</a></li>

</ul>
</details>

**Tags**: `#CUDA`, `#GPU`, `#ZLUDA`, `#open-source`, `#Rust`

---

<a id="item-2"></a>
## [First Fully Autonomous AI Agent Ransomware Attack Discovered](https://www.ithome.com/0/972/424.htm) ⭐️ 9.0/10

Security firm Sysdig has documented the first-ever fully autonomous ransomware attack carried out by an AI agent, named JADEPUFFER, which exploited a known Langflow vulnerability (CVE-2025-3248) to complete the entire attack chain without human intervention. This event marks a paradigm shift in cybersecurity, demonstrating that AI agents can autonomously orchestrate multi-step attacks, lowering the technical barrier for ransomware deployment and forcing defenders to rethink detection and response strategies. JADEPUFFER executed over 600 attack payloads, autonomously recovered from failures within 31 seconds, and encrypted 1,342 configuration records in Nacos using MySQL's AES_ENCRYPT() function, but failed to store the encryption key, making ransom impossible.

rss · IT之家 · Jul 3, 11:57

**Background**: Langflow is an open-source workflow tool for building AI agent pipelines. CVE-2025-3248 is a critical remote code execution vulnerability in Langflow versions before 1.3.0, allowing unauthenticated attackers to execute arbitrary Python code. AI agents are software entities that can autonomously plan and execute tasks using large language models and external tools. This attack demonstrates how an AI agent can chain together multiple known vulnerabilities and misconfigurations (like default MinIO credentials) to achieve a full compromise.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/horizon3ai_unsafe-at-any-speed-abusing-python-exec-activity-7315844970278539264-yK3v">CVE - 2025 - 3248 : Langflow vulnerability found by Horizon3.ai | LinkedIn</a></li>
<li><a href="https://wiki.archlinux.org/title/MinIO">MinIO - ArchWiki</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#ransomware`, `#cybersecurity`, `#autonomous attack`, `#vulnerability exploitation`

---

<a id="item-3"></a>
## [Unisplendour Titan-3: China's first billion-gate FPGA with FinFET](https://www.ithome.com/0/972/407.htm) ⭐️ 9.0/10

Unisplendour Information Technology (紫光同创) announced the Titan-3 series, China's first domestically developed billion-gate high-end FPGA fabricated using FinFET process, at the 2026 Munich Shanghai Electronics Show. This breakthrough fills a critical gap in China's high-performance programmable chip supply, reducing reliance on foreign FPGA vendors and enabling domestic applications in communications, data centers, AI, and aerospace. The Titan-3 series includes models PG3T1300 and PG3T1500, supporting on-chip large-capacity HRM+DRM architecture, high-speed DDR4 memory interfaces, multi-rate EMAC hard cores, PCIe Gen4, and high-speed SerDes interfaces. A companion PG3T1300 accelerator card with 4x25G optical ports and PCIe 4.0 x8 was also unveiled.

rss · IT之家 · Jul 3, 10:48

**Background**: FPGA (Field Programmable Gate Array) is a programmable logic chip widely used in telecom, data centers, video processing, and aerospace. FinFET (Fin Field-Effect Transistor) is an advanced transistor technology that improves performance and power efficiency. China has been striving for self-sufficiency in semiconductors, and high-end FPGAs were a notable weakness in the domestic supply chain.

<details><summary>References</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/electronics-engineering/high-speed-serdes-serializer-deserializer-interfaces/">High - Speed SerDes (Serializer-Deserializer) Interfaces</a></li>
<li><a href="https://www.youtube.com/watch?v=gUsHwi4M4xE">EEVblog #496 - What Is An FPGA ? - YouTube</a></li>

</ul>
</details>

**Tags**: `#FPGA`, `#semiconductor`, `#China technology`, `#FinFET`, `#hardware`

---

<a id="item-4"></a>
## [CDD recovers finetuning data from LLM logits alone](https://www.reddit.com/r/MachineLearning/comments/1umn2dk/contrastive_decoding_diffing_cdd_recovering/) ⭐️ 9.0/10

Contrastive Decoding Diffing (CDD) is a novel method that recovers verbatim finetuning data from large language models using only logit access, without needing model weights or activation values. This advances AI safety and interpretability by enabling white-box-level model diffing with only grey-box access, outperforming previous white-box methods like Activation Difference Lens. CDD achieves a verbatim recovery score of 4+/5 on 19 out of 20 organism x model pairs across four model families (1B to 32B parameters), while ADL never exceeds 3/5 despite requiring full weight access.

reddit · r/MachineLearning · /u/CebulkaZapiekana · Jul 3, 19:01

**Background**: Model diffing aims to identify changes in a model after fine-tuning. Contrastive decoding is a technique that compares logits from two models to improve generation. CDD applies contrastive decoding between a base and fine-tuned model to extract fine-tuning data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2210.15097">[2210.15097] Contrastive Decoding: Open-ended Text Generation as Optimization</a></li>
<li><a href="https://www.lesswrong.com/w/model-diffing">Model Diffing — LessWrong</a></li>
<li><a href="https://www.emergentmind.com/topics/contrastive-decoding">Contrastive Decoding in Language Models</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#LLMs`, `#interpretability`, `#AI safety`, `#finetuning`

---

<a id="item-5"></a>
## [European Parliament Spyware Investigator Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

A member of the European Parliament's committee investigating spyware was hacked with Pegasus spyware, as confirmed by Citizen Lab forensic analysis. The infections occurred in October 2022 and March 2023. This incident underscores the brazenness of state-sponsored espionage targeting the very institutions tasked with investigating spyware abuse. It threatens democratic oversight and the integrity of European parliamentary processes. The first infection overlapped with a known Pegasus campaign targeting Russian and Belarusian-speaking exiled journalists in Europe, suggesting a Pegasus customer with authorization to spy across multiple EU countries. The phone also contained both personal medical and confidential government documents.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is spyware developed by the Israeli company NSO Group, marketed for counterterrorism but frequently used by governments to surveil journalists, activists, and opposition figures. Citizen Lab is a cybersecurity research group at the University of Toronto that has extensively documented Pegasus infections. The European Parliament has been investigating the use of spyware including Pegasus within the EU.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_Project_(investigation)">Pegasus Project (investigation) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted the broader Pegasus scandal in Greece, with evidence suggesting orchestration by the prime minister's office. Some argued that the attack should be seen as an attack by EU member states rather than an external attack on the European Parliament, highlighting the complicity of governments that abused Pegasus.

**Tags**: `#cybersecurity`, `#Pegasus`, `#espionage`, `#European Parliament`, `#spyware`

---

<a id="item-6"></a>
## [Local SOTA LLM Guide Highlights High Costs and Limitations](https://github.com/jamesob/local-llm) ⭐️ 8.0/10

Jamesob published a guide on GitHub detailing how to run state-of-the-art LLMs locally, but community comments highlight that the recommended setup costs $40,000–$55,000 and involves significant quality compromises through quantization and expert pruning. This guide and its community discussion underscore that running top-tier LLMs locally remains prohibitively expensive for most individuals and often yields lower quality than cloud services, contradicting the common perception that local deployment is more cost-effective. The guide recommends a build with 4 GPUs costing $12,000 each, totaling over $50,000, and uses a REAP-pruned, Int8-mix NVFP4 quantized version of GLM-5.2 with about 594B parameters. A more affordable option mentioned is using two RTX 3090s for 48GB VRAM to run Qwen3.6-27B.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: SOTA (state-of-the-art) in AI refers to the currently best-performing models on specific benchmarks. Local LLM inference involves running large language models on personal hardware rather than relying on cloud APIs, which requires substantial GPU memory and processing power. The guide aims to help users achieve near-cloud-quality inference at home, but the hardware demands are extremely high for top-tier models.

<details><summary>References</summary>
<ul>
<li><a href="https://maddevs.io/glossary/state-of-the-art-models/">What Is SOTA in AI? State-of-the-Art Models | Machine Learning Glossary</a></li>
<li><a href="https://grokipedia.com/page/Pre-built_PCs_for_Local_LLM_Inference">Pre-built PCs for Local LLM Inference</a></li>

</ul>
</details>

**Discussion**: Community commenters express significant skepticism about the practicality of the guide's high-end build, noting that the cost ($40k–$55k) could cover years of cloud subscriptions. Others highlight that pruned and quantized models often degrade in quality, and there are security concerns about backdoored models. A few suggest more affordable alternatives like 128GB unified memory setups or dual RTX 3090s.

**Tags**: `#LLM`, `#local inference`, `#hardware`, `#cost analysis`, `#community discussion`

---

<a id="item-7"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Wordgard is a new in-browser rich-text editor system created by Marijn Haverbeke, the author of ProseMirror. It offers a semantic approach to content editing with precise control over document structure. This release is significant because it comes from the creator of ProseMirror, a widely-used editor framework, and introduces a different architecture that may influence future editor development. Developers building custom editors now have a new option that promises better type safety and simpler API design. Wordgard is not a free-form HTML editor but focuses on semantic content types, similar to ProseMirror but with significant conceptual differences. There is no direct upgrade path from ProseMirror, so migration would require substantial rework.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a battle-tested open-source rich-text editor framework known for its flexibility and performance. It has a steep learning curve and is used as the foundation for many editors like Tiptap. Wordgard was announced by its creator as a new system that shares some concepts but aims to address limitations like type safety and API complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://wordgard.net/">Wordgard</a></li>
<li><a href="https://code.haverbeke.berlin/wordgard/wordgard">wordgard / wordgard : The Wordgard rich text editor</a></li>
<li><a href="https://news.ycombinator.com/item?id=48772573">Wordgard : The new in-browser rich - text editor from... | Hacker News</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion includes questions about the rationale for creating a new editor, with some users noting the lack of an upgrade path and potential instability on mobile. Others praise the design and the validation of seeing similarities with their own custom solutions, while some express frustration over the lack of a web standard for rich-text editing.

**Tags**: `#rich-text editor`, `#web development`, `#prosemirror`, `#javascript`, `#open source`

---

<a id="item-8"></a>
## [Superpowers: A New Methodology for Coding Agents](https://github.com/obra/superpowers) ⭐️ 8.0/10

A GitHub repository called 'obra/superpowers' introduces a complete software development methodology and agentic skills framework for coding agents, emphasizing design-first, subagent-driven development. This framework could standardize how AI agents assist in software development, potentially improving code quality and reducing manual oversight. Its composable skills approach may accelerate adoption of AI-assisted coding in enterprises. Superpowers supports multiple harnesses including Claude Code, Antigravity, Codex, and Cursor, and is available as a plugin in Anthropic's official marketplace. It automates tasks like spec elicitation, plan creation, and subagent task execution.

rss · GitHub Trending - Daily · Jul 3, 01:32

**Background**: Coding agents are AI tools that can autonomously write, edit, and debug code based on natural language instructions. Examples include Claude Code by Anthropic, Antigravity by Google, and Codex by OpenAI. These agents typically assist developers but often require careful prompt engineering to avoid errors.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview">Claude Code overview - Anthropic</a></li>
<li><a href="https://antigravity.google/?ref=producthunt">Google Antigravity - Build the new way</a></li>
<li><a href="https://en.wikipedia.org/wiki/Codex_(AI_agent)">Codex (AI agent) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#software development methodology`, `#agentic framework`, `#coding agents`

---

<a id="item-9"></a>
## [Chrome DevTools MCP Server Enables AI Agents to Control Browsers](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

The Chrome DevTools team released 'chrome-devtools-mcp', an MCP server that allows AI coding assistants like Claude, Cursor, and Copilot to control and inspect a live Chrome browser for automation and debugging. This official tool bridges Chrome DevTools and AI coding agents via the Model Context Protocol, enabling reliable automation, in-depth debugging, and performance analysis directly from AI assistants, which could significantly improve developer productivity. The tool uses Puppeteer for browser automation and Chrome DevTools for performance tracing; it collects usage statistics by default but allows opt-out via a flag, and performance tools may send trace URLs to the Google CrUX API unless disabled.

rss · GitHub Trending - Daily · Jul 3, 01:32

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 that standardizes how AI applications connect to external tools and data sources. MCP acts like a 'USB-C port' for AI apps, allowing them to interact with various systems through a unified interface.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://docs.anthropic.com/en/docs/mcp">Model Context Protocol ( MCP ) - Anthropic</a></li>

</ul>
</details>

**Tags**: `#Chrome DevTools`, `#MCP`, `#AI coding agents`, `#automation`, `#debugging`

---

<a id="item-10"></a>
## [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) ⭐️ 8.0/10

A plugin to integrate OpenAI Codex's code review and task delegation capabilities into Claude Code.

rss · GitHub Trending - Daily · Jul 3, 01:32

**Tags**: `#AI`, `#code review`, `#plugin`, `#developer tools`, `#OpenAI`

---

<a id="item-11"></a>
## [Hugging Face Transformers: Leading Open-Source ML Library](https://github.com/huggingface/transformers) ⭐️ 8.0/10

Hugging Face Transformers is a state-of-the-art open-source library for training and inference across text, vision, audio, and multimodal tasks, hosting over 100,000 pretrained models on the Hugging Face Hub. It has become the de facto standard for applying transformer models in both research and industry, significantly lowering the barrier to using cutting-edge AI. Its widespread adoption accelerates innovation across NLP, computer vision, speech processing, and multimodal AI. The library supports over 100,000 pretrained model checkpoints and integrates seamlessly with other Hugging Face tools like Datasets and Spaces. It provides a unified API for PyTorch, TensorFlow, and JAX, enabling flexible training and inference.

rss · GitHub Trending - Python Daily · Jul 3, 01:38

**Background**: Transformer architecture, introduced in the 2017 paper 'Attention Is All You Need,' replaced recurrent neural networks by using self-attention mechanisms to process sequences in parallel. This architecture has become foundational to modern AI, powering models like GPT, BERT, and ViT. Hugging Face Transformers provides a user-friendly interface to easily load, fine-tune, and deploy these models.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@raiyanmd17357/transformer-architecture-in-machine-learning-800b4691264b">“ Transformer Architecture in Machine Learning ” | Medium</a></li>
<li><a href="https://introml.mit.edu/notes/transformers.html">9 Transformers – 6.390 - Intro to Machine Learning</a></li>
<li><a href="https://medium.com/@jude.ananth/advancements-in-multimodal-machine-learning-the-future-of-ai-3552c7f19888">Advancements in Multimodal Machine Learning : The... | Medium</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#NLP`, `#transformers`, `#deep learning`, `#open source`

---

<a id="item-12"></a>
## [Anthropic Launches Claude Code: Agentic Coding Tool in Terminal](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic has released Claude Code, an agentic coding tool that operates directly in the terminal, allowing developers to execute tasks, explain code, and manage git workflows using natural language commands. This release marks a significant step in integrating large language models into developer workflows, potentially boosting productivity by automating routine coding tasks. It positions Anthropic as a key player in the emerging agentic AI coding assistant space. Claude Code supports multiple installation methods including curl, Homebrew, and Winget, while the npm package is deprecated. It offers plugins for extended functionality and collects usage data for improvement, with privacy safeguards in place.

rss · GitHub Trending - Python Daily · Jul 3, 01:38

**Background**: Claude is a series of large language models developed by Anthropic, trained using constitutional AI for improved ethical compliance. Agentic AI refers to systems that can autonomously pursue goals and use tools, and Claude Code exemplifies this by operating within a terminal environment to assist with coding tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_(AI)">Claude (AI) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI coding assistant`, `#developer tools`, `#Claude`, `#agentic`, `#natural language programming`

---

<a id="item-13"></a>
## [Meta Open Sources Astryx Design System with 150+ Components](https://github.com/facebook/astryx) ⭐️ 8.0/10

Meta has open sourced Astryx, a fully customizable design system for React applications that includes over 150 accessible components, brand-level theming, dark mode, a CLI, and AI-ready tooling. As Meta's most-used internal design system powering 13,000+ apps, Astryx offers a mature, production-tested foundation that can significantly boost developer productivity and consistency across React projects, while its agent-ready design aligns with the growing trend of AI-assisted development. Astryx is built on React and Meta's own StyleX CSS-in-JS library but allows developers to override styles with any CSS solution via className. It features a swizzling mechanism to eject full component source code for deep customization.

rss · GitHub Trending - TypeScript Daily · Jul 3, 01:40

**Background**: A design system is a collection of reusable UI components, guidelines, and tools that help teams build consistent user interfaces efficiently. Astryx was developed internally at Meta over eight years and is now open source under an MIT license, leveraging StyleX for compile-time CSS optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/stylex">Stylex</a></li>

</ul>
</details>

**Tags**: `#design-system`, `#react`, `#open-source`, `#meta`, `#ui-components`

---

<a id="item-14"></a>
## [Microsoft Launches 'Skills' Repository for Grounded AI Coding Agents](https://github.com/microsoft/skills) ⭐️ 8.0/10

Microsoft released a new open-source repository called 'skills' on GitHub that provides a framework for building grounded coding agents using MCP servers, custom agents, and AGENTS.md templates, with over 175 pre-built skills for Azure SDKs and Microsoft AI Foundry. This repository addresses a key limitation of coding agents by providing domain-specific context and activation patterns, making AI agents more reliable and effective for real-world software development tasks, especially within the Microsoft ecosystem. The skills can be installed via a simple npx command (npx skills add microsoft/skills) into the agent's directory like .github/skills/ for GitHub Copilot, and the repository is actively developed with ongoing additions and improvements, as indicated by a 'Work in Progress' notice.

rss · GitHub Trending - TypeScript Daily · Jul 3, 01:40

**Background**: Coding agents, such as GitHub Copilot, leverage large language models to assist with code generation and software tasks. However, they often lack domain-specific context about a project's SDKs, APIs, and internal codebase, leading to generic or incorrect suggestions. Grounding refers to anchoring agent behavior in actual project code and documentation to improve accuracy. MCP (Model Context Protocol) servers provide a standardized way to expose external tools and data sources to AI agents.

<details><summary>References</summary>
<ul>
<li><a href="https://mcpservers.org/">Awesome MCP Servers</a></li>
<li><a href="https://bitoai.my/product/grounded-coding/">Grounded coding with AI Architect | Bito</a></li>

</ul>
</details>

**Tags**: `#Microsoft`, `#AI Agents`, `#MCP`, `#SDK`, `#GitHub`

---

<a id="item-15"></a>
## [MCP Apps Protocol Enables Interactive UIs in AI Chatbots](https://github.com/modelcontextprotocol/ext-apps) ⭐️ 8.0/10

Anthropic, OpenAI, and the MCP community have released the official specification and SDK for the MCP Apps protocol, which allows MCP servers to serve interactive UIs (e.g., charts, forms, dashboards) that render inline within AI chatbots like Claude and ChatGPT. This standardizes the embedding of rich user interfaces in AI chatbots, enabling more complex and interactive interactions beyond plain text, which is a significant step for practical AI applications and the MCP ecosystem. MCP Apps builds on the Model Context Protocol (MCP) and uses standard web technologies (HTML, CSS, JavaScript) for UI rendering. The SDK is available on npm (@modelcontextprotocol/ext-apps), and the protocol is already supported by Claude and ChatGPT as compliant chat clients.

rss · GitHub Trending - TypeScript Daily · Jul 3, 01:40

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems integrate with external tools and data sources. MCP Apps is the first official extension to MCP (SEP-1865), designed to allow MCP servers to deliver interactive UI components directly into chat interfaces, greatly expanding the capabilities of AI assistants.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://serpapi.com/blog/mcp-apps-with-fastmcp-interactive-ui/">MCP Apps with FastMCP: Turning Tool Output Into Interactive UI</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol (MCP)? - Model Context Protocol</a></li>

</ul>
</details>

**Tags**: `#MCP`, `#UI`, `#AI Chatbots`, `#Protocol`, `#Specification`

---

<a id="item-16"></a>
## [uv: A Rust-Powered, Ultra-Fast Python Package Manager](https://github.com/astral-sh/uv) ⭐️ 8.0/10

Astral has released uv, a Python package and project manager written in Rust that promises 10-100x speed improvements over pip and replaces multiple existing tools like pip, poetry, pyenv, and more. uv addresses long-standing bottlenecks in Python package management, especially installation speed and tool fragmentation, potentially improving developer productivity significantly. Its backing by Astral, creators of Ruff, lends credibility and suggests a growing trend of replacing Python tools with Rust counterparts. uv achieves its speed through Rust implementation and a global cache for dependency deduplication, and it can be installed via curl or pip without requiring Rust or Python itself. It also features a pip-compatible interface for easy migration and supports Cargo-style workspaces for scalable projects.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: Python package management traditionally involves multiple tools like pip for installing packages, poetry for dependency management, pyenv for Python version management, and others. These tools are often written in Python themselves, leading to performance overhead. uv is part of a broader movement to rewrite core Python infrastructure in Rust, following successful examples like Ruff (a fast linter) and PyO3/maturin.

**Tags**: `#Rust`, `#Python`, `#package manager`, `#developer tools`

---

<a id="item-17"></a>
## [Tree-sitter: Incremental Parsing Library for Programming Tools](https://github.com/tree-sitter/tree-sitter) ⭐️ 8.0/10

Tree-sitter is an incremental parsing system that can build a concrete syntax tree for a source file and efficiently update it as the file is edited on every keystroke. It is widely adopted in text editors like Neovim, Atom, and Emacs for syntax highlighting and code analysis. By enabling fast and robust parsing on every edit, tree-sitter significantly improves the responsiveness and accuracy of IDE features like syntax highlighting, code folding, and semantic navigation. This makes it a foundational tool for modern developer tooling. The runtime library is written in pure C and is dependency-free, making it easy to embed in any application. It provides bindings for Rust and WebAssembly, and a command-line interface for generating parsers from grammar files.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: Incremental parsing is a technique that re-parses only the changed portions of a file, rather than the entire file, enabling real-time updates even in large codebases. A concrete syntax tree (CST) preserves all syntactic details from the source text exactly as written, unlike an abstract syntax tree (AST) that may omit certain tokens. Tree-sitter combines these concepts to produce accurate syntax trees that can be updated incrementally with minimal delay.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Concrete_syntax_tree">Concrete syntax tree</a></li>
<li><a href="https://stackoverflow.com/questions/1888854/what-is-the-difference-between-an-abstract-syntax-tree-and-a-concrete-syntax-tre">parsing - What is the difference between an Abstract Syntax Tree and...</a></li>
<li><a href="https://offlinetools.org/a/json-formatter/incremental-parsing-for-responsive-json-formatting">Incremental Parsing for Responsive JSON Formatting | Offline Tools</a></li>

</ul>
</details>

**Tags**: `#parsing`, `#syntax tree`, `#programming tools`, `#incremental parsing`

---

<a id="item-18"></a>
## [Rolldown: New Rust-based JS/TS Bundler with Rollup API](https://github.com/rolldown/rolldown) ⭐️ 8.0/10

Rolldown is a new JavaScript/TypeScript bundler written in Rust, offering a Rollup-compatible API and plugin interface. It is intended to serve as the future bundler for Vite. Rolldown combines Rust's performance with Rollup's familiar API, potentially offering significantly faster builds for large-scale JavaScript/TypeScript projects. Its adoption as Vite's future bundler could reshape the tooling ecosystem. Rolldown is developed by VoidZero Inc. and is available as an npm package. It supports multiple platforms including macOS, Linux, Windows, and WebAssembly via WASM.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: A bundler is a tool that combines multiple JavaScript or TypeScript modules into a single file for use in browsers. Rollup is a popular bundler known for its tree-shaking and plugin ecosystem, while esbuild is a fast bundler written in Go. Rolldown aims to provide the best of both: Rollup's API and Rust's speed.

<details><summary>References</summary>
<ul>
<li><a href="https://rollupjs.org/">Rollup</a></li>

</ul>
</details>

**Tags**: `#rust`, `#bundler`, `#javascript`, `#typescript`, `#performance`

---

<a id="item-19"></a>
## [Helix: A Post-Modern Modal Text Editor in Rust](https://github.com/helix-editor/helix) ⭐️ 8.0/10

Helix is a post-modern modal text editor written in Rust, inspired by Kakoune and Neovim, that has gained significant traction in the developer community for its speed, built-in language server support, and tree-sitter integration. Helix represents a new generation of terminal-based editors that combine the efficiency of modal editing with modern features like multiple selections and native LSP support, challenging established editors such as Vim and Neovim. Helix uses tree-sitter for incremental syntax highlighting and code editing, and relies on Kakoune's multiple selections as a core paradigm. It is primarily terminal-based but plans to explore a custom GUI renderer using wgpu.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: A modal editor is a text editor with different modes for inserting, navigating, and executing commands, popularized by Vim. Multiple selections allow editing several cursor positions simultaneously, boosting productivity. Tree-sitter is a parser generator for fast, incremental parsing, enabling smart syntax highlighting and code navigation. Language Server Protocol (LSP) provides a standardized interface for language-specific features like autocomplete and diagnostics. Helix bundles all these features into a single Rust binary for high performance.

<details><summary>References</summary>
<ul>
<li><a href="https://helix-editor.com/">Helix</a></li>
<li><a href="https://grokipedia.com/page/Helix_text_editor">Helix (text editor)</a></li>
<li><a href="https://phoenixnap.com/glossary/modal-editor">What Is a Modal Editor ? | phoenixNAP IT Glossary</a></li>

</ul>
</details>

**Tags**: `#text editor`, `#rust`, `#modal editor`, `#open source`

---

<a id="item-20"></a>
## [ttl: A Modern Rust-Based Traceroute Alternative](https://github.com/lance0/ttl) ⭐️ 8.0/10

ttl is a new network diagnostic tool written in Rust that provides a real-time TUI, per-hop statistics, ASN/GeoIP lookup, ECMP detection, MPLS label parsing, and many other advanced features. It aims to be a superior replacement for the classic mtr tool. This tool modernizes network diagnostics by integrating features often requiring multiple separate utilities, such as path MTU discovery, NAT detection, and route flap alerts, into a single, fast, and scriptable application. It benefits network engineers, system administrators, and anyone needing detailed network path analysis. ttl supports Paris/Dublin traceroute for ECMP path enumeration, binary search path MTU discovery, NAT detection via source port rewriting, and MPLS label parsing from ICMP extensions. It offers scriptable output formats (JSON, CSV, text) and a daemon mode with a Prometheus exporter.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: Traceroute is a classic network diagnostic tool that traces the path packets take to a destination, revealing each hop's IP address and latency. Traditional traceroute lacks features like ECMP detection (which identifies load-balanced paths) and MPLS label parsing (which decodes labels in MPLS networks). ttl is built in Rust, a systems programming language known for performance and safety, and it integrates these advanced capabilities along with real-time visualization and enrichment from external databases like ASN and GeoIP.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lance0/ttl">GitHub - lance0/ttl: Fast, modern traceroute with real-time TUI, per-hop...</a></li>
<li><a href="https://ru.wikipedia.org/wiki/MPLS">MPLS — Википедия</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#networking`, `#traceroute`, `#CLI`, `#tool`

---

<a id="item-21"></a>
## [wgpu: Safe, Cross-Platform Rust Graphics API](https://github.com/gfx-rs/wgpu) ⭐️ 8.0/10

wgpu is a mature, pure-Rust implementation of the WebGPU standard that runs natively on Vulkan, Metal, D3D12, and OpenGL, as well as on WebGL2 and WebGPU in the browser. It is used in major projects such as Firefox, Servo, and Deno. wgpu provides a safe and modern graphics API for Rust developers, enabling cross-platform GPU compute and rendering without unsafe code. Its adoption by key browsers and runtimes makes it a cornerstone for WebGPU's future in both web and native applications. The API mirrors the WebGPU specification but is tailored for Rust, offering zero-cost abstractions and seamless integration with the Rust ecosystem. wgpu also provides C bindings via wgpu-native for use in other languages like C++.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: WebGPU is a next-generation graphics API standardized by the W3C, designed to supersede WebGL and provide low-level GPU access for the web. Rust is a systems programming language focused on safety and performance. wgpu bridges these two ecosystems, allowing Rust developers to write GPU code that runs across diverse hardware backends with full safety guarantees.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU - Wikipedia</a></li>
<li><a href="https://www.w3.org/TR/webgpu/">WebGPU - W3C</a></li>
<li><a href="https://en.wikipedia.org/wiki/Graphics_processing_unit">Graphics processing unit - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Rust`, `#graphics`, `#WebGPU`, `#cross-platform`, `#API`

---

<a id="item-22"></a>
## [FFF: Fast File Search SDK for AI Agents and Developers](https://github.com/dmtrKovalenko/fff) ⭐️ 8.0/10

A new file search SDK called 'fff' has been released, offering typo-resistant path and content search, frecency-ranked file access, and a background watcher. It claims to be faster than ripgrep and fzf in long-running processes. This tool bridges the gap between traditional CLI file search tools and AI agent needs, providing a library that integrates with multiple languages and MCP servers. It can significantly improve developer productivity and AI agent efficiency in code navigation. FFF supports Rust, C, Python, Bun, NodeJS, and provides an MCP server for AI agents like Claude Code. It uses SIMD-accelerated fuzzy matching and Smith-Waterman scoring for content search.

rss · GitHub Trending - Rust Daily · Jul 3, 01:39

**Background**: Traditional file search tools like ripgrep and fzf are optimized for single-use searches but have overhead for repeated searches. Frecency ranking combines frequency and recency to prioritize files that are used often, while typo-resistant search algorithms like Smith-Waterman allow matching despite typos.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/dmtrKovalenko/fff">dmtrKovalenko/fff: The fastest and the most accurate file search SDK...</a></li>
<li><a href="https://www.aitoolnet.com/fff">fff - Fast, resident-memory file search for AI agents - Aitoolnet</a></li>

</ul>
</details>

**Tags**: `#file-search`, `#SDK`, `#Rust`, `#AI-agents`, `#developer-tools`

---

<a id="item-23"></a>
## [Ollama: Run Open-Source LLMs Locally](https://github.com/ollama/ollama) ⭐️ 8.0/10

Ollama is a highly popular open-source tool that allows users to run large language models such as DeepSeek, Qwen, and Gemma directly on their own computers, providing a command-line interface, REST API, and integrations with coding assistants. By enabling local execution of powerful AI models, Ollama democratizes access to advanced AI, reduces dependency on cloud services, and enhances data privacy, which is a significant advantage for developers and researchers seeking cost-effective and private AI inference. Ollama leverages llama.cpp as its primary backend for efficient inference and offers official Python and JavaScript libraries. It also integrates with tools like Claude Code and Copilot CLI through a simple 'ollama launch' command.

rss · GitHub Trending - Go Daily · Jul 3, 01:35

**Background**: Large language models (LLMs) are typically accessed via cloud APIs, which can be expensive and raise privacy concerns. Ollama addresses this by allowing users to run open-weight models locally on their own hardware. Models like DeepSeek and Qwen are open-source alternatives that have gained popularity due to their competitive performance and low cost.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ollama">Ollama</a></li>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLM`, `#open-source`, `#local-inference`, `#Go`

---

<a id="item-24"></a>
## [Bridgewater Study: Frontier AI Models Fail 80% Financial Accuracy Threshold](https://www.ithome.com/0/972/445.htm) ⭐️ 8.0/10

Bridgewater's AIA Labs and Thinking Machines Lab tested frontier AI models (GPT, Claude, Gemini) on basic financial judgment tasks, finding they achieved only 50-70% accuracy even with expert prompts. A fine-tuned open-source Qwen3-235B model reached 84.7% accuracy with 1/14th the inference cost. This study challenges the assumption that frontier AI models are superior for specialized financial tasks, demonstrating that fine-tuned open-source models can outperform them at a fraction of the cost. It underscores the value of proprietary data and domain-specific fine-tuning, with implications for AI deployment in regulated industries. The fine-tuned Qwen3-235B model used the Tinker platform and techniques including CISPO loss, asymmetric clipping, and on-policy distillation. The model reduced error rate by 29.8% compared to the best frontier model (78.2%), and cost only about 1/14th as much for inference.

rss · IT之家 · Jul 3, 13:51

**Background**: Frontier AI models like GPT-4 and Claude are large language models trained on massive datasets, but they often underperform on specialized tasks without fine-tuning. Fine-tuning adapts a pre-trained model to a specific domain using labeled data. Financial judgment tasks require replicating expert intuition, which is hard to codify, making them a challenging benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://thinkingmachines.ai/tinker/">Tinker - Thinking Machines Lab</a></li>
<li><a href="https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/CISPO.html">Clipped Importance Sampling Policy Optimization ( CISPO ) — swift...</a></li>
<li><a href="https://langdb.ai/app/models/deepinfra/qwen3-235b-a22b-2507">qwen 3 - 235 b -a22b-2507 by deepinfra | AI Model Pricing... | LangDB</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Finance`, `#Fine-tuning`, `#Open-source`, `#Large Language Models`

---

<a id="item-25"></a>
## [Vidu S1: Real-Time Video Chat with Voice Control via Autoregressive Diffusion](https://www.ithome.com/0/972/436.htm) ⭐️ 8.0/10

Shengshu Technology released Vidu S1, a new model supporting real-time video chat and voice-controlled video direction, based on an autoregressive diffusion approach. It allows users to interact continuously with digital characters via voice commands. This marks a significant step in interactive AI, combining real-time video generation with voice control for dynamic, ongoing interactions. It could transform applications like virtual assistants, live streaming, and digital avatars. Vidu S1 supports 540P resolution at 25 FPS (up to 42 FPS) and can create interactive characters from real people, anime, or pets with personalized voices. It uses an autoregressive diffusion model that generates video frame-by-frame based on historical frames and voice commands.

rss · IT之家 · Jul 3, 13:00

**Background**: Autoregressive diffusion models combine autoregressive (AR) generation with diffusion processes. AR models generate data step-by-step conditioned on previous outputs, while diffusion models are generative models that learn to reverse a noising process. Vidu S1 integrates both to generate video continuously in real time, responding to voice input.

<details><summary>References</summary>
<ul>
<li><a href="https://cloud.tencent.com/developer/article/2508274">爆火Block Diffusion引发LLM...</a></li>
<li><a href="https://www.dongaigc.com/a/autoregressive-diffusion-pytorch">Autoregressive Diffusion: 基于PyTorch的 自 回 归 扩 散 模 型 实现 - 懂AI</a></li>

</ul>
</details>

**Tags**: `#AI`, `#real-time video`, `#voice control`, `#diffusion model`, `#interactive AI`

---

<a id="item-26"></a>
## [JD Logistics Launches China's First L4 Autonomous Heavy Truck Demo](https://www.ithome.com/0/972/419.htm) ⭐️ 8.0/10

On July 3, 2025, JD Logistics, in collaboration with Sinotruk and Inceptio Technology, began the first L4 autonomous heavy truck freight demonstration in China's express delivery industry, covering a 31 km route with a full load of 43 tons. This milestone moves autonomous trucking from testing to real-world logistics, bridging the gap between last-mile and long-haul automation, and potentially reducing costs and improving efficiency in freight transport. The trucks are equipped with Inceptio Technology's full-stack L4 autonomous driving system, using lidar, millimeter-wave radar, and multi-camera perception. They have a three-tier safety framework: vehicle autonomous decision, real-time cloud monitoring, and remote emergency handling, with a safety driver in the cab.

rss · IT之家 · Jul 3, 11:25

**Background**: L4 autonomous driving means the vehicle can handle all driving tasks in specific conditions without human intervention, but within a defined operational design domain. Beijing's High-Level Autonomous Driving Demonstration Zone provides over 100 square kilometers of roads with intelligent infrastructure. JD Logistics has been developing unmanned technologies including delivery robots and drones, and now extends to heavy trucks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Inceptio_Technology">Inceptio Technology - Wikipedia</a></li>
<li><a href="https://english.beijing.gov.cn/investinginbeijing/WhyBeijing/DistrictsParks/Economic_Area/Key_industrial_parks/202501/t20250110_3985832.html">Beijing High - Level Autonomous Driving Demonstration Zone</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#logistics`, `#L4 autonomous truck`, `#JD Logistics`, `#freight`

---

<a id="item-27"></a>
## [Alibaba Bans All Anthropic Products After Hidden Backdoor Found](https://www.36kr.com/p/3879721635361032) ⭐️ 8.0/10

Alibaba has issued an internal notice banning all Anthropic products, including Claude, Claude Code, Sonnet, Opus, and Fable, effective July 10. The decision follows the discovery of a hidden backdoor in Claude Code that secretly fingerprints Chinese users and tampers with system prompts. This marks a major shift in trust between Chinese tech companies and foreign AI tool providers, as Alibaba moves from encouraging external model usage to prioritizing security. The incident could lead other Chinese enterprises to reevaluate their reliance on closed-source AI tools from non-domestic vendors. The backdoor, present since Claude Code version 2.1.91 (April 2026), checked system timezone and proxy settings for Chinese entities, then stealthily modified system prompts using invisible Unicode characters to exfiltrate data. Anthropic acknowledged the issue and rolled back the changes on July 2.

rss · 36氪 - 24小时热榜 · Jul 3, 10:15

**Background**: Claude Code is an AI coding agent with file system and shell execution privileges, making it a sensitive tool for development environments. The backdoor used steganography to hide fingerprinting data within normal-looking prompts, raising severe security and trust concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://digg.com/tech/misirerb">It reportedly detects local timezone settings when proxies are enabled</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/72518">[BUG] Anthropic embedded spyware in Claude Code · Issue #72518...</a></li>
<li><a href="https://www.indiatoday.in/technology/news/story/anthropic-tried-to-spy-on-chinese-claude-users-through-hidden-code-now-faces-backlash-2938754-2026-07-02">Anthropic tried to spy on Chinese Claude users through hidden code ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#Anthropic`, `#Claude`, `#Alibaba`

---

<a id="item-28"></a>
## [Baidu's AI chip unit Kunlun Chip targets $50B Hong Kong IPO](https://www.36kr.com/p/3879603134312449) ⭐️ 8.0/10

Kunlun Chip, Baidu's AI chip subsidiary, is nearing a Hong Kong IPO with a target valuation of about $50 billion, and is requiring potential cornerstone investors to commit to purchasing chips worth 3 to 7 times their investment amount. This IPO could value Kunlun Chip higher than its parent Baidu, marking a significant milestone in China's AI hardware sector and reflecting the surging demand for domestic AI accelerators amid US export restrictions. Kunlun Chip's main product is the P800 (2024), targeting data center inference, followed by the M100 (early 2026) and M300 (2027) for large-scale training. The company holds a 11.6% share in China's AI accelerator server market (IDC 2025), tied with Cambricon for third place among domestic vendors.

rss · 36氪 - 24小时热榜 · Jul 3, 09:29

**Background**: Kunlun Chip originated from Baidu's internal AI chip team founded in 2011, and was spun off as an independent company in 2021 with a valuation of about 13 billion yuan. The company develops AI accelerators for cloud-to-edge scenarios, leveraging Baidu's ecosystem including PaddlePaddle deep learning framework. Its chips are used in Baidu's search, cloud, and autonomous driving businesses, as well as by external clients like China Mobile.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kunlunxin">Kunlunxin - Wikipedia</a></li>
<li><a href="https://www.zdnet.com/article/baidu-creates-kunlun-silicon-for-ai/">Baidu creates Kunlun silicon for AI | ZDNET</a></li>

</ul>
</details>

**Tags**: `#IPO`, `#AI chips`, `#Baidu`, `#Kunlun Chip`, `#semiconductor`

---

<a id="item-29"></a>
## [Huawei Mate 80 Pro gaming efficiency surpasses Snapdragon 8 Gen3](https://www.bilibili.com/video/BV1F7T46wEyT) ⭐️ 8.0/10

Geekerwan's review reveals that the Huawei Mate 80 Pro series, powered by the Kirin 9030 chip, achieves better gaming energy efficiency than the Snapdragon 8 Gen3 thanks to native HarmonyOS optimization. This demonstrates that Huawei's software-hardware co-optimization can overcome process node disadvantages, potentially reshaping the mobile chip landscape and offering users longer battery life without sacrificing performance. The Mate 80 Pro Max runs Genshin Impact at 60fps with a total power consumption of just 4.9W, and Honor of Kings at 120fps with around 3W, while the CPU multi-core efficiency falls between Snapdragon 8 Gen2 and Gen3.

telegram · bilibili 排行榜-全站 · Jul 3, 13:27

**Background**: The Kirin 9030 series is believed to use a 7nm process with a 9-core CPU and Maleoon 935 GPU, featuring around 15 billion transistors. Huawei's 'Soft-Hard-Core-Cloud' integration is a system-level optimization that coordinates operating system, hardware, chip, and cloud resources to improve real-world performance beyond raw specs.

<details><summary>References</summary>
<ul>
<li><a href="https://m.zol.com.cn/article/10921163.html">华为 麒 麟 9030 系列发布 性能追赶国际主流但存制程差距-中关村在线</a></li>
<li><a href="https://post.smzdm.com/p/adozp02z/">麒 麟 9030 芯 片 性能显著提升_CPU_什么值得买</a></li>
<li><a href="http://www.fengsung.com/n-251230145203716.html">fengsung.com/n-251230145203716.html</a></li>

</ul>
</details>

**Tags**: `#Huawei`, `#Kirin 9030`, `#HarmonyOS`, `#mobile processors`, `#energy efficiency`

---

<a id="item-30"></a>
## [Native low-rank factorization improves transformer training efficiency](https://www.reddit.com/r/MachineLearning/comments/1umtiqk/training_transformers_where_every_layer_w_vu%E1%B5%80/) ⭐️ 8.0/10

A new method called Native Factorized Weights (NFW) replaces every linear layer in a transformer with a low-rank factorization W = V·U^T from initialization, training from scratch without post-hoc compression or adapters. NFW achieves better perplexity than dense baselines with fewer parameters, revealing a corpus-determined optimal rank that prevents memorization and improves generalization, potentially leading to more parameter-efficient model design. On WikiText-2 with a 4-layer transformer of hidden size 2048, NFW with rank 32 achieved validation perplexity 5.617 versus dense baseline 6.219, using fewer parameters and staying stable with dropout; the optimal rank r* is bounded by underfitting and memorization thresholds.

reddit · r/MachineLearning · /u/MrAddams_LibraLogic · Jul 3, 23:33 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1umtiqk/training_transformers_where_every_layer_w_vuᵀ/)

**Background**: Low-rank factorization decomposes a large weight matrix into two smaller matrices, reducing parameters. LoRA applies this only during fine-tuning of pretrained models, whereas NFW uses it from the start of training, making the low-rank structure inherent.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2602.12429">Stabilizing Native Low-Rank LLM Pretraining</a></li>
<li><a href="https://proceedings.mlsys.org/paper_files/paper/2023/file/c2db3ef0b1ad4c5ec7c3a0a0c6f6c832-Paper-mlsys2023.pdf">Cuttlefish: Low - rank Model Training without All The Tuning</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#low-rank factorization`, `#efficient deep learning`, `#parameter efficiency`, `#machine learning research`

---

<a id="item-31"></a>
## [Anthropic Accuses Alibaba of Massive Distillation Attack on Claude](https://t.me/zaihuapd/42327) ⭐️ 8.0/10

Anthropic has accused Alibaba of perpetrating the largest known distillation attack against its Claude AI model, using 25,000 fraudulent accounts to extract capabilities between April 22 and June 5, 2026. This accusation highlights critical security vulnerabilities in AI APIs and underscores the escalating intellectual property battles between leading AI companies, potentially shaping future regulations on model protection. Anthropic reported over 28.8 million interactions with Claude from the fraudulent accounts, and the attack is linked to Alibaba's AI lab Qwen.

telegram · zaihuapd · Jul 3, 06:21

**Background**: Model distillation is a technique where a weaker model learns from a stronger model's outputs to replicate capabilities efficiently. Distillation attacks refer to unauthorized use of this technique to steal proprietary models. Anthropic previously published methods to detect such attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>
<li><a href="https://www.mindstudio.ai/blog/ai-model-distillation-attacks-explained">AI Model Distillation Attacks : What They Are and Why... | MindStudio</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Model Distillation`, `#Intellectual Property`, `#Anthropic`, `#Alibaba`

---

<a id="item-32"></a>
## [NASA Launches LINK Spacecraft to Rescue Swift Telescope](https://apnews.com/article/swift-nasa-satellite-rescue-katalyst-a7ddd740ca099587c58865f583c7245a) ⭐️ 8.0/10

NASA launched the LINK spacecraft on July 3, 2025, to rendezvous with the aging Swift gamma-ray burst observatory and boost its orbit by about 240 kilometers, preventing it from burning up in Earth's atmosphere later this year. This mission marks the first private spacecraft to attempt capturing and boosting a US government satellite, demonstrating on-orbit servicing capabilities that could help reduce space debris and extend the life of valuable scientific instruments. LINK will use a robotic arm to grapple Swift and slowly raise its altitude over several months. Swift, launched in 2004, has been in orbit for over 20 years and its orbit has been decaying faster due to increased solar activity.

telegram · zaihuapd · Jul 3, 15:43

**Background**: On-orbit satellite servicing involves refueling, boosting, or repairing satellites while in space. Swift is a gamma-ray burst observatory that has made significant discoveries. Without intervention, it would re-enter Earth's atmosphere around October 2025. The LINK spacecraft is built by a private company, representing a new era of commercial space servicing.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nasa.gov/image-article/link-spacecraft-set-for-mission-to-boost-nasas-swift-observatory/">LINK Spacecraft Set for Mission to Boost NASA’s Swift... - NASA</a></li>
<li><a href="https://en.wikipedia.org/wiki/On-orbit_satellite_servicing">On-orbit satellite servicing</a></li>

</ul>
</details>

**Tags**: `#space`, `#NASA`, `#satellite rescue`, `#astronomy`, `#space technology`

---

<a id="item-33"></a>
## [Tencent Xuanwu Lab's Atuin AI surpasses Mythos in CyberGym test](https://mp.weixin.qq.com/s/BzU7g-2iG7d6h4ViwMhxyg) ⭐️ 8.0/10

Tencent Xuanwu Lab announced that its Atuin AI achieved a 84.0% score on the UC Berkeley-led CyberGym cybersecurity benchmark, surpassing Anthropic's Claude Mythos Preview. It was built on the locally deployable open-source model GLM-5.1, costing less than 0.1% of Mythos's budget. This demonstrates a major breakthrough in applying open-source AI to real-world cybersecurity, achieving superior results at a fraction of the cost of proprietary models. It shows that accessible AI can discover critical vulnerabilities overlooked by other systems, potentially improving software security across the industry. Atuin AI discovered multiple high-risk logic vulnerabilities in projects like curl, gnark, OpenSSL, Python cryptography, and Java bc-java, with severity scores up to 9.3. In the Berkeley BVI real-world vulnerability list, it ranked 1st in severity and 5th in total number of critical vulnerabilities.

telegram · zaihuapd · Jul 3, 16:12

**Background**: CyberGym is a large-scale cybersecurity evaluation framework based on 1,507 real-world vulnerabilities from 188 open-source projects, designed to assess AI agents' vulnerability analysis capabilities. GLM-5.1 is an open-source large language model developed by Z.ai (formerly Zhipu AI), released under the MIT License since July 2025, with strong coding capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cybergym.io/cybergym/">CyberGym : Evaluating AI Agents' Real-World Cybersecurity...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GLM_5.1">GLM 5.1</a></li>
<li><a href="https://www.xugj520.cn/archives/cybergym-ai-cybersecurity-test.html">CyberGym 揭示AI 网 络 安 全 真实水平：1507个漏洞挑战下仅12...</a></li>

</ul>
</details>

**Tags**: `#AI安全`, `#网络安全`, `#基准测试`, `#开源模型`, `#漏洞挖掘`

---