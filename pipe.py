import random
import pygame
class Pipe:
	def __init__(self, x, space, screen_height, height, width):
		self.top_image = pygame.transform.scale(pygame.image.load('static/pipe.png'),(width, height))
		initial_pos = -(self.top_image.get_rect().height - screen_height//2) - 200
		initial_pos += random.randrange(200)	

		self.top_rect = pygame.Rect(x,initial_pos ,width, self.top_image.get_rect().height)

		self.bottom_image = pygame.transform.scale(pygame.image.load('static/pipe.png'),(width, height))
		self.bottom_rect = pygame.Rect(x, initial_pos + self.top_rect.height + space, 70, 400)

	def move(self, speed):
		self.top_rect.x -= speed
		self.bottom_rect.x -= speed

