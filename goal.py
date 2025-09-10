class Goal:
    def __init__(self, name, target_amount, category):
        self.name = name
        self.target_amount = target_amount
        self.current_balance = 0
        self.category = category
        self.status = "В процессе"

    def add_funds(self, amount):
        """Увеличение текущего баланса."""
        if self.current_balance + amount > self.target_amount:
            print("Сумма превышает целевую сумму!")
            return False
        self.current_balance += amount
        self.update_status()
        return True

    def withdraw_funds(self, amount):
        """Уменьшение текущего баланса."""
        if self.current_balance - amount < 0:
            print("Недостаточно средств!")
            return False
        self.current_balance -= amount
        self.update_status()
        return True

    def update_status(self):
        """Обновление статуса цели."""
        if self.current_balance >= self.target_amount:
            self.status = "Выполнена"

    def progress_percentage(self):
        """Вычисление процента выполнения цели."""
        return (self.current_balance / self.target_amount) * 100

    def to_dict(self):
        """Преобразование объекта в словарь для сохранения."""
        return {
            "name": self.name,
            "target_amount": self.target_amount,
            "current_balance": self.current_balance,
            "category": self.category,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data):
        """Создание объекта из словаря."""
        goal = Goal(data["name"], data["target_amount"], data["category"])
        goal.current_balance = data["current_balance"]
        goal.status = data["status"]
        return goal