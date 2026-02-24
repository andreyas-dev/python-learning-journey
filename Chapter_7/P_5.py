# Prgoram to findsum of first n natural numbers

num = int(input("Enter the number:"))

sum = 0
for i in range(1,num+1):
    sum+=i

print(f"The sum of fisrt {num} natural numbers is: {sum}")