message = input("Enter the message: ")
check = input("Enter the word you want to check: ")
if( check in message):
    print(f"{check} is in the message.")
else:
    print(f"{check} is not in the message.")