from anytree.exporter import JsonExporter
from anytree import Node, RenderTree

all_income_type = Node("All Income Type")

salary = Node("Salary", parent=all_income_type)
selling_used = Node("Selling Used", parent=all_income_type)


print(RenderTree(all_income_type).by_attr())

exporter = JsonExporter(indent=2)
all_income_type_json_string = exporter.export(all_income_type)

with open("income_category_tree.json", "w") as f:
    f.write(all_income_type_json_string)
