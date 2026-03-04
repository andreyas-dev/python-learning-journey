# Write a fucntion which converts inches to cm

def inches_to_cm(n):
    return n * 2.54

inches = float(input("Enter the length in inches: "))

print(f"The length in cm is: {inches_to_cm(inches)}")