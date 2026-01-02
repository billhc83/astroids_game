import pygame
from circleshape import CircleShape
import main
import constants
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity*dt

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_num  = random.uniform(20, 50)
            new_vector_1  = self.velocity.rotate(random_num)
            new_vector_2 = self.velocity.rotate(-random_num)
            new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_2 = Asteroid(self.position[0], self.position[1], new_radius)
            new_asteroid_1.velocity = new_vector_1 * 1.2
            new_asteroid_2.velocity =  new_vector_2 * 1.2