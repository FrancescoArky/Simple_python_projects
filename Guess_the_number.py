from random import randint

def starting_func():

    game_start = input("Welcome to the number guessing game! Wanna play? Y or N    ").lower()
    while True:
        if game_start == "y":
            play_game() #I would also like to ask why it is possible to call this function even though play_game is a completely separate function
            break
        elif game_start == "n":
            print("goodbye!")
            break
        else:
            print("enter a valid input")

def select_diff():
    difficulty = input("Select a difficulty, easy or hard     ").lower()
    while True:
        if difficulty == "easy":
            n_lives = 10
            return n_lives
            break
        elif difficulty == "hard":
            n_lives = 5
            return n_lives
            break
        else:
            print("please select a difficulty")

def play_game():
    secret_number = randint(1, 100) #random number between 1 and 100
    print(secret_number) #check if the code works
        
    n_lives = select_diff()
    print(n_lives) #prints the number of lives
    gameplay = True
        
    while gameplay is True:
        try:
            input_number = int(input("Please choose a number   "))
        except:
            print("Please choose a valid number") #If the input is not a valid INT value, this "except" catch the error correctly

        if input_number < 1 or input_number > 100:
            print("Please choose a valid number") #for numbers out of range
        elif input_number < secret_number:
            n_lives = n_lives - 1 # ERROR: n_lives is not defined
            print(n_lives)
            print("Your number is too low!")
        elif input_number > secret_number:
                n_lives = n_lives - 1
                print(n_lives)
                print("Your number is too high!")
        elif input_number==secret_number:
            print("You won!") #the remaining case is when the guessed number is correct
            gameplay = False
                
        if n_lives == 0:
            print("You lost!")
            gameplay = False
            starting_func()
        else:
            gameplay = True        

if __name__ == '__main__':
    starting_func()
