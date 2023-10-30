"""
projekt_2.py: Druhý projekt do Engeto Online Python Akademie

author: Lenka Pazourová
email: lenka.pazourova@seznam.cz
discord: LenkaP
"""

import random
import datetime

# Funkce kontrolující vstup uživatele
def check_len(user_number):
    """Zkontroluj zadání uživatele a pokud nemá 4 znaky, vrať True, jinak False."""
    if len(user_number) != 4:
           return True
    else:
        return False

def check_zero(user_number):
    """Zkontroluj zadání uživatele a pokud začíná nulou, vrať True, jinak False."""
    if user_number[0] == '0':
        return True
    else:
        return False

def check_numeric(user_number):
    """Zkontroluj zadání uživatele a pokud obsahuje nenumerické znaky, vrať True, jinak False"""
    if not user_number.isnumeric():
        return True
    else:
        return False

def check_duplicate(user_number):
    """ Zkontroluj zadání uživatele a pokud obsahuje duplicity, vrať True, jinak vrať False."""
    for index in range(len(user_number)):
        for index_plus_one in range(index + 1, len(user_number)):
            if user_number[index] == user_number[index_plus_one]:
                return True
    else: 
        return False

# Generování náhodného čísla
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while True:
    secret_number = random.sample(numbers, 4)
    if secret_number[0] != 0:
        break

separator = 50 * "-"

# Úvodní pozdrav
print("Hi there!",
      separator,
      "I've generated a random 4 digit number for you.",
      "Let's play a bulls and cows game.",
      separator,
      sep="\n")

attempt = 0 # Počítání pokusů uživatele

start_time = datetime.datetime.now()

while True:
    enter_number = input("Enter a number: ")
    print(separator)
    if check_len(enter_number):
        print("You did not enter a 4 digit number. Try again.")
    elif check_zero(enter_number):
        print("Number must not start with zero. Try again.")
    elif check_numeric(enter_number):
        print("Number contains not numeric character. Try again.")
    elif check_duplicate(enter_number):
        print("You entered duplicated values. Try again.")
    else:
        print(">>>", enter_number)
        bulls = 0
        cows = 0

        for index, number in enumerate(enter_number):
            if enter_number[index] == str((secret_number)[index]):
                bulls += 1
            elif number in str(secret_number):
                cows += 1
        
        attempt += 1

        if bulls == 4:
            end_time = datetime.datetime.now()
            game_time = end_time - start_time
            print("Correct, you've guessed the right number", 
                    f"in {attempt} guesses.",
                    f"Your game time was {game_time}",
                    separator,
                    sep="\n")
            break
        
        bulls_word = "bull" if bulls == 1 else "bulls"
        cows_word = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bulls_word}, {cows} {cows_word}")
        print(separator)