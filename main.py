import pygame

pygame.init()

window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width,window_height))
background_color = (50, 45, 50)
window.fill(background_color)
clock = pygame.time.Clock()
running = True
show_rect = False;
max_fps = 60
player_x = 32
player_y = 32
player_speed = 150

while running:
    # block next frame if fps would exceed max_fps and, when unblocking,
    # determine time since last frame in seconds
    delta_time = clock.tick(max_fps) / 1000
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        running = False

    key_pressed = pygame.key.get_pressed()
    velocity = player_speed * delta_time
    if key_pressed[pygame.K_RIGHT]:
        player_x += velocity
    if key_pressed[pygame.K_LEFT]:
        player_x -= velocity
    if key_pressed[pygame.K_UP]:
        player_y -= velocity
    if key_pressed[pygame.K_DOWN]:
        player_y += player_speed * delta_time

    window.fill(background_color)
    pygame.draw.rect(window, "green", (player_x, player_y, 20, 20))
    pygame.display.update()

pygame.quit()