import pygame
pygame.init()


win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Assassin Game")


x = 50
y = 425
width = 40
height = 60
vel = 5

screen_width = 500

is_Jump = False
jumpCount = 10
# all pygame has a main loop which checks for collition , mouse events , movements etc

run = True
while run:
    pygame.time.delay(100)  # in ms

    for event in pygame.event.get():  # list of all events
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < screen_width - width - vel:
        x += vel

    if not(is_Jump):

        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < screen_width - height - vel:
            y += vel

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

    win.fill((0, 0, 0))

    # draw our character
    # every character in pygame is a surface and it lies on the window and colors all are in RGB
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # to show you need to refresh the window
    pygame.display.update()


pygame.quit()
