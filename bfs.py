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

def findElement(element):
    x = 0
    y = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == element:
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
    x,y = findElement("5")
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
    costoAcumulado = 0
    #ciervo = false
    cola = queue.PriorityQueue()
    visitados = list()
    makemapa()
    x,y = findElement("5")
    hijos = list()
    cola.put((0,[x,y]))
    xv,yv = findElement("3")
    tuplaCiervo =[xv,yv]
    while cola is not cola.empty():
        expandL = list(cola.get())
        expand = expandL[1]
        costoAcumulado = expandL[0]
        colaDibujo.append(expand)
        visitados.append(expand)
        if int(mapa[expand[0]][expand[1]]) == 4: # es meta?
            #print(expand[0]," ",expand[1])
            break
        if int(mapa[expand[0]][expand[1]]) == 3:
            refactorMapa()
        hijos = hijosNodo([expand[0],expand[1]]) # creo los hijos
        if len(hijos) != 0:
            for i in range(len(hijos)):
                if hijos[i] not in visitados: #no me devuelvo
                    tupla = hijos[i]
                    if int(mapa[tupla[0]][tupla[1]]) == 4 :
                        cola.put((1+costoAcumulado,hijos[i]))
                    if int(mapa[tupla[0]][tupla[1]]) == 3 :
                        #ciervo = 1
                        cola.put((1+costoAcumulado,hijos[i]))
                    if int(mapa[tupla[0]][tupla[1]]) != 0 and int(mapa[tupla[0]][tupla[1]]) != 3 and int(mapa[tupla[0]][tupla[1]]) != 4 : # no deberia mirar muros xd
                        cola.put((int(mapa[tupla[0]][tupla[1]])+costoAcumulado,hijos[i])) #hijos en cola
def profundidadIterativa():
    cola = deque()
    hijos = list()
    makemapa()
    x,y = findElement("5")
    cola.append([x,y])
    visitados = list()
    profundidad = -1
    find = 0
    while not find:
        profundidad +=1
        profAux = profundidad
        while len(cola) != 0 and profAux >= 0:
            expand = cola.popleft()
            visitados.append(expand)
            if int(mapa[expand[0]][expand[1]]) == 4: # es meta?
                #print(expand[0]," ",expand[1])
                find = 1
                break
            hijos = hijosNodo([expand[0],expand[1]]) # creo los hijos
            #print(len(hijos))
            for i in range(len(hijos)):
                if hijos[i] not in visitados: #no me devuelvo
                    tupla = hijos[i]
                    if int(mapa[tupla[0]][tupla[1]]) != 0: # no deberia mirar muros xd
                        cola.append(hijos[i]) #hijos en cola
            profAux -=1
            #print(1)
        print(cola)
        cola = deque()
        cola.append([x,y])

        visitados = list()
    print(profundidad)


profundidadIterativa()
