import json
from expense_functions import expense_string, income_string
from expense_module import Income, Expense


with open("all_expense.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [Expense(**entry) for entry in expense_list_data]

with open("all_income.json", "r") as f:
    income_list_data = json.load(f)

income_list = [Income(**entry) for entry in income_list_data]

print("Expenses:")

i = 0
for item in expense_list:
    i += 1
    print(f"{i}. " + expense_string(item))

print("=" * 100)
print("Income:")

i = 0
for item in income_list:
    i += 1
    print(f"{i}. " + income_string(item))


print("print for practicing merge")
