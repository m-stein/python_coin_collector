import pygame
import coin

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.speed = 200
        self.color = (100, 120, 100)

    def velocity(self, delta_time):
        return self.speed * delta_time

    def update(self, delta_time, coins, surface_width, surface_height):
        collider = pygame.Rect(self.x, self.y, self.width, self.height)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.y -= self.velocity(delta_time)
        if key_pressed[pygame.K_DOWN]:
            self.y += self.velocity(delta_time)
        if key_pressed[pygame.K_LEFT]:
            self.x -= self.velocity(delta_time)
        if key_pressed[pygame.K_RIGHT]:
            self.x += self.velocity(delta_time)
        for coin in coins:
            if collider.colliderect(coin.collider):
                coin.respawn(surface_width, surface_height)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
