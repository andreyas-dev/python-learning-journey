# Program to find the file is identical or mateches the content of another file

with open("poem.txt","r") as f:
    content_1 = f.read()

with open("this.txt","r") as f:  #replace this.txt with P_6.txt to check non identical condition 
    content_2 = f.read()

if (content_1 == content_2):
    print("These two files are identical!")
else:
   print("These two files are not identical!") 