import pygame
import random
from circleshape import *
from constants import *
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def split(self):
        self.kill()
        log_event("asteroid_split")
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20.00, 50.00)
        vec1 = self.velocity.rotate(random_angle)
        vec2 = self.velocity.rotate(random_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid1.velocity = vec1 * 1.2
        new_asteroid2.velocity = vec2 * 1.2
    def update(self, dt):
        self.position += (self.velocity * dt)