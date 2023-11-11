import random

chances = 5
print("Welcome to a guessing game personally designed by Ife.py")
play_again = ""
while play_again.lower() != "no":
    game_complexity = input(
        "what level do you wanna play EASY,MEDIUM or HARD\n"
    ).lower()
    while chances > 0:
        chances -= 1

        guess_start = 0
        guess_end = 0

        if game_complexity == "easy":
            guess_end = 20
        elif game_complexity == "medium":
            guess_end = 50
        elif game_complexity == "hard":
            guess_end = 70

        print(f"you have to guess numbers from range {guess_start} to {guess_end}")
        computer_res = random.randrange(guess_start, guess_end)
        prompt = int(input("try and guess a number\n "))
        if prompt != computer_res:
            print("you've guessed wrong")
            print(f"correct answer is {computer_res}")
            print(f"you have {chances} of trials left")

        elif prompt == computer_res:
            print("you guessed correctly")
            play_again = input("Do you want to continue playing/n")
            if play_again == "yes":
                chances = 5
            elif play_again == "no":
                break

        if chances == 0:
            play_again = input("Do you want to continue playing/n")
            if play_again == "yes":
                chances=5