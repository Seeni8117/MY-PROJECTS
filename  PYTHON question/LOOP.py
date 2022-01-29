'''
#4
#infinety
i=0
while i<=1:
    print('hello')
'''
'''
#7
#sum numbers
num=int(input("Enter the values:"))
result=0
while num>0:
    sum=num%10
    result=result+sum
    num=num//10

print("sum of values are:",result)
'''
'''
#11
#prime num
for i in range(1,100):
    count=0
    for j in range(1,i+1):
        if (i % j == 0):
            count=count+1
    if (count == 2):
        print(i, end=" ")
        '''

'''
#10
#prime facter
n=int(input("Enter the value:"))
a=2
while(n!=1):
    rem=n%a
    if rem==0:
        n=n/a
        print(a)
    else:
        a=a+1
        '''
'''
#15
rev=input("Enter the string:")
for i in range(len(rev)-1,-1,-1):
    print(rev[i],end="")
'''
'''
#8
#Armstrong
for i in range(100,501):
    num=i
    result=0
    n=len(str(i))
    while (i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)
   '''
'''
#18
m1=(int(input("physics mark:")))
m2=(int(input("chemistry mark:")))
m3=(int(input("biology mark:")))
m4=(int(input("mathematics mark:")))
m5=(int(input("computre mark:")))
total=m1+m2+m3+m4+m5
pre=(total/500)*100
print(pre)
if pre>=90:
    print("grade A")
elif pre>=80:
    print("grade B")
elif pre>=70:
    print("grade C")
elif pre>=60:
    print("grade D")
elif pre>=40:
    print("grade E")
else:
    print("FAIL")
'''
'''
#19
num=int(input("Enter the number="))
if num < 0:
    print(-num)
else:
    print(num)
'''

#20
held_classes=int(input("Held classes:"))
attended_classes=int(input("Student coming classes:"))
per=(attended_classes*held_classes)/100
print(per)
if per > 75:
    print("Allowed the exam hall")
else:
    print("Not allowed in exam hall")


'''
#14
num=[]
for i in range(0,601):
    if (i%3==0) and (i%6==0) and (i%13==0):
        num.append(str(i))
print(','.join(num))
'''
'''
#9
#Reversing numbers
list=int(input("Enter the numbers:"))

rev=0
while(list>0):
    rev=(rev*10)+list%10
    list=list//10
print("The reverse numbers are:",rev)
'''
'''
num=[]
for i in range(1500,2701):
    if (i%7==0) and(i*5==0):
        num=''

print(num)
'''
















