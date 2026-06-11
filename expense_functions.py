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
        category_index = valid_input(message, valid_list)

        enter_index = int(category_index) - 1
        current_category = current_category.children[enter_index]

    category = current_category.name

    return category


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
    message = f"{entry.date[0]}/{entry.date[1]}/{entry.date[2]} {entry.category} {entry.note} {entry.quantity} ${entry.cost} {entry.tag}"
    return message


def income_string(entry):
    message = f"{entry.date[0]}/{entry.date[1]}/{entry.date[2]} {entry.category} {entry.note} ${entry.amount}"
    return message
