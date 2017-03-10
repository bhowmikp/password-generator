import unittest
from password_generator import *

class TestPasswordLengthChecker(unittest.TestCase):

    def test_too_short_negative(self):
        with self.assertRaises(LengthError):
            password_length_checker(-1)

    def test_too_short_positive(self):
        with self.assertRaises(LengthError):
            password_length_checker(5)

    def test_no_errors_1(self):
        self.assertEquals(password_length_checker(6), None, "Returns something that's not None")

    def test_no_errors_2(self):
        self.assertEquals(password_length_checker(15), None, "Returns something that's not None")

    def test_no_errors_3(self):
        self.assertEquals(password_length_checker(40), None, "Returns something that's not None")

    def test_too_long_1(self):
        with self.assertRaises(LengthError):
            password_length_checker(41)

    def test_too_long_2(self):
        with self.assertRaises(LengthError):
            password_length_checker(1000)


class TestFindRange(unittest.TestCase):

    def test_none(self):
        with self.assertRaises(ValidationError):
            find_range(False, False, False, False)

    def test_upper_case(self):
        ascii_range = list(range(65, 90 + 1))
        self.assertEquals(find_range(True, False, False, False), ascii_range, "Range of uppercase is 65 - 90. Return value not correct")

    def test_lower_case(self):
        ascii_range = list(range(97, 122 + 1))
        self.assertEquals(find_range(False, True, False, False), ascii_range, "Range of lowercase is 97 - 122. Return value not correct")

    def test_numbers(self):
        ascii_range = list(range(48, 57 + 1))
        self.assertEquals(find_range(False, False, True, False), ascii_range, "Range of symbols is 48 - 57. Return value not correct")

    def test_symbols(self):
        ascii_range = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + list(range(91, 96 + 1)) + list(range(123, 126 + 1))
        self.assertEquals(find_range(False, False, False, True), ascii_range, "Not correct range of symbols")




if __name__ == "__main__":
    unittest.main()
