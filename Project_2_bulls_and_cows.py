"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie

author: Lenka Pazourová
email: lenka.pazourova@seznam.cz
discord: LenkaP
"""

import random
import datetime

separator = 50 * "-"

# Úvodní pozdrav
print("Hi there!",
      separator,
      "I've generated a random 4 digit number for you.",
      "Let's play a bulls and cows game.",
      separator,
      sep="\n")

# Generování náhodného 4 ciferného čísla
secret_number = [random.randint(1,9)] # range(1, 9) --> aby náhodné číslo nezačínalo nulouu
while len(secret_number) != 4:
    one_number = random.randint(0, 9)
    if one_number not in secret_number: # Číslice musí být unikátní
        secret_number.append(one_number)

def check_duplicate(user_number):
    """ Zkontroluj zadání uživatele a pokud obsahuje duplicity, vrať True, jinak vrať False."""
    for index in range(len(user_number)):
        for index_plus_one in range(index + 1, len(user_number)):
            if user_number[index] == user_number[index_plus_one]:
                return True
    else: 
        return False

attempt = 0 # Počítání pokusů uživatele

start_time = datetime.datetime.now()

while True:
    enter_number = input("Enter a number: ")
    print(separator)
    if len(enter_number) != 4:
        print("You did not enter a 4 digit number. Try again.")
    elif enter_number[0] == '0':
        print("Number must not start with zero. Try again.")
    elif not enter_number.isnumeric():
        print("Number contains not numeric character. Try again.")
    elif check_duplicate(enter_number):
        print("You entered duplicated values. Try again.")
    else:
        print(">>>", enter_number)
        bulls = 0
        cows = 0