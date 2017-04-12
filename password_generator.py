#!/usr/bin/env python3
"""This script gets necessary inputs from the user to generate a
randomized password"""

import os

FILE_NAME = "Notes.txt"


class ValidationError(Exception):
    """Error raised if the user does not pick any type of characters"""
    pass


class LengthError(Exception):
    """Error raised if the length of string is too short or too long"""
    pass


def password_length_checker(length):
    """Checks length of password asked for validity

    Determines if the password is the correct length.
    Less than 6 characters is too short. Greater than 40
    characters is too long.

    Args:
        length: int determing the number of characters the
            password should contain

    Raises:
        LengthError: Error occurred because password length is
            invalid
    """
    if length < 6:
        raise LengthError("WARNING: Password too short")
    elif length > 40:
        raise LengthError("WARNING: Password too long")


def find_range(upper_case, lower_case, numbers, symbols):
    """Finds the range of ascii characters that the user wants

    Finds the ascii representation of all the characters
    that the user wants to create their password out of.

    Args:
        upper_case: boolean used to determine if upper
            case characters are wanted
        lower_case: boolean used to determine if lower
            case characters are wanted
        numbers: boolean used to determine if numbers
            are wanted
        symbols: boolean used to determine if symbols
            are wanted

    Returns:
        list of ints containing ascii representation of
        characters that is wanted

    Raises:
        ValidationError: An error occured where no type
            of character selected to make the string
    """
    if upper_case:
        upper_case_range = range(65, 90 + 1)
    else:
        upper_case_range = range(0, 0)

    if lower_case:
        lower_case_range = range(97, 122 + 1)
    else:
        lower_case_range = range(0, 0)

    if numbers:
        numbers_range = range(48, 57 + 1)
    else:
        numbers_range = range(0, 0)

    if symbols:
        symbols_range = list(range(33, 47 + 1)) + list(range(58, 64 + 1)) + \
            list(range(91, 96 + 1)) + list(range(123, 126 + 1))
    else:
        symbols_range = range(0, 0)

    total_range = list(upper_case_range) + list(lower_case_range) + \
        list(numbers_range) + list(symbols_range)

    if list(total_range) == []:
        raise ValidationError("No character type has been selected")

    return total_range


def generate_password(length=30, upper_case=True,
                      lower_case=True, numbers=True, symbols=True):
    """Generates a randomized string.

    Generates a string of specifications set in the paraments,
    determining length and the type of characters acceptable.

    Args:
        length: Optional integer parameter. Set as 30 by default.
            Determines the number of characters the password should contain
        upper_case: Optional boolean parameter. Set as true by default.
            Determines if upper case characters are wanted in the password
        lower_case: Optional boolean parameter. Set as true by default.
            Determines if lower case characters are wanted in the password.
        numbers: Optional boolean parameter. Set as true by default.
            Determines if numbers are wanted in the password.
        symbols: Optional boolean parameter. Set as true by default.
            Determines if symbols (i.e - ?, $ etc.) are wanted in the password.
    """
    counter = 0
    password = ""

    # finds the range of letters that the user has chosen
    try:
        total_range = find_range(upper_case, lower_case, numbers, symbols)
    except ValidationError:
        return "Please fix settings. Password could not be generated"

    try:
        password_length_checker(length)
    except LengthError:
        return 'Password length must be between 6 and 40 characters'

    while counter < length:
        # gets os to generate rand numbers for more randomized generation
        letter = ord(os.urandom(1))

        # only accepts values that the user has chosen
        if letter in total_range:
            password += chr(letter)
            counter += 1

    return password


def create_file(site, user_name, password, file_name=FILE_NAME):
    """Creates a file info containing site name, user name and password

    Args:
        site: String containing the name of the site the username and
            password is for
        user_name: the user name for the site
        password: the password for the site
        file_name: String containing the name of the file that will hold
            the information. Deafault = FILE_NAME
    """
    file = open(file_name, 'a')
    file.write(
        site + "\nUsername: " + user_name + "\nPassword: " + password + "\n\n")
    file.close()


def main():
    """Gets inputs from the user and puts contents into a file

    Gets the site name, username from the user. Generates a randomized
    password. Puts the site name, user name and password into a file.
    """
    site = input("Enter the account password to be generated for: ")
    user_name = input("Enter your username: ")
    password = generate_password()
    create_file(site, user_name, password, FILE_NAME)


if __name__ == "__main__":
    main()
