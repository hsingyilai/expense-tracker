import pickle

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

total = 0
for item in expense_list:
    total += float(item.cost)

total = round(total, 2)

print(f"Total spending is ${total}.")
