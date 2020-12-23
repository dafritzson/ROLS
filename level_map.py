import pygame
from program_variables import settings

class LevelMap():
	def __init__(self):
		self.screen = settings.screen

		self.image = pygame.image.load('.\\Images\\Maps\\Lobby\\Lobby_Test_Wall.png')
		#self.image = pygame.image.load('.\\Images\\Maps\\map_background_test.png')
		self.rect = self.image.get_rect()
		self.rect.x = self.screen.rect.x
		self.rect.y = self.screen.rect.y 

		self.image_overlay = pygame.image.load('.\\Images\\Maps\\Lobby\\Lobby_Test_Art.png')
		#self.image_overlay = pygame.image.load('.\\Images\\Maps\\map_test_overlay.png')
		self.rect_overlay = self.image_overlay.get_rect()
		self.rect_overlay.x = self.screen.rect.x
		self.rect_overlay.y = self.screen.rect.y 

	def blitme(self):
		self.screen.display.blit(self.image, self.rect)
	def blit_overlay(self):
		self.screen.display.blit(self.image_overlay, self.rect_overlay)


