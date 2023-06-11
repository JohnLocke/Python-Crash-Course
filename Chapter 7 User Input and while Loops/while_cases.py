# 7-4 Pizza Toppings
# prompt = "Please tell me what toppings do you want? "
# prompt += "\n(Enter 'quit' when you are finished.)\n"

# while True:
#     topping = input(prompt)

#     if topping == 'quit':
#         break
#     else:
#         print(f"I’ll add {topping} to your pizza.\n")


# 7-5 Movie Tickets
# prompt = "How old are you?"
# prompt += "\n(Enter 'quit' when you are finished.)\n"

# while True:
#     age = input(prompt)

#     if age == 'quit':
#         break

#     else:
#         age = int(age)

#         if age < 3:
#             print("The ticket is free.\n")
#         elif age < 12:
#             print("The ticket is $10.\n")
#         else:
#             print("The ticket is $15.\n")


# 7-6 Three Exits
# Plan A: Use a conditional test in the while statement to stop the loop.
# prompt = "How old are you?"
# prompt += "\n(Enter 'quit' when you are finished.)\n"

# age = ''

# while age != 'quit':
#     age = input(prompt)

#     if age != 'quit':
#         age = int(age)

#         if age < 3:
#             print("The ticket is free.\n")
#         elif age < 12:
#             print("The ticket is $10.\n")
#         else:
#             print("The ticket is $15.\n")

# Plan B: Use an active variable to control how long the loop runs.
# prompt = "How old are you?"
# prompt += "\n(Enter 'quit' when you are finished.)\n"

# active = True

# while active:
#     age = input(prompt)

#     if age == 'quit':
#         active = False

#     else:
#         age = int(age)

#         if age < 3:
#             print("The ticket is free.\n")
#         elif age < 12:
#             print("The ticket is $10.\n")
#         else:
#             print("The ticket is $15.\n")


# Plan C: Use a break statement to exit the loop when the user enters a 'quit' value.
# prompt = "How old are you?"
# prompt += "\n(Enter 'quit' when you are finished.)\n"

# while True:
#     age = input(prompt)

#     if age == 'quit':
#         break

#     else:
#         age = int(age)

#         if age < 3:
#             print("The ticket is free.\n")
#         elif age < 12:
#             print("The ticket is $10.\n")
#         else:
#             print("The ticket is $15.\n")


# 7-7 Infinity
# while True:
#     print(1)


# 7-8 Deli
# sandwich_orders = ['Reuben sandwich', 'Submarine sandwich', 'oyster poboy',
#                    'Philly cheesesteak']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()

#     print(f"I made your {current_sandwich}.")
#     finished_sandwiches.append(current_sandwich)

# print("\n--- Finished_sandwiches ---")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)


# 7-9 No Pastrami
# sandwich_orders = ['Pastrami', 'Tuna', 'Ham', 'Chicken',
#                    'Pastrami', 'Ham', 'Pastrami']
# finished_sandwiches = []

# print("The deli has run out of pastrami.")

# while 'Pastrami' in sandwich_orders:
#     sandwich_orders.remove('Pastrami')

# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()

#     print(f"I made your {current_sandwich}.")
#     finished_sandwiches.append(current_sandwich)

# print("\n--- Finished_sandwiches ---")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)


# 7-10 Dream Vacation
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would you go? "

vacation_poll = {}
poll_active = True

while poll_active:
    name = input(name_prompt)
    place = input(place_prompt)

    vacation_poll[name] = place

    repeat = input("Would you like to ask another person? (yes/no) ")
    if repeat == 'no':
        poll_active = False

print("\n--- Poll Results ---")
for name, place in vacation_poll.items():
    print(f"{name.title()} would like to visit {place}.")



























    

