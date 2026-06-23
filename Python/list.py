fruits = ["Apple", "Mango", "Cherry", 1, 1.2, True]
print(fruits)

# Accesing the items of the list
# For this python uses the index which starts from the 0 to infinity
print("First element of the fruit list is = ", fruits[0])

# For accesing the last element of the list use can use the len(list) - 1 or directly use the -1 index.
print("Last element of the list is  = ", fruits[len(fruits) - 1])
print("Last element of the list is  = ", fruits[-1])


# For adding the element to list we use the append method
fruits.append("Orange")
print("List after appending the Orange is = ", fruits)


# For removing an element from the list we use the remove method. This method accepts the element which you want to remove from the list.
fruits.remove("Orange")
print("List after removing the Orange from the list is = ",fruits)


# Iterating over the list
for fruit in fruits:
    print(fruit) 

# Find the length of the list
print("Length of the list is = ", len(fruits))   

# Existence of the item in the list

print("Is Mango present in the list ", "Mango" in fruits)
print("Is mango present in the list ", "mango" in fruits)