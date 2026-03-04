# Program to acccept marks of 6 students

marks = []
m_1 = int(input("Enter number of student 1:"))
m_2 = int(input("Enter number of student 2:"))
m_3 = int(input("Enter number of student 3:"))
m_4 = int(input("Enter number of student 4:"))
m_5 = int(input("Enter number of student 5:"))
m_6 = int(input("Enter number of student 6:"))

marks.append(m_1)
marks.append(m_2)
marks.append(m_3)
marks.append(m_4)
marks.append(m_5)
marks.append(m_6)

marks.sort()

print(marks)