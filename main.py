import pygame,Controls

from Restart_Menu import RestartMenu
from Player import PlayerBird
from Ground import Ground
from Beam import Beam
from Start_Menu import StartMenu

from random import randint

pygame.init()

screen = pygame.display.set_mode((1000, 800))
white = (250,250,250)
black = (0,0,0)
blue = (112, 197, 206)

lose = False

score = 0
highscore = 0

scorefont = pygame.font.SysFont('bahnschrift',40)

running = True
pygame.display.set_caption('Flappy Bird')
bird = pygame.image.load('Sources/images/flappy bird.png').convert()
icon = pygame.image.load('Sources/images/icon.png')
pygame.display.set_icon(icon)

screen.fill(blue)
pygame.display.update()

player = PlayerBird(0,100)
beams = [Beam(1000,200),Beam(1300,300),Beam(2000,400)]

ground = Ground()

def update():
    global score,beams,running,highscore
    screen.fill(blue)

    player.update()
    for beam in beams:
        beam.update()
        if beam.x < player.x-100:
            beams.remove(beam)
            beams.append(Beam(beams[1].x + (50 * randint(6,10)),randint(100,450)))

    ground.update()

    screen.blit(scorefont.render('Score: '+str(score), True, white), (400, 720))

    if (beams[0].x-180 < player.x < beams[0].x and not beams[0].height + 30 < player.y < beams[0].height + 200) or player.y >= 650:
        Controls.paused = True

        if score > highscore:
            highscore = score

        menu = RestartMenu()
        menu.update()

        while Controls.paused and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 450 < event.pos[0] < 540 and 400 < event.pos[1] < 500:
                        score = 0
                        beams = [Beam(1000, 200), Beam(1300, 300), Beam(2000, 400)]
                        player.x = 0
                        player.y = 100
                        player.Y_change = 0
                        Controls.paused = False
                        screen.fill(blue)
                        pygame.display.update()

                        del menu

            pygame.time.delay(20)

    elif beams[0].x - 40 < player.x < beams[0].x - 30:
        score += 1

    pygame.display.update((400, 720), (451, 721))


menu = StartMenu()
while not menu.playButtonPressed and running:
    menu.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100)

del menu

while running:
    try:
        update()
        pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    except pygame.error:
        quit()

pygame.display.quit()
pygame.quit()
