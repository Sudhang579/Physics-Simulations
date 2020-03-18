import pygame
import math

pygame.init()
winx, winy = 1350, 700
centre = (int(winx / 2), int(winy / 2))
radius = 150
win = pygame.display.set_mode((winx, winy))
theta = 0
theta_step = -0.001
n_points = 5000
n_circles = 3
waveVel = 0.03
x_wave_centre = centre[0] + 100

waveArr = []



class WavePoint:

    def __init__(self, ax, ay, waveVel):
        self.x = ax
        self.y = ay
        self.waveVel = waveVel

    def updateW(self):
        self.x += self.waveVel

    def drawWave(self):
        pygame.draw.line(win, (255, 255, 255), (self.x, self.y), (self.x, self.y))

class Circle:

    def __init__(self, xc, yc, radius, theta, theta_step):
        self.xc = int(xc)
        self.yc = int(yc)
        self.radius = int(radius)
        self.theta = int(theta)
        self.theta_step = theta_step
        self.x = 0
        self.y = 0

    def drawCircle(self):

        pygame.draw.circle(win, (255, 255, 255), (self.xc, self.yc), self.radius, 1)
        pygame.draw.line(win, (255, 255, 255), (self.xc, self.yc), (self.x, self.y ) )

    def update(self):
        self.x = int(self.xc + self.radius * math.cos(self.theta))
        self.y = int(self.yc + self.radius * math.sin(self.theta))
        self.theta += self.theta_step



circArr = []

    #circArr.append(Circle(centre[0], centre[1], radius, 1, 0.01))

circArr.append(Circle(centre[0], centre[1], radius, 0, theta_step))
circArr[0].update()
for o in range(1, n_circles):
    circArr.append(Circle( circArr[o-1].x, circArr[o-1].y, radius/ (2*o +1) , 0, theta_step * (2*o +1 ) ))

run = True

z = 0
while run:
    x = 0
    y = 0
    win.fill((0, 0, 0))
    circArr[0].drawCircle()
    circArr[0].update()

    #circArr[0].x = int(centre[0] + radius * math.cos(circArr[0].theta))
    #circArr[0].y = int(centre[1] + radius * math.sin(circArr[0].theta))
    for o in range(1, n_circles):
        circArr[o].xc = circArr[o-1].x
        circArr[o].yc = circArr[o-1].y


        circArr[o].drawCircle()
        circArr[o].update()
    x = circArr[n_circles -1].x
    y = circArr[n_circles - 1].y


    #circArr[1].drawCircle()
    #circArr[1].update()



    waveArr.append(WavePoint(ax=centre[0] + 200, ay=y, waveVel=waveVel))
    waveArr[z].y = y

    for i in range(len(waveArr)):
        waveArr[i].updateW()
        waveArr[i].drawWave()
    pygame.draw.line(win, (255,255,255), ( x,y ), (centre[0] + 200, y ), 1)
    z += 1
    if (z>n_points):
        waveArr = []
        z = 0

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
