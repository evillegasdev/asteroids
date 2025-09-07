import pygame
from pygame.locals import *
from constants import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\n"
          f"Screen height: {SCREEN_HEIGHT}")
    pygame_init = pygame.init()
    if pygame_init[1] != 0:
        print(f"Initialized {pygame_init[0]}/{pygame_init[0] + pygame_init[1]} pygame modules")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
