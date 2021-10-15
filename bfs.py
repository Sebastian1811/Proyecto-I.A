from collections import deque
import txt
import queue
cola = deque()
colaDibujo = deque()
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

    if nodo[0]-1 >= 0:
        hijos.append([nodo[0]-1,nodo[1]])

    if nodo[1]-1 >= 0:
        hijos.append([nodo[0],nodo[1]-1])
    return hijos

def findStart():
    x = 0
    y = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "5":
                x = i
                y = j
    return x,y
def refactorMapa():
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "2":
                mapa[i][j] = "1"
def bfs():
    visitados = list()
    makemapa()
    x,y = findStart()
    hijos =list()
    cola.append([x,y])
    while len(cola) != 0:
        expand = cola.popleft()
        colaDibujo.append(expand)
        visitados.append(expand)
        if int(mapa[expand[0]][expand[1]]) == 4: # es meta?
            print(expand[0]," ",expand[1])
            break
        hijos = hijosNodo([expand[0],expand[1]]) # creo los hijos
        for i in range(len(hijos)):
            if hijos[i] not in visitados: #no me devuelvo
                tupla = hijos[i]
                if int(mapa[tupla[0]][tupla[1]]) != 0: # no deberia mirar muros xd
                    cola.append(hijos[i]) #hijos en cola
def costoUniforme():
    cola = queue.PriorityQueue()
    visitados = list()
    makemapa()
    x,y = findStart()
    hijos =list()
    cola.put((0,[x,y]))
    while cola is not cola.empty():
        expandL = list(cola.get())
        expand = expandL[1]
        colaDibujo.append(expand)
        visitados.append(expand)
        if int(mapa[expand[0]][expand[1]]) == 4: # es meta?
            print(expand[0]," ",expand[1])
            break
        if int(mapa[expand[0]][expand[1]]) == 3:
            refactorMapa()
        hijos = hijosNodo([expand[0],expand[1]]) # creo los hijos
        for i in range(len(hijos)):
            if hijos[i] not in visitados: #no me devuelvo
                tupla = hijos[i]
                if int(mapa[tupla[0]][tupla[1]]) != 0 and int(mapa[expand[0]][expand[1]]) == 3:
                    cola.put((0,hijos[i]))
                if int(mapa[tupla[0]][tupla[1]]) != 0: # no deberia mirar muros xd
                    cola.put((int(mapa[tupla[0]][tupla[1]]),hijos[i])) #hijos en cola
        #print(visitados)

#costoUniforme()
