import json
import os

DATA_FILE = "goals_data.json"

def save_goals(goals):
    """Сохранение целей в файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([goal.to_dict() for goal in goals], file, ensure_ascii=False, indent=4)

def load_goals():
    """Загрузка целей из файла."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
        return [Goal.from_dict(item) for item in data]