from tracker import ExpenseTracker


def print_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total spending")
    print("4. View spending by category")
    print("5. Exit")
    print("======================")


def add_expense(tracker: ExpenseTracker):
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


def view_all_expenses(tracker: ExpenseTracker):
    expenses = tracker.get_all_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    print(f"\n{'#':<4} {'Date':<22} {'Category':<15} {'Description':<25} {'Amount':>8}")
    print("-" * 78)
    for i, e in enumerate(expenses, 1):
        print(f"{i:<4} {e.date:<22} {e.category:<15} {e.description:<25} ${e.amount:>7.2f}")


def view_total(tracker: ExpenseTracker):
    total = tracker.get_total()
    count = len(tracker.get_all_expenses())
    print(f"\nTotal spending: ${total:.2f} across {count} expense(s).")


def view_by_category(tracker: ExpenseTracker):
    totals = tracker.get_total_by_category()
    if not totals:
        print("No expenses recorded yet.")
        return
    print(f"\n{'Category':<20} {'Total':>10}")
    print("-" * 32)
    for category, total in sorted(totals.items()):
        print(f"{category:<20} ${total:>9.2f}")
    print("-" * 32)
    print(f"{'TOTAL':<20} ${tracker.get_total():>9.2f}")


def main():
    tracker = ExpenseTracker()
    actions = {
        "1": add_expense,
        "2": view_all_expenses,
        "3": view_total,
        "4": view_by_category,
    }

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice in actions:
            actions[choice](tracker)
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
