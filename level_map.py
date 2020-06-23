import pygame

class LevelMap():
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings

		self.image = pygame.image.load('.\\Images\\Map\\test_map.png')
		self.rect = self.image.get_rect()

		#position
		self.rect.centerx = self.screen.rect.centerx
		self.rect.centery = self.screen.rect.centery 

	#def move_map_right(self):
	#	self.rect.centerx -= self.player.speed

	#def move_map_left(self):
#		self.rect.centerx += self.player.speed

#	def move_map_up(self):
#		self.rect.centery += self.player.speed

#	def move_map_down(self):
#		self.rect.centery -= self.player.speed


	def blitme(self):
		self.screen.display.blit(self.image, self.rect)