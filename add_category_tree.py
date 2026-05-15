import pickle
from anytree import Node, RenderTree

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
    category_index = input(message)

    if category_index == "0":
        name = input("Please enter the name of the new category: ")
        new_category = Node(name, parent=current_category)
    elif category_index != "exit":
        enter_index = int(category_index) - 1
        current_category = current_category.children[enter_index]

print(RenderTree(all_category).by_attr())

with open("category_tree.pickle", "wb") as file:
    pickle.dump(all_category, file)
