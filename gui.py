import sys, pygame
import time
import agente

pygame.init()
size = width, height = 600, 650
white = 255, 255, 255
red = (255,0,0)
black = (0,0,0)
x=0
y=0
screen = pygame.display.set_mode(size,pygame.RESIZABLE)
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
amplitud = 0
profundidad = 0
costo = 0
estadofinal = 0
princesaMononoke = agente.agente('Mononoke')
princesaMononoke.setPercepcion()

def Eventos_teclado():

    global estadofinal
    global costo
    global amplitud
    global profundidad

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q and not estadofinal:
            amplitud = 1
            estadofinal = 1
            princesaMononoke.setActuacion(1)
        if event.key == pygame.K_w and not estadofinal:
            costo = 1
            estadofinal = 1
            princesaMononoke.setActuacion(2)
        if event.key == pygame.K_e and not estadofinal:
            profundidad = 1
            estadofinal = 1
            princesaMononoke.setActuacion(3)
        if event.key == pygame.K_r :
            amplitud = 0
            costo = 0
            profundidad = 0
            princesaMononoke.setMovimientos()
            estadofinal = 0
            princesaMononoke.percepcion = list()
            princesaMononoke.setPercepcion()

def pintarmapa():

    x=0
    y=0
    mapa = princesaMononoke.percepcion

    for fila in range(len(mapa)):
        for  columna in range(len(mapa[0])):
            if mapa[fila][columna] == "0":
                pygame.draw.rect(screen,red,[x,y,120,120],0)
                x+=121
            if mapa[fila][columna] == "5":
                screen.blit(Mononoke,[x+10,y+10])
                x+=121
            if mapa[fila][columna] == "3":
                screen.blit(Ciervo,[x+10,y+10])
                x+=121
            if mapa[fila][columna] == "4":
                screen.blit(dios_Ciervo,[x+10,y+10])
                x+=121
            if mapa[fila][columna] == "2":
                screen.blit(Elemental,[x+10,y+10])
                x+=121
            if mapa[fila][columna] == "1":
                pygame.draw.rect(screen,white,[x,y,120,120],0)
                x+=121
        x=0
        y+=121
if __name__ != '__main__':
    while 1:
        screen.fill(black)
        pintarmapa()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            Eventos_teclado()
        if amplitud:

            princesaMononoke.movimiento()
        if costo:
            princesaMononoke.movimiento()
        if profundidad:
            princesaMononoke.movimiento()
        time.sleep(0.5)
        screen.blit(Aviso_Amplitud,(40,500))
        screen.blit(Aviso_CostoU,(40,540))
        screen.blit(Aviso_ProfundidadI,(40,580))
        screen.blit(Aviso_Reinicio,(40,620))
        pygame.display.flip()
