import pygame
paused = False
jump = False
prevkey = 'none'

def test():
    try:
        global paused,jump,prevkey
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]:
            if prevkey != 'jump':
                jump = True
                prevkey = 'jump'
            else:
                jump = False

        elif keys[pygame.K_ESCAPE]:
            if prevkey != 'escape':
                paused = not paused
                prevkey = 'escape'

        else:
            prevkey = 'none'
            jump = False

    except pygame.error:
        quit()
