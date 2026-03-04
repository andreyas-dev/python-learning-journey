'''Write a Program to generate multiplication tables from 2 to 20 
and write this to different files in a folder for 13-years old student.'''

def generate_table(n):
    table = ""
    for i in range(1,11):
        table+=f"{n} * {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.txt" , "w")as f:
        f.write(table)



for i in range (2,21):
    print (f"Table of {i}")
    generate_Table = generate_table(i)
