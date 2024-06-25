import pygame
import vpython as vp

class Player:

    def __init__(self, x, y, move_area_width, move_area_height):
        self.collider = None
        self.pos = vp.vector(x, y, 0.)
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

        direction = vp.vector(0., 0., 0.)
        if key_pressed[pygame.K_UP]:
            direction.y -= 1
        if key_pressed[pygame.K_DOWN]:
            direction.y += 1
        if key_pressed[pygame.K_LEFT]:
            direction.x -= 1
        if key_pressed[pygame.K_RIGHT]:
            direction.x += 1

        if direction.mag > 0:
            self.pos += direction.norm() * self.velocity(delta_time)
            if self.pos.x < 0:
                self.pos.x = 0
            if self.pos.y < 0:
                self.pos.y = 0
            max_x = self.move_area_width - self.width
            if self.pos.x > max_x:
                self.pos.x = max_x
            max_y = self.move_area_height - self.height
            if self.pos.y > max_y:
                self.pos.y = max_y

            self.update_collider()
            for coin in coins:
                if self.collider.colliderect(coin.collider):
                    coin.spawn()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.pos.x, self.pos.y, self.width, self.height))

    def update_collider(self):
        self.collider = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
