def ask_category():

    category_index = input(
        "What category does it belongs to?(Please enter a number) "
        "1. Drinks & Snacks, 2. Housing, 3. Fees, 4. Travel: "
    )

    match category_index:
        case "1":
            category = "Drinks & Snackes"
        case "2":
            category = "Housing"
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
        "What category does it belongs to?(Please enter a number) 1. Salary: "
    )

    match category_index:
        case "1":
            category = "Salary"
        case _:
            category = "unknown category"

    return category
