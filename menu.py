import pygame

class Menu():
	'''top level class of all menu types'''
	def __init__(self, screen, settings, player):
		self.screen = screen
		self.settings = settings
		self.player = player
		self.screen_rect = self.screen.get_rect()

		#Default Menu locations
		self.width = 400
		self.height = 300

		self.menu_left = self.screen_rect.centerx - self.width/2
		self.menu_top = self.screen_rect.centery - self.height/2

		#Load menu
		self.menu_rect = pygame.Rect(self.menu_left, self.menu_top, self.width, self.height)


	def blitme(self):
		'''draw the menu rectangles to the screen'''
		pygame.draw.rect(self.screen, (255, 255, 255), self.menu_rect)


class MainMenu(Menu):
	'''Beginning Menu'''
	def __init__(self, screen, settings, player):
		super().__init__(screen, settings, player)

		#Define the main menu rectangles
		self.newgame_image = pygame.image.load('.\\Images\\Menu\\New Game.png')
		self.newgame_image = pygame.transform.scale(self.newgame_image, (150, 40))	
		self.newgame_rect = self.newgame_image.get_rect()
		self.newgame_rect.centerx = self.screen_rect.centerx
		self.newgame_rect.y = self.screen_rect.y + 200

		self.continuegame_image = pygame.image.load('.\\Images\\Menu\\Continue Game.png')
		self.continuegame_image = pygame.transform.scale(self.continuegame_image, (150, 40))
		self.continuegame_rect = self.continuegame_image.get_rect()
		self.continuegame_rect.centerx  = self.screen_rect.centerx
		self.continuegame_rect.y = self.screen_rect.y + 300

	def blitme(self):
		'''draw the menu rectangles to the screen'''
		pygame.draw.rect(self.screen, (255, 255, 255), self.menu_rect)
		self.screen.blit(self.newgame_image, self.newgame_rect)
		self.screen.blit(self.continuegame_image, self.continuegame_rect)

class GameMenu(Menu):
	'''In-game menu'''
	def __init__(self, screen, settings, player):
		super().__init__(screen, settings, player)

		self.menu_left = self.screen_rect.centerx - self.width/2
		self.menu_top = self.screen_rect.centery - self.height/2

		#Define the main menu rectangles
		self.newgame_image = pygame.image.load('.\\Images\\Menu\\New Game.png')
		self.newgame_image = pygame.transform.scale(self.newgame_image, (150, 40))	
		self.newgame_rect = self.newgame_image.get_rect()
		self.newgame_rect.centerx = self.screen_rect.centerx
		self.newgame_rect.y = self.screen_rect.y + 200

		self.continuegame_image = pygame.image.load('.\\Images\\Menu\\Continue Game.png')
		self.continuegame_image = pygame.transform.scale(self.continuegame_image, (150, 40))
		self.continuegame_rect = self.continuegame_image.get_rect()
		self.continuegame_rect.centerx  = self.screen_rect.centerx
		self.continuegame_rect.y = self.screen_rect.y + 300

	def blitme(self):
		'''draw the menu rectangles to the screen'''
		pygame.draw.rect(self.screen, (255, 255, 255), self.menu_rect)
		self.screen.blit(self.newgame_image, self.newgame_rect)
		self.screen.blit(self.continuegame_image, self.continuegame_rect)