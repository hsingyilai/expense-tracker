import pickle

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

total = 0
for item in expense_list:
    total += float(item.cost)

total = round(total, 2)

print(f"Total spending is ${total}.")

print("Category breakdown:")

check_total = 0
total = 0
for item in expense_list:
    if item.category in (
        "Meat",
        "Vegetable",
        "Snacks",
        "Tea & Coffee",
        "Other Drinks",
        "Fruits",
        "Other Ingredients",
    ):
        total += float(item.cost)

total = round(total, 2)
print(f"Eating & Drinking: ${total}.")

check_total += total

total = 0
for item in expense_list:
    if item.category in (
        "Rent + Related Fixed Fee",
        "Laundry",
        "PG&E",
        "Other Housing Fee",
    ):
        total += float(item.cost)

total = round(total, 2)
print(f"Housing: ${total}.")

check_total += total

total = 0
for item in expense_list:
    if item.category in ("Credit Card Annual Fee", "Tax Related Fee"):
        total += float(item.cost)

total = round(total, 2)
print(f"Fees: ${total}.")

check_total += total

total = 0
for item in expense_list:
    if item.category in ("Travel"):
        total += float(item.cost)

total = round(total, 2)
print(f"Travel: ${total}.")

check_total += total

total = 0
for item in expense_list:
    if item.category in ("Bathroom Products", "Kitchen Products"):
        total += float(item.cost)

total = round(total, 2)
print(f"Home Consumables: ${total}.")

check_total += total

total = 0
for item in expense_list:
    if item.category in ("Dentist", "Other Medical"):
        total += float(item.cost)

total = round(total, 2)
print(f"Medical: ${total}.")

check_total += total
total = round(total, 2)
print(f"Check total: ${check_total}")

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
