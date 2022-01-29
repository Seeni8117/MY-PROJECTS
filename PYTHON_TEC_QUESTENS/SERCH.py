def search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    print("not in list")

l=[1,2,3,4,1,0,10]
print(search(l,4))
