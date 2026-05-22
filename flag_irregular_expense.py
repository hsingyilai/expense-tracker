import pickle
from expense_functions import expense_string


with open("all_expense.pickle", "rb") as file:
    expense_list = pickle.load(file)

with open("irregular_expense_list.pickle", "rb") as file:
    irregular_list = pickle.load(file)


# append the irregular expense list for new entries
for i in range(len(expense_list)):
    if i >= len(irregular_list):
        irregular_list.append(False)


index_to_flag = ""
while index_to_flag != "exit":
    print("Regualr expenses:")

    i = 0
    for item in expense_list:
        i += 1
        if not irregular_list[i - 1]:
            print(f"{i}. " + expense_string(item))

    print("Irregular expenses:")

    i = 0
    for item in expense_list:
        i += 1
        if irregular_list[i - 1]:
            print(f"{i}. " + expense_string(item))

    print('Enter "exit" to stop.')
    index_to_flag = input("Which expense is irregular?: ")
    if index_to_flag != "exit":
        irregular_list[int(index_to_flag) - 1] = True

with open("irregular_expense_list.pickle", "wb") as file:
    pickle.dump(irregular_list, file)
