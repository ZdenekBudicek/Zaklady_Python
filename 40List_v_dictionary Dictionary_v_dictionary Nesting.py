# Nesting

cities = {
    "Spain": "Madrid",
    "France": "Paris"
}

# List v dictionary

print(cities["Spain"])

travel_diary = {
    "Spain": ["Madrid", "Leon", "Valancia"],
    "France": ["Paris", "Nice", "Rennes"]
}

print(travel_diary)
print(travel_diary["France"][0])

# Dictionary v dictionary

travel_diary = {
    "Spain": {"visited_cities": ["Madrid", "Leon", "Valancia"], "visits": 5},
    "France": {"visited_cities": ["Paris", "Nice", "Rennes"], "visits": 18}
}
print(travel_diary["Spain"]["visited_cities"][1])
print(travel_diary["France"]["visits"])

# Dictionary v listu

travel_diary = [
    {"country": "Spain",
     "visited_cities": ["Madrid", "Leon", "Valancia"],
     "visits": 5
     },

    {"country": "France",
     "visited_cities": ["Paris", "Nice", "Rennes"],
     "visits": 18
     },
]
print(travel_diary[0])
