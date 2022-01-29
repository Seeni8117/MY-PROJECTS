class Computer():
    def __init__(self,windo,memory,fan):
        self.windo=windo
        self.memory=memory
        self.fan=fan
    def comIntro(self):
        print("compurt cpu",self.windo,"any thing ",self.memory,"cool the computer",self.fan)

class Destop(Computer):
    def __init__(self,windo,memory,fan,moniter):
        super().__init__(windo,memory,fan)
        self.moniter=moniter
    def comIntro(self):
        print("compurt cpu",self.windo,"any thing ",self.memory,"cool the computer",self.fan,"seeing to moniter",self.moniter)

class Laptop(Computer):
    def __init__(self,windo,memory,fan,fold):
        super().__init__(windo,memory,fan)
        self.fold=fold
    def comIntro(self):
        print("compurt cpu",self.windo,"any thing ",self.memory,"cool the computer",self.fan,"pik every place",self.fold)
destop=Destop("win10","stored","cooleing the destop","seeing")
laptop=Laptop("win8","stored","cooleing laptop","pik every place")
destop.comIntro()
laptop.comIntro()