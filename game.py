import os
import pygame
from bird import Bird
from pipe import Pipe
from network import Network


WHITE = (255,255,255)
LIGHT_BLUE = (135, 200, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
G = 0.4
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600
PIPE_DIST = 200
START_PIPE_X = 300
PIPE_WIDTH = 70

class Game:
    
    def __init__(self):
        self.player = Bird(100,100, 30, 20)
        self.speed = 0
        self.score = 0
        self.pipes = [Pipe(START_PIPE_X, 120, SCREEN_HEIGHT, PIPE_WIDTH), 
        Pipe(START_PIPE_X + PIPE_DIST, 120, SCREEN_HEIGHT, PIPE_WIDTH), 
        Pipe(START_PIPE_X +PIPE_DIST*2, 120, SCREEN_HEIGHT, PIPE_WIDTH)]
        self.net = Network()

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
                        self.speed = -7



            self.move_items()
            if self.collision():
                pass
                running = False

            screen.fill(LIGHT_BLUE)
            print(self.speed)
            
            rot_image = self.player.rot_center(-self.speed*2)

            screen.blit(rot_image, (self.player.rect.x,self.player.rect.y))


            for pipe in self.pipes:

                screen.blit(pipe.top_image, (pipe.top_rect.x,pipe.top_rect.y))
                screen.blit(pipe.bottom_image, (pipe.bottom_rect.x,pipe.bottom_rect.y))


            font = pygame.font.SysFont("comicsansms", 30)
            text = font.render("Score: " + str(self.score), True, (0, 128, 0))
            screen.blit(text,(0,0))

            pygame.display.flip()

    def move_items(self):
        self.speed += G
        self.player.move(self.speed)

        for pipe in self.pipes:
            pipe.move(2)

        if self.pipes[0].top_rect.x + PIPE_WIDTH < 0:
            self.pipes[0] = self.pipes[1]
            self.pipes[1] = self.pipes[2]
            self.pipes[2] = Pipe(self.pipes[1].top_rect.x + PIPE_DIST, 120, SCREEN_HEIGHT, PIPE_WIDTH)
            self.score += 1

    def collision(self):
        if self.player.rect.colliderect(self.pipes[0].top_rect) or self.player.rect.colliderect(self.pipes[0].bottom_rect):
            return True
        if self.player.rect.y < 0 or self.player.rect.y > SCREEN_HEIGHT:
            return True
        return False



if __name__ == "__main__":
    game = Game()
    game.play()
