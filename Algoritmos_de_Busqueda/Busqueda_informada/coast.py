import operator
class Nodo():
    paths=dict()
    def __init__(self, value):
        self.value=value


ns=Nodo('s')
na=Nodo('a')
nb=Nodo('b')
nc=Nodo('c')
nd=Nodo('d')
ne=Nodo('e')

ns.paths = {na:1}
na.paths = {ne:8,nd:3,nb:1}
nb.paths = {nc:1}
ne.paths = {nd:1}
s=sorted(na.paths.items(), key=operator.itemgetter(1))
print(s)
print(s[0])
print(s[0][0].paths)
