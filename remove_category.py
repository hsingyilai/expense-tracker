import pickle
from anytree import RenderTree


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

    message += '(Please enter a number or type "remove"): '

    category_index = input(message)

    if category_index == "remove":
        category_index = input("Which one to remove? (Please enter a number): ")
        enter_index = int(category_index) - 1
        current_category.children[enter_index].parent = None
    elif category_index != "exit":
        enter_index = int(category_index) - 1
        current_category = current_category.children[enter_index]

print(RenderTree(all_category).by_attr())

with open("category_tree.pickle", "wb") as file:
    pickle.dump(all_category, file)
