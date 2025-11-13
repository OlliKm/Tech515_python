#shopping list
from itertools import count

shopping_list = ['eggs', 'bread', 'bananas','biscuits', 'milk']
print(shopping_list)
print(shopping_list[0])
print(shopping_list[4])
print(type(shopping_list))
shopping_list[2] = 'rice'
print(shopping_list[2])
# another way to make lists - shop_list = list(("apple", "banana", "cherry")) # note the double round-brackets
shopping_list.append('rice')
print(shopping_list)
print(shopping_list.insert(0,'carrots'))
#adds toffee and coffee onto list placing them first / positon 0
shopping_list[0:0] = ['toffee',  'coffee']
print(shopping_list)
#pop(0) removes first item pop() deletes last element
shopping_list.pop(0)
print(shopping_list)




