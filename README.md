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

- **Дата:** 2026-04-05
- **Успешно собрано:** 18 из 27 источников
- **Не загрузилось:** 9 (Reddit — блокирует автоматический доступ, GitHub Discussions — 404)
- **Общий размер данных:** ~1.7 MB

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

## Запуск

```bash
# Парсинг
pip install playwright requests beautifulsoup4 markdownify
playwright install chromium
python scraper.py

# Анализ
python agent/run_analysis.py
```
