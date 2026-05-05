import pickle

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)


with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

print("Expenses:")

for item in expense_list:
    print(
        f"{item.date[0]}/{item.date[1]}/{item.date[2]} {item.note} {item.quantity} ${item.cost}"
    )

print("Income:")

for item in income_list:
    print(
        f"{item.date[0]}/{item.date[1]}/{item.date[2]} {item.category} {item.note} ${item.amount}"
    )
