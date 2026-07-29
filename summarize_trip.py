# This script summarized the expenses linked to a single trip.
import json
from anytree.importer import JsonImporter
from anytree import PreOrderIter, PostOrderIter
from expense_functions import valid_input
import matplotlib.pyplot as plt
from expense_module import ExpenseEntry

# Load the expense list and expense categories.
with open("my_expenses.json", "r") as file:
    expense_list_data = json.load(file)

expense_list = [ExpenseEntry(**entry) for entry in expense_list_data]

importer = JsonImporter()
with open("expense_categories.json", "r") as f:
    expense_type = importer.read(f)


# Create the list of trips for the user to select.
trip_list = []
for entry in expense_list:
    if entry.trip != "":
        trip_list.append(entry.trip)

trip_list = list(set(trip_list))
trip_list.sort()

if trip_list == []:
    print("There are no trips to summarize.")
else:
    # Ask which trip to summarize.
    message = "Please select a trip. "

    i = 0
    for trip in trip_list:
        i += 1
        message += str(i) + ". " + trip + ". "

    message += "(Please enter a number): "
    trip_selected = valid_input(message, [str(i) for i in range(1, len(trip_list) + 1)])

    # Remove all other entries from the list.
    new_expense_list = []
    for entry in expense_list:
        if entry.trip == trip_list[int(trip_selected) - 1]:
            new_expense_list.append(entry)

    expense_list = new_expense_list

    # Sum the spending at the last child level.
    for category in PreOrderIter(expense_type):
        setattr(category, "total", 0)
        for entry in expense_list:
            if category.name == entry.category:
                category.total += entry.cost

    # Sum the spending of subcategories into categories.
    for category in PostOrderIter(expense_type):
        for child in category.children:
            category.total += child.total

    for category in PreOrderIter(expense_type):
        category.total = round(category.total, 2)

    print("Total spending in each category:")
    total_category = []
    total_value = []
    for category in PreOrderIter(expense_type):
        if category.total > 0:
            print(
                f"{len(category.ancestors) * '   '}{category.name}: ${category.total}"
            )
            if len(category.children) == 0:
                total_category.append(category.name + f" ${category.total}")
                total_value.append(category.total)

    # Draw the pie charts.
    plot_title = trip_list[int(trip_selected) - 1]
    plt.pie(total_value, labels=total_category, autopct="%1.1f%%")
    plt.title(plot_title)
    plt.show()
