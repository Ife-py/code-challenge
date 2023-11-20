
#from file2 import decimal_to_binary


sum_of_even=0
sum_of_odd=0


user_choice=input("do you want to calcuate sum of even or odd numbers\n").lower()
user_desired_end=int(input("enter the end number you wanna calculate to\n"))

for i in range (0,user_desired_end+1):
    #print(i)
    if user_choice=='even':
        if i % 2==0:
            sum_of_even+=i                
    elif user_choice=='odd':
        if i%2 !=0:
            sum_of_odd+=i

if user_choice == 'even':
    print(f'the sum of all odd numbers from 1 to {user_desired_end} is {sum_of_even}')
if user_choice == 'odd':
    print(f'the sum of all odd numbers from 1 to {user_desired_end} is {sum_of_odd}')


#g = decimal_to_binary()