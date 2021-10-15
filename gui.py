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
count = 0
Xamongus = 0
Yamongus = 0
while 1:
    screen.fill(black)
    x=0
    y=0

    for fila in range(len(mapa)):
        for  columna in range(len(mapa[0])):
            if mapa[fila][columna] != "0" and mapa[fila][columna] != "5":
                pygame.draw.rect(screen,white,[x,y,120,120],0)
                x+=121
            if mapa[fila][columna] == "0":
                pygame.draw.rect(screen,black,[x,y,120,120],0)
                x+=121
            if mapa[fila][columna] == "5":
                screen.blit(Mononoke,[x,y])
                #pygame.draw.rect(screen,white,[x,y,40,40],0)
                #print(fila, " ",columna)
                Xamongus = fila
                Yamongus = columna
                x+=121
        x=0
        y+=121
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        elif event.type == pygame.KEYDOWN:
            try:
                if event.key == pygame.K_UP:
                    contenido = mapa[(int(Xamongus)-1)][int(Yamongus)]
                    if contenido != "0":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[(int(Xamongus)-1)][int(Yamongus)]="5"
                if event.key == pygame.K_DOWN:
                    contenido = mapa[(int(Xamongus)+1)][int(Yamongus)]
                    if contenido != "0":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[int(Xamongus)+1][int(Yamongus)]="5"
                if event.key == pygame.K_LEFT:
                    contenido = mapa[(int(Xamongus))][int(Yamongus)-1]
                    if contenido != "0":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[int(Xamongus)][int(Yamongus)-1]="5"
                if event.key == pygame.K_RIGHT:
                    contenido = mapa[(int(Xamongus))][int(Yamongus)+1]
                    if contenido != "0":
                        mapa[int(Xamongus)][int(Yamongus)]="1"
                        mapa[int(Xamongus)][int(Yamongus)+1]="5"
            except Exception as inst:
                print("amongus no tiene mas espacio")



    #pintar mapa


    pygame.display.flip()
