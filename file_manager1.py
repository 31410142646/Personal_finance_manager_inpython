import csv
from expense import Expense


FILE_NAME = 'data/expenses.csv'
def save_expenses(expenses):
    with open(FILE_NAME, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        for exp in expenses:
            writer.writerow(exp.to_list())




def load_expenses():
    expenses = []
    try:
        with open(FILE_NAME, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expense = Expense(
                    row['Amount'],
                    row['Category'],
                    row['Date'],
                    row['Description']
                )
                expenses.append(expense)
    except FileNotFoundError:
        pass # File will be created automatically
    return expenses




def backup_data():
    with open(FILE_NAME, 'r') as src:
        with open('backup/expenses_backup.csv', 'w') as dest:
            dest.write(src.read())