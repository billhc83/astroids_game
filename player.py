from circleshape import CircleShape
import pygame
import main
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)
        self.rotation = 0
        self.__x = x
        self.__y = y

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle())
    
