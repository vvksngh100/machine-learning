# For loop
print("Tying to print numbers from 1 to 9 using the for loop :")
for i in range(1,10): # Here first number(1) is included and last number(10) is excluded.
    print(i)



print("Trying to print the numbers from 1 to 5 using the while loop :")
# Using while loop
i = 1
while i <= 5:
    print(i)
    i += 1

print("Applied the break statement whenn i == 2 : ")
# break statement
for i in range(1,5):
    if(i == 2):
        break
    print(i)

print("Applied the continue statement when i == 2 : ")
# continue statement 
for i in range(1,5):
    if(i == 2):
        continue
    print(i)


# Else statement while using the loop
print("Demonstrating the else statement with the for loop : ")
for i in range(1,6):
    print(i)
else:
    print("Loop is completed!")