expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
    else:
        print("\nYour expenses:")

        for expense in expenses:
            print(expense["name"], "-", expense["amount"])


def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total expenses:", total)


while True:
    print("\n--- Expense Tracker ---")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")