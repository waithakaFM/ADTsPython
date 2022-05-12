# list: ordered, mutable, allows duplicate of elements

# create a list and accessing
myList = ["banana", "Cherry", "Apple", 23, True]
print(myList)
item = myList[2]
print(item)

# empty list
myList1 = list()
print(myList1)

# iterate through the list
print("Items in the list:")
for i in myList:
    print(i)

# check if an item is the list
print("Check if banana is the list")
if "banana" in myList:
    print("Yes it is")
else:
    print("No it is not")

# check length
print("Length of list is ", len(myList))

# append and insert item
myList.append("Lemon")
print("Lemon appended in our list")
print(myList)

myList.insert(3, "Kiwi fruit")
print("Kiwi fruit added in our list at index 3")
print(myList)

# remove the last element
item = myList.pop()
print("Item removed is ", item)
print(myList)
item = myList.pop()
print("Item removed is ", item)
print(myList)

# remove a specific element
myList.remove("Cherry")
print(myList)

# remove all elements
myList.clear()
print("All element in myList are removed")
print(myList)

# sort the list
myNumbers = [12, 234, 1, -23, -78, 124, 9, 13, 89, 91]
myNumbers.sort()
print(myNumbers)

# create a new sorted list
new_list = sorted(myNumbers)
print(new_list)

# other operations
myList2 = ["*"] * 4
print(myList2)
# concatenate
new_list1 = myNumbers + myList2
print(new_list1)
# slicing
a = myNumbers[1:5]
print(a)
# from the beginning to end with steps
b = myNumbers[::2]
print(b)
# reverse the list trick
reverse = myNumbers[::-1]
print(reverse)
# copy a list
list_cpy = myList2.copy()
list_cpy.append("Biscuit")
# or
list_cpy2 = list(list_cpy)
print(list_cpy)
print(list_cpy2)
# 0r
list_cpy3 = list_cpy2[:]
list_cpy3.append("Mango")
print(list_cpy3)

# create a new list with existing list
num = [11, 12, 13 , 14, 15, 16, 17 ,18, 19]
squired = [i*i for i in num]

print(num)
print("After squiring my num items")
print(squired)

# index of
print("Index of '12'", num.index(12))




