programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    }

programming_dictionary["Loop"] = "The action of doing something over and over again."



empty_dictionary = {}

# programming_dictionary = {}

# print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer"

# print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France":{"cities_visited":["Paris","Lille","Dijon"]},
    "USA":{"trips_taken": ["Los Angeles","Brooklyn","Las Vegas"],"trips_to_come":2},
}



travel_log = [
    {
    "country":"France",
    "cities_visited":["Paris","Lille","Dijon"],
    "total_visits": 12,
    },
    {
    "home_country":"USA",
    "trips_taken": ["Los Angeles","Brooklyn","Las Vegas"],"trips_to_come":2
    },
]

