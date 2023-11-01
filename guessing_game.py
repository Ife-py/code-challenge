import random
#Guesssing game in python
count=5
prompt=""
print("Welcome to a guessing game personally designed by Ife.py")
print("To stop guessing press exit to stop")
game_complexity=input("what level do you wanna play EASY,MEDIUM or HARD\n")
if game_complexity=="EASY"or "Easy"or "easy":
    f=random.randrange(0,20)
    while prompt!="exit" and count<=5>0:
        count -= 1
        if prompt!=f:
            prompt= int(input("try and guess a number\n "))
            print(f"you have{count} number of trials left ")
            print("you've guessed wrong")
        
            if count == 0:
                break

        elif prompt== f:
            print("you guessed correctly")
            break
    print(f"correct answer is {f}")
elif game_complexity=="MEDIUM"or "Medium"or "medium":
    g=random.randrange(0,50)
    while prompt!="exit" and count<=5>0:
        count -= 1
        if prompt!=g:
            prompt= int(input("try and guess a number\n "))
            print("you've guessed wrong")
            print(f"you have{count} number of trials left ")
        
            if count == 0:
                break

        elif prompt== g:
            print("you guessed correctly")
            break            
    print(f"correct answer is {g}")
elif game_complexity=="HARD"or"Hard"or"hard":
    h=random.randrange(0,70)
    while prompt!="exit" and count<=5>0:
        count -= 1
        if prompt!=h:
            prompt= int(input("try and guess a number\n "))
            print(f"you have{count} number of trials left ")
            print("you've guessed wrong")
        
            if count == 0:
                break
        elif prompt== h:
            print("you guessed correctly")
            break
    print(f"correct answer is {h}")