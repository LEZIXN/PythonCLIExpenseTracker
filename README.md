# 🧾 Expense Tracker (CLI)

This is a simple command-line based **Expense Tracker** built with Python. It allows users to:

- Add daily expenses (with date, category, and amount)
- View all recorded expenses
- Calculate the total amount spent

## 📁 How it works

All data is stored in a plain text file named `expenses.txt`. Each line in the file represents a single expense in the format:

DD-MM-YYYY,Category,Amount

Example:
05-07-2025,Food,250.50
06-07-2025,Travel,100.00

## 🚀 Features

- ✅ Add new expenses
- 📄 View all recorded expenses
- 💰 Show the total amount of expenses
- 🧹 Error handling for invalid input and missing files

## ▶️ How to Run

1. Clone this repository or download the `expenses.py` file.
2. Open a terminal and navigate to the project folder.
3. Run the script using:

python expenses.py
Follow the on-screen menu.

## 🧪 Sample Run

=== Expense Tracker ===

1. Add Expense
2. View Expense
3. Show Total Expense
4. Exit
   Enter your choice (1-4): 1
   Enter date (DD-MM-YYY): 05-07-2025
   Enter category (Food/Travel): Food
   Enter amount: 250
   Expense added!

## 📦 Requirements

This script requires Python 3.x. No external libraries are used.

## 📂 File Structure

```
├── expenses.py # Main application
├── expenses.txt # Data file (auto-generated)
├── requirements.txt # (Optional) For future dependencies
├── README.md # Project documentation
└── .gitignore # Ignore data files and cache
```

### ⚠️ Note

The script does not validate the date format strictly.
Future versions could include filtering by category/date or exporting to CSV/Excel.

## 🛡 License

This project is open-source and available under the MIT License.
