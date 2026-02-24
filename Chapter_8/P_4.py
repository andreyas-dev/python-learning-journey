# Program a recurrsive function to find sum of first n natural number

def sum_of_natural(n):
    if n == 1:
        return 1
    else:
        return n+sum_of_natural(n-1)
    

num = int(input("Enter a number: "))
print(f"The sum of first {num} natural numbers is: {sum_of_natural(num)}")