# OpenClaw Use Cases Research

Исследование реальных кейсов использования OpenClaw — open-source AI-агент фреймворка.

## Структура

```
openclaw-research/
├── raw/              ← Собранные данные из 27 источников (блоги, GitHub, Reddit, etc.)
├── meta/
│   ├── sources.json  ← Список URL + статус + дата сбора
│   └── errors.log    ← Что не загрузилось
├── agent/
│   ├── AGENT_INSTRUCTIONS.md  ← Инструкции для агента-аналитика
│   └── run_analysis.py        ← Скрипт запуска анализа
├── analysis/         ← Результаты анализа (генерируются агентом)
├── scraper.py        ← Основной скрипт парсинга
└── README.md
```

## Статистика сбора

### Раунд 1 (2026-04-05)
- **Успешно собрано:** 18 из 27 источников
- **Не загрузилось:** 9 (Reddit — блокирует автоматический доступ, GitHub Discussions — 404)
- **Общий размер данных:** ~1.7 MB

### Раунд 2 (2026-04-14) — Дополнение
- **Новых источников добавлено:** 16
- **Заблокировано/требует ручной проверки:** 22 URL (Reddit, Medium paywall, Substack paywall)
- **Итого в базе:** 43 файла

## Источники

### Успешно собрано (18):
- openclaw.ai/showcase
- openclaw.rocks/blog
- openclaw.com.au/use-cases
- remoteopenclaw.com (2 статьи)
- solvea.cx/glossary
- sidsaladi.substack.com
- aiblewmymind.substack.com
- theinteractive.studio
- clawbot.blog (50 use cases)
- datacamp.com/blog
- kdnuggets.com
- institutionalinvestor.com
- GitHub awesome-openclaw-usecases (README)
- GitHub openclaw/openclaw (main repo)
- clawhub.ai catalog
- redditor.ai/blog
- openclawroadmap.com

### Не загрузилось (9):
- Reddit (все 8 URL) — 403 Blocked
- GitHub Discussions — 404 Not Found

### Добавлено в раунде 2 (16 новых):
- kanerika.com — 15 use cases
- tldl.io — 25+ real examples с метриками удержания
- hostinger.com — 25 use cases
- o-mega.ai — top 50 rankings с оценками ease/impact
- latenode.com — popular use cases + Latenode MCP интеграция
- medium.com (Dr. Shea Johnson) — личная история: 24/7 assistant на Mac Mini
- medium.com (Juan C. Olamendy) — технический: Bot V2, skills, context files, prompt caching
- lennysnewsletter.com — полный гайд, Claire Vo (9 агентов)
- simplified.com — top 10 с приоритетами внедрения
- buildtolaunch.substack.com — solo founder Jenny: что работает, что сломалось
- contabo.com — бизнес-кейсы по всем отделам
- github.com/mergisi/awesome-openclaw-agents — 199 шаблонов агентов в 24 категориях
- wikipedia.org — история, скандалы, безопасность, глобальное принятие
- techradar.com — 10 wild projects (Polymarket bot, Moltbook, WHOOP+RPi...)
- alexmcfarland.substack.com — co-work setup (частично за paywall)
- 45_reddit_urls_to_check_manually.md — список из 22 URL для ручного сбора

### Требует ручной проверки (22 URL):
- Reddit: r/openclaw, r/OpenClawCentral, r/myclaw, r/openclawpirates, r/OpenClawDevs + поиски
- medium.com member-only статья (11 insane use cases)
- Substack paywall: imprasit, amankhan1
- openclawdesktop.com (403)
- GitHub Discussions

## Запуск

```bash
# Парсинг
pip install playwright requests beautifulsoup4 markdownify
playwright install chromium
python scraper.py

# Анализ
python agent/run_analysis.py
```
