no = int(input("enter the number of rows"))

for i in range(no+1):
    for j in range(no-i):
        print(" ",end=" ")

    for k in range(2*i -1):
        print("*",end=" ")

    print()

for l in range(no-1,0,-1):
    for m in range(no-l):
        print(" ",end=" ")

    for n in range(2*l - 1):
        print("*",end= " ")
    print()