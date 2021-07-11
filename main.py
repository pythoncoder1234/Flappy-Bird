import pygame,Controls
import AI

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

highscoretxt = open("highscore.txt")
highscore = int(highscoretxt.read())
highscoretxt.close()

scorefont = pygame.font.SysFont('bahnschrift',40)

running = True
pygame.display.set_caption('Flappy Bird')
bird = pygame.image.load('images/flappy bird.png').convert()
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

screen.fill(blue)
pygame.display.update()

player = PlayerBird(0,100)
beams = [Beam(1000,200),Beam(1500,300),Beam(2000,400)]

ground = Ground()

def reset():
    global score
    score = 0
    beams = [Beam(1000, 200), Beam(1300, 300), Beam(2000, 400)]
    player.x = 0
    player.y = 100
    player.Y_change = 0
    Controls.paused = False
    screen.fill(blue)
    pygame.display.update()
 

def update():
    global score,beams,running,highscore,highscoretxt
    screen.fill(blue)

    player.update(auto)
    if auto:
        AI.update(player, beams)

    for beam in beams:
        beam.update()
        if beam.x < player.x-100:
            beams.remove(beam)
            beams.append(Beam(beams[1].x + (50 * randint(6,10)),randint(100,450)))

    ground.update()

    screen.blit(scorefont.render('Score: '+str(score), True, white), (400, 720))

    if (beams[0].x-180 < player.x < beams[0].x and not beams[0].height + 30 < player.y < beams[0].height + 200) or player.y >= 650:
        Controls.paused = True

        if score > highscore and not auto:
            highscore = score
            highscoretxt = open("highscore.txt", 'w')
            highscoretxt.write(str(highscore))
            highscoretxt.close()

        menu = RestartMenu()
        menu.update(auto)

        while Controls.paused and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 450 < event.pos[0] < 540 and 400 < event.pos[1] < 500:
                        reset()

                        del menu

            pygame.time.delay(50)

    elif beams[0].x - 60 < player.x < beams[0].x - 50:
        score += 1

    pygame.display.update((400, 720), (451, 721))


menu = StartMenu()
while not menu.playButtonPressed and running:
    menu.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(100)

auto = menu.auto
del menu

clock = pygame.time.Clock()

while running:
    update()
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(50)

pygame.display.quit()
pygame.quit()
quit()
