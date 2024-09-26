class ExpenseReport:
    def __init__(self):
        self.expense = None
        self.hasExpense = False
        self.expenseDate = None
        self.expenseDescription = None
        self.expenseAmount = 0.00
        self.expenseBalance = 0.00
    def generate_report(self):
        if self.hasExpense:
            expenseLine = "| " + self.expenseDate + " | " + self.expenseDescription + " | " + f"{self.expenseAmount:.2f}" + " | " + f"{self.expenseBalance:,.2f}" + " |"
            expenseLine2 = "| " + self.expenseDate + " | " + self.expenseDescription + " | " + f"{self.expenseAmount:.2f}" + " | " + f"{self.expenseBalance:,.2f}" + " |"

        else:
            expenseLine = ""
            expenseLine2 = ""
        return "| Date | Description | Amount | Balance |" + expenseLine + expenseLine2

    def initialize(self, date, description, amount, balance):
        self.hasExpense = True
        self.expense = Expense()
        self.expenseDate = date
        self.expenseDescription = description
        self.expenseAmount = amount
        self.expenseBalance = balance
        pass

class Expense:
    def __init__(self):
        self.expenseDate = None
        self.expenseDescription = None
        self.expenseAmount = 0.00
        self.expenseBalance = 0.00










