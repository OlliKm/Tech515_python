def division(numerator: int = 2, denominator: int = 5) -> float:
    return numerator / denominator

a: int = 4
b: int = 6
print(division(denominator=b))

def print_items_in_collection(collection_passed_in):
    print(type(collection_passed_in))
    for item in collection_passed_in:
        print(item)
    number_of_items = len(collection_passed_in)
    print(f"The collection has {number_of_items} items.")

# the list is passed in as a single collection (tuple) with the list being the first item in the tuple
print_items_in_collection([1, 2, 2, 3, 3, 4, 5, 5])
# the list is passed in as a single collection (tuple) with the list being the first item in the tuple
print_items_in_collection((1, 2, 2, 3, 3, 4, 5, 5))

def print_items_in_dict(**dict_passed_in):
    print(type(dict_passed_in))
    for item in dict_passed_in:
        print(f"The key is {item} and its value is {dict_passed_in[item]}")
    number_of_items = len(dict_passed_in)
    print(f"The dictionary has {number_of_items} items.")

print_items_in_dict(a=1, b=2)