from expense_functions import ask_category, expense_string
import pickle
import json
import datetime
from expense_module import Expense


with open("all_expense.json", "r") as file:
    expense_list_data = json.load(file)

expense_list = [Expense(**entry) for entry in expense_list_data]

with open("category_tree.pickle", "rb") as file:
    category_tree = pickle.load(file)

print("Expenses:")

i = 0
for item in expense_list:
    i += 1
    print(f"{i}. " + expense_string(item))

option = input(
    "Do you want to: 1. delete an entry, or 2. modify an entry? (enter 1 or 2) "
)


valid_option = True
match option:
    case "1":
        entry_index = (
            int(input("Which entry do you want to delete? (enter a number): ")) - 1
        )
        del expense_list[entry_index]
    case "2":
        entry_index = (
            int(input("Which entry do you want to modify? (enter a number): ")) - 1
        )

        update_what = input(
            "What would you want to modify?"
            ": 1. date, 2. cost, 3. category, 4. note, 5. quantity, 6. tag "
        )
        match update_what:
            case "1":
                is_today = input("Is this perchase made today? : (1. Yes, 2. No) ")

                match is_today:
                    case "1":
                        today = datetime.datetime.now()
                        month = str(int(today.strftime("%m")))
                        day = str(int(today.strftime("%d")))
                        year = str(int(today.strftime("%Y")))
                        date = [month, day, year]
                    case _:
                        month = input("What month did you made this purchase?: ")
                        day = input("What day did you made this purchase?: ")
                        year = input("What year did you made this purchase?: ")
                        date = [month, day, year]

                expense_list[entry_index].date = date
            case "2":
                cost = float(input("How much in dollar does it cost?: "))
                expense_list[entry_index].cost = cost
            case "3":
                category = ask_category(category_tree)
                expense_list[entry_index].category = category
            case "4":
                note = input("Please enter any notes: ")
                expense_list[entry_index].note = note
            case "5":
                quantity = input("Please enter the quantity: ")
                expense_list[entry_index].quantity = quantity
            case "6":
                tag = input("Please enter a tag: ")
                expense_list[entry_index].tag = tag
            case _:
                print("Invalid Option.")
                valid_option = False

    case _:
        print("Invalid Option.")
        valid_option = False


expense_list_data = [vars(entry) for entry in expense_list]
with open("all_expense.json", "w") as file:
    json.dump(expense_list_data, file, indent=4)

if valid_option:
    print("The expense list has been updated!")
else:
    print("Please start over again.")
