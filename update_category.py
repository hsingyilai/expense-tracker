# This script scan the expense list for a category and change it.
import json
from expense_module import ExpenseEntry

# Load the expense list.
with open("my_expenses.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [ExpenseEntry(**entry) for entry in expense_list_data]

# Scan and change the recorded category.
i = 0
for entry in expense_list:
    if (
        entry.category == "Frozen Vegetable"
    ):  # Change this to the category to be replaced.
        expense_list[i].category = "Vegetable"  # Change this to the new category.

    i += 1

# Save the new expense list.
expense_list_data = [vars(entry) for entry in expense_list]
with open("my_expenses.json", "w") as f:
    json.dump(expense_list_data, f, indent=4)
