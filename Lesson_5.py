import csv

from helper_functions import (display_table, get_llm_response, print_llm_response)
from IPython.display import Markdown


## ------------------------------------------------------ ##
f = open("itinerary.csv", 'r')

## ------------------------------------------------------ ##
csv_reader = csv.DictReader(f)
itinerary = []

for row in csv_reader:
    print(row)
    itinerary.append(row)

## ------------------------------------------------------ ##
f.close()

## ------------------------------------------------------ ##
print(itinerary)

## ------------------------------------------------------ ##
type(itinerary)

## ------------------------------------------------------ ##
print(itinerary[0])
print(itinerary[6])

## ------------------------------------------------------ ##
print(itinerary[0]["Country"])
print(itinerary[5]["City"])

## ------------------------------------------------------ ##
print(itinerary[4])
print(itinerary[-2]["Country"])

## ------------------------------------------------------ ##
display_table(itinerary)

## ------------------------------------------------------ ##
filtered_data = []
filtered_city = []

for trip_stop in itinerary:
    if trip_stop["Country"] == "Japan":
        filtered_data.append(trip_stop)

for city_stop in itinerary:
    if city_stop["City"] == "New York":
        filtered_city.append(city_stop)

## ------------------------------------------------------ ##
display_table(filtered_data)
display_table(filtered_city)

## ------------------------------------------------------ ##
trip_stop = itinerary[0]
print(trip_stop)

city_stop = itinerary[6]
print(city_stop)

## ------------------------------------------------------ ##
city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]

my_city = city_stop["City"]
my_country = city_stop["Country"]
my_arrival = city_stop["Arrival"]
my_departure = city_stop["Departure"]

## ------------------------------------------------------ ##
prompt = f"""I will visit {city}, {country}, from {arrival} to {departure}.
        Please create a detailed daily itinerary."""

prmpt = f"""
        I am going to travel to {my_country}, {my_city}, from {my_arrival} to {my_departure}.
        Please create recommendations for sightseeing.
        """

print(prompt)
print(" ")
print(prmpt)

## ------------------------------------------------------ ##
response = get_llm_response(prompt)
my_response = get_llm_response(prmpt)

display(Markdown(response))
display(Markdown(my_response))

## ------------------------------------------------------ ##
filtered_data_Brazil = []

for trip_stop_Brazil in itinerary:
    if trip_stop_Brazil["Country"] == "Brazil":
        filtered_data_Brazil.append(trip_stop_Brazil)

print(filtered_data_Brazil)

## ------------------------------------------------------ ##
trip_stop = filtered_data_Brazil[0]

city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]

print(f" The city is: {city}")
print(f" The country is: {country}")
print(f" The arrival date is: {arrival}")
print(f" The departure date is: {departure}")

## ------------------------------------------------------ ##
prompt = f"""I will visit {city}, {country}, from {arrival} to {departure}.
        Please create a detailed daily itinerary."""

print_llm_response(prompt)

## ------------------------------------------------------ ##
f = open("itinerary.csv", "r")
csv_reader = csv.DictReader(f)
itinerary = []

for row in csv_reader:
    print(row)
    itinerary.append(row)

f.close()

unique_countries = []

for trip_stop in itinerary:
    country = trip_stop["Country"]

    if country not in unique_countries:
        unique_countries.append(country)
        print(f"Country: {country} .")
