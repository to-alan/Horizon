---
layout: default
title: "Horizon Summary: 2026-08-22 (EN)"
date: 2026-08-22
lang: en
---

> From 282 items, 13 important content pieces were selected

---

**Technology News**
1. [Windows IKE RCE Exploited](#item-tech-news-1) ⭐️ 8.0/10
2. [W3 Total Cache Flaw Enables Arbitrary File Writes](#item-tech-news-2) ⭐️ 8.0/10
3. [NASA AIT-GUI Vulnerability Fixed](#item-tech-news-3) ⭐️ 8.0/10
4. [SGLang v0.5.18](#item-tech-news-4) ⭐️ 7.0/10
5. [MCP Roadmap Targets Remote Services and Agent Authentication](#item-tech-news-5) ⭐️ 7.0/10
6. [Apache Maka Debuts](#item-tech-news-6) ⭐️ 7.0/10
7. [Tencent AI-Infra-Guard](#item-tech-news-7) ⭐️ 7.0/10
8. [OpenAI launches Codex CLI](#item-tech-news-8) ⭐️ 7.0/10
9. [Agent Substrate Open Sources Agent Sandbox Runtime](#item-tech-news-9) ⭐️ 7.0/10
10. [Google ADK for Go](#item-tech-news-10) ⭐️ 7.0/10
11. [Tesla China Recall Response](#item-tech-news-11) ⭐️ 7.0/10
12. [Stripe&\#x27;s Reported OpenRouter Deal](#item-tech-news-12) ⭐️ 7.0/10
13. [Open Models Catch Up Faster](#item-tech-news-13) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Windows IKE RCE Exploited](https://www.ithome.com/0/993/113.htm) ⭐️ 8.0/10

CISA added a critical Windows Internet Key Exchange \(IKE\) Extension remote code execution flaw, CVE-2026-33824, to its Known Exploited Vulnerabilities catalog on August 18 and confirmed that it is being actively exploited. The bug is a double-free in the Windows IKE Extension component and can let an unauthenticated attacker send crafted network packets to execute code on systems with IKEv2 enabled, with attack traffic typically reaching UDP 500 and UDP 4500. Microsoft says it fixed the issue in its April 14 security update, which covered 165 newly disclosed vulnerabilities, and that the affected systems include unpatched Windows Server 2016/2019/2022/2022 23H2/2025 plus Windows 10 1607 through 22H2 and Windows 11 23H2 through 26H1. Microsoft and CISA both advise priority patching, and Microsoft recommends blocking external UDP 500 and 4500 traffic or restricting it to known peers if patching is not immediately possible.

rss · IT之家 · Aug 22, 15:15

**「Background」** IKE is part of IPsec and is used to negotiate keys and security associations for protected network communication. Windows IKE Extension adds extra functionality around those exchanges and runs in the IKEEXT service, which makes bugs in this component especially sensitive when the service is exposed to the network.

**「Impact」** Any unpatched Windows device exposing IKEv2 on the network can be targeted for unauthenticated remote code execution, so defenders should patch or restrict UDP 500 and 4500 immediately.

**Tags**: `#cybersecurity`, `#windows`, `#remote-code-execution`, `#vulnerability-management`

---

<a id="item-tech-news-2"></a>
### [W3 Total Cache Flaw Enables Arbitrary File Writes](https://www.ithome.com/0/993/088.htm) ⭐️ 8.0/10

WPScan disclosed a critical flaw in the WordPress plugin W3 Total Cache, which has more than 900,000 active installs, and identified it as CVE-2026-18051 with a CVSS score of 10.0. The bug stems from improper handling of cached file paths, allowing an attacker to write files to arbitrary existing directories on the server, including locations outside the web root. On Apache servers, the issue could also let an attacker overwrite .htaccess and disable or alter security rules, potentially breaking the site or easing follow-on attacks. BoldGrid has released version 2.10.5 to fix the issue, and sites running 2.10.4 or earlier are urged to upgrade before the planned public PoC release on September 17.

rss · IT之家 · Aug 22, 12:09

**「Background」** W3 Total Cache is a popular WordPress plugin used to improve site performance by caching content and related files. A file-write vulnerability is especially serious in web plugins because it can let attackers modify server files and sometimes chain that access into broader compromise.

**「Impact」** WordPress sites using W3 Total Cache 2.10.4 or earlier should upgrade to 2.10.5 immediately to reduce the risk of arbitrary file writes and possible site takeover steps.

**Tags**: `#WordPress`, `#安全漏洞`, `#CVE`, `#Web安全`, `#开源插件`

---

<a id="item-tech-news-3"></a>
### [NASA AIT-GUI Vulnerability Fixed](https://www.ithome.com/0/993/085.htm) ⭐️ 8.0/10

On August 22, IT之家 reported that Cycode disclosed a severe vulnerability in NASA&\#x27;s AMMOS Instrument Toolkit web control interface, AIT-GUI, tracked as GHSA-p9r8-2q67-fp86 with a CVSS score of 9.4. The flaw stems from missing authentication, access control, and CSRF protections, while the server also listens on all network interfaces by default. Researchers said an attacker could trick an operator into opening a malicious page and then use the browser to make AIT-GUI act without direct system compromise. The issue could allow arbitrary commands on the spacecraft and scientific-instrument command bus, as well as server-side script and command execution, and the development team released version 2.5.2 on August 12 to fix it.

rss · IT之家 · Aug 22, 11:53

**「Background」** AMMOS Instrument Toolkit is a NASA and Jet Propulsion Laboratory framework used for ground-station command uplink and telemetry downlink between Earth systems and spacecraft or scientific instruments. AIT-GUI is its web-based control interface, so weaknesses there can affect both operator workstations and the connected mission systems behind them.

**「Impact」** Operators and mission teams using affected AIT-GUI deployments faced a risk of unauthorized command execution against spacecraft and instruments until version 2.5.2 was installed.

**Tags**: `#cybersecurity`, `#vulnerability disclosure`, `#aerospace software`, `#NASA`, `#control systems`

---

<a id="item-tech-news-4"></a>
### [SGLang v0.5.18](https://github.com/sgl-project/sglang/releases/tag/v0.5.18) ⭐️ 7.0/10

SGLang released v0.5.18 as a large community update with 710 PRs from 212 contributors. The release expands model support across autoregressive, multimodal, and diffusion workloads, including Muse Glimmer, Intern-S2-Mobius, SANA-Video, LingBot-Video-MoE, LTX-2.5, Cosmos3 Edge &amp; Distilled, and LongCat-Image, plus new cookbook recipes for Qwen3.8, Ling-3.0, Nemotron 3.5 Lightning, Dots3-Note, and DeepSeek-V4-Pro-0813. It also adds performance work such as overlapped checkpoint staging at startup, TP LMHead all-to-all for pure-DP dp-attention, and FlashInfer MNNVL reuse for pure allreduce, with reported gains on H100, B200, and Blackwell systems. A notable breaking change moves Triton, FlashInfer, Inductor, DeepGEMM, and CUDA driver caches under \`SGLANG\_CACHE\_DIR\`, so the first launch after upgrading recompiles once.

github · Fridge003 · Aug 22, 00:09

**「Background」** SGLang is an open-source serving and inference runtime for large language models and related workloads. Its release notes often matter to operators because they combine new model support with backend and kernel changes that can affect startup behavior, compatibility, and throughput.

**「Impact」** Teams running supported models on H100, B200, or Blackwell hardware can get faster startup or decode performance, but upgrading may require one recompilation because several kernel caches now share \`SGLANG\_CACHE\_DIR\`.

**Tags**: `#llm inference`, `#open source release`, `#multimodal models`, `#diffusion models`, `#AI infrastructure`

---

<a id="item-tech-news-5"></a>
### [MCP Roadmap Targets Remote Services and Agent Authentication](https://blog.modelcontextprotocol.io/posts/mcp-roadmap/) ⭐️ 7.0/10

The Model Context Protocol roadmap describes planned changes intended to make MCP more practical for remote HTTP services and agent-based clients. A central focus is extending authorization beyond browser-based approval by standardizing how servers recognize and trust agents running as cloud workloads, acting for absent users, or delegating narrower authority to sub-agents. The roadmap is prospective rather than a report of a completed release, so adoption, implementation details, and compatibility remain uncertain.

hackernews · pentagrama · Aug 22, 13:31 · [Discussion](https://news.ycombinator.com/item?id=49399591)

**「Background」** Model Context Protocol, or MCP, is a standard for connecting AI clients to external tools and services through a common interface. Roadmap updates matter because MCP is still evolving, and changes to transport and authentication determine whether it works cleanly for local desktop apps, remote servers, and cloud-hosted agents. For developers, the main issue is interoperability: the protocol has to support both interactive users and non-interactive agent workloads without forcing each service to invent its own integration model.

**「Impact」** MCP service developers may eventually gain a more standardized path for authenticating noninteractive agents and exposing remote endpoints, but they will need to implement the planned mechanisms before clients can rely on them consistently.

**「Community Discussion」** Commenters welcomed the reported move toward treating remote MCP servers like ordinary HTTP workloads, while others questioned whether MCP is easier for agents to use than REST APIs, criticized its changing standards and complexity, and doubted how many servers will implement the proposed agent-identity model. Some developers said these earlier issues had already pushed them toward local tools and conventional APIs.

**Tags**: `#model context protocol`, `#AI infrastructure`, `#authentication`, `#developer tools`

---

<a id="item-tech-news-6"></a>
### [Apache Maka Debuts](https://github.com/apache/maka) ⭐️ 7.0/10

Apache Maka \(Incubating\) is a local-first AI agent workspace that records model messages, tool calls, tool results, permission decisions, and termination events in an append-only log. The project says the log is the runtime, with sessions, UI state, model context, and recovery derived from that ledger rather than treated as disposable history. It supports Desktop, a terminal TUI, a non-interactive CLI, and evaluation runs, all routed through a Runtime Host that manages sessions, turns, agent lifecycle, continuation, tools, and events. The project is still under active development, and the first public macOS Desktop build is for Apple Silicon only; data formats, CLI commands, and experimental capabilities may still change.

rss · GitHub Trending - Daily · Aug 22, 02:11

**「Background」** Local-first software keeps data and state on the user’s machine by default instead of relying on a hosted service. In AI agent systems, append-only event logs can help make tool use, permissions, and outputs auditable and easier to replay or recover.

**「Impact」** Apple Silicon Mac users can try Maka’s signed and notarized Desktop app now, while Intel Macs, Windows, and Linux remain unsupported or only previewed.

**Tags**: `#AI Agents`, `#Open Source`, `#Auditability`, `#Developer Tools`

---

<a id="item-tech-news-7"></a>
### [Tencent AI-Infra-Guard](https://github.com/Tencent/AI-Infra-Guard) ⭐️ 7.0/10

Tencent&\#x27;s AI-Infra-Guard is an open-source, full-stack AI red teaming platform for scanning Agent behavior, Skills, MCP integrations, AI infrastructure, and LLM jailbreak resistance. The repository says it combines ClawScan, Agent Scan, AI infra vulnerability scanning, MCP Server and Agent Skills scanning, and jailbreak evaluation to help teams self-test AI security risks. Its latest listed release, v4.5.2 on 2026-08-17, adds .pyc bytecode bypass detection and charset smuggling defense for Skill-Scan, dynamic-mode tool whitelisting for MCP-Scan to prevent RCE, a new SkillJack research project, and an expanded vulnerability library with 2,000+ CVE rules. Earlier 2026 releases also added multi-turn jailbreak attacks, more OWASP skills, standalone CLI tools, and a larger rule base.

rss · GitHub Trending - Python Daily · Aug 22, 02:24

**「Background」** AI red teaming is the practice of probing an AI system for jailbreaks, unsafe tool use, prompt injection, and other security failures before attackers do. MCP, or Model Context Protocol, is commonly used to connect AI applications to external tools and services, which makes it a useful but security-sensitive target for scanning.

**「Impact」** Teams deploying AI agents, MCP services, or LLM-powered workflows now have a single open-source platform that can test multiple layers of their stack with dedicated scans and rule sets.

**Tags**: `#AI Security`, `#Red Teaming`, `#LLM Safety`, `#MCP`, `#Open Source`

---

<a id="item-tech-news-8"></a>
### [OpenAI launches Codex CLI](https://github.com/openai/codex) ⭐️ 7.0/10

OpenAI&\#x27;s Codex CLI is presented as a lightweight coding agent that runs locally in the terminal on your computer. The repository documents installation for macOS, Linux, and Windows through shell scripts, npm, Homebrew, or GitHub Releases, and notes that the standalone installers prefer downloads from releases.openai.com with a fallback to GitHub if needed. It also distinguishes the terminal CLI from related Codex options for IDEs, a desktop app, and the cloud-based Codex Web service. Users can sign in with a ChatGPT account for Plus, Pro, Business, Edu, or Enterprise plans, or use an API key with additional setup.

rss · GitHub Trending - Rust Daily · Aug 22, 02:26

**「Background」** Codex CLI is OpenAI’s terminal-based version of its Codex coding agent, intended to run locally on a developer’s computer rather than only through a web interface or editor integration. It sits in the broader category of AI coding agents, which can help inspect code, propose changes, and automate development tasks from environments such as terminals, IDEs, desktop apps, or CI workflows.

**「Impact」** Developers now have a documented local terminal workflow for using OpenAI&\#x27;s Codex alongside editor, desktop, and web entry points.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/codex">GitHub - openai/codex: Lightweight coding agent that runs in your terminal · GitHub</a></li>
<li><a href="https://developers.openai.com/codex/github-action">Codex GitHub Action | ChatGPT Learn</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#developer tools`, `#CLI`, `#OpenAI`, `#GitHub`

---

<a id="item-tech-news-9"></a>
### [Agent Substrate Open Sources Agent Sandbox Runtime](https://github.com/agent-substrate/substrate) ⭐️ 7.0/10

Agent Substrate is an open-source runtime and control plane for running large-scale agent sandboxes, published on GitHub under the Apache 2.0 license. It is designed to map many idle &quot;actors&quot; onto a smaller pool of ready workers, with full lifecycle management for create, destroy, suspend, and resume, plus traffic routing. The project supports multiple sandbox technologies, including microVMs and gVisor, and uses Kubernetes for underlying provisioning and worker lifecycle management. The repository says the system is still in early development, is not ready for production use, and its APIs and backward compatibility may change.

rss · GitHub Trending - Go Daily · Aug 22, 02:16

**「Background」** In this project, an &quot;actor&quot; is the application being hosted inside a sandbox, often an AI agent or another stateful workload. Kubernetes provides the base infrastructure, while Agent Substrate adds agent-specific scheduling and state management to keep many mostly idle workloads multiplexed efficiently.

**「Impact」** Developers building agent infrastructure can experiment with a high-density, stateful sandbox runtime that targets low-latency suspend and resume, but they should treat it as pre-production software.

**Tags**: `#AI infrastructure`, `#open source`, `#sandboxing`, `#cloud infrastructure`, `#virtualization`

---

<a id="item-tech-news-10"></a>
### [Google ADK for Go](https://github.com/google/adk-go) ⭐️ 7.0/10

Google has published \`google/adk-go\`, an open-source, code-first Go toolkit for building, evaluating, and deploying AI agents. The project presents ADK as a flexible, modular framework that applies software development practices to agent workflows, from simple tasks to more complex multi-agent systems. It is described as model-agnostic and deployment-agnostic, while being optimized for Gemini and positioned for cloud-native use. The repository points to Go docs, samples, and sibling ADK implementations in Python, Java, Kotlin, TypeScript, and web tooling.

rss · GitHub Trending - Go Daily · Aug 22, 02:16

**「Background」** Agent development kits provide reusable abstractions for agent logic, tool use, orchestration, and deployment so teams do not have to assemble those pieces from scratch. In Go, this kind of toolkit is most relevant to developers building concurrent services and cloud-native applications.

**「Impact」** Go developers now have an official ADK option for building and deploying agentic applications with Google-backed documentation, samples, and package distribution.

**Tags**: `#Go`, `#AI agents`, `#open source`, `#developer tools`, `#Google`

---

<a id="item-tech-news-11"></a>
### [Tesla China Recall Response](https://www.ithome.com/0/993/052.htm) ⭐️ 7.0/10

Tesla is responding to a China recall covering 2.976 million vehicles, including domestically built Model 3 and Model Y cars and imported Model 3, Model X, and Model S models. The recall was triggered because the in-car emergency mechanical release is similar in color to the interior trim and can be hard to find and use in extreme crash scenarios when the low-voltage system fails. Tesla says it will address the issue by adding free warning labels near the emergency release and by pushing an OTA software update that adds an automatic window-lowering strategy after an accident. Tesla China also said owners do not need to visit service centers immediately; some vehicles only need the software updates, while others can pick up the stickers at service centers during routine maintenance, with the labeling campaign available for three years.

rss · IT之家 · Aug 22, 09:58

**「Background」** An emergency mechanical door release is a manual way to open a vehicle door if powered systems stop working after a crash or electrical failure. OTA updates let automakers change vehicle software remotely, which is often used to fix safety-related behavior without requiring an in-person repair.

**「Impact」** Affected Tesla owners in China can generally wait for OTA updates and collect the warning stickers later, instead of making an immediate service visit.

**Tags**: `#electric vehicles`, `#Tesla`, `#vehicle safety`, `#OTA updates`, `#automotive software`

---

<a id="item-tech-news-12"></a>
### [Stripe&\#x27;s Reported OpenRouter Deal](https://www.36kr.com/p/3950020635180169) ⭐️ 7.0/10

The article says Stripe acquired OpenRouter for $8 billion, describing OpenRouter as a 90-person company that aggregates more than 400 model APIs behind one interface and takes a 5.5% platform fee. It argues the business is valuable because it gives developers one key, one bill, model choice across many providers, and strong routing reliability without building models or data centers. The piece contrasts that with gray-market AI relay services that resell or obscure model access, then places Stripe&\#x27;s move in the context of a broader competition over trusted model routing, billing, and control of usage data. Several of the valuation, revenue, and customer claims are presented as sourced from reports or company materials, but the article itself does not provide direct verification of the acquisition terms.

rss · 36氪 - 24小时热榜 · Aug 22, 02:29

**「Background」** OpenRouter is a model-routing platform that lets developers send requests through one API and choose among many underlying AI providers. This kind of service reduces integration work when applications need fallback routing, multiple model choices, or unified billing across vendors. In the AI stack, the routing layer sits between app developers and model providers, so whoever controls it can influence price, reliability, and usage visibility.

**「Impact」** If the acquisition is accurate, it would give Stripe a direct position in the AI routing layer, which could matter for developers that rely on neutral multi-model access and for companies that want predictable billing and compliance.

**Tags**: `#AI infrastructure`, `#developer tools`, `#startup acquisitions`, `#API platforms`

---

<a id="item-tech-news-13"></a>
### [Open Models Catch Up Faster](https://newsletter.semianalysis.com/p/are-open-models-catching-up) ⭐️ 7.0/10

SemiAnalysis argues that the gap between open and closed frontier models has been shrinking in recurring cycles, and that each generation of open models is catching up in about half the time of the last. The report divides model history into three eras, ending with an agent era in which the pace of convergence is fastest. It says Kimi K2.6 surpassed Opus 4.5 in 4.8 months and GLM-5.2 exceeded GPT-5.2 in 6 months. The article adds that GLM 5.3 and Kimi K3 can already handle many coding and agent tasks that helped Anthropic reach more than $6.5 billion in annualized revenue, raising concerns about model-layer commoditization even though Anthropic still has an advantage in productization.

telegram · zaihuapd · Aug 22, 08:26

**「Background」** Open models are released with public weights or code, while closed models are proprietary and controlled by the vendor. In this context, agentic and coding tasks refer to models that can plan, use tools, and complete software work, which has become a key battleground for frontier AI systems.

**「Impact」** If SemiAnalysis’s assessment is right, AI buyers and developers may find that core coding and agent capabilities are becoming easier to source from open models, increasing price pressure on closed-model vendors while leaving product integration and deployment as differentiators.

**Tags**: `#open-source models`, `#large language models`, `#AI industry`, `#agents`, `#model commoditization`

---