from bk_utils import clear
import locale

locale.setlocale(locale.LC_ALL, '')

menu_items = [
    ["Day 7 - Hangman", "from day7hangman import hangman as hangman",
        "hangman.main_loop()"],
    ["Day 7 - Hangman OOP", "from day7hangmanOOP import hangmanOOP as hangmanOOP",
        "hangmanOOP.play()"],
    ["Day 8 - Paint Coverage Calculator",
        "from day8 import area_calc as d8area", "d8area.main()"],
    ["Day 8 - Prime Checker",
        "from day8 import prime_finder as d8prime", "d8prime.main()"],
    ["Day 8 - Caesar Cipher",
        "from day8 import caesar as d8caesar", "d8caesar.main()"],
    ["Day 9 - Caesar Cipher",
     "from day9 import auction as d9auction", "d9auction.main()"],
]


def display_menu():
    clear()
    print("       MENU\n========================")
    for i in range(0, len(menu_items)):
        print(f'{i + 1}: {menu_items[i][0]}')
    print("Q: Quit\n")


def menu():
    for item in menu_items:
        print(f'Executing \"{item[1]}\"...')
        exec(f'{item[1]}')

    while True:
        display_menu()
        choice = input("Option: ")
        if choice.lower() == "q":
            clear()
            exit()
        elif int(choice) in range(1, len(menu_items) + 1):
            exec(f"{menu_items[int(choice) - 1][2]}")
        else:
            pass


menu()
