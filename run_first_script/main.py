
import random
# Word slicing game,

original_word = "recommendation"

scrambled_word = "eoommandretnic"

hints = [
    (original_word[6: 7],"is the 7th positon"),
     (original_word[8: 10], "is the 9th & 10th positon"),
      (original_word[11: 13],"is the 12th & 13th positon"),
       (original_word[14: 16], "is the 15 & 16th position")
    ]

print("Scrambled word:", scrambled_word)
print("Guess the original word from the scrambled version.")

attempts = 0

while True:
    guess = input("What's your guess?").lower()

    if guess == original_word:
        print("Your guess is correct!")
        break
    else:
        print("Wrong")
        if attempts < len(hints):
            print(hints[attempts])
        else:
            print("no more hints left")
        attempts += 1

