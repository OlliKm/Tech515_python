from symtable import Class
from turtledemo.penrose import start
from wsgiref.validate import check_input

bad_string = "I said 'Wow!'"
print(bad_string)
bad_string = 'I said "Wow!"'
print(bad_string)
bad_string = 'I said `Wow!`'
print(bad_string * 2)

Hw = "Hello world!"
print(Hw)
print(Hw[0:5])
print(Hw[6:12])
# -1 / - numbers means it goes backwards from last number
print(Hw[-2:6])
print(Hw[1])
# the [] is determining what letter and what position from 0 to 12 characters.

#String Slicing game
import random

print("You must guess the word, the less amount of letters the more points you gain when providing the correct word")
Words = ["Ghosts", "mitochondria", "Recommendation"]

Words = ["Recommendation","mitochondria","Ghosts"]
Recommendation = ["R","e","c","o","m","m","e","n","d","a","t","i","o","n" ]
mitochondria = ["M","i","t","o","c","h","o","n","d","r","i","a" ]
Ghosts = ["G","h","o","s","t","s" ]

guesses = 5

answer = (random.choice(Words))
if answer == "Ghosts": print(f"Your first letter is:   {random.choice(Ghosts)}")
if answer == "mitochondria": print(f"Your first letter is:   {random.choice(mitochondria)}")
if answer == "Recommendation": print(f"Your random letter provided is:   {random.choice(Recommendation)}")



prev_answer = answer[1]

while True:
    guesses = input("Guess the word: ")
    if guesses == Words:
        guesses = True
        print("You guessed the word!")
        break
    else:
        print("This is incorrect try again")
        print(random.choice(answer[2]) + prev_answer)
