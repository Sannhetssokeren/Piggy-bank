from goal import Goal
from data_handler import save_goals, load_goals

def display_menu():
    print("\n--- Копилка ---")
    print("1. Добавить цель")
    print("2. Просмотреть цели")
    print("3. Изменить баланс цели")
    print("4. Удалить цель")
    print("5. Просмотреть общий прогресс")
    print("6. Выход")

def add_goal(goals):
    name = input("Введите название цели: ")
    target_amount = float(input("Введите целевую сумму: "))
    category = input("Введите категорию (например, Работа, Здоровье): ")
    goals.append(Goal(name, target_amount, category))
    print(f"Цель '{name}' добавлена!")

def view_goals(goals):
    if not goals:
        print("Целей нет.")
        return
    for i, goal in enumerate(goals, 1):
        progress = goal.progress_percentage()
        print(f"{i}. {goal.name} ({goal.category}) - {progress:.2f}% ({goal.current_balance}/{goal.target_amount}) [{goal.status}]")

def modify_balance(goals):
    view_goals(goals)
    choice = int(input("Выберите цель для изменения баланса: ")) - 1
    if 0 <= choice < len(goals):
        action = input("Введите 'add' для пополнения или 'withdraw' для списания: ").strip().lower()
        amount = float(input("Введите сумму: "))
        if action == "add":
            goals[choice].add_funds(amount)
        elif action == "withdraw":
            goals[choice].withdraw_funds(amount)
        else:
            print("Неверное действие.")
    else:
        print("Неверный выбор.")

def delete_goal(goals):
    view_goals(goals)
    choice = int(input("Выберите цель для удаления: ")) - 1
    if 0 <= choice < len(goals):
        removed_goal = goals.pop(choice)
        print(f"Цель '{removed_goal.name}' удалена.")
    else:
        print("Неверный выбор.")

def calculate_total_progress(goals):
    total_target = sum(goal.target_amount for goal in goals)
    total_current = sum(goal.current_balance for goal in goals)
    if total_target == 0:
        return 0
    return (total_current / total_target) * 100

def main():
    goals = load_goals()
    while True:
        display_menu()
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            add_goal(goals)
        elif choice == "2":
            view_goals(goals)
        elif choice == "3":
            modify_balance(goals)
        elif choice == "4":
            delete_goal(goals)
        elif choice == "5":
            progress = calculate_total_progress(goals)
            print(f"Общий прогресс: {progress:.2f}%")
        elif choice == "6":
            save_goals(goals)
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()