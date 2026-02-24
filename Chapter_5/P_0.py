# Dictoniries and Sets

# Dictoniries

marks ={
    'Andreyas' : 67,
    'Hassan' : 78,
    'Aiman' : 67
}

print(f"{marks}\n{type(marks)}")
print(marks['Andreyas'])

#Dictoniries methods
print(marks.items())
print(marks.keys())
print(marks.values())
u = marks.update({'Andreyas':99 , 'Ali' : 88})
print(marks)

print(marks.get('Andreyas'))
print(marks.get('Ahsan'))           # print None
# print(marks["ahsan"])             # Rturn error

# Sets
a = {}   # Empty dictoniry
b = {1,2,3,4,5,6}  # Set  | sets are immutable
s = set()  # Empty set

print(f"a = {type(a)}\nb = {type(b)}\ns = {type(s)}")

s = {1,2,3,4,5,6} 
s.add(7)
print(s)
print(s.union({8,9,10}))
print(s.intersection({1,2,30}))