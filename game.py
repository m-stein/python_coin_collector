import pygame
import player
import coin


class Game:

    def __init__(self, num_coins):
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        self.clock = pygame.time.Clock()
        self.max_fps = 60
        self.background_color = (50, 45, 50)
        self.coins = []
        while num_coins:
            self.coins.append(coin.Coin(self.window_width, self.window_height))
            num_coins = num_coins - 1
        self.player = player.Player(25, 2, self.window_width, self.window_height)
        pygame.init()

    def run(self):
        running = True
        while running:
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

            self.player.update(delta_time, self.coins)
            for curr_coin in self.coins:
                curr_coin.update(delta_time)

            self.window.fill(self.background_color)
            self.player.draw(self.window)
            for curr_coin in self.coins:
                curr_coin.draw(self.window)
            pygame.display.update()

        pygame.quit()
