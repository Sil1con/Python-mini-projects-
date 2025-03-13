# Blackjack
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def congrats():
    print(f"You won! Congratulations!")

def lost():
    print(f"You lost! Computer Won!")

def count_score(cards):
    score = 0
    for card in cards:
        score += card
    return score
def add_card(deck):
    rand = int((random.random() * len(deck)) - 0.5)
    return deck[rand]

def final_result(player_cards, computer_cards):
    player_score = count_score(player_cards)
    computer_score = count_score(computer_cards)
    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's cards: {computer_cards}, final score: {computer_score}")
    
    if player_score == computer_score:
        print("Bust!")
    elif player_score == 21:
        print("Blackjack! You won!")
    elif computer_score == 21:
        print("Computer won with a Blackjack!")
    elif player_score > 21:
        lost()
    elif computer_score > 21:
        congrats()
    elif player_score > computer_score:
        congrats()
    elif player_score < computer_score:
        lost()

def fill_computer_cards(computer_cards):
    computer_score = count_score(computer_cards)
    if computer_score == 21:
        final_result(player_cards, computer_cards)
    while computer_score < 17:
        card = add_card(deck)
        if card == 11 and computer_score + card > 21:
            card = 1
            computer_cards.append(card)
        else:
            computer_cards.append(card)
        computer_score = count_score(computer_cards)
    else:
        final_result(player_cards, computer_cards)

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
stop = False

# Start of the program
while stop != True:
    print("\n")
    print(logo)
    player_cards = []
    computer_cards = []
    computer_score = 0
    player_score = 0
    
    # Reward player and computer by two cards
    for i in range(0, 2):
        random.shuffle(deck)
        player_cards.append(add_card(deck))
        computer_cards.append(add_card(deck))
    
    computer_score = count_score(computer_cards)
    player_score = count_score(player_cards)
    print(f"    Your cards: {player_cards}, current score: {player_score}")
    print(f"    Computer's card: {computer_cards[0]}")
    
    if player_score == 21:
        final_result(player_cards, computer_cards)
    else: 
        answer = input("Type 'yes' to get additional card or 'no' to pass: ")
        if answer == "no":
            fill_computer_cards(computer_cards)
        else:
            while answer == "yes":
                player_score = count_score(player_cards)
                card = add_card(deck)
                player_cards.append(card)
                player_score = count_score(player_cards)
                print(f"    Your cards: {player_cards}, current score: {player_score}")
                print(f"    Computer's card: {computer_cards[0]}")
                
                # Check user's score
                if player_score == 21:
                    final_result(player_cards, computer_cards)
                    break
                elif player_score > 21:
                    final_result(player_cards, computer_cards)
                    break
                else:    
                    # Repeat while-loop
                    answer = input("Type 'yes' to get additional card or 'no' to pass: ")
                    if answer == "yes":
                        continue
                    else:
                        fill_computer_cards(computer_cards)
                        break
                            
    # Restart the game
    answer = input("Would you like to restart?: ")
    if answer == "yes":
        continue
    else:
        stop = True
        