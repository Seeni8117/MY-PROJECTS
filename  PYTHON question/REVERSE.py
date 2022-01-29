


check1=["learn","quiz","practic","contriu"]
check2=check1
print(check2 is check1)
check3=check1[:]
print(check3 is check1)
check2[0]="code"
print(check2)
check3[1]="mcq"
print(check3)
count=0
for c in (check1,check2,check3):
    if c[0]=="code":
        count+=1
    if c[1]=="mcq":
        count+=10
    print(count)
