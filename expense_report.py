class ExpenseReport:
    def __init__(self):
        self.expense = None
        self.hasExpense = False

    def generate_report(self):
        if self.hasExpense:
            expenseLine = "| " + self.expense.date + " | " + self.expense.description + " | " + f"{self.expense.amount:.2f}" + " | " + f"{self.expense.balance:,.2f}" + " |"
            expenseLine2 = "| " + self.expense.date + " | " + self.expense.description + " | " + f"{self.expense.amount:.2f}" + " | " + f"{self.expense.balance:,.2f}" + " |"

        else:
            expenseLine = ""
            expenseLine2 = ""
        return "| Date | Description | Amount | Balance |" + expenseLine + expenseLine2

    def initialize(self, date, description, amount, balance):
        self.hasExpense = True
        self.expense = Expense(date, description, amount, balance)
        pass

class Expense:
    def __init__(self, date, description, amount, balance):
        self.date = date
        self.description = description
        self.amount = amount
        self.balance = balance










