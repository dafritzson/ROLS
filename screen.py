import pygame

class Screen():
	'''A class for all attributes and fucntions related to the game screen'''
	def __init__(self, settings):
		self.settings = settings
		self.width =  self.settings.tile_size*12
		self.height = self.settings.tile_size*12
		self.display = pygame.display.set_mode(size=(self.width, self.height))
		self.rect = self.display.get_rect()


	def fill(self):
		self.display.fill(self.settings.bg_color)
