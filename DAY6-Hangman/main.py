from stages import stages
from logo import logo
from os import system, name
  
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
    "words": [],
    "score": 6,
    "letter": ""
}


def setup():
    global params
    with open('words.txt', 'r') as f:
        params["words"] = f.readlines()
    params["words"] = [x.strip() for x in params["words"]]


def prompt_for_guess():
    global params
    params["guess"] = input("Guess a letter: ").lower()

def draw_gallows():
    global params
    print(stages[params["score"]])

def display():
    global params
    clear()
    print(logo)
    print()
    draw_gallows()
    prompt_for_guess()


def main_loop():
    global params
    while params["play"] == True:
        pass


setup()
display()

