import pygame

class LevelMap():
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load('.\\Images\\Maps\\Lobby\\Lobby_Test_Wall.png')
		self.rect = self.image.get_rect()
		self.rect.x = self.screen.rect.x
		self.rect.y = self.screen.rect.y 

		self.image_overlay = pygame.image.load('.\\Images\\Maps\\Lobby\\Lobby_Test_Art.png')
		self.rect_overlay = self.image_overlay.get_rect()
		self.rect_overlay.x = self.screen.rect.x
		self.rect_overlay.y = self.screen.rect.y 

	def blitme(self):
		self.screen.display.blit(self.image, self.rect)
	def blit_overlay(self):
		self.screen.display.blit(self.image_overlay, self.rect_overlay)

	def round_to_tileset(self, value_to_round):
		self.value_to_round = value_to_round
		return self.settings.tile_size * round(self.value_to_round / self.settings.tile_size)
