class ExpenseReport:
    def __init__(self):
        self.expense_list = []
        self.beginningBalance = 0

    def generate_report(self):
        report_so_far = "| Date | Description | Amount | Balance |"
        currentBalance = self.beginningBalance
        for expense in self.expense_list:
            currentBalance = currentBalance - expense.amount
            expenseLine = self.createExpenseLine(expense, currentBalance)
            report_so_far = report_so_far + expenseLine
        return report_so_far

    def createExpenseLine(self, expense, currentBalance):
        if expense == None:
            expenseLine = ""
        else:
            expenseLine = "| " + expense.date + " | " + expense.description + " | " + f"{expense.amount:.2f}" + " | " + f"{currentBalance:,.2f}" + " |"
        return expenseLine

    def initialize(self, date, description, amount, balance=None):
        expense = Expense(date, description, amount, balance)
        self.expense_list.append(expense)


    def setBeginningBalance(self, beginningBalance):
        self.beginningBalance = beginningBalance


class Expense:
    def __init__(self, date, description, amount, balance):
        self.date = date
        self.description = description
        self.amount = amount
        self.balance = balance
