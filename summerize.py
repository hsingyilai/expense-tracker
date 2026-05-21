import pickle
from anytree import PreOrderIter, PostOrderIter
from pint import UnitRegistry

ureg = UnitRegistry()
Q_ = ureg.Quantity

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

print("----------------------")

cheapest_meat_per_lb = -1
most_expensive = 0
total_meat_weight = 0
total_meat_cost = 0
i = -1
for entry in expense_list:
    i += 1
    if entry.category == "Meat":
        weight_in_lb = Q_(entry.quantity).to("lb")
        price_per_lb = entry.cost / weight_in_lb.magnitude
        total_meat_weight += weight_in_lb.magnitude
        total_meat_cost += entry.cost
        if cheapest_meat_per_lb < 0 or price_per_lb < cheapest_meat_per_lb:
            cheapest_meat_per_lb = price_per_lb
            cheapest_meat_index = i
        if price_per_lb > most_expensive:
            most_expensive = price_per_lb
            most_expensive_index = i

print(
    f"The cheapest meat is: ${round(cheapest_meat_per_lb, 2)} per pound, with the following purchase:"
)
entry = expense_list[cheapest_meat_index]
print(
    f"{entry.date[0]}/{entry.date[1]}/{entry.date[2]} {entry.category} {entry.note} {entry.quantity} ${entry.cost} {entry.tag}"
)
print(
    f"The most expensive meat is: ${round(most_expensive, 2)} per pound, with the following purchase:"
)
entry = expense_list[most_expensive_index]
print(
    f"{entry.date[0]}/{entry.date[1]}/{entry.date[2]} {entry.category} {entry.note} {entry.quantity} ${entry.cost} {entry.tag}"
)
print(
    f"You bought {round(total_meat_weight, 1)} lb of meat in total, ${round(total_meat_cost / total_meat_weight, 2)} per pound on average."
)
print(
    f"You can save ${round(total_meat_cost - total_meat_cost / total_meat_weight, 2)} if you stick with the cheapest option."
)

print("----------------------")

cheapest_vege_per_lb = -1
most_expensive = 0
total_vege_weight = 0
total_vege_cost = 0
i = -1
for entry in expense_list:
    i += 1
    if entry.category == "Vegetable":
        weight_in_lb = Q_(entry.quantity).to("lb")
        price_per_lb = entry.cost / weight_in_lb.magnitude
        total_vege_weight += weight_in_lb.magnitude
        total_vege_cost += entry.cost
        if cheapest_vege_per_lb < 0 or price_per_lb < cheapest_vege_per_lb:
            cheapest_vege_per_lb = price_per_lb
            cheapest_vege_index = i
        if price_per_lb > most_expensive:
            most_expensive = price_per_lb
            most_expensive_index = i

print(
    f"The cheapest vegetable is: ${round(cheapest_vege_per_lb, 2)} per pound, with the following purchase:"
)
entry = expense_list[cheapest_vege_index]
print(
    f"{entry.date[0]}/{entry.date[1]}/{entry.date[2]} {entry.category} {entry.note} {entry.quantity} ${entry.cost} {entry.tag}"
)
print(
    f"The most expensive vegetable is: ${round(most_expensive, 2)} per pound, with the following purchase:"
)
entry = expense_list[most_expensive_index]
print(
    f"{entry.date[0]}/{entry.date[1]}/{entry.date[2]} {entry.category} {entry.note} {entry.quantity} ${entry.cost} {entry.tag}"
)
print(
    f"You bought {round(total_vege_weight, 1)} lb of vegetable in total, ${round(total_vege_cost / total_vege_weight, 2)} per pound on average."
)
print(
    f"You can save ${round(total_vege_cost - total_vege_cost / total_vege_weight, 2)} if you stick with the cheapest option."
)
