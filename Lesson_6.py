from helper_functions import get_llm_response
from helper_functions import print_llm_response
from IPython.display import Markdown, display


## ------------------------------------------------------ ##
print("Hello World!")

## ------------------------------------------------------ ##
friends_list = ["Tommy", "Isabel", "Daniel", "Otto"]

len(friends_list)

## ------------------------------------------------------ ##
print_llm_response("What is the capital of France")

## ------------------------------------------------------ ##
f = open("cape_town.txt", "r")
journal_cape_town = f.read()
f.close()
print(journal_cape_town)

## ------------------------------------------------------ ##
f = open("paris.txt", "r")
journal_paris = f.read()
f.close()
print(journal_paris)

## ------------------------------------------------------ ##
def print_journal(file):
    f = open(file, "r")
    journal = f.read()
    f.close()
    print(journal)

## ------------------------------------------------------ ##
print_journal("sydney.txt")

## ------------------------------------------------------ ##
def read_journal(file):
    f = open(file, "r")
    journal = f.read()
    f.close()
    # print(journal)

    return journal

## ------------------------------------------------------ ##
journal_tokyo = read_journal("tokyo.txt")

## ------------------------------------------------------ ##
print(journal_tokyo)

## ------------------------------------------------------ ##
print(len(journal_tokyo))

## ------------------------------------------------------ ##
fahrenheit = 72

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

## ------------------------------------------------------ ##
fahrenheit = 68

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

## ------------------------------------------------------ ##
fahrenheit = 76

celsius = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

## ------------------------------------------------------ ##
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9

    print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

## ------------------------------------------------------ ##
fahrenheit_to_celsius(71)

## ------------------------------------------------------ ##
fahrenheit_to_celsius(70)

## ------------------------------------------------------ ##
fahrenheit_to_celsius(212)

## ------------------------------------------------------ ##
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    # print(f"{fahrenheit}°F is equivalent to {celsius:.2f}°C")

    return celsius

## ------------------------------------------------------ ##
fahrenheit = 45
celsius = fahrenheit_to_celsius(fahrenheit)

## ------------------------------------------------------ ##
print(celsius)

## ------------------------------------------------------ ##
type(celsius)

## ------------------------------------------------------ ##
def celsius_to_fahrenheit(celcius):
    fahrenheit = round((9 / 5 * celcius + 32), 2)

    return fahrenheit


print(celsius_to_fahrenheit(0))
print('')
print(celsius_to_fahrenheit(100))
print('')
print(celsius_to_fahrenheit(13))

## ------------------------------------------------------ ##
def meters_to_feet(meters):
    feet = round(3.28084 * meters, 5)

    return feet


print(meters_to_feet(10))
print(meters_to_feet(0.7))

## ------------------------------------------------------ ##
def create_bullet_points(file):
    f = open(file, "r")
    file_contents = f.read()
    f.close()

    prompt = f"""
            Create a three bullet point summary of the following text:
            {file_contents}.
            """

    bullets = get_llm_response(prompt)

    return bullets


bullet_points = create_bullet_points("istanbul.txt")
print(bullet_points)
print("Length of bullet points:", len(bullet_points))
print("Type of bullet points:", type(bullet_points))
