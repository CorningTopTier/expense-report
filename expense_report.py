class ExpenseReport:
    def __init__(self):
        self.expense = None
        self.expense2 = None
        self.hasExpense = False

    def generate_report(self):
        if self.expense2 !=None:
            expenseLine2 = "| " + self.expense2.date + " | " + self.expense2.description + " | " + f"{self.expense2.amount:.2f}" + " | " + f"{self.expense2.balance:,.2f}" + " |"
        else:
            expenseLine2 = ""
        if self.hasExpense:
            expenseLine = "| " + self.expense.date + " | " + self.expense.description + " | " + f"{self.expense.amount:.2f}" + " | " + f"{self.expense.balance:,.2f}" + " |"

        else:
            expenseLine = ""
            expenseLine2 = ""
        return "| Date | Description | Amount | Balance |" + expenseLine + expenseLine2

    def initialize(self, date, description, amount, balance):
        self.hasExpense = True
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










