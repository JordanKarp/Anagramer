import os


def clear_terminal():
    """Clears the terminal screen depending on the operating system being used."""
    _ = os.system("cls") if os.name == "nt" else os.system("clear")


def input_ranged_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                print("Invalid input. Please try again!")
        except ValueError:
            print("Invalid input. Please try again!")
