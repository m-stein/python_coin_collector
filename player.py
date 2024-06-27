import pygame
import vpython as vp
import animation


class Player:

    def __init__(self, x, y, move_area_width, move_area_height, score, coins):
        self.collider = None
        self.pos = vp.vector(x, y, 0)
        self.move_area_width = move_area_width
        self.move_area_height = move_area_height
        self.width = 20
        self.height = 20
        self.speed = 200
        self.score = score
        self.coins = coins
        self.sprite_scale = 2
        self.sprite = pygame.image.load("content/player_standing_down.png").convert_alpha()
        self.sprite = pygame.transform.scale(
            self.sprite,
            (self.sprite.get_width() * self.sprite_scale, self.sprite.get_height() * self.sprite_scale))
        self.sprite_scaled_size = vp.vector(self.sprite.get_width(), self.sprite.get_height(), 0) * self.sprite_scale
        self.collider_offset = vp.vector(8, 16, 0) * self.sprite_scale
        self.collider_size = vp.vector(17, 14, 0) * self.sprite_scale
        self.animation = animation.Animation(vp.vector(32, 32, 0) * self.sprite_scale, 4, 0.5)
        self.update_collider()

    def velocity(self, delta_time):
        return self.speed * delta_time

    def update(self, delta_time):
        self.animation.update(delta_time)
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
            min_x = -self.collider_offset.x
            if self.pos.x < min_x:
                self.pos.x = min_x
            min_y = -self.collider_offset.y
            if self.pos.y < min_y:
                self.pos.y = min_y
            max_x = self.move_area_width - self.collider_offset.x - self.collider_size.x
            if self.pos.x > max_x:
                self.pos.x = max_x
            max_y = self.move_area_height - self.collider_offset.y - self.collider_size.y
            if self.pos.y > max_y:
                self.pos.y = max_y

            self.update_collider()
            for coin in self.coins:
                if self.collider.colliderect(coin.collider):
                    coin.spawn()
                    self.score.increment()

    def draw(self, surface):
        surface.blit(self.sprite, (self.pos.x, self.pos.y), self.animation.frame_rectangle())

    def update_collider(self):
        self.collider = pygame.Rect(
            self.pos.x + self.collider_offset.x,
            self.pos.y + self.collider_offset.y,
            self.collider_size.x,
            self.collider_size.y)
