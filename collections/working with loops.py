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
for data2 in embedded_lists:
    print(data2)
    for item in data2:
        print(item)

#result
# [1, 2, 3]
# 1
# 2
# [4, 5, 6]
# 4
# 5
print("Dict data")

#try simplicity the way its done
for key in dict_data:
    print(dict_data[key])

print("\n part 6")

for data in dict_data:
    print(dict_data[data]["name"])
    print(dict_data[data]["money"])

print("question 7")

for data3 in dict_data:
    print(dict_data[data3]["money"])




