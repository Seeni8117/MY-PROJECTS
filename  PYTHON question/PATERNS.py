#1
for i in range(5):
    for j in range(i):
        print("*",end="")
    print()


#2
for i in range(3-1):
    for j in range(i,3):
        print("",end="")

    for j in range(i):
        print("*",end="")

    for j in range(i+1):
        print("*",end="")
    print()
for i in range(3):
    for j in range(i+1):
        print("", end="")
    for j in range(i, 3 - 1):
            print("*", end="")

    for j in range(i,3):
            print("*", end="")
    print()
#3
for i in range(5):
    for j in range(i,5-1):
        print(j%2,end="")
    #for j in range(i,9-1):
        #print(j % 2, end="")
    #for j in range(i,5):
        #print(j % 2, end="")
    print()
