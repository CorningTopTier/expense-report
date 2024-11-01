import unittest

from assertpy import assert_that

from expense_report import ExpenseReport

import custom_string_assert

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
        expense_report.setBeginningBalance(1586.24 + 52.25)
        expense_report.initialize(date="6/05/1998", description="Gasoline", amount=52.25)
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
        expense_report.setBeginningBalance(1586.24 + 52.25)
        expense_report.initialize(date="6/05/1998", description="Groceries", amount=52.25)
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
        expense_report.setBeginningBalance(1586.24 + 52.25)
        expense_report.initialize(date="09/26/2024", description="Groceries", amount=52.25)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .ends_with("| 09/26/2024 | Groceries | 52.25 | 1,586.24 |"))

    def test_should_output_header_followed_by_expense_data_with_expense_report_with_99_00_in_amount(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.setBeginningBalance(1586.24 + 99.00)
        expense_report.initialize(date="09/26/2024", description="Groceries", amount=99.00)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .ends_with("| 09/26/2024 | Groceries | 99.00 | 1,586.24 |"))

    def test_should_output_header_followed_by_expense_data_with_expense_report_with_1000_00_in_balance(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.setBeginningBalance(1099.00)
        expense_report.initialize("09/26/2024", "Groceries", 99.00)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .ends_with("| 09/26/2024 | Groceries | 99.00 | 1,000.00 |"))

    def test_should_output_header_followed_by_the_first_expense_then_the_second_expense(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.setBeginningBalance(1035.00)
        expense_report.initialize("09/25/2024", "Movies", 35.00)
        expense_report.initialize("09/26/2024", "Groceries", 99.00)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .contains("| 09/25/2024 | Movies | 35.00 | 1,000.00 |")
            .ends_with("| 09/26/2024 | Groceries | 99.00 | 901.00 |"))

    def test_should_output_header_followed_by_three_expenses(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.setBeginningBalance(1035.00)
        expense_report.initialize("09/25/2024", "Movies", 35.00)
        expense_report.initialize("09/26/2024", "Groceries", 99.00)
        expense_report.initialize("10/03/2024", "Car Repair", 450.00)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .contains("| 09/25/2024 | Movies | 35.00 | 1,000.00 |")
            .contains("| 09/26/2024 | Groceries | 99.00 | 901.00 |")
            .ends_with("| 10/03/2024 | Car Repair | 450.00 | 451.00 |"))

    def test_should_output_header_followed_by_three_expenses_when_using_a_starting_balance_and_not_providing_expense_balances(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.setBeginningBalance(1035.00)
        expense_report.initialize("09/25/2024", "Movies", 35.00)
        expense_report.initialize("09/26/2024", "Groceries", 99.00)
        expense_report.initialize("10/03/2024", "Car Repair", 450.00)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .contains("| 09/25/2024 | Movies | 35.00 | 1,000.00 |")
            .contains("| 09/26/2024 | Groceries | 99.00 | 901.00 |")
            .ends_with("| 10/03/2024 | Car Repair | 450.00 | 451.00 |"))

        (assert_that(expense_report_output, "export report")
         .is_equal_to_with_diff("""\
| Date | Description | Amount | Balance |
| 09/25/2024 | Movies | 35.00 | 1,000.00 |
| 09/26/2024 | Groceries | 99.00 | 901.00 |
| 10/03/2024 | Car Repair | 450.00 | 451.00 |"""))


    def test_should_output_header_followed_by_three_expenses_in_date_order(self):
        # Given
            # an expense report without any expense
        expense_report = ExpenseReport()  # an expense report without any expense
        expense_report.setBeginningBalance(1035.00)
        expense_report.initialize("09/26/2024", "Groceries", 99.00)
        expense_report.initialize("10/03/2024", "Car Repair", 450.00)
        expense_report.initialize("09/25/2024", "Movies", 35.00)
        # When
        expense_report_output = expense_report.generate_report()

        # Then
        (assert_that(expense_report_output, "export report")
            .starts_with("| Date | Description | Amount | Balance |")
            .contains("| 09/25/2024 | Movies | 35.00 | 1,000.00 |")
            .contains("| 09/26/2024 | Groceries | 99.00 | 901.00 |")
            .ends_with("| 10/03/2024 | Car Repair | 450.00 | 451.00 |"))

        (assert_that(expense_report_output, "export report")
         .is_equal_to_with_diff("""\
| Date | Description | Amount | Balance |
| 09/25/2024 | Movies | 35.00 | 1,000.00 |
| 09/26/2024 | Groceries | 99.00 | 901.00 |
| 10/03/2024 | Car Repair | 450.00 | 451.00 |"""))





if __name__ == '__main__':
    unittest.main()
