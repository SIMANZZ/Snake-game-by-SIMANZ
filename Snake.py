import pygame
from random import randrange

pygame.init()


def gameLoop():
    # Resolution of window
    RES = 800
    # The size of 1 sector of the snake
    HEAD = 50

    # Spawn snake and apple in random place
    x, y = randrange(0, RES, HEAD), randrange(0, RES, HEAD)
    apple = randrange(0, RES, HEAD), randrange(0, RES, HEAD)

    # To rule out accidental death)
    dirs = {'W': True, 'S': True, 'A': True, 'D': True}

    length = 1
    snake = [(x, y)]
    x1, y1 = 0, 0
    score = 0
    fps = 7

    window = pygame.display.set_mode((RES, RES))
    pygame.display.set_caption('by SIMANZ')
    snake_speed = pygame.time.Clock()
    font_score = pygame.font.SysFont('Arial', 26, bold=True)
    font_end = pygame.font.SysFont('Arial', 66, bold=True)
    font_chose = pygame.font.SysFont('Arial', 40, bold=True)
    img = pygame.image.load('1.jpg')

    while True:
        # Filling screen
        window.blit(img, (0, 0))

        # Drawing snake and apple
        [(pygame.draw.rect(window, pygame.Color('green'), (i, j, HEAD - 2, HEAD - 2))) for i, j in snake]
        pygame.draw.rect(window, pygame.Color('red'), (*apple, HEAD, HEAD))

        # Show score
        render_score = font_score.render('SCORE:' + str(score), True, pygame.Color('yellow'))
        window.blit(render_score, (5, 5))

        # Snake movement:
        x += x1 * HEAD
        y += y1 * HEAD
        snake.append((x, y))
        snake = snake[-length:]

        # Eating food
        if snake[-1] == apple:
            apple = randrange(0, RES, HEAD), randrange(0, RES, HEAD)
            length += 1
            score += 1

        # Game over
        if x < 0 or x > RES or y < 0 or y > RES or len(snake) != len(set(snake)):
            while True:
                render_end = font_end.render('GAME OVER', True, pygame.Color('yellow'))
                window.blit(render_end, (RES // 2 - 200, RES // 3))
                render_end = font_chose.render('Press SPACE-restart or ESC-exit', True, pygame.Color('yellow'))
                window.blit(render_end, (RES // 2 - 280, RES // 3 + 70))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            gameLoop()
                        elif event.key == pygame.K_ESCAPE:
                            exit()

        # Update display
        pygame.display.flip()
        snake_speed.tick(fps)

        # Controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and dirs['W']:
                    x1, y1 = 0, -1
                    dirs = {'W': True, 'S': False, 'A': True, 'D': True}
                elif event.key == pygame.K_s and dirs['S']:
                    x1, y1 = 0, 1
                    dirs = {'W': False, 'S': True, 'A': True, 'D': True}
                elif event.key == pygame.K_a and dirs['A']:
                    x1, y1 = -1, 0
                    dirs = {'W': True, 'S': True, 'A': True, 'D': False}
                elif event.key == pygame.K_d and dirs['D']:
                    x1, y1 = 1, 0
                    dirs = {'W': True, 'S': True, 'A': False, 'D': True}


gameLoop()
