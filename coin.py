import pygame
import random

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.updateCollider()

    def update(self, delta_time):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, "yellow", (self.x, self.y), self.radius)

    def respawn(self, surface_width, surface_height):
        self.x = random.uniform(0, surface_width - self.radius * 2)
        self.y = random.uniform(0, surface_height - self.radius * 2)
        self.updateCollider()

    def updateCollider(self):
        self.collider = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)