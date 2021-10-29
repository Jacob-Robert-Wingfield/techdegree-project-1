import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    answer = random.randrange(1, 10)
    player_guess = 0
    attempts = 0
    while player_guess == 0:
        attempts += 1
        try:
            player_guess = int(input("Pick a number between 1 and 10: "))
        except ValueError:
            print("Type a number")

    while player_guess != answer:
        attempts += 1
        if player_guess > answer:
            try:
                player_guess = int(input("It is lower, try again:  "))
            except ValueError:
                print("Type a number")
        if player_guess < answer:
            try:
                player_guess = int(input("It is higher, try again:  "))
            except ValueError:
                print("Try a number")
    if player_guess == answer:
        print("You got it! It took you {} attempts. \nClosing game, see you next time!".format(attempts))


start_game()
