import pygame

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.collider = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, delta_time):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, "yellow", (self.x, self.y, self.width, self.height))
