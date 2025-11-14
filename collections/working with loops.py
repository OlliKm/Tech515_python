from idlelib.configdialog import is_int

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

counter = 0 # starting number of lists

while counter < 10: # 1 counter = 5 = list_data
    for number in list_data: # for every number within the list
        print(f'num {number}') # it needs to print the number
        counter = counter + 1 #as there's 5 numbers in list until it reaches 10 printed keep printing list

data = embedded_lists
for data in embedded_lists:
    print(data)

print("New list")

#cant get this to add 3
data2 = embedded_lists
for data2 in embedded_lists:
    print(data2)
    print(data2[0])
    print(data2[1])
#result
# [1, 2, 3]
# 1
# 2
# [4, 5, 6]
# 4
# 5
print("Dict data")

name = dict_data
for name in dict_data:
    print(name)
print("loop through dictionairy")

name2 = dict_data
print(name2 )

