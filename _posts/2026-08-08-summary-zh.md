---
layout: default
title: "Horizon Summary: 2026-08-08 (ZH)"
date: 2026-08-08
lang: zh
---

> 从 312 条内容中筛选出 12 条重要资讯。

---

**科技新闻**
1. [pgrust 以向量化执行加速 PostgreSQL 分析查询](#item-tech-news-1) ⭐️ 7.0/10
2. [Cloudflare 推出面向智能体的 Kitesurf 浏览器](#item-tech-news-2) ⭐️ 7.0/10
3. [2027 memory capacity is reportedly sold out](#item-tech-news-3) ⭐️ 7.0/10
4. [uber/ADR](#item-tech-news-4) ⭐️ 7.0/10
5. [新 AI 预估全球冰川蕴藏约 15 万立方千米的冰，融化可抬升海平面 32.3 厘米](#item-tech-news-5) ⭐️ 7.0/10
6. [SK 海力士确认 V10 NAND 闪存为 375 层堆叠，导入晶圆键合技术](#item-tech-news-6) ⭐️ 7.0/10
7. [赵祺握住了豆包的方向盘](#item-tech-news-7) ⭐️ 7.0/10
8. [美国审查中国 AI 企业海外获取英伟达芯片渠道](#item-tech-news-8) ⭐️ 7.0/10
9. [sub2api 曝 OAuth 高危漏洞，仅凭邮箱即可接管账户](#item-tech-news-9) ⭐️ 7.0/10

**财经新闻**
1. [寒武纪 2026 上半年归母净利润 23.11 亿元，同比增长 122.61%](#item-finance-news-1) ⭐️ 7.0/10
2. [雪佛兰退出中国：750 万车主、21 年合资终落幕](#item-finance-news-2) ⭐️ 7.0/10
3. [北京非京籍购房社保年限下调至 1 年](#item-finance-news-3) ⭐️ 7.0/10

---

## 科技新闻

<a id="item-tech-news-1"></a>
### [pgrust 以向量化执行加速 PostgreSQL 分析查询](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 7.0/10

pgrust 查询引擎项目宣称，通过批处理、算子融合、SIMD 和自适应规划，可将 PostgreSQL 分析查询的性能最高提升约 300 倍。由于未提供原文、测试配置、工作负载范围和完整基准数据，现有材料无法确认这一最高值适用于多少查询或生产环境。项目作者表示当前首要目标是正确性，并称过去两周结合了形式化验证与差分模糊测试，已证明 1000 多个面向用户的函数在 pgrust 与 PostgreSQL 中采用完全相同的逻辑。即便这些验证成立，它们也不能单独证明整个查询引擎在所有 SQL 语义、并发和故障场景下均与 PostgreSQL 一致。

hackernews · poly2it · 8月7日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**「背景」** pgrust 是一个以 Rust 重新实现 PostgreSQL 行为的项目，项目方称其兼容 PostgreSQL 的网络协议和 SQL 方言，并通过了 PostgreSQL 的 46,066 项回归测试；此次性能工作对应 0.2 版。\[tool-1-1\]\[tool-1-3\] 批处理和 SIMD 让查询引擎一次处理多行数据，算子融合则减少查询算子之间的中间结果与调度开销，这些都是分析型查询引擎常用的向量化执行技术。

**「实际影响」** 对分析型 PostgreSQL 工作负载的开发者而言，pgrust 可能显著缩短查询时间，但公开性能数据来自其项目自有基准，且项目仍在通过差分模糊测试和模拟测试验证兼容性与正确性，因此尚不足以证明其适合广泛生产部署。

**「社区讨论」** 评论者认可向量化执行和自适应规划的技术潜力，但对正确性覆盖范围、I/O 与线程调度、噪声邻居问题以及长期维护提出疑问。部分人认为数据库的采用取决于 PostgreSQL 团队级别的信誉、连续维护和运营可靠性，而不仅是性能或开发速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/">Rebuilding Postgres for 300x faster analytics: batching ...</a></li>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now ...</a></li>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/pgrust: Postgres rewritten in Rust, now ...</a></li>
<li><a href="https://github.com/malisper/pgrust/tree/main/benchmarks">pgrust/benchmarks at main · malisper/pgrust · GitHub</a></li>

</ul>
</details>

**标签**: `#PostgreSQL`, `#query engines`, `#SIMD`, `#database performance`, `#Rust`

---

<a id="item-tech-news-2"></a>
### [Cloudflare 推出面向智能体的 Kitesurf 浏览器](https://blog.cloudflare.com/kitesurf/) ⭐️ 7.0/10

Cloudflare 介绍了 Kitesurf，一款面向 AI 智能体工作负载、运行于 V8 isolates 的浏览器。它基于模块化开源浏览器引擎 Blitz 构建，体现了将浏览器能力嵌入隔离执行环境的新架构方向。现有信息未能确认 Kitesurf 当前是否已开源，也没有提供其成熟度、性能、Web 标准兼容性或反自动化机制适配情况。Blitz 作者表示自己未参与 Kitesurf 的开发，但获悉 Cloudflare 有意开源相关代码并将补丁上游合并；这仍属于转述的未来计划。

hackernews · m3h · 8月7日 10:42 · [社区讨论](https://news.ycombinator.com/item?id=49208393)

**「背景」** V8 isolate 是相互隔离的 JavaScript 执行环境，Cloudflare Workers 以此类轻量运行模型在其全球基础设施上执行代码。Kitesurf 将浏览器能力直接放入 Workers，并采用无状态、可横向扩展的设计，目标是为 AI 代理提供比传统人工交互式浏览器更合适的网页操作工具。

**「社区讨论」** 讨论者主要关注 Kitesurf 的开放源码计划、标准兼容性，以及运行在 Cloudflare 基础设施中的智能体是否会绕过或仍受其反机器人机制限制。另有用户质疑 Cloudflare 同时经营 CDN、安全业务和智能体平台可能产生利益冲突，也有人指出浏览器智能体代购等实际应用目前并不清晰。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cloudflare.com/kitesurf/">Introducing Kitesurf: The agent-first browser that runs in V8 isolates on Cloudflare Workers | Cloudflare Blog</a></li>

</ul>
</details>

**标签**: `#browser-engines`, `#AI-agents`, `#V8-isolates`, `#Cloudflare`, `#open-source`

---

<a id="item-tech-news-3"></a>
### [2027 memory capacity is reportedly sold out](https://www.ign.com/articles/ramageddon-continues-another-year-as-2027-memory-capacity-is-reportedly-sold-out) ⭐️ 7.0/10

Memory production capacity for 2027 is reportedly already sold out as AI-driven HBM demand places pressure on the supply of conventional DRAM.

hackernews · inigyou · 8月7日 07:58 · [社区讨论](https://news.ycombinator.com/item?id=49207236)

**标签**: `#memory-supply`, `#HBM`, `#DRAM`, `#AI-hardware`, `#semiconductors`

---

<a id="item-tech-news-4"></a>
### [uber/ADR](https://github.com/uber/ADR) ⭐️ 7.0/10

Uber has released ADR, a system for monitoring, benchmarking, detecting threats to, and preventing unsafe actions by enterprise AI agents.

rss · GitHub Trending - Python Daily · 8月7日 03:59

**标签**: `#AI agent security`, `#threat detection`, `#observability`, `#enterprise AI`, `#open source`

---

<a id="item-tech-news-5"></a>
### [新 AI 预估全球冰川蕴藏约 15 万立方千米的冰，融化可抬升海平面 32.3 厘米](https://www.ithome.com/0/987/225.htm) ⭐️ 7.0/10

IceBoost v2.0 估算南极和格陵兰冰盖之外的全球冰川约含 15 万立方千米冰，全部融化对应全球平均海平面上升约 32.3 厘米。

rss · IT之家 · 8月7日 23:22

**标签**: `#人工智能`, `#机器学习`, `#气候建模`, `#冰川研究`, `#海平面上升`

---

<a id="item-tech-news-6"></a>
### [SK 海力士确认 V10 NAND 闪存为 375 层堆叠，导入晶圆键合技术](https://www.ithome.com/0/987/148.htm) ⭐️ 7.0/10

SK 海力士公布采用晶圆键合和 375 层堆叠的 V10 NAND，并计划于 2027 年上半年量产相关企业级 SSD。

rss · IT之家 · 8月7日 10:02

**标签**: `#NAND闪存`, `#晶圆键合`, `#企业级SSD`, `#存储硬件`, `#SK海力士`

---

<a id="item-tech-news-7"></a>
### [赵祺握住了豆包的方向盘](https://www.36kr.com/p/3929019838348417) ⭐️ 7.0/10

报道称字节跳动将飞书产品团队并入豆包，由赵祺统筹新团队，以整合 AI 产品线并加码企业办公市场。

rss · 36氪 - 24小时热榜 · 8月7日 07:04

**标签**: `#字节跳动`, `#豆包`, `#飞书`, `#AI办公`, `#组织重构`

---

<a id="item-tech-news-8"></a>
### [美国审查中国 AI 企业海外获取英伟达芯片渠道](https://www.bloomberg.com/news/articles/2026-08-07/us-reviews-china-s-offshore-access-to-nvidia-chips-after-ai-breakthroughs) ⭐️ 7.0/10

报道称美国 BIS 正审查中国 AI 企业通过海外走私或远程租赁渠道使用英伟达芯片的情况，同时国会拟立法明确其监管海外云算力的权限。

telegram · zaihuapd · 8月7日 11:18

**标签**: `#芯片出口管制`, `#AI算力`, `#英伟达`, `#云计算`, `#中美科技政策`

---

<a id="item-tech-news-9"></a>
### [sub2api 曝 OAuth 高危漏洞，仅凭邮箱即可接管账户](https://github.com/Wei-Shaw/sub2api/issues/5350) ⭐️ 7.0/10

据报 sub2api v0.1.171 及更早版本的 OAuth pending session 校验缺陷可使攻击者仅凭注册邮箱绑定受害者账户并取得控制权。

telegram · zaihuapd · 8月7日 14:59

**标签**: `#OAuth`, `#账户接管`, `#API安全`, `#sub2api`, `#漏洞披露`

---

## 财经新闻

<a id="item-finance-news-1"></a>
### [寒武纪 2026 上半年归母净利润 23.11 亿元，同比增长 122.61%](https://www.ithome.com/0/987/181.htm) ⭐️ 7.0/10

寒武纪披露 2026 年上半年营收 59.96 亿元、归母净利润 23.11 亿元，分别同比增长 108.13%和 122.61%，但经营现金流明显下滑。

rss · IT之家 · 8月7日 12:01

**标签**: `#寒武纪`, `#半年度业绩`, `#AI芯片`, `#经营现金流`, `#研发投入`

---

<a id="item-finance-news-2"></a>
### [雪佛兰退出中国：750 万车主、21 年合资终落幕](https://m.mydrivers.com/newsview/1142126.html) ⭐️ 7.0/10

报道称雪佛兰结束在中国的新车零售业务，上汽通用将重心转向别克和凯迪拉克，并保留雪佛兰出口生产及授权售后服务。

telegram · zaihuapd · 8月7日 11:12

**标签**: `#雪佛兰`, `#上汽通用`, `#中国汽车市场`, `#新能源汽车竞争`, `#合资品牌`

---

<a id="item-finance-news-3"></a>
### [北京非京籍购房社保年限下调至 1 年](https://www.peopleapp.com/column/30052875352-500007640471) ⭐️ 7.0/10

北京据报放宽非京籍购房资格并提高公积金贷款及装修提取支持力度。

telegram · zaihuapd · 8月7日 13:57

**标签**: `#北京房地产`, `#住房限购`, `#非京籍购房`, `#住房公积金`, `#房地产政策`

---