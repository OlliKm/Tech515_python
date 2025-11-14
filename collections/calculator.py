
# calculator

#defining basic operations x & y
def Add(x,y):
    return x+y
def Subtract(x,y):
    return x-y
def Multiply(x,y):
    return x*y
def Divide(x,y):
    if y == 0:
        return "Error, cant divide by zero"
    return x/y

#defining advanced operations - not done yet

#chat-text - what will be presented to user
print("Welcome to the calculator")
print("Operations available:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

#user input
question = input("What operator would you like to use?")
x = float(input("Enter your first number: "))
y = float(input("Enter second number: "))

#if - elif actual math part - adding the 2 user numbers plus operator together
if question == '+':
    print(Add(x,y))
elif question == '-':
    print(Subtract(x,y))
elif question == '*':
    print(Multiply(x,y))
elif question == '/':
    print(Divide(x,y))
else:
    print("Please enter a valid operator ")
