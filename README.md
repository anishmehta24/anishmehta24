<h1 align="center">Hi, I'm Anish Mehta 👋</h1>
<h3 align="center">Backend & systems engineer who likes finding the bug nobody else noticed</h3>

<p align="center">
  CSE '27 @ BIT Mesra &nbsp;·&nbsp; Software Engineering Intern @ Clootrack &nbsp;·&nbsp; Open-source contributor
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/anish-mehta-81080029b/">LinkedIn</a> ·
  <a href="mailto:mehtaanish111@gmail.com">Email</a> ·
  <a href="https://leetcode.com/anishmehta_24">LeetCode</a> ·
  <a href="https://codeforces.com/profile/Anish_2407">Codeforces</a>
</p>

---

### What I do

- **Backend at [Clootrack](https://www.clootrack.com/)** (Feb 2026 – present): Python and Go services for Clootrack Neo, a no-code analytics platform. Cut cross-region dataset latency with regional Azure Blob caching, replaced a Spark CSV pipeline with Polars for higher ingestion throughput, designed event-driven cleanup workflows on Dapr pub/sub + Celery, and migrated core services from Django to Go.
- **Open source**: I find bugs by differential testing and fuzzing frontends, then fix them with regression tests. I care about the root cause, not the symptom.
- **Competitive programming**: Codeforces Specialist (max 1424) · LeetCode Knight (max 1930).

### Open-source contributions

| Project | What |
|---|---|
| [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | **2 PRs merged** — reasoning content preserved on tool-call follow-ups ([#8405](https://github.com/microsoft/agent-framework/pull/8405)), streamed image generation no longer dropped ([#8424](https://github.com/microsoft/agent-framework/pull/8424)); a third fixes lost output on crash recovery of checkpointed workflows ([#8478](https://github.com/microsoft/agent-framework/pull/8478)) |
| [Apache Beam](https://github.com/apache/beam) | Python SDK honours the `disable*Metrics` experiments for high-throughput jobs, re-landing a reverted feature without breaking the public metrics API ([#40165](https://github.com/apache/beam/pull/40165)) |
| [Intel OpenVINO](https://github.com/openvinotoolkit/openvino) | PyTorch-frontend fixes for negative-step slicing ([#38242](https://github.com/openvinotoolkit/openvino/pull/38242)), `narrow` with a negative start ([#38259](https://github.com/openvinotoolkit/openvino/pull/38259)) and integer floor division ([#38260](https://github.com/openvinotoolkit/openvino/pull/38260)); found and reported a GPU-plugin bug and a CPU/GPU `Divide` spec violation along the way |
| [microsoft/onnxscript](https://github.com/microsoft/onnxscript) | `torch.sort(stable=True)` / `argsort` now export through the dynamo ONNX exporter ([#3053](https://github.com/microsoft/onnxscript/pull/3053)) |
| NVIDIA NeMo Agent Toolkit · Haystack · Agno · Arize Phoenix · Opik · Strands Agents | Root-caused bugs (type resolution, text chunking, concurrency-safe metrics, error handling), each with a self-filed issue and regression tests |

### Things I've built

- **[Verse](https://github.com/anishmehta24/verse)** — real-time collaborative workspace: docs, code, whiteboard and audio/video in one place. Yjs CRDTs over WebSockets for conflict-free editing, WebRTC calls with Socket.IO signalling, TypeScript/React/Node. [Live](https://collab-docs-web.onrender.com/)
- **[OSS Contributor Engine](https://github.com/anishmehta24/OSS-Contributor-engine)** — multi-agent platform that profiles your GitHub history, hunts matching open-source issues and drafts pitches. Five specialist agents, pgvector ranking, a fault-tolerant multi-LLM router (Groq/Gemini failover), FastAPI + Next.js. [Live](https://oss-contributor-engine.vercel.app)

### Toolbox

`Python` `Go` `TypeScript` `Java` `C++` `SQL` · FastAPI, Node.js/Express, React/Next.js · PostgreSQL, pgvector, MongoDB, Redis · Apache Spark, Apache Beam, Polars · Dapr, Celery, Docker, CI/CD · Azure, AWS · PyTest

### Off the keyboard

Guitar, singing, and chasing boundaries on the cricket field.

---

<div align="center">
  <img height="150" src="https://github-readme-stats.vercel.app/api?username=anishmehta24&show_icons=true&locale=en&layout=compact&theme=dark" alt="GitHub stats" />
  <img height="150" src="https://leetcard.jacoblin.cool/anishmehta_24?theme=dark&font=Lato&ext=heatmap" alt="LeetCode" />
</div>
