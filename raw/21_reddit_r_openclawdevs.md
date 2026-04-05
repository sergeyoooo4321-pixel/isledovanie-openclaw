# Reddit r/OpenClawDevs — Top All Time
**URL:** https://www.reddit.com/r/OpenClawDevs/top/?t=all  
**Дата сбора:** 2026-04-05 21:05  
**Статус:** OK  

---

ИСТОЧНИК 6: r/OpenClawDevs — Top All Time

URL: https://www.reddit.com/r/OpenClawDevs/top/?t=all

Статус: OK (нишевый девелоперский сабреддит)

Описание: Open Claw discussions & cool demos. Created Jan 30, 2026. 93 weekly visitors.
POST 1

Заголовок: DevClaw v1.2.2 – Turns OpenClaw into a high performing development team | OpenClaw plugin for multi-project dev workflow orchestration

Author: u/henknozemans | Score: 11 | Flair: -

Permalink: r/OpenClawDevs (2 months ago)





Текст:

I do all my development in DevClaw now. I go to bed, wake up, and the work is done across multiple projects.





DevClaw is an OpenClaw plugin that turns your orchestrator agent into a development manager. Each group chat becomes an isolated project with its own team. You create issues, the agent handles the rest.





Features:

- Autonomous dev/QA pipeline: DEV writes code, QA reviews it, failures loop back to DEV automatically. No human in the loop. You wake up to completed issues.

- Multi-project isolation: Each group chat = separate project with its own queue, workers, sessions, state. Multiple projects run in parallel.

- Developer roles, not model IDs: Don't configure claude-sonnet-4-5, assign a "medior developer." CSS typo → junior. Database migration → architect.

- Session reuse: Workers keep codebase knowledge across tasks instead of re-reading from scratch each time. ~50K tokens saved per pickup.

- Token-free scheduling: work_heartbeat scans queues and dispatches workers through pure CLI calls. Zero LLM tokens spent on orchestration.

- Atomic operations with rollback: Label transition + state update + session dispatch + audit log in one call. Either everything succeeds or everything rolls back.

- Issues as source of truth: Runs on GitHub/GitLab issues, not internal database.





Result: ~60-80% token savings versus running one large model with fresh context each time.





----------------------------------------------------------------





POST 2

Заголовок: I Spent 5 Days Fixing My AI Agent's Memory. Here's Everything That Actually Worked.

Author: u/Silent_Employment966 | Score: 3 (via r/AskClaw) | Flair: -

Permalink: r/OpenClawDevs (1 month ago) [cross-post from r/AskClaw — 93 upvotes there]





Текст:

I built an AI agent that runs on Telegram, handles support for two SaaS products, drafts tweets, manages invoices, and coordinates with my co-founder across timezones.





Day 1 — Agent forgets after long conversations (compaction problem):

Fix: enable memory flush before compaction:

{ "compaction": { "memoryFlush": { "enabled": true, "softThresholdTokens": 4000 } } }

Key learning: compaction isn't the problem. Losing information during compaction is. If it's only in context window, it's temporary. If it's on disk, it survives.





Day 2 — Search returns garbage:

Issue: default SQLite uses vector embeddings, semantic similarity — fails on exact matches.

Fix: switch to QMD (BM25 keyword + vector + reranker). Client names, specific numbers, exact phrases now found.





Day 3 — Agent finds it but doesn't use it:

Problem: retrieval isn't automatic — agent has to decide to search.

Fix: explicit retrieval instructions at top of AGENTS.md: "Before starting any task: Search daily logs for related context. Check LEARNINGS.md for rules about this type of task."

Added retrieval test: plant specific marker in daily log, new session, ask agent about it.





Day 4 — Compaction-safe:

Issue: very long sessions where compaction runs multiple times (memory flush only triggers once per cycle).

Fix: configure context pruning: { "contextPruning": { "mode": "cache-ttl", "ttl": "6h", "keepLastAssistants": 3 } }





Day 5 — System prompt was 28% bloated:

Found via /context detail: 11,887 tokens before first message. 51 skills loaded (20 unused). MEMORY.md = 200 lines of company wiki on every session. BOOT.md was doing nothing (OpenClaw doesn't auto-load it!).





Key discoveries:

- Only these files auto-load: AGENTS.md, SOUL.md, TOOLS.md, IDENTITY.md, USER.md, HEARTBEAT.md, MEMORY.md. EVERYTHING ELSE needs explicit read instruction in AGENTS.md.

- BOOT.md is NOT a real thing in OpenClaw. Had one for weeks. It did nothing.

- Boot sequence goes at VERY TOP of AGENTS.md (not middle, not bottom).

- Never write directly to MEMORY.md during tasks — curate it during periodic reviews.

- LEARNINGS.md is most underrated file: every mistake → one-line rule (compounds over weeks).

- Handover protocol for model switches: write current state to daily log before switching.

- Run /context detail regularly to see what's eating tokens.





Results: system prompt from 11,887 to 8,529 tokens. Skills from 51 to 32. Session tokens from 18,280 to 14,627 (28% lighter).





----------------------------------------------------------------





POST 3

Заголовок: Bounded Mission: how we run OpenClaw safely without neutering its usefulness

Author: u/Advanced_Pudding9228 | Score: 4 | Flair: -

Permalink: r/OpenClawDevs (2 months ago)





Текст:

Operating principle: OpenClaw should be powerful for automation, but incapable by default of doing dangerous things. Not "trusted." Not "careful." Incapable.





Scope boundaries (hard limits):

- Dedicated runtime: never on primary workstation, never on host with SSH keys/cloud credentials

- Network isolation: outbound access allowlisted to only what it needs, no inbound except admin via allowlist or VPN

- Least-privilege credentials: every token minimal, scoped, rotatable; short-lived where possible

- Filesystem containment: run as non-root user; one workspace directory read/write; everything else inaccessible

- Command execution guardrails: deny by default; no curl|sh, no rm -rf, no privilege escalation, no Docker socket access

- Skill hygiene: only trusted sources, pin versions, review before enabling





Threat model: malicious/compromised skills, prompt injection, tool misuse, unexpected agent behavior.





Operating rule: if task requires access to sensitive systems, OpenClaw must either generate instructions for human operator OR raise "needs manual approval" flag. Never directly connect using privileged access.





Verification checklist:

- Host contains zero production credentials and zero prod SSH keys

- Outbound network restricted by allowlist

- Bot runs as non-root with minimal filesystem mounts

- Dangerous commands blocked or explicitly allowlisted

- Skills pinned and reviewed

- Heartbeat and skill actions logged and reviewed on schedule
