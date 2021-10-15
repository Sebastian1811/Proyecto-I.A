import sys, pygame
import bfs
pygame.init()

size = width, height = 700, 700
white = 255, 255, 255
red = (255,0,0)
black = (0,0,0)
x=0
y=0

screen = pygame.display.set_mode(size)
bfs.makemapa()
mapa = bfs.mapa
Mononoke = pygame.image.load("Among u s.png")
Aparicion = [120,480]
count = 0
Xamongus = 0
Yamongus = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #pintar mapa
    screen.fill(white)
    x=0
    y=0
    for fila in range(len(mapa)):
        for  columna in range(len(mapa[0])):
            if mapa[fila][columna] != "0" and mapa[fila][columna] != "5":
                pygame.draw.rect(screen,black,[x,y,40,40],0)
                x+=41
            if mapa[fila][columna] == "0":
                pygame.draw.rect(screen,red,[x,y,40,40],0)
                x+=41
            if mapa[fila][columna] == "5":
                #screen.blit(Mononoke,[x,y])
                pygame.draw.rect(screen,white,[x,y,40,40],0)
                #print(fila, " ",columna)
                Xamongus = fila
                Yamongus = columna
                x+=41
        x=0
        y+=41

    #mover derecha
    if not count:
        print(Xamongus," ",Yamongus)
        mapa[int(Xamongus)][int(Yamongus)]="1"
        mapa[int(Xamongus)-1][int(Yamongus)+1]="5"
        count+=1




    pygame.display.flip()
