import random
numberList=[151,251,351,451,551,651,751,851,951]
weight=(10,20,30,40,50,60,70,80,90)
print(random.choices(numberList,weight,k=10))
print (random.random())
random.shuffle(numberList)
print (numberList)
print(random.randint(151,951))
print(random.randrange(151,951))