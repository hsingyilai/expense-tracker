# This script load samples for the user to get famaliar to this project
import json
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter
from expense_module import ExpenseEntry, IncomeEntry


# Load the sample expense list, income list and categories.
with open("sample_expenses.json", "r") as f:
    expense_list_data = json.load(f)

expense_list = [ExpenseEntry(**entry) for entry in expense_list_data]

with open("sample_incomes.json", "r") as f:
    income_list_data = json.load(f)

income_list = [IncomeEntry(**entry) for entry in income_list_data]

importer = JsonImporter()
with open("sample_expense_categories.json", "r") as f:
    expense_type = importer.read(f)

with open("sample_income_categories.json", "r") as f:
    income_type = importer.read(f)


# Save the samples as actual data
confirm = input(
    "This will overwrite the datas into the samples, are you sure you want to proceed? (Yes/No): "
)
if confirm == "Yes":
    with open("my_expenses.json", "w") as f:
        json.dump(expense_list_data, f, indent=4)

    exporter = JsonExporter(indent=2)
    all_category_json_string = exporter.export(expense_type)

    with open("expense_categories.json", "w") as f:
        f.write(all_category_json_string)

    income_list_data = [vars(entry) for entry in income_list]
    with open("my_incomes.json", "w") as f:
        json.dump(income_list_data, f, indent=4)

        all_category_json_string = exporter.export(income_type)

    with open("income_categories.json", "w") as f:
        f.write(all_category_json_string)

    print("The samples are loaded.")
else:
    print("The samples are not loaded.")
