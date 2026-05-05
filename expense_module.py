class Expense:
    def __init__(self, date, cost, category, note, quantity, tag):
        self.date = date
        self.cost = cost
        self.category = category
        self.note = note
        self.quantity = quantity
        self.tag = tag


class Income:
    def __init__(self, date, amount, category, note):
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note
