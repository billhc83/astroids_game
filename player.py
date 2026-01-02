from circleshape import CircleShape
import pygame
import main
import constants
import shot
class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__( x, y, radius)
        self.rotation = 0
        self.__x = x
        self.__y = y
        self.cooldown_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle())

    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if self.cooldown_timer >= 0: 
            self.cooldown_timer -= dt
        else:
            self.cooldown_timer = 0


        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.cooldown_timer == 0:
                self.shoot()    
                self.cooldown_timer = constants.PLAYER_SHOOT_COOLDOWN_SECONDS
               
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * constants.PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    
    def shoot(self):
        shot1 = shot.Shot(self.position[0], self.position[1], constants.SHOT_RADIUS)
        shot_vector = pygame.Vector2(0,1)
        rotated_shot = shot_vector.rotate(self.rotation)
        shot1.velocity = rotated_shot * constants.PLAYER_SHOT_SPEED
        
        