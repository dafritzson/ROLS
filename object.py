'''
import pygame
from pygame.sprite import Sprite


class Object(Sprite):
	def __init__(self, screen, settings):
		super(Object, self).__init__()
		self.screen = screen
		self.settings = settings

		#Load Image
		self.image = pygame.image.load('.\\Images\\Objects\\desk.png')
		self.image = pygame.transform.scale(self.image, (110, 80))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()

		#position
		self.rect.x = self.screen_rect.centerx + 150
		self.rect.y = self.screen_rect.centery - 100

	def blitme(self):
		self.screen.blit(self.image, self.rect)


'''
