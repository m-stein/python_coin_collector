import pygame
import numpy as np

def vector2_normalize(vector2):
    norm = np.linalg.norm(vector2)
    if norm == 0:
        return vector2
    return vector2 / norm

def vector2_length(vector2):
    return np.linalg.norm(vector2)

class Player:

    def __init__(self, x, y, move_area_width, move_area_height):
        self.collider = None
        self.pos = np.array([float(x), float(y)])
        self.move_area_width = move_area_width
        self.move_area_height = move_area_height
        self.width = 20
        self.height = 20
        self.speed = 200
        self.color = (100, 120, 100)
        self.update_collider()

    def velocity(self, delta_time):
        return self.speed * delta_time

    def update(self, delta_time, coins):
        key_pressed = pygame.key.get_pressed()

        direction = np.array([0., 0.])
        if key_pressed[pygame.K_UP]:
            direction[1] -= 1
        if key_pressed[pygame.K_DOWN]:
            direction[1] += 1
        if key_pressed[pygame.K_LEFT]:
            direction[0] -= 1
        if key_pressed[pygame.K_RIGHT]:
            direction[0] += 1

        if vector2_length(direction) > 0:
            self.pos += vector2_normalize(direction) * self.velocity(delta_time)
            self.update_collider()
            for coin in coins:
                if self.collider.colliderect(coin.collider):
                    coin.spawn()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.pos[0], self.pos[1], self.width, self.height))

    def update_collider(self):
        self.collider = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
