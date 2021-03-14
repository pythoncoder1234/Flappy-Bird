import Controls,pygame

pygame.init()

class PlayerBird:
    def __init__(self,x,y):
        import main
        self.x = x
        self.y = y
        self.Y_change = -1

        self.screen = main.screen
        self.bird = main.bird
        self.score = main.score

    def update(self):
        try:
            Controls.test()

            if not Controls.paused:
                self.x += 5
                if Controls.jump and self.y > 100:
                    self.Y_change = 12

                self.Y_change -= 1
                self.y -= self.Y_change

                self.screen.fill((112, 197, 206))
                self.screen.blit(self.bird,(100,self.y))
                pygame.display.update((100,self.y+self.Y_change),(105,self.y+self.Y_change))

        except pygame.error:
            quit()
