b=input("enter a letter\n")
c=[]
for char  in b:
    if char not in c:
        c.append(char)
output=''.join(c)
print(output)  