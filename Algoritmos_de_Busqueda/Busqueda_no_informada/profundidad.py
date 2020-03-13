import queue
class BusquedaProfundidad():

    def Profundidad(self,root,goal,exp):
        nodo = root
        explorados=[]
        explorados=exp
        print("revisando nodo:"+nodo.value)
        if nodo.value==goal:
            print("encontrado nodo: "+nodo.value)
            return True
        explorados.append(nodo)
        print("explorando nodo: "+nodo.value)
        for n in nodo.nexts:
            if not n in explorados:
                if self.Profundidad(n,goal,explorados):
                    return "encontrado"

       
       
class Grafo():
    value =''
    nexts = []
    def __init__(self,val):
        self.value=val

n1 = Grafo('1')
n2 = Grafo('2')
n3 = Grafo('3')
n4 = Grafo('4')
n5 = Grafo('5')
n6 = Grafo('6')

n1.nexts= [n2,n5]
n2.nexts= [n1,n5,n4,n3]
n3.nexts= [n2,n4]
n4.nexts = [n2,n3,n5]
n5.nexts= [n1,n2,n4,n6]
n6.nexts =[n6]

prof=BusquedaProfundidad()

print(prof.Profundidad(n1,'6',[]))