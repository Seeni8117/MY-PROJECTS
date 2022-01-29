'''
file=open("filename_with.txt",'w')
file.write("i am in python classS")
file.close()
'''
'''
file=open("filename_Name.txt",'a')
file.write("i am in java classS \n")
file.close()
'''
'''
file=open("filename_Name.txt",'r')
#file.write("i am in java classS \n")
print(type(file))
for ch in file:
    print(ch)
'''
'''
file=open("filename_Name.txt",'r')
print(file.read())
'''
'''
file=open("filename_with.txt",'r+')
file.write("hello,seeni")
file.flush()
file.seek(0)
print(file.read())
'''
'''
file=open("filename_with.txt",'r')
#file.write("hello,seeni")

#print(file.read())
print(file.readlines())
'''
from zipfile import ZipFile
file="C:\Program Files\Python39\python.exe"
with ZipFile("f.zip",'w') as Z:
    Z.write(file)




