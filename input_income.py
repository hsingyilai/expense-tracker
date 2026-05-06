from expense_module import Income
from expense_functions import what_income
import pickle


# open the saved list
with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

# get info
month = input("What month did you receive this income?: ")
day = input("What day did you receive this income?: ")
year = input("What year did you receive this income?: ")

date = [month, day, year]

amount = float(input("How much in dollar did you earn?: "))

category = what_income()

note = input("Please enter any notes: ")

# append the new expense
new_income = Income(date, amount, category, note)

income_list.append(new_income)

with open("all_income.pickle", "wb") as file:
    pickle.dump(income_list, file)

print("New income has been recorded!")
