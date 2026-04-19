from math import cos, floor, pi, sin, tan
from random import randint, sample
from statistics import mean, median, stdev

from helper_functions import get_llm_response


## ------------------------------------------------------ ##
print(pi)

## ------------------------------------------------------ ##
type(pi)

## ------------------------------------------------------ ##
values = [0, pi/2, pi, 3/2*pi, 2*pi]

## ------------------------------------------------------ ##
for value in values:
    print(f"The cosine of {value:.2f} is {cos(value):.2f}")

## ------------------------------------------------------ ##
for value in values:
    print(f"The sine of {value:.2f} is {sin(value):.2f}")

## ------------------------------------------------------ ##
floor(5.7)

## ------------------------------------------------------ ##
my_friends_heights = [160, 172, 155, 180, 165, 170, 158, 182, 175, 168]

## ------------------------------------------------------ ##
mean(my_friends_heights)

## ------------------------------------------------------ ##
stdev(my_friends_heights)

## ------------------------------------------------------ ##
spices = ["cumin", "turmeric", "oregano", "paprika"]
vegetables = ["lettuce", "tomato", "carrot", "broccoli"]
proteins = ["chicken", "tofu", "beef", "fish", "tempeh"]

## ------------------------------------------------------ ##
random_spices = sample(spices, 2)
random_vegetables = sample(vegetables, 2)
random_protein = sample(proteins, 1)

## ------------------------------------------------------ ##
print(random_protein)

## ------------------------------------------------------ ##
prompt = f"""Please suggest a recipe that includes the following ingredients.

        Spices: {random_spices}
        Vegetables: {random_vegetables}
        Proteins: {random_protein}
        """

## ------------------------------------------------------ ##
print(prompt)

## ------------------------------------------------------ ##
recipe = get_llm_response(prompt)

print(recipe)

## ------------------------------------------------------ ##
values = [0, pi/2, pi, 3/2*pi, 2*pi]

for value in values:
    print (f"The tangent of {value:.2f} is {tan(value):.2f} .")

## ------------------------------------------------------ ##
scores = [28, 14, 15, 25, 21, 26, 30, 8, 36]

median_score = median(scores)
print(median_score)

## ------------------------------------------------------ ##
digits_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

random_digit = sample(digits_sample, 1)
print("Random sample digit:", random_digit)

random_value = randint(1, 10)
print("Random randint value:", random_value)
