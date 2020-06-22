import pygame

class LevelMap():
	def __init__(self, settings, screen):
		self.screen = screen
		self.screen_rect = self.screen.rect
		self.settings = settings

		self.image=pygame.image.load('.\\Images\\Map\\test_map.png')
		self.rect=self.image.get_rect()

		#position
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery 

	def blitme(self):
		self.screen.display.blit(self.image, self.rect)