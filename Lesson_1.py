from helper_functions import print_llm_response, get_llm_response

## ------------------------------------------------------ ##
name = "Tommy"

## ------------------------------------------------------ ##
prompt = f"""
        Write a four line birthday poem for my friend {name}.
        The poem should be inspired by the first letter of my friend's name.
        """

print_llm_response(prompt)

## ------------------------------------------------------ ##
friends_list = ["Tommy", "Isabel", "Daniel"]

## ------------------------------------------------------ ##
print(friends_list)

## ------------------------------------------------------ ##
type(friends_list)

## ------------------------------------------------------ ##
len(friends_list)

## ------------------------------------------------------ ##
prompt = f"""
        Write a set of four line birthday poems for my friends {friends_list}.
        The poems should be insipred by the first letter of each friend's name.
        """

print(prompt)

## ------------------------------------------------------ ##
print_llm_response(prompt)

## ------------------------------------------------------ ##
first_friend = friends_list[0]
print(first_friend)

## ------------------------------------------------------ ##
print(friends_list[1])

## ------------------------------------------------------ ##
print(friends_list[3]) # Gives an error

## ------------------------------------------------------ ##
print(friends_list[2])

## ------------------------------------------------------ ##
print(friends_list)

## ------------------------------------------------------ ##
friends_list.append("Otto")

## ------------------------------------------------------ ##
friends_list.append('Cuci')
print(friends_list)

## ------------------------------------------------------ ##
friends_list.remove("Tommy")

## ------------------------------------------------------ ##
friends_list.remove("Cuci")
print(friends_list)

## ------------------------------------------------------ ##
list_ages = [42, 28, 30]

## ------------------------------------------------------ ##
print(list_ages)

## ------------------------------------------------------ ##
list_of_tasks = ["Compose a brief email to my boss explaining that I will be late for tomorrow's "
                "meeting.",
                "Write a birthday poem for Otto, celebrating his 28th birthday.",
                "Write a 300-word review of the movie 'The Arrival'."]

## ------------------------------------------------------ ##
task = list_of_tasks[0]
print_llm_response(task)

## ------------------------------------------------------ ##
task = list_of_tasks[1]
print_llm_response(task)

## ------------------------------------------------------ ##
task = list_of_tasks[2]
print_llm_response(task)
print_llm_response("Write a 100-word review of the film 'Edge of Tomorrow'.")

## ------------------------------------------------------ ##
movie_list = ['Inception', 'Edge of Tomorrow', 'The Arrival', 'Oblivion', 'Interstellar']

## ------------------------------------------------------ ##
prime_numbers = [2, 3, 5, 7, 11]

for prime in prime_numbers:
    print(prime)

## ------------------------------------------------------ ##
prime_numbers = [2, 3, 5, 7, 11]

print(prime_numbers[3])

## ------------------------------------------------------ ##
friends_list = ["Tommy", "Isabel", "Daniel", "Otto"]

friends_list.append("John")

print(friends_list)

## ------------------------------------------------------ ##
countries_in_south_america = ["Colombia", "Peru", "Brasil", "Japan", "Argentina"]

countries_in_south_america.remove("Japan")

print(countries_in_south_america)
