from expense_module import ExpenseEntry
from expense_functions import ask_category, valid_input, expense_string
from anytree.importer import JsonImporter
from anytree import PreOrderIter
import json
import datetime

# open the saved list
with open("my_expenses.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [ExpenseEntry(**entry) for entry in expense_list_data]

importer = JsonImporter()
with open("expense_categories.json", "r") as f:
    category_tree = importer.read(f)

stage = 1  # for controlling which stage we're in
the_date = datetime.date.today()
while stage > 0:
    match stage:
        case 1:  # enter the cost
            valid_cost = False
            while not valid_cost:
                print('Enter "go back" to go back, "exit" to exit. ')
                cost_input = input("How much in dollar does it cost?: ")
                if cost_input == "go back":
                    try:
                        entry_in_edit = expense_list.pop()
                    except IndexError:
                        print("The expense list is empty, cannot go back.")
                        valid_cost = True
                    else:
                        valid_cost = True
                        stage = 4
                        print("")
                elif cost_input == "exit":
                    valid_cost = True
                    stage = -1
                    print("")
                else:
                    try:
                        cost = float(cost_input)
                    except ValueError:
                        print("Invalid Input. Please only enter a number.")
                    else:
                        valid_cost = True
                        # create the entry, with placeholders
                        entry_in_edit = ExpenseEntry(
                            str(the_date),
                            cost,
                            "Placeholder",
                            {"note": "The date is a placeholder"},
                            True,
                            "",
                        )
                        stage = 2
                        print("")
        case 2:  # enter the category
            print("Entry in edit:")
            print(expense_string(entry_in_edit))
            print('Enter "go back" to go back, "exit" to exit. ')
            print("Please choose the category.")
            category_node = ask_category(category_tree)
            if category_node == "exit":
                stage = -1
                print("")
            elif category_node == "go back":
                stage = 1
                print("")
            else:
                entry_in_edit.category = category_node.name
                stage = 3
                print("")

        case 3:  # enter notes
            for node in PreOrderIter(category_tree):
                if node.name == entry_in_edit.category:
                    category_node = node
            for key in category_node.notes:
                entry_in_edit.notes[key] = input(f"Please enter the {key}: ")
            stage = 4
            print("")
        case 4:  # decide next step
            print(f"The expense you will record is:\n{expense_string(entry_in_edit)}")
            print('Enter "go back" to go back, "exit" to save this entry and exit,')

            message = "Or choose from: 1. Change date, 2. Flag as "
            if entry_in_edit.regular:
                message += "irregular"
            else:
                message += "regular"
            message += ", 3. Link to a trip, 4. Save and record another expense on the same date. "

            response = valid_input(
                message,
                ["go back", "exit", "1", "2", "3", "4"],
            )
            match response:
                case "go back":
                    stage = 3
                    print("")
                case "exit":
                    stage = -1
                    expense_list.append(entry_in_edit)
                    expense_list_data = [vars(entry) for entry in expense_list]
                    with open("my_expenses.json", "w") as f:
                        json.dump(expense_list_data, f, indent=4)
                    print("\nThe expense:")
                    print(expense_string(entry_in_edit))
                    print("has been recorded!")
                case "1":
                    valid_date = False
                    while not valid_date:
                        entered_date = input(
                            "Please enter a date in the " + str(the_date) + " format: "
                        )
                        try:
                            the_date = datetime.date.fromisoformat(entered_date)
                        except ValueError:
                            print("Invalid Date.")
                        else:
                            valid_date = True
                            entry_in_edit.date = str(the_date)
                            print("")

                case "2":
                    entry_in_edit.regular = not entry_in_edit.regular
                    print("")
                case "3":
                    entry_in_edit.trip = input("Please enter the name of the trip: ")
                    print("")
                case "4":
                    expense_list.append(entry_in_edit)
                    expense_list_data = [vars(entry) for entry in expense_list]
                    with open("my_expenses.json", "w") as f:
                        json.dump(expense_list_data, f, indent=4)
                    print("\nThe expense:")
                    print(expense_string(entry_in_edit))
                    print("has been recorded!")
                    stage = 1
                    print("")
