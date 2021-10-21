import bfs

class agente:

    percepcion = list()
    actuacion = list()
    posx = 0
    posy = 0
    meta = list()
    movimientosRealizados = 0
    nombre = ''

    def __init__(self,nombre):
        self.nombre = nombre

    def setPercepcion(self):
        self.percepcion = bfs.makemapa()
        self.posx,self.posy = bfs.findElement('5',self.percepcion)
        x,y = bfs.findElement('4',self.percepcion)
        self.meta = [x,y]

    def setActuacion(self,algoritmo):
        self.actuacion = bfs.returnPath(algoritmo,self.percepcion)
        print(self.actuacion)
    def setMovimientos(self):
        self.movimientosRealizados = 0

    def movimiento(self):
        if [self.posx,self.posy] != self.meta and self.movimientosRealizados < len(self.actuacion):
            self.percepcion[self.posx][self.posy] = '1'
            self.posx = self.actuacion[self.movimientosRealizados][0]
            self.posy = self.actuacion[self.movimientosRealizados][1]
            self.percepcion[self.posx][self.posy] = '5'
            self.movimientosRealizados += 1
