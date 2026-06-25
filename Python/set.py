# Unordered, mutable and unindexed collection of unique elements.

# Creation of a set
mySet = {1,2,3,4,5}
print("My first set ", mySet)

# Trying to enter the duplicate element
mySet1 = {1,2,3,4,5,6,7,7,7,7}
print("Tried to add the duplicate element in the set ", mySet1)

# Adding element to the set
mySet.add(6)
print("Set value after adding 6 ", mySet)

# Removing element from the set
mySet.remove(6) # Here we need to explicity pass the element which we want to remove.
print("Value of set after removing 6 ", mySet)


# Set operation (union, intersection and difference)
print("Union of mySet and mySet1 is ", mySet | mySet1)

print("Intersection of mySet and mySet1 is ", mySet & mySet1)

print("Difference of mySet and mySet1 is ", mySet - mySet1)

print("Difference of mySet1 and mySet is ", mySet1 - mySet)