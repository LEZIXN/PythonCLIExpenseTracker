FILENAME = "expense.txt"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (food/travel): ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Try again.")
        return
    with open(FILENAME, 'a') as file:
        file.write(f"{date},{category},{amount}\n")
        print("Expense added!")

def view_expense():
    print("\nAll Expenses:\n")
    try:
        with open(FILENAME, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No expenses recorded yet!")

def show_total():
    try:
        total = 0.0
        with open(FILENAME, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    total += float(parts[2])
        print(f"\nTotal Expenses: ₹{total:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet!")
    except:
        print("Encountered an unknown error")

while True:
    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Show Total Expense")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")    
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expense()
    elif choice == '3':
        show_total()
    elif choice == '4':
        print("Exiting the expense tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")