import pygame
from constants import *
from logger import log_state

def main():
    pygame.init()
    # Time vars
    clock = pygame.time.Clock()
    dt = 0.0
    # print info
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'''Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Loop constantly
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
         # Draw background
        screen.fill("black")
        # Refresh
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
