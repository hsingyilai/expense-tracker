import json
from expense_module import Expense

with open("all_expense.json", "r") as file:
    expense_list_data = json.load(file)

expense_list = [Expense(**entry) for entry in expense_list_data]

i = 0
for entry in expense_list:
    if entry.category == "Frozen Vegetable":
        expense_list[i].category = "Vegetable"

    i += 1

expense_list_data = [vars(entry) for entry in expense_list]
with open("all_expense.json", "w") as file:
    json.dump(expense_list_data, file, indent=4)
