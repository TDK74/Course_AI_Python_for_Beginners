from helper_functions import print_llm_response, get_llm_response


## ------------------------------------------------------ ##
food_preferences_tommy = {"dietary_restrictions" : "vegetarian",
                        "favorite_ingredients" : ["tofu", "olives"],
                        "experience_level" : "intermediate",
                        "maximum_spice_level" : 6}

## ------------------------------------------------------ ##
print(food_preferences_tommy.keys())

## ------------------------------------------------------ ##
print(food_preferences_tommy.values())

## ------------------------------------------------------ ##
prompt = f"""Please suggest a recipe that tries to include the following ingredients:
             {food_preferences_tommy["favorite_ingredients"]}.
            The recipe should adhere to the following dietary restrictions:
             {food_preferences_tommy["dietary_restrictions"]}.
            The difficulty of the recipe should be:
             {food_preferences_tommy["experience_level"]}.
            The maximum spice level on a scale of 10 should be:
             {food_preferences_tommy["maximum_spice_level"]}.
            Provide a two sentence description.
            """

## ------------------------------------------------------ ##
print(prompt)

## ------------------------------------------------------ ##
print_llm_response(prompt)

## ------------------------------------------------------ ##
available_spices = ["cumin", "turmeric", "oregano", "paprika"]

## ------------------------------------------------------ ##
prompt = f"""Please suggest a recipe that tries to include the following ingredients:
             {food_preferences_tommy["favorite_ingredients"]}.
            The recipe should adhere to the following dietary restrictions:
             {food_preferences_tommy["dietary_restrictions"]}.
            The difficulty of the recipe should be:
             {food_preferences_tommy["experience_level"]}.
            The maximum spice level on a scale of 10 should be:
             {food_preferences_tommy["maximum_spice_level"]}.
            Provide a two sentence description.

            The recipe should not include spices outside of this list:
            Spices: {available_spices}
            """

print(prompt)

## ------------------------------------------------------ ##
recipe = get_llm_response(prompt)

## ------------------------------------------------------ ##
print(recipe)

## ------------------------------------------------------ ##
print(food_preferences_tommy["dietary_restrictions"])

## ------------------------------------------------------ ##
food_preferences_tommy["is_vegetarian"] = True

## ------------------------------------------------------ ##
print(food_preferences_tommy)

## ------------------------------------------------------ ##
my_food_preferences = {"dietary_restrictions" : ['aubergine', 'nettle'],
                        "favorite_ingredients" : ['red-hot peppers', 'chilli sauce', 'garlic',
                                                'onion', 'leek', 'cheese', 'yellow cheese',
                                                'yogurt', 'pork meat', 'chicken meat',
                                                'grilled vegetables', 'grilled meat', 'fish'],
                        "experience_level" : "gourmand",
                        "maximum_spice_level" : 10}

print(my_food_preferences)

## ------------------------------------------------------ ##
prompt = f"""Please suggest a recipe that tries to include the following ingredients:
             {my_food_preferences["favorite_ingredients"]}.
            The recipe should adhere to the following dietary restrictions:
             {my_food_preferences["dietary_restrictions"]}.
            The difficulty of the recipe should be:
             {my_food_preferences["experience_level"]}.
            The maximum spice level on a scale of 10 should be:
             {my_food_preferences["maximum_spice_level"]}.
            Provide a recipe that includes detailed instructions.
            """

print_llm_response(prompt)
