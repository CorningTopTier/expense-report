import unittest
from assertpy import assert_that



class MyTestCase(unittest.TestCase):
    def test_something(self):
        # self.assertEqual(True, False)  # add assertion here
        assert_that(True, "some value").is_equal_to(False).is_false()


if __name__ == '__main__':
    unittest.main()
