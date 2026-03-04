#Write program to find out line number where python is present
line = 1
with open("P_6.txt","r") as f:
    lines = f.readlines()
line_found = []
lineno = 1  
for line in lines:
    if ("python" in line.lower()):
        line_found.append(lineno)        
    lineno+=1

if not line_found:   
     print("python is not available in your file")
else:
        print(f"python is availabe on lines {line_found}")