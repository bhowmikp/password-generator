import os

# symbols 33- 47 && 58-64 && 91-96 && 173-176
# number 48-57
# uppercase letters 65-90
# lowercase letters 97-122

counter = 0
password = ""
PASSWORD_LENGTH = 30

# get user info
site = input("Enter the account password to be generated for: ")
username = input("Enter your username: ")

# the length of the password decided on
while (counter != PASSWORD_LENGTH):
    # gets os to generate rand numbers for more randomized generation
    x = (ord(os.urandom(1)))

    # sets the range of ascii values that is acceptable for the password
    if (x >= 33 and x <= 126):
        password += chr(x)
        counter += 1

# password
print ("Password: " + password)

# create file with the info
file = open("Notes.txt", 'a')
file.write(
    site + "\nUsername: " + username + "\nPassowrd: " + password + "\n\n")
file.close()
