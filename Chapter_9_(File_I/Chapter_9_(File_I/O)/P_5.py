# Repeat program 4 for a list of such words to be censored

words = ["Donkey","Bad","Ganda"]

with open("P_5.txt") as f:
    content = f.read()
for word in words:
    content = content.replace(word,"#"*len(word))

with open("P_5.txt", "w") as f:
    f.write(content)