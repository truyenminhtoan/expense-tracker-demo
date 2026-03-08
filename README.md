# Expense Tracker

A simple command-line expense tracking application written in Python.

## Features

- Add expenses with amount, category, and description
- View all expenses in a formatted table
- View total spending
- View spending broken down by category
- Persistent storage via JSON file

## Project Structure

```
expense-tracker/
├── expense.py      # Expense data model
├── tracker.py      # ExpenseTracker business logic
├── main.py         # CLI interface
├── tests/
│   ├── test_expense.py
│   └── test_tracker.py
└── conftest.py
```

## Usage

```bash
python3 main.py
```

### Menu Options

1. **Add expense** — enter amount, category, and description
2. **View all expenses** — table of all recorded expenses
3. **View total spending** — sum of all expenses
4. **View spending by category** — breakdown per category
5. **Delete expense** — remove an expense by its number
6. **Exit**

## Running Tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest
pytest tests/ -v
```

## Data Storage

Expenses are saved to `expenses.json` in the working directory.
