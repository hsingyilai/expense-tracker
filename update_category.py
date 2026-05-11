import pickle

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

i = 0
for entry in expense_list:
    if entry.category == "Frozen Vegetable":
        expense_list[i].category = "Vegetable"

    i += 1

with open("all_expense.pickle", "wb") as file:
    pickle.dump(expense_list, file)
