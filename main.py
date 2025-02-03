import pygame
import constants as CONST
from circleshape import CircleShape


def main():
    print("Starting asteroids!")
    print(f"Screen width: {CONST.SCREEN_WIDTH}")
    print(f"Screen height: {CONST.SCREEN_HEIGHT}")

    numpass, numfail = pygame.init()
    print(f"init: {pygame.get_init()}  numpass: {numpass}  numfail: {numfail}")

    screen = pygame.display.set_mode((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    circle = CircleShape(0, 0, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
