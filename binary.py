#simple cocde to convert decimal to binary
b= int(input("enter number to be converted to binary\n"))
final = ""

while b > 0:
    reminder = b % 2
    u = str(reminder)
    final=u+final
    #floor division of our final re
    b =b //2
print(f"The conversion of {b} to a binary is {final}")
