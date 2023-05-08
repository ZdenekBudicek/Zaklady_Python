travel_diary = [
    {
        "country": "Spain",
        "visited_cities": ["Madrid", "Leon", "Valencia"],
        "visits": 5
    },
    {
        "country": "France",
        "visited_cities": ["Paris", "Nice", "Rennes"],
        "visits": 2
    }
]


def add_country(country_name, town_list, visits_number):
    new_dictionary = {}
    new_dictionary["country"] = country_name
    new_dictionary["visited_cities"] = town_list
    new_dictionary["visits"] = visits_number
    travel_diary.append(new_dictionary)


add_country("Itealy", ["Rome", "Florence", "Milan"], 9)
print(travel_diary)
print(travel_diary[2]["visited_cities"][1])
