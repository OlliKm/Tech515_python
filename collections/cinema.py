# possible film ratings are "universal", "pg", "12", "12a", "15", "18"
film_rating = "12a"
#checking user age
user_age = int(input("What is your age?"))

# ratings
if user_age < 12:
    print("this film is suitable for all")
elif user_age <= 12:
    print("General viewing, but some scenes may be unsuitable for young children.")
elif user_age <= 12:
    print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
elif user_age <= 15:
    print("No one younger than 15 may see a 15 film in a cinema.")
elif user_age < 18:
    print("No one younger than 18 may see an 18 film in a cinema.")
elif user_age > 18:
    print("you can watch any of the films")
else:
    print("This is not a correct rating, please use universal, pg, 12, 12a, 15, 18")