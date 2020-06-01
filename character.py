import pygame
from pygame.sprite import Sprite

class Character(Sprite):
	def __init__(self, screen, settings, display_box):
		super(Character, self).__init__()
		self.screen = screen
		self.settings = settings
		self.display_box = display_box

		#Character movement states
		self.move_in_progress = False
		self.moving_right = True
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		#Load player image surface and define rectangle
		self.image = pygame.image.load('.\\Images\\Character\\the_girl.png')
		self.image = pygame.transform.scale(self.image, (35, 85))
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.x = 500
		self.rect.y = 100
		#NPC exact position
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def movement(self):

		if self.moving_right:
			print("hi")
			if self.rect.x < 700:
				print("hi")
				self.x += self.settings.character_speed
				print(self.rect.x)
			else:
				self.moving_right = False
				self.moving_down = True
		elif self.moving_down:
			if self.y < 300:
				self.y += self.settings.character_speed
			else:	
				self.moving_down = False
				self.moving_up = True
		elif self.moving_up:
			if self.y > 100:
				self.y -= self.settings.character_speed
			else:
				self.moving_up = False
				self.moving_left = True
		elif self.moving_left:
			if self.x > 500:
				self.x -= self.settings.character_speed
			else:
				self.moving_left = False
				self.moving_right = True 
		self.rect.x = int(self.x)
		self.rect.y = int(self.y)

	def blitme(self):
		self.screen.blit(self.image, self.rect)