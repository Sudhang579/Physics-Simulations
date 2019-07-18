import pygame
import random

class Drop():
    g = 0.01

    def __init__(self, x, y , z):
        self.x = x
        self.y = y
        self.z = z
        self.yvel = z/20
        self.g = z / 20 * 0.01
        self.t = 0


    def fall(self):
        self.y += self.yvel
        self.yvel += self.g

    def show(self, win):
        pygame.draw.line(win, (0 , 0 , 0), (self.x, self.y), (self.x, self.y + 10), int(self.z / 20 *4))


def reDraw(object):

    object.show(win)

win = pygame.display.set_mode((1366 , 720))

n_drops = 1000
drops = []
for i in range(n_drops):
    drops.append(Drop(random.randrange(0, 1366), random.randrange(-1500, -0), random.randint( 0 , 20 )))


run = True
while run:
    win.fill((230, 230, 250))
    for i in range(n_drops):
        reDraw(drops[i])
        if drops[i].y >= 720:
            drops[i].y = 0
            drops[i].yvel = 1

        else:
            drops[i].fall()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


