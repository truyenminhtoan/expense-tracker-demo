import json
import os
from expense import Expense


class ExpenseTracker:
    def __init__(self, data_file: str = "expenses.json"):
        self.data_file = data_file
        self.expenses: list[Expense] = []
        self._load()

    def add_expense(self, amount: float, category: str, description: str) -> Expense:
        expense = Expense(amount=amount, category=category, description=description)
        self.expenses.append(expense)
        self._save()
        return expense

    def get_all_expenses(self) -> list[Expense]:
        return self.expenses

    def get_total(self) -> float:
        return sum(e.amount for e in self.expenses)

    def get_total_by_category(self) -> dict[str, float]:
        totals: dict[str, float] = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount
        return totals

    def _save(self):
        with open(self.data_file, "w") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=2)

    def _load(self):
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, "r") as f:
            data = json.load(f)
            self.expenses = [Expense.from_dict(d) for d in data]
