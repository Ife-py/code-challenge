import random
#Guesssing game in python
#this line takes in input 
count=""
prompt=""
print("Welcome to a guessing game personally designed by Ife.py")
print("To stop guessing press exit to stop")
game_complexity=input("what level do you wanna play EASY,MEDIUM or HARD\n").lower
outer_counter=1
play_again=''
#i created an outer loop to loop through the inner code for a number of time
while play_again!="no"or"No"or"NO" and outer_counter==5:
    #game complexity for easy
    if game_complexity=="easy":
        print("you have to guess numbers from range 0 to 20")
        f=random.randrange(0,20)
        count=5
        while prompt!="exit" and count<=5>0:
            count -= 1
            if prompt!=f:
                prompt= int(input("try and guess a number\n "))
                print(f"you have {count} number of trials left ")
                print("you've guessed wrong")
        
                if count == 0:
                    break

            elif prompt== f:
                print("you guessed correctly")
                break
        print(f"correct answer is {f}")
        #game complexity for medium
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
        #game complexity for HARD
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
        #OUTPUT TO BE GENERATED
    play_again=input("do you want to play again Yes or No\n").lower
    #while loop if you want to play again
    if play_again=="yes":
        game_complexity=input("what level do you wanna play EASY,MEDIUM or HARD\n")
    elif play_again=="no":
        break
print("Thanks for playing randoguess by 'Ife.py'")
