class Fighter():

    def __init__(self,name,age,weight,height,style,rank,opponnent):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
        self.style=style
        self.rank=rank
        self.opponnent=opponnent


    def KO(self):
        return "{} knocked out {}".format(self.name,self.opponnent)

class Fights(Fighter):

    def __init__(self,name,age,weight,height,style,rank,last_fight,opponnent):
        self.last_fight=last_fight
        Fighter.__init__(self,name,age,weight,height,style,rank,opponnent)
        




Ciryl = Fights("Ciryl Gane",31,"Heavy","6'4","Kickboxing",94,"L-Francis Ngannou","Rozenstruik")
print(Ciryl.KO())