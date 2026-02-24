# Program to renamed a file by renamed_by_python.txt

#1st method but not good 
'''with open("old.txt","r") as f:
    content = f.read()

with open("renamed_by_python.txt","w") as f:
    f.write(content)'''

#2nd method according to requirement of our problem.

import os

old_name = "old.txt"
new_name = "rename_by_python.txt"

os.rename(old_name,new_name)
print("The file has renamed successfully!")