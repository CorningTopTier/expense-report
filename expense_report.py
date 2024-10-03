class ExpenseReport:
    def __init__(self):
        self.expense_list = []

    def generate_report(self):
        if len(self.expense_list) > 0:
            expenseLine = self.createExpenseLine(self.expense_list[0])
        else:
            expenseLine = ""
        if len(self.expense_list) > 1:
            expenseLine2 = self.createExpenseLine(self.expense_list[1])
        else:
            expenseLine2 = ""
        if len(self.expense_list) > 2:
            expenseLine3 = self.createExpenseLine(self.expense_list[2])
        else:
            expenseLine3 = ""

        return "| Date | Description | Amount | Balance |" + expenseLine + expenseLine2 + expenseLine3

    def createExpenseLine(self, expense):
        if expense == None:
            expenseLine = ""
        else:
            expenseLine = "| " + expense.date + " | " + expense.description + " | " + f"{expense.amount:.2f}" + " | " + f"{expense.balance:,.2f}" + " |"
        return expenseLine

    def initialize(self, date, description, amount, balance):
        expense = Expense(date, description, amount, balance)
        self.expense_list.append(expense)


class Expense:
    def __init__(self, date, description, amount, balance):
        self.date = date
        self.description = description
        self.amount = amount
        self.balance = balance











