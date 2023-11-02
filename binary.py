b= int(input("enter number to be converted to decimal\n"))
final = ""

while b > 0:
    reminder = b % 2
    u = str(reminder)
    final=u+final
    b =b //2
print(f"The conversion of {b} to a binary is {final}")