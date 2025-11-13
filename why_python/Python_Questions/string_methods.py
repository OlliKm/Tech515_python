first_name = 'Jack'

print(first_name.replace('ck','que'))

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

names = "Lassie"
years = 7
height_cm = 60.2
print(f"{names} is {years} years old and {height_cm}cm tall")

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
