#for categorywise summary
def show_summary(expenses):
    total = 0
    category_totals = {}

    for exp in expenses:
        total += exp.amount
        category_totals[exp.category] = (
            category_totals.get(exp.category, 0) + exp.amount
        )

    print("\n📊 EXPENSE SUMMARY")
    print("Total Spent: ₹", total)

    print("\nCategory-wise Spending:")
    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount}")

#for monthly analysis
def monthly_report(expenses, month, year):
    total = 0
    category_totals = {}

    for exp in expenses:
        exp_year, exp_month, _ = exp.date.split('-')

        if exp_year == year and exp_month == month:
            total += exp.amount
            category_totals[exp.category] = (
                category_totals.get(exp.category, 0) + exp.amount
            )

    print("\n📅 MONTHLY REPORT")
    print(f"Month: {month}-{year}")
    print("---------------------------")

    if total == 0:
        print("No expenses found for this month.")
        return

    print(f"Total Spent: ₹{total}\n")
    print("Category-wise Breakdown:")
    for cat, amt in category_totals.items():
        print(f"{cat}: ₹{amt}")

#for search expenses
def search_expenses(expenses, keyword):
    print("\n🔍 SEARCH RESULTS")
    print("---------------------------")

    found = False
    keyword = keyword.lower()

    for exp in expenses:
        if (
            keyword in exp.category.lower()
            or keyword in exp.description.lower()
            or keyword in exp.date
        ):
            print(exp)
            found = True

    if not found:
        print("No matching expenses found.")
