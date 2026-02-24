# Program to convert celsius to fahrenheit

def celsius_to_Farhenheit(c):
    return (c * 9/5) + 32


c = float(input("Enter the temperature in celsius: "))

print("The temperature in fahrenheit is: ", celsius_to_Farhenheit(c))