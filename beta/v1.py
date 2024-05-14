# imports
import random

# global variables
blackjack = 21
jack, queen, king =  10, 10, 10
ace = 11 # ace 
cards = [ace, 2, 3, 4, 5, 6, 7, 8, 9, jack, queen, king]
# cards= [ace]

# replacing an ace in the off-chance one or both aces are drawn in the starting hand
# AND THE PLAYER/DEALER KEEPS DRAWING ACES (YES IT JUST HAPPENED, ONLY REASON WHY THIS FUNCTION EXISTS)
def replace_ace(lst, old_value, new_value):
    # output = [str(x) for x in lst]
    found_11 = False
    new_list = []
    for x in lst:
        if x == old_value and not found_11:
            new_list.append(new_value)
            found_11 = True
        elif x == old_value and found_11:
            new_list.append(1)  # Convert the second instance of 11 to 1
        else:
            new_list.append(x)
    return new_list

# player playing the game
def gameplay(player_hand, dealer_hand):

    # player draws immediate blackjack
    if (sum(player_hand) == blackjack):
        print(f"BLACKJACK. YOU WIN WITH A DRAW of {player_hand}.\n")
        replay_game()

    # converting player ace from 11 into 1 to keep him in the game
    if (sum(player_hand) > blackjack) and (11 in player_hand):
        player_hand = replace_ace(player_hand, 11, 1)
        print(f"player hand ace has now been converted into an 1 to stay in the game.\n")
        if (sum(player_hand) > blackjack):
            print(f"Busted. You Lose. You went over 21. Your Hand {player_hand}. Final score {sum(player_hand)}\n")

    # getting player input
    user_input = input("Hit or Stand? (hit/stand): ")

    if (user_input.lower() == "hit") or (user_input.lower() == "h") or (user_input.lower() == ";"):
        print(f"Player chose \"{user_input}\" == HIT")
        player_hand.append(random.choice(cards))

        # player went over blackjack
        if (sum(player_hand) > blackjack) and (11 not in player_hand):
                print(f"Busted. You Lose. You went over 21. Your Hand {player_hand}. Final score {sum(player_hand)}\n")
                replay_game()
        else:
            print(f"This is your current hand {player_hand}. Total score {sum(player_hand)}")
            print(f"Dealer Hand is {dealer_hand}")
            gameplay(player_hand=player_hand, dealer_hand=dealer_hand)

    elif (user_input.lower() == "stand") or (user_input.lower() == "s") or (user_input.lower() == "'"):
        print(f"Player chose \"{user_input}\" == STAND")
        dealer_win_condition(player_hand=player_hand, dealer_hand=dealer_hand)
    else:
        print("redo input...")
        gameplay(player_hand=player_hand, dealer_hand=dealer_hand)

# dealer playing the game
def dealer_win_condition(player_hand, dealer_hand):
    # dealer must keep hitting until it meets any end condition
    running = True
    while running:
        if (sum(dealer_hand) < 17):
            dealer_hand.append(random.choice(cards))
            print(f"Your Hand {player_hand}. Player score {sum(player_hand)}")
            print(f"Dealer Hand {dealer_hand}. Dealer score {sum(dealer_hand)}\n")
        
        # converting dealer ace from 11 into 1 to keep him in the game
        elif (sum(dealer_hand) > blackjack) and (11 in dealer_hand):
            dealer_hand = replace_ace(dealer_hand, 11, 1)
            print(f"dealer hand ace has now been converted into an 1 to stay in the game.\n")

        # dealer bust
        elif (sum(dealer_hand) > blackjack) and (11 not in dealer_hand):
            running = False
            print(f"Dealer Hand Busted. You Win. Dealer went over 21 and Your Hand is still VALID.\n")
            replay_game()

        # checking to see which hand is greater for the game to end
        elif (sum(dealer_hand) >= 17) or (sum(dealer_hand) <= blackjack):
            running = False
            if (sum(dealer_hand) == blackjack) and (sum(player_hand) < blackjack):
                print(f"Dealer has drawn BLACKJACK. You Lose.\n")
                replay_game()
            elif sum(player_hand) > sum(dealer_hand):
                print(f"Player Hand is Greater. You Win.\n")
                replay_game()
            elif sum(player_hand) < sum(dealer_hand):
                print(f"Dealer Hand is Greater. You Lose.\n")
                replay_game()
            elif sum(player_hand) == sum(dealer_hand):
                print(f"DRAW GAME.\n")
                replay_game()
        
# checking to see if the player wants to play another game
def replay_game():
    another_game = input("Do you want to play another game? (Y/N): ")
    if (another_game.upper() == "Y") or (another_game.upper() == "YES") or (another_game.upper() == ";"):
        playgame(player_hand=[], dealer_hand=[])
    else:
        print("GAME OVER\n\t\t\t\t\t---End of Program---")

# starting a new game
def playgame(player_hand=[], dealer_hand=[]):
    print("\n...New game...")

    # shuffling and dealing player hand
    player_hand.append(random.choice(cards))
    player_hand.append(random.choice(cards))

    # shuffling and dealing dealer hand
    dealer_hand.append(random.choice(cards))

    # if player draws two aces at once
    player_hand = replace_ace(player_hand, 11, 1)
    print("Player has drawn two aces. One has been converted into one. Read Note for more details.")

    print(f"This is your current hand {player_hand}. Total score {sum(player_hand)}")
    print(f"This is the dealer hand {dealer_hand}")

    # if ace has been drawn
    if (sum(dealer_hand) == 11) or (11 in player_hand):
        print("\nNOTE: Ace has drawn. It can either have a value of 1 or 11.")
        print("Ace can be either value is higher for your hand or the value that keeps you in the game.\n")
        
    gameplay(player_hand=player_hand, dealer_hand=dealer_hand)

# making sure that the program is inititated from the correct tab
if __name__ == "__main__":
    playgame()
