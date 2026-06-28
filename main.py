import pygame
from constants import *
from logger import log_state

def main():
    pygame.init()
    # print info
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'''Screen width: {SCREEN_WIDTH}
Screen height: {SCREEN_HEIGHT}''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        # Loop constantly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # Draw background
            screen.fill("black")
            # Refresh
            pygame.display.flip()

if __name__ == "__main__":
    main()
