# Why Python?

* Why learn python over other languages
  * syntax - simple and readable
  * extensive libraries
  * community support

* How can Python help with Cloud/DevOps/Support Engineering?
  * To integrate with tools/platforms that we need to use
  * To automate Repetitive tasks and processes using python scripts
  * to retrieve and manipulate data from external systems, services, application components
  
* How does it run?
  * interpreted ( may run slower than something compiled )
  * doesn't need compiling

* What is a Venv ( Virtual Environment)
  * An isolated system/environment to run particular libraries or versions of library needed for project.
  
# String Method
``` 
str_with_extra_spaces = "   extra spaces at the start and end   "
print(str_with_extra_spaces.strip())
print(len(str_with_extra_spaces))

#len() tells you the numbers of characters in a string
# .strip() removes spaces at the start and end of a string but not in the middle

#counts how many times jack is mentioned in print
print("captain jack jack sparrow".count('jack'))
#covert string to lowercase
print("captain jack sparrow".lower())
#covert to upper case
print("captain jack sparrow".upper())
#capatalise first letter
print("captain jack sparrow".capitalize())
#replace letter/word in string
print("captain jack sparrow".replace("captain","jack"))
```

## Concatenate these variables with different data types
``` 
x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"
#bidmas allows for numbers to be added with string also
print(str(x+y)+z)

#converting string into int/float
int_string = "6"
print(int_string)
print(int(int_string))
print(float(int_string))
```
## print line as an F-string
``` 
name = "Lassie"
years = 7
height_cm = 60.2
print(f"{name} is {years} years old and {height_cm}cm tall")
```
## F strings to format numbers 
``` 
pi = 3.14159265359
# (:) introduces format specification (.3/.5) round to 3/5 decimal places (f) floating point number
print(f"Pi to 3 decimal places is {pi:.3f}")
print(f"Pi to 3 decimal places is {pi:.5f}")

score = 16
max_score = 26
score_as_percent = 100 / 26 * score
score_as_decimal = score/max_score

print(f"score is {score_as_decimal}")
#score at percent round to 2 decimal figures
print(f"score is {score_as_percent:.2f}%")
# .0 means to 0 decimal places, % means to convert to percentage 
print(f"score is {score_as_decimal :.0%}")
```

## improvement of collecting data and presenting it
``` 
#defining inputs as variables
name = input("What is your name?")
age = input("What is your age?")
birth_month = input("what month is your bday in ?")
dob = input("what year were you born?")
#printing each variable with text 
print(f"Hi {name}, {age}, You were born in {birth_month} in {dob}")

//  Calculating the users year of birth //

#taking our user info as data
name = input("What is your name? ")
age = int(input("What is your age? "))
#defining year
current_year = 2025
# maths to deduct age from current year
year_born = current_year - age
# number of years x day in year including leap year x 24 hours in day 
hours = age * 365.25 * 24
#print out the users date of birth from the subtraction above
print(f"{name} is born in {year_born} you have lived {hours} hours ")

```

## Collections 
### shopping list
``` 
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

```
## mixing data in lists 
``` 
#taking our user info as data
name = input("What is your name? ")
age = int(input("What is your age? "))
height = float(input("What is your height in cm? "))
Date_of_birth = input("What is your date of birth? ")

Personal_detail = [ name,age,height,Date_of_birth]
print(Personal_detail)
print(f"{height}cm")
```
## slicing lists
``` 
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

```

## Tuples 
* How are tuples similar to lists? 
  * store collection of data

* Are tuples immutable and what does this mean? 
    * Yes they are immutable which means they cannot be modified

* What other data types are immutable?
    *numbers, boolean, tuples, and strings

* What are good use cases for tuples instead of lists? 
  * when you work with large datasets as they:
  * consume less memory
  * less error prone
  * more suitable for accessing elements efficiently 

* What does the following piece of code do? 

`essentials = ("bread", "eggs", "milk") `
 
`print(essentials) `
`print(essentials.count("bread")) `
* it counts how many times the word bread is mentioned/occurs within the tuple
 
