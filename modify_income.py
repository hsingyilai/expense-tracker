from expense_module import Income
from expense_functions import what_income, income_string
import pickle
import datetime


with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

with open("income_category_tree.pickle", "rb") as file:
    all_income_type = pickle.load(file)

print("Income:")

i = 0
for item in income_list:
    i += 1
    print(f"{i}. " + income_string(item))

option = input(
    "Do you want to: 1. delete an entry, or 2. modify an entry? (enter 1 or 2) "
)


valid_option = True
match option:
    case "1":
        entry_index = (
            int(input("Which entry do you want to delete? (enter a number): ")) - 1
        )
        del income_list[entry_index]
    case "2":
        entry_index = (
            int(input("Which entry do you want to modify? (enter a number): ")) - 1
        )

        print("Please enter the updated information:")

        amount = float(input("How much in dollar did you earn?: "))

        category = what_income(all_income_type)

        note = input("Please enter any notes: ")

        is_today = input("Is this income receive today? : (1. Yes, 2. No) ")

        match is_today:
            case "1":
                today = datetime.datetime.now()
                month = str(int(today.strftime("%m")))
                day = str(int(today.strftime("%d")))
                year = str(int(today.strftime("%Y")))
                date = [month, day, year]
            case _:
                month = input("What month did you receive it?: ")
                day = input("What day did you receive it?: ")
                year = input("What year did you receive it?: ")
                date = [month, day, year]

        # append the new expense
        updated_income = Income(date, amount, category, note)

        income_list[entry_index] = updated_income
    case _:
        print("Invalid Option.")
        valid_option = False

with open("all_income.pickle", "wb") as file:
    pickle.dump(income_list, file)

if valid_option:
    print("The income list has been updated!")
else:
    print("Please start over again.")
