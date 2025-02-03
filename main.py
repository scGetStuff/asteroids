import pygame
import constants as CONST


def main():
    print("Starting asteroids!")
    print(f"Screen width: {CONST.SCREEN_WIDTH}")
    print(f"Screen height: {CONST.SCREEN_HEIGHT}")

    numpass, numfail = pygame.init()
    print(f"init: {pygame.get_init()}  numpass: {numpass}  numfail: {numfail}")

    screen = pygame.display.set_mode((CONST.SCREEN_WIDTH, CONST.SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0)
        pygame.display.flip()


if __name__ == "__main__":
    main()
