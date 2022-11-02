# blackjack machine simulator

# Importing required libraries
import random

# constant variables which can be changed in program
CASH = 0
MIN_BET = 1
MAX_BET = 200
CARDS = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11,  # A is 1 or 11 depends which is better for the player
}


# creating player hand composed of 2 hands, the result of the function is value of both hands
def players_hand():
    player_hand = []
    player_hand_value = []

    while len(player_hand) != 2:
        var_p = random.choice(list(CARDS.keys()))
        val_var_p = CARDS[var_p]
        player_hand.append(var_p)
        player_hand_value.append(int(val_var_p))
        if len(player_hand) == 2:
            print(f"Player's cards are: {player_hand}")
            return sum(player_hand_value)


# creating computer hand composed of 2 hands, the result of the function is value of both hands
def computers_hand():
    computer_hand = []
    computer_hand_value = []

    while len(computer_hand) != 2:
        var_c = random.choice(list(CARDS.keys()))
        val_var_c = CARDS[var_c]
        computer_hand.append(var_c)
        computer_hand_value.append(int(val_var_c))
        if len(computer_hand) == 2:
            print(f"Computer's cards are X and {computer_hand[-1]}")
            return sum(computer_hand_value)


# Function about the bet and it's value
def bet():
    while True:
        amount = input("How much would you like to bet?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be greater than 0 and lower than Maximum bet.")
        else:
            print("Please enter the appropriate number.")
    return amount


# main function
def game():

    # values from previous functions
    money = bet()
    com_sum = computers_hand()
    player_sum = players_hand()

    # condition describing computer's value
    if com_sum == 21:
        print("Computer has won.")
    elif com_sum > 21:
        print("Player won, because computer had value over 21. ")
    # looping to create computer and player's hand
    while player_sum < 21:
        decision = input("Do you want to bet/stay/hit?")
        if decision == "hit":
            next_card = random.choice(list(CARDS.keys()))
            if next_card == 'A' and player_sum > 11:
                player_sum += 1
            else:
                val_next_card = CARDS[next_card]
                player_sum += (int(val_next_card))
            print(f"After hit your hand's value is {player_sum}")
        elif decision == "bet":
            actual_bet = bet()
            next_card = random.choice(list(CARDS.keys()))
            if next_card == 'A' and player_sum > 11:
                player_sum += 1
            else:
                val_next_card = CARDS[next_card]
                player_sum += (int(val_next_card))
            print(f"After hit your hand's value is {player_sum} with actual bet: {int(money) + int(actual_bet)}")
        elif decision == "stay":
            while com_sum < player_sum:
                com_sum += (int(random.choice(list(CARDS.values()))))
            print(f"Values of the hands are: "
                  f"player: {int(player_sum)} "
                  f"computer: {int(com_sum)}.")
            if com_sum > 21:
                print("Player wins!")
            elif player_sum < com_sum < 21:
                return "Computer wins!"
            else:
                return "Player wins!"

    if player_sum > 21:
        return "Computer wins!"

    elif player_sum == 21:
        return "Player wins!"


print(game())
