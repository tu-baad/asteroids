import pygame
from constants import * 

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=000)
        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000
        print(dt)
        











if __name__ == "__main__":
    main()