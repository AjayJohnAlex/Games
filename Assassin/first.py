import pygame
pygame.init()


win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Assassin Game")

clock = pygame.time.Clock()


class player(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.is_Jump = False
        self.jumpCount = 10
        self.screen_width = 500
        self.right = False
        self.left = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.left:
            win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        elif self.right:
            win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1

        else:
            win.blit(char, (self.x, self.y))


# loading multiple images
# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load(
    'Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]

walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load(
    'Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]

bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')


def redrawGameWindow():
    win.blit(bg, (0, 0))

    # draw our charact er
    # every character in pygame is a surface and it lies on the window and colors all are in RGB
    man.draw(win)
    # to show you need to refresh the window
    pygame.display.update()
# all pygame has a main loop which checks for collition , mouse events , movements etc


man = player(300, 410, 64, 64)

run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():  # list of all events
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False

    if keys[pygame.K_RIGHT] and man.x < man.screen_width - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False

    else:
        man.right = False

    if not(man.is_Jump):
        if keys[pygame.K_SPACE]:
            man.is_Jump = True
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1

        else:
            man.is_Jump = False
            man.jumpCount = 10

    # fill the screen before drawing the character
    redrawGameWindow()
pygame.quit()
