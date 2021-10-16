class Nodo:
    padre = 0
    valor = 0
    nodoExpand = 0
    def __init__(self,padre,valor,nodoExpand):
        self.padre = padre
        self.valor = valor
        self.nodoExpand = nodoExpand
    def makenodo(self):
        return [self.padre,self.valor,self.nodoExpand]
    def expandido(self):
        self.nodoExpand = 1
