'''
#Agefuntion
def voterornot(age):
    if(age>18 and age<100):
        print("yes you can vote")
    else:
        print("no you can not vote")

age = int(input("Enter your age:"))
voterornot(age)
'''

age=int(input("Enter the input:"))
if(age>=18 and age<=100):
    print("yes your elegeble for vote")
if(age>35 and age<55):
    print("yes your elegeble for work")
else:
    print("you are not elegeble ")
'''
age=int(input("Enter the age:"))
if(age>=5 and age<=10):
    print("you studying 1st to 5th")
if(age>=11 and age<=15):
    print("you studying 6th to 10th")
if(age>=16 and age<=18):
    print("you studying 11th to 12th")
if(age>=19 and age<=24):
    print("you studying college")
if(age>=25 and age<=100):
    print("vip")
else:
    print("rip")
'''