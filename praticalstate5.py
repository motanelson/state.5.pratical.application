class state5:
    def __init__(self,fire):
        self.fire=int(float(float(fire)/20.00))
        #print("<"+str(self.fire))
        if self.fire>4:
            self.fire=4
    
    def lost(self):
            self.fire=self.fire-1
            if self.fire<1:
               self.fire=0

    def win(self):
            self.fire=self.fire+1
            if self.fire>4:
               self.fire=4


    def report(self):
        #print(">"+str(self.fire))
        print("fire : "+str(int(self.fire * 20.00))+" % ")


a=state5(20)
for b in range(5):
    a.report()
    a.win()
