from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter
from anytree import RenderTree

importer = JsonImporter()
with open("category_tree.json", "r") as f:
    all_category = importer.read(f)

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

    print("")
    print('Enter "exit" to end.')
    category_index = input(message)

    if category_index == "remove":
        category_index = input("Which one to remove? (Please enter a number): ")
        enter_index = int(category_index) - 1
        current_category.children[enter_index].parent = None
    elif category_index != "exit":
        enter_index = int(category_index) - 1
        current_category = current_category.children[enter_index]

print(RenderTree(all_category).by_attr())


exporter = JsonExporter(indent=2)
all_category_json_string = exporter.export(all_category)

with open("category_tree.json", "w") as f:
    f.write(all_category_json_string)
