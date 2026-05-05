import pickle

# open the saved list
with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

del expense_list[3]

with open("all_expense.pickle", "wb") as file:
    pickle.dump(expense_list, file)
