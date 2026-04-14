# GitHub — mergisi/awesome-openclaw-agents: 199 Production-Ready Agent Templates
**URL:** https://github.com/mergisi/awesome-openclaw-agents  
**Дата сбора:** 2026-04-14  
**Статус:** OK  

---

## О репозитории

**199 production-ready AI agent templates** в 24 категориях, каждый — copy-paste-ready `SOUL.md` конфиг-файл.  
**Акцент:** Быстрый деплой без нужды в терминальной экспертизе.  
**132 верифицированных кейса** из реального мира.

## Категории агентов (24)

### Productivity (7 агентов)
Task coordination, analytics, email triage, meeting notes

### Development (11 агентов)
Code review, documentation, bug analysis, testing, schema design

### Marketing & Content (20 агентов)
Blog writing, social media, SEO, newsletter, influencer research

### Business (12 агентов)
Customer support, sales assistance, invoicing, churn prediction

### Personal (7 агентов)
Daily planning, fitness coaching, travel booking, journaling

### DevOps (10 агентов)
Incident response, deployment monitoring, infrastructure management

### Finance (10 агентов)
Expense tracking, invoicing, revenue analysis, fraud detection

### Education (8 агентов)
Tutoring, quiz generation, study planning, research assistance

### Healthcare (7 агентов)
Wellness coaching, meal planning, symptom triage

### Legal (6 агентов)
Contract review, compliance checking, patent analysis

### HR (7 агентов)
Recruiting, onboarding, performance reviews

### Creative (11 агентов)
Branding, video scripting, copywriting

### Security (7 агентов)
Vulnerability scanning, threat monitoring, phishing detection

### E-Commerce (6 агентов)
Product listing, review responses, inventory tracking

### Data (7 агентов)
ETL pipelines, data cleaning, report generation

### SaaS (5 агентов)
User onboarding, feature requests, churn prevention

### Real Estate (5 агентов)
Property scouting, market analysis, lead qualification

### Freelance (3 агента)
Proposal writing, time tracking, client management

### Supply Chain, Compliance, Voice, Customer Success, Automation (20+ дополнительно)

## Ключевые особенности

- **Configuration-First:** Агенты определяются полностью через SOUL.md файлы — без Python chains или сложных фреймворков
- **Multi-Channel:** Встроенные интеграции Telegram, Slack, Discord, email
- **Pre-Built Skills:** 13+ переиспользуемых on-device скиллов для Gemma и Claude Code
- **Quick Deployment:** 5-минутная установка через CLI или one-command Docker через CrewClaw

## Технологии

- **Язык:** Node.js
- **Размер:** ~150MB
- **Минимум RAM:** 512MB
- **Multi-Agent:** Да, через AGENTS.md
- **Модели:** Claude, Ollama (бесплатные локальные), DeepSeek, GPT-4 и другие
- **MCP:** Полная поддержка Model Context Protocol

## Варианты деплоя

- **Local:** Самохостинг
- **Cloud:** Docker-based
- **CrewClaw Platform:** Zero-configuration managed deployment
- **Ollama:** Бесплатный локальный инференс с Gemma4 или Qwen

## Отличие от конкурентов

- Легче CrewAI/LangChain (проще конфиг, быстрее setup)
- Более функционален, чем ZeroClaw (Rust, 5MB, edge-focused)
