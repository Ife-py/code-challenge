import random
for i in range(0,101):
    if i%3==0 and i%5==0:
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)