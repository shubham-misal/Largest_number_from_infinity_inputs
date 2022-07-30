#wap to find the greatest number and take n number of inputs from user.
print("\n=============== < Greatest & Smallest number > =================")
print("\t\t<=== Type q or Q to check ===> ")
print("\nEnter numbers:")
x=[]
while True:
    a=input(">>")
    if(a=="q" or a=="Q"):
        break
    elif(a>="a" and a<="z" or a>="A" and a<="Z"):
        print("\nInvalid input")
        print("Try Again\n")
        x.clear()
        print("Enter numbers:")
    elif(a=="" or a==None):
        print("No input from user")
    else:
        b=int(a)
        x.append(b)
#x = [int(x) for x in input("\nEnter multiple value: \n>>").split()]
largenum=x[0]
smallnum=x[0]
for i in x:
    if(i>largenum):
        largenum=i
    elif(i<smallnum):
        smallnum=i
print("\nGreatest number from:\n>>",x,"==>",largenum)
print("\nSmallest number from:\n>>",x,"==>",smallnum)

