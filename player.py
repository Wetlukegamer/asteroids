import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # overwrite draw
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    # rotation
    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    # movement
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1) # create vector
        unit_vector = unit_vector.rotate(self.rotation) # rotate vector
        unit_vector = unit_vector * PLAYER_SPEED * dt # add speed
        self.position += unit_vector
    
    # rotation and movement detecion
    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
    
    # provide refrence class for drawing player
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
