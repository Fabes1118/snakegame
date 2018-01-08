        # Snake Game!
        import pygame
        import sys
        import random
        import time
        import shelve



        check_errors = pygame.init()
        if check_errors[1] > 0:
            print('(!) Had {0} intialising erros,existing...'.format(check_errors[1]))
            sys.exit(-1)
        else:
            print("(+) PyGame successfully intialised")



        #Play Surface and sound

        playSurface = pygame.display.set_mode((720, 460))
        pygame.display.set_caption('Snake Game!')
        eating_sound = pygame.mixer.Sound("powerpellet.wav")
    #validation of direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    # left to right increase
    # up to down increase
    #updating the sanke position

    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10
    #Body update

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 10
        foodSpawn = False
        eating_sound.play()
        fpscontroller.tick() + 1
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playSurface.fill(brown)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, (pos[0], pos[1], 10, 10), 0)

    pygame.draw.rect(playSurface, red, (foodPos[0], foodPos[1], 10, 10), 0)

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()

    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()



    showscore()


    gamescore = open('score.txt', 'w')
    gamescore.write('Score : {}'.format(score))
    gamescore.close()

    pygame.display.update()
    fpscontroller.tick(15)
#gameOver()

