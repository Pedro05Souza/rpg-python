import os

__all__ = ['clear_terminal']

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')