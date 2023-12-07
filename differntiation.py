"""me attempting to write a code that solves normal differentiation"""
"""variables to use coefficient, unknnown, power, and output"""

print("welcome to trying to slove differentiation of first principle using python")
a=int(input("enter the coefficient of the variable to be differentiated\n"))
b=input("enter the unknown value to be differentiated\n")
c=int(input("enter the power of the coefficient to be used\n"))
f=a*c
g=c-1
new_value=(f"your differentiated figuure is given as {f}{b}**{g}")
print(new_value)