import json
import os
from datetime import datetime
from typing import List, Dict

class HabitTracker:
    """Профессиональный трекер привычек с хранением данных в JSON."""
    
    def __init__(self, filename: str = "habits.json"):
        self.filename = filename
        self.habits = self.load_data()

    def load_data(self) -> List[Dict]:
        """Загрузка данных из файла с обработкой ошибок."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def save_data(self):
        """Сохранение текущего состояния в JSON."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.habits, f, indent=4, ensure_ascii=False)

    def add_habit(self, name: str):
        """Добавление новой привычки."""
        new_habit = {
            "name": name,
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "completed_days": [],
            "streak": 0
        }
        self.habits.append(new_habit)
        self.save_data()
        print(f"✅ Привычка '{name}' успешно добавлена!")

    def list_habits(self):
        """Вывод всех привычек в консоль."""
        if not self.habits:
            print("\n--- Список пуст. Пора завести полезную привычку! ---")
            return

        print("\n=== ВАШИ ПРИВЫЧКИ ===")
        for i, h in enumerate(self.habits):
            last_date = h["completed_days"][-1] if h["completed_days"] else "Никогда"
            print(f"{i}. [{h['name']}]")
            print(f"   🔥 Серия: {h['streak']} дн. | Последний раз: {last_date}")
        print("=====================\n")

    def complete_habit(self, index: int):
        """Отметка о выполнении на сегодня."""
        if 0 <= index < len(self.habits):
            today = datetime.now().strftime("%Y-%m-%d")
            habit = self.habits[index]
            
            if today not in habit["completed_days"]:
                habit["completed_days"].append(today)
                habit["streak"] += 1
                self.save_data()
                print(f"⭐ Молодец! Привычка '{habit['name']}' выполнена!")
            else:
                print(f"⏳ На сегодня привычка '{habit['name']}' уже отмечена.")
        else:
            print("❌ Ошибка: привычки с таким номером не существует.")

    def delete_habit(self, index: int):
        """Удаление привычки по индексу."""
        if 0 <= index < len(self.habits):
            removed = self.habits.pop(index)
            self.save_data()
            print(f"🗑️ Привычка '{removed['name']}' удалена.")
        else:
            print("❌ Неверный индекс для удаления.")

if __name__ == "__main__":
    tracker = HabitTracker()
    
    # Имитация работы приложения для демонстрации
    print("--- Система управления привычками v2.0 ---")