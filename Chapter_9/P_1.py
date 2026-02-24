# File I/O


# code to find whether word "twinkle" in in poem.txt file or not.

with open("poem.txt","r") as f:
    data = f.read()
    
    if "twinkle" in data:
        print("twinkle is available in poem.txt file.")
    else:
        print("twinkle is not available in poem.txt file.")