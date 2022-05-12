# tuple: ordered, immutable, allows duplicate elements. Often used to object that belong together
import sys
import timeit

# creating
myTuple = "Frank", 21, "Nyeri"
myTuple1 = "Billy",
print(myTuple)
print(myTuple1)

# tuple from a list
myTuple2 = tuple(["Mike", "John", "Tom"])
print(myTuple2)
myList = ["Mango", "Apple", "Watermelon"]
myTuple3 = tuple(myList)
print(myTuple3)

# access item
item = myTuple[2]
print(item)

# count an element in the tuple
myTuple4 = ('q', 'w', 'r', 'd', 'w', 'q', 'w')

print("How many 'w' in myTuple", myTuple4.count('w'))

# find the index of an item
print("Index of 'd' ", myTuple4.index("d"))

# unpack the tuple
myTuple5 = "Billy", 39, "Jiji"

name, age, city = myTuple5
print("Name: ", name)
print("Age: ", age)
print("City: ", city)

myTuple6 = ("Mark", "John", "Tom", "Cris", "Tim", "Billy")

i1, *i2, i3 = myTuple6

print("The first element ", i1)
print("The last element ", i3)
print("The middle elements:")
print(i2)

# a tuple is more efficient especially when working with large data, it occupies lesser space than list, here is a demo
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print("The size of the list is ", sys.getsizeof(my_list), "bytes")
print("The size of the tuple is ", sys.getsizeof(my_tuple), "bytes")

# also efficient in iterating through the elements: demo
print("Creating a list a million time takes ", timeit.timeit(stmt="[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]", number=1000000))
print("Creating a tuple a million time takes ", timeit.timeit(stmt="(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)", number=1000000))