import pytest
from expense import Expense


def test_expense_creation():
    e = Expense(amount=10.0, category="Food", description="Lunch")
    assert e.amount == 10.0
    assert e.category == "Food"
    assert e.description == "Lunch"
    assert e.date is not None


def test_expense_to_dict():
    e = Expense(amount=5.5, category="Transport", description="Bus", date="2026-03-08 10:00:00")
    d = e.to_dict()
    assert d == {"amount": 5.5, "category": "Transport", "description": "Bus", "date": "2026-03-08 10:00:00"}


def test_expense_from_dict():
    data = {"amount": 20.0, "category": "Food", "description": "Dinner", "date": "2026-03-08 12:00:00"}
    e = Expense.from_dict(data)
    assert e.amount == 20.0
    assert e.category == "Food"
    assert e.description == "Dinner"
    assert e.date == "2026-03-08 12:00:00"


def test_expense_str():
    e = Expense(amount=15.0, category="Food", description="Pizza", date="2026-03-08 09:00:00")
    assert str(e) == "[2026-03-08 09:00:00] Food: Pizza - $15.00"
