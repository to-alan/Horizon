---
layout: default
title: "Horizon Summary: 2026-08-29 (EN)"
date: 2026-08-29
lang: en
---

> From 311 items, 19 important content pieces were selected

---

**Technology News**
1. [ChromeDevTools/chrome-devtools-mcp](#item-tech-news-1) ⭐️ 8.0/10
2. [actions/checkout](#item-tech-news-2) ⭐️ 8.0/10
3. [Xiamen University Tin Perovskite LED Breakthrough](#item-tech-news-3) ⭐️ 8.0/10
4. [Triton 3.8.0 adds new APIs and backend fixes](#item-tech-news-4) ⭐️ 7.0/10
5. [Htmx 4.0](#item-tech-news-5) ⭐️ 7.0/10
6. [Just the rumour of a bug is enough to find an exploit these days](#item-tech-news-6) ⭐️ 7.0/10
7. [GLM-5.3 is now open-weight](#item-tech-news-7) ⭐️ 7.0/10
8. [Bug Rumors Now Trigger Exploit Probing](#item-tech-news-8) ⭐️ 7.0/10
9. [JetBrains releases modern Go agent guidelines](#item-tech-news-9) ⭐️ 7.0/10
10. [lance-format/lance](#item-tech-news-10) ⭐️ 7.0/10
11. [Dynamo Inference Framework](#item-tech-news-11) ⭐️ 7.0/10
12. [Scleral Retina BCI Implant](#item-tech-news-12) ⭐️ 7.0/10
13. [openKylin 3.0 Released](#item-tech-news-13) ⭐️ 7.0/10
14. [Zhipu’s GLM-5.3-Flash Takes Aim at DeepSeek](#item-tech-news-14) ⭐️ 7.0/10
15. [Tiny Image Generator on RP2350](#item-tech-news-15) ⭐️ 7.0/10
16. [Tencent Hunyuan Releases Hy4 Preview](#item-tech-news-16) ⭐️ 7.0/10
17. [Zhipu Opens GLM-5.3](#item-tech-news-17) ⭐️ 7.0/10

**Financial News**
1. [Court rules against prediction markets](#item-finance-news-1) ⭐️ 7.0/10
2. [China Extends Mortgage Term Limit to 40 Years](#item-finance-news-2) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools MCP connects coding agents to live Chrome sessions for browser automation, debugging, and performance analysis.

rss · GitHub Trending - Daily · Aug 28, 12:25

**Tags**: `#Chrome DevTools`, `#Model Context Protocol`, `#AI Coding Agents`, `#Browser Automation`

---

<a id="item-tech-news-2"></a>
### [actions/checkout](https://github.com/actions/checkout) ⭐️ 8.0/10

actions/checkout v7 adds safer default handling for fork pull requests in privileged GitHub Actions workflows.

rss · GitHub Trending - TypeScript Daily · Aug 28, 12:42

**Tags**: `#GitHub Actions`, `#CI/CD Security`, `#Supply Chain Security`, `#Open Source`, `#DevOps`

---

<a id="item-tech-news-3"></a>
### [Xiamen University Tin Perovskite LED Breakthrough](https://www.ithome.com/0/995/889.htm) ⭐️ 8.0/10

On August 28, Xiamen University said a team led by Professor Jie Rongjun from its School of Materials, together with Professor Wang Lixin’s team at Fudan University, made a major advance in lead-free perovskite LEDs, and the work was published in Science on August 27. The researchers identified electrochemical oxidation of tin-based perovskite CsSnI₃ under an electric field as the key cause of LED degradation, linking device failure to carrier-injection imbalance and irreversible oxidation of Sn2+. By combining lattice doping with surface passivation, they improved film stability and optoelectronic performance and built a near-infrared tin perovskite LED with a peak external quantum efficiency of 21.2%. At an initial luminance of 7.1 W·sr⁻¹·m⁻², the device reached a T50 lifetime of more than 900 hours.

rss · IT之家 · Aug 29, 03:26

**「Background」** Perovskite LEDs are light-emitting devices that use perovskite semiconductors in the active layer, and tin-based versions are being explored as lead-free alternatives to lead-containing designs. A long-running challenge for these materials is that tin ions oxidize easily, which makes it difficult to keep efficiency and lifetime high at the same time.

**「Impact」** The result gives perovskite-LED researchers a clearer failure mechanism and a practical route toward more efficient, longer-lived lead-free devices, especially for near-infrared applications.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ime.cas.cn/icac/learning/learning_2/202010/t20201009_5714390.html">中外科学家合作破解钙钛矿稳定性难题--科普知识</a></li>

</ul>
</details>

**Tags**: `#perovskite LEDs`, `#optoelectronics`, `#materials science`, `#semiconductor devices`

---

<a id="item-tech-news-4"></a>
### [Triton 3.8.0 adds new APIs and backend fixes](https://github.com/triton-lang/triton/releases/tag/v3.8.0) ⭐️ 7.0/10

Triton 3.8.0 introduces new public frontend APIs, including \`@triton.aggregate\` and \`@gluon.aggregate\`, a \`descending\` flag for \`tl.topk\`, tuple support for tensor descriptors, and interpreter support for \`tl.dot\_scaled\`. The release also adds autotuning listener output, deterministic JIT dependency cache keys, and several correctness fixes for division, atomics, NaN handling, block-pointer padding, and Python 3.14 annotations. On the compiler and backend side, it updates the pinned LLVM revision, expands multi-CTA support across layout conversion, reductions, gather/scatter, TMA, and multicast, and adds new debugging and sanitizer capabilities such as FpSan, GSan, and broader ConSan coverage. The notes also highlight substantial AMD/HIP work for gfx1250/CDNA 5, including tensor data movement, WMMA and atomics updates, and warp-pipelining improvements.

github · warrendeng · Aug 28, 18:25

**「Background」** Triton is an open-source language and compiler stack for writing custom GPU kernels, especially in machine learning workloads. Its releases typically matter to developers who need new kernel-building primitives, backend support for newer GPU features, and fixes that affect correctness or performance.

**「Impact」** Developers using Triton for GPU kernels gain new frontend APIs and broader backend support, while also getting several compiler and runtime fixes that can improve correctness and debugging.

**Tags**: `#triton`, `#gpu-compilers`, `#ai-infrastructure`, `#open-source`, `#machine-learning`

---

<a id="item-tech-news-5"></a>
### [Htmx 4.0](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 7.0/10

htmx 4.0 is released, drawing substantial community discussion around the next major version of the library.

hackernews · rmsaksida · Aug 28, 13:28 · [Discussion](https://news.ycombinator.com/item?id=49478178)

**Tags**: `#htmx`, `#web development`, `#frontend`, `#release`, `#open source`

---

<a id="item-tech-news-6"></a>
### [Just the rumour of a bug is enough to find an exploit these days](https://anil.recoil.org/notes/rumour-is-the-exploit) ⭐️ 7.0/10

A discussion of how bug rumors can rapidly lead to exploit attempts, and how that is affecting open-source security work.

hackernews · avsm · Aug 28, 15:58 · [Discussion](https://news.ycombinator.com/item?id=49480466)

**Tags**: `#security`, `#exploit-development`, `#vulnerability-disclosure`, `#open-source-maintenance`, `#AI-assisted-development`

---

<a id="item-tech-news-7"></a>
### [GLM-5.3 is now open-weight](https://huggingface.co/zai-org/GLM-5.3) ⭐️ 7.0/10

GLM-5.3 has been released as open weights, drawing notable interest from the AI community.

hackernews · jeudesprits · Aug 28, 15:20 · [Discussion](https://news.ycombinator.com/item?id=49479878)

**Tags**: `#open-weight models`, `#foundation models`, `#LLMs`, `#AI release`

---

<a id="item-tech-news-8"></a>
### [Bug Rumors Now Trigger Exploit Probing](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 7.0/10

Simon Willison highlights a post by Anil Madhavapeddy, a Cambridge computer science professor and core OCaml compiler maintainer, describing how security issues in OCaml projects are attracting attempted exploits within minutes of patches being shared for discussion. Madhavapeddy says one site began seeing probes for percent-encoded traversal sequences about ten minutes after the patch discussion, suggesting automated watchers are tracking public repositories closely. He argues that modern coding agents can use even a vague hint of a bug to uncover the flaw quickly, and says he has demonstrated this with his own agents, including switching to DeepSeek V4 Pro when Claude Fable refused the task. The post warns that this pace may not fit current open-source embargo practices and that communities may need new disclosure processes to stay safe.

rss · Simon Willison · Aug 28, 22:12

**「Background」** Open-source security fixes are often discussed privately first so maintainers can patch a vulnerability before publishing details, a practice meant to reduce the chance of immediate exploitation. This piece is about how automated watchers and coding agents can monitor public repositories for even small hints of a bug, which can compress the window between disclosure and probing to minutes.

**「Impact」** Open-source maintainers may need faster disclosure and patching workflows because public bug discussion can now be followed by exploit probing within minutes.

<details><summary>References</summary>
<ul>
<li><a href="https://anil.recoil.org/notes/rumour-is-the-exploit">Just a rumour of a bug is enough to find a security exploit ...</a></li>
<li><a href="https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/">Just a rumour of a bug is enough to find a security exploit these days</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI agents`, `#vulnerability disclosure`, `#open source`

---

<a id="item-tech-news-9"></a>
### [JetBrains releases modern Go agent guidelines](https://github.com/JetBrains/go-modern-guidelines) ⭐️ 7.0/10

JetBrains has published the JetBrains/go-modern-guidelines repository, which packages guidance for AI coding agents to write modern, idiomatic Go. The repository says the skill covers useful language and standard-library features from Go 1.0 through Go 1.27, and it tailors its recommendations to the project&\#x27;s Go version from go.mod. Examples include using max\(a, b\), slices.Contains, cmp.Or\(a, b, c\), new\(42\), and errors.AsType\[T\]\(err\) instead of older manual patterns. The guidelines are available for Junie, Claude Code, Codex, Cursor, and other agents via skills.sh, and the CLI targets Go 1.25 or newer while relying on automatic toolchain switching on older installs when GOTOOLCHAIN=auto is enabled.

rss · GitHub Trending - Daily · Aug 28, 12:25

**「Background」** Go adds new language and standard-library features over time, so code written for older versions can miss newer idioms even when it still works. JetBrains says these guidelines are meant to complement the Go team&\#x27;s own modernize analyzer, which helps update code toward newer patterns.

**「Impact」** For users of supported coding agents, the repository provides a concrete way to steer generated Go toward newer idioms and reduce cleanup after code generation.

**Tags**: `#Go`, `#AI Coding Agents`, `#Software Engineering`, `#Developer Tools`

---

<a id="item-tech-news-10"></a>
### [lance-format/lance](https://github.com/lance-format/lance) ⭐️ 7.0/10

Lance is an open lakehouse format designed to improve multimodal AI data storage, retrieval, search, and versioning across common Python and analytics ecosystems.

rss · GitHub Trending - Rust Daily · Aug 28, 12:40

**Tags**: `#Multimodal AI`, `#Data Infrastructure`, `#Vector Search`, `#Lakehouse`, `#Rust`

---

<a id="item-tech-news-11"></a>
### [Dynamo Inference Framework](https://github.com/ai-dynamo/dynamo) ⭐️ 7.0/10

ai-dynamo/dynamo is an Apache-licensed, open-source framework for datacenter-scale distributed AI inference serving. The project describes Dynamo as an orchestration layer above inference engines such as SGLang, TensorRT-LLM, and vLLM, turning them into a coordinated multi-node system rather than replacing them. Its key capabilities include disaggregated serving, intelligent KV-aware routing, multi-tier KV caching, automatic scaling, and fast replica cold starts. The README says it is built in Rust for performance and Python for extensibility, and it targets LLM, reasoning, multimodal, and video generation workloads.

rss · GitHub Trending - Rust Daily · Aug 28, 12:40

**「Background」** Inference serving systems run machine learning models in production and need to balance latency, throughput, and cost. At datacenter scale, operators often coordinate multiple GPUs or nodes and separate prefill from decode to use hardware more efficiently. KV-aware routing matters because it can reuse cached context instead of recomputing it for every request.

**「Impact」** Teams running large-model inference across multiple GPUs or nodes now have an open-source orchestration layer aimed at improving throughput, latency, and scaling across supported backends.

**Tags**: `#AI Inference`, `#Distributed Systems`, `#MLOps`, `#Rust`, `#Open Source`

---

<a id="item-tech-news-12"></a>
### [Scleral Retina BCI Implant](https://www.ithome.com/0/995/870.htm) ⭐️ 7.0/10

Wuhan University Renmin Hospital says it has carried out the world’s first clinical use of a high-resolution semi-invasive retinal brain-computer interface, and that a 60-year-old man who had been blind for four years from retinitis pigmentosa regained partial visual function. On July 8, the team implanted a stimulation chip into the patient’s sclera, or white of the eye, without penetrating the eyeball or using external wires. By August 26, the patient reportedly could recognize and write digits, Chinese characters, and English letters, grasp objects, and walk independently with smart glasses. The hospital says the device is wireless, can be fully removed or upgraded, and avoids the higher-risk intraocular surgery used in many earlier approaches.

rss · IT之家 · Aug 29, 02:09

**「Background」** Retinal brain-computer interfaces try to restore vision by turning camera-captured images into electrical signals that can stimulate surviving retinal neurons when photoreceptors have been damaged, as in retinitis pigmentosa. Earlier experimental systems often used invasive eye surgery to place electrodes inside the eye, so a scleral, non-penetrating design is notable because it aims to lower surgical risk while still reaching the visual pathway.

**「Impact」** If validated beyond this single case, the approach could give patients with preserved optic nerves a less invasive and reversible path to visual prosthesis than fully intraocular implants.

<details><summary>References</summary>
<ul>
<li><a href="https://jxt.hubei.gov.cn/bmdt/rdjj/202608/t20260827_6002616.shtml">全 球 首 例 临 床 成功！ 失明多年患者在 汉 重见光明-湖北省经济和信息化厅</a></li>
<li><a href="https://kjj.wuhan.gov.cn/xwzx_8/kjspxw/202608/t20260828_2839956.html">科技新闻</a></li>

</ul>
</details>

**Tags**: `#脑机接口`, `#视网膜植入`, `#医疗硬件`, `#神经工程`, `#生物医学`

---

<a id="item-tech-news-13"></a>
### [openKylin 3.0 Released](https://www.ithome.com/0/995/859.htm) ⭐️ 7.0/10

OpenAtom openKylin 3.0 has been officially released, with the project claiming a major platform refresh centered on a cross-generation move from Linux 6.6 to Linux 7.0. The release also updates more than 180 core components and aligns the base stack with GCC 15, glibc 2.42, LLVM 22, and JDK 25. Security and platform changes include NIST post-quantum algorithms ML-KEM, ML-DSA, and SLH-DSA through openHiTLS, TPM-backed trusted boot, Rust For Linux support, and initial Rust rewrites of tools such as wget and time. openKylin 3.0 also adds an AI-oriented system architecture, new multimodal desktop features in UKUI 4.24, and support across x86, ARM, RISC-V, and LoongArch.

rss · IT之家 · Aug 29, 01:19

**「Background」** openKylin is an open-source Linux distribution project under the OpenAtom Open Source Foundation. Like other major distribution releases, it combines kernel, toolchain, desktop, and hardware-support updates into a single platform version. Rust For Linux refers to efforts to write kernel components in Rust to reduce memory-safety bugs, while post-quantum cryptography is intended to prepare systems for future attack models.

**「Impact」** The release gives supported openKylin users and developers a newer base system, new cryptographic primitives, and broader architecture support, while giving kernel and application developers an environment that can target Rust and AI-integrated workflows.

**Tags**: `#openKylin`, `#Linux 内核`, `#Rust`, `#后量子密码`, `#国产操作系统`

---

<a id="item-tech-news-14"></a>
### [Zhipu’s GLM-5.3-Flash Takes Aim at DeepSeek](https://www.36kr.com/p/3958937888609920) ⭐️ 7.0/10

Zhipu AI has released GLM-5.3-Flash, the first native multimodal model in its GLM-5 series, and the article says it is the same model that appeared anonymously as &quot;Ox Alpha&quot; on OpenRouter. Zhipu says it scores 57 on the Artificial Analysis Intelligence Index, ahead of DeepSeek V4 Pro&\#x27;s 53, and claims it can match Claude Opus 4.8 on some benchmarks. The model is priced aggressively at RMB 0.8 per million input tokens and RMB 2.8 per million output tokens, with a two-week half-price promotion and separate cache-hit pricing, putting it directly against DeepSeek&\#x27;s cost advantage. The article argues that GLM-5.3-Flash is especially aimed at agent and coding workloads, but that its real price edge depends on how much of the traffic is cache-hit versus cache-miss.

rss · 36氪 - 24小时热榜 · Aug 28, 10:15

**「Background」** DeepSeek became known for combining strong model performance with very low API prices, which made it a benchmark for value-conscious developers. In multimodal systems, the model can handle inputs beyond text, and in agent workflows, repeated prompts and shared context make cache-hit pricing especially important.

**「Impact」** Developers who run frequent agent or coding workloads now have another low-cost multimodal model to consider, but the effective savings will vary depending on cache-hit usage and whether Zhipu&\#x27;s short-lived discount is still active.

**Tags**: `#artificial-intelligence`, `#large-language-models`, `#multimodal-models`, `#AI-industry`, `#benchmarking`

---

<a id="item-tech-news-15"></a>
### [Tiny Image Generator on RP2350](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 7.0/10

A Reddit project post from /u/cpldcpu describes a tiny latent flow transformer that runs image generation on an RP2350 microcontroller. The model is 2.4 to 4 million parameters, quantized to int8, and can generate 128x128 face images entirely on the microcontroller in about 20 seconds for the longest run. It uses 12 layers with AdaLN-Zero conditioning, supports classifier-free guidance, and streams weights from flash over DMA while the previous layer is computed. The inference engine also uses ReLU^2 activations to increase sparsity and skip some calculations, after extensive ablation work to make the design fit the hardware.

reddit · r/MachineLearning · /u/cpldcpu · Aug 28, 19:48

**「Background」** A latent flow transformer is a generative model that works in a compressed latent space instead of directly operating on full images. Microcontrollers like the RP2350 have very limited RAM and compute, so running even small image-generation models usually requires aggressive quantization, memory streaming, and other efficiency tricks.

**「Impact」** The post shows that 128x128 image generation can be made to run on an RP2350-class microcontroller when the model is small, int8-quantized, and optimized for streamed inference.

**Tags**: `#embedded-ml`, `#image-generation`, `#microcontrollers`, `#model-quantization`, `#edge-ai`

---

<a id="item-tech-news-16"></a>
### [Tencent Hunyuan Releases Hy4 Preview](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 7.0/10

Tencent reportedly released Hy4 preview on August 28, 2026, describing it as its strongest open-source Hunyuan model to date. The model is said to have 770B total parameters, 49B active parameters, and a 1M-token context window, with a focus on long-running software engineering tasks, office-document workflows, and scientific research. The source says Hy4 preview is available through Tencent Cloud, GitHub, Hugging Face, ModelScope, AtomGit, OpenRouter, and other channels. In a blind evaluation of 203 engineering tasks, it reportedly scored 2.99, slightly ahead of GLM-5.3 at 2.92 and Kimi K3 at 2.94, with API pricing listed at $0.834 per 1M input tokens and $2.501 per 1M output tokens.

telegram · zaihuapd · Aug 28, 06:11

**「Background」** Hy4 preview is Tencent Hunyuan’s latest Mixture-of-Experts flagship model, and “preview” indicates an early release intended for wider testing and feedback. Models with very long context windows can keep much more code, text, or research material in view at once, which is why they are often positioned for software engineering, document work, and analysis tasks.

**「Impact」** Developers evaluating open-source long-context models may gain another large Hunyuan option for coding, document, and research workloads, but the reported benchmark edge is small and comes from a brief repost rather than independently verified results.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aibase.com/news/30694">Tencent Hunyuan launches open - source flagship model ...</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent - Hunyuan / Hy 4 - preview · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI models`, `#open source`, `#Tencent Hunyuan`, `#software engineering`, `#LLM benchmarks`

---

<a id="item-tech-news-17"></a>
### [Zhipu Opens GLM-5.3](http://z.ai/) ⭐️ 7.0/10

Zhipu AI has released GLM-5.3 as an open model aimed at agentic programming and network defense, with weights available for download, local use, and customization. The company says GLM-5.3 shares the same base model as GLM-5.2, and that all improvements come from post-training rather than a new foundation model. It reports stronger complex coding and long-horizon task performance, citing Terminal Bench 2.1 at 88.2 and DeepSWE at 66.9, both above GLM-5.2. The model is distributed under a custom GLM-5.3 License that allows individuals and small or medium businesses to use, fine-tune, and commercialize it, but requires companies with more than $10 billion in annual revenue that offer model-as-a-service to pass a Z.AI security review first.

telegram · zaihuapd · Aug 28, 15:32

**「Background」** GLM-5.3 is part of Zhipu AI’s GLM-5 family, which is positioned around reasoning, coding, and agentic capabilities. In this context, &quot;open&quot; means the model weights can be downloaded and run by users instead of being accessible only through a hosted API, which is why the release matters for teams that want local deployment or customization. Agentic programming refers to using a model to handle multi-step coding tasks with tools, while network defense points to cybersecurity uses rather than general-purpose chat.

**「Impact」** Teams working on coding agents or defensive security tools can adopt and customize GLM-5.3 under the stated license, while very large model-service providers face an added security-review requirement before commercial deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://models.dev/models/zhipuai/glm-5.3/">GLM - 5 . 3 pricing, providers, and specs | Models .dev</a></li>
<li><a href="https://glm5.net/">GLM - 5 | Zhipu AI &#x27;s Next-Generation Large Language Model</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#open source`, `#agentic coding`, `#cybersecurity`, `#AI licensing`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Court rules against prediction markets](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 7.0/10

The 9th U.S. Circuit Court of Appeals ruled against Kalshi, Crypto.com and Robinhood, saying sports-related event contracts are not federally regulated swaps and refusing to block Nevada from stopping their operations. The decision deepens a split with the 3rd Circuit over whether states or the CFTC control these markets, making a Supreme Court review more likely.

rss · CNBC Finance · Aug 29, 02:23

**「background」** The dispute is over whether sports-related prediction contracts are swaps regulated by the Commodity Futures Trading Commission or gambling products that states can police, and the 9th Circuit ruling clashes with a 3rd Circuit decision on the same issue.

<details><summary>References</summary>
<ul>
<li><a href="https://predictionnews.com/story/robinhood-kalshi-and-crypto-com-lose-appeals-for-injunctive-relief-against-nevad-c5361eb2">Ninth Circuit rejects Robinhood, Kalshi, and Crypto.com bid ...</a></li>

</ul>
</details>

**Tags**: `#prediction markets`, `#CFTC`, `#gaming regulation`, `#sports betting`, `#appeals court`

---

<a id="item-finance-news-2"></a>
### [China Extends Mortgage Term Limit to 40 Years](https://news.ifeng.com/c/8vxm6huJOMR) ⭐️ 7.0/10

China’s central bank and financial regulator said they will extend the maximum term for personal housing loans from 30 years to 40 years. The new limit is in a joint notice on reforming housing credit management, and the final loan term will still be agreed between the buyer and the commercial bank.

telegram · zaihuapd · Aug 28, 12:16

**「Background」** On 28 August, the People’s Bank of China and the National Financial Regulatory Administration jointly issued an opinion on reforming real-estate credit management and supporting a new housing development model.

<details><summary>References</summary>
<ul>
<li><a href="https://m.163.com/dy/article/L5ELRKSM0512B07B.html">两部门：将 个 人 住 房 贷 款 期 限 由 最 长 30 年 延 长 至 最 长 40 年 _手机网易网</a></li>

</ul>
</details>

**Tags**: `#房地产政策`, `#住房贷款`, `#金融监管`, `#银行`

---