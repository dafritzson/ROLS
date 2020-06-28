import pygame

class DisplayBox():
	'''class to define the display box at the bottom of the screen'''
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings
		
		#FOnt settings
		self.text_color = (4,65,33)
		self.font = pygame.font.SysFont('calibri', 20)

		self.color = (240, 240, 240)

		#Default display box locations
		self.width = self.screen.rect.width
		self.height = self.screen.rect.height / 5

		self.left = 0
		self.top = self.screen.rect.bottom - self.height

		#Load dsiplay box
		self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
		self.message = "hello the_Guy"
		
		self.prep_message()


	def prep_message(self):
		'''prep the dislay box image'''

		self.message_image = self.font.render(self.message, True, self.text_color, self.color)

		#Display message in the display box
		self.message_rect = self.message_image.get_rect()
		self.message_rect.centerx = self.rect.centerx
		self.message_rect.top = self.rect.centery

	def blitme(self):
		'''draw the display box rectangles to the screen'''
		pygame.draw.rect(self.screen.display, self.color, self.rect)
		self.screen.display.blit(self.message_image, self.message_rect)