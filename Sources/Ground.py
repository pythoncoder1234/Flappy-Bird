import Controls,pygame

class Ground:
    def __init__(self):
        self.x = 0

        from main import screen,bird
        self.screen = screen
        self.bird = bird

    def update(self):
        if not Controls.paused:
            self.x -= 5
            if self.x == -160:
                self.x = 0

        for i in range(15):
            pygame.draw.rect(self.screen,(30, 132, 73),(self.x+(i*80),700,80,20))
            pygame.draw.rect(self.screen,(39, 174, 96),(self.x+2+(i*80),702,76,16))

        pygame.draw.rect(self.screen,(243, 156, 18),(0,720,1000,100))
        pygame.display.update((0,700),(1000,800))
