import pygame
from constants import *
from logger import log_state
from player import Player

def main():
    pygame.init()
    # Time vars
    clock = pygame.time.Clock()
    dt = 0.0
    # print info
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'''Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}''')
    # create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    # manage group-object relations
    Player.containers = (updatable, drawable)
    # create objects
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Loop constantly
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # imput check
        updatable.update(dt)
        # Draw sprites
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        # Refresh
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
