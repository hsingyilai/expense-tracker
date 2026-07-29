# This script simply print out all the recored expenses and incomes.
import json
from expense_functions import expense_string, income_string
from expense_module import IncomeEntry, ExpenseEntry

# Load the expense list and income list.
try:
    with open("my_expenses.json", "r") as f:
        expense_list_data = json.load(f)
except FileNotFoundError:
    print("Please run initialize_data.py first.")
else:
    expense_list = [ExpenseEntry(**entry) for entry in expense_list_data]

    with open("my_incomes.json", "r") as f:
        income_list_data = json.load(f)

    income_list = [IncomeEntry(**entry) for entry in income_list_data]

    # Print the expenses.
    print("Expenses:")

    i = 0
    for item in expense_list:
        i += 1
        print(f"{i}. " + expense_string(item))

    print("=" * 100)

    # Print the incomes.
    print("Income:")

    i = 0
    for item in income_list:
        i += 1
        print(f"{i}. " + income_string(item))
