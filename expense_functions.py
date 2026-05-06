def ask_category():

    category_index = input(
        "What category does it belongs to?(Please enter a number) "
        "1. Eating & Drinking, 2. Housing, 3. Fees, 4. Travel: "
    )

    match category_index:
        case "1":
            category_index = input(
                "(Please enter a number) 1. Frozen Meat, 2. Frozen Vegetable, 3. Snacks, 4. Drinks: "
            )
            match category_index:
                case "1":
                    category = "Frozen Meat"
                case "2":
                    category = "Frozen Vegetable"
                case "3":
                    category = "Snacks"
                case "4":
                    category = "Dinks"
                case _:
                    category = "unknown category"
        case "2":
            category_index = input(
                "(Please enter a number) 1. Rent + Related Fixed Fee, 2. Laundry: "
            )
            match category_index:
                case "1":
                    category = "Rent + Related Fixed Fee"
                case "2":
                    category = "Laundry"
                case _:
                    category = "unknown category"
        case "3":
            category_index = input(
                "What type of fee?: (Please enter a number) "
                "1.Credit Card Annual Fee, 2. Tax Related Fee: "
            )
            match category_index:
                case "1":
                    category = "Credit Card Annual Fee"
                case "2":
                    category = "Tax Related Fee"
                case _:
                    category = "unknown category"
        case "4":
            category = "Travel"
        case _:
            category = "unknown category"

    return category


def what_income():
    category_index = input(
        "What category does it belongs to?(Please enter a number) 1. Salary, 2. Selling Used: "
    )

    match category_index:
        case "1":
            category = "Salary"
        case "2":
            category = "Selling Used"
        case _:
            category = "unknown category"

    return category
