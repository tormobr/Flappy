import os
import pygame
from bird import Bird

WHITE = (255,255,255)
LIGHT_BLUE = (135, 200, 250)
RED = (255, 0, 0)
G = 1
class Game:
    
    def __init__(self):
        self.player = Bird(100,100, 10, 10)
        self.speed = 0

    def play(self):
        print("STARTING GAME!!")
        # Initialise pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        # Set up the display
        pygame.display.set_caption("FLAPPY-BIRD")
        screen = pygame.display.set_mode((570, 660))

        clock = pygame.time.Clock()




        running = True
        while running:
            
            clock.tick(60)
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                    if e.key == pygame.K_SPACE:
                        self.speed = -10

            self.speed += G*0.4
            self.player.move(self.speed)


            screen.fill(LIGHT_BLUE)

            pygame.draw.rect(screen, RED, self.player.rect)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.play()
