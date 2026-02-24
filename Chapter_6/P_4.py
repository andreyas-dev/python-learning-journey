# Program to check given username have less the 10 characters or not

Username = input("Enter your username: ")

if (len(Username) < 10):
    print("User name is Valid!")
else:
    print("Username is Invalid!\nIt should be less than 10 characters.")