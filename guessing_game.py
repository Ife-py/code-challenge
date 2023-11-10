import random
#Guesssing game in python

count=5
prompt=""
print("Welcome to a guessing game personally designed by Ife.py")
print("To stop guessing press exit to stop")
outer_counter=1
play_again=''
#outer loop if you wanna play again
while play_again!="no" and outer_counter <= 5:
    game_complexity=input("what level do you wanna play EASY,MEDIUM or HARD\n").lower()
    #inner loop for amount of trials 
    while prompt != "exit" or count <= 5 > 0:
        count -= 1
        #game complexity
        if game_complexity=="easy":
            print("you have to guess numbers from range 0 to 20")
            f=random.randrange(0,20)
            prompt= int(input("try and guess a number\n "))
            if prompt!=f:
                print(f"you have {count} number of trials left ")
                print("you've guessed wrong")
        
                if count == 0:
                    break

            elif prompt== f:
                print("you guessed correctly")
                break
            print(f"correct answer is {f}")
        elif game_complexity=="medium":
            print("you have to guess numbers from range 0 to 50")
            g=random.randrange(0,50)
            while prompt!="exit" and count<=5>0:
                count -= 1
                if prompt!=g:
                    prompt= int(input("try and guess a number\n "))
                    print("you've guessed wrong")
                    print(f"you have {count} number of trials left ")
        
                    if count == 0:
                        break

                elif prompt== g:
                    print("you guessed correctly")
                    break            
                print(f"correct answer is {g}")
        elif game_complexity=="hard":
            print("you have to guess numbers from range 0 to 70")
            h=random.randrange(0,70)
            while prompt!="exit" and count<=5>0:
                count -= 1
                if prompt!=h:
                    prompt= int(input("try and guess a number\n "))
                    print(f"you have {count} number of trials left ")
                    print("you've guessed wrong")
        
                    if count == 0:
                        break
                elif prompt== h:
                    print("you guessed correctly")
                    break
            print(f"correct answer is {h}") 
    play_again=input("do you want to play again Yes or No\n").lower()
    #input to checki if one wants to play again
    if play_again!="yes":
        game_complexity=input("what level do you wanna play\n").lower()
        break
print("Thanks for playing randoguess by 'Ife.py'")
