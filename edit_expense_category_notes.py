from anytree.importer import JsonImporter
from anytree.exporter import JsonExporter


importer = JsonImporter()
with open("expense_categories.json", "r") as f:
    category_tree = importer.read(f)

current_category = category_tree
next_layer = True
while next_layer:
    message = "Which category do you want to edit?: "
    i = 0
    for child_category in current_category.children:
        i += 1
        message += str(i) + ". " + child_category.name + " "

    message += "(Please enter a number): "

    category_index = input(message)

    enter_index = int(category_index) - 1

    choice = current_category.children[enter_index]

    valid_input = False
    while not valid_input:
        decided = input(
            f"Do you want to: 1. Edit the note of {choice.name}, "
            f"2. Choose from the subcateogries of {choice.name}? (Please enter a number): "
        )

        if decided == "1":
            valid_input = True
            next_layer = False
            category_to_edit = choice
        elif decided == "2":
            if not choice.children:
                print("There is no more subcategory.")
            else:
                current_category = choice
                valid_input = True
        else:
            print("Not a valid option.")

print("The notes for this category are:")
print(choice.notes)

note_to_add = input("What other note do you want to take for this category?")

choice.notes.append(note_to_add)

print("The notes for this category are now:")
print(choice.notes)

exporter = JsonExporter(indent=2)
all_category_json_string = exporter.export(category_tree)

with open("expense_categories.json", "w") as f:
    f.write(all_category_json_string)
