from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class Expense:
    """Represents a single financial expense."""

    def __init__(self, amount: float, category: str, description: str, date: str = None):
        """Initialize an expense.

        Args:
            amount: Monetary value of the expense (must be positive).
            category: Category of the expense (e.g., Food, Transport).
            description: Brief description of the expense.
            date: Optional timestamp string; defaults to current datetime.
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date or datetime.now().strftime(DATE_FORMAT)

    def to_dict(self) -> dict:
        """Serialize the expense to a dictionary."""
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        """Deserialize an expense from a dictionary."""
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            date=data["date"],
        )

    def __str__(self) -> str:
        return f"[{self.date}] {self.category}: {self.description} - ${self.amount:.2f}"

    def __repr__(self) -> str:
        return f"Expense(amount={self.amount}, category={self.category!r}, description={self.description!r})"
