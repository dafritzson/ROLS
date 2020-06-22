import pygame

class Menu():
	'''top level class of all menu types'''
	def __init__(self, settings, screen, player):
		self.screen = screen
		self.settings = settings
		self.player = player


		#Default Menu locations
		self.width = 400
		self.height = 300
		self.color = (255, 255, 255)

		self.menu_left = self.screen.rect.centerx - self.width/2
		self.menu_top = self.screen.rect.centery - self.height/2

		#Load menu
		self.menu_rect = pygame.Rect(self.menu_left, self.menu_top, self.width, self.height)


	def blitme(self):
		'''draw the menu rectangles to the screen'''
		pygame.draw.rect(self.screen, self.color, self.menu_rect)


class MainMenu(Menu):
	'''Beginning Menu'''
	def __init__(self, settings, screen, player):
		super().__init__(settings, screen, player)

		#Define the main menu rectangles
		self.newgame_image = pygame.image.load('.\\Images\\Menu\\New Game.png')
		self.newgame_image = pygame.transform.scale(self.newgame_image, (150, 40))	
		self.newgame_rect = self.newgame_image.get_rect()
		self.newgame_rect.centerx = self.screen.rect.centerx
		self.newgame_rect.y = self.screen.rect.y + 200

		self.continuegame_image = pygame.image.load('.\\Images\\Menu\\Continue Game.png')
		self.continuegame_image = pygame.transform.scale(self.continuegame_image, (150, 40))
		self.continuegame_rect = self.continuegame_image.get_rect()
		self.continuegame_rect.centerx  = self.screen.rect.centerx
		self.continuegame_rect.y = self.screen.rect.y + 300

	def blitme(self):
		'''draw the menu rectangles to the screen'''
		pygame.draw.rect(self.screen.display, (255, 255, 255), self.menu_rect)
		self.screen.display.blit(self.newgame_image, self.newgame_rect)
		self.screen.display.blit(self.continuegame_image, self.continuegame_rect)

class GameMenu(Menu):
	'''In-game menu'''
	def __init__(self, settings, screen, player):
		super().__init__(settings, screen, player)

		self.menu_left = self.screen.rect.centerx - self.width/2
		self.menu_top = self.screen.rect.centery - self.height/2

		#Define the main menu rectangles
		self.newgame_image = pygame.image.load('.\\Images\\Menu\\New Game.png')
		self.newgame_image = pygame.transform.scale(self.newgame_image, (150, 40))	
		self.newgame_rect = self.newgame_image.get_rect()
		self.newgame_rect.centerx = self.screen.rect.centerx
		self.newgame_rect.y = self.screen.rect.y + 200

		self.continuegame_image = pygame.image.load('.\\Images\\Menu\\Continue Game.png')
		self.continuegame_image = pygame.transform.scale(self.continuegame_image, (150, 40))
		self.continuegame_rect = self.continuegame_image.get_rect()
		self.continuegame_rect.centerx  = self.screen.rect.centerx
		self.continuegame_rect.y = self.screen.rect.y + 300

	def blitme(self):
		'''draw the menu rectangles to the screen'''
		pygame.draw.rect(self.screen, (255, 255, 255), self.menu_rect)
		self.screen.dsiplay.blit(self.newgame_image, self.newgame_rect)
		self.screen.dispaly.blit(self.continuegame_image, self.continuegame_rect)