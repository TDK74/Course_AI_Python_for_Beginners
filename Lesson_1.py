from os import *

import helper_functions

from helper_functions import *
from helper_functions import celsius_to_fahrenheit


## ------------------------------------------------------ ##
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")


def my_celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius}°C is equivalent to {fahrenheit:.2f}°F.")

## ------------------------------------------------------ ##
fahrenheit_to_celsius(68)
my_celsius_to_fahrenheit(34)

## ------------------------------------------------------ ##
celsius_to_fahrenheit(20)

## ------------------------------------------------------ ##
celsius_to_fahrenheit(20)

## ------------------------------------------------------ ##
helper_functions.print_llm_response("What is the capital of France?")

## ------------------------------------------------------ ##
response = get_llm_response("What is the capital of France?")

## ------------------------------------------------------ ##
response = helper_functions.get_llm_response("What is the capital of France?")
print(response)
reply = helper_functions.print_llm_response("What is the capital of Bulgaria?")

## ------------------------------------------------------ ##
response = get_llm_response("Give me three tips to become a good learner.")
reply = getcwd()

## ------------------------------------------------------ ##
print(response)
print(reply)
