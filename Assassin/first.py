import pygame
pygame.init()


win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Assassin Game")

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5

screen_width = 500

is_Jump = False
jumpCount = 10

left = False
right = False
walkCount = 0

# loading multiple images
# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load(
    'Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]

walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load(
    'Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]

bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')


def redrawGameWindow():
    global walkCount

    win.blit(bg, (0, 0))

    # draw our charact er
    # every character in pygame is a surface and it lies on the window and colors all are in RGB
    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1

    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1

    else:
        win.blit(char, (x, y))

    # to show you need to refresh the window
    pygame.display.update()
# all pygame has a main loop which checks for collition , mouse events , movements etc


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():  # list of all events
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False

    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel
        right = True
        left = False

    else:
        right = False

    if not(is_Jump):
        if keys[pygame.K_SPACE]:
            is_Jump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1

        else:
            is_Jump = False
            jumpCount = 10

    # fill the screen before drawing the character
    redrawGameWindow()
pygame.quit()
