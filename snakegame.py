
# Snake Game !

import pygame, sys, random, time


check_errors = pygame.init()
if check_errors[1] > 0:
    print('(!) Had {0} intialising erros,existing...'.format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) PyGame successfully intialised")

#Play Surface

playSurface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('This Fabians Snake Game!')
#time.sleep(5)

#colours rgb
red = pygame.Color(255, 0 ,0) #gameover
green = pygame.Color(0, 255, 0) #snake
black = pygame.Color(0, 0, 0)#score
white = pygame.Color(255, 255, 255)#background
brown = pygame.Color(165, 42, 42)#food

#FPS controller

fpscontroller = pygame.time.Clock()

# Variable
#snake position x& dont exceed screen size

snakePos = [100, 50]
snakeBody = [[100,50],[90,50],[80,50]]

#food spawning randomised x,y

foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
foodSpawn = True

#directional spawn

direction = 'RIGHT'
changeto = direction

score = 0
#Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco',72)
    GOsurf = myFont.render('Game Over!',True, red)
    Gorect = GOsurf.get_rect()
    Gorect.midtop = (360, 15)
    playSurface.blit(GOsurf, Gorect)
    showscore(0)
    pygame.display.flip()
    time.sleep(20)
    pygame.quit()#game exit
    sys.exit() #console
# Main logic -Events- controls
# ascii value ord('a')

#show score
def showscore(choice =1):
    sfont = pygame.font.SysFont('monaco', 24)
    ssurf = sfont.render('Score : {}'.format(score), True, black)
    Srect = ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(ssurf, Srect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
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
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, (pos[0], pos[1], 10, 10), 0)

    pygame.draw.rect(playSurface, brown, (foodPos[0], foodPos[1], 10, 10), 0)

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()

    showscore()
    pygame.display.update()
    fpscontroller.tick(15)
#gameOver()

