from helper_functions import print_llm_response


## ------------------------------------------------------ ##
print_llm_response("What is the capital of France?")

## ------------------------------------------------------ ##
name = "Otto Matic"
dog_age = 21 / 7

## ------------------------------------------------------ ##
print_llm_response(f"""If {name} were a dog, he would be {dog_age} years old.
                 Describe what life stage that would be for a dog and what that might
                 entail in terms of energy level, interests, and behavior.""")

## ------------------------------------------------------ ##
driver = "unicorn"
drivers_vehicle = "colorful, asymmetric dinosaur car"
favorite_planet = "Pluto"

## ------------------------------------------------------ ##
print_llm_response(f"""Write me a 300 word children's story about a {driver} racing
                     a {drivers_vehicle} for the {favorite_planet} champion cup.""")

## ------------------------------------------------------ ##
first_favorite_book = "1001 Ways to Wear a Hat"
second_fav_book = "2002 Ways to Wear a Scarf"
print(f"My most favorite book is {first_favorite_book}, but I also like {second_fav_book}.")

## ------------------------------------------------------ ##
my_fav_game = "Halo"
my_fav_films = "Edge of Tomorrow and Inception"
my_fav_food = "Home made food"
print_llm_response(f"""Recommend me a new song to listen to if
                     my favourite game is {my_fav_game},
                     my favourite films are {my_fav_films}
                     and my favourite food is {my_fav_food}
                    """)
