
#group 5 Make Functions
#Question 1
#function with no argument
def print_something():
    print("Hello There")
    return

#function with one argument
def print_something_custom(message):
    print(message)
print_something()  # Calls the first one
print_something_custom("This is my custom message!")
# Calls the second one

def greet(name):
    print("Hello, " + name + "!")
greet("Susan")


def addition(int1, int2):
    return int1 + int2
print(addition(3,4))