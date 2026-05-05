from expense_module import Expense
import pickle

# open the saved list
with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

# get info
month = input("What month did you made this purchase?: ")
day = input("What day did you made this purchase?: ")
year = input("What year did you made this purchase?: ")

date = [month, day, year]

cost = float(input("How much in dollar does it cost?: "))

main_category_index = input(
    "What category does it belongs to?(Please enter a number) "
    "1. Drinks & Snacks, 2. Housing, 3. Fees, 4. Travel: "
)

match main_category_index:
    case "1":
        main_category = "Drinks & Snackes"
    case "2":
        main_category = "Housing"
    case "3":
        main_category = "Fees"
    case "4":
        main_category = "Travel"
    case _:
        main_category = "unknown category"

note = input("Please enter any notes: ")

quantity = input("Please enter the quantity: ")

tag = input("Please enter a tag: ")

# append the new expense
new_expense = Expense(date, cost, main_category, note, quantity, tag)

expense_list.append(new_expense)

with open("all_expense.pickle", "wb") as file:
    pickle.dump(expense_list, file)

print("New expense has been recorded!")
