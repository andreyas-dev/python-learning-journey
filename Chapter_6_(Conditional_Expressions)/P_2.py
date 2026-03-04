'''Program to check student is passed or failed baed on marks entered by user
in 3 subjects. If student gets 40% overall and 33% in each subject then only he is passed.'''

s1 = int(input("Enters marks of English out of 100: "))
s2 = int(input("Enter marks of Mathematics out of 100: "))
s3 = int(input("Enter marks of DLD out of 100: "))

total = s1 + s2 + s3
t_Per = total/300 * 100
if (t_Per >= 40 and s1 >= 33 and s2 >= 33 and s3 >= 33):
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry! You have failed the exam.")
