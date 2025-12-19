import re
from datetime import datetime


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than 0")
            else:
                return amount
        except ValueError:
            print("❌ Please enter a valid number")


def get_valid_category():
    while True:
        category = input("Enter category(Food/Transport/Entertainment/Shopping/Other): ").strip()
        if category.isalpha():
            return category
        else:
            print("❌ Category should contain only letters")


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("❌ Invalid date format. Use YYYY-MM-DD")


def get_valid_description():
    while True:
        description = input("Enter description: ").strip()
        if description:
            return description
        else:
            print("❌ Description cannot be empty")
