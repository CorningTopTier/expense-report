import unittest
from assertpy import assert_that
from example_gui import create_app  # Replace 'example_gui' with the actual module name if different

class TestNameInputApp(unittest.TestCase):
    def test_submit_name(self):
        # Variable to hold the callback result_container
        result_container = []

        # Define a callback function to capture the name
        def test_callback(name):
            result_container.append(name)

        # Create the Tkinter app with the test callback
        root, name_entry, submit_button = create_app(on_submit_callback=test_callback)

        # Insert a test name into the entry field
        name_entry.insert(0, "Alice")

        # Simulate button click
        submit_button.invoke()

        # Check that the callback was called with the correct name
        assert_that(result_container).is_equal_to(["Alice"])

        # Destroy the Tk instance after the test
        root.destroy()

if __name__ == '__main__':
    unittest.main()
