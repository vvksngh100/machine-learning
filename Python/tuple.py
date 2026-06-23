myTupple = ("apple", "mango", "cherry", 1, 1.2, True)

print(myTupple)

# Accessing the element of the tuple - use the index
print(myTupple[0]) # By this we are trying to access the first element of the tuple.

# For find the length of the tuple we use len
print("Length of the tuple is = ", len(myTupple))

# For accessing the last element of the we can use len(tuple) - 1 or -1 as index
print("Last element of the tuple is = ", myTupple[len(myTupple) - 1]) # Using len
print("Last element of the tuple is = ", myTupple[-1])  # Using -1

# Tuple unpacking
print("Tuple unpacking :")
numbers = (40,20,50,60)
a,b,c,d = numbers
print(a)
print(b)
print(c)
print(d)


# Iterating over tuple
print("Printing numbers using the for loop :")
for number in numbers:
    print(number)


# Concatenation of tuples
tuple1 = (1,2,3)
tuple2 = (4,5,6)
print(tuple1 + tuple2) 

# Deletion of tuple
tup = (1,2,3,4,5)
print("tup before deletion : ", tup)
del(tup)
#print("After deletion : ", tup) # Get NameError: name 'tup' is not defined

