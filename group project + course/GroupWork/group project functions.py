
#group 5 Make Functions
#Question 1
#function with no argument

def print_something():
    print("Hello There")
    return

#question2
#function with one argument
def print_something_custom(message):
    print(message)
print_something()  # Calls the first one
print_something_custom("This is my custom message!")
# Calls the second one

#question 3
def greet(name):
    print("Hello, " + name + "!")
greet("Susan")

#question 4
def addition(int1, int2):
    return int1 + int2
a = 1
b = 2

print(addition(2, 2))


#question 5
def addition(int1=2, int2=2):
    return int1 + int2
a = 1
b = 2
#can leave addition () as we defined that int1 & int2 = 2
print(addition())
print(addition(4,4))

#question 6
#  the { * } symbol makes it a tuple
def print_every_number(*numbers):
    #printing the data type
    print(type(numbers))
    #loop through each number
    for num in numbers:
        print(num)
print_every_number(1,2,3,4,5)

#question 7
def greet2(name: str):
    print(f"Hint: argument is of type {type(str)}* ")
    print("Hello, " + str(name) + "!")
greet2(24601)

#Question 8
def devision(a: int = 2 ,b: int = 5) -> float:
    result: float = a / b
    print(f"Hint: return value of this type is {type(result)}")
    return result
print(devision())