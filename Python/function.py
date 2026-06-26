# Function definition
def greet():
    print("Hello Vivek")

# Function call
greet()



# Passing parameters in the function
name = input()
def greetName(name):
    print("Hello " + name)

greetName(name)


# Add function
def add(num1, num2):
    return int(num1) + int(num2)

num1 = input("Enter the first number ")
num2 = input("Enter the second number ")
print(add(num1, num2))


# Default argument
def welcome(name="Vivek Singh"):
    print(f"Welcome {name}!")

welcome()

# Keywords in parameter
def profile(name, age):
    print(f"Name: {name}, Age: {age}")
profile(age=13, name="Test")
profile(name="Vivek Singh", age=29)
profile("John Doe", 35)


# Multiple arguments
def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4,5))



def displayInfo(**info):
    for key, value in info.items():
        print(key, value)

displayInfo(name="Vivek Singh", age=29)

def calc(a,b):
    return a+b, a*b

sumVal, prodVal = calc(3,4)
print(sumVal)
print(prodVal)

# lambda function
# Syntac: => lambda arguments : expression

x = lambda a : a + 10
print(x(5))