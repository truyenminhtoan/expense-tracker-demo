import json
import os
from expense import Expense


class ExpenseTracker:
    """Manages a collection of expenses with JSON file persistence."""

    def __init__(self, data_file: str = "expenses.json"):
        """Initialize the tracker and load any existing expenses from disk.

        Args:
            data_file: Path to the JSON file used for persistence.
        """
        self.data_file = data_file
        self.expenses: list[Expense] = []
        self._load()

    def add_expense(self, amount: float, category: str, description: str) -> Expense:
        """Create and persist a new expense.

        Args:
            amount: Monetary value of the expense.
            category: Expense category.
            description: Short description.

        Returns:
            The newly created Expense.
        """
        expense = Expense(amount=amount, category=category, description=description)
        self.expenses.append(expense)
        self._save()
        return expense

    def get_all_expenses(self) -> list[Expense]:
        """Return all tracked expenses."""
        return self.expenses

    def get_total(self) -> float:
        """Return the sum of all expense amounts."""
        return sum(e.amount for e in self.expenses)

    def delete_expense(self, index: int) -> Expense:
        """Remove an expense by its 1-based index.

        Args:
            index: 1-based position of the expense to remove.

        Returns:
            The removed Expense.

        Raises:
            IndexError: If index is out of range.
        """
        if index < 1 or index > len(self.expenses):
            raise IndexError(f"Index {index} out of range.")
        expense = self.expenses.pop(index - 1)
        self._save()
        return expense

    def get_total_by_category(self) -> dict[str, float]:
        """Return total spending grouped by category."""
        totals: dict[str, float] = {}
        for expense in self.expenses:
            totals[expense.category] = totals.get(expense.category, 0) + expense.amount
        return totals

    def _save(self) -> None:
        """Persist all expenses to the JSON data file."""
        with open(self.data_file, "w") as f:
            json.dump([e.to_dict() for e in self.expenses], f, indent=2)

    def _load(self) -> None:
        """Load expenses from the JSON data file if it exists."""
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                self.expenses = [Expense.from_dict(d) for d in data]
        except (json.JSONDecodeError, KeyError):
            self.expenses = []
