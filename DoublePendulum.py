import pygame
import math

r1 = 100
r2 = 100
m1 = 1
m2 = 1
a1 = math.pi/4
a2 = math.pi/4
x2 = 10
y2 = 10
cx = 683
cy = 360
a1_v = 0
a1_a = 0
a2_v = 0
a2_a = 0
g = 0.02
wScreen = 1366
hScreen = 720
win = pygame.display.set_mode( (wScreen, hScreen) )

def draw():
    x1 = cx + r1 * math.sin(a1)
    y1 = cy + r1 * math.cos(a1)
    x2 = x1 + r2 * math.sin(a2)
    y2 = y1 + r2 * math.cos(a2)

    pygame.draw.circle( win, (0, 0, 0), list(map(int, (x1, y1))) , 10 )
    pygame.draw.circle( win, (0, 0, 0), list(map(int, (x2, y2))) , 10 )

    pygame.draw.line( win, (0, 0, 0), (cx, cy), (x1, y1), 3 )
    pygame.draw.line( win, (0, 0, 0), (x1, y1), (x2, y2), 3 )
    pygame.draw.line( win, (0, 0, 0), (x1, y1), (x2, y2), 3 )
    #pygame.draw.line( win, (0, 0, 0), (x2_t, y2_t), (x2, y2), 1 )


def redraw():
    win.fill( (255, 255, 255) )
    draw( )
    pygame.display.update()

def to_pygame( coords, h = hScreen, w = wScreen):
    return (coords[0], h - coords[1])


run = True

while run:

    redraw()

    a1_v += a1_a
    a2_v += a2_a

    a1 += a1_v
    a2 += a2_v

    num1 = -g * ( 2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * g * math.sin(a1 - 2*a2)
    num3 = -2 * math.sin(a1 -a2) * m2
    num4 = a2_v*a2_v* r2 + a1_v*a1_v * r1 * math.cos(a1 - a2)
    den = r1 * ( 2*m1 + m2 - m2*math.cos(2*a1 - 2*a2))
    a1_a = (num1 + num2 + num3 * num4)/ den

    num1 = 2 * math.sin(a1 - a2)
    num2 = (a1_v * a1_v * r1 *(m1 + m2))
    num3 = g*(m1 + m2) * math.cos(a1)
    num4 = a2_v * a2_v * r2*m2*math.cos(a1-a2)
    den = r2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))
    a2_a = ( num1*(num2 + num3 + num4)) / den

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
