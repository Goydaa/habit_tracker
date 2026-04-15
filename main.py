import json
from datetime import datetime
from typing import List, Dict

class HabitTracker:
    def __init__(self, filename: str = "habits.json"):
        self.filename = filename
        self.habits = self.load_data()

    def load_data(self) -> List[Dict]:
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.habits, f, indent=4, ensure_ascii=False)

    def add_habit(self, name: str):
        new_habit = {
            "name": name,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "completed_days": [],
            "streak": 0
        }
        self.habits.append(new_habit)
        self.save_data()
        print(f" Привычка '{name}' добавлена!")

    def complete_habit(self, index: int):
        if 0 <= index < len(self.habits):
            today = datetime.now().strftime("%Y-%m-%d")
            if today not in self.habits[index]["completed_days"]:
                self.habits[index]["completed_days"].append(today)
                self.habits[index]["streak"] += 1
                self.save_data()
                print(f" Отлично! Привычка '{self.habits[index]['name']}' выполнена.")
            else:
                print(" Сегодня вы уже это делали!")

    def list_habits(self):
        print("\n--- Список ваших привычек ---")
        for i, h in enumerate(self.habits):
            print(f"{i}. {h['name']} | Серия: {h['streak']} дн. | Создана: {h['created_at']}")
        print("-----------------------------\n")

if __name__ == "__main__":
    tracker = HabitTracker()
    # Демонстрация работы
    tracker.add_habit("Пить 2л воды")
    tracker.add_habit("Читать 20 страниц")
    tracker.list_habits()
    tracker.complete_habit(0)