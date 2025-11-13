mixture = [1, 2, 3,"one", "two", "three"]

print(mixture)
#print the 2 and 3rd item in list
print(mixture[1:3])
# [2:] is saying print everything onwards starting from number 2 works backwords to [:4]
print(mixture[2:])
#prints every second element from list
B = mixture[::2]
print(B)
#
C = mixture[1:6:3]
print(C)
print("new type")
#
print(mixture[-1:2:-1])

#desert island game

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = None  # YOUR CODE GOES HERE INSTEAD OF 'None'
# print the tuple
print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")
# try to add the 4th item to the tuple
# if you can't add the 4th item, work out how to save the 4th item to the tuple
# YOUR CODE GOES HERE
print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)