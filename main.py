import pygame
import random
from constants import * 
from player import *
from asteroidfield import *
from circleshape import *

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots_group = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, shots_group)
    asteroid_field = AsteroidField()


    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        
        for u in updatable:
            u.update(dt)
        
        for a in asteroids:
            if a.collision_check(player) == True:
                print("Game over!")
                raise SystemExit

        for a in asteroids:
            for s in shots_group:
                if s.collision_check(a):
                    s.kill()
                    a.split()

        
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        

        #limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        











if __name__ == "__main__":
    main()