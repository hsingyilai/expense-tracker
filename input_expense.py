from expense_module import Expense
from expense_functions import ask_category
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

main_category = ask_category()

note = input("Please enter any notes: ")

quantity = input("Please enter the quantity: ")

tag = input("Please enter a tag: ")

# append the new expense
new_expense = Expense(date, cost, main_category, note, quantity, tag)

expense_list.append(new_expense)

with open("all_expense.pickle", "wb") as file:
    pickle.dump(expense_list, file)

print("New expense has been recorded!")
