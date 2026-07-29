# Expense Tracker

## A collection of Python scripts to track and analyze expenses stored as .json files using terminal as user interface.

This project uses Python to track and analyze expenses. The expenses are stored in my_expenses.json, while the incomes are stored in my_incomes.json. The user can define categories stored in expense_categories.json and income_categories.json, with general tree structure implimented in the Python package anytree, so can have as many subcatories as you want. The main scripts include the following:

* enter_expense.py: Let the user enter expenses and append to the expense list, using the terminal as user interface. If the expense list need to modified, please edit my_expenses.json directly.
* enter_income.py: Similar to enter_expense.py, but for incomes.
* expense_categories_add.py: This let user add categories to the expense category tree. For income, the user need to directly edit my_incomes.json because most people have rather simple income types, compare to their expenses.
* initialize_data.py: This scripts wipe out all data stored in the expense list, income list and their categories, allowing a fresh start for new users.
* load_samples.py: This scripts load the sample expense list, income list, etc., to allow now users to play with the existing functions before they log in their real expenses.
* print_expenses_by_category.py: This print out the expenses in the selected catogry to the terminal.
* print_list.py: This simply print out all recored expenses and incomes in my_expenses.json and my_incomes.py, useful for debugging.
* summarize_trip.py: This script summarize the expenses linked to the selected trip.
* summarize.py: This summarize the expenses and incomes for either all time or a selected month. There is a build-in feature which if a category has "quantity (weight)" as one of the notes, it will compare prices by lb. However, the user need to record the quantities by weight with units supported by the Python package Pint.

Besides the scripts meant to be run by the user, expense_functions.py stores all the functions defined for this project, and expense_module.py stores all the classes defined for this project. The users are welcomed to write their own Python scripts to analyze their expenses in whatever way they want.

## Watch this demo video!
<://placeholder.com>

## How to use this expense tracker.

* Step 0. Have a way to run Python scripts on your device.
* Step 1. Download every files on the github repository.
* Step 2. Use pip install -r requirements.txt to install the required Python packages, or install them one by one when error messages show up.
* Step 3. Run load_samples.py, then play around with the scripts.
* Step 4. Run initialize_data.py, then you can start recording your own expenses!

## How to modify this project.

The expense list stores a Python list of elements in the ExpenseEntry class, defined in expense_module.py. People can write their own scripts to load it, following the codes in print_list.py or other existing scripts, and do whatever they want. Similarly, the income list stores IncomeEntry class object also defined in expense-module.py. The cateogoris implimented with anytree.Node object in the Python package anytree. All the above are stored as .json file, so using languages other than Python is possible.

## How to contribute.
If you want to share your script for any type of analysis, please create a new script with name different than the existing ones. If you want to modify an existing script, copy the code and create a new script. Please do not change the following file's name or format:

* my_expenses.json
* my_incomes.json
* income_categories.json
* expense_categories.json

If you have suggestions regarding the above file's format, please submit an issue or leave a comment.

## Known issues (Work in progress)

The terminal is not the best user interface. I am working using PyQt6 to have a GUI, the repository's link is here:
<://placeholder.com>

Currently there is no plan to turn this into an mobile app, as both Android and Apple requires some form of payment even just to put an app on my own phone. However, if this project get enough support I will consider this. Or people can take the ideas and do it themselve, this is definitely not this first expense tracker ever made.

## If you want to support me.
Here's my GitHub Sponsors profile:
< ://placeholder.com>





