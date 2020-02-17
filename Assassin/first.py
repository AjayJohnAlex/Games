import pygame
pygame.init()


win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("Assassin Game")

clock = pygame.time.Clock()


# loading multiple images
# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('Game/R1.png'), pygame.image.load('Game/R2.png'), pygame.image.load('Game/R3.png'), pygame.image.load('Game/R4.png'), pygame.image.load(
    'Game/R5.png'), pygame.image.load('Game/R6.png'), pygame.image.load('Game/R7.png'), pygame.image.load('Game/R8.png'), pygame.image.load('Game/R9.png')]

walkLeft = [pygame.image.load('Game/L1.png'), pygame.image.load('Game/L2.png'), pygame.image.load('Game/L3.png'), pygame.image.load('Game/L4.png'), pygame.image.load(
    'Game/L5.png'), pygame.image.load('Game/L6.png'), pygame.image.load('Game/L7.png'), pygame.image.load('Game/L8.png'), pygame.image.load('Game/L9.png')]

bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')


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
        self.standing = True
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

# for the projectile


class projectile(object):

    def __init__(self, x, y, radius, color, facing):

        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):

        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

# enemy


class enemy(object):

    walkRight = [pygame.image.load('Game/R1E.png'), pygame.image.load('Game/R2E.png'), pygame.image.load('Game/R3E.png'), pygame.image.load('Game/R4E.png'), pygame.image.load('Game/R5E.png'), pygame.image.load(
        'Game/R6E.png'), pygame.image.load('Game/R7E.png'), pygame.image.load('Game/R8E.png'), pygame.image.load('Game/R9E.png'), pygame.image.load('Game/R10E.png'), pygame.image.load('Game/R11E.png')]
    walkLeft = [pygame.image.load('Game/L1E.png'), pygame.image.load('Game/L2E.png'), pygame.image.load('Game/L3E.png'), pygame.image.load('Game/L4E.png'), pygame.image.load('Game/L5E.png'), pygame.image.load(
        'Game/L6E.png'), pygame.image.load('Game/L7E.png'), pygame.image.load('Game/L8E.png'), pygame.image.load('Game/L9E.png'), pygame.image.load('Game/L10E.png'), pygame.image.load('Game/L11E.png')]

    def __init__(self, x, y, width, height, end):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50, 10))

            pygame.draw.rect(win, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 20,
                              50 - (5 * (10 - self.health)), 10))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:  # change the direction
                self.vel = self.vel * -1
                self.walkCount = 0

        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:  # change the direction
                self.vel = self.vel * -1
                self.walkCount = 0

    # when the ene,y is hit
    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


def redrawGameWindow():
    win.blit(bg, (0, 0))

    # draw our charact er
    # every character in pygame is a surface and it lies on the window and colors all are in RGB
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    goblin.draw(win)
    text = font.render('score: ' + str(score), 1, (0, 0, 0))
    win.blit(text, (390, 10))
    # to show you need to refresh the window
    pygame.display.update()
# all pygame has a main loop which checks for collition , mouse events , movements etc


# for text to appear in pygame we need to create a font variable
font = pygame.font.SysFont('comicsans', 30, True, True)

man = player(50, 410, 64, 64)
bullets = []
goblin = enemy(80, 410, 64, 64, 400)
shoot_ones = 0
score = 0
run = True
while run:
    clock.tick(27)

    if shoot_ones > 0:
        shoot_ones += 1
    if shoot_ones > 3:
        shoot_ones = 0

    for event in pygame.event.get():  # list of all events
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        # checking if the bullets are hitting the enemy
        #  y co ordinate
        if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
            # x co orfinate
            if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:

                goblin.hit()
                score += 1
                bullets.pop(bullets.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel  # setting the bullet speed
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()
#  the and shoot_ones == 0 is to stop spaming of the space bar
    if keys[pygame.K_SPACE] and shoot_ones == 0:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width // 2),
                                      round(man.y + man.height // 2), 6, (0, 0, 0), facing))
        shoot_ones = 1

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False

    elif keys[pygame.K_RIGHT] and man.x < man.screen_width - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False

    else:
        man.standing = True
        man.walkCount = 0

    if not(man.is_Jump):
        if keys[pygame.K_UP]:
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
