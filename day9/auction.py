from os import system, name
from day9.art import logo as logo
import locale


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def display_logo():
    print(logo + "\n")


def ask_for_bid(bid_index):
    name = input("What is your name? ")
    bid = float(input("What is your bid? "))
    more_bidders = True
    if input("Are there anymore bidders? ").lower() == "n":
        more_bidders = False
    clear()
    return {"bid_index": bid_index, "name": name, "bid": bid, "more_bidders": more_bidders}


def take_bids():
    bids = []
    bid = {"name": None, "bid": None, "more_bidders": True}
    bid_index = 0

    while bid["more_bidders"] == True:
        bid = ask_for_bid(bid_index)
        bids.append(bid)
        bid_index += 1

    return bids


def display_winner(bids):
    winner = {"name": None, "bid": 0.00}
    for bid in bids:
        if bid["bid"] > winner["bid"]:
            winner["name"] = bid["name"]
            winner["bid"] = bid["bid"]

    winning_amount = locale.currency(float(winner["bid"]), grouping=True)
    print(f'The winner is {winner["name"]} with a bid of {winning_amount}')


def main():
    bids = {}
    clear()
    display_logo()
    bids = take_bids()
    display_winner(bids)
    input("<Enter> to continue...")
