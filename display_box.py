import pygame

class DisplayBox():
	'''class to define the display box at the bottom of the screen'''
	def __init__(self, screen, settings):
		self.screen = screen
		self.settings = settings

		self.screen_rect = self.screen.get_rect()
		
		#FOnt settings
		self.text_color = (4,65,33)
		self.font = pygame.font.SysFont('calibri', 20)

		self.box_color = (240, 240, 240)

		#Default display box locations
		self.box_width = self.screen_rect.width
		self.box_height = self.screen_rect.height / 5

		self.box_left = 0
		self.box_top = self.screen_rect.bottom - self.box_height

		#Load dsiplay box
		self.box_rect = pygame.Rect(self.box_left, self.box_top, self.box_width, self.box_height)
		
		self.prep_message()


	def prep_message(self):
		'''prep the dislay box image'''
		message = "hello the_Guy"
		#box_str = "{:,}".format(message)
		self.message_image = self.font.render(message, True, self.text_color, self.box_color)

		#Display message in the display box
		self.message_rect = self.message_image.get_rect()
		self.message_rect.centerx = self.box_rect.centerx
		self.message_rect.top = self.box_rect.centery

	def blitme(self):
		'''draw the display box rectangles to the screen'''
		pygame.draw.rect(self.screen, self.box_color, self.box_rect)
		self.screen.blit(self.message_image, self.message_rect)