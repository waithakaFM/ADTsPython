# Sets: unordered, mutable, no dublicates

# declare
mySet = {"a", "b", "c", "d", "e", "f", "a"} # 'a' is printed only once
mySet1 = set([1, 2, 3, 4, 5, 6, 7])
mySet2 = set("Hello")
print(mySet)
print(mySet1)
print(mySet2)

# empty set
mySet3 = set()
print(mySet3)

# add item
mySet3.add("Mili")
mySet3.add("John")
mySet3.add("June")
print(mySet3)

# remove item
mySet3.remove("John")
print(mySet3)

mySet3.discard("Frank") # using discard method no error is raised even if an item is in the list
print(mySet3)
mySet3.discard("June")
print(mySet3)

mySet3.clear() # to empty
print(mySet3)

print(mySet.pop()) # remove the arbitrary element
print(mySet)

# iterate through
for i in mySet:
    print(i)

# check if an element is in the set
if "l" in mySet2:
    print("yes")
else:
    print("no")

# union and intesection
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8,}
primes = {2, 3, 5, 7}

u = primes.union(evens) # combine both sets without dublication
print(u)

i = odds.intersection(evens) # take elements found in both sets
print("Empty set since no number which is both odd and even")
print(i)

i1 = odds.intersection(primes)
print("All the odd numbers from 0 to 10 that are prime")
print(i1)

i2 = evens.intersection(primes)
print("All the even numbers from 0 to 10 that are prime")
print(i2)

# difference of two sets
set1 = {1,2,3,4,5,6,7,8,9,0}
set2 = {1, 2, 3, 12, 34, 78, 9, 0}
set4 = {9, 45, 14, 7, 8, 4, 12, 34, 1,2}

diff = set1.difference(set2)
print("Elements in the set1 that are not in set2")
print(diff)

diff = set2.difference(set1)
print("Elements in the set2 that are not in set1")
print(diff)

diff = set2.symmetric_difference(set1)
print("All elements that are not in both sets")
print(diff)

# unite two set without creating a new one, update
set1.update(set2)
print("set1 contains all its element and that of set 2")
print(set1)

set4.intersection_update(set1)
print("Update set4 only with element in both set1 and set4")
print(set4)

set1.difference_update(set4)
print("set4: ", set4)
print("set1: ", set2)
print("Update set1 by removing elements found in set4")
print("set1: ", set1)

# elements not found in both sets
set2.symmetric_difference(set4)
print(set2)

# subset and disjoint method
# subset: A set A is a subset of another set B if all elements of the set A are elements of the set B.
# superset: A set containing all elements of a smaller set.
# disjoint: A pair of sets which does not have any common element are called disjoint sets.
setA = {1,2,3,4,5,6,7,0}
setB = {0,1,2,3}
setC = {9,10}
print("Is setA a subset of setB")
print(setA.issubset(setB))
print("Is setA a subset of setB")
print(setB.issubset(setA))
print("Is setA a supersetset of setB")
print(setA.issuperset(setB))

print("Is setA disjoint of setB")
print(setA.isdisjoint(setB))
print("Is setA disjoint of setC")
print(setA.isdisjoint(setC))

# copy sets
print(setC)
setD = setC.copy()
setD.add("Good!")
print(setD)

setE = set(setD)
setE.add("Luck")
print(setE)

# Frozenset: immutable version of a nomal set
fSet = frozenset([1,2,3,4,5,6])
# fSet.add(2) <- this gives an error, cannnot be changed
print(fSet)
