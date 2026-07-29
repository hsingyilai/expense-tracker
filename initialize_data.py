# This script will initialize the data to empty.
import json
from anytree import Node
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter


expense_list = []
income_list = []
expense_type = Node("All Categories")
expense_type.notes = ["note"]

importer = JsonImporter()
with open("sample_income_categories.json", "r") as f:
    income_type = importer.read(f)


# Save the samples as actual data
confirm = input(
    "This will clear the datas, are you sure you want to proceed? (Yes/No): "
)
if confirm == "Yes":
    with open("my_expenses.json", "w") as f:
        json.dump(expense_list, f, indent=4)

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
