import pygame
import player

class Game:

    def __init__(self):
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.max_fps = 60
        self.background_color = (50, 45, 50)
        self.player = player.Player()
        pygame.init()

    def run(self):
        running = True
        while (running):
            # block next frame if fps would exceed max_fps and, when unblocking,
            # determine time since last frame in seconds
            delta_time = self.clock.tick(self.max_fps) / 1000
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                running = False

            self.player.update(delta_time)
            self.window.fill(self.background_color)
            self.player.draw(self.window)
            pygame.display.update()

        pygame.quit()
