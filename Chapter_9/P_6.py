# Program to mine a log file and find out whether it contain python.

with open("P_6.txt","r") as f:
    content = f.read()

count = content.count("python")
if count>0:
    print(f"python is avaliable {count} times in your file")
    
else:
    print("python is not avaliable in your file")
