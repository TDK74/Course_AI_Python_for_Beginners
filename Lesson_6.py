import os

from aisetup import authenticate, get_llm_response, print_llm_response
from dotenv import load_dotenv
from openai import OpenAI


## ------------------------------------------------------ ##
load_dotenv('.env', override = True)
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key = openai_api_key)

## ------------------------------------------------------ ##
def get_llm_response(prompt):
    completion = client.chat.completions.create(model = "gpt-4o-mini",
                                                messages = [
                                                            {
                                                            "role" : "system",
                                                            "content" : "You are an AI assistant.",
                                                            },
                                                            {"role" : "user", "content" : prompt},
                                                            ],
                                                temperature = 0.0,
                                                )
    response = completion.choices[0].message.content

    return response

## ------------------------------------------------------ ##
prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)

## ------------------------------------------------------ ##
def get_llm_response(prompt):
    completion = client.chat.completions.create(model = "gpt-4o-mini",
                                                messages = [
                                                            {
                                                            "role" : "system",
                                                            "content" : "You are a drunk AI "
                                                                        "assistant.",
                                                            },
                                                            {"role" : "user", "content" : prompt},
                                                            ],
                                                temperature = 0.5,
                                                )
    response = completion.choices[0].message.content

    return response

## ------------------------------------------------------ ##
prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)

## ------------------------------------------------------ ##
def get_llm_response(prompt):
    completion = client.chat.completions.create(model = "gpt-4o-mini",
                                                messages = [
                                                            {
                                                            "role" : "system",
                                                            "content" : "You are an artistic AI "
                                                                        "assistant.",
                                                            },
                                                            {"role" : "user", "content" : prompt},
                                                            ],
                                                temperature = 0.7,
                                                )
    response = completion.choices[0].message.content

    return response

## ------------------------------------------------------ ##
prompt = "What is the capital of France?"
response = get_llm_response(prompt)
print(response)

## ------------------------------------------------------ ##
authenticate("YOUR API KEY HERE")

print_llm_response("What is the capital of France")

response = get_llm_response("What is the capital of France")
print(response)

## ------------------------------------------------------ ##
load_dotenv('.env', override = True)
openai_api_key = os.getenv('OPENAI_API_KEY')
authenticate(openai_api_key)

print_llm_response("What is the capital of France")

response = get_llm_response("What is the capital of France")
print(response)
