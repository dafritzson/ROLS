import pygame
from pygame.sprite import Sprite

class GoldenMapTile(Sprite):
	def __init__(self, x, y):
		super(GoldenMapTile, self).__init__()
		self.x = x
		self.y = y
		self.image = pygame.image.load('.\\Images\\Maps\\golden_tile.png')
		self.rect = self.image.get_rect()


	def blitme(self):
		pass