class ExpenseReport:
    def __init__(self):
        self.expense = None
        self.expense2 = None
        self.expense3 = None

    def generate_report(self):
        expenseLine = self.createExpenseLine(self.expense)
        expenseLine2 = self.createExpenseLine(self.expense2)
        expenseLine3 = self.createExpenseLine(self.expense3)

        return "| Date | Description | Amount | Balance |" + expenseLine + expenseLine2 + expenseLine3

    def createExpenseLine(self, expense):
        if expense == None:
            expenseLine = ""
        else:
            expenseLine = "| " + expense.date + " | " + expense.description + " | " + f"{expense.amount:.2f}" + " | " + f"{expense.balance:,.2f}" + " |"
        return expenseLine

    def initialize(self, date, description, amount, balance):
        if self.expense == None:
            self.expense = Expense(date, description, amount, balance)
        elif self.expense2 == None:
            self.expense2 = Expense(date, description, amount, balance)
        else:
            self.expense3 = Expense(date, description, amount, balance)


class Expense:
    def __init__(self, date, description, amount, balance):
        self.date = date
        self.description = description
        self.amount = amount
        self.balance = balance










