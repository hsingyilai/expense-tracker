import json
import datetime
from expense_module import Expense, ExpenseEntry
from anytree import PreOrderIter
from anytree.importer import JsonImporter


with open("all_expense.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [Expense(**entry) for entry in expense_list_data]

with open("irregular_expense_list.json", "r") as f:
    irregular_list = json.load(f)

importer = JsonImporter()
with open("expense_categories.json", "r") as f:
    category_tree = importer.read(f)

updated_expense_list = []
i = 0
for entry in expense_list:
    date = datetime.date(int(entry.date[2]), int(entry.date[0]), int(entry.date[1]))
    list_of_notes = []
    for category in PreOrderIter(category_tree):
        if entry.category == category.name:
            list_of_notes = category.notes

    notes = {}
    for key in list_of_notes:
        notes[key] = ""

    if entry.category == "Meat":
        notes["quantity (weight)"] = entry.quantity
        notes["note"] = entry.note + " " + entry.tag
    elif entry.category == "Vegetable":
        notes["quantity (weight)"] = entry.quantity
        notes["note"] = entry.note + " " + entry.tag
    elif entry.category in [
        "Snacks",
        "Tea & Coffee",
        "Other Drinks",
        "Fruits",
        "Other Ingredients",
    ]:
        notes["quantity"] = entry.quantity
        notes["note"] = entry.note + " " + entry.tag
    else:
        notes["note"] = entry.note + " " + entry.tag + " " + entry.quantity

    updated_expense_list.append(
        ExpenseEntry(
            str(date), entry.cost, entry.category, notes, not irregular_list[i], ""
        )
    )
    i += 1


expense_list_data = [vars(entry) for entry in updated_expense_list]
with open("my_expenses.json", "w") as f:
    json.dump(expense_list_data, f, indent=4)
