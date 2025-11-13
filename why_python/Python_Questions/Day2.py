from calendar import month

# variables_examples.py

#String
First_Name = "John"
Last_Name = "Smith"
Name = First_Name + " " + Last_Name
#integers
Age = 26
#float
Bank_Balance = 59.99
#boolean
Can_Drive = True
#equal to ==
A = [1,2,3]
B = [1,2,3,4]
A == B

#Printing the Name, Age, Bank Balance & Whether they can drive
print("Your name is: " + Name,)
print(f"Your age is: {Age}")
print(f"Your Bank_Balance is: £{Bank_Balance}")
print(f"You Can_Drive is: {Can_Drive} ")
print(A == B) #WIll give false as an answer as they are not the same

#Python strong typed language example
bob = 1
bob = ("bob")

print(bob)

print("Hi I am the system, I need to confirm some details")
name = input("Tell me your name: ")
DOB = input("Tell me your what year were you born?: ")

print("Hello " + name)



#work in progress
from datetime import datetime
def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (today.month, today.day))
    return age


