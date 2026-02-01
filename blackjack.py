# ===============================
# BLACKJACK GAME - DAY 11
# ===============================
#made by abraham paul sanhith
import random

# -------- CARD DECK --------
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

# -------- DEAL A CARD --------
def deal_card():
    """Returns a random card from the deck"""
    return random.choice(cards)

# -------- CALCULATE SCORE --------
def calculate_score(hand):
    """
    Takes a list of cards and returns the score.
    Blackjack (21 with 2 cards) returns 0.
    Ace (11) becomes 1 if score > 21.
    """
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

# -------- COMPARE SCORES --------
def compare(player_score, computer_score):
    """Compares final scores and returns result"""
    if player_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "You win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over 21. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over 21. You win 😁"
    elif player_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

# -------- MAIN GAME --------
def play_blackjack():
    print("\n🃏 WELCOME TO BLACKJACK 🃏")

    player_cards = []
    computer_cards = []
    game_over = False

    # Deal initial cards
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Player turn
    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)

        print("\nYour cards:", player_cards, "Score:", player_score)
        print("Computer's first card:", computer_cards[0])

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if choice == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    # Computer turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final results
    print("\n========== FINAL RESULT ==========")
    print("Your final hand:", player_cards, "Score:", player_score)
    print("Computer final hand:", computer_cards, "Score:", computer_score)
    print(compare(player_score, computer_score))
    print("=================================\n")

# -------- REPLAY LOOP --------
while True:
    play_blackjack()
    again = input("Do you want to play again? Type 'y' or 'n': ").lower()
    if again != "y":
        print("Thanks for playing Blackjack! 👋")
        break
