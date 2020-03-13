from Node import Nodo
from path import Path

ns=Nodo('s')
na=Nodo('a')
nb=Nodo('b')
nc=Nodo('c')
nd=Nodo('d')
ne=Nodo('e')
ng=Nodo('g')


p1=Path(ns,na,1)
ns.paths.append(p1)
print(len(ns.paths))
p2=Path(na,nb,1)
na.paths.append(p2)
print(len(ns.paths))
p3=Path(na,nd,3)
na.paths.append(p3)
print(len(ns.paths))
p4=Path(na,ne,8)
na.paths.append(p4)
print(len(ns.paths))
p5=Path(nb,nc,1)
nb.paths.append(p5)
print(len(ns.paths))
p6=Path(nd,ng,2)
nd.paths.append(p6)
print(len(ns.paths))
p7=Path(ne,nd,1)
ne.paths.append(p7)
print(len(ns.paths))

print(list(ns.paths))
for p in ns.paths:
    print(p.stri())
'''
def prDntG(root,explore):
    expl=explore
    print(root.value)
    if(root.paths):
       
        for p in root.paths:
            if not p in expl:
                expl.append(p)
                print(root.value+'-'+str(p.distance)+'-')
                printG(p.nodoI,expl)'''


def Coast(root,goal,explore):
    expl=[]
    expl=explore
    print("Explorando nodo: "+str(root.value))
    if root.value==goal:
        return True
    expl.append(root)
    if(root.paths):
        sorted(root.paths, key=lambda x:x.distance)
        for p in root.paths:
            print(str(p.nodoI.value))
            '''
        for p in root.paths:
            if not p.nodoI in expl:
                Coast(p.nodoI,goal,expl)
        return False'''

