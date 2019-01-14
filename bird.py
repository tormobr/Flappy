import pygame
class Bird:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y

		self.rect = pygame.Rect(x, y, width, height)

	def move(self, movement):
		self.y += movement
		self.rect.top = self.y