# Program to calculate the grade of student from marks in 3 subjects.

s1 = int(input("Enters marks of English out of 100: "))
s2 = int(input("Enter marks of Mathematics out of 100: "))
s3 = int(input("Enter marks of DLD out of 100: "))
total = s1 + s2 + s3
t = total/300 * 100
if (t >= 90 and t == 100):
    print("Congratulations! You have got A+ grade.")
elif (t >= 80 and t < 90):
    print("Congratulations! You have got A grade.")
elif (t >= 70 and t < 80):
    print("Congratulations! You have got B grade.")
elif (t >= 60 and t < 70):
    print("Congratulations! You have got C grade.")
elif (t >= 50 and t < 60):
    print("Congratulations! You have got D+ grade.")
elif (t >= 40 and t < 50):
    print("Congratulations! You have got D grade.")
else:
    print("Sorry! You have got F grade.")
