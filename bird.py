import pygame
class Bird:
	def __init__(self, x, y, width, height):
		self.image = pygame.transform.scale(pygame.image.load('static/bird.png'), (width ,height))
		self.x = x
		self.y = y

		self.rect = pygame.Rect(x, y, width, height)

	def move(self, movement):
		self.y += movement
		self.rect.top = self.y


	def rot_center(self, angle):
	    """rotate an image while keeping its center"""
	    rot_image = pygame.transform.rotate(self.image, angle)
	    rot_rect = rot_image.get_rect(center=self.rect.center)
	    return rot_image