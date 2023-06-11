# 6-1
# acquaintances = {
#     'first_name': 'John',
#     'last_name': 'Locke',
#     'age': 21,
#     'city': 'Beijing',
# }
# print(acquaintances['first_name'])
# print(acquaintances['last_name'])
# print(acquaintances['age'])
# print(acquaintances['city'])


# 6-2
# favorite_numbers = {
#     'Tatum': 0,
#     'Brown': 7,
#     'Curry': 30,
#     'Harden': 13,
#     'Kobe': 24,
# }

# favorite_number = favorite_numbers['Tatum']
# print(f"Tatum's favorite number is {favorite_number}.")


# 6-3
glossary ={
    'object': 'Any data with state (attributes or value) and '\
               'defined behavior (methods).',
    'method': 'A function which is defined inside a class body.',
    'PEP': 'Python Enhancement Proposal.',
    'list': 'A built-in Python sequence.',
    'dictionary': 'An associative array, where arbitrary keys are '\
                   'mapped to values. '
}

# print(f"object: {glossary['object']}")
# print(f"\nmethod: {glossary['method']}")
# print(f"\nPEP: {glossary['PEP']}")
# print(f"\nlist: {glossary['list']}")
# print(f"\ndictionary: {glossary['dictionary']}")

# 6-4
# for key, value in glossary.items():
#     print(f"{key}: {value}")

# 6-5
# rivers = {
#     'Yangtze River': 'China', 
#     'Seine River': 'France',
#     'Mississippi River': "USA"
# }

# for river, country in rivers.items():
#     print(f"The {river} runs through {country}.")
# for river in rivers.keys():
#     print(river)
# for country in rivers.values():
#     print(country)

# 6-6 polling
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# poll_list = ['jen', 'edward', 'lily', 'kevin']

# for person in poll_list:
#     if person in favorite_languages.keys():
#         print(f"Thank you for taking the poll, {person.title()}.")
#     else:
#         print(f"Welcome to take the poll, {person.title()}.")


# 6-7
# john = {
#     'first_name': 'John',
#     'last_name': 'Locke',
#     'age': 21,
#     'city': 'Beijing',
# }

# jason = {
#     'first_name': 'Jason',
#     'last_name': 'Tatum',
#     'age': 25,
#     'city': 'Boston',
# }

# jaylen= {
#     'first_name': 'Jaylen',
#     'last_name': 'Brown',
#     'age': 26,
#     'city': 'LA',
# }

# people = [john, jason, jaylen]

# for p in people:
#     print(f"Name: {p['first_name'].title()} {p['last_name'].title()}")
#     print(f"Age: {p['age']}")
#     print(f"City: {p['city']}\n")

# 6-8
# pet_0 = {
#     'type': 'dog',
#     'owner': 'john',
# }

# pet_1 = {
#     'type': 'cat',
#     'owner': 'jason',
# }

# pet_2 = {
#     'type': 'bird',
#     'owner': 'jaylen',
# }

# pets =[pet_0, pet_1, pet_2]

# for pet in pets:
#     print(f"{pet['owner'].title()} has a {pet['type']}.")


# 6-9
# favorite_places = {
#     'john': ['Beijing', 'Pairs', 'Toronto'],
#     'jason': ['LA', 'New York'],
#     'jaylen': ['Boston'],
# }

# for people, places in favorite_places.items():
#     if len(favorite_places[people]) == 1:
#         print(f"\n{people.title()}'s favorite place is {place}.")
#     else:
#         print(f"\n{people.title()}'s favorite place are:")
#         for place in places:
#             print("\t" + place)


# 6-10
# favorite_numbers = {
#     'Tatum': [0, 24],
#     'Brown': [1, 7],
#     'Curry': [11, 30],
#     'Harden': [1, 13],
#     'Kobe': [8, 24],
# }

# for name, numbers in favorite_numbers.items():
#     print(f"\n{name.title()}'s favorite number are:")
#     for number in numbers:
#         print(f"\t{number}")

# 6-11
cities = {
    'Beijing': {
        'country': 'China',
        'population': 21_540_000,
        'fact': "the captial of China",
    },

    'Pairs': {
        'country': 'France',
        'population': 11_000_000,
        'fact': "the captial of France",
    },

    'New York': {
        'country': 'the USA',
        'population': 8_390_000,
        'fact': 'not the captial of the USA',
    },
}

for city, info in cities.items():
    print(f"\n{city}")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")





























