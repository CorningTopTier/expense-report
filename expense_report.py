class ExpenseReport:
    def __init__(self):
        self.expense = None
        self.expense2 = None

    def generate_report(self):
        expenseLine = self.createExpenseLine(self.expense)
        expenseLine2 = self.createExpenseLine(self.expense2)

        return "| Date | Description | Amount | Balance |" + expenseLine + expenseLine2

    def createExpenseLine(self, expense):
        if expense == None:
            expenseLine2 = ""
        else:
            expenseLine2 = "| " + expense.date + " | " + expense.description + " | " + f"{expense.amount:.2f}" + " | " + f"{expense.balance:,.2f}" + " |"
        return expenseLine2

    def initialize(self, date, description, amount, balance):
        if self.expense == None:
            self.expense = Expense(date, description, amount, balance)
        else:
            self.expense2 = Expense(date, description, amount, balance)
        pass

class Expense:
    def __init__(self, date, description, amount, balance):
        self.date = date
        self.description = description
        self.amount = amount
        self.balance = balance










