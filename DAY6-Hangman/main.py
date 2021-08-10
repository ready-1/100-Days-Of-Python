from stages import stages
from logo import logo


params = {
    "play": True,
    "words": []
}


def setup():
    global params
    with open('words.txt', 'r') as f:
        params["words"] = f.readlines()
    params["words"] = [x.strip() for x in params["words"]]


def main_loop():
    while play == True:
        pass


setup()

