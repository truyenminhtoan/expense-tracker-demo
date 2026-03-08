import json
import os
import pytest
from tracker import ExpenseTracker


@pytest.fixture
def tracker(tmp_path):
    data_file = str(tmp_path / "test_expenses.json")
    return ExpenseTracker(data_file=data_file)


def test_add_expense(tracker):
    e = tracker.add_expense(10.0, "Food", "Lunch")
    assert e.amount == 10.0
    assert e.category == "Food"
    assert e.description == "Lunch"
    assert len(tracker.get_all_expenses()) == 1


def test_get_total(tracker):
    tracker.add_expense(10.0, "Food", "Lunch")
    tracker.add_expense(5.0, "Transport", "Bus")
    assert tracker.get_total() == 15.0


def test_get_total_by_category(tracker):
    tracker.add_expense(10.0, "Food", "Lunch")
    tracker.add_expense(5.0, "Food", "Snack")
    tracker.add_expense(8.0, "Transport", "Taxi")
    totals = tracker.get_total_by_category()
    assert totals["Food"] == 15.0
    assert totals["Transport"] == 8.0


def test_persistence(tmp_path):
    data_file = str(tmp_path / "expenses.json")
    t1 = ExpenseTracker(data_file=data_file)
    t1.add_expense(20.0, "Entertainment", "Movie")

    t2 = ExpenseTracker(data_file=data_file)
    assert len(t2.get_all_expenses()) == 1
    assert t2.get_all_expenses()[0].amount == 20.0


def test_load_empty_file(tmp_path):
    data_file = str(tmp_path / "empty.json")
    tracker = ExpenseTracker(data_file=data_file)
    assert tracker.get_all_expenses() == []


def test_delete_expense(tracker):
    tracker.add_expense(10.0, "Food", "Lunch")
    tracker.add_expense(5.0, "Transport", "Bus")
    removed = tracker.delete_expense(1)
    assert removed.amount == 10.0
    assert len(tracker.get_all_expenses()) == 1


def test_delete_expense_invalid_index(tracker):
    tracker.add_expense(10.0, "Food", "Lunch")
    with pytest.raises(IndexError):
        tracker.delete_expense(99)


def test_load_corrupt_file(tmp_path):
    data_file = str(tmp_path / "corrupt.json")
    with open(data_file, "w") as f:
        f.write("not json")
    tracker = ExpenseTracker(data_file=data_file)
    assert tracker.get_all_expenses() == []
