import os
import pygame
from bird import Bird
from pipe import Pipe
import time

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
PIPE_HEIGHT = 500

class Game:
    
    def __init__(self):
        self.player = Bird(100,100, 30, 20)
        self.speed = 0
        self.score = 0
        self.pipes = [Pipe(START_PIPE_X, 120, SCREEN_HEIGHT, PIPE_HEIGHT, PIPE_WIDTH), 
        Pipe(START_PIPE_X + PIPE_DIST, 120, SCREEN_HEIGHT, PIPE_HEIGHT, PIPE_WIDTH), 
        Pipe(START_PIPE_X +PIPE_DIST*2, 120, SCREEN_HEIGHT, PIPE_HEIGHT, PIPE_WIDTH)]

    def play(self):
        print("STARTING GAME!!")
        # Initialise pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()

        # Set up the display
        pygame.display.set_caption("FLAPPY-BIRD")
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        clock = pygame.time.Clock()
        top_back = pygame.image.load('static/top_back.png').convert_alpha()
        bottom_back = pygame.image.load('static/bottom_back.png').convert_alpha()
        bottom_x = [0, bottom_back.get_rect().width-5]

        running = False

        while not running:

        	clock.tick(60)
        	screen.blit(top_back, (0,0))
        	rot_image = self.player.rot_center(-self.speed*2)
        	screen.blit(rot_image, (self.player.rect.x,self.player.rect.y))
        	for pipe in self.pipes:
        		screen.blit(pipe.top_image, (pipe.top_rect.x,pipe.top_rect.y))
        		screen.blit(pipe.bottom_image, (pipe.bottom_rect.x,pipe.bottom_rect.y))
        	screen.blit(bottom_back, (bottom_x[0],top_back.get_rect().height+5))
        	screen.blit(bottom_back, (bottom_x[1],top_back.get_rect().height+5))


        	pygame.display.flip()
	        for e in pygame.event.get():

	            if e.type == pygame.KEYDOWN:
	                if e.key == pygame.K_ESCAPE:
	                    running = False
	                if e.key == pygame.K_SPACE:
	                    self.speed = -7

	                    running =True
	        
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
                running = False

            
            screen.blit(top_back, (0,0))
            rot_image = self.player.rot_center(-self.speed*2)

            screen.blit(rot_image, (self.player.rect.x,self.player.rect.y))


            for pipe in self.pipes:

                screen.blit(pipe.top_image, (pipe.top_rect.x,pipe.top_rect.y))
                screen.blit(pipe.bottom_image, (pipe.bottom_rect.x,pipe.bottom_rect.y))


            font = pygame.font.SysFont("comicsansms", 30)
            text = font.render("Score: " + str(self.score), True, (RED))
            screen.blit(text,(0,0))

            bottom_x[0] -= 2
            bottom_x[1] -= 2
            if bottom_x[0] + bottom_back.get_rect().width < 0:
                tmp = bottom_x[0]
                bottom_x[0] = bottom_x[1]
                bottom_x[1] += bottom_back.get_rect().width-5

            screen.blit(bottom_back, (bottom_x[0],top_back.get_rect().height+5))
            screen.blit(bottom_back, (bottom_x[1],top_back.get_rect().height+5))

            pygame.display.flip()
        self.end(screen)
    def move_items(self):
        self.speed += G
        self.player.move(self.speed)

        for pipe in self.pipes:
            pipe.move(2)

        if self.pipes[0].top_rect.x + PIPE_WIDTH < 0:
            self.pipes[0] = self.pipes[1]
            self.pipes[1] = self.pipes[2]
            self.pipes[2] = Pipe(self.pipes[1].top_rect.x + PIPE_DIST, 120, SCREEN_HEIGHT, PIPE_HEIGHT, PIPE_WIDTH)
            self.score += 1


    def collision(self):
        if self.player.rect.colliderect(self.pipes[0].top_rect) or self.player.rect.colliderect(self.pipes[0].bottom_rect):
            return True
        if self.player.rect.y < 0 or self.player.rect.y > SCREEN_HEIGHT - 150:
            return True
        return False

    def end(self,screen):
        font = pygame.font.SysFont("comicsansms", 80)
        text = font.render("Score: " + str(self.score), True, (WHITE))
        screen.blit(text,(SCREEN_WIDTH/2-50,SCREEN_HEIGHT/2-100))
        pygame.display.flip()
        time.sleep(1)


if __name__ == "__main__":
    game = Game()
    game.play()
