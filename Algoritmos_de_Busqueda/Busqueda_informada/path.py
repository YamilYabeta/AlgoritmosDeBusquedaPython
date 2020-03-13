class Path():
    def __init__(self,nodoD,nodoI,distance):
        self.nodoD=nodoD
        self.nodoI=nodoI
        self.distance=distance
    def __str__(self):
         return str(self.nodoD.value)+"-"+str(self.distance)+"-"+str(self.nodoI.value)

    def __repr__(self):
        return str(self.nodoD.value)+"-"+str(self.distance)+"-"+str(self.nodoI.value)
    def stri(self):
        return str(self.nodoD.value)+"-"+str(self.distance)+"-"+str(self.nodoI.value)