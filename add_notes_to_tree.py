from anytree import PreOrderIter
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter

importer = JsonImporter()

with open("category_tree.json", "r") as f:
    all_category = importer.read(f)

for category in PreOrderIter(all_category):
    category.notes = ["note"]

exporter = JsonExporter(indent=2)
all_category_json_string = exporter.export(all_category)

with open("expense_categories.json", "w") as f:
    f.write(all_category_json_string)
