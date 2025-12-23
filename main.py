import pygame
import constants
import player
from logger import log_state
def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.time.Clock
    dt = 0 
    player1 = player.Player( constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,constants.PLAYER_RADIUS)
    while True:
        log_state()
        screen.fill("black")
        player1.draw(screen)
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
