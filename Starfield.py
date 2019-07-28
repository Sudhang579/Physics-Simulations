import pygame
import random
import math
pygame.init()

cx = 768
cy = 360
win = pygame.display.set_mode( (1366, 720 ) )

class Star:

    def __init__(self, x = 768, y = 360 , z = 100, speed = 0.01):
        self.x = random.randint( -768 , 768 )
        self.y = random.randint( -360 , 360 )
        self.z = math.sqrt(self.x**2 + self.y**2)/ 1000
        self.parm = 5
        self.speed = speed
        self.r = int ( self.z / 10)
        self.px = self.x
        self.py = self.y


    def draw(self, win ):

        pygame.draw.circle( win, (255, 255, 255), (cx + int(self.x), cy + int(self.y) ), self.r)
        pygame.draw.line(win, (255, 255, 255), (cx + int(self.px), cy + int(self.py) ), (cx + int(self.x), cy + int(self.y) ))

    def update(self):
        self.px = self.x
        self.py = self.y
        self.x +=  (self.speed * (  self.x) )
        self.y +=  ( self.speed * ( self.y) )
        #self.z = math.sqrt(self.x**2 + self.y**2)/ 20
        self.z += 0.1
        self.r = int ( self.z / 10)
        self.check()

    def check(self):
        if self.x < - 768 or self.x > 768:
            self.x = random.randint(-768, 768)
            self.y = random.randint(-360, 360)
            self.z = math.sqrt(self.x**2 + self.y**2)/ 1000
            self.px = self.x
            self.py = self.y

        if self.y < - 360 or self.y > 360:
            self.x = random.randint(-768, 768)
            self.y = random.randint(-360, 360)
            self.z = math.sqrt(self.x**2 + self.y**2)/ 1000
            self.px = self.x
            self.py = self.y


n_stars = 100
stars= []

for i in range(n_stars):
    stars.append(Star())

run = True


while run:
    win.fill((0, 0, 0))

    for i in range(n_stars):
        stars[i].draw(win)
        stars[i].update()



    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



















