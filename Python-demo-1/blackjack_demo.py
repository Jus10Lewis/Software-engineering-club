import random

def calculate_score(hand):
    """Calculates the score of a hand of cards."""
    # Number cards are their value, face cards are 10, Ace is 11 (initially)
    score = 0
    aces = 0
    
    for card in hand:
        if card in ['J', 'Q', 'K']:
            score += 10
        elif card == 'A':
            aces += 1
            score += 11
        else:
            score += card
            
    # If the score is over 21 and we have an Ace, count the Ace as 1 instead of 11
    while score > 21 and aces > 0:
        score -= 10
        aces -= 1
        
    return score


# Define the deck
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
random.shuffle(cards)

# Deal initial hands
player_hand = [cards.pop(), cards.pop()]
dealer_hand = [cards.pop(), cards.pop()]

game_over = False

print("--- Welcome to Terminal Blackjack! ---")

while not game_over:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    
    print(f"\nYour hand: {player_hand} (Current Score: {player_score})")
    print(f"Dealer's first card: {dealer_hand[0]}")
    
    if player_score == 21:
        print("Blackjack! You win!")
        break
    elif player_score > 21:
        print("Bust! You lose.")
        break
        
    # Player Choice
    action = input("Type 'h' to Hit, 's' to Stand: ").lower()
    
    if action == 'h':
        player_hand.append(cards.pop())
    else:
        game_over = True
        
# Only run dealer's turn and final results if player hasn't already won or busted
if player_score < 21:
    # Dealer's Turn (Dealer hits until score is 17 or higher)
    print(f"\nDealer's final hand: {dealer_hand} (Score: {dealer_score})")
    while calculate_score(dealer_hand) < 17:
        print("Dealer hits...")
        dealer_hand.append(cards.pop())
        dealer_score = calculate_score(dealer_hand)
        print(f"Dealer's hand: {dealer_hand} (Score: {dealer_score})")
        
    # Final Results
    player_score = calculate_score(player_hand)

    if dealer_score > 21:
        print("Dealer busts! You win!")
    elif player_score > dealer_score:
        print(f"You win with {player_score} vs {dealer_score}!")
    elif player_score < dealer_score:
        print(f"Dealer wins with {dealer_score} vs {player_score}!")
    else:
        print(f"It's a push (tie) at {player_score}!")

