import csv
import os
from datetime import datetime

# Define the file path for storing income and expenses
CSV_FILE = 'expenses.csv'

# Function to initialize the CSV file if it doesn't exist
def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            # Create headers: date, category, amount, description
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

# Function to add a new transaction (income or expense)
def add_transaction(category, amount, description):
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        date = datetime.now().strftime('%Y-%m-%d')
        writer.writerow([date, category, amount, description])
    print(f"Transaction added: {category} - {amount} - {description}")

# Function to display all transactions
def view_transactions():
    with open(CSV_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# CLI to interact with the user
def main():
    init_csv()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income/Expense")
        print("2. View Transactions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (e.g., Income, Food, Rent, Bills): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            add_transaction(category, amount, description)
        
        elif choice == '2':
            print("\nTransactions:")
            view_transactions()
        
        elif choice == '3':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
