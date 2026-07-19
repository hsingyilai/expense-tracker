import pickle
from expense_functions import expense_string, income_string


with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)


with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

print("Expenses:")

i = 0
for item in expense_list:
    i += 1
    print(f"{i}. " + expense_string(item))

print("==============================================")
print("Income:")

i = 0
for item in income_list:
    i += 1
    print(f"{i}. " + income_string(item))

print("Test Message")
