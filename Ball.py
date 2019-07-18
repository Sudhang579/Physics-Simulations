
import pygame, time
import math

wScreen = 1366
hScreen = 720
win = pygame.display.set_mode((wScreen, hScreen))

class ball(object):

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius-1)

    @staticmethod
    def ballPath( startx , starty, vel_0, ang, time):
        newx = startx + (math.cos(ang)* vel_0)* time
        vy = math.sin(angle) * vel_0
        newy = starty - ( vy*time - 4.9 * (time**2)/2 )

        newx = round(newx)
        newy = round(newy)
        return newx, newy



def find_angle(pos):
        sX = golfBall.x
        sY = golfBall.y
        try:
            angle = math.atan((sY - pos[1]) / (sX - pos[0]))
        except:
            angle = math.pi / 2

        if pos[1] < sY and pos[0] > sX:
            angle = abs(angle)
        elif pos[1] < sY and pos[0] < sX:
            angle = math.pi - angle
        elif pos[1] > sY and pos[0] < sX:
            angle = math.pi + abs(angle)
        elif pos[1] > sY and pos[0] > sX:
            angle = (math.pi * 2) - angle
        return angle
def redrawWindow():
    win.fill((64, 64, 64))
    golfBall.draw(win)
    pygame.draw.line(win , (255, 255, 255), positions[0], positions[1])
    pygame.display.update()

x = 0
y = 0
golfBall = ball(600, 714, 5, (255, 255, 255))
run = True
vel_0 = 0
time = 0
shoot = False
while run:

    if shoot:
        if golfBall.y < 715:
            time+=0.05
            po = golfBall.ballPath( x, y, vel_0, angle, time)
            golfBall.x = po[0]
            golfBall.y = po[1]
        else:
            #shoot = False
            time = 0
            #x = golfBall.x
            #y = golfBall.y
            golfBall.y = 719 - golfBall.radius
            x = golfBall.x
            y =golfBall.y
        for event in pygame.event.get():
            if event.type == pygame.BUTTON_LEFT:
                    shoot = False
                    x = golfBall.x
                    y = golfBall.y

    pos = pygame.mouse.get_pos()
    positions = [ (golfBall.x , golfBall.y), pos]

    redrawWindow()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if shoot == False:
                shoot = True
                x = golfBall.x
                y = golfBall.y
                vel_0 = math.sqrt( (positions[0][0]-positions[1][0])**2 + (positions[0][1]-positions[1][1])**2) / 8
                angle = find_angle(pos)



