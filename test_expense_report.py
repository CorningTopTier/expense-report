import unittest

from assertpy import assert_that

from expense_report import ExpenseReport


class ExpenseReportTests(unittest.TestCase):
    def test_should_output_date_description_amount_balance_when_the_expense_report_has_no_expenses(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense


        # When
        expense_report_output = expense_report.generate_report()

        # Then
        assert_that(expense_report_output, "export report").is_equal_to("| Date | Description | Amount | Balance |")

    def test_should_output_header_followed_by_expense_data_with_expense_report_with_one_gasoline_expense(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.initialize(date="6/05/1998", description="Gasoline", amount=52.25, balance=1586.24)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .ends_with("| 6/05/1998 | Gasoline | 52.25 | 1,586.24 |"))

    def test_should_output_header_followed_by_expense_data_with_expense_report_with_one_grocery_expense(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.initialize(date="6/05/1998", description="Groceries", amount=52.25, balance=1586.24)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .ends_with("| 6/05/1998 | Groceries | 52.25 | 1,586.24 |"))

    def test_should_output_header_followed_by_expense_data_with_expense_report_with_9_26_2024_expense(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.initialize(date="09/26/2024", description="Groceries", amount=52.25, balance=1586.24)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .ends_with("| 09/26/2024 | Groceries | 52.25 | 1,586.24 |"))




if __name__ == '__main__':
    unittest.main()
