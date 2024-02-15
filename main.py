import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("TIPE : évolution")

run = True
while run: 
    screen.fill((40, 35, 40))

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
