import pygame
import vpython as vp

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
        self.frame = 0
        self.frame_width = 32 * self.sprite_scale
        self.frame_height = 32 * self.sprite_scale
        self.frame_duration = 0.5
        self.frame_time = 0.
        self.num_frames = 4
        self.sprite_scaled_size = vp.vector(self.sprite.get_width(), self.sprite.get_height(), 0) * self.sprite_scale
        self.collider_offset = vp.vector(8, 16, 0) * self.sprite_scale
        self.collider_size = vp.vector(17, 14, 0) * self.sprite_scale
        self.update_collider()

    def draw_frame(self, surface, frame, destination):
        surface.blit(
            self.sprite, (destination.x, destination.y),
            (frame * self.frame_width, 0, self.frame_width, self.frame_height))

    def velocity(self, delta_time):
        return self.speed * delta_time

    def update(self, delta_time):
        self.frame_time += delta_time
        self.frame = (self.frame + int(self.frame_time / self.frame_duration)) % self.num_frames
        self.frame_time %= self.frame_duration

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
            for coin in self.coins:
                if self.collider.colliderect(coin.collider):
                    coin.spawn()
                    self.score.increment()

    def draw(self, surface):
        self.draw_frame(surface, self.frame, self.pos)

    def update_collider(self):
        self.collider = pygame.Rect(
            self.pos.x + self.collider_offset.x,
            self.pos.y + self.collider_offset.y,
            self.collider_size.x,
            self.collider_size.y)
