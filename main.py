import sys
import pygame
from pygame.locals import *
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")

    pygame_init = pygame.init()
    if pygame_init[1] != 0:
        print(f"Initialized {pygame_init[0]}/{pygame_init[0] + pygame_init[1]} pygame modules")

    clock_object = pygame.time.Clock()
    dt = 0 # initial time delta since .tick() was last called

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create groups and add classes to groups via 'containers' attribute
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    player_shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (all_asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (player_shots, updatable, drawable)

    # initialize player and asteroidfield objects
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock_object.tick(60) / 1000
        updatable.update(dt)
        for asteroid_obj in all_asteroids:
            if asteroid_obj.detect_collision(player):
                print("Game over!")
                sys.exit()
            for bullet in player_shots:
                if bullet.detect_collision(asteroid_obj):
                    bullet.kill()
                    asteroid_obj.kill()
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()



if __name__ == "__main__":
    main()
