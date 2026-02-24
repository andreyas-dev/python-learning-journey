# Functions and Recurrsion

# Write a function to check the greatest numbet among three numbers

def greeater(a,b,c):
    if(a > b and a > c):
        return a

    elif(b > a and b > c):
        return b

    else:
        return c


# Conditional Expressions

#Program to print greateest of the four nunbers entered by the user

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))


print(f"The greatest number is {greeater(a,b,c)}")


