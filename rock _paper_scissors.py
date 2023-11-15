import random
a = ["rock","paper","scissors"]
shuffler=random.choice(a)
#print(shuffler)
play_again=''
count=""
take_input=''
outer_counter=1
count=2
while play_again!="no" or "exit" and outer_counter==5: 
   
    while count<=2>0:
        count-=1
        take_input=input("enter your choice Rock, Paper ,or Scissors\n").lower()
        if take_input== shuffler:
            print("its a tie try again")
            print(f"you have {count} number of trials left")
        elif take_input== "rock" and shuffler=="scissors" :
            print("you won this round correctly")
            break
        elif take_input=="paper" and shuffler=="rock":
            print("you won this round ")
            break
        elif take_input=="scissors" and shuffler=="paper":
            print("you won this round ")
            break
        else:
            print("you lost try again")
            if count==0:
                break
    print(f"computer chose {shuffler} hereby you lost")
    print(f"computer answer is {shuffler} therefore you won")
    play_again=input("do you want to play again yes or no\n").lower()
    if play_again!="yes":
        break
print("thanks for playing")