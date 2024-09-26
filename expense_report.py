class ExpenseReport:
    def __init__(self):
        self.hasExpense = False
        self.expenseDate = None
        self.expenseDescription = None
        self.expenseAmount = 0.00
        self.expenseBalance = 0.00
    def generate_report(self):
        if self.hasExpense:
            expenseLine = "| " + self.expenseDate + " | " + self.expenseDescription + " | " + f"{self.expenseAmount:.2f}" + " | " + f"{self.expenseBalance:,.2f}" + " |"
        else:
            expenseLine = ""
        return "| Date | Description | Amount | Balance |" + expenseLine

    def initialize(self, date, description, amount, balance):
        self.hasExpense = True
        self.expenseDate = date
        self.expenseDescription = description
        self.expenseAmount = amount
        self.expenseBalance = balance
        pass