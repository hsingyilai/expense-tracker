# This script is for the user to record an income.
from expense_module import IncomeEntry
from expense_functions import what_income
import json
from anytree.importer import JsonImporter
import datetime


# Load the saved list and categories.
try:
    with open("my_incomes.json", "r") as f:
        income_list_data = json.load(f)
except FileNotFoundError:
    print("Please run initialize_data.py first.")
else:
    income_list = [IncomeEntry(**entry) for entry in income_list_data]

    importer = JsonImporter()
    with open("income_categories.json", "r") as f:
        income_type = importer.read(f)

    # Start the input process.
    amount = float(input("How much in dollar did you earn?: "))

    category = what_income(income_type)

    note = input("Please enter any notes: ")

    is_today = input("Is this income receive today? : (1. Yes, 2. No) ")
    the_date = datetime.date.today()
    match is_today:
        case "1":
            date = str(the_date)
        case _:
            valid_date = False
            while not valid_date:
                entered_date = input(
                    "Please enter a date in the " + str(the_date) + " format: "
                )
                try:
                    the_date = datetime.date.fromisoformat(entered_date)
                except ValueError:
                    print("Invalid Date.")
                else:
                    valid_date = True
                    date = str(the_date)

    # Append the new income.
    new_income = IncomeEntry(date, amount, category, note)

    income_list.append(new_income)

    # Save the income list with new income.
    income_list_data = [vars(entry) for entry in income_list]
    with open("my_incomes.json", "w") as f:
        json.dump(income_list_data, f, indent=4)

    print("New income has been recorded!")
