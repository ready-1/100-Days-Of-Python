from os import system, name
from math import ceil


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def calculate_coverage(height, width, coverage):
    area = (height * width)
    cans_required = area / coverage
    return ceil(cans_required)


def main():
    clear()

    height = int(input("What is the height of the wall? "))
    width = int(input("What is the  of the wall? "))
    coverage = int(input("What is the per can? "))

    total_cans = calculate_coverage(height, width, coverage)

    print(f"HEIGHT: {height}")
    print(f"WIDTH: {width}")
    print(f"COVERAGE: {coverage}")
    print(f"You will need {total_cans} cans of paint.")

    print(input("<Enter> to continue..."))
