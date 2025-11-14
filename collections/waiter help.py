print("Bonjour, welcome to the fanciest restraint in the world")
print("\nI will be your waiter tonight, look over the menu and let me know what you are wanting")

#defining courses as lists
starters = {
    'bread ': 5.00,
    'salad ': 4.50,
    'chili squid ': 6.00
}

main = {
    'steak ':12.00,
    'duck': 11.00,
    'pork': 11.50
}

dessert = {
    'brownie': 4.00,
    'cookie dough': 4.20,
    'icecream': 2.90
}


print('\n Starter Courses')
for items, price in starters.items():
    print(f"{items} - £{price:.2f}")
print('\nMain Course')
for items, price in main.items():
    print(f"{items} - £{price:.2f}")
print('\n Dessert Courses'),
for items, price in dessert.items():
    print(f"{items} - £{price:.2f}")

def menu():
    print("\n---Starters---")
    print(starters)
    print("\n---mains---")
    print(main)
    print("\n---Desserts---")
    print(dessert)

starter_choice = input("What would you like for starters? ")

if starter_choice in starters:
    print("good choice")
 else:
    print("sorry, that's not on the menu.")

total = 0
total += starters[starter_choice]

second_starter = input("Would you like another stater? yes/no: ")

order_more = "yes"










