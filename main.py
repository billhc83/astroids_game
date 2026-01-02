import sys
import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_RADIUS
import player
from logger import log_state
import asteroid
import asteroidfield
from logger import log_event
import circleshape
import shot
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shot.Shot.containers = (shots, updatable, drawable)
    player.Player.containers = (updatable, drawable) 
    asteroid.Asteroid.containers = (asteroids,updatable,drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    player1 = player.Player( SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    asteroid1 = asteroidfield.AsteroidField()
    
    dt = 0
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)  
        for a in asteroids:
            if circleshape.CircleShape.collides_with(player1, a) == True:
                print(circleshape.CircleShape.collides_with(player1, a))
                log_event("player_hit")
                print("game over")
                sys.exit()
        for a in asteroids:
            for s in shots:
                if circleshape.CircleShape.collides_with(s, a) == True:
                    log_event("asteroid_shot")
                    asteroid.Asteroid.split(a)
                    pygame.sprite.Sprite.kill(s)
            
        screen.fill("black")

        for d in drawable:
            d.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
