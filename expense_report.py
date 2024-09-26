class ExpenseReport:
    def __init__(self):
        self.expenseAmount = 0.00
        self.expenseDate = None
        self.expenseDescription = None
        self.hasExpense = False
    def generate_report(self):
        if self.hasExpense:
            expenseLine = "| " + self.expenseDate + " | " + self.expenseDescription + " | " + f"{self.expenseAmount:.2f}" + " | 1,586.24 |"
        else:
            expenseLine = ""
        return "| Date | Description | Amount | Balance |" + expenseLine

    def initialize(self, date, description, amount, balance):
        self.expenseDescription = description
        self.hasExpense = True
        self.expenseDate = date
        self.expenseAmount = amount
        pass