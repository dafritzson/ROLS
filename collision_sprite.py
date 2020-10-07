import pygame
from pygame.sprite import Sprite


class CollisionSprite(Sprite):
	def __init__(self, x, y):
		super(CollisionSprite, self).__init__()
		self.image = pygame.image.load('.\\Images\\Player\\player_test.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
