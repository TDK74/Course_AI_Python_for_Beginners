from helper_functions import *


## ------------------------------------------------------ ##
print("¯\_(ツ)_/¯")

## ------------------------------------------------------ ##
print_llm_response("What is the capital of France?")

## ------------------------------------------------------ ##
type(17)

## ------------------------------------------------------ ##
print(len("Hello World!"))

## ------------------------------------------------------ ##
print(round(42.17))

## ------------------------------------------------------ ##
string_length = len("Hello World!")
print(string_length)

## ------------------------------------------------------ ##
name = "Tommy"
potatoes = 4.75
prompt = f"""Write a couplet about my friend {name} who has about {round(potatoes)} potatoes"""
response = get_llm_response(prompt)
print(response)

## ------------------------------------------------------ ##
lucky_number = 34 * 10
print(f"Your lucky number is {lucky_number}!")

favorite_number = int(input("Enter one of your favorite numbers: "))
lucky_number = favorite_number * 10
print(f"Your lucky number is {lucky_number}!")

## ------------------------------------------------------ ##
number_of_lines = 34
prompt = f"""Write a poem about with {number_of_lines} number of lines"""
print_llm_response(prompt)

## ------------------------------------------------------ ##
number_of_lines = 15
prompt = f"""Write a heroic poem about with {number_of_lines} number of lines"""
response = get_llm_response(prompt)
print(response)
