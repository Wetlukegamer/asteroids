import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        init_velocity = self.velocity * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # spawn asteroids
        def new_asteroid() -> "Asteroid":
            return Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1, asteroid_2 = new_asteroid(), new_asteroid()
        # apply velocity
        asteroid_1.velocity = init_velocity.rotate(random_angle)
        asteroid_2.velocity = init_velocity.rotate(-random_angle)
