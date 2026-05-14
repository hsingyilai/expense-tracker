def ask_category(category_tree):

    current_category = category_tree
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
