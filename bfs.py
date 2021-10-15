from collections import deque
import txt
cola = deque()
mapa= list()
mapaString=''

def makemapa():
    fila = ''
    count = 0
    global mapaString
    mapaString = txt.leerTxt('mapa.txt')
    for i in range(len(mapaString)):
        if mapaString[i] == "\n":
            mapa.append(list(fila))
            #print(fila)
            fila=''
            count+=1
        if mapaString[i] != "\n" and mapaString[i] !=" ":
            fila += mapaString[i]

def hijosNodo(nodo):
    hijos = list()
    if nodo[0]+1 < len(mapa):
        hijos.append([nodo[0]+1,nodo[1]])

    if nodo[1]+1 < len(mapa[0]):
        hijos.append([nodo[0],nodo[1]+1])

    if nodo[0]-1 > 0:
        hijos.append([nodo[0]-1,nodo[1]])

    if nodo[1]-1 > 0:
        hijos.append([nodo[0],nodo[1]-1])

    print(hijos)

def bfs():
    visitados = list()
    makematriz()
    cola.append(mapa[0][0])
    visitados.append([0,0])
    while len(cola) != 0:
        a = cola.popleft()
        j=0
        print(a)
        for i in range(len(mapa)):
            "como todos ven"

#makemapa()
#hijosNodo([0,0])
