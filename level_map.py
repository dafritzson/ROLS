import pygame

class LevelMap():
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load('.\\Images\\Maps\\test_map.png')
		self.rect = self.image.get_rect()

		#position
		self.rect.centerx = self.screen.rect.centerx
		self.rect.centery = self.screen.rect.centery 


	def blitme(self):
		self.screen.display.blit(self.image, self.rect)