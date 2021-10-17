mapa =''
def leerTxt(name):
    veces = returnFilas()
    file = open(name,'r')
    global mapa
    while(veces > 0):
        mapa += file.readline()
        veces -= 1
    file.close()
    mapa_ = mapa
    mapa = ''
    return mapa_

def returnFilas():
    fichero = open('mapa.txt','r')
    fichero.seek(0)
    veces = len(fichero.readlines())
    fichero.close()
    return veces
