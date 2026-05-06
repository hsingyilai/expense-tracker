from expense_module import Income
from expense_functions import what_income
import pickle


with open("all_income.pickle", "rb") as file:
    income_list = pickle.load(file)

print("Income:")

i = 0
for item in income_list:
    i += 1
    print(
        f"{i}. {item.date[0]}/{item.date[1]}/{item.date[2]} {item.category} {item.note} ${item.amount}"
    )

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

        month = input("What month did you receive this income?: ")
        day = input("What day did you receive this income?: ")
        year = input("What year did you receive this income?: ")

        date = [month, day, year]

        amount = float(input("How much in dollar did you earn?: "))

        category = what_income()

        note = input("Please enter any notes: ")

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
