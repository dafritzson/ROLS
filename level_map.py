import pygame

class LevelMap():
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load('.\\Images\\Maps\\map_test.png')
		self.rect = self.image.get_rect()

		#position
		self.rect.x = self.screen.rect.x
		self.rect.y = self.screen.rect.y 


	def blitme(self):
		self.screen.display.blit(self.image, self.rect)