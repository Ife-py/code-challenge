a= input("enter the plate number\n")
b=a.split()
f=[]
if len(a)>=2 and len(a)<=6:
    print("its valid")
    print('first check complete')
else:
    print("invalid plate number")
    print('first check complete')
for i in a:
    print(i)
    f.append(i)
    print(f)
    if f[0] or f[1].isdigit():
        #print(type(f[0]))
#q=(type(f[0]))
#j=(type(f[1]))
#if q  and j !=str:
        print("error")
        print("second check complete")
    else:
        print("you passed this check round")
        print("second check complete")
    
"""if f[0]==0:
    print("error")
    print("third check complete")
else:
    print("pass")"""