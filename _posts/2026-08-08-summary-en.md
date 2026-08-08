---
layout: default
title: "Horizon Summary: 2026-08-08 (EN)"
date: 2026-08-08
lang: en
---

> From 312 items, 12 important content pieces were selected

---

**Technology News**
1. [pgrust Claims 300x Faster PostgreSQL Analytics](#item-tech-news-1) ⭐️ 7.0/10
2. [Cloudflare Introduces Kitesurf, an Agent-First Browser](#item-tech-news-2) ⭐️ 7.0/10
3. [2027 memory capacity is reportedly sold out](#item-tech-news-3) ⭐️ 7.0/10
4. [uber/ADR](#item-tech-news-4) ⭐️ 7.0/10
5. [新 AI 预估全球冰川蕴藏约 15 万立方千米的冰，融化可抬升海平面 32.3 厘米](#item-tech-news-5) ⭐️ 7.0/10
6. [SK 海力士确认 V10 NAND 闪存为 375 层堆叠，导入晶圆键合技术](#item-tech-news-6) ⭐️ 7.0/10
7. [赵祺握住了豆包的方向盘](#item-tech-news-7) ⭐️ 7.0/10
8. [美国审查中国 AI 企业海外获取英伟达芯片渠道](#item-tech-news-8) ⭐️ 7.0/10
9. [sub2api 曝 OAuth 高危漏洞，仅凭邮箱即可接管账户](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [寒武纪 2026 上半年归母净利润 23.11 亿元，同比增长 122.61%](#item-finance-news-1) ⭐️ 7.0/10
2. [雪佛兰退出中国：750 万车主、21 年合资终落幕](#item-finance-news-2) ⭐️ 7.0/10
3. [北京非京籍购房社保年限下调至 1 年](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [pgrust Claims 300x Faster PostgreSQL Analytics](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 7.0/10

The pgrust query-engine project claims PostgreSQL analytics speedups of up to 300x using vectorized execution techniques such as batching, operator fusion, and SIMD. It also includes adaptive planning, which can revise execution decisions as a query runs. The project author says correctness is the current priority and reports using formal verification and differential fuzz testing, including proofs that more than 1,000 user-facing functions implement the same logic as PostgreSQL. Because the source content and benchmark details are unavailable, the scope, workloads, compatibility constraints, and reproducibility of the headline performance claim cannot be established from the supplied evidence.

hackernews · poly2it · Aug 7, 11:00 · [Discussion](https://news.ycombinator.com/item?id=49208535)

**「Background」** pgrust is a Rust reimplementation of PostgreSQL intended to preserve its wire protocol and SQL dialect compatibility; its repository reports passing all 46,066 tests in PostgreSQL’s regression suite. Its analytics engine uses batching to process groups of rows, operator fusion to reduce intermediate work, and SIMD instructions to perform the same operation across multiple values in parallel.

**「Impact」** PostgreSQL users considering pgrust for analytics can evaluate its published ClickBench and OLTP benchmarks, but the headline 300x gain should be treated as workload-specific while the project continues differential fuzzing and simulation testing for correctness.

**「Community Discussion」** Commenters welcomed the performance work and adaptive planning, but questioned whether an independently developed engine could earn PostgreSQL-level operational trust, longevity, and continuity. They also requested architectural details about thread and I/O scheduling, particularly for noisy-neighbor workloads, while one commenter noted that running PostgreSQL on RAM-backed storage can independently produce large gains when the database fits in memory.

<details><summary>References</summary>
<ul>
<li><a href="https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/">Rebuilding Postgres for 300x faster analytics: batching ...</a></li>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now ...</a></li>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now ...</a></li>
<li><a href="https://github.com/malisper/pgrust/tree/main/benchmarks">pgrust/benchmarks at main · malisper/pgrust · GitHub</a></li>

</ul>
</details>

**Tags**: `#PostgreSQL`, `#query engines`, `#SIMD`, `#database performance`, `#Rust`

---

<a id="item-tech-news-2"></a>
### [Cloudflare Introduces Kitesurf, an Agent-First Browser](https://blog.cloudflare.com/kitesurf/) ⭐️ 7.0/10

Cloudflare has introduced Kitesurf, an agent-oriented browser architecture that runs with V8 isolates. It is built on Blitz, a modular open-source browser engine developed by the Dioxus Labs community, although Kitesurf&\#x27;s current source availability, standards compatibility, maturity, and performance are not established by the supplied material. A Blitz developer said they were not involved in Kitesurf but had been told that Cloudflare intends to open-source its work and upstream its patches. The design is technically notable because it adapts browser infrastructure for software agents, but its practical capabilities and limitations remain unclear.

hackernews · m3h · Aug 7, 10:42 · [Discussion](https://news.ycombinator.com/item?id=49208393)

**「Background」** V8 isolates are lightweight, separated JavaScript execution environments; Cloudflare Workers uses this model instead of assigning a full virtual machine to every workload. Kitesurf applies that architecture to a stateless browser designed for AI agents, with Cloudflare describing it as running entirely on Workers for scalable web interaction.

**「Community Discussion」** Discussion focused on whether Cloudflare will open-source and upstream Kitesurf&\#x27;s changes, whether workloads running on its infrastructure will receive special treatment from Cloudflare&\#x27;s anti-bot systems, and how compatible the browser will be with web standards. Some commenters also questioned the demand for browser agents and raised concerns about Cloudflare operating both agent infrastructure and security services.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/kitesurf/">Introducing Kitesurf: The agent-first browser that runs in V8 isolates on Cloudflare Workers | Cloudflare Blog</a></li>

</ul>
</details>

**Tags**: `#browser-engines`, `#AI-agents`, `#V8-isolates`, `#Cloudflare`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [2027 memory capacity is reportedly sold out](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out) ⭐️ 7.0/10

Memory production capacity for 2027 is reportedly already sold out as AI-driven HBM demand places pressure on the supply of conventional DRAM.

hackernews · inigyou · Aug 7, 07:58 · [Discussion](https://news.ycombinator.com/item?id=49207236)

**Tags**: `#memory-supply`, `#HBM`, `#DRAM`, `#AI-hardware`, `#semiconductors`

---

<a id="item-tech-news-4"></a>
### [uber/ADR](https://github.com/uber/ADR) ⭐️ 7.0/10

Uber has released ADR, a system for monitoring, benchmarking, detecting threats to, and preventing unsafe actions by enterprise AI agents.

rss · GitHub Trending - Python Daily · Aug 7, 03:59

**Tags**: `#AI agent security`, `#threat detection`, `#observability`, `#enterprise AI`, `#open source`

---

<a id="item-tech-news-5"></a>
### [新 AI 预估全球冰川蕴藏约 15 万立方千米的冰，融化可抬升海平面 32.3 厘米](https://www.ithome.com/0/987/225.htm) ⭐️ 7.0/10

IceBoost v2.0 估算南极和格陵兰冰盖之外的全球冰川约含 15 万立方千米冰，全部融化对应全球平均海平面上升约 32.3 厘米。

rss · IT之家 · Aug 7, 23:22

**Tags**: `#人工智能`, `#机器学习`, `#气候建模`, `#冰川研究`, `#海平面上升`

---

<a id="item-tech-news-6"></a>
### [SK 海力士确认 V10 NAND 闪存为 375 层堆叠，导入晶圆键合技术](https://www.ithome.com/0/987/148.htm) ⭐️ 7.0/10

SK 海力士公布采用晶圆键合和 375 层堆叠的 V10 NAND，并计划于 2027 年上半年量产相关企业级 SSD。

rss · IT之家 · Aug 7, 10:02

**Tags**: `#NAND闪存`, `#晶圆键合`, `#企业级SSD`, `#存储硬件`, `#SK海力士`

---

<a id="item-tech-news-7"></a>
### [赵祺握住了豆包的方向盘](https://www.36kr.com/p/3929019838348417) ⭐️ 7.0/10

报道称字节跳动将飞书产品团队并入豆包，由赵祺统筹新团队，以整合AI产品线并加码企业办公市场。

rss · 36氪 - 24小时热榜 · Aug 7, 07:04

**Tags**: `#字节跳动`, `#豆包`, `#飞书`, `#AI办公`, `#组织重构`

---

<a id="item-tech-news-8"></a>
### [美国审查中国 AI 企业海外获取英伟达芯片渠道](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 7.0/10

报道称美国 BIS 正审查中国 AI 企业通过海外走私或远程租赁渠道使用英伟达芯片的情况，同时国会拟立法明确其监管海外云算力的权限。

telegram · zaihuapd · Aug 7, 11:18

**Tags**: `#芯片出口管制`, `#AI算力`, `#英伟达`, `#云计算`, `#中美科技政策`

---

<a id="item-tech-news-9"></a>
### [sub2api 曝 OAuth 高危漏洞，仅凭邮箱即可接管账户](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 7.0/10

据报 sub2api v0.1.171 及更早版本的 OAuth pending session 校验缺陷可使攻击者仅凭注册邮箱绑定受害者账户并取得控制权。

telegram · zaihuapd · Aug 7, 14:59

**Tags**: `#OAuth`, `#账户接管`, `#API安全`, `#sub2api`, `#漏洞披露`

---

## Financial News

<a id="item-finance-news-1"></a>
### [寒武纪 2026 上半年归母净利润 23.11 亿元，同比增长 122.61%](https://www.ithome.com/0/987/181.htm) ⭐️ 7.0/10

寒武纪披露 2026 年上半年营收 59.96 亿元、归母净利润 23.11 亿元，分别同比增长 108.13%和 122.61%，但经营现金流明显下滑。

rss · IT之家 · Aug 7, 12:01

**Tags**: `#寒武纪`, `#半年度业绩`, `#AI芯片`, `#经营现金流`, `#研发投入`

---

<a id="item-finance-news-2"></a>
### [雪佛兰退出中国：750 万车主、21 年合资终落幕](https://m.mydrivers.com/newsview/1142126.html) ⭐️ 7.0/10

报道称雪佛兰结束在中国的新车零售业务，上汽通用将重心转向别克和凯迪拉克，并保留雪佛兰出口生产及授权售后服务。

telegram · zaihuapd · Aug 7, 11:12

**Tags**: `#雪佛兰`, `#上汽通用`, `#中国汽车市场`, `#新能源汽车竞争`, `#合资品牌`

---

<a id="item-finance-news-3"></a>
### [北京非京籍购房社保年限下调至 1 年](https://www.peopleapp.com/column/30052875352-500007640471) ⭐️ 7.0/10

北京据报放宽非京籍购房资格并提高公积金贷款及装修提取支持力度。

telegram · zaihuapd · Aug 7, 13:57

**Tags**: `#北京房地产`, `#住房限购`, `#非京籍购房`, `#住房公积金`, `#房地产政策`

---