#Write a function to print star pattern of given range

def star_pattern(n):
    for i in range(1,n+1):
        print("* " * i)

n = int(input("Enter the number of rows for the star pattern: "))
star_pattern(n)