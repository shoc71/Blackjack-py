import random

# Global variables
blackjack = 21
ace = 11
cards = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]  # Values for ace through 10

# Function to replace an ace from 11 to 1 if needed to keep the hand valid
def replace_ace(hand):
    if sum(hand) > 21:
        for i, card in enumerate(hand):
            if card == ace:
                hand[i] = 1
                break
    return hand

# Function for player's turn
def player_turn(player_hand, dealer_hand):
    while sum(player_hand) <= blackjack:
        print(f"\nPlayer's Hand: {player_hand}")
        print(f"Dealer's Hand: {dealer_hand[0]} [Hidden]")
        decision = input("Hit or Stand? (hit/stand): ").lower()
        if decision == "hit" or decision == "h":
            player_hand.append(random.choice(cards))
            player_hand = replace_ace(player_hand)
            print(f"Player hits. Player's Hand: {player_hand}")
        elif decision == "stand" or decision == "s":
            print("Player stands.")
            break
        else:
            print("Invalid input. Please try again.")

# Function for dealer's turn
def dealer_turn(player_hand, dealer_hand):
    while sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
        dealer_hand = replace_ace(dealer_hand)
        print(f"Dealer hits. Dealer's Hand: {dealer_hand}")
    if sum(dealer_hand) > blackjack:
        print("Dealer busts.")

# Function to determine the outcome of the game
def determine_winner(player_hand, dealer_hand):
    player_total = sum(player_hand)
    dealer_total = sum(dealer_hand)
    if player_total > blackjack:
        print("Player busts. Dealer wins.")
    elif dealer_total > blackjack:
        print("Dealer busts. Player wins.")
    elif player_total == dealer_total:
        print("It's a tie.")
    elif player_total > dealer_total:
        print("Player wins.")
    else:
        print("Dealer wins.")

# Function to replay the game
def replay_game():
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes" or replay == "y":
        play_game()
    else:
        print("Thanks for playing!")

# Main function to play the game
def play_game():
    print("Welcome to Blackjack!")
    player_hand = [random.choice(cards), random.choice(cards)]
    dealer_hand = [random.choice(cards), random.choice(cards)]
    print(f"Player's Hand: {player_hand}")
    print(f"Dealer's Hand: {dealer_hand[0]} [Hidden]")

    player_turn(player_hand, dealer_hand)
    if sum(player_hand) <= blackjack:
        dealer_turn(player_hand, dealer_hand)
        determine_winner(player_hand, dealer_hand)
    replay_game()

# Start the game
play_game()
