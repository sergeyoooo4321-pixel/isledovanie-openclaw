# Запуск: python agent/run_analysis.py
# Агент читает все файлы из raw/, анализирует по инструкции выше
# Результат пишет в analysis/YYYY-MM-DD_findings.md
# Параметры анализа вводятся пользователем в терминале

import os
import glob
from datetime import datetime

RAW_DIR = "raw/"
OUTPUT_DIR = "analysis/"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=== Агент анализа кейсов OpenClaw ===")
focus = input("Что конкретно искать? (Enter = всё по умолчанию): ").strip()
if not focus:
    focus = "все реальные кейсы использования OpenClaw"

# Читаем все raw файлы
files = glob.glob(f"{RAW_DIR}*.md")
print(f"Найдено файлов для анализа: {len(files)}")

# Здесь агент (Claude Code) сам читает файлы и анализирует
# согласно AGENT_INSTRUCTIONS.md
# Результат → analysis/YYYY-MM-DD_findings.md

output_file = f"{OUTPUT_DIR}{datetime.now().strftime('%Y-%m-%d')}_findings.md"
print(f"Результат будет в: {output_file}")
print("Начинаю анализ...")
