---
layout: default
title: "Horizon Summary: 2026-08-27 (EN)"
date: 2026-08-27
lang: en
---

> From 227 items, 14 important content pieces were selected

---

**Technology News**
1. [Nvidia reportedly pursues Hugging Face acquisition](#item-tech-news-1) ⭐️ 8.0/10
2. [Z.ai Announces GLM-5.3-Flash](#item-tech-news-2) ⭐️ 8.0/10
3. [vLLM 0.28.0 Expands Inference Optimizations](#item-tech-news-3) ⭐️ 7.0/10
4. [Mechanical Turk Reportedly Shutting Down September 30](#item-tech-news-4) ⭐️ 7.0/10
5. [AWS Acquires DuckLabs](#item-tech-news-5) ⭐️ 7.0/10
6. [Alleged AGPL Violation in 3D Printing](#item-tech-news-6) ⭐️ 7.0/10
7. [Qwen3.8-Flash-Next Announced](#item-tech-news-7) ⭐️ 7.0/10
8. [OpenAI Addresses Hugging Face Incident](#item-tech-news-8) ⭐️ 7.0/10
9. [AWS Plans 2 Million More NVIDIA GPUs](#item-tech-news-9) ⭐️ 7.0/10
10. [Chinese Team Reports 600 Wh/kg Lithium-Metal Pouch Cell](#item-tech-news-10) ⭐️ 7.0/10
11. [36Kr Roundup Highlights Apple and Nvidia Claims](#item-tech-news-11) ⭐️ 7.0/10
12. [China Tests Earth-Moon Laser Communications](#item-tech-news-12) ⭐️ 7.0/10
13. [Google Updates Gemini Audio With Gemini 3.5 Transcribe](#item-tech-news-13) ⭐️ 7.0/10

**Financial News**
1. [Earnings Drive After-Hours Stock Moves](#item-finance-news-1) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Nvidia reportedly pursues Hugging Face acquisition](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8) ⭐️ 8.0/10

Nvidia is reported to have held serious talks to acquire Hugging Face in a deal valuing the AI model hub at more than $13 billion, with linked coverage split between stronger wording that Nvidia has agreed to buy it and more cautious wording that talks are ongoing. The primary linked report from The Information is paywalled, and the supplied Business Insider/RSS excerpt says the companies have been negotiating in recent weeks, so the exact deal status remains uncertain from the available evidence. The potential acquisition matters because Hugging Face is a major discovery, hosting, and distribution platform for open-source and commercial AI models, datasets, and tooling. If completed, the deal would extend Nvidia’s influence beyond GPUs and CUDA into a central layer of the AI software and model distribution stack.

hackernews · mfiguiere · Aug 27, 01:12 · [Discussion](https://news.ycombinator.com/item?id=49458161)

**「Background」** Hugging Face is widely used as an AI developer platform and model repository, making it an important distribution point for open-source and commercial machine-learning models. Nvidia dominates AI accelerator hardware and the CUDA software ecosystem, so a potential purchase of Hugging Face would connect a major AI hardware supplier with a major AI model and tooling hub.

**「Impact」** Developers and organizations that rely on Hugging Face for model hosting, downloads, and tooling would face new uncertainty over platform neutrality, open-source governance, pricing, and integration with Nvidia’s hardware and software ecosystem.

**「Community Discussion」** Commenters largely focused on concentration and control risks, with several arguing that Nvidia has a history of favoring proprietary drivers and APIs and could gain strategic visibility into model download patterns, hardware surveys, and AI development workflows. Others noted possible short-term benefits such as free or discounted credits, congratulated the Hugging Face team, and questioned whether earlier perceptions of Hugging Face as a more open alternative to OpenAI would survive under Nvidia ownership.

<details><summary>References</summary>
<ul>
<li><a href="https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8">Nvidia Has Been in Talks to Buy Hugging Face for More Than ...</a></li>
<li><a href="https://techcrunch.com/2026/08/24/hugging-face-reportedly-in-talks-to-be-acquired-for-13b/">Hugging Face reportedly in talks to be acquired for $13B</a></li>

</ul>
</details>

**Tags**: `#AI industry`, `#acquisitions`, `#open source`, `#Nvidia`, `#Hugging Face`

---

<a id="item-tech-news-2"></a>
### [Z.ai Announces GLM-5.3-Flash](https://z.ai/blog/glm-5.3-flash) ⭐️ 8.0/10

Z.ai announced GLM-5.3-Flash, a new AI model release that attracted Hacker News attention around open weights, serving costs, benchmark results, and deployment hardware. The supplied discussion points to model weights on Hugging Face under zai-org/GLM-5.3-Flash, making local or third-party experimentation a practical focus for readers. Commenters described the release as a lower-parameter, lower-cost follow-up to GLM-5.3 with near-GLM-5.3 performance, but those performance and cost comparisons are community claims rather than independently verified details in the supplied source. The discussion also raised caveats about Z.ai’s terms of service, including broad licenses over user inputs and outputs and vague content or conduct restrictions.

hackernews · Philpax · Aug 26, 14:08 · [Discussion](https://news.ycombinator.com/item?id=49449507)

**「Background」** Z.ai, formerly associated with Zhipu AI branding in some coverage, publishes GLM-family large language models and has released GLM-5.3-Flash with publicly available Hugging Face weights under an MIT license. The model is described in external coverage as a 320B-A18B mixture-of-experts model with a 1M-token context window, meaning it has many total parameters but activates a smaller subset per token to reduce serving cost and latency compared with dense models.

**「Impact」** AI developers evaluating open-weight models may now have another GLM-family option to test on their own infrastructure, while hosted use requires attention to Z.ai’s service terms.

**「Community Discussion」** Hacker News commenters were broadly interested in the pace of Chinese model releases, reported Hugging Face availability, and debated benchmark strength, claimed cost reductions, and serving on Chinese chips. Concerns centered on whether benchmarks and pricing claims are reliable and whether Z.ai’s terms of service are too broad or restrictive for some users.

<details><summary>References</summary>
<ul>
<li><a href="https://www.explainx.ai/blog/glm-5-3-flash-ox-alpha-official-launch-august-2026">GLM-5.3-Flash Launch — Ox Alpha Was Zhipu (MIT) | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://officechai.com/ai/glm-5-3-flash-benchmarks/">Z.AI Reveals Ox Alpha Is GLM 5.3 Flash, Competes With Claude Opus 4.8 &amp; GPT 5.6 Terra On Benchmarks</a></li>

</ul>
</details>

**Tags**: `#ai-models`, `#open-weights`, `#machine-learning`, `#benchmarks`, `#ai-infrastructure`

---

<a id="item-tech-news-3"></a>
### [vLLM 0.28.0 Expands Inference Optimizations](https://github.com/vllm-project/vllm/releases/tag/v0.28.0) ⭐️ 7.0/10

vllm-project released vLLM v0.28.0 with 584 commits from 270 contributors, including 76 new contributors, focused on LLM serving performance, model coverage, and deployment artifacts. The release includes a major Kimi-K3 optimization push with Decode Context Parallel support, fused FlashKDA decode and prefill kernels, SiTU activation support for MegaMoE, GEMM-RS for sequence parallelism, combined all-gathers with a reported 1.5 to 3x kernel-level speedup, an adaptive speculative token budget with about 60% better DSpark TTFT, optional shared-expert sharding saving about 17 GiB per GPU, and ROCm support through the V2 model runner. DeepSeek V4 gains end-to-end sparse MLA for plain decode, MTP, and DSpark speculative decoding, plus AMD Quark NVFP4 support, reasoning-effort prompt mappings, sparse top-k metadata kernel optimizations, narrowed eager CUDA graph regions, and ROCm enablement on gfx11 and gfx950. Broader changes include DFlash2 and DSpark speculative decoding improvements, Model Runner V2 maturation, tiered KV cache disk offloading, Rust frontend and gRPC additions, new defaults such as raising max\_num\_batched\_tokens from 8192 to 16384, and breaking changes including moving bitsandbytes support to an out-of-tree plugin, bumping Transformers to 5.15.0, and removing calculate\_kv\_scales and override\_attention\_dtype.

github · khluu · Aug 26, 09:46

**「Background」** vLLM is an open-source inference and serving engine for large language models, described by the project as high-throughput and memory-efficient. Releases like this matter to infrastructure teams because vLLM sits in the serving layer where GPU kernels, KV-cache management, batching, speculative decoding, and hardware backend support directly affect cost and latency.

**「Impact」** Teams serving models such as Kimi-K3, DeepSeek V4, Qwen variants, and multimodal workloads with vLLM may see new performance, memory, ROCm, and deployment options, but they must account for the listed breaking changes and updated CUDA, ROCm, Docker, and Python wheel targets.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient inference and serving engine for LLMs · GitHub</a></li>

</ul>
</details>

**Tags**: `#vLLM`, `#LLM inference`, `#GPU kernels`, `#open source`, `#ROCm`

---

<a id="item-tech-news-4"></a>
### [Mechanical Turk Reportedly Shutting Down September 30](https://www.mturk.com/) ⭐️ 7.0/10

A Hacker News item reports that Amazon Mechanical Turk is shutting down on September 30, with the linked URL pointing to mturk.com but no additional source content supplied here. The reported closure would matter because Mechanical Turk has long been used for crowdsourced microtasks, data labeling, surveys, research workflows, and machine-learning evaluation work. The available details do not include an official shutdown notice, migration instructions, account deadlines, or policy terms, so the date and operational specifics should be treated as unverified from the supplied material. Community discussion frames the move as connected to AI-driven task completion, reduced viability for broad low-skill microtask markets, and Amazon’s apparent shift toward Bedrock and SageMaker model-evaluation services.

hackernews · tmp10423288442 · Aug 26, 23:55 · [Discussion](https://news.ycombinator.com/item?id=49457545)

**「Background」** Amazon Mechanical Turk, launched in 2005, is a crowdsourcing marketplace where requesters pay workers to complete small human-intelligence tasks that software historically handled poorly. It became widely used for data labeling, surveys, content moderation, and machine-learning evaluation, reflecting Jeff Bezos’s early description of the service as “artificial artificial intelligence.”

**「Impact」** If the reported September 30 shutdown is accurate, Mechanical Turk requesters and workers would need to move task pipelines, payments, and labor workflows to other platforms or internal systems before that date.

**「Community Discussion」** Commenters largely saw the shutdown as unsurprising, citing AI-assisted arbitrage, declining fit for horizontal microtask marketplaces, and a lack of active stewardship after personnel moved toward AWS AI evaluation products. Some disagreed that the service had exhausted its usefulness, arguing that human task networks could become more valuable when coordinated with AI agents for real-world work.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pymnts.com/amazon/2026/amazon-sunsets-crowd-sourced-work-platform-mturk/">PYMNTS | Amazon Sunsets Crowd-Sourced Work Platform MTurk</a></li>
<li><a href="https://www.linkedin.com/news/story/amazon-is-ending-its-20-year-old-mechanical-turk-work-platform-9278106/">Amazon is ending its 20-year-old Mechanical Turk work... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#crowdsourcing`, `#machine-learning`, `#data-labeling`, `#tech-industry`

---

<a id="item-tech-news-5"></a>
### [AWS Acquires DuckLabs](https://ducklabs.com/news/2026/08/26/ducklabs-to-join-aws) ⭐️ 7.0/10

AWS is acquiring DuckLabs, a company associated with DuckDB, according to the submitted item. The acquisition matters to the data systems and open-source communities because commenters emphasized that DuckDB itself was not acquired: the open-source DuckDB intellectual property remains with the nonprofit DuckDB Foundation. The supplied material does not include detailed transaction terms, technical roadmap changes, or AWS integration plans. The key distinction is between DuckLabs joining AWS and DuckDB’s open-source governance remaining formally separate under the foundation.

hackernews · onderkalaci · Aug 26, 12:59 · [Discussion](https://news.ycombinator.com/item?id=49448321)

**「Background」** DuckDB is an open-source analytical database commonly used as an embedded engine for local or application-level data analysis, and its open-source project is licensed under MIT according to external reports. DuckLabs is the company associated with the DuckDB ecosystem, while the DuckDB Foundation is described as continuing to steward the open-source projects and hold their IP, which is why the acquisition of DuckLabs is distinct from an acquisition of DuckDB itself.

**「Impact」** DuckDB users and contributors face ownership uncertainty around DuckLabs’ future role, but the supplied comments indicate the open-source DuckDB IP remains with the DuckDB Foundation.

**「Community Discussion」** Commenters broadly congratulated the founders while expressing concern about AWS stewardship, team retention, and the risk that a major cloud provider could deprioritize or reshape the project. Several pushed back on the headline framing, stressing that AWS acquired DuckLabs rather than DuckDB, and one commenter suggested Apache DataFusion as an alternative, especially for Rust integration.

<details><summary>References</summary>
<ul>
<li><a href="https://elsolitario.org/en/2026/08/26/ducklabs-aws-duckdb-open-source-en/">DuckDB Open Source: DuckLabs Joins AWS in 2026</a></li>
<li><a href="https://www.comparethecloud.net/news/aws-acquires-ducklabs-commits-to-keeping-duckdb-open-source">AWS acquires DuckLabs, commits to keeping DuckDB open source</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#DuckDB`, `#databases`, `#open-source`, `#acquisitions`

---

<a id="item-tech-news-6"></a>
### [Alleged AGPL Violation in 3D Printing](https://lwn.net/SubscriberLink/1089390/46116614cc74b814/) ⭐️ 7.0/10

An LWN-linked item discusses an alleged ongoing AGPL violation in a 3D-printer software ecosystem, with the supplied metadata framing it as a dispute over open source compliance and networked device control. The central issue is that AGPL-licensed software carries source-availability obligations when modified software is provided as a network service, making noncompliance especially relevant for connected hardware platforms. The available item data does not include the article text, the specific software components at issue, the accused vendor&\#x27;s response, or any legal finding, so the claim should be treated as an allegation rather than an established outcome. The discussion matters because 3D-printer ecosystems increasingly combine firmware, slicers, cloud services, and proprietary device integrations that can affect both license compliance and user ownership.

hackernews · Velocifyer · Aug 26, 17:41 · [Discussion](https://news.ycombinator.com/item?id=49452980)

**「Background」** The Affero General Public License version 3 is a copyleft license designed to require source-code availability not only when software is distributed, but also when modified software is used to provide network services. In the 3D-printing workflow, slicer software converts a model into printer instructions, so licensing disputes around slicers and printer firmware can affect both desktop applications and network-connected device ecosystems. The reported dispute concerns Bambu Lab 3D-printer software and Software Freedom Conservancy allegations that Bambu has not provided source code for AGPLv3-covered modifications, including issues tied to slicer software and device firmware.

**「Impact」** Affected 3D-printer users and open source developers face continued uncertainty over whether the relevant ecosystem is honoring AGPL obligations and preserving practical user control over connected devices.

**「Community Discussion」** Commenters debated enforcement paths, including import pressure and litigation, while others argued that the practical appeal of printers that “just work” can outweigh licensing concerns for many customers. One commenter described using LAN mode with OrcaSlicer and an open source reverse-engineered networking plugin to avoid Bambu servers, but that is individual practical experience rather than a verified general solution.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linuxnews.net/articles/an-ongoing-3d-printer-agpl-violation">An ongoing 3D-printer AGPL violation - Linux News</a></li>
<li><a href="https://sfconservancy.org/news/2026/may/18/bambu-studio-3d-printer-agpl-violation-response/">Comprehensive Response to Bambu&#x27;s AGPLv3 Violations</a></li>
<li><a href="https://lwn.net/Articles/1074286/">Comprehensive Response to Bambu&#x27;s AGPLv3 Violations (Software ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#AGPL`, `#hardware`, `#3D-printing`, `#licensing`

---

<a id="item-tech-news-7"></a>
### [Qwen3.8-Flash-Next Announced](https://qwen.ai/blog?id=qwen3.8-flash-next) ⭐️ 7.0/10

Qwen announced Qwen3.8-Flash-Next, described in the supplied RSS excerpt as another open-weights model and a multimodal MoE, but the provided source body is incomplete and links to a third-party page rather than the stated Qwen blog. The Hacker News discussion cites a claimed architecture with a 125B-parameter main model, an additional 51B N-gram embeddings, and 6B parameters activated per token, though those details are not fully verifiable from the supplied source content alone. Commenters focused on what the sparse and N-gram design means for effective model size, quantization, self-hosting memory requirements, and coding-agent performance. One user reported using QwenCloud for repository merging and regression bisection with about 90M cached input tokens and 400k output tokens for $0.45, but this is an individual community report rather than benchmark evidence.

hackernews · tosh · Aug 26, 12:52 · [Discussion](https://news.ycombinator.com/item?id=49448210)

**「Background」** Qwen is Alibaba’s open-weights large language model family, and this item concerns a new Qwen3.8-Flash-Next release described as a multimodal mixture-of-experts model. In a mixture-of-experts architecture, only a subset of the model’s parameters is used for each token, which is why the reported 125B-parameter main model and 51B N-gram embeddings can coexist with 6B activated parameters per token.

**「Impact」** Developers evaluating Qwen3.8-Flash-Next may need hosted access or substantial local memory depending on quantization, because commenters expect the model’s stated 125B plus 51B-embedding footprint to be difficult to fit on typical self-hosted hardware.

**「Discussion」** The discussion was technically focused but cautious, with interest in the model’s N-gram embeddings, activated-parameter count, reasoning levels, and whether it improves on Qwen 3.8 27B in practical coding tasks. Some commenters reported strong coding-agent results, while others questioned memory feasibility and noted mixed subjective output quality in informal tests.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">Qwen3.8-Flash-Next - GitHub</a></li>
<li><a href="https://qwen.ai/blog?id=qwen3.8-flash-next">Qwen3.8-Flash-Next: A New Architecture, Towards Ultimate Cost ...</a></li>

</ul>
</details>

**Tags**: `#large-language-models`, `#qwen`, `#model-architecture`, `#ai-coding-tools`, `#self-hosting`

---

<a id="item-tech-news-8"></a>
### [OpenAI Addresses Hugging Face Incident](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) ⭐️ 7.0/10

OpenAI published a first-party post titled “The Hugging Face incident and the road ahead,” discussing an incident connected to Hugging Face and its implications for AI safety and security practices. The supplied item frames the post as relevant to cybersecurity, model evaluation, and agentic AI, but no source text is available here to verify the specific technical sequence, affected systems, dates, mitigations, or scope. The available context indicates the incident involved internal evaluation conditions around advanced exploitation and complex attack paths, raising questions about how model behavior should be tested and interpreted. Because the primary content is unavailable, the concrete impact and technical conclusions remain uncertain from the supplied evidence alone.

hackernews · amrrs · Aug 26, 19:15 · [Discussion](https://news.ycombinator.com/item?id=49454314)

**「Background」** Hugging Face is a major platform for hosting and sharing machine learning models and related tooling, so incidents involving it can affect how AI developers evaluate model security and deployment risk. OpenAI frames this post as a follow-up that shares findings from the Hugging Face security incident and describes steps to strengthen AI model security, monitoring, and alignment.

**「Discussion」** Commenters debated whether the behavior should be described as dangerous actions no human directed, with one pointing to OpenAI’s prior description of an internal evaluation that prompted models to pursue advanced exploitation. Others focused on multi-agent coordination, the possibility of rogue AI behavior, the absence of agents contacting humans, and concerns that reinforcement-learning evaluations may be vulnerable to reward hacking or cheating.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/hugging-face-incident-and-the-road-ahead/">The Hugging Face incident and the road ahead | OpenAI</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#cybersecurity`, `#model evaluation`, `#agentic AI`, `#OpenAI`

---

<a id="item-tech-news-9"></a>
### [AWS Plans 2 Million More NVIDIA GPUs](https://www.ithome.com/0/994/836.htm) ⭐️ 7.0/10

IT Home reports that Amazon AWS announced in a joint press release with NVIDIA that it plans to deploy an additional 2 million NVIDIA GPUs across its global infrastructure during 2027-2028. AWS had previously committed at GTC 2026 in March to deploying 1 million NVIDIA GPUs, so the new announcement raises its stated total deployment scale to 3 million GPUs. The report also says AWS will introduce NVIDIA Groq LPU, offer infrastructure based on NVIDIA Vera CPU in its own cloud services, and integrate its own chips with NVIDIA NVLink Fusion and NVHBM. AWS and NVIDIA are also described as cooperating on AI in factories, network interconnects, models, and physical-domain applications.

rss · IT之家 · Aug 27, 01:36

**「Background」** AWS is Amazon’s cloud computing division, and large GPU clusters are a core input for training and serving modern AI models because they can process many parallel matrix operations efficiently. NVIDIA’s Blackwell Ultra, Rubin and Rubin Ultra are successive AI accelerator generations referenced in the AWS-NVIDIA announcement for deployments planned across AWS Global Infrastructure in 2027-2028.

**「Impact」** If carried out as stated, the deployment would substantially expand AWS&\#x27;s NVIDIA-based AI compute capacity for customers using its global cloud infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://nvidianews.nvidia.com/news/aws-and-nvidia-to-deliver-2-million-additional-gpus-and-next-generation-infrastructure-for-agentic-and-physical-ai">AWS and NVIDIA to Deliver 2 Million Additional GPUs and Next-Generation Infrastructure for Agentic and Physical AI</a></li>

</ul>
</details>

**Tags**: `#AWS`, `#NVIDIA`, `#AI infrastructure`, `#cloud computing`, `#GPUs`

---

<a id="item-tech-news-10"></a>
### [Chinese Team Reports 600 Wh/kg Lithium-Metal Pouch Cell](https://www.ithome.com/0/994/825.htm) ⭐️ 7.0/10

IT Home reports that Tianmushan Laboratory announced on August 26 that a team led by Professor Gong Yongji, working with Professor Liu Kai’s group at Tsinghua University’s Department of Chemical Engineering, published a Nature Communications paper titled “Additive Strongly-Coordinated Solvation Structure towards High-Voltage 600 Wh/kg-class Lithium Metal pouch cell.” The study proposes an Additive Coordinated Solvation Structure electrolyte strategy using the multifunctional additive TMSFS, which is said to form thinner, denser cathode-electrolyte interphases of about 6.1 nm on high-voltage cathodes and LiF/Li₂S/Li₂O-rich solid-electrolyte interphases on lithium-metal anodes. Reported test results include a Li\|\|Cu average Coulombic efficiency of 97.8%, lithium symmetric-cell cycling for more than 2,000 hours at 1 mA cm⁻², a 10 Ah Li\|\|NCM811 pouch cell reaching 550.7 Wh/kg with 80% capacity retention after 180 cycles at 0.1C charge and 0.5C discharge, and a lithium-rich manganese-based pouch cell reaching 602.5 Wh/kg with 80% capacity retention after 60 cycles at 0.1C. The result matters because commercial graphite-anode lithium-ion batteries are described as approaching a 350 Wh/kg theoretical ceiling, while lithium-metal batteries are viewed as a possible route to longer-endurance eVTOLs, industrial drones, and electric general aviation aircraft. The report is still based on laboratory and publication claims, and it does not establish commercial manufacturability, aviation-grade safety validation, or independent replication.

rss · IT之家 · Aug 27, 01:13

**「Background」** Lithium-metal batteries replace the graphite anode used in conventional lithium-ion cells with metallic lithium, which can raise specific energy but tends to suffer from electrolyte breakdown, unstable interfaces, and dendrite growth. Electrolyte solvation design is one route researchers use to control the interphases that form on high-voltage cathodes and lithium-metal anodes; the linked Nature Communications paper identifies this work as a study of an additive strongly coordinated solvation structure for a high-voltage 600 Wh/kg-class lithium-metal pouch cell.

**「Impact」** For eVTOL, industrial drone, and electric aircraft battery developers, the result suggests a lab route toward cells well above 350 Wh/kg aviation-battery targets, but the reported pouch-cell endurance of 180 cycles at 550.7 Wh/kg and 60 cycles at 602.5 Wh/kg remains short of proving production-ready safety, lifetime, or manufacturability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41467-026-77095-x.pdf">Additive strongly-coordinated solvation structure towards ...</a></li>
<li><a href="https://interestingengineering.com/energy/worlds-first-catl-set-to-mass-produce-350-wh-kg-prismatic-cell-aviation-battery">CATL readies world`s first 350 Wh/kg prismatic cell aviation battery</a></li>

</ul>
</details>

**Tags**: `#battery-research`, `#hardware`, `#energy-storage`, `#lithium-metal`, `#electric-aviation`

---

<a id="item-tech-news-11"></a>
### [36Kr Roundup Highlights Apple and Nvidia Claims](https://www.36kr.com/p/3957017574030727) ⭐️ 7.0/10

A 36Kr daily roundup reports that Apple will hold a September 9 product event at its California headquarters under the theme “Surprise and shine,” where it says the company will release its first foldable phone. The item frames the launch as the first major product event under incoming CEO John Ternus, described as a key backer of the foldable iPhone project, and separately says Tim Cook will step down as CEO on September 1 and become executive chairman. The roundup also says Nvidia reported fiscal 2027 second-quarter revenue of $96.221 billion, up 106% year over year, and net profit of $59.688 billion, up 126%, with CFO Colette Kress projecting roughly 70% sales growth next fiscal year and saying revenue could potentially double without supply constraints. Other technology items include Apple Maps ads in the U.S. and Canada without a full user opt-out, Alibaba’s QwenWork international public beta, Samsung Electronics and SK Hynix plans to increase 8-layer HBM4 supply to Nvidia, SpaceX shifting Florida Starlink launches from Falcon 9 to Starship, and Chinese policy work on 6G, brain-computer interface standards, and OpenHarmony ecosystem growth.

rss · 36氪 - 24小时热榜 · Aug 27, 00:11

**「Background」** Apple’s September iPhone events are the company’s main annual stage for introducing new flagship models, and a foldable iPhone would mark its entry into a category already pursued by several Android manufacturers. Nvidia’s data-center GPUs are central to current AI infrastructure spending, so its reported fiscal 2027 second-quarter revenue of $96.2 billion and supply-constrained fiscal 2028 growth outlook are being read as indicators of continuing AI hardware demand.

**「Impact」** If accurate, the reported Apple foldable launch and Nvidia guidance would affect smartphone competitors, AI infrastructure buyers, and memory suppliers by signaling major new device competition and continued constrained AI-chip demand.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/26/apple-iphone-launch-date-john-ternus.html">Apple sets iPhone launch date, first under new CEO John Ternus</a></li>
<li><a href="https://www.cnn.com/2026/08/26/tech/apple-iphone-launch-john-ternus">‘Surprise and shine’: Apple to hold first major iPhone launch ...</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027">NVIDIA Announces Financial Results for Second Quarter Fiscal 2027 | NVIDIA Newsroom</a></li>
<li><a href="https://finance.yahoo.com/technology/ai/articles/nvidia-q2-earnings-call-highlights-230417656.html">NVIDIA Q2 Earnings Call Highlights</a></li>

</ul>
</details>

**Tags**: `#apple`, `#nvidia`, `#ai-hardware`, `#smartphones`, `#tech-industry`

---

<a id="item-tech-news-12"></a>
### [China Tests Earth-Moon Laser Communications](https://www.stdaily.com/web/gdxw/2026-08/26/content_570163.html) ⭐️ 7.0/10

China reportedly established its first bidirectional high-speed laser communication link across the Earth-Moon distance, led by the Technology and Engineering Center for Space Utilization of the Chinese Academy of Sciences. The test used the DRO-A satellite and operated over more than 400,000 kilometers, marking a move for China’s space laser communications work from low Earth orbit into cislunar space. The reported rates were 1.25 Mbps uplink and 100 Mbps downlink. The source compared this with a traditional 5 Mbps microwave downlink, saying an 8K high-definition lunar surface image that would take about 4 to 5 minutes by microwave could be transmitted in about 12 seconds at 100 Mbps laser communication speed.

telegram · zaihuapd · Aug 27, 00:33

**「Background」** Laser communication uses optical beams rather than radio-frequency microwave links, which can support higher data rates but requires precise pointing across long distances. DRO-A refers to a Chinese satellite associated with distant retrograde orbit work in the Earth-Moon region; a DRO is a bounded periodic orbit in cislunar space, and DRO-A was previously reported as part of China’s Earth-Moon communications and measurement efforts.

**「Impact」** If validated and operationalized, the link would give China’s cislunar missions a much faster downlink option for high-volume data such as high-resolution lunar imagery.

<details><summary>References</summary>
<ul>
<li><a href="http://english.csu.cas.cn/lb/202505/t20250509_1042892.html">China Successfully Ushers in New Era of Earth-Moon Space Exploration</a></li>
<li><a href="https://www.china-in-space.com/p/china-begins-operating-first-distant">China Begins Operating First Distant Retrograde Orbit Communications Network</a></li>

</ul>
</details>

**Tags**: `#space-communications`, `#laser-communications`, `#satellite-systems`, `#hardware`, `#china-tech`

---

<a id="item-tech-news-13"></a>
### [Google Updates Gemini Audio With Gemini 3.5 Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/) ⭐️ 7.0/10

Google reportedly updated Gemini Audio with new models including Gemini 3.5 Transcribe, a speech transcription model designed to turn unstructured audio into formatted text. The source says it can automatically recognize more than 85 languages, remove filler words such as “um” and “uh,” and support spoken instructions for editing transcript content. It can learn custom vocabulary, recognize alphanumeric strings such as order numbers, and add word-level timestamps for up to three speakers in prerecorded audio. Google plans to integrate it into Chrome web input fields, Search Live, Gemini Live, Docs, Keep, and Gmail, and to make it available through an API.

telegram · zaihuapd · Aug 27, 01:02

**「Background」** Gemini Audio is Google’s speech-focused Gemini model family for turning spoken input into text and related actions. Transcription systems increasingly combine automatic speech recognition with language-model features such as speaker labeling, punctuation, formatting, vocabulary hints, and downstream editing, which is the context for Google positioning Gemini 3.5 Transcribe as a more intent-aware transcription model.

**「Impact」** Developers and Google app users may gain access to more automated multilingual transcription and cleanup workflows, including custom vocabulary and speaker/time annotations, once the integrations and API are available.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Introducing Gemini 3.5 Transcribe - The Keyword</a></li>
<li><a href="https://deepmind.google/models/gemini-audio/ai-transcription/">Gemini Audio - AI transcription — Google DeepMind</a></li>

</ul>
</details>

**Tags**: `#speech-recognition`, `#Gemini`, `#AI APIs`, `#Google`, `#transcription`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Earnings Drive After-Hours Stock Moves](https://www.cnbc.com/2026/08/26/stocks-making-the-biggest-moves-after-hours-nvda-crm-crwd-urbn-and-more.html) ⭐️ 7.0/10

Several large U.S. stocks moved after hours after earnings and guidance updates, led by Nvidia, which rose 4% after reporting second-quarter adjusted earnings of $2.22 per share and revenue of $96.22 billion versus LSEG analyst estimates of $2.10 per share and $92.17 billion.

rss · CNBC Finance · Aug 26, 21:31

**「Background」** After-hours trading happens after the regular market close, when earnings reports and company forecasts can move shares before the next trading day.

**Tags**: `#earnings`, `#after-hours trading`, `#technology stocks`, `#guidance`, `#equities`

---