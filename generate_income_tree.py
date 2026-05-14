import pickle
from anytree import Node, RenderTree

all_income_type = Node("All Income Type")

salary = Node("Salary", parent=all_income_type)
selling_used = Node("Selling Used", parent=all_income_type)


print(RenderTree(all_income_type).by_attr())

with open("income_category_tree.pickle", "wb") as file:
    pickle.dump(all_income_type, file)
