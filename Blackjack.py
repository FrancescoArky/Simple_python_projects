import random
from replit import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        print("blackjack!")
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(computer_score, user_score):
    if user_score > 21 and computer_score > 21:
        return "Above 21. You lose"


    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "Above 21. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    print("user cards", user_cards)
    print("house cards:", ["x"] + computer_cards[1:])

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 21 or user_score > 21:
            print(user_score)
            print("game over!")
            is_game_over = True
        else:
            user_should_deal = input("Another card? Y or N    ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
                print(user_cards)
            else:
                is_game_over = True
                
    while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(computer_score, user_score))

if input("Wanna play? Y or N").lower() == "y":
    clear()
    play_game()
    
