import random

names_string = input('Give me everybodys names, seperated by comma. ')

names = names_string.split(',')

person_who_will_pay = random.choice(names)

print(person_who_will_pay + ' is to pay for the meal today!')

"""num_items = len(names)

random_choice = random.randint(0, num_items - 1)
lists_of_names = names[random_choice]
print(lists_of_names + " is to pay for the meal today")"""

