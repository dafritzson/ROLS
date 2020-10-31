import pygame

class Screen():
	'''A class for all attributes and fucntions related to the game screen'''
	def __init__(self, program_data):
		self.program_data = program_data
		self.bg_color = (3,181,133)
		self.bg_color_battle = (230, 230, 230)
		self.width =  self.program_data.tile_size*12
		self.height = self.program_data.tile_size*12
		self.display = pygame.display.set_mode(size=(self.width, self.height))
		self.rect = self.display.get_rect()


	def fill(self):
		self.display.fill(self.bg_color)

	def fill_battle(self):
		self.display.fill(self.bg_color_battle)

