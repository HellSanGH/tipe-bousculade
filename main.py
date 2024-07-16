#████████╗██╗██████╗░███████╗
#╚══██╔══╝██║██╔══██╗██╔════╝
#░░░██║░░░██║██████╔╝█████╗░░
#░░░██║░░░██║██╔═══╝░██╔══╝░░
#░░░██║░░░██║██║░░░░░███████╗
#░░░╚═╝░░░╚═╝╚═╝░░░░░╚══════╝
#    █▀█ ─█▀█─ ── █▀█ █▀▀ 
#    ─▄▀ █▄▄█▄ ▀▀ ─▄▀ ▀▀▄ 
#    █▄▄ ───█─ ── █▄▄ ▄▄▀
####################################################
# Imports
import pygame
import time
from math import *
from random import *

####################################################
# Classes and functions

class Circle:
    def __init__(self, default_x, default_y, color = (255, 255, 255)):
        self.coordinate_x = default_x
        self.coordinate_y = default_y
        self.color = color
        self.goal = (self.coordinate_x, self.coordinate_y)
        self.vx = 0
        self.vy = 0

    def set_goal(self, goal_x, goal_y):
        self.goal = (goal_x, goal_y)

    def render_goal(self):
        circle = pygame.draw.circle(screen, (255,0,0), (self.goal[0], self.goal[1]), 5, 3)

    def render_tick(self, portee = []):
        n = int(255/(len(portee)+1))
        self.color = (255, n, n)
        circle = pygame.draw.circle(screen, self.color, (self.coordinate_x, self.coordinate_y), radius, radius) # colour, cords, radius, thickness
        self.render_goal()
        # Représentation des vecteurs direction
        # pygame.draw.line(screen, line_color, (self.coordinate_x, self.coordinate_y), (self.coordinate_x+self.vx*10, self.coordinate_y+self.vy*10))
        self.movement(portee)

    def goal_tick(self):
        self.coordinate_x += self.vx
        self.coordinate_y += self.vy

    def movement(self, portee):
        d_x = self.goal[0] - self.coordinate_x
        d_y = self.goal[1] - self.coordinate_y
        if not (d_x == 0 and d_y == 0):
            v_x = ( d_x / (abs(d_x) + abs(d_y))) *speed
            v_y = ( d_y / (abs(d_x) + abs(d_y))) *speed
        else :
            v_x = 0
            v_y = 0

        flag = 0
        for w in walls:
            if is_circle_wall_collide(self, w):
                flag = 1
                v = sqrt(v_x ** 2 + v_y **2)
                if w.orientation == 0:
                    v_y = 0
                    if d_x < 0 :
                        v_x = -v
                    else :
                        v_x = v
                if w.orientation == 1:
                    v_x = 0
                    if d_y < 0 :
                        v_y = -v
                    else :
                        v_y = v
        for i in portee:
            v_x += (i.vx)
            v_y += (i.vy)
        N = len(portee) + 1
        self.vx = v_x*(1/N)
        self.vy = v_y*(1/N)

        v_x = 0
        v_y = 0

        if flag == 0:
            for i in portee:
               if not(self.coordinate_x == i.coordinate_x) :
                   self.vx += (2/(self.coordinate_x - i.coordinate_x))
               if not(self.coordinate_y == i.coordinate_y) :
                   self.vy += (2/(self.coordinate_y - i.coordinate_y))



class Wall:
    def __init__(self, start_x, start_y, end_x, end_y):
        self.coordinates_start = (start_x, start_y)
        self.coordinates_end = (end_x, end_y)
        if self.coordinates_start[0] == self.coordinates_end[0] :
            self.orientation = 1 # 0 = Vertical
        if self.coordinates_start[1] == self.coordinates_end[1] :
            self.orientation = 0 # 0 = Horizontal
    
    def render_tick(self):
        pygame.draw.line(screen, line_color, self.coordinates_start, self.coordinates_end)




def on_goal(Circle: Circle):
    return abs(Circle.coordinate_x-Circle.goal[0]) <=10 and abs(Circle.coordinate_y-Circle.goal[1]) <= (10*radius)

def is_circle_wall_collide(Circle: Circle, Wall:  Wall): # Detects if the circle collides with the wall
    x = Circle.coordinate_x
    y = Circle.coordinate_y
    return (Wall.coordinates_start[0] - radius < x and x < Wall.coordinates_end[0] + radius) and (Wall.coordinates_start[1] - radius < y and y < Wall.coordinates_end[1] + radius)

def in_range(Circle: Circle, i): # Returns the set of circles in range of the circle
    portee = []
    for c in range(len(circles)):
        if c != i:
            if sqrt((circles[c].coordinate_x - Circle.coordinate_x)**2 + (circles[c].coordinate_y - Circle.coordinate_y)**2) <= (2 * radius):
                portee.append(circles[c])
    return portee



####################################################
# Pygame initialisation

screen_res = (1280, 720)
background_color = (50, 50, 50)
line_color = (255, 255, 255)
radius = 15
speed = 3

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(screen_res)
pygame.display.set_caption("TIPE : bousculades")
screen.fill(background_color)

####################################################
# Main run body
n = 15
circles = []

########################### Circles
# goal = (randint(0, screen_res[0]), randint(0, screen_res[1]))
goal = (640, 30)
for i in range(n):
#    circles.append(Circle(randint(0, screen_res[0]), randint(0, screen_res[1]), (randint(0,255), randint(0,255), randint(0,255))))
    circles.append(Circle(randint(100 + radius, 1180 - radius), randint(60 + radius, 660 - radius), (randint(0,255), randint(0,255), randint(0,255))))
    circles[i].set_goal(goal[0], goal[1])
#    a[i].set_goal(randint(0, screen_res[0]), randint(0, screen_res[1]))

########################### Walls
walls = []
walls.append(Wall(100, 60, 100, 660))
walls.append(Wall(1180, 60, 1180, 660))
walls.append(Wall(100, 60, 620, 60))
walls.append(Wall(660, 60, 1180, 60))
walls.append(Wall(100, 660, 1180, 660))

walls.append(Wall(300, 200, 620, 200)) # horizontal middle1
walls.append(Wall(660, 200, 1000, 200)) # horizontal middle2

walls.append(Wall(200, 200, 200, 500)) # vertical side left
walls.append(Wall(760, 250, 760, 600)) # vertical side right








run = True
while run:
    for i in range(0,1):
        a = Circle(randint(100 + radius, 1180 - radius), randint(60 + radius, 660 - radius), (randint(0,255), randint(0,255), randint(0,255)))
        a.set_goal(goal[0], goal[1])
        circles.append(a)

    #print(pygame.time.get_ticks())
    for i in range(len(circles)):
        circles[i].goal_tick()

    #Render tick
    screen.fill(background_color)

    for i in range(len(circles)):
        portee = in_range(circles[i], i)
        print(len(portee))
        if not(on_goal(circles[i])):
            circles[i].render_tick(portee)

    circles_new = []
    for w in range(len(circles)):
        if not(on_goal(circles[w])):
            circles_new.append(circles[w])
    circles = circles_new



    for j in range(len(walls)):
        walls[j].render_tick()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()
