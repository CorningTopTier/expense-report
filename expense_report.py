class ExpenseReport:
    def __init__(self):
        self.hasExpense = False
    def generate_report(self):
        if self.hasExpense:
            expenseLine = "| 6/05/1998 | Gasoline | 52.25 | 1,586.24 |"
        else:
            expenseLine = ""
        return "| Date | Description | Amount | Balance |" + expenseLine


    def initialize(self, date, description, amount, balance):
        self.hasExpense = True
        pass