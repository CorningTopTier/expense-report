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

    def test_should_create_window_with_dimensions_of_300_by_150(self):
        # Given
        # When
        root = create_app()
        root.update()

        # Then
        assert_that(root.geometry()).is_equal_to("300x150+0+0")

if __name__ == '__main__':
    unittest.main()
