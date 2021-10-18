import sys, pygame
import time
import bfs
pygame.init()

size = width, height = 620, 650
white = 255, 255, 255
red = (255,0,0)
black = (0,0,0)
x=0
y=0
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
bfs.makemapa()
mapa = bfs.mapa
#camino = bfs.returnPath(1)
Mononoke = pygame.image.load("mononoke.png")
Mononoke = pygame.transform.scale(Mononoke, (100, 100))
Ciervo = pygame.image.load("ciervo.png")
Ciervo = pygame.transform.scale(Ciervo,(100,100))
Elemental = pygame.image.load("elementales.png")
Elemental = pygame.transform.scale(Elemental,(100,100))
dios_Ciervo = pygame.image.load("dios_ciervo.png")
dios_Ciervo = pygame.transform.scale(dios_Ciervo,(100,100))
Fuente = pygame.font.Font(None,20)
Aviso_Amplitud= Fuente.render("Para Amplitud presione la tecla Q",True,(200,60,80))
Aviso_CostoU= Fuente.render("Para Costo uniforme presione la tecla W",True,(135,200,80))
Aviso_ProfundidadI= Fuente.render("Para Profundidad Iterativa presione la tecla E",True,(100,120,200))
Aviso_Reinicio= Fuente.render("Para Reiniciar el programa presione la tecla R",True,(200,200,200))
Musica = pygame.mixer.music.load("music.mp3")
Musica=pygame.mixer.music.play(10)
count = 0
Xamongus = 0
Yamongus = 0
amplitud = 0
profundidad = 0
costo = 0
reinicio = 0
estadofinal = 0
i = 0
def Eventos_teclado():
    global mapa
    global estadofinal
    global camino
    global costo
    global amplitud
    global profundidad
    global reinicio
    global i
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q and not estadofinal:
            amplitud = 1
            estadofinal = 1
            camino = bfs.returnPath(1)
        if event.key == pygame.K_w and not estadofinal:
            costo = 1
            estadofinal = 1
            camino = bfs.returnPath(2)
        if event.key == pygame.K_e and not estadofinal:
            profundidad = 1
            estadofinal = 1
            camino = bfs.returnPath(3)
        if event.key == pygame.K_r :
            amplitud = 0
            costo = 0
            profundidad = 0
            i = 0
            estadofinal = 0
            mapa = list()
            bfs.mapa = list()
            bfs.mapaString =''
            bfs.makemapa()
            camino = list()
            mapa = bfs.mapa
            #reinicio = 0


def pintarmapa():
    x=0
    y=0
    global Xamongus
    global Yamongus
    for fila in range(len(mapa)):
        for  columna in range(len(mapa[0])):
            if mapa[fila][columna] == "0":
                pygame.draw.rect(screen,black,[x,y,120,120],0)
                x+=121
            if mapa[fila][columna] == "5":
                screen.blit(Mononoke,[x,y])
                Xamongus = fila
                Yamongus = columna
                x+=121
            if mapa[fila][columna] == "3":
                screen.blit(Ciervo,[x,y])
                x+=121
            if mapa[fila][columna] == "4":
                screen.blit(dios_Ciervo,[x,y])
                x+=121
            if mapa[fila][columna] == "2":
                screen.blit(Elemental,[x,y])
                x+=121
            if mapa[fila][columna] == "1":
                pygame.draw.rect(screen,white,[x,y,120,120],0)
                x+=121
        x=0
        y+=121

def guiarMononoke():
    global i
    global Xamongus
    global Yamongus
    if Xamongus >= 0 and Yamongus <= 4 and i < len(camino):
        mapa[Xamongus][Yamongus] = '1'
        Xamongus = camino[i][0]
        Yamongus = camino[i][1]
        mapa[Xamongus][Yamongus] = '5'
        i += 1

while 1:
    screen.fill(black)
    pintarmapa()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        Eventos_teclado()
    if amplitud:
        guiarMononoke()
    if costo:
        guiarMononoke()
    if profundidad:
        guiarMononoke()

    time.sleep(0.5)
    screen.blit(Aviso_Amplitud,(40,500))
    screen.blit(Aviso_CostoU,(40,540))
    screen.blit(Aviso_ProfundidadI,(40,580))
    screen.blit(Aviso_Reinicio,(40,620))

    pygame.display.flip()
