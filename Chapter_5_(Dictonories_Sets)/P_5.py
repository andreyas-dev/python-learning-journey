# Create empty ditionary and ask your four friencds to enter their favourite language and use keys as their names and values as their favourite language.

dict = {}

name = input("Enter your name:")
lang = input("Enter your favourite language:")
dict[name] = lang
#dict.update({name:lang}) also do same thing as above line do.

name = input("Enter your name:")
lang = input("Enter your favourite language:")
dict[name] = lang

name = input("Enter your name:")
lang = input("Enter your favourite language:")
dict[name] = lang

print(dict)

# what if two frinds have same name? then value will updated. 
# Key can not be duplicate but value can be duplicate.
