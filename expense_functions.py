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
            category = "Fees"
        case "4":
            category = "Travel"
        case _:
            category = "unknown category"

    return category
