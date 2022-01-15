movies_watched = {"The Matrix", "Her", "The Big Short"}
user_movie = input("Enter a movie you've recently watched: ")

# The "in" keyword works in sets, lists, tuples, and strings
# It returns a boolean value based on whether the first element is found within the second
print(user_movie in movies_watched)