# Conditional Expressions

#Program to print greateest of the four nunbers entered by the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

if(a > b and a > c and a > d):
    print(f"The highest number is {a}")

elif(b > a and b > c and b > d):
    print(f"The highest number is {b}")

elif(c > a and c > b and c > d):
    print(f"The highest number is {c}")

else:
    print(f"The highest number is {d}")
