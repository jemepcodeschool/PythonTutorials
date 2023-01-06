# -*- coding: utf-8 -*-
"""lists.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RYvcGwW10f3rDm7egBK7wiaEzUwXaC0I

What is a list

Is a data type that allows you to add and remove values, access its values and iterate through its values
"""

# printing a list
names_of_students = ['mykel', 'sam', 'jon']

print(names_of_students)

# Printing each value in a list
for name in names_of_students:
  print(name)

# Enumerating through a list
# Enumerate pos and the value of each element
for i,j in enumerate(names_of_students):
  print(i)

# Prints the value occupaying the first pos
print(names_of_students[1])

# Assigning value to a position
names_of_students[1] = 'bob'

print(names_of_students)

# delete a position
del names_of_students[2]

print(names_of_students)

# Add value to the bottom of the list

names_of_students.append('alice')
names_of_students.append('mary')

print(names_of_students)

# remove an element from a list

names_of_students.remove('mykel')

print(names_of_students)

# insert a value at a specific position in a list

names_of_students.insert(0, 'jose')

print(names_of_students)

# for pos,elem in enumerate(names_of_students):
#   print(pos, elem)

#[   0,     1,       2,       3 ]
#[  -4,    -3,      -2,      -1 ]
#['jose', 'bob', 'alice', 'mary']

print(names_of_students[-1] == names_of_students[3])

# Getting the last value using the len of the list

number_of_students = len(names_of_students)

last_position_of_list = len(names_of_students) - 1

print(names_of_students[last_position_of_list])

# Get the last element of a list using negative index

print(names_of_students[-1])

# Creating a list by addition

names_teachers = ['jack', 'jane']

print(names_of_students + names_teachers)

# Multiplying a list

print(names_teachers * 3)

print(names_of_students)
print(names_teachers)

# using slices

print(names_of_students[0:4:2])

# using lists with loops

for student in names_of_students:
  if student == 'bob':
    print('Hello bob')
  else:
    print('You are not bob')

# using lists with loops

science_students = ['alice']

for student in names_of_students:
  if student not in science_students:
    science_students.append(student)
  else:
    print('You are already a science student')

print(science_students)

# sorting a list

student_ids = [102,343,111,901,221,678]

student_ids.sort()

print(student_ids)

# sorting using a key

chars = ['aA', 'bb', 'Ae', 'zb', 'cC', 'l', 'Mn', 'c']
chars.sort()

print(chars)

chars.sort(key=str.lower)

print(chars)

chars.sort(key=str.upper)

print(chars)

# sort in reverse
print(names_of_students)

names_of_students.sort(reverse=True)

print(names_of_students)

# Reversing a list

print(names_of_students)

#names_of_students.reverse()

print(names_of_students[::-1])