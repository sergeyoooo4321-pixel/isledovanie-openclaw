# Medium — How I Built My Own OpenClaw Bot V2: Skills, Context Files, and a Smarter Brain
**URL:** https://medium.com/@juanc.olamendy/how-i-built-my-own-openclaw-bot-v2-skills-context-files-and-a-smarter-brain-084acbfa9630  
**Автор:** Juan C. Olamendy  
**Дата публикации:** March 2026  
**Дата сбора:** 2026-04-14  
**Статус:** OK  

---

## Что починил/улучшил

4 критические проблемы первой версии:

| Проблема | Решение |
|---------|----------|
| Запутанный 300-строчный системный промпт | Модульная сборка из 7 источников |
| Агент не знал о доступных инструментах | Автоматическое обнаружение скиллов |
| Нет осведомлённости о недавнем контексте | Ежедневные логи памяти (сегодня + вчера) |
| Промпт перестраивался на каждый вызов | Один билд на сессию сообщения |

## Архитектура

### 1. Модульный системный промпт
Функция `build_system_prompt()` собирает из:
- Текущая дата/время
- 5 контекстных файлов (AGENTS.md, SOUL.md, USER.md, IDENTITY.md, TOOLS.md)
- Ежедневные логи памяти
- Индекс скиллов
- Инструкции для memory tool

**Ключевая оптимизация:** "Building it once at the message boundary and every subsequent tool call in that turn gets a cache hit" — prompt caching через Anthropic API

### 2. Контекстные файлы

| Файл | Назначение |
|------|---------|
| `SOUL.md` | Личность, стиль общения, мнения |
| `USER.md` | Знания агента: имя, timezone, tech stack, проекты |
| `AGENTS.md` | Маршрутизация multi-agent и правила эскалации |
| `IDENTITY.md` | Самоконцепция агента и операционные ограничения |
| `TOOLS.md` | Документация кастомных инструментов и паттерны использования |

Отсутствующие файлы деградируют gracefully без ошибок.

### 3. Система ежедневной памяти
- Загружает логи сегодня и вчера (`YYYY-MM-DD.md`)
- Автоматически инжектируется в системный промпт
- Агент пишет сводки через инструмент `write_file`
- Создаёт natural journaling loop: недавний прогресс → dated logs → automatic context surfacing

### 4. Система обнаружения скиллов

**Структура директории:**
```
workspace/skills/
  skill-name/
    SKILL.md (с YAML frontmatter)
    scripts/
      (исполняемые файлы)
```

**Автоматическое сканирование:** Система парсит директории скиллов, извлекает метаданные, генерирует XML-индекс в системном промпте.  
**Нет регистрации:** Просто брось папку в `workspace/skills/`, работает на следующей сессии.

## Реализованные скиллы

- **Code Formatter:** Python via Black and isort
- **Deploy:** Production deployment via SSH
- **Research:** Многошаговые исследовательские процессы

## Технические детали

- **Всего кода:** ~500 строк Python
- **Модель:** Claude Sonnet 4.6
- **Ключевая фича API:** Prompt caching для стабильных префиксов

## Workflow использования

1. Агент получает сообщение
2. `build_system_prompt()` собирает контекст один раз
3. Агент видит доступные скиллы через XML-индекс
4. При совпадении задачи — читает SKILL.md, выполняет со скриптом
5. Результаты логируются в дневной лог памяти

## Insight

> "Prompt caching: building it once at the message boundary — every subsequent tool call in that turn gets a cache hit"
