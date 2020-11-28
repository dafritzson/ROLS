import pygame
from pygame.sprite import Sprite

class MapEntity(Sprite):
	def __init__(self, x, y):
		super(MapEntity, self).__init__()
		self.x = x
		self.y = y
		self.image = None
		self.rect = None

	def blitme(self):
		pass

class GoldenMapTile(MapEntity):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.image = pygame.image.load('.\\Images\\Maps\\golden_tile.png')
		self.rect = self.image.get_rect()

class PhysicalMapEntity(MapEntity):
	def __init__(self, x, y, program_data):
		super().__init__(x, y)

		self.program_data = program_data
		self.level_map = self.program_data.level_map
		self.screen = self.program_data.screen

	def blitme(self):
		self.rect.x = self.x
		self.rect.y = self.y
		self.screen.display.blit(self.image, self.rect)

class Carpet(PhysicalMapEntity):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)
		self.image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
		self.rect = self.image.get_rect()


	

		