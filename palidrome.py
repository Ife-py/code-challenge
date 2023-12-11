a=input("enter the word to be checked\n")
b=[]
for i in a:
    #print(i)
    b.append(i)
print(b)
c= len(b)
print(c)
if b[0:-1] == b[-1:0]:
    print("this is a palindrome word")
else:
    print('this isnt a palindrome word')