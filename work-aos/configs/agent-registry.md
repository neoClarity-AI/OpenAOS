---
title: Agent Registry
file_type: config
schema_version: 1.0.0
builder_version: 1.0.0
created_date: 2026-06-04
last_updated: 2026-06-05
status: active
---

# Agent Registry

One row per agent. Status values: installed | available | paused | retired.

| Agent | Status | Required | Builder file | Agent folder | Notes |
|---|---|---|---|---|---|
| Security / Permissions | installed | yes | /builders/build-security-agent.md | /agents/security-agent | Owns permissions + tool matrix |
| Memory | installed | yes | /builders/build-memory-agent.md | /agents/memory-agent | Owns memory routing + hygiene |
| Chief of Staff | installed | yes | /builders/build-chief-of-staff-agent.md | /agents/chief-of-staff-agent | Default coordinator; joint owner of /aos-router.md |
| Review / Reflection | installed | yes | /builders/build-review-agent.md | /agents/review-agent | Owns reviews + user guide |
| Inbox / Communications | installed | no | /builders/build-inbox-agent.md | /agents/inbox-agent | Drafts; send = approval |
| Calendar / Scheduling | installed | no | /builders/build-calendar-agent.md | /agents/calendar-agent | Modify = approval |
| Task / Commitment | installed | no | /builders/build-task-agent.md | /agents/task-agent | Task list owner |
| Project Manager | installed | no | /builders/build-project-manager-agent.md | /agents/project-manager-agent | Owns project lifecycle |
| Research | installed | no | /builders/build-research-agent.md | /agents/research-agent | Web search when granted |
| Automation | available | no | /builders/build-automation-agent.md | — | Not installed |
| Document Librarian | available | no | /builders/build-document-librarian-agent.md | — | Not installed |
| Finance | available | no | /builders/build-finance-agent.md | — | Not installed |
| Health & Life Logistics | available | no | /builders/build-health-life-logistics-agent.md | — | Not installed |
| Learning | available | no | /builders/build-learning-agent.md | — | Not installed |
| Personal CRM | available | no | /builders/build-personal-crm-agent.md | — | Not installed |
| Writing / Content | available | no | /builders/build-writing-agent.md | — | Not installed |
