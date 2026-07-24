class Expense:
    '''An entry to the expense list

    This class is the skeleton for recording an expense

    Attributes:
        date: A datetime.date object converted to string in standard ISO format, such as "2026-07-23".
        cost: How much money does it cost in dollar.
        category: What category does this expense belongs to.
        note: Things that you want to take notes on according to the category it belongs to.
        regular: True if it is a regular expense.
    '''
    def __init__(self, date: str, cost: float, category: str, note: dict, regular: bool):
        self.date = date
        self.cost = cost
        self.category = category
        self.note = note
        self.regular = regular



class Income:
    def __init__(self, date, amount, category, note):
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note


class ExpenseEntry:
    '''An entry to the expense list

    This class is the skeleton for recording an expense

    Attributes:
        date: A datetime.date object converted to string in standard ISO format, such as "2026-07-23".
        cost: How much money does it cost in dollar.
        category: What category does this expense belongs to.
        note: Things that you want to take notes on according to the category it belongs to.
        regular: True if it is a regular expense.
    '''
    def __init__(self, date: str, cost: float, category: str, note: dict, regular: bool):
        self.date = date
        self.cost = cost
        self.category = category
        self.note = note
        self.regular = regular
