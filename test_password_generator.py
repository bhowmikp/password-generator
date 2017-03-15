import unittest
import os
from password_generator import password_length_checker, LengthError, find_range, ValidationError, generate_password, create_file

class TestPasswordLengthChecker(unittest.TestCase):

    def test_too_short_negative(self):
        with self.assertRaises(LengthError):
            password_length_checker(-1)

    def test_too_short_positive(self):
        with self.assertRaises(LengthError):
            password_length_checker(5)

    def test_no_errors_1(self):
        self.assertEqual(password_length_checker(6), None, "Returns something that's not None")

    def test_no_errors_2(self):
        self.assertEqual(password_length_checker(15), None, "Returns something that's not None")

    def test_no_errors_3(self):
        self.assertEqual(password_length_checker(40), None, "Returns something that's not None")

    def test_too_long_1(self):
        with self.assertRaises(LengthError):
            password_length_checker(41)

    def test_too_long_2(self):
        with self.assertRaises(LengthError):
            password_length_checker(1000)


class TestFindRange(unittest.TestCase):

    def setUp(self):
        self.uppercase = list(range(65, 90 + 1))
        self.lowercase = list(range(97, 122 + 1))
        self.numbers = list(range(48, 57 + 1))
        self.symbols = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + list(range(91, 96 + 1)) + list(range(123, 126 + 1))

    def test_none(self):
        with self.assertRaises(ValidationError):
            find_range(False, False, False, False)

    def test_upper_case(self):
        self.assertEqual(find_range(True, False, False, False), self.uppercase, "Range of uppercase is 65 - 90. Return value not correct")

    def test_lower_case(self):
        self.assertEqual(find_range(False, True, False, False), self.lowercase, "Range of lowercase is 97 - 122. Return value not correct")

    def test_numbers(self):
        self.assertEqual(find_range(False, False, True, False), self.numbers, "Range of symbols is 48 - 57. Return value not correct")

    def test_symbols(self):
        self.assertEqual(find_range(False, False, False, True), self.symbols, "Not correct range of symbols")

    def test_uppercase_and_lowercase(self):
        ascii_range = list(self.uppercase) + list(self.lowercase)
        self.assertEqual(find_range(True, True, False, False), ascii_range, "Not correct range")

    def test_lowercase_and_symbols(self):
        ascii_range = list(self.lowercase) + list(self.symbols)
        self.assertEqual(find_range(False, True, False, True), ascii_range, "Not correct range")

    def test_uppercase_and_numbers(self):
        ascii_range = list(self.uppercase) + list(self.numbers)
        self.assertEqual(find_range(True, False, True, False), ascii_range, "Not correct range")

    def test_uppercase_numbers_symbols(self):
        ascii_range = list(self.uppercase) + list(self.numbers) + list(self.symbols)
        self.assertEqual(find_range(True, False, True, True), ascii_range, "Not correct range")

    def test_lowercase_numbers_symbols(self):
        ascii_range = list(self.lowercase) + list(self.numbers) + list(self.symbols)
        self.assertEqual(find_range(False, True, True, True), ascii_range, "Not correct range")

    def test_uppercase_lowercase_symbols(self):
        ascii_range = list(self.uppercase) + list(self.lowercase) + list(self.symbols)
        self.assertEqual(find_range(True, True, False, True), ascii_range, "Not correct range")

    def test_all(self):
        ascii_range = list(self.uppercase) + list(self.lowercase) + list(self.numbers) + list(self.symbols)
        self.assertEqual(find_range(True, True, True, True), ascii_range, "Not correct range")


class TestGeneratePassword(unittest.TestCase):
    def setUp(self):
        self.uppercase = list(range(65, 90 + 1))
        self.lowercase = list(range(97, 122 + 1))
        self.numbers = list(range(48, 57 + 1))
        self.symbols = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + list(range(91, 96 + 1)) + list(range(123, 126 + 1))

    def test_default(self):
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

        self.assertTrue(status, "Password length or characters of password incorrect")

class TestCreateFile(unittest.TestCase):
    def test_file_creation_default(self):
        create_file("Site", "Name", "Hello123", "Nothing.txt")

        with open('Nothing.txt') as file:
            lines = file.readlines()

        self.assertEqual(lines[0].strip(), 'Site', 'Site name not correct')
        self.assertEqual(lines[1].strip(), 'Username: Name', 'Username not correct')
        self.assertEqual(lines[2].strip(), 'Password: Hello123', 'Password not correct')
        self.assertEqual(lines[3], '\n', 'No space after input')

        os.remove("Nothing.txt")

    def test_file_creation(self):
        create_file("None", "No Name", "Nothing")

        with open('Notes.txt') as file:
            lines = file.readlines()

        self.assertEqual(lines[0].strip(), 'None', 'Site name not correct')
        self.assertEqual(lines[1].strip(), 'Username: No Name', 'Username not correct')
        self.assertEqual(lines[2].strip(), 'Password: Nothing', 'Password not correct')
        self.assertEqual(lines[3], '\n', 'No space after input')

        os.remove("Notes.txt")


    def test_file_two_site(self):
        create_file("Site", "Name", "Hello123", "Nothing.txt")
        create_file("None", "No Name", "Nothing")

        with open('Nothing.txt') as file:
            lines = file.readlines()

        with open('Notes.txt') as file1:
            lines1 = file1.readlines()

        self.assertEqual(lines[0].strip(), 'Site', 'Site name not correct')
        self.assertEqual(lines[1].strip(), 'Username: Name', 'Username not correct')
        self.assertEqual(lines[2].strip(), 'Password: Hello123', 'Password not correct')
        self.assertEqual(lines[3], '\n', 'No space after input')

        self.assertEqual(lines1[0].strip(), 'None', 'Site name not correct')
        self.assertEqual(lines1[1].strip(), 'Username: No Name', 'Username not correct')
        self.assertEqual(lines1[2].strip(), 'Password: Nothing', 'Password not correct')
        self.assertEqual(lines1[3], '\n', 'No space after input')

        os.remove('Nothing.txt')
        os.remove('Notes.txt')

if __name__ == "__main__":
    unittest.main()
