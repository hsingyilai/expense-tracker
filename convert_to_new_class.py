import json
import datetime
from expense_module import Expense, ExpenseEntry


with open("all_expense.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [Expense(**entry) for entry in expense_list_data]

with open("irregular_expense_list.json", "r") as f:
    irregular_list = json.load(f)

updated_expense_list = []
i = 0
for entry in expense_list:
    date = datetime.date(int(entry.date[2]), int(entry.date[0]), int(entry.date[1]))
    note = {"note": entry.note, "quantity": entry.quantity, "tag": entry.tag}
    updated_expense_list.append(
        ExpenseEntry(str(date), entry.cost, entry.category, note, not irregular_list[i])
    )
    i += 1


expense_list_data = [vars(entry) for entry in updated_expense_list]
with open("my_expense.json", "w") as f:
    json.dump(expense_list_data, f, indent=4)
