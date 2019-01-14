import random
import pygame
class Pipe:
	def __init__(self, x, space, height):
		self.top_rect = pygame.Rect(x,0,70, random.randrange(height/4, height*3/4))

		self.bottom_rect = pygame.Rect(x, self.top_rect.height+space, 70, 400)

	def move(self, speed):
		self.top_rect.x -= speed
		self.bottom_rect.x -= speed

