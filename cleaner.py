import random
prompt=''
print('welcome to guessing game ')
print('To stop playimg press exit to stop') 
starting =0
stop =0
outer_counter=5
def initial(prompt):
    play_again=''
    count=5
    while play_again !="no" and outer_counter<=5:
        game_complexity=input('what level do you wanna play Easy Medium or hard\n').lower()
        while prompt!= "exit" or count<=5>0:
            count -=1
            if game_complexity=="easy":
                stop=20
                print("you have to guess number from range 0 to 20")
            elif game_complexity=="medium":
                stop=50
                print("you have to guess number from range 0 to 50")
            elif game_complexity=="hard":
                stop=70
                print("you have to guess number from range 0 to 70")
            f=random.randrange(starting,stop)
            prompt=int(input("try and guess a number\n"))
            if prompt!=f:
                print(f"you have {count} number of trials left")
                print("you've guessed wrong")
            elif prompt==f:
                print("you guessed correctly")
                if play_again=="yes":
                    count=5
                elif play_again!="yes": 
                    break
            print(f"the correct answer is {f}")
            if count==0:        
                play_again=input("do you wanna play again yes or no\n").lower()
                game_complexity=input('what level do you wanna play Easy Medium or hard\n').lower()
                if play_again=="yes":
                    count==5
    print("Thanks for playing randoguess by ife.py")
initial(prompt)
