# blackjack machine simulator
import random


def cash_in():
    while True:
        amount = input("Type amount of money you want to play with: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Given number must be greater than 0.')
        else:
            print("The number is incorrect. Type another number")
    return amount


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


def player_roll():
    pass


def players_hand():
    player_hand = []
    player_hand_value = []

    while len(player_hand) != 2:
        var_p = random.choice(list(CARDS.keys()))
        val_var_p = CARDS[var_p]
        player_hand.append(var_p)
        player_hand_value.append(int(val_var_p))
        if len(player_hand) == 2:
            print(f"Player's cards are: {player_hand} and it's value is equal to: {sum(player_hand_value)}")

        return sum(player_hand_value)


def computers_hand():
    computer_hand = []
    computer_hand_value = []

    while len(computer_hand) != 2:
        var_c = random.choice(list(CARDS.keys()))
        val_var_c = CARDS[var_c]
        computer_hand.append(var_c)
        computer_hand_value.append(int(val_var_c))
        if len(computer_hand) == 2:
            print(f"Computer's cards are X and  {computer_hand[-1]}"
                  f" and it's value is equal to: {sum(computer_hand_value)}")
            return sum(computer_hand_value)


def bet():
    while True:
        amount = input("How much would you like to bet?")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter the appropriate number.")
    return amount


def game():
    com_sum = computers_hand()
    player_sum = players_hand()
    if com_sum == 21:
        print("Computer has won.")
    elif com_sum > 21:
        print("Player won, because computer had value over 21. ")
    while player_sum < 21:
        decision = input("Do you want to bet/stay/hit?")
        if decision == "hit":
            player_sum += (int(random.choice(list(CARDS.values()))))
            print(f"After hit your hand's value is {player_sum}")
        elif decision == "bet":
            actual_bet = bet()
            player_sum += (int(random.choice(list(CARDS.values()))))
            print(f"After hit your hand's value is {player_sum} with actual bet: {actual_bet}")
        elif decision == "stay":
            print(f"Values of the hands are: "
                  f"player: {int(player_sum)}"
                  f"computer: {int(com_sum)}")
            if com_sum > player_sum:
                print("Computer wins!")
            else:
                print("Player wins!")
                break
    if player_sum > 21:
        return "Computer wins!"

    elif player_sum == 21:
        return "Player wins!"


print(game())

