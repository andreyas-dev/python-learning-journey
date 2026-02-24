#Program to replace Donkey word with #####

word = 'Donkey'

with open("P_4.txt", "r") as f:
    content = f.read()

content_new = content.replace(word, "#####")

with open("P_4.txt", "w") as f:
    f.write(content_new)