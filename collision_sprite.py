import pygame
from pygame.sprite import Sprite


class CollisionSprite(Sprite):
	def __init__(self, x, y):
		super(CollisionSprite, self).__init__()
		self.x = x
		self.y = y
		self.image = pygame.image.load('.\\Images\\Player\\player_test.png')
		self.rect = self.image.get_rect()
		self.rect.x = self.x
		self.rect.y = self.y
