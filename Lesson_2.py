from helper_functions import print_llm_response, get_llm_response


## ------------------------------------------------------ ##
list_of_tasks = ["Compose a brief email to my boss explaining that I will be late for tomorrow's "
                "meeting.",
                "Write a birthday poem for Otto, celebrating his 28th birthday.",
                "Write a 300-word review of the movie 'The Arrival'."]

print(list_of_tasks)

## ------------------------------------------------------ ##
task = list_of_tasks[0]
print_llm_response(task)

## ------------------------------------------------------ ##
for task in list_of_tasks:
    print(task)

## ------------------------------------------------------ ##
for task in list_of_tasks:
    print_llm_response(task)

## ------------------------------------------------------ ##
ice_cream_flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

## ------------------------------------------------------ ##
for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below,
                provide a captivating description that could be used for promotional purposes.

            Flavor: {flavor}

            """

    # print(prompt)
    print_llm_response(prompt)

## ------------------------------------------------------ ##
promotional_descriptions = []

for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below,
                provide a captivating description that could be used for promotional purposes.

            Flavor: {flavor}

            """

    description = get_llm_response(prompt)
    promotional_descriptions.append(description)

## ------------------------------------------------------ ##
print(promotional_descriptions)
#print(promotional_descriptions[3])

## ------------------------------------------------------ ##
ice_cream_flavors = ["Chocolate", "Mint Chocolate Chip"]

for flavor in ice_cream_flavors:
    print(flavor)

## ------------------------------------------------------ ##
ice_cream_flavors = ["Vanilla", "Strawberry"]

for flavor in ice_cream_flavors:
    prompt = f"""For the ice cream flavor listed below,
                translate the flavors in ice_cream_flavors to Spanish and Bulgarian.

            Flavor: {flavor}
            """

    print_llm_response(prompt)

## ------------------------------------------------------ ##
words_with_typos = ["Aple", "Wether", "Newpaper"]
words_without_typos = []

for word in words_with_typos:
    prompt = f"""Fix the spelling mistake in the following word: {word}
                and translate it in Bulgarian as well.
                Provide only the pairs in the following format:
                English word / Bulgarian word.
            """

    correct_word = get_llm_response(prompt)
    words_without_typos.append(correct_word)

print(words_without_typos)
