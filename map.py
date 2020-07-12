import pygame
from pygame.sprite import Sprite

class MapEntity(Sprite):
	def __init__(self, x, y, settings, screen):
		super(MapEntity, self).__init__()
		self.x = x
		self.y = y
		self.settings = settings
		self.screen = screen
		self.image = None
		self.rect = None

	def blitme(self):
		#self.level_map.image.blit(self.image, self.rect)
		self.rect.x = self.x
		self.rect.y = self.y
		self.screen.display.blit(self.image, self.rect)

class Carpet(MapEntity):
	def __init__(self, x, y, settings, screen):
		super().__init__(x, y, settings, screen)
		self.image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
		self.rect = self.image.get_rect()

class GoldenMapTile(MapEntity):
	def __init__(self, x, y, settings, screen):
		super().__init__(x, y, settings, screen)
		self.image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
		self.rect = self.image.get_rect()
	
	#def blitme(self):
		#pass

		