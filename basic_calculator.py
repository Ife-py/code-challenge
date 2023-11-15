numb=float(input("enter number\n"))
operator=input(f"what operator do you want to use.'addition''subtraction''division''multiplucation'\n").lower
numb2=float(input("enter number\n"))
if operator == "addition" or "+":
    print(f"the sum of {numb} and {numb2} is {numb+numb2} ")
elif operator=="subtraction" or "-":
    print(f"the difference between {numb} and {numb2} is {numb-numb2}")
elif operator== "division" or "/":
    print(f"the division of {numb} and {numb2} is {numb/numb2}")
elif operator== "multiplication" or "*":
    print(f"the product of {numb} and {numb2} is {numb*numb2}")