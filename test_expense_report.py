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


if __name__ == '__main__':
    unittest.main()
