from stages import stages
from logo import logo
from os import system
  
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
    "words": []
}


def setup():
    global params
    with open('words.txt', 'r') as f:
        params["words"] = f.readlines()
    params["words"] = [x.strip() for x in params["words"]]


def display():
    global params

    clear()


def main_loop():
    while play == True:
        pass


setup()

