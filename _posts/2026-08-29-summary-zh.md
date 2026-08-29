---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 311 条内容中筛选出 19 条重要资讯。

---

**科技新闻**
1. [ChromeDevTools/chrome-devtools-mcp](#item-tech-news-1) ⭐️ 8.0/10
2. [actions/checkout](#item-tech-news-2) ⭐️ 8.0/10
3. [厦大锡基钙钛矿 LED 突破](#item-tech-news-3) ⭐️ 8.0/10
4. [Triton 3.8.0 发布](#item-tech-news-4) ⭐️ 7.0/10
5. [Htmx 4.0](#item-tech-news-5) ⭐️ 7.0/10
6. [Just the rumour of a bug is enough to find an exploit these days](#item-tech-news-6) ⭐️ 7.0/10
7. [GLM-5.3 is now open-weight](#item-tech-news-7) ⭐️ 7.0/10
8. [漏洞传闻也会引来利用尝试](#item-tech-news-8) ⭐️ 7.0/10
9. [JetBrains 发布现代 Go 指南](#item-tech-news-9) ⭐️ 7.0/10
10. [lance-format/lance](#item-tech-news-10) ⭐️ 7.0/10
11. [Dynamo 分布式推理框架](#item-tech-news-11) ⭐️ 7.0/10
12. [巩膜外视网膜脑机接口植入](#item-tech-news-12) ⭐️ 7.0/10
13. [openKylin 3.0 发布](#item-tech-news-13) ⭐️ 7.0/10
14. [智谱 GLM-5.3-Flash 挑战 DeepSeek](#item-tech-news-14) ⭐️ 7.0/10
15. [RP2350 上的微型图像生成模型](#item-tech-news-15) ⭐️ 7.0/10
16. [腾讯混元发布 Hy4 preview](#item-tech-news-16) ⭐️ 7.0/10
17. [智谱开源 GLM-5.3](#item-tech-news-17) ⭐️ 7.0/10

**财经新闻**
1. [美国上诉法院裁定不利于预测市场](#item-finance-news-1) ⭐️ 7.0/10
2. [个人住房贷款期限延长](#item-finance-news-2) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools MCP connects coding agents to live Chrome sessions for browser automation, debugging, and performance analysis.

rss · GitHub Trending - Daily · 8月28日 12:25

**标签**: `#Chrome DevTools`, `#Model Context Protocol`, `#AI Coding Agents`, `#Browser Automation`

---

<a id="item-tech-news-2"></a>
### [actions/checkout](https://github.com/actions/checkout) ⭐️ 8.0/10

actions/checkout v7 adds safer default handling for fork pull requests in privileged GitHub Actions workflows.

rss · GitHub Trending - TypeScript Daily · 8月28日 12:42

**标签**: `#GitHub Actions`, `#CI/CD Security`, `#Supply Chain Security`, `#Open Source`, `#DevOps`

---

<a id="item-tech-news-3"></a>
### [厦大锡基钙钛矿 LED 突破](https://www.ithome.com/0/995/889.htm) ⭐️ 8.0/10

厦门大学材料学院解荣军教授团队联合复旦大学王利新教授团队，在无铅锡基钙钛矿 LED 研究上取得新进展，并于 8 月 27 日在《科学》发表相关成果。研究首次阐明，锡基钙钛矿 CsSnI₃ 在电场作用下发生电化学氧化，是器件发光衰减的关键机制。团队据此提出晶格掺杂与表面钝化协同策略，显著提升了薄膜结构稳定性和光电性能，制备出峰值外量子效率达 21.2%、在初始辐亮度 7.1 W·sr⁻¹·m⁻² 下 T50 超过 900 小时的近红外锡基钙钛矿 LED。IT 之家称，这一结果表明该类低毒、可溶液加工器件在效率和寿命上都取得了重要提升。

rss · IT之家 · 8月29日 03:26

**「背景」** 钙钛矿 LED 是以卤化物钙钛矿为发光层的器件，因可溶液加工、潜在效率高而被视为新一代显示和近红外光源候选，但材料稳定性一直是关键瓶颈。锡基方案主要是为了避开含铅材料的毒性问题，不过二价锡容易氧化，通常会同时拉低器件效率和工作寿命。

**「影响」** 这项工作为无铅锡基钙钛矿 LED 提供了明确的失效机理和可操作的稳定化路径，并把器件寿命提升到超过 900 小时的水平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ime.cas.cn/icac/learning/learning_2/202010/t20201009_5714390.html">中外科学家合作破解钙钛矿稳定性难题--科普知识</a></li>

</ul>
</details>

**标签**: `#perovskite LEDs`, `#optoelectronics`, `#materials science`, `#semiconductor devices`

---

<a id="item-tech-news-4"></a>
### [Triton 3.8.0 发布](https://github.com/triton-lang/triton/releases/tag/v3.8.0) ⭐️ 7.0/10

Triton 发布了 v3.8.0，带来面向 GPU 内核开发的多项前端、编译器和后端更新。前端方面，\`@triton.aggregate\` 和 \`@gluon.aggregate\` 现在成为公开 API，\`tl.topk\` 新增 \`descending\` 参数，张量描述符可作为元组形式的内核参数传递，解释器也加入了对 \`tl.dot\_scaled\` 的支持。编译与运行时方面，这一版扩展了 multi-CTA 对布局转换、归约、gather/scatter、TMA 和 multicast 的支持，并加入了 FpSan、GSan 和 ConSan 等调试/检测能力，同时修复了若干正确性问题，包括 LLVM 相关的 GFX950 BF16 误编译。发布说明还提到 JIT 缓存键的确定性、自动调优监听器、Python 3.14 注解处理和 block-pointer 载入零填充等改进。

github · warrendeng · 8月28日 18:25

**「背景」** Triton 是用于编写高性能 GPU 内核的编译器和 Python 领域特定语言，常见于 AI 和机器学习基础设施。每个版本通常会同时影响前端 API、编译优化、后端代码生成以及调试工具，因此对依赖 Triton 的开发者来说，版本更新往往会直接影响可用能力和内核正确性。

**「影响」** 使用 Triton 编写 NVIDIA 和 AMD GPU 内核的开发者将获得更多公开 API、覆盖更广的后端能力，以及更强的编译期和运行期错误检测工具。

**标签**: `#triton`, `#gpu-compilers`, `#ai-infrastructure`, `#open-source`, `#machine-learning`

---

<a id="item-tech-news-5"></a>
### [Htmx 4.0](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 7.0/10

htmx 4.0 is released, drawing substantial community discussion around the next major version of the library.

hackernews · rmsaksida · 8月28日 13:28 · [社区讨论](https://news.ycombinator.com/item?id=49478178)

**标签**: `#htmx`, `#web development`, `#frontend`, `#release`, `#open source`

---

<a id="item-tech-news-6"></a>
### [Just the rumour of a bug is enough to find an exploit these days](https://anil.recoil.org/notes/rumour-is-the-exploit) ⭐️ 7.0/10

A discussion of how bug rumors can rapidly lead to exploit attempts, and how that is affecting open-source security work.

hackernews · avsm · 8月28日 15:58 · [社区讨论](https://news.ycombinator.com/item?id=49480466)

**标签**: `#security`, `#exploit-development`, `#vulnerability-disclosure`, `#open-source-maintenance`, `#AI-assisted-development`

---

<a id="item-tech-news-7"></a>
### [GLM-5.3 is now open-weight](https://huggingface.co/zai-org/GLM-5.3) ⭐️ 7.0/10

GLM-5.3 has been released as open weights, drawing notable interest from the AI community.

hackernews · jeudesprits · 8月28日 15:20 · [社区讨论](https://news.ycombinator.com/item?id=49479878)

**标签**: `#open-weight models`, `#foundation models`, `#LLMs`, `#AI release`

---

<a id="item-tech-news-8"></a>
### [漏洞传闻也会引来利用尝试](https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/) ⭐️ 7.0/10

Simon Willison 转述了 Cambridge 的 Anil Madhavapeddy 关于 OCaml 项目的观察：一旦修补信息在公开仓库中出现，安全探测往往会在几分钟内开始，文中提到大约 10 分钟后网站就收到了针对百分号编码目录穿越序列的探测。Anil 认为，现代编码代理和自动化监视器已经强到只凭“可能有新漏洞”的线索就能反推出可利用点，他还表示自己曾用代理复现这一点，并在 Claude Fable 拒绝任务后改用 DeepSeek V4 Pro。文章因此指出，现有开源漏洞披露和保密窗口的流程可能已经跟不上这种发现与利用速度，需要重新设计社区的安全协作方式。rclone 维护者 Nick Craig-Wood 也在 Hacker News 里说，项目近一个月收到的安全披露超过 40 条，而前 10 年只有约 20 条，并称 GitHub 的 CVE 分配时间已从 2-3 天拉长到 3-4 周。

rss · Simon Willison · 8月28日 22:12

**「背景」** 这篇文章讨论的是开源项目常见的漏洞披露流程：维护者往往会先私下协调修复，再在准备好发布时公开补丁，以便争取一段相对安全的窗口期。文中提到的“自动化 watcher”和编码代理，指的是会持续监视公开仓库、并尝试根据新补丁或漏洞线索自动推断可利用点的工具；作者举到 OCaml 项目和 rclone 的经验，说明这种从“有风声”到“被尝试利用”的时间已经被压缩到几分钟内。

**「影响」** 对开源维护者来说，公开讨论补丁和漏洞细节现在可能很快就会引来自动化探测甚至利用尝试，因此需要更快的披露、修复和协调流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://anil.recoil.org/notes/rumour-is-the-exploit">Just a rumour of a bug is enough to find a security exploit ...</a></li>
<li><a href="https://simonwillison.net/2026/Aug/28/just-a-rumour-of-a-bug/">Just a rumour of a bug is enough to find a security exploit these days</a></li>

</ul>
</details>

**标签**: `#security`, `#AI agents`, `#vulnerability disclosure`, `#open source`

---

<a id="item-tech-news-9"></a>
### [JetBrains 发布现代 Go 指南](https://github.com/JetBrains/go-modern-guidelines) ⭐️ 7.0/10

JetBrains 发布了仓库 JetBrains/go-modern-guidelines，用来帮助 AI 编码代理生成更现代、符合惯例的 Go 代码。该指南覆盖 Go 1.0 到 Go 1.27 的常用特性，并会根据项目的 go.mod 识别 Go 版本，只使用该版本可用的语言特性和标准库新增能力。文档给出的示例包括用 max\(a, b\) 代替 if-else、用 slices.Contains 代替手写循环、用 cmp.Or\(a, b, c\) 代替一串 nil 检查，以及 Go 1.26 的 new\(42\) 和 errors.AsType\[T\]\(err\)。JetBrains 还说明该指南与 Go 团队的 modernize 分析器方向一致，适用于 Junie、Claude Code、Codex、Cursor 以及通过 skills.sh 接入的其他代理。

rss · GitHub Trending - Daily · 8月28日 12:25

**「背景」** AI 编码代理常会生成过时写法，一方面是训练数据对新特性覆盖不足，另一方面是模型更容易复用训练集中高频但较旧的模式。Go 社区一直强调用更新的语言和标准库能力来简化代码，而 modernize 分析器就是用来把旧代码自动迁移到更现代写法的工具。

**「影响」** 对使用这些代理编写 Go 代码的开发者来说，这套指南提供了一个可直接参考的规则层，有助于减少过时惯用法和后续返工。

**标签**: `#Go`, `#AI Coding Agents`, `#Software Engineering`, `#Developer Tools`

---

<a id="item-tech-news-10"></a>
### [lance-format/lance](https://github.com/lance-format/lance) ⭐️ 7.0/10

Lance is an open lakehouse format designed to improve multimodal AI data storage, retrieval, search, and versioning across common Python and analytics ecosystems.

rss · GitHub Trending - Rust Daily · 8月28日 12:40

**标签**: `#Multimodal AI`, `#Data Infrastructure`, `#Vector Search`, `#Lakehouse`, `#Rust`

---

<a id="item-tech-news-11"></a>
### [Dynamo 分布式推理框架](https://github.com/ai-dynamo/dynamo) ⭐️ 7.0/10

ai-dynamo/dynamo 发布了一个 Apache 2.0 许可的开源框架，定位为“数据中心规模的分布式推理服务栈”。它不是替代 SGLang、TensorRT-LLM 或 vLLM，而是作为它们之上的编排层，把多个节点和 GPU 组织成协同工作的推理系统。项目强调解耦式服务、KV 感知路由、多层 KV 缓存、自动扩缩容和快速冷启动，目标是同时提升吞吐并降低延迟，适用于 LLM、推理、 多模态和视频生成等工作负载。仓库还说明其核心以 Rust 实现以追求性能，同时用 Python 提供扩展性。

rss · GitHub Trending - Rust Daily · 8月28日 12:40

**「背景」** 推理服务是把训练完成的大模型部署到线上并对外提供响应的系统，通常需要处理路由、缓存、并发和资源调度。所谓解耦式服务，通常是把预填充和解码等阶段分开扩展，以便更灵活地利用 GPU 和降低成本。

**标签**: `#AI Inference`, `#Distributed Systems`, `#MLOps`, `#Rust`, `#Open Source`

---

<a id="item-tech-news-12"></a>
### [巩膜外视网膜脑机接口植入](https://www.ithome.com/0/995/870.htm) ⭐️ 7.0/10

据武汉大学人民医院消息，因视网膜色素变性彻底失明 4 年的 60 岁患者邱先生，于 7 月 8 日接受了半侵入式视网膜脑机接口植入，芯片被放置在眼白外侧的巩膜微小囊袋中，整个过程不穿透眼球、也没有外接导线。术后一个多月系统开机后，他先能辨认并写下数字 1 到 10；截至 8 月 26 日，官方称其在开机仅一周内已能辨认和书写汉字、英文字母，抓取物品，并借助智能眼镜独立行走。院方表示，经公开文献检索，这是全球首例高分辨率半侵入式视网膜脑机接口临床应用获得安全有效成果的病例。该方案通过无线电磁耦合，把智能眼镜采集的信息转成电信号，再由植入芯片刺激眼底残存神经节细胞，主打微创、可逆和可迭代更换。

rss · IT之家 · 8月29日 02:09

**「背景」** 视网膜脑机接口，也常被称为“电子视网膜”，是把外部视觉信息转换为电信号，再刺激视网膜或相关神经通路，帮助部分失明患者恢复有限视觉的一类技术。与把电极直接放入眼内的全侵入方案相比，这类“半侵入式”路径把芯片放在眼白外侧，目标是降低手术创伤、减少并发症风险，并保留设备可取出和迭代更换的可能。

**「影响」** 如果后续随访和更多病例能验证这一结果，这种不穿透眼球、可完整取出的植入路径，可能为仍保留视神经的失明患者提供风险更低的人工视觉方案。当前证据仍只来自单个病例和院方通报。

**标签**: `#脑机接口`, `#视网膜植入`, `#医疗硬件`, `#神经工程`, `#生物医学`

---

<a id="item-tech-news-13"></a>
### [openKylin 3.0 发布](https://www.ithome.com/0/995/859.htm) ⭐️ 7.0/10

据开放原子开源基金会，OpenAtom openKylin 3.0 已正式发布。此次版本把系统内核从 Linux 6.6 跨代升级到 Linux 7.0，并对 180 余个核心组件、GCC 15、glibc 2.42、LLVM 22 和 JDK 25 等基础软件进行了更新。官方还在系统中加入 NIST 三大后量子密码标准、通过 openHiTLS 和 TPM 构建可信启动链，支持 Rust For Linux，并将 AI 能力、语音输入、隔空手势和屏幕朗读等功能纳入新版本。openKylin 3.0 还宣称同源支持 x86、ARM、RISC-V 和 LoongArch 四种架构，覆盖桌面、移动端、服务器和部分 AI 终端场景。

rss · IT之家 · 8月29日 01:19

**「背景」** openKylin 是由开放原子开源基金会推动的国产 Linux 发行版项目，主要面向桌面和多架构生态适配。Linux 内核、编译工具链和密码套件的升级，通常会直接影响系统兼容性、硬件支持和开发者的移植成本。

**「影响」** 对使用 openKylin 的开发者和部署方而言，这一版本把新内核、Rust 驱动支持、后量子密码和多架构适配集中到同一发行版中，便于在国产 Linux 生态里进行统一验证和应用移植。

**标签**: `#openKylin`, `#Linux 内核`, `#Rust`, `#后量子密码`, `#国产操作系统`

---

<a id="item-tech-news-14"></a>
### [智谱 GLM-5.3-Flash 挑战 DeepSeek](https://www.36kr.com/p/3958937888609920) ⭐️ 7.0/10

智谱 AI 发布了 GLM-5.3-Flash，这被描述为 GLM-5 系列首个原生多模态模型，也对应此前在 OpenRouter 上匿名出现的 Ox Alpha。文中称它在 Artificial Analysis Intelligence Index 上得分 57，高于 DeepSeek V4 Pro 正式版的 53，并且官方表示在部分口径上可对标 Claude Opus 4.8。定价方面，它的未命中缓存输入和输出分别为每百万 Token 0.8 元和 2.8 元，且提供两周限时半价优惠，但在缓存命中场景下，按文中给出的价格，它并不总比 DeepSeek 便宜。文章还称该模型可处理文本、图片和视频输入，支持最长 104 万 Token 上下文，并依托国产芯片和专用推理引擎降低成本。

rss · 36氪 - 24小时热榜 · 8月28日 10:15

**「背景」** 多模态模型可以同时处理文本、图像和视频等不同类型输入，适合更复杂的交互和代理式应用。Agent 场景里，同一套系统提示、工具定义和历史上下文会被反复调用，因此缓存命中价格往往会显著影响最终账单。

**「影响」** 对于高频调用、且缓存命中率很高的 Agent 开发者来说，GLM-5.3-Flash 的账单未必比 DeepSeek 更低，选型需要同时看未命中和缓存命中两类价格。

**标签**: `#artificial-intelligence`, `#large-language-models`, `#multimodal-models`, `#AI-industry`, `#benchmarking`

---

<a id="item-tech-news-15"></a>
### [RP2350 上的微型图像生成模型](https://www.reddit.com/r/MachineLearning/comments/1w10tax/i_implemented_a_very_tiny_image_generation_model/) ⭐️ 7.0/10

一位 Reddit 用户展示了一个在 RP2350 微控制器上运行的超小型图像生成模型，可生成 128×128 的人脸图像。该模型参数量为 240 万到 400 万，经过 int8 量化后，最长一次生成大约需要 20 秒，并可将结果显示到显示器或通过 USB 传输。模型采用 12 层 latent flow transformer，并使用 AdaLN-Zero 进行条件控制，同时支持 CFG，以明显提升生成质量。推理引擎还通过 DMA 从闪存流式读取权重，并利用 Relu² 带来的稀疏性跳过部分计算。作者表示，为了把模型压到这种规模并保持可用效果，做了很多消融实验。

reddit · r/MachineLearning · /u/cpldcpu · 8月28日 19:48

**「背景」** RP2350 是一类资源非常受限的微控制器，通常不适合承载图像生成这类计算密集型任务。latent flow transformer 属于生成式模型架构之一，而 AdaLN-Zero、CFG 和量化、稀疏推理则是常见的模型压缩与推理加速手段。

**「影响」** 这一项目表明，经过量化、稀疏化和权重流式加载后，微控制器也能运行小型图像生成模型，但速度仍然很慢，且结果只适合 128×128 的低分辨率输出。

**标签**: `#embedded-ml`, `#image-generation`, `#microcontrollers`, `#model-quantization`, `#edge-ai`

---

<a id="item-tech-news-16"></a>
### [腾讯混元发布 Hy4 preview](https://mp.weixin.qq.com/s/ymr3X878B8oa2XP15CH8TQ) ⭐️ 7.0/10

腾讯在 2026 年 8 月 28 日发布了开源模型 Hy4 preview，称其为目前最强版本之一。该模型总参数量 770B、活跃参数 49B，支持 1M token 上下文，主要面向长周期软件工程、文档办公和科学研究。腾讯还表示，Hy4 preview 已上线腾讯云、GitHub、HuggingFace、ModelScope、AtomGit 和 OpenRouter 等渠道，并在 203 个工程任务的盲评中以 2.99 分略高于 GLM 5.3 的 2.92 分和 Kimi K3 的 2.94 分；API 定价为每 1M tokens 输入 0.834 美元、输出 2.501 美元。

telegram · zaihuapd · 8月28日 06:11

**「背景」** Hy4 preview 是腾讯混元新一代开源旗舰模型，采用 MoE（混合专家）架构，因此总参数量 770B 与每个 token 实际激活的 49B 参数并不相同。它的 1M token 上下文窗口意味着模型可以一次处理更长的输入，这类能力通常更适合长周期软件工程、文档处理和科研场景。

**「影响」** 对需要长上下文能力的软件工程和文档处理用户来说，Hy4 preview 现在可以通过多个平台直接试用，并提供了明确的 API 计费标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aibase.com/news/30694">Tencent Hunyuan launches open - source flagship model ...</a></li>
<li><a href="https://github.com/Tencent-Hunyuan/Hy4-preview">GitHub - Tencent - Hunyuan / Hy 4 - preview · GitHub</a></li>

</ul>
</details>

**标签**: `#AI models`, `#open source`, `#Tencent Hunyuan`, `#software engineering`, `#LLM benchmarks`

---

<a id="item-tech-news-17"></a>
### [智谱开源 GLM-5.3](http://z.ai/) ⭐️ 7.0/10

智谱 AI 发布开源模型 GLM-5.3，定位于智能体编程与网络防御场景，权重已开放下载、运行和定制。来源称，GLM-5.3 与 GLM-5.2 共用同一基础模型，本次能力提升全部来自后训练，并在复杂编程和长周期任务上增强。其公布的成绩包括 Terminal Bench 2.1 得分 88.2、DeepSWE 得分 66.9，均被称为大幅领先 GLM-5.2。该模型采用自定义 GLM-5.3 License，个人与中小企业可自由使用、微调和商用，但连续 12 个月营收超过 100 亿美元且对外提供模型即服务的公司，需先通过 Z.AI 安全审查。

telegram · zaihuapd · 8月28日 15:32

**「背景」** GLM 是智谱 AI 的第五代大模型系列，公开资料将其定位在推理、编程和智能体能力方向。这里的“智能体编程”通常指模型不仅生成代码，还能分步骤调用工具、处理更长链路的任务；“网络防御”则是把模型用于安全分析、检测和应急等场景。

**「影响」** 对需要本地或可定制智能体编程、网络防御模型的团队，GLM-5.3 提供了新的开源权重选择，但大型模型服务商需要先评估其自定义许可限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://glm5.net/">GLM - 5 | Zhipu AI &#x27;s Next-Generation Large Language Model</a></li>

</ul>
</details>

**标签**: `#large language models`, `#open source`, `#agentic coding`, `#cybersecurity`, `#AI licensing`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [美国上诉法院裁定不利于预测市场](https://www.cnbc.com/2026/08/28/appeals-court-rules-against-prediction-markets-tees-up-scotus-fight.html) ⭐️ 7.0/10

美国第九巡回上诉法院驳回 Kalshi、Crypto.com 和 Robinhood 阻止内华达州博彩监管机构执法的请求，并认定体育相关事件合约不是由美国商品期货交易委员会监管的衍生品。该裁决与第三巡回上诉法院 4 月认为只有 CFTC 有权监管这类合约的裁决相冲突，法律专家称这可能使争议进入最高法院。

rss · CNBC Finance · 8月29日 02:23

**「背景」** 这起案件争的是体育相关“事件合约”到底该按联邦衍生品规则由美国商品期货交易委员会（CFTC）监管，还是可由各州按博彩法监管；第九巡回法院的判断还与第三巡回法院今年早些时候的结论相冲突。

**「影响」** Kalshi、Crypto.com 和 Robinhood 在内华达州的体育相关事件合约业务面临州博彩监管继续介入，因为法院未阻止该州叫停其相关运营。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kucoin.com/news/flash/ninth-circuit-rules-kalshi-sports-contracts-not-swaps-contradicting-third-circuit">Ninth Circuit Rules Kalshi Sports Contracts Not Swaps ...</a></li>
<li><a href="https://predictionnews.com/story/robinhood-kalshi-and-crypto-com-lose-appeals-for-injunctive-relief-against-nevad-c5361eb2">Ninth Circuit rejects Robinhood, Kalshi, and Crypto.com bid ...</a></li>

</ul>
</details>

**标签**: `#prediction markets`, `#CFTC`, `#gaming regulation`, `#sports betting`, `#appeals court`

---

<a id="item-finance-news-2"></a>
### [个人住房贷款期限延长](https://news.ifeng.com/c/8vxm6huJOMR) ⭐️ 7.0/10

中国人民银行和国家金融监督管理总局 28 日联合印发意见，将个人住房贷款期限从最长 30 年延长至最长 40 年。意见称，这是为适应经济社会发展需要，具体期限由购房人与商业银行协商确定。

telegram · zaihuapd · 8月28日 12:16

**「背景」** 中国人民银行和国家金融监督管理总局于 28 日联合印发《关于改革完善房地产信贷管理 推动加快构建房地产发展新模式的意见》，这是此次房贷期限调整所依据的文件；“个人住房贷款期限”指房贷最长还款年限。 \[source: tool-1-3\]

<details><summary>参考链接</summary>
<ul>
<li><a href="https://m.163.com/dy/article/L5ELRKSM0512B07B.html">两部门：将 个 人 住 房 贷 款 期 限 由 最 长 30 年 延 长 至 最 长 40 年 _手机网易网</a></li>

</ul>
</details>

**标签**: `#房地产政策`, `#住房贷款`, `#金融监管`, `#银行`

---