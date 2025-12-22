import pygame
import constants
from logger import log_state
def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.time.Clock
    dt = 0 
    while True:
        log_state()
        screen.fill("black")
        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)
        dt = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}" )
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
