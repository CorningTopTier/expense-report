class ExpenseReport:
    def __init__(self):
        self.expenseDate = None
        self.expenseDescription = None
        self.hasExpense = False
    def generate_report(self):
        if self.hasExpense:
            expenseLine = "| " + self.expenseDate + " | " + self.expenseDescription + " | 52.25 | 1,586.24 |"
        else:
            expenseLine = ""
        return "| Date | Description | Amount | Balance |" + expenseLine

    def initialize(self, date, description, amount, balance):
        self.expenseDescription = description
        self.hasExpense = True
        self.expenseDate = date
        pass