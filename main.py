import pygame
from pygame import Rect

pygame.init()
screen = pygame.display.set_mode((1200, 640))
run = True
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLOR1 = (250, 128, 114)
COLOR2 = (65, 105, 225)
COLOR4 = (255, 127, 80)
COLOR3 = (221, 160, 221)
COLOR5 = (144, 238, 144)
background = WHITE

c = 0
f = 0
flag = False
drawing = False
# clock = pygame.time.Clock()
x, y = 0, 0
speed = 10
screen.fill(WHITE)
pygame.display.update()
width, height = 0, 0
size = 0

r = Rect(100, 50, 50, 50)
v = [2, 2]
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_CAPSLOCK:
                if c == 0:
                    background = COLOR1
                elif c == 1:
                    background = COLOR2
                elif c == 2:
                    background = COLOR3
                elif c == 3:
                    background = COLOR4
                else:
                    background = COLOR5
                c = (c + 1) % 5
            if event.key == pygame.K_BACKSPACE:
                background = WHITE
            screen.fill(background)
            pygame.display.update()

            if event.key == pygame.K_SPACE and f == 0:
                width, height = size
                f = 1
            if event.key == pygame.K_SPACE and f == 1:
                flag = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
        elif event.type == pygame.MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            screen.fill(background)
            rect = pygame.draw.rect(screen, BLACK, (start, size))
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            drawing = False
            screen.fill(background)
            rect = pygame.draw.rect(screen, BLACK, (start, size))
            r = Rect(start, size)
            pygame.display.update()

        if flag:
            tg = height / width
            step_x = 1
            step_y = tg
            x += step_x
            y += step_y
            plus_x = True
            plus_y = True
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, (x, y, width, height))
            pygame.display.update()

            while x != 0 and y != 0:
                if x + step_x >= 1200 - width:
                    plus_x = False
                elif x - step_x <= 0:
                    plus_x = True
                elif y + step_y >= 640 - height:
                    plus_y = False
                elif y - step_y <= 0:
                    plus_y = True

                if plus_x:
                    x += step_x
                else:
                    x -= step_x
                if plus_y:
                    y += step_y
                else:
                    y -= step_y
                screen.fill(WHITE)
                pygame.draw.rect(screen, BLACK, (x, y, width, height))
                pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x >= 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x <= 1200 - width:
            x += speed
        if keys[pygame.K_UP] and y >= 0:
            y -= speed
        if keys[pygame.K_DOWN] and y <= 640 - height:
            y += speed
        pygame.draw.rect(screen, BLACK, (x, y, width, height))
        pygame.display.update()

