import pygame
pygame.init()




class Block:


    count = 0

    def __init__(self, x , w, v, m ):
        self.x = x
        self.w = w
        self.v = v
        self.m = m


    def update(self):
        self.x += self.v

    def draw(self):
        #pygame.draw.circle( win, (255, 255, 255), (self.x, self.w), 15)
        pygame.draw.rect( win, ( 255, 255, 255), (self.x, 720 - self.w , self.w, self.w ) )

    def collide(self, other):
        if (self.x > (other.x + other.w) ) or ( ( self.x + self.w ) <  other.x ):
            return False
        else:
            return True

    def bounce(self, other):
        if self.collide(other):
            Block.count += 1
            newV1 = ( (self.m - other.m)/(self.m + other.m) ) * self.v + ( 2 * other.m * other.v / ( self.m + other.m ) )
            newV2 = ( (other.m - self.m)/(self.m + other.m) ) * other.v + ( 2 * self.m * self.v / ( self.m + other.m ) )
            self.v = newV1
            other.v = newV2

        #self.checkWall()
        other.checkWall()

    def checkWall(self):
        if self.x < 0:
            self.v = - self.v
            Block.count += 1

def redraw(object):
    object.draw()

win = pygame.display.set_mode( (1366, 720) )
font = pygame.font.Font('freesansbold.ttf', 32)

time_step = 10

b1 = Block( 200, 100 , -1/time_step, 10**4)
b2 = Block( 100, 50 , 0 , 1)
run = True

while run:

    for i in range(time_step):
        win.fill((0, 0, 0))
        text = font.render(str(Block.count), True, (0, 255, 0), (0, 0, 255))
        textRect = text.get_rect()
        textRect.center = (1000, 600)
        win.blit(text, textRect)

        b1.update()
        b2.update()

        b1.bounce(b2)

        redraw(b1)
        redraw(b2)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False








