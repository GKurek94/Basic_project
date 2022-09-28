#blackjack machine simulator
import random

BALANCE = 0 

def cash_in():
    while True:
        amount = input("Type amount of money you want to play with: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print('Given number must be greater than 0.')
        else:
            print("The number is incorrect. Type another number")
    return amount            


CARDS = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10,
    'A':11, # A is 1 or 11 depends which is better for the player
} 

def player_roll():
    #function which decides who is starting the game
    possibilities = ['player', 'casino']
    return random.choice(possibilities)

def game_of_computer():
    BALANCE = 0 
    while BALANCE < 21:
        BALANCE += random.choice(CARDS.values)
    return BALANCE
game_of_computer()