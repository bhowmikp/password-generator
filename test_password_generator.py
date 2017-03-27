'''Unit test for password generator'''

import unittest
import os
from password_generator import password_length_checker, LengthError
from password_generator import find_range, ValidationError
from password_generator import generate_password, create_file


class TestPasswordLengthChecker(unittest.TestCase):
    '''Test password_length_checker'''

    def test_too_short_negative(self):
        '''Test if the param is a negative number'''
        with self.assertRaises(LengthError):
            password_length_checker(-1)

    def test_too_short_positive(self):
        '''Test if password is positive but below
        acceptable range'''
        with self.assertRaises(LengthError):
            password_length_checker(5)

    def test_no_errors_1(self):
        '''Test with correct param'''
        self.assertEqual(password_length_checker(6), None,
                         "Returns something that's not None")

    def test_no_errors_2(self):
        '''Test with correct param'''
        self.assertEqual(password_length_checker(15), None,
                         "Returns something that's not None")

    def test_no_errors_3(self):
        '''Test with correct param'''
        self.assertEqual(password_length_checker(40), None,
                         "Returns something that's not None")

    def test_too_long_1(self):
        '''Test with number over accepted range'''
        with self.assertRaises(LengthError):
            password_length_checker(41)

    def test_too_long_2(self):
        '''Test with number over accepted range'''
        with self.assertRaises(LengthError):
            password_length_checker(1000)


class TestFindRange(unittest.TestCase):
    '''Test find_range'''

    def setUp(self):
        '''Sets up the variables used to test the function'''
        self.uppercase = list(range(65, 90 + 1))
        self.lowercase = list(range(97, 122 + 1))
        self.numbers = list(range(48, 57 + 1))
        self.symbols = list(range(33, 47 + 1)) + \
                       list(range(58, 64 + 1)) + \
                       list(range(91, 96 + 1)) + \
                       list(range(123, 126 + 1))

    def test_none(self):
        '''Test with all types of characters set as False'''
        with self.assertRaises(ValidationError):
            find_range(False, False, False, False)

    def test_upper_case(self):
        '''Test with only uppercase characters'''
        self.assertEqual(
            find_range(
                True,
                False,
                False,
                False),
            self.uppercase,
            "Range of uppercase is 65 - 90. Return value not correct")

    def test_lower_case(self):
        '''Test with only lowercase characters'''
        self.assertEqual(
            find_range(
                False,
                True,
                False,
                False),
            self.lowercase,
            "Range of lowercase is 97 - 122. Return value not correct")

    def test_numbers(self):
        '''Tets with only numbers'''
        self.assertEqual(
            find_range(
                False,
                False,
                True,
                False),
            self.numbers,
            "Range of symbols is 48 - 57. Return value not correct")

    def test_symbols(self):
        '''Test with only symbols'''
        self.assertEqual(
            find_range(
                False,
                False,
                False,
                True),
            self.symbols,
            "Not correct range of symbols")

    def test_uppercase_and_lowercase(self):
        '''Test with uppercase and lowercase characters'''
        ascii_range = list(self.uppercase) + list(self.lowercase)
        self.assertEqual(
            find_range(
                True,
                True,
                False,
                False),
            ascii_range,
            "Not correct range")

    def test_lowercase_and_symbols(self):
        '''Test with lowercase characters and symbols'''
        ascii_range = list(self.lowercase) + list(self.symbols)
        self.assertEqual(
            find_range(
                False,
                True,
                False,
                True),
            ascii_range,
            "Not correct range")

    def test_uppercase_and_numbers(self):
        '''Test with uppercase letters and numebrs'''
        ascii_range = list(self.uppercase) + list(self.numbers)
        self.assertEqual(
            find_range(
                True,
                False,
                True,
                False),
            ascii_range,
            "Not correct range")

    def test_uppercase_numbers_symbols(self):
        '''Test with uppercase characters, numbers and symbols'''
        ascii_range = list(self.uppercase) + \
            list(self.numbers) + list(self.symbols)
        self.assertEqual(
            find_range(
                True,
                False,
                True,
                True),
            ascii_range,
            "Not correct range")

    def test_lowercase_numbers_symbols(self):
        '''Test with lowercase characters, numbers and symbols'''
        ascii_range = list(self.lowercase) + \
            list(self.numbers) + list(self.symbols)
        self.assertEqual(
            find_range(
                False,
                True,
                True,
                True),
            ascii_range,
            "Not correct range")

    def test_upper_lowercase_symbols(self):
        '''Test with uppercase and lowercase characters and symbols'''
        ascii_range = list(self.uppercase) + \
            list(self.lowercase) + list(self.symbols)
        self.assertEqual(
            find_range(
                True,
                True,
                False,
                True),
            ascii_range,
            "Not correct range")

    def test_all(self):
        '''Test with uppercase and lowercase characters, and symbols
        and numbers
        '''
        ascii_range = list(self.uppercase) + list(self.lowercase) + \
            list(self.numbers) + list(self.symbols)
        self.assertEqual(
            find_range(
                True,
                True,
                True,
                True),
            ascii_range,
            "Not correct range")


class TestGeneratePassword(unittest.TestCase):
    '''Test generate_password'''

    def setUp(self):
        '''Sets up the variables used to test the function'''
        self.uppercase = list(range(65, 90 + 1))
        self.lowercase = list(range(97, 122 + 1))
        self.numbers = list(range(48, 57 + 1))
        self.symbols = list(range(33, 47 + 1)) + \
                       list(range(58, 64 + 1)) + \
                       list(range(91, 96 + 1)) + \
                       list(range(123, 126 + 1))

    def test_default(self):
        '''Check if length of password is 30 by default and all character
        types are used by default to generate password
        '''
        status = True
        length = 30

        password = generate_password()
        password_list = generate_password().split()

        ascii_range = self.uppercase + self.lowercase + self.numbers + self.symbols

        if len(password) != length:
            status = False

        if len(password_list) != 1:
            status = False

        for letter in password:
            if ord(letter) not in ascii_range:
                status = False

        self.assertTrue(
            status,
            "Password length or characters of password incorrect")


class TestCreateFile(unittest.TestCase):
    '''Test create_file'''

    def test_file_creation_default(self):
        '''Test file with one case of input and default params'''
        create_file("Site", "Name", "Hello123", "Nothing.txt")

        with open('Nothing.txt') as file:
            lines = file.readlines()

        self.assertEqual(lines[0].strip(), 'Site', 'Site name not correct')
        self.assertEqual(
            lines[1].strip(),
            'Username: Name',
            'Username not correct')
        self.assertEqual(
            lines[2].strip(),
            'Password: Hello123',
            'Password not correct')
        self.assertEqual(lines[3], '\n', 'No space after input')

        os.remove("Nothing.txt")

    def test_file_creation(self):
        '''Test file creation with different inputs'''
        create_file("None", "No Name", "Nothing")

        with open('Notes.txt') as file:
            lines = file.readlines()

        self.assertEqual(lines[0].strip(), 'None', 'Site name not correct')
        self.assertEqual(
            lines[1].strip(),
            'Username: No Name',
            'Username not correct')
        self.assertEqual(
            lines[2].strip(),
            'Password: Nothing',
            'Password not correct')
        self.assertEqual(lines[3], '\n', 'No space after input')

        os.remove("Notes.txt")

    def test_file_two_site(self):
        '''Test with two sites being created'''
        create_file("Site", "Name", "Hello123", "Nothing.txt")
        create_file("None", "No Name", "Nothing", "Nothing.txt")

        with open('Nothing.txt') as file:
            lines = file.readlines()

        self.assertEqual(lines[0].strip(), 'Site', 'Site name not correct')
        self.assertEqual(
            lines[1].strip(),
            'Username: Name',
            'Username not correct')
        self.assertEqual(
            lines[2].strip(),
            'Password: Hello123',
            'Password not correct')
        self.assertEqual(lines[3], '\n', 'No space after input')

        self.assertEqual(lines[4].strip(), 'None', 'Site name not correct')
        self.assertEqual(
            lines[5].strip(),
            'Username: No Name',
            'Username not correct')
        self.assertEqual(
            lines[6].strip(),
            'Password: Nothing',
            'Password not correct')
        self.assertEqual(lines[7], '\n', 'No space after input')

        os.remove('Nothing.txt')

if __name__ == "__main__":
    unittest.main()
