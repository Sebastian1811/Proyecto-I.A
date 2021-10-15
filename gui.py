import sys, pygame
pygame.init()

size = width, height = 720, 480
white = 255, 255, 255
red = (255,0,0)
x=0
y=0

screen = pygame.display.set_mode(size)

mapa = [
    "XXXXXXX",
    "X     X",
    "X X   X",
    "X  XX X",
    "X0    X",
    "XXXXXXX"

]

Mononoke = pygame.image.load("Among u s.png")
Aparicion = (120,480)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #pintar mapa
    screen.fill(white)
    x=0
    y=0
    for fila in mapa:
        for  muro in fila:
            if muro == "X":
                pygame.draw.rect(screen,red,[x,y,120,120],0)
            x+=121
        x=0
        y+=121
    
    x=0
    y=0
    for fila in mapa:
        for muro in fila:
            if muro == "0":
                screen.blit(Mononoke,Aparicion)



    pygame.display.flip()
