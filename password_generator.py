import os

PASSWORD_LENGTH = 30
FILE_NAME = "Notes.txt"


def generate_password():
    ''' () -> str

    Generate a randomly generated string using alphanumeric
    characters and symbols

    >>> generate_password()
    '''
    counter = 0
    password = ""

    # the length of the password decided on
    while (counter != PASSWORD_LENGTH):
        # gets os to generate rand numbers for more randomized generation
        x = (ord(os.urandom(1)))

        # sets the range of ascii values that is acceptable for the password
        if (x >= 33 and x <= 126):
            password += chr(x)
            counter += 1

    return password


def create_file(fileName, site, user_name, password):
    ''' (str, str, str, str) -> ()

    Creates/appends file with the data provided

    >>> create_file("File.txt", "Website", "Username", "Password")
    '''
    # create file with the info
    file = open(fileName, 'a')
    file.write(
        site + "\nUsername: " + user_name + "\nPassowrd: " + password + "\n\n")
    file.close()


if __name__ == "__main__":
    # get user info
    site = input("Enter the account password to be generated for: ")
    user_name = input("Enter your username: ")
    # get passwor
    password = generate_password()
    # store user info in a file
    create_file(FILE_NAME, site, user_name, password)
