import pygame

class Screen():
	'''A class for all attributes and fucntions related to the game screen'''
	def __init__(self, settings):
		self.width =  900
		self.height = 600
		self.settings = settings
		self.display = pygame.display.set_mode(size=(self.width, self.height))
		self.rect = self.display.get_rect()


	def fill(self):
		self.display.fill(self.settings.bg_color)
