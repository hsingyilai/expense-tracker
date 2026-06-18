import pickle
from expense_functions import expense_string, valid_input


with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

with open("irregular_expense_list.pickle", "rb") as file:
    irregular_list = pickle.load(file)


# append the irregular expense list for new entries
for i in range(len(expense_list)):
    if i >= len(irregular_list):
        irregular_list.append(False)

# choose the range to flag
message = "What range fo date do you want to flag? 1. All time, 2. Specific month (Please enter a number): "
time_range = valid_input(message, ["1", "2"])

if time_range == "2":
    # figure out how many years
    year_list = []
    for entry in expense_list:
        year_list.append(int(entry.date[2]))

    year_list = list(set(year_list))
    year_list.sort()

    # figure out the months
    month_list = []  # store year in month in year*100+month integer format
    for entry in expense_list:
        for year in year_list:
            if int(entry.date[2]) == year:
                month_list.append(year * 100 + int(entry.date[0]))

    month_list = list(set(month_list))
    month_list.sort()

    # ask which month to summarize
    message = "Please select a month. "
    i = 0
    for month in month_list:
        i += 1
        message += str(i) + ". " + str(month % 100) + "/" + str(month // 100) + " "

    message += "(Please enter a number): "

    valid_response = False
    while not valid_response:
        month_selected = input(message)
        if month_selected in [str(x) for x in range(1, i + 1)]:
            valid_response = True
            month = str(month_list[int(month_selected) - 1] % 100)
            year = str(month_list[int(month_selected) - 1] // 100)
        else:
            print("Invalid option.")


index_to_flag = ""
while index_to_flag != "exit":
    print("Regualr expenses:")

    i = 0
    for item in expense_list:
        i += 1
        if not irregular_list[i - 1]:
            if time_range == "1":
                print(f"{i}. " + expense_string(item))
            elif time_range == "2":
                if item.date[0] == month and item.date[2] == year:
                    print(f"{i}. " + expense_string(item))

    print("======================================================")
    print("Irregular expenses:")

    i = 0
    for item in expense_list:
        i += 1
        if irregular_list[i - 1]:
            if time_range == "1":
                print(f"{i}. " + expense_string(item))
            elif time_range == "2":
                if item.date[0] == month and item.date[2] == year:
                    print(f"{i}. " + expense_string(item))

    print('Enter "exit" to stop.')
    index_to_flag = input("Which expense is irregular?: ")
    if index_to_flag != "exit":
        irregular_list[int(index_to_flag) - 1] = True

with open("irregular_expense_list.pickle", "wb") as file:
    pickle.dump(irregular_list, file)
