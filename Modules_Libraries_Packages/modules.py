from Math_Operations import *


# Mini-calculator
first_num = int(input("Enter the first number: "))
operator = str(input("Enter the operator: "))
second_num = int(input("Enter the second number: "))


if input() == "+":
    result = first_num + second_num
elif input() == "-":
    result = first_num - second_num
elif input() == "*":
    result = first_num * second_num
elif input() == "/":
    result = first_num / second_num



result = add(first_num, second_num)
print(f"{first_num} + {second_num} = {result}")