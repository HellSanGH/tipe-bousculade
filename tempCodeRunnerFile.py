import pygame

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("TIPE : bousculades")
# Initializing RGB Color
color = (50, 50, 50)
 
# Changing surface color
screen.fill(color)
circle = pygame.draw.circle(screen, (255,255,255), (50, 50), 15, 15) # colour, cords, radius, thickness
x = 50

run = True
while run: 
    print(pygame.time.get_ticks())
    x+=5
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255,255,255), (x, 50), 15, 15)
    pygame.display.update()
    clock.tick(60)

pygame.quit()

'''
# Importing the library
import pygame
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 720))
color = (255, 0 , 0)
# Initializing Pygame modules
def main():
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(color)
        pygame.display.flip()
        pygame.display.update()
        clock.tick(60)
main()
'''