# Creation of dictionary
myDict = {"name": "Paul", "age": 10, "marks": 50 }
print(myDict)


# Accessing items in a dictionary
print(myDict["age"])

# Adding and updating
myDict["grade"] = "D"
print(myDict)

myDict['age'] = 12
print(myDict)

# Delete key from a dictionary
del myDict["age"]
print(myDict)

# Iterating throgh the dictionary
for key,value in myDict.items():
    print(key, value)