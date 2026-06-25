# List comprehension
square = [x**2 for x in range(1,5)]
print("List of squares from 1 to 4", square)

# List of even numbers
even = [x for x in range(1,10) if x % 2 == 0]
print("List of even numbers between 1 to 10", even)


# Dictionary comprehension
# Dictionary of square
squareDict = {x:x**2 for x in range(1,5)}
print("Dictionary of square from 1 to 4", squareDict)


# Set comprehension
uniqueNumbers = {x for x in range(10)}
print("Set using the set comprehension : ", uniqueNumbers)


uniqueNumbers1 = {x for x in {1,1,2,2,3,3,3,4,4,5,5,6,6}}
print("Unique numbers : ", uniqueNumbers1)