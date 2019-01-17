import random
import pygame
class Pipe:
	def __init__(self, x, space, height, width):
		self.top_image = pygame.transform.scale(pygame.image.load('static/pipe.png'), (width ,height))
		self.top_rect = pygame.Rect(x,0,width, random.randrange(height/4, height*3/4))

		self.bottom_image = pygame.transform.scale(pygame.image.load('static/pipe.png'), (width ,height))
		self.bottom_image = pygame.transform.rotate(self.bottom_image, 180)
		self.bottom_rect = pygame.Rect(x, self.top_rect.height+space, 70, 400)

	def move(self, speed):
		self.top_rect.x -= speed
		self.bottom_rect.x -= speed

