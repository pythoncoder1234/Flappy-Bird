import pygame

class Beam:
    def __init__(self, x, height):
        from main import screen, player
        self.player = player
        self.x = x
        self.height = height
        self.screen = screen

    def update(self):
        self.screen.fill((112, 197, 206))

        if self.x - self.player.x > 0:
            green = (88, 214, 141)
            black = (0, 0, 0)

            # The drawing process
            pygame.draw.rect(self.screen, black, (self.x - self.player.x - 1, 0, 52, self.height + 2))       # Top vertical rectangle outline
            pygame.draw.rect(self.screen, green, (self.x - self.player.x, 0, 50, self.height))               # Top vertical rectangle
            pygame.draw.rect(self.screen, black, (self.x - self.player.x - 26, self.height - 1, 103, 33))    # Top horizontal rectangle outline
            pygame.draw.rect(self.screen, green, (self.x - self.player.x - 25, self.height, 100, 30))        # Top horizontal rectangle
            pygame.display.update((self.x - self.player.x - 50, 0), (self.x - self.player.x + 150, self.height + 33))
            pygame.draw.rect(self.screen, black,                                                             # Bottom vertical rectangle outline
                             (self.x - self.player.x - 1, self.height + 224, 52, 702 - (self.height + 149)))
            pygame.draw.rect(self.screen, green,                                                             # Bottom vertical rectangle
                             (self.x - self.player.x, self.height + 225, 50, 700 - (self.height + 150)))
            pygame.draw.rect(self.screen, black, (self.x - self.player.x - 26, self.height + 199, 103, 33))  # Bottom horizontal rectangle outline
            pygame.draw.rect(self.screen, green, (self.x - self.player.x - 25, self.height + 200, 100, 30))  # Bottom horizontal rectangle
            pygame.display.update((self.x - self.player.x - 50, self.height + 199), (self.x - self.player.x + 150, 700-self.height))

        else:
            pygame.display.update((self.x - self.player.x - 50, 0), (self.x - self.player.x + 150, 700))
