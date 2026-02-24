# Program to write table of given number in reverse order
num = int(input("ENter the number:"))

for i in range(10,0,-1):
    print(f"{num}*{i}={num*i}")
    i+=1