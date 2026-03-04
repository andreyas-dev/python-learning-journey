# Program to check if given name is in list or not.
name = ['Ali', 'Ahmed', 'Hassan', 'Hussain', 'Andreyas']

check = input("Enter the name you want to check: ")

if (check in name):
    print(f"{check} is present in the list.")
else:
    print(f"{check} is not present in the list.")