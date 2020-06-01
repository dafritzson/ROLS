import pygame
from pygame.sprite import Sprite


class Barrier(Sprite):
	def __init__(self, screen, settings, x, y):
		super(Barrier, self).__init__()
		self.screen = screen
		self.settings = settings
		self.x = x
		self.y = y

		#self.rect = pygame.rect(self.x, self.y, self.settings.tile_size, self.settings.tile_size)
		#self.screen_rect = self.screen.get_rect()

		self.image = pygame.image.load('.\\Images\\Map\\Carpet.png')
		self.rect = self.image.get_rect()

		#position
		self.rect.x = self.x
		self.rect.y = self.y



class Object(Barrier):
	def __init__(self ,screen, settings, x, y):
		super().__init__(screen, settings, x, y)

		#Load Image
		self.image = pygame.image.load('.\\Images\\Objects\\desk.png')
		self.image = pygame.transform.scale(self.image, (110, 80))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		#position
		self.rect.x = self.x
		self.rect.y = self.y

	def blitme(self):
		self.screen.blit(self.image, self.rect)
