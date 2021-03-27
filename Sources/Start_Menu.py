import pygame
from Ground import Ground
from Beam import Beam

class StartMenu:
    def __init__(self):  # Draws the menu
        try:
            import main
            self.screen = main.screen
            self.blue = (78,193,202)
            self.title = pygame.image.load('Sources/images/title.png').convert()
            self.bird = main.bird
            self.bird = pygame.transform.scale(self.bird,(120,100))
            self.playButtonPressed = False
            self.font = pygame.font.SysFont('calibri',32,True)

            self.screen.fill(self.blue)

            Beam(800,200).update()
            Ground().update()

            self.screen.blit(self.title,(250,150))
            self.screen.blit(self.bird,(400,300))
            pygame.draw.rect(self.screen,pygame.Color('green'),(400,500,125,50),0,5,5,5,5)
            text = self.font.render('Play',True,pygame.Color('white'))
            self.screen.blit(text,(430,510))

            pygame.display.update()

        except pygame.error:
            quit()

    def update(self):  # Waits until the play button is pressed
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos()
            if 400 < mouse[0] < 520 and 500 < mouse[1] < 550:
                self.playButtonPressed = True
                self.screen.fill((112, 197, 206))
                pygame.display.update()
