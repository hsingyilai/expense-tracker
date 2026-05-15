import pickle
from anytree import PreOrderIter, PostOrderIter

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

with open("category_tree.pickle", "rb") as file:
    category_tree = pickle.load(file)

with open("income_category_tree.pickle", "rb") as file:
    all_income_type = pickle.load(file)

# sum the spending at the last child level
for category in PreOrderIter(category_tree):
    setattr(category, "total", 0)
    for entry in expense_list:
        if category.name == entry.category:
            category.total += entry.cost

# sum the spend of subcategories into categories
for category in PostOrderIter(category_tree):
    for child in category.children:
        category.total += child.total

for category in PreOrderIter(category_tree):
    category.total = round(category.total, 2)

print("Total spending in each category:")

for category in PreOrderIter(category_tree):
    print(f"{len(category.ancestors) * '   '}{category.name}: ${category.total}")

print("----------------------")

with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

with open("income_category_tree.pickle", "rb") as file:
    all_income_type = pickle.load(file)

# sum the spending at the last child level
for income_type in PreOrderIter(all_income_type):
    setattr(income_type, "total", 0)
    for entry in income_list:
        if income_type.name == entry.category:
            income_type.total += entry.amount

# sum the spend of subcategories into categories
for income_type in PostOrderIter(all_income_type):
    for child in income_type.children:
        income_type.total += child.total


for income_type in PreOrderIter(all_income_type):
    income_type.total = round(income_type.total, 2)

print("Total earning in each type of income:")

for income_type in PreOrderIter(all_income_type):
    print(
        f"{len(income_type.ancestors) * '   '}{income_type.name}: ${income_type.total}"
    )
