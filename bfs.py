from collections import deque
import txt
import queue
import nodo

path = list()
arbol = list()
visitados = list()

def makemapa():
    fila = ''
    count = 0
    mapa= list()
    mapaString=''
    mapaString = txt.leerTxt('mapa.txt')
    for i in range(len(mapaString)):
        if mapaString[i] == "\n":
            mapa.append(list(fila))
            fila=''
            count+=1
        if mapaString[i] != "\n" and mapaString[i] !=" ":
            fila += mapaString[i]
    return mapa

def findPadre(tupla,lista):
    for i in lista:
        if i[1] == tupla:
            return lista.index(i)

def findBranch(lista,meta):
    branch = 0
    for i in lista:
        if i[2] and meta == i[1]:
            branch = i
    return branch

def findPath(nodo):
    global path
    if nodo[0] == []:
        path.append(nodo[1])
        return 1
    elif nodo[2]:
        path.append(nodo[1])
        findPath(nodo[0])

def findElement(element,mapa):
    x = 0
    y = 0
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == element:
                x = i
                y = j
    return x,y

def hijosNodo(nodo,mapa):
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

def refactorMapa():
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            if mapa[i][j] == "2":
                mapa[i][j] = "1"
def bfs(mapa):
    global arbol
    cola = deque()
    visitados = list()
    nodos = list()
    #makemapa()
    x,y = findElement("5",mapa)
    hijos =list()
    cola.append([x,y])
    Nodo = nodo.Nodo(list(),[x,y],0)
    nodos.append(Nodo.makenodo())
    while len(cola) != 0:
        expand = cola.popleft()
        visitados.append(expand)
        nodos[findPadre(expand,nodos)][2] = 1
        if int(mapa[expand[0]][expand[1]]) == 4: # es meta?
            break
        hijos = hijosNodo([expand[0],expand[1]],mapa) # creo los hijos
        for i in range(len(hijos)):
            if hijos[i] not in visitados: #no me devuelvo
                tupla = hijos[i]
                if int(mapa[tupla[0]][tupla[1]]) != 0: # no deberia mirar muros xd
                    cola.append(hijos[i]) #hijos en cola
                    arbol_ = nodo.Nodo(nodos[len(nodos)-1],hijos[i],0)
                    arbol.append(arbol_.makenodo())
                    nodo_ = nodo.Nodo(nodos[findPadre(expand,nodos)],hijos[i],0)
                    nodos.append(nodo_.makenodo())
    return nodos

def costoUniforme(mapa):
    costoAcumulado = 0
    cola = queue.PriorityQueue()
    visitados = list()
    nodos = list()
    x,y = findElement("5",mapa)
    hijos = list()
    cola.put((0,[x,y]))
    Nodo = nodo.Nodo(list(),[x,y],0)
    nodos.append(Nodo.makenodo())
    while cola is not cola.empty():
        expandL = list(cola.get())
        expand = expandL[1]
        costoAcumulado = expandL[0]
        visitados.append(expand)
        nodos[findPadre(expand,nodos)][2] = 1
        if int(mapa[expand[0]][expand[1]]) == 4: # es meta?
            break
        hijos = hijosNodo([expand[0],expand[1]],mapa) # creo los hijos
        if len(hijos) != 0:
            for i in range(len(hijos)):
                if hijos[i] not in visitados: #no me devuelvo
                    tupla = hijos[i]
                    if int(mapa[tupla[0]][tupla[1]]) == 4 :
                        cola.put((1+expandL[0],hijos[i]))
                        arbol_ = nodo.Nodo(nodos[len(nodos)-1],hijos[i],0)
                        arbol.append(arbol_.makenodo())
                        nodo_ = nodo.Nodo(nodos[findPadre(expand,nodos)],hijos[i],0)
                        nodos.append(nodo_.makenodo())
                    if int(mapa[tupla[0]][tupla[1]]) == 3 :
                        cola.put((1+expandL[0],hijos[i]))
                        arbol_ = nodo.Nodo(nodos[len(nodos)-1],hijos[i],0)
                        arbol.append(arbol_.makenodo())
                        nodo_ = nodo.Nodo(nodos[findPadre(expand,nodos)],hijos[i],0)
                        nodos.append(nodo_.makenodo())
                    if int(mapa[tupla[0]][tupla[1]]) != 0 and int(mapa[tupla[0]][tupla[1]]) != 3 and int(mapa[tupla[0]][tupla[1]]) != 4 : # no deberia mirar muros xd
                        cola.put((int(mapa[tupla[0]][tupla[1]])+expandL[0],hijos[i])) #hijos en cola
                        arbol_ = nodo.Nodo(nodos[len(nodos)-1],hijos[i],0)
                        arbol.append(arbol_.makenodo())
                        nodo_ = nodo.Nodo(nodos[findPadre(expand,nodos)],hijos[i],0)
                        nodos.append(nodo_.makenodo())
    return nodos

def BPI(raiz,objetivo,mapa):
    profundidad = 0
    global visitados
    while 1:
        resultado = bpl(raiz,objetivo,profundidad,mapa)
        if resultado == objetivo:
            return resultado
        profundidad += 1

def bpl (nodo,objetivo, profundidad,mapa):
    global visitados
    global path
    if profundidad == 0 and nodo == objetivo:
        path.append(nodo)
        return nodo
    elif profundidad > 0:
        hijos = hijosNodo(nodo,mapa)
        visitados.append(nodo)
        for i in hijos:
            if int(mapa[i[0]][i[1]]) != 0:
                resultado = bpl([i[0],i[1]],objetivo,profundidad-1,mapa)
                if resultado != None:
                    path.append(nodo)
                    return resultado
    else:
        return None
def returnPath(algoritmo,mapa):
    global path
    if algoritmo == 1:
        nodos = bfs(mapa)
        x,y = findElement('4',mapa)
        nodoMeta = findBranch(nodos,[x,y])
        findPath(nodoMeta)
        rPath = path
        path = list()
        return list(reversed(rPath))
    if algoritmo == 2:
        nodos = costoUniforme(mapa)
        x,y = findElement('4',mapa)
        nodoMeta = findBranch(nodos,[x,y])
        findPath(nodoMeta)
        rPath = path
        path = list()
        return list(reversed(rPath))
    if algoritmo == 3:
        xprincesa,yprincesa = findElement('5',mapa)
        xllegada, yllegada =findElement('4',mapa)
        BPI([xprincesa,yprincesa],[xllegada, yllegada],mapa)
        rPath = path
        path = list()
        return list(reversed(rPath))

if __name__ == '__main__':

    print(returnPath(2,makemapa()))
