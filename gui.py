import sys, pygame
pygame.init()

size = width, height = 1000, 1000
black = 0, 0, 0

screen = pygame.display.set_mode(size)


Mononoke = pygame.image.load("Among u s.png")
velocidad_amongus = 0


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
            
    screen.fill(black)
    screen.blit(Mononoke, (500,500))
    pygame.display.flip()
