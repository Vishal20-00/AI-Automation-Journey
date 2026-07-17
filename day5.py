age = int(input("Entre your age:"))
is_movie_18 = input("Is the movie rated 18+? (Yes/No)").lower() =="yes"
if not is_movie_18:
    print("You can watch this movie.")
elif age >= 18:
    print("You can watch this movie")
else:
    print("You are under 18 and you can not watch this movie")
    