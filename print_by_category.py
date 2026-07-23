import pickle
import json
from expense_module import Expense
from expense_functions import expense_string


with open("all_expense.json", "r") as file:
    expense_list_data = json.load(file)

expense_list = [Expense(**entry) for entry in expense_list_data]

with open("category_tree.pickle", "rb") as file:
    category_tree = pickle.load(file)


current_category = category_tree
next_layer = True
while next_layer:
    message = "Which category of expenses do you want to print?: "
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
            f"Do you want to: 1. Print Expenses in {choice.name}, "
            f"2. Choose from the subcateogries of {choice.name}? (Please enter a number): "
        )

        if decided == "1":
            valid_input = True
            next_layer = False
            category_to_print = choice.name
        elif decided == "2":
            if not choice.children:
                print("There is no more subcategory.")
            else:
                current_category = choice
                valid_input = True
        else:
            print("Not a valid option.")

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
        print(f"{i}. " + expense_string(item))
