from tracker import ExpenseTracker

# Table column widths for the all-expenses view
COL_INDEX = 4
COL_DATE = 22
COL_CATEGORY = 15
COL_DESCRIPTION = 25
COL_AMOUNT = 8
TABLE_WIDTH = COL_INDEX + 1 + COL_DATE + 1 + COL_CATEGORY + 1 + COL_DESCRIPTION + 1 + COL_AMOUNT

# Table width for the by-category view
CATEGORY_TABLE_WIDTH = 32


def print_menu() -> None:
    """Display the main menu options."""
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Delete expense")
    print("6. Exit")
    print("======================")


def add_expense(tracker: ExpenseTracker) -> None:
    """Prompt the user to enter and add a new expense.

    Args:
        tracker: The active ExpenseTracker instance.
    """
    try:
        amount = float(input("Amount: $"))
        if amount <= 0:
            print("Amount must be positive.")
            return
    except ValueError:
        print("Invalid amount.")
        return

    category = input("Category (e.g. Food, Transport, Entertainment): ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    description = input("Description: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    expense = tracker.add_expense(amount, category, description)
    print(f"Added: {expense}")


def view_all_expenses(tracker: ExpenseTracker) -> None:
    """Display all expenses in a formatted table.

    Args:
        tracker: The active ExpenseTracker instance.
    """
    expenses = tracker.get_all_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(
        f"\n{'#':<{COL_INDEX}} {'Date':<{COL_DATE}} "
        f"{'Category':<{COL_CATEGORY}} {'Description':<{COL_DESCRIPTION}} {'Amount':>{COL_AMOUNT}}"
    )
    print("-" * TABLE_WIDTH)
    for i, e in enumerate(expenses, 1):
        print(
            f"{i:<{COL_INDEX}} {e.date:<{COL_DATE}} "
            f"{e.category:<{COL_CATEGORY}} {e.description:<{COL_DESCRIPTION}} ${e.amount:>{COL_AMOUNT - 1}.2f}"
        )


def view_total(tracker: ExpenseTracker) -> None:
    """Display total spending and expense count.

    Args:
        tracker: The active ExpenseTracker instance.
    """
    total = tracker.get_total()
    count = len(tracker.get_all_expenses())
    print(f"\nTotal spending: ${total:.2f} across {count} expense(s).")


def delete_expense(tracker: ExpenseTracker) -> None:
    """Prompt the user to delete an expense by index.

    Args:
        tracker: The active ExpenseTracker instance.
    """
    expenses = tracker.get_all_expenses()
    if not expenses:
        print("No expenses to delete.")
        return

    view_all_expenses(tracker)
    try:
        index = int(input("\nEnter expense number to delete: "))
        removed = tracker.delete_expense(index)
        print(f"Deleted: {removed}")
    except ValueError:
        print("Invalid number.")
    except IndexError as e:
        print(str(e))


def view_by_category(tracker: ExpenseTracker) -> None:
    """Display spending broken down by category.

    Args:
        tracker: The active ExpenseTracker instance.
    """
    totals = tracker.get_total_by_category()
    if not totals:
        print("No expenses recorded yet.")
        return
    print(f"\n{'Category':<20} {'Total':>10}")
    print("-" * CATEGORY_TABLE_WIDTH)
    for category, total in sorted(totals.items()):
        print(f"{category:<20} ${total:>9.2f}")
    print("-" * CATEGORY_TABLE_WIDTH)
    print(f"{'TOTAL':<20} ${tracker.get_total():>9.2f}")


def main() -> None:
    """Run the expense tracker CLI."""
    tracker = ExpenseTracker()
    actions = {
        "1": add_expense,
        "2": view_all_expenses,
        "3": view_total,
        "4": view_by_category,
        "5": delete_expense,
    }

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "6":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice](tracker)
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
