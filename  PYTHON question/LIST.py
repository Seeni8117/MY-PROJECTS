'''
list1=[1,3,4]
list2=[3,0,0]
list3=[]
for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(list3)


#sum,mul,max,min of given list 1,2,3,4

sum1=[6,23,4,80,]
sum=0
for i in sum1:
    sum=sum+i
    mul=sum*i
    larg=max(sum1)
    smal=min(sum1)
print("The total sum of given list:",sum)
print("The total multeplecation of given list:",mul)
print("The largest value is:",larg)
print("The smalest value is:",smal)
'''
import itertools
import random

'''
#5
list=["abc","xyz","aba","1221"]
count=0
print("The first and last charecter same:")

for i in list:
    if len(i) > 1 and i[0] == i[-1]:
        count = count + 1
        print(i)
print("Number of strings are:",count)
'''
'''
#6
list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def sortbysec(element):
    return element[1]
list.sort(key=sortbysec)
print(list)
'''
'''
#7
list1=[1,3,4,2,5,6,7,10,10,81,1,1,2]
result=[]
for i in list1:
    if i not in result:
        result.append(i)
print(result)
'''
'''
#8
list=[]
if not list:
    print("list is Epety")
else:
    print("List is Filled")
'''
'''
#9
orlist=[[100,"hello",3,4],1,3,44,22,67]
copy_list=list(orlist)
copy_list[0][2]="sathish"
copy_list[-1]="apple"
print(copy_list)
print(orlist)
'''
'''
#10
list1=[1,5,6,3,8,100,9]
list2=[88,10,12,15,17,20,100]
for x in list1:
    for y in list2:
        if x&y:
            print("True")
        else:
            print("False")
'''
'''
#12
list=['Red','Green','White','Black','Pick','yellow']
list=[x for (i,x) in enumerate(list) if i not in (0,4,5)]
print(list)
'''
'''
#13
array=[[['*' for col in range(6)]for col in range(4)]for row in range(3)]
print(array)
'''
'''
#14
num=[1,2,3,5,6,10,17,19,13,66]
#num=[x for x in num if x%2!=0]
#print(num)
for i in list:
    if i%2!=0:
        print(i)
'''
'''
#15
from random import shuffle
num=['dog','cat','gote','gost','line','lapede','crow']
shuffle(num)
print(num)
'''
'''
#16
list=[]
for i in range(1,31):
    list.append(i**2)
print(list[:6])
print(list[-6:])
'''
'''
#17
list=[]
for i in range(1,31):
    list.append(i**2)
print(list[:6])
'''
'''
#18
import itertools
print(list(itertools.permutations([1,2,3])))
'''
'''
#19
list1=[1,2,5,3,10,19,6,22]
list2=[1,2,10,65,45,3,77,100]
diff_list1_list2=list(set(list1)-set(list2))
diff_list2_list1=list(set(list1)-set(list2))
total_diff=diff_list1_list2+diff_list2_list1
print(total_diff)
'''
'''
#20
list1=[1,2,9,'sathish',10,30,'seeni']
for list1_index,list1_val in enumerate(list1):
    print(list1_index,list1_val)
'''
'''
#21
s=['s','a','t','h','i','s','h']
str1=''.join(s)
print(str1)
'''
'''
#22
list=['apple',1,4,5,0,10]
print(list.index(10))
'''
'''
#23
import itertools
list1=[['dog','cat'],[12],[3,5,12],['fish',100,99,4]]
list2=list(itertools.chain(*list1))
print(list2)
'''
'''
#24
list1=['apple',1,4,5,0,10]
list2=[['dog','cat'],[12],[3,5,12],['fish',100,99,4]]
list2.append(1000)
print(list2)
'''
'''
#25
import random
animal_list=['dog','cat','lion','tiger','fish']
print(random.choice(animal_list))
'''
#26

def student():
    print("my name is seenivasan")
    print(" i good")
student()
