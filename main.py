import pygame
from pygame.locals import *
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")
    pygame_init = pygame.init()
    if pygame_init[1] != 0:
        print(f"Initialized {pygame_init[0]}/{pygame_init[0] + pygame_init[1]} pygame modules")
    clock_object = pygame.time.Clock()
    dt = 0 # time delta since .tick() was last called
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2) 


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock_object.tick(60) / 1000


if __name__ == "__main__":
    main()
