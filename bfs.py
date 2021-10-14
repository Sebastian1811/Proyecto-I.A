from collections import deque
cola = deque()
mapa= list()

def makematriz():
    a= [0]*5
    for i in range(4):
        mapa.append(a)

def bfs():
    visitados = list()
    makematriz()
    cola.append(mapa[0][0])
    visitados.append([0,0])
    while  len(cola) != 0:
        a = cola.popleft()
        j=0
        print(a)
        for i in range(len(mapa)):
            nodo =[i,j]
            if i == 0 or j== 0 :
                nodo = [i,j+1]
                if nodo not in visitados:
                    visitados.append(nodo)
                nodo = [i+1,j]
                if nodo not in visitados:
                    visitados.append(nodo)
            if i==len(mapa) or j==len(mapa):
                nodo = [i,j+1]
                if nodo not in visitados:
                    visitados.append(nodo)
                nodo = [i+1,j]
                if nodo not in visitados:
                    visitados.append(nodo) 
            if nodo not in visitados:

        j += 1
bfs()
