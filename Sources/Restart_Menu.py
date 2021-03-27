import pygame

class RestartMenu:
    def __init__(self):
        import main
        self.screen = main.screen
        self.font = pygame.font.SysFont('bahnschrift',40)
        self.image = pygame.image.load('Sources/images/restart button.jpg').convert()
        self.image = pygame.transform.scale(self.image,(100,100))

    def update(self):
        import main
        pygame.draw.rect(self.screen,pygame.Color('black'),(350,200,300,400))
        pygame.draw.rect(self.screen,pygame.Color('white'),(351,201,298,398))

        scoretext = self.font.render("Your Score: "+ str(main.score),True,pygame.Color('black'))
        self.screen.blit(scoretext,(380,250))
        scoretext = self.font.render("Highscore: "+str(main.highscore),True,pygame.Color('black'))
        self.screen.blit(scoretext,(380,300))

        self.screen.blit(self.image,(450,400))

        pygame.display.update((350,200),(700,700))
