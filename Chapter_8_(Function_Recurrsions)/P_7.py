# Create a function to remove a given word from a string and strip it at the same time

def remove_word(lst, remove):

    return [i for i in lst if i != remove]

my_list = [1,2,3,4,5,3,2,1]
word = input("Enter the word to remove: ")
print(f"Orignal list: {my_list}")
mylist = remove_word(my_list, int(word))
print(f"List after removing {word}: {mylist}")