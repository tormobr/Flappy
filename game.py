import os
import pygame
from bird import Bird
from pipe import Pipe

WHITE = (255,255,255)
LIGHT_BLUE = (135, 200, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
G = 1
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
class Game:
    
    def __init__(self):
        self.player = Bird(100,100, 10, 10)
        self.speed = 0
        self.pipes = [Pipe(300, 120, SCREEN_HEIGHT), Pipe(500, 120, SCREEN_HEIGHT), Pipe(700, 120, SCREEN_HEIGHT)]

    def play(self):
        print("STARTING GAME!!")
        # Initialise pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        # Set up the display
        pygame.display.set_caption("FLAPPY-BIRD")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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

            for pipe in self.pipes:
                pipe.move(3)

            for pipe in self.pipes:
                if pipe.top_rect.x + 70 < 0:
                    self.pipes[0] = self.pipes[1]
                    self.pipes[1] = self.pipes[2]
                    self.pipes[2] = Pipe(self.pipes[1].top_rect.x+200, 100, SCREEN_HEIGHT)

            screen.fill(LIGHT_BLUE)

            pygame.draw.rect(screen, RED, self.player.rect)

            for pipe in self.pipes:
                pygame.draw.rect(screen, GREEN, pipe.top_rect)
                pygame.draw.rect(screen, GREEN, pipe.bottom_rect)
            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.play()
