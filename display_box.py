import pygame

class DisplayBox():
	'''class to define the display box at the bottom of the screen'''
	def __init__(self, settings, screen):
		self.settings = settings
		self.screen = screen
		
		#Font settings
		self.text_color = (4,65,33)
		self.font = pygame.font.SysFont('calibri', 20)

		self.color = (240, 240, 240)

		#Default display box locations
		self.width = self.screen.rect.width
		self.height = self.settings.tile_size*3

		self.left = self.screen.rect.left
		self.top = self.screen.rect.bottom - self.height

		self.rect = pygame.Rect(self.left, self.top, self.width, self.height)
		self.messages = {
		'intro' : "hello the_Guy", 
		'NPC_girl' : "Welcome to the office",
		'desk' : "This is my desk",
		'item_report_1' : "You found a level 1 BitCorp Report",
		'coffee_machine' : "Enjoy your brew"
		}
		self.message_to_write = "Hello the_Guy"

		#Dynamic Attributes
		self.visible = False
		self.message_key = 'intro'
		
		self.prep_message()


	def prep_message(self):
		self.message_to_write = self.messages.get(self.message_key)

	def blitme(self):
		'''prep the dislay box image'''
		self.message_image = self.font.render(self.message_to_write, True, self.text_color, self.color)


		#Display message in the display box
		self.message_rect = self.message_image.get_rect()
		self.message_rect.centerx = self.rect.centerx
		self.message_rect.centery = self.rect.centery
		'''draw the display box rectangles to the screen'''
		pygame.draw.rect(self.screen.display, self.color, self.rect)
		self.screen.display.blit(self.message_image, self.message_rect)