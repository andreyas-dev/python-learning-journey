# Porgram to make a copy of poem.txt

with open("poem.txt","r") as f:
    content = f.read()

with open("this.txt","w") as f:
    f.write(content)