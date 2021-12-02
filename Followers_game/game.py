import random
from art import logo, vs
from game_data import data

print(logo)
print("Welcome to the higher-lower game!")

N_WINS = 0
Afollowers = 0
Bfollowers = 0
correct_answer = " "
A = " "
B = " "
gameplay = True
repeat_game = True

def selection():
    global A
    global B
    A = random.choice(data)
    print(A['name'], ", a " + A['description'] + " from " + A['country'])
    Afollowers = A['follower_count']
    data.remove(A)
    print(vs)
    B = random.choice(data)
    print(B['name'], ", a " + B['description'] + " from " + B['country'])
    Bfollowers = B['follower_count']
    return A
    return B
    return Afollowers
    return Bfollowers

def select_answer():
    global correct_answer
    global Afollowers
    global Bfollowers

    if Afollowers > Bfollowers:
        correct_answer = "a"
    else:
        correct_answer = "b"
    return correct_answer

def substitute():
    global A
    global B
    global Afollowers
    global Bfollowers
    data.append(A)
    A = B
    data.remove(B)
    B = random.choice(data)
    print(A['name'], ", a " + A['description'] + " from " + A['country'])
    Afollowers = A['follower_count']
    print(vs)
    print(B['name'], ", a " + B['description'] + " from " + B['country'])
    Bfollowers = B['follower_count']

def game():
    global gameplay
    global N_WINS

    while gameplay:

        select_answer()

        choice = input("Who has the highest number of followers? A or B?  ").lower()

        if choice == correct_answer:
            N_WINS = N_WINS + 1
            print("correct!")
            print(N_WINS)
            substitute()
        else:
            print("you lose")
            print("Final score:", N_WINS)
            N_WINS = 0
            gameplay = False

selection()

game()

while repeat_game:
    play_again = input("Wanna play another game? Y or N   ").lower()

    if play_again == "y":
        gameplay = True
        substitute()
        game()
    else:
        print("Goodbye!")
        repeat_game = False
