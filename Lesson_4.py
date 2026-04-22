import requests

from aisetup import celsius_to_fahrenheit as CtF
from aisetup import get_llm_response
from bs4 import BeautifulSoup
from helper_functions import *
from IPython.display import HTML, display


## ------------------------------------------------------ ##
url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

response = requests.get(url)

print(response)

## ------------------------------------------------------ ##
HTML(f'<iframe src={url} width="60%" height="400"></iframe>')

## ------------------------------------------------------ ##
soup = BeautifulSoup(response.text, 'html.parser')

all_text = soup.find_all('p')

combined_text = ""

for text in all_text:
    combined_text = combined_text + "\n" + text.get_text()

print(combined_text)

## ------------------------------------------------------ ##
prompt = f"""Extract the key bullet points from the following text.

        Text:
        {combined_text}
        """

## ------------------------------------------------------ ##
print_llm_response(prompt)

## ------------------------------------------------------ ##
response = get_llm_response("Why is the programming language called Python?")

print(response)

## ------------------------------------------------------ ##
prompt = f"""Extract the answer of the question:
        "Who built the new short course mentioned in the letter?"
        from the following text.

        Text:
        {combined_text}
        """

print_llm_response(prompt)

## ------------------------------------------------------ ##
zero_celsius_in_fahrenheit = CtF(0)
print(zero_celsius_in_fahrenheit)

## ------------------------------------------------------ ##
url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

batch_response = requests.get(url)

print(batch_response)

HTML(f'<iframe src={url} width="60%" height="400"></iframe>')

soup = BeautifulSoup(batch_response.text, 'html.parser')

all_text = soup.find_all('h1')

title_text = ""

for text in all_text:
    title_text = title_text + "\n" + text.get_text()

    if title_text == "The World Needs More Intelligence":
        break

title = title_text

print(title)

print("===========================================================================")

url = 'https://www.deeplearning.ai/the-batch/the-world-needs-more-intelligence/'

try:
    batch_response = requests.get(url)
    batch_response.raise_for_status()

    soup = BeautifulSoup(batch_response.text, 'html.parser')

    title_element = soup.find('h1')

    if title_element:
        title = title_element.get_text()
    else:
        title = "Title not found"

    print(title)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
