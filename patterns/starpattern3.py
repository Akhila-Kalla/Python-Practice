r=5
for i in range(1,r+1):
    for k in range(r-i):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()