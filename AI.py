import pygame
import Controls

pygame.init()

def update(player,beams:list):
    if player.x < beams[0].x:
        if player.y > beams[0].height+120:
            Controls.jump = True
        else:
            Controls.jump = False
    else:
        if player.y > beams[1].height+120:
            Controls.jump = True
        else:
            Controls.jump = False
