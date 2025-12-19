from expense import Expense
from file_manager1 import save_expenses, load_expenses, backup_data
from utils1 import get_valid_amount,get_valid_category,get_valid_date,get_valid_description
from reports1 import show_summary,monthly_report,search_expenses
from menu import show_menu




def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Enter choice (1-7): ")
        
        if choice == '1':
            amount = get_valid_amount()
            category = get_valid_category()
            date = get_valid_date()
            description = get_valid_description()

            expenses.append(Expense(amount, category, date, description))
            save_expenses(expenses)
            print("✅ Expense added successfully")

        elif choice == '2':
            print("\n📋 ALL EXPENSES")
            for exp in expenses:
                print(exp)

        elif choice == '3':
            show_summary(expenses)

        elif choice == '4':
           month = input("Enter month (MM): ")
           year = input("Enter year (YYYY): ")
           monthly_report(expenses, month, year)

        elif choice == '5':
            keyword = input("Enter keyword (category/date/description): ")
            search_expenses(expenses, keyword)

        elif choice == '6':
            backup_data()
            print("📁 Backup created successfully")
            
        elif choice == '7':
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice")




if __name__ == '__main__':
    main()