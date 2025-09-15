import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, position_vector, radius= SHOT_RADIUS):
        super().__init__(position_vector[0], position_vector[1], radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

