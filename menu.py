from bk_utils import clear


menu_items = [
    ["Day 6 - Hangman", "from day7hangman import hangman as hangman",
        "hangman.main_loop()"],
    ["Day 6 - Hangman OOP", "from day7hangmanOOP import hangmanOOP as hangmanOOP",
        "hangmanOOP.play()"],
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

        print(dir())
        exec(f"{menu_items[int(choice) - 1][2]}")


menu()
