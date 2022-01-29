class path():

    def __init__(self,ritepath,wrongpath):
        self.ritepath=ritepath
        self.wrongpath=wrongpath

    def ritepath(self):
        pass
    with open("recorse/msg.txt","r") as file:
        lines=file.read()
        print(lines)
    def wrongpath(self):
        pass
try:
    with open("recorse/msg.txt","r") as file:
        lines=file.read()
        print(lines)
except FileNotFoundError as e:
        print("the given file name is wrong so file not found ",e)



