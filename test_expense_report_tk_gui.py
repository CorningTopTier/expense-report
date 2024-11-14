import unittest

from assertpy import assert_that

from expense_report_tk_gui import create_app


class ExpenseReportTests(unittest.TestCase):
    def test_should_create_window_named_enter_expense(self):
        # Given

        # When
        root = create_app()

        # Then
        assert_that(root.title(), "window title").is_equal_to("Enter Expense")






if __name__ == '__main__':
    unittest.main()
