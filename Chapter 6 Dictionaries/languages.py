favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# items()
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# keys()
# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}.")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")


# Loop through all keys in order
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")


# Loop through all values
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# Loop through all values without duplicate items.
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())


# build a set directly using braces
languages = {'python', 'ruby', 'python', 'c'}
print(languages)












