import pygame
import player
import coin
import score


class Game:

    def __init__(self, num_coins):
        pygame.init()
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
        self.score = score.Score()
        self.player = player.Player(25, 2, self.window_width, self.window_height, self.score, self.coins)

    def run(self):
        running = True
        while running:

            # block next frame if fps would exceed max_fps and, when unblocking,
            # determine time since last frame in seconds
            delta_time = self.clock.tick(self.max_fps) / 1000

            # handle global user input
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        running = False
                    case pygame.KEYDOWN:
                        match event.key:
                            case pygame.K_ESCAPE:
                                running = False

            # update objects
            self.player.update(delta_time)
            for curr_coin in self.coins:
                curr_coin.update(delta_time)
            self.score.update(delta_time)

            # draw to window surface
            self.window.fill(self.background_color)
            self.player.draw(self.window)
            for curr_coin in self.coins:
                curr_coin.draw(self.window)
            self.score.draw(self.window)

            pygame.display.update()

        pygame.quit()
