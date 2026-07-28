import json
from expense_module import ExpenseEntry

with open("my_expenses.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [ExpenseEntry(**entry) for entry in expense_list_data]

i = 0
for entry in expense_list:
    if entry.category == "Frozen Vegetable":
        expense_list[i].category = "Vegetable"

    i += 1

expense_list_data = [vars(entry) for entry in expense_list]
with open("my_expenses.json", "w") as f:
    json.dump(expense_list_data, f, indent=4)
