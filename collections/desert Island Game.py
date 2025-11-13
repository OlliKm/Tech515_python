#desert island game

# "Stranded on a Desert Island" game
# Rationale: Practice tuples
# Type of exercise: Finish the code
print("You are stranded on a desert island. You can take only THREE items.")
essential_item1 = input("What is an essential item you would take? ")
essential_item2 = input("What is an essential item you would take? ")
essential_item3 = input("What is an essential item you would take? ")
# save the items as a tuple
essentials_tuple = (essential_item1, essential_item2, essential_item3)

# rewrite over the tuple including the new item to keep same name but give new id

print("Here are your items as a tuple:", essentials_tuple)
print("")
print("I lied. You can take one more item.")
essential_item4 = input("What is one more essential item you would take? ")

#creaitng a new tuple with a new id
essentials_tuple = (essential_item1, essential_item2, essential_item3, essential_item4)

print("Here are your items as a tuple (with the 4th item added):", essentials_tuple)