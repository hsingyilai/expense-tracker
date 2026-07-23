import pickle
import json

# income list
with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)


income_list_data = [vars(entry) for entry in income_list]

with open("all_income.json", "w") as file:
    json.dump(income_list_data, file, indent=4)

# expense list
with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)


expense_list_data = [vars(entry) for entry in expense_list]

with open("all_expense.json", "w") as file:
    json.dump(expense_list_data, file, indent=4)

# irregular list
with open("irregular_expense_list.pickle", "rb") as file:
    irregular_expense_list = pickle.load(file)

with open("irregular_expense_list.json", "w") as file:
    json.dump(irregular_expense_list, file, indent=4)
