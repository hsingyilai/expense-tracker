import pickle

with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

with open("category_tree.pickle", "rb") as file:
    category_tree = pickle.load(file)

category_to_print = "Vegetable"

print(category_to_print + " expenses:")

for node in category_tree.descendants:
    if node.name == category_to_print:
        root_of_print = node

list_of_category_to_print = []
for node in root_of_print.descendants:
    list_of_category_to_print.append(node.name)

list_of_category_to_print.append(root_of_print.name)


i = 0
for item in expense_list:
    if item.category in list_of_category_to_print:
        i += 1
        print(
            f"{i}. {item.date[0]}/{item.date[1]}/{item.date[2]} {item.category} {item.note} {item.quantity} ${item.cost} {item.tag}"
        )
