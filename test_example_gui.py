import unittest

from assertpy import assert_that
from tkinter import Tk, Entry

# Import the submit_name function
from example_gui import submit_name

class ExpenseReportTests(unittest.TestCase):
    def test_submit_name(self):
        # Create a Tkinter Entry widget for testing
        root = Tk()
        name_input_field = Entry(root)

        # Insert a test name into the entry widget
        test_name = "Alice"
        name_input_field.insert(0, test_name)

        # Call submit_name and verify the result
        result = submit_name(name_input_field)
        assert_that(result).is_equal_to(test_name)

        # Destroy the Tk instance after the test
        root.destroy()

# Running this test will verify that the submit_name function correctly returns the name entered

if __name__ == '__main__':
    unittest.main()
