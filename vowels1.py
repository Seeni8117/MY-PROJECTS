'''
list = ["seenivasan","sathish","venu","tamilarasan"]
s = "".join(list)
vowels = "aeiou"
print("The vowels are:")
count = 0
for i in s:
    if i in vowels:
        count=count+1
        print(i,end=" ")

print("\n Total vowels in the given list :",count)
'''

for i in range(0,11):
    if(i== 5):
        print("seeni")
    elif(i==9):
        print("sathish")
    else:
        print(i)



