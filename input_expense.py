from expense_module import Expense
from expense_functions import ask_category, valid_input, expense_string
from anytree.importer import JsonImporter
import json
import datetime


# open the saved list
with open("all_expense.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [Expense(**entry) for entry in expense_list_data]

importer = JsonImporter()
with open("category_tree.json", "r") as f:
    category_tree = importer.read(f)

enter_more = True
know_date = False
num_entry = 0
while enter_more:
    # get info
    valid_cost = False
    while not valid_cost:
        try:
            cost = float(input("How much in dollar does it cost?: "))
        except ValueError:
            print("Invalid Input. Please only enter a number.")
        else:
            valid_cost = True

    category = ask_category(category_tree)

    note = input("Please enter any notes: ")

    quantity = input("Please enter the quantity: ")

    tag = input("Please enter a tag: ")

    if not know_date:
        message = "Is this perchase made today? : (1. Yes, 2. No) "
        valid_list = ["1", "2"]
        is_today = valid_input(message, valid_list)

        match is_today:
            case "1":
                today = datetime.datetime.now()
                month = str(int(today.strftime("%m")))
                day = str(int(today.strftime("%d")))
                year = str(int(today.strftime("%Y")))
                date = [month, day, year]
            case _:
                month = valid_input(
                    "What month did you made this purchase?: ",
                    [str(i) for i in range(1, 13)],
                )

                match month:
                    case "1":
                        valid_list = [str(i) for i in range(1, 32)]
                    case "2":
                        valid_list = [str(i) for i in range(1, 30)]
                    case "3":
                        valid_list = [str(i) for i in range(1, 32)]
                    case "4":
                        valid_list = [str(i) for i in range(1, 31)]
                    case "5":
                        valid_list = [str(i) for i in range(1, 32)]
                    case "6":
                        valid_list = [str(i) for i in range(1, 31)]
                    case "7":
                        valid_list = [str(i) for i in range(1, 32)]
                    case "8":
                        valid_list = [str(i) for i in range(1, 32)]
                    case "9":
                        valid_list = [str(i) for i in range(1, 31)]
                    case "10":
                        valid_list = [str(i) for i in range(1, 32)]
                    case "11":
                        valid_list = [str(i) for i in range(1, 31)]
                    case "12":
                        valid_list = [str(i) for i in range(1, 32)]

                day = valid_input("What day did you made this purchase?: ", valid_list)

                valid_year = False
                while not valid_year:
                    year = input("What year did you made this purchase?: ")
                    if year.isdigit():
                        valid_year = True
                    else:
                        print("Please enter a positive integer.")

                date = [month, day, year]

    # append the new expense
    new_expense = Expense(date, cost, category, note, quantity, tag)
    num_entry += 1
    expense_list.append(new_expense)

    message = "Do you want to record another expense on the same day? 1. Yes, 2. No: "
    response = valid_input(message, ["1", "2"])

    if response == "2":
        enter_more = False
    else:
        know_date = True
        print(f"Please enter another spending on {date[0]}/{date[1]}/{date[2]}.")


expense_list_data = [vars(entry) for entry in expense_list]
with open("all_expense.json", "w") as f:
    json.dump(expense_list_data, f, indent=4)

print("The following expense(s) has been recorded!")
for index in range(1, num_entry + 1):
    message = str(index) + ". "
    message += expense_string(expense_list[-index])
    print(message)
