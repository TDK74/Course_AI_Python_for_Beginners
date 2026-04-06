from helper_functions import get_llm_response, print_llm_response


## ------------------------------------------------------ ##
f = open("cape_town.txt", "r")
journal_cape_town = f.read()
f.close()

## ------------------------------------------------------ ##
print(journal_cape_town)

## ------------------------------------------------------ ##
f = open("tokyo.txt", "r")
journal_tokyo = f.read()
f.close()

## ------------------------------------------------------ ##
print(journal_tokyo)

## ------------------------------------------------------ ##
prompt = f"""Respond with "Relevant" or "Not relevant":
        the journal describes restaurants and their specialties.

        Journal:
        {journal_tokyo}
        """

## ------------------------------------------------------ ##
print_llm_response(prompt)

## ------------------------------------------------------ ##
files = ["cape_town.txt", "madrid.txt", "rio_de_janeiro.txt", "sydney.txt", "tokyo.txt"]

## ------------------------------------------------------ ##
for file in files:
    f = open(file, "r")
    journal = f.read()
    f.close()

    prompt = f"""Respond with "Relevant" or "Not relevant":
    the journal describes restaurants and their specialties.

    Journal:
    {journal}
    """

    print(f"{file} -> {get_llm_response(prompt)}")

## ------------------------------------------------------ ##
f = open("madrid.txt", "r")
print(f.read())
f.close()

## ------------------------------------------------------ ##
files = ["cape_town.txt", "madrid.txt", "rio_de_janeiro.txt", "sydney.txt", "tokyo.txt"]
prompts = ["Respond with 'Relevant' or 'Not relevant': the journal describes restaurants and "
            "their specialties.",
            "Respond with 'Yes' or 'No': the journal describes restaurants and food dishes.",
            "Respond with 'Yes' or 'No': the journal mentions a dessert.",
            "Respond with 'Positive' or 'Negative': the journal describes the restaurant design."]

for file in files:
    f = open(file, "r")
    journal = f.read()
    f.close()

    for prompt in prompts:
        prmpt = f"""{prompt}

                Journal:
                {journal}
                """

        print(f"{file} -> {get_llm_response(prmpt)}")

## ------------------------------------------------------ ##
files = ["cape_town.txt", "madrid.txt", "rio_de_janeiro.txt", "sydney.txt", "tokyo.txt"]

for file in files:
    f = open(file, "r")
    journal = f.read()
    f.close()

    prompt = f"""Respond with "Yes" or "No" if the journal mentions:
            - a vegetarian dish;
            - a vegan dish;
            - both;
            - neither.

            Journal:
            {journal}
            """

    print(f"{file} -> {get_llm_response(prompt)}")
