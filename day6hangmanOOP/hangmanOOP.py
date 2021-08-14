from random import randint
from os import system, path, name
import linecache
from pprint import pprint as pp
from day6hangmanOOP.assets import logo, stages
from string import ascii_letters as ascii_letters
import string


word_list = path.join(path.dirname(__file__), "words.txt")


class Game:

    def __init__(self):
        self.score = 6  # remaining plays in this game
        self.letter_board = []  # the wheel of fortune
        self.play_state = "playing"  # can be playing, won, lost
        self.min_length = 1  # TODO add word length filters
        self.max_length = 99
        self.word = ""  # the current random word
        self.history = []  # every keystroke the player has entered while playing a game
        self.current_guess = ""  # the last letter the player entered
        self.flash_message = ""  # message to display to the player when the screen refreshes
        self.continue_game = True  # keep the main loop going
        self.reset()  # set all the params to their defaults

    def reset(self):
        # reset the score, letter_board and history
        self.score = 6
        self.letter_board = []
        self.history = []
        self.current_guess = ""
        self.flash_message = ""
        self.play_state = "playing"

        # get a new word
        self.word = self.get_new_word()
        # set up the letter board
        self.letter_board = ["_" for i in range(0, len(self.word))]

    def get_new_word(self):
        with open(word_list, 'r') as fp:
            for count, line in enumerate(fp):
                pass
        i = randint(0, count)
        return linecache.getline(word_list, i).strip()

    def display_logo(self):
        global logo
        print(logo)
        print("Object Oriented Version")

    def display_stage_graphic(self):
        # display the current gallows
        global stages
        print(stages[self.score])

    def display_board(self):
        for i in self.letter_board:
            print(f'{i} ', end='')
        print("\n")

    def display_score(self):
        print(f'PLAYS REMAINING: {self.score}')

    def display_flash(self):
        print(self.flash_message)

    def display_stats(self):
        print()
        print(
            f'The word is "{self.word}" which is {len(self.word)} characters long.')
        print(f'You used {len(self.history)} guesses.')
        print(f'Your guesses were: {" ".join(self.history)}')
        print()

    def enter_new_guess(self):
        self.current_guess = input("Enter a letter: ")

    def add_to_history(self):
        # inserts the current guess at the front of the list
        self.history.append(self.current_guess)

    def update_letter_board(self):
        # loop through the word and change the letterboard to
        # the correct letter using the index of the letter's position
        # in the current word.
        for i in range(0, len(self.word)):
            if self.word[i] == self.current_guess:
                self.letter_board[i] = self.current_guess

    def ask_another_game(self):
        while True:
            response = input("Play again? Y/N ").upper()
            if response == "Y":
                self.reset()
                return True
            elif response == "N":
                return False
            else:
                print("I didn't understand that...")

    def score_current_guess(self):
        guess = self.current_guess
        # "!" to quit
        if guess == "!":
            self.continue_game = False
            self.flash_message = "GOODBYE"
        # not a letter
        elif guess not in ascii_letters:
            self.flash_message = f'"{guess}" is not a letter.  Try again.'
            self.add_to_history()
        # already been guessed
        elif guess in self.history:
            self.flash_message = f'You\'ve already guessed "{guess}".  Try again.'
        # guess is correct
        elif guess in self.word:
            self.update_letter_board()
            self.flash_message = "CORRECT!"
            self.add_to_history()
            # easy test for winners: is the letterboard full?
            if "_" not in self.letter_board:
                self.play_state = "won"
                self.flash_message = "WINNER!"
        # guess is wrong
        else:
            self.score -= 1
            self.flash_message = f'INCORRECT!'
            self.add_to_history()
            if self.score == 0:
                self.play_state = "lost"
                self.flash_message = "GAME OVER"

    def refresh_display(self):
        self.status()
        self.clear()
        self.display_logo()
        self.display_stage_graphic()
        self.display_board()
        self.display_score()
        self.display_flash()

    def play_turn(self):
        self.refresh_display()
        self.enter_new_guess()
        self.score_current_guess()

    # this is the main game loop
    def play_game(self):
        while self.continue_game == True:
            if self.play_state == "playing":
                # the actual gameplay
                self.play_turn()
            elif self.play_state == "lost" or self.play_state == "won":
                self.refresh_display()
                self.display_stats()
                self.continue_game = self.ask_another_game()

        self.clear()
        print(logo)
        print("GOODBYE")

    # borrowed from https://www.geeksforgeeks.org/clear-screen-python/

    def clear(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    # for debugging
    def status(self):
        print(f'SCORE: {self.score}')
        print(f'BOARD: {self.letter_board}')
        print(f'PLAY: {self.play_state}')
        print(f'MIN LEN: {self.min_length}')
        print(f'MAX LEN: {self.max_length}')
        print(f'CURRENT WORD: {self.word}')
        print(f'HISTORY: {self.history}')


def play():
    g = Game()
    g.play_game()
