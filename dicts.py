# Dictionary: key-value pairs, unordered, mutable

# declare
mydict = {"Name": "Son", "Age": 33, "City": "Nairobi"}
print(mydict)

mydict1 = dict(Name="Carlos", Age=14, City="Los Mary")
print(mydict1)

# access a value
value = mydict1["Name"]
print(value)

# mutability
mydict["email"] = "son@gmail.com"
print(mydict)

# delete
del mydict1["Name"]
print(mydict1)

mydict1.pop("Age")
print(mydict1)

mydict.popitem()
print(mydict)

# check if a key in dict
if "Name" in mydict:
    print(mydict["Name"])

try:
    print(mydict["email"])
except:
    print("Error")

# loop
print("Print key in the dict")
for key in mydict.keys():
    print(key)

print("Print value in the dict")
for value in mydict.values():
    print(value)

print("Print both the key and the value in the dict")
for key, value in mydict.items():
    print(key, value)

# copy the dict
mydict_cpy = mydict.copy()
mydict_cpy["email"] = "me@email.com"
print("Original dict")
print(mydict)
print("Copied")
print(mydict_cpy)

mydict_cpy1 = dict(mydict_cpy)
mydict_cpy1["contact"] = 11231213
print("Original dict")
print(mydict_cpy)
print("Copied")
print(mydict_cpy1)

# matching dicts
print("Update mydict with mydicy_cpy1")
mydict.update(mydict_cpy1)
print(mydict)

# using tuple as key
mytuple = (15, 7)
add = {mytuple: 22}
print(add)

# creating dict from sequences
mytuple1 = ("John", "Lucy", "Carlos", "Kimani", "Otieno", "Mwas")
mapping = dict(zip(range(1, 7), mytuple1))
print(mapping)

mytuple2 = ("Njoki", "Jose", "Kithondu")
mytuple3 = ("Surname", "Fname", "Lname")
mapping1 = dict(zip(mytuple3, mytuple2))
print(mapping1)