import pickle
from anytree import Node, RenderTree
from expense_functions import valid_input

with open("category_tree.pickle", "rb") as file:
    all_category = pickle.load(file)

print(RenderTree(all_category).by_attr())

current_category = all_category
category_index = ""
while category_index != "exit":
    message = ""
    i = 0
    for child_category in current_category.children:
        i += 1
        message += str(i) + ". " + child_category.name + " "

    message += "0. Add New Category (Please enter a number): "

    print("")
    print('Enter "exit" to end.')
    valid_list = [str(x) for x in range(0, i + 1)]
    valid_list.append("exit")
    category_index = valid_input(message, valid_list)

    if category_index == "0":
        name = input("Please enter the name of the new category: ")
        new_category = Node(name, parent=current_category)
    elif category_index != "exit":
        enter_index = int(category_index) - 1
        current_category = current_category.children[enter_index]

print(RenderTree(all_category).by_attr())

with open("category_tree.pickle", "wb") as file:
    pickle.dump(all_category, file)
