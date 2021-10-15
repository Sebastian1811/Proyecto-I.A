import sys, pygame
import bfs
pygame.init()

size = width, height = 1280, 720
white = 255, 255, 255
red = (255,0,0)
black = (0,0,0)
x=0
y=0

screen = pygame.display.set_mode(size,pygame.RESIZABLE)
bfs.makemapa()
mapa = bfs.mapa
Mononoke = pygame.image.load("mononoke.png")
Mononoke = pygame.transform.scale(Mononoke, (100, 100))
Ciervo = pygame.image.load("ciervo.png")
Ciervo = pygame.transform.scale(Ciervo,(100,100))
Elemental = pygame.image.load("elementales.png")
Elemental = pygame.transform.scale(Elemental,(100,100))
dios_Ciervo = pygame.image.load("dios_ciervo.png")
dios_Ciervo = pygame.transform.scale(dios_Ciervo,(100,100))

count = 0
Xamongus = 0
Yamongus = 0
while 1:
    screen.fill(black)
    x=0
    y=0

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_UP:
                    contenido = mapa[(int(Xamongus)-1)][int(Yamongus)]
                    if contenido != "0" or contenido !="4" or contenido != "2":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[(int(Xamongus)-1)][int(Yamongus)]="5"
                if event.key == pygame.K_DOWN:
                    contenido = mapa[(int(Xamongus)+1)][int(Yamongus)]
                    if contenido != "0" or contenido !="4" or contenido != "2":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[int(Xamongus)+1][int(Yamongus)]="5"
                if event.key == pygame.K_LEFT:
                    contenido = mapa[(int(Xamongus))][int(Yamongus)-1]
                    if contenido != "0" or contenido !="4" or contenido != "2":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[int(Xamongus)][int(Yamongus)-1]="5"
                if event.key == pygame.K_RIGHT:
                    contenido = mapa[(int(Xamongus))][int(Yamongus)+1]
                    if contenido != "0" or contenido !="4" or contenido != "2":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[int(Xamongus)][int(Yamongus)+1]="5"
            except Exception as inst:
                print("amongus no tiene mas espacio")



    #pintar mapa


    pygame.display.flip()
