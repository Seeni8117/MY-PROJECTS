'''
#creates the file it does not exist
file=open("demofile.txt",'w')
file.write("Hello!This is demofile.txt.")
file.write("\nThis is for tasting porpes.")
file.write("\nGood luck!")
file.close()
'''
'''
#read the file
file=open("demofile.txt",'r')
print(file.read())
print(file.readline())#tis will be read for one line
print(file.readline(10))
file.close()
for x in file:
    print(x)
'''
'''
file=open("demofile.txt",'a')
file.write("\nNow the file has more content")
file.close()
'''
'''
with open("demofile2.txt",'w') as file:#we use this method don't mention close() in last
    file.write("Hello!This is demofile.txt.")
    file.write("\nThis is for tasting porpes.")
    file.write("\nGood luck!")
'''
'''
with open("demofile2.txt",'a') as file:
    file.write("Woops! I have deleted the content!")
    file.write("\nAnd i will adding the line")
'''
