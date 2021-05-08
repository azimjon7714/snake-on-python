# install pygame and import, also import randrange for random numbers
from ctypes.wintypes import SIZE

import pygame
from random import randrange

RES = 600
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 5

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
img = pygame.image.load('1.jpg').convert()

while True:
    sc.blit(img, (0, 0))
    #drawing snake, and apple
    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
    # show score
    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    # snake movement
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]
    # eating apple
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        fps += 1
    # game over mode
    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

    pygame.display.flip()
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        # control
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            dx, dy = 0, -1
        if key[pygame.K_s]:
            dx, dy = 0, 1
        if key[pygame.K_a]:
            dx, dy = -1, 0
        if key[pygame.K_d]:
            dx, dy = 1, 0