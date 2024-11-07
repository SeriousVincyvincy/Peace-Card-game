import random

# Define the ranks and suits
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "diamonds", "clubs", "spades")
war_pile = []
war_counter = 0
# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]
print(deck)
# Shuffle the deck 
random.shuffle(deck)

# Split the deck into two hands

hand1 = deck[0:26]
hand2 = deck[26:]


def card_comparison(hand1, hand2):

    """This is the logic that compares two cards to find the stronger card
		Return 1 if player 1's card is strong, 2 for player 2
		if the cards are equal, return 0.

		Hint, using the index function will make this very simple (one liner)"""
    # Your code here

    print(f"Player 1 plays {hand1[0]}, Player 2 plays {hand2[0]}")
    
    if ranks.index(hand1[0][0]) == ranks.index(hand2[0][0]):
        print("Time to go to war!")
        war(hand1, hand2, war_counter)
    elif ranks.index(hand1[0][0]) > ranks.index(hand2[0][0]):
        print("Player 1 wins this round!")
        hand1.append(hand2.pop(0))
        hand1.append(hand1.pop(0))
    else:
        print("Player 2 wins this round!")
        hand2.append(hand1.pop(0))
        hand2.append(hand2.pop(0))


def play_round(hand1, hand2):
    """Play a single round of the game.
		That is, each player flips a card, and the winner is determined using the card_comparison function
		if both players flip the same value card, call the war function
	"""
    # Your code here

    input("Press Enter to play the next round...")
    print(len(hand1))
    print(len(hand2))   
    card_comparison(hand1, hand2)
        

def war(hand1, hand2, war_counter):
    """Handle the 'war' scenario when cards are equal.
		recall the rules of war, both players put 3 cards face down, 
		then both players flip face up a 4th card. The player with the stronger
		card takes all the cards.		
	"""
    # Your code here
    global war_pile
    
    if (len(hand1) < 4 or len(hand2) < 4):
        if len(hand1)<4:
            hand1.append(hand2)
            hand2 == 0 
        else:
            hand2.append(hand1)
            hand1 == 0 
    
    else: 
        
        print("Each player place 4 cards!")

        for _ in range(4):
            war_pile.append(hand1.pop(0))
        for _ in range(4):
            war_pile.append(hand2.pop(0))


        card1 = war_pile[-8]
        card2 = war_pile[-4]
        
        print(f"Player 1 has a {card1} going to war!")
        

        print(f"Player 2 has a {card2} going to war!")

        if ranks.index(card1[0]) == ranks.index(card2[0]):
            print(f"It's time for war {war_counter} x!")
            war_counter += 1
            war(hand1, hand2, war_counter)
        
            
        elif ranks.index(card1[0]) > ranks.index(card2[0]):
            print("Player 1 wins the war!")
            hand1 += war_pile
            war_pile = [ ]
            war_counter = 0

        else:
            print("Player 2 wins the war!")
            hand2 += war_pile
            war_pile = [ ]
            war_counter = 0

def play_game():
    """Main function to run the game."""
    # Your code here

    while len(hand1) > 0 and len(hand2) > 0: 
        play_round(hand1, hand2)

    if len(hand1) == 0: 
        print("Player 2 wins the game! Congratulations Player 2!")

    elif len(hand2) == 0:
        print("Player 1 wins the game! Congratulations Player 1!")

# Call the main function to start the game
play_game()
