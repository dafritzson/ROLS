import pygame
from pygame.sprite import Sprite

class MapEntity(Sprite):
	def __init__(self, x, y, settings, screen):
		super(MapEntity, self).__init__()
		self.x = x
		self.y = y
		# centerX and centerY are pixel locations
		self.centerX = 0
		self.centerY = 0
		self.settings = settings
		self.screen = screen
		self.image = None
		self.rect = None

	def blitme(self):
		#self.level_map.image.blit(self.image, self.rect)
		self.rect.x = self.x
		self.rect.y = self.y
		self.screen.display.blit(self.image, self.rect)

class Tile(MapEntity):
	def __init__(self, x, y, settings, screen):
		super().__init__(x, y, settings, screen)
		# tileX and tileY are tile locations based on number of tiles in map
		self.tileX = 0
		self.tileY = 0
		self.walkable = False

class Carpet(Tile):
	def __init__(self, x, y, settings, screen):
		super().__init__(x, y, settings, screen)
		self.image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
		self.rect = self.image.get_rect()
		self.walkable = True

class Wall(Tile):
	def __init__(self, x, y, settings, screen):
		super().__init__(x, y, settings, screen)
		self.image = pygame.image.load('.\\Images\\Maps\\cubicle1.png')
		self.rect = self.image.get_rect()
		self.interactable = False

class GoldenMapTile(MapEntity):
	def __init__(self, x, y, settings, screen):
		super().__init__(x, y, settings, screen)
		self.image = pygame.image.load('.\\Images\\Maps\\carpet_test.png')
		self.rect = self.image.get_rect()


		