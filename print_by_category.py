import pickle

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

print("Expenses:")

i = 0
for item in expense_list:
    if item.category in ("Travel"):
        i += 1
        print(
            f"{i}. {item.date[0]}/{item.date[1]}/{item.date[2]} {item.category} {item.note} {item.quantity} ${item.cost} {item.tag}"
        )
