import pygame

class Player:

    def __init__(self):
        self.x = 25
        self.y = 25
        self.width = 20
        self.height = 20
        self.speed = 200
        self.color = (100, 120, 100)

    def velocity(self, delta_time):
        return self.speed * delta_time

    def update(self, delta_time):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.y -= self.velocity(delta_time)
        if key_pressed[pygame.K_DOWN]:
            self.y += self.velocity(delta_time)
        if key_pressed[pygame.K_LEFT]:
            self.x -= self.velocity(delta_time)
        if key_pressed[pygame.K_RIGHT]:
            self.x += self.velocity(delta_time)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
