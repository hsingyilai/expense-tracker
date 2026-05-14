from expense_module import Expense
from expense_functions import ask_category
import pickle
import datetime


# open the saved list
with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

with open("category_tree.pickle", "rb") as file:
    category_tree = pickle.load(file)

# get info
cost = float(input("How much in dollar does it cost?: "))

category = ask_category(category_tree)

note = input("Please enter any notes: ")

quantity = input("Please enter the quantity: ")

tag = input("Please enter a tag: ")

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

# append the new expense
new_expense = Expense(date, cost, category, note, quantity, tag)

expense_list.append(new_expense)

with open("all_expense.pickle", "wb") as file:
    pickle.dump(expense_list, file)

print("New expense has been recorded!")
