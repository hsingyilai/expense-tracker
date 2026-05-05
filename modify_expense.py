from expense_module import Expense
from expense_functions import ask_category
import pickle


with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

print("Expenses:")

i = 0
for item in expense_list:
    i += 1
    print(
        f"{i}. {item.date[0]}/{item.date[1]}/{item.date[2]} {item.category} {item.note} {item.quantity} ${item.cost}"
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
        del expense_list[entry_index]
    case "2":
        entry_index = (
            int(input("Which entry do you want to modify? (enter a number): ")) - 1
        )

        print("Please enter the updated information:")

        month = input("What month did you made this purchase?: ")
        day = input("What day did you made this purchase?: ")
        year = input("What year did you made this purchase?: ")

        date = [month, day, year]

        cost = float(input("How much in dollar does it cost?: "))

        main_category = ask_category()

        note = input("Please enter any notes: ")

        quantity = input("Please enter the quantity: ")

        tag = input("Please enter a tag: ")

        updated_expense = Expense(date, cost, main_category, note, quantity, tag)

        expense_list[entry_index] = updated_expense
    case _:
        print("Invalid Option.")
        valid_option = False


with open("all_expense.pickle", "wb") as file:
    pickle.dump(expense_list, file)

if valid_option:
    print("The expense list has been updated!")
else:
    print("Please start over again.")
