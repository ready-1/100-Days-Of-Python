from day6hangman.stages import stages
from day6hangman.logo import logo, goodbye, game_over, winner
from os import system, path, name
from random import randint
import linecache
from pprint import pprint as pp
  
# borrowed from https://www.geeksforgeeks.org/clear-screen-python/
def clear():  
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


params = {
    "play": True,
    "word": "",
    "score": 6,
    "guess": "",
    "names_file": path.join(path.dirname(__file__),"words.txt"),
    "letter_board": [],
    "used_letters": [],
    "message": ""
}


def get_random_word():
    with open(params["names_file"], 'r') as fp:
        for count, line in enumerate(fp):
            pass
    i = randint(0,count)
    return linecache.getline(params["names_file"], i).strip()


def setup_letter_board():
    
    result = []
    for letter in params["word"]:
        result.append("_")
    return result

def show_letter_board():
    for char in params["letter_board"]:
        print(char, end=" ")
    print("\n")


def setup():
    params["score"] = 6
    params["word"] = get_random_word()
    params["letter_board"] = setup_letter_board()
    params["used_letters"] = []
    params["guess"] = ""

    params["play"] = True
    params["word"] = get_random_word()
    params["score"] = 6
    params["guess"] = ""
    params["letter_board"] = setup_letter_board()
    params["used_letters"] = []
    params["message"] = ""



def score_the_guess():
    # exit
    if params["guess"] == "!":
        params["play"] = False
    # empty string
    elif  params["guess"] == "":
        params["message"] =  f'You didn\'t enter a letter.\nTry again.'
    # not a letter
    elif params["guess"].lower() not in "abcdefghijklmnopqrstuvwxyz-":
        params["message"] =  f'You entered \"{params["guess"]}\". That\'s not a letter.\nTry again.'
    # already guessed
    elif params["guess"] in params["used_letters"]:
        params["message"] =  f'You\'ve already guessed the letter \"{params["guess"]}\".\nTry again.'
    # good guess
    elif params["guess"] in params["word"]:
        params["message"] =  f'Correct!'
        params["used_letters"].append(params["guess"])
        for i in range(0, len(params["word"])):
            if params["word"][i] == params["guess"]:
                params["letter_board"][i] = params["guess"]
    # bad guess
    else:
        params["score"] -= 1
        if params["score"] == 0:
            params["play"] = False
        params["used_letters"].append(params["guess"])
        params["message"] =  f'You guessed wrong.  \"{params["guess"]}\" is not in the word.'
    return

def check_for_winner():
    return "_" not in params["letter_board"]
        

def prompt_for_guess():
    params["guess"] = input("Guess a letter: ").lower()


def draw_gallows():
    print(stages[params["score"]])


def display():
    clear()
    print(logo)
    print()
    draw_gallows()
    show_letter_board()
    print(params["message"])
    

def end_game():
    clear()
    if params["score"] == 0:
        print(game_over)
    else:
        print(goodbye)
    print()
    input("<Enter> to continue...")

def is_a_winner():
    clear()
    print(logo)
    print(winner)
    if input("Play Again? ").lower() == "y":
        setup()
    else:
        params["play"] = False

def main_loop():
    
    setup()
    while params["play"] == True:
        display()
        prompt_for_guess()
        score_the_guess()
        if check_for_winner():
            is_a_winner()

    end_game()

