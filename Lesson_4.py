from helper_functions import *
from IPython.display import HTML, display


## ------------------------------------------------------ ##
journal_rio_de_janeiro = read_journal("rio_de_janeiro.txt")

## ------------------------------------------------------ ##
prompt = f"""
        Given the following journal entry from a food critic,
        identify the restaurants and their best dishes.
        Highlight and bold each restaurant (in orange) and
        best dish (in blue) within the original text.
        Highlight any desserts in green.
        Add a relevant emoji beside any ingredients.

        Provide the output as HTML suitable for display in a Jupyter notebook.

        Journal entry:
        {journal_rio_de_janeiro}
        """

print(prompt)

## ------------------------------------------------------ ##
html_response = get_llm_response(prompt)
print(html_response)

## ------------------------------------------------------ ##
display(HTML(html_response))

## ------------------------------------------------------ ##
journal_tokyo = read_journal("tokyo.txt")

prompt = f"""
        Given the following journal entry from a food critic,
        identify the restaurants and their best dishes.
        Highlight and bold each restaurant (in orange)
        and best dish (in blue) within the original text.
        Highlight any desserts in green.
        Add a relevant emoji beside any ingredients.


        Provide the output as HTML suitable for display in a Jupyter notebook.

        Journal entry:
        {journal_tokyo}
        """

html_response = get_llm_response(prompt)
display(HTML(html_response))

## ------------------------------------------------------ ##
prompt = f"""Please extract a comprehensive list of the restaurants
        and their respective best dishes mentioned in the following journal entry.
        Ensure that each restaurant name is accurately identified and listed.

        Provide your answer in CSV format, ready to save.
        Exclude the "```csv" declaration, don't add spaces after the comma, include column headers.

        Format:
        Restaurant, Dish
        Res_1, Dsh_1
        ...

        Journal entry:
        {journal_rio_de_janeiro}
        """

restaurants_csv_ready_string = get_llm_response(prompt)

print(restaurants_csv_ready_string)

## ------------------------------------------------------ ##
files = ["cape_town.txt", "istanbul.txt", "new_york.txt", "paris.txt", "rio_de_janeiro.txt",
         "sydney.txt", "tokyo.txt"]

for file in files:
    journal_entry = read_journal(file)

    prompt =  f"""Please extract a comprehensive list of the restaurants
            and their respective best dishes mentioned in the following journal entry.

            Extract the restaurant name and the neighborhood it is located in.

            Extract each dish and it's main ingredient.

            Ensure that each restaurant name is accurately identified and listed.
            Provide your answer in CSV format, ready to save.

            Exclude the "```csv" declaration, don't add spaces after the
            comma, include column headers.

            Format:
            Restaurant, Neighborhood, Dish, Main ingredient
            Res_1, Nbh_1, Dsh_1, M_ingr_1
            ...

            Journal entry:
            {journal_entry}
            """

    print(file)
    print_llm_response(prompt)
    print("")

## ------------------------------------------------------ ##
display(HTML(html_response))

## ------------------------------------------------------ ##
# f = open("highlighted_text.html", 'w')
# f.write(html_response)
# f.close()

with open("highlighted_text.html", 'w') as f:
    f.write(html_response)

## ------------------------------------------------------ ##
download_file()

## ------------------------------------------------------ ##
journal_sydney = read_journal("sydney.txt")

# Modify the prompt below
prompt = f"""
        Given the following journal entry from a food critic,
        identify the restaurants and their best dishes.
        Highlight and bold each restaurant name (in green),
        its neighborhoods (in pink),
        its best dish (in blue),
        highlight any desserts (in yellow) and
        add a relevant emoji beside any ingredients within the original text.

        Provide the output as HTML suitable for display in a Jupyter notebook.

        Journal entry:
        {journal_sydney}
        """

html_sydney = get_llm_response(prompt)
display(HTML(html_sydney))

## ------------------------------------------------------ ##
#f = open()
#f.write()
#f.close()

with open("highlighted_sydney.html", 'w') as f:
    f.write(html_sydney)

## ------------------------------------------------------ ##
download_file()
