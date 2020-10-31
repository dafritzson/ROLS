import pygame
from pygame.sprite import Sprite

class MapEntity(Sprite):
	def __init__(self, x, y, program_data, screen):
		super(MapEntity, self).__init__()
		self.x = x
		self.y = y
		self.program_data = program_data
		self.screen = screen
		self.image = None
		self.rect = None

	def blitme(self):
		self.rect.x = self.x
		self.rect.y = self.y
		self.screen.display.blit(self.image, self.rect)


class Carpet(MapEntity):
	def __init__(self, x, y, program_data, screen):
		super().__init__(x, y, program_data, screen)
		self.image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
		self.rect = self.image.get_rect()

class GoldenMapTile(MapEntity):
	def __init__(self, x, y, program_data, screen):
		super().__init__(x, y, program_data, screen)
		self.image = pygame.image.load('.\\Images\\Maps\\golden_tile.png')
		self.rect = self.image.get_rect()
	

		