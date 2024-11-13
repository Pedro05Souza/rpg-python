import os
from random import choice

__all__ = ['clear_terminal', 'name_generator']

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def name_generator() -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    combinations = [
        "VCV",
        "CVC",
        "VCCV",
        "CVCC",
        "CVCCV",
        "VCCVC",
        "CVCCC",
        "CVCCCC",
        "CVCCCCV",
    ]
    random_combination = choice(combinations)

    name = ""
    for letter in random_combination:
        if letter == "V":
            name += choice("aeiou")
        else:
            name += choice(alphabet)

    return name.capitalize()