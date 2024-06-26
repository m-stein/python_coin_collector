import pygame
import random

class Coin:
    def __init__(self, spawn_area_width, spawn_area_height):
        self.collider = None
        self.radius = 5
        self.spawn_area_width = spawn_area_width
        self.spawn_area_height = spawn_area_height
        self.spawn()

    def update(self, delta_time):
        pass

    def draw(self, surface):
        pygame.draw.circle(surface, "yellow", (self.x, self.y), self.radius)

    def spawn(self):
        self.x = random.uniform(0, self.spawn_area_width - self.radius * 2)
        self.y = random.uniform(0, self.spawn_area_height - self.radius * 2)
        self.update_collider()

    def update_collider(self):
        self.collider = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
