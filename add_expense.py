import pickle

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

total = 0
for item in expense_list:
    total += float(item.cost)

total = round(total, 2)

print(f"Total spending is ${total}.")

print("Category breakdown:")

total = 0
for item in expense_list:
    if item.category in (
        "Frozen Meat",
        "Frozen Vegetable",
        "Snacks",
        "Tea & Coffee",
        "Other Drinks",
        "Fruits",
    ):
        total += float(item.cost)

total = round(total, 2)
print(f"Eating & Drinking: ${total}.")

total = 0
for item in expense_list:
    if item.category in ("Rent + Related Fixed Fee", "Laundry"):
        total += float(item.cost)

total = round(total, 2)
print(f"Housing: ${total}.")

total = 0
for item in expense_list:
    if item.category in ("Credit Card Annual Fee", "Tax Related Fee"):
        total += float(item.cost)

total = round(total, 2)
print(f"Fees: ${total}.")

total = 0
for item in expense_list:
    if item.category in ("Travel"):
        total += float(item.cost)

total = round(total, 2)
print(f"Travel: ${total}.")

total = 0
for item in expense_list:
    if item.category in ("Bathroom Products", "Kitchen Products"):
        total += float(item.cost)

total = round(total, 2)
print(f"Home Consumables: ${total}.")

total = 0
for item in expense_list:
    if item.category in ("Dentist", "Other Medical"):
        total += float(item.cost)

total = round(total, 2)
print(f"Medical: ${total}.")

print("----------------------")

with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

total = 0
for item in income_list:
    total += float(item.amount)

total = round(total, 2)

print(f"Total income is ${total}.")

print("Category breakdown:")

total = 0
for item in income_list:
    if item.category in ("Salary"):
        total += float(item.amount)

total = round(total, 2)
print(f"Salary: ${total}.")

total = 0
for item in income_list:
    if item.category in ("Selling Used"):
        total += float(item.amount)

total = round(total, 2)
print(f"Selling Used: ${total}.")
