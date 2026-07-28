import datetime


def valid_input(message, valid_list):
    valid = False
    while not valid:
        input_string = input(message)
        if input_string in valid_list:
            valid = True
        else:
            print("Invalid input.")
    return input_string


def ask_category(category_tree):
    current_category = category_tree
    while current_category.children:
        message = ""
        i = 0
        for child_category in current_category.children:
            i += 1
            message += str(i) + ". " + child_category.name + " "

        message += "(Please enter a number): "

        valid_list = [str(i) for i in range(1, i + 1)]
        valid_list.append("exit")
        valid_list.append("go back")
        category_index = valid_input(message, valid_list)
        if category_index == "exit":
            return "exit"
        elif category_index == "go back":
            return "go back"
        else:
            enter_index = int(category_index) - 1
            current_category = current_category.children[enter_index]

    return current_category


def what_income(all_income_type):
    current_category = all_income_type

    while current_category.children:
        message = ""
        i = 0
        for child_category in current_category.children:
            i += 1
            message += str(i) + ". " + child_category.name + " "

        message += "(Please enter a number): "

        category_index = input(message)

        enter_index = int(category_index) - 1
        current_category = current_category.children[enter_index]

    category = current_category.name

    return category


def expense_string(entry):
    date = datetime.date.fromisoformat(entry.date)
    message = (
        f"{date.strftime("%m/%d/%Y")} {entry.category} ${entry.cost} {entry.notes} "
    )
    if not entry.regular:
        message += "Irregular"
    if entry.trip != "":
        message += f" Trip: {entry.trip}"
    return message


def income_string(entry):
    message = f"{entry.date[0]}/{entry.date[1]}/{entry.date[2]} {entry.category} {entry.note} ${entry.amount}"
    return message


def add_note(new_category):
    choice = valid_input("Do you want to add another note? 1. Yes, 2. No: ", ["1", "2"])
    if choice == "1":
        new_note = input("Please enter the name of the note: ")
        new_category.notes.append(new_note)
        add_note(new_category)
