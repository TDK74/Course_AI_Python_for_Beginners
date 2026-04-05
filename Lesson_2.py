from helper_functions import upload_txt_file, list_files_in_directory, print_llm_response


## ------------------------------------------------------ ##
list_files_in_directory()

## ------------------------------------------------------ ##
# f = open("email.txt", "r")
# email = f.read()
# f.close()

with open("email.txt", "r") as f:
    email = f.read()

print(email)

## ------------------------------------------------------ ##
# f = open("recipe.txt", "r")
# recipe = f.read()
# f.close()

with open("recipe.txt", "r") as f:
    recipe = f.read()

print(recipe)

## ------------------------------------------------------ ##
upload_txt_file()

## ------------------------------------------------------ ##
list_files_in_directory()

## ------------------------------------------------------ ##
f = open("testcheta.txt", "r")
your_file_content = f.read()
f.close()

## ------------------------------------------------------ ##
print(your_file_content)

## ------------------------------------------------------ ##
prompt = f"""Summarize the content from the following text
        in at most two sentences.

        Text:
        {your_file_content}
        """

## ------------------------------------------------------ ##
print(prompt)

## ------------------------------------------------------ ##
print_llm_response(prompt)

## ------------------------------------------------------ ##
prompt = f"""What is the corect answer of question #1 (Q1)?
        What is the corect answer of question #2 (Q2)?
        What is the corect answer of question #3 (Q3)?
        What is the corect answer of question #4 (Q4)?
        What is the corect answer of question #5 (Q5)?

        Please, elaborate a bit on each of answer.

        Text:
        {your_file_content}
        """

print_llm_response(prompt)

## ------------------------------------------------------ ##
prompt = f"""Identify all of the cooking techniques, used in the
        following recipe:

        Elaborate a bit on each technique.

        Recipe:
        {recipe}
        """

print_llm_response(prompt)
