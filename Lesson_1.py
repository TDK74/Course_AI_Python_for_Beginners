from helper_functions import get_llm_response
from helper_functions import print_llm_response
from IPython.display import Markdown, display


## ------------------------------------------------------ ##
ingredients = ['chicken', 'broccoli', 'rice']

prompt = f"""
        Create a short recipe that uses the following ingredients:
        {ingredients}
        """

response = get_llm_response(prompt)

print(response)

## ------------------------------------------------------ ##
f = open("email.txt", "r")
email = f.read()
f.close()

## ------------------------------------------------------ ##
print(email)


## ------------------------------------------------------ ##
prompt = f"""Extract bullet points from the following email.
            Include the sender information.

            Email:
            {email}
            """

print(prompt)

## ------------------------------------------------------ ##
bullet_points = get_llm_response(prompt)
print(bullet_points)

## ------------------------------------------------------ ##
display(Markdown(bullet_points))

## ------------------------------------------------------ ##
prompt = f"""Summarise from the email in bullet points
            all the countries mentioned in it.

            Email:
            {email}
            """

countries = get_llm_response(prompt)
print(countries)

## ------------------------------------------------------ ##
prompt = f"""list all of the activities that Daniel did on
            his trip in bullet points per country / city or town.

            Email:
            {email}
            """

print("Displayed with get_llm_response(prompt)")
activities = get_llm_response(prompt)
print(activities)

print("\n Displayed in Markdown format with get_llm_response()")
display(Markdown(activities))

print("\n Displayed with print_llm_response(prompt)")
print_llm_response(prompt)

print("\n Displayed in Markdown format with print_llm_response(prompt)")
display(Markdown(activities))
