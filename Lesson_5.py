from helper_functions import print_llm_response, get_llm_response


## ------------------------------------------------------ ##
food_preferences_tommy = {
                        #"dietary_restrictions" : "vegetarian",
                        "favorite_ingredients" : ["mushrooms", "olives"],
                        "experience_level" : "intermediate",
                        "maximum_spice_level" : 6
                        }

## ------------------------------------------------------ ##
food_preferences_tommy["is_vegetarian"] = True

## ------------------------------------------------------ ##
print(food_preferences_tommy)

## ------------------------------------------------------ ##
print(True)
print(False)

## ------------------------------------------------------ ##
type(True)

## ------------------------------------------------------ ##
type(False)

## ------------------------------------------------------ ##
is_tommy_my_friend = True

## ------------------------------------------------------ ##
is_isabel_older_than_me = False

## ------------------------------------------------------ ##
print(is_tommy_my_friend)

## ------------------------------------------------------ ##
print(is_isabel_older_than_me)

## ------------------------------------------------------ ##
type(is_isabel_older_than_me)

## ------------------------------------------------------ ##
isabel_age = 28
daniel_age = 30
tommy_age = 30

## ------------------------------------------------------ ##
print(isabel_age > daniel_age)

## ------------------------------------------------------ ##
print(isabel_age < daniel_age)

## ------------------------------------------------------ ##
is_isabel_older_than_daniel = isabel_age > daniel_age
print(is_isabel_older_than_daniel)

## ------------------------------------------------------ ##
print(isabel_age <= daniel_age)

## ------------------------------------------------------ ##
print(tommy_age < daniel_age)

## ------------------------------------------------------ ##
print(tommy_age <= daniel_age)

## ------------------------------------------------------ ##
print(tommy_age == daniel_age)

## ------------------------------------------------------ ##
print(isabel_age == daniel_age)

## ------------------------------------------------------ ##
print("vegetarian" == "vegan")

## ------------------------------------------------------ ##
is_tommy_my_friend = True
is_isabel_my_friend = True

## ------------------------------------------------------ ##
print(is_tommy_my_friend and is_isabel_my_friend)

## ------------------------------------------------------ ##
print(is_tommy_my_friend or is_isabel_my_friend)

## ------------------------------------------------------ ##
isabel_age = 28
daniel_age = 30
otto_age = 29

## ------------------------------------------------------ ##
is_isabel_younger_than_tommy = isabel_age < tommy_age
is_isabel_younger_than_daniel = isabel_age < daniel_age

## ------------------------------------------------------ ##
print(is_isabel_younger_than_tommy and is_isabel_younger_than_daniel)

## ------------------------------------------------------ ##
is_isabel_older_than_tommy = isabel_age > tommy_age
is_isabel_older_than_daniel = isabel_age > daniel_age

print("Check if Isabel is older than at least one of my friends")
print(is_isabel_older_than_tommy or is_isabel_older_than_daniel)
