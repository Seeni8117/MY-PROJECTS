'''
list=["Apple","Banana","Papaya","Kiwi","Orange","Pin"]
def my():
    for val in list:
        yield val
x=my()
print(x.__next__())
print(x.__next__())
x.__next__()
print(x.__next__())
print(x.__next__())
print(x.__next__())
'''

def range(limit):
    temp=0
    while(temp<limit):
        yield temp
        temp+=1
for i in range(10):
    print(i)






