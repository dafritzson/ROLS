import pygame
from pygame.sprite import Sprite
from program_variables import program_data as pd, settings



class MapEntity(Sprite):
	def __init__(self, x, y):
		super(MapEntity, self).__init__()
		self.x = x
		self.y = y
		self.image = None
		self.rect = None

	def blitme(self):
		pass



class PhysicalMapEntity(MapEntity):
	def __init__(self, x, y):
		super().__init__(x, y)

		self.level_map = pd.level_map
		self.screen = settings.screen
		self.tile_size = settings.tile_size
		self.collisions = pd.collisions

	def blitme(self):
		self.rect.x = self.x
		self.rect.y = self.y
		self.screen.display.blit(self.image, self.rect)

class Carpet(PhysicalMapEntity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
		self.rect = self.image.get_rect()


	

		