#out put 10 numbers
n=int(input("Enter the num element:"))
list=[]
sum=0

for i in range(n):
    list.append(int(input()))
for i in list:
    sum=sum+i
    avg=sum/len(list)
print("sum of list is:",sum)
print("sum of avg is",avg)

