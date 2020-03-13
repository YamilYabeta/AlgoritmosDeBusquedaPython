import queue
class BusquedaAnchura():

    def Profundidad(self,root,goal):
        nodo=root
        if nodo.value==goal:
            return "se encontro en: "+nodo.value
        explorando = queue.Queue()
        explorando.put(nodo)
        explorado=[]
        while True:
            if explorando.empty():
                return "No se encontro"
            nodo = explorando.get()
            print("explorando nodo:"+nodo.value)
            for n in nodo.nexts:
                if not n in explorado:
                    print("verificando nodo:"+n.value)
                    if n.value==goal:
                        return "encontrado"
                    explorando.put(n)
            explorado.append(nodo)

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

prof=BusquedaAnchura()

print(prof.Profundidad(n3,'6'))