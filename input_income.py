from expense_module import Income
from expense_functions import what_income
import pickle
import datetime


# open the saved list
with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

amount = float(input("How much in dollar did you earn?: "))

category = what_income()

note = input("Please enter any notes: ")

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
new_income = Income(date, amount, category, note)

income_list.append(new_income)

with open("all_income.pickle", "wb") as file:
    pickle.dump(income_list, file)

print("New income has been recorded!")
