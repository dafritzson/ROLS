import pygame
from pygame.sprite import Sprite


class Player(Sprite):
	def __init__(self, screen, settings, display_box, collisions):
		super(Player, self).__init__()
		self.screen = screen
		self.settings = settings
		self.display_box = display_box
		self.collisions = collisions

		#Default Image
		self.image = pygame.image.load('.\\Images\\Player\\the_guy_l.png')
		self.image = pygame.transform.scale(self.image, (30, 85))

		#Player movement states
		self.move_in_progress = False
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

		#Load player image surface and define rectangle
		self.image_left = pygame.image.load('.\\Images\\Player\\the_guy_l.png')
		self.image_right = pygame.image.load('.\\Images\\Player\\the_guy_r.png')
		self.image_left = pygame.transform.scale(self.image_left, (30, 85))
		self.image_right = pygame.transform.scale(self.image_right, (30, 85))
		self.rect = self.image_left.get_rect()
		self.screen_rect = self.screen.get_rect()
		self.rect.center = self.screen_rect.center

		#Player exact positions
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)


	def update_position(self):
		'''Update character movement. Character can only move in one direction'''
		#self.move_animating = True
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x = self.x + self.settings.character_speed
			self.direction = "right"
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.x = self.x - self.settings.character_speed
			self.direction = "left"
		elif self.moving_up and self.rect.top > self.screen_rect.top:
			self.y = self.y - self.settings.character_speed
			self.direction = "up"
		elif self.moving_down and self.rect.bottom < self.display_box.box_rect.top:
			self.y = self.y + self.settings.character_speed
			self.direction="down"
		#If player collides with an object rectangle, stop the player from moving in that direction
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			self.move_back()
		self.rect.x = int(self.x)
		self.rect.y = int(self.y)

	def move_back(self):
		if self.direction =="right":
			self.x = self.x - self.settings.character_speed
		elif self.direction == "left":
			self.x = self.x + self.settings.character_speed
		elif self.direction == "up":
			self.y = self.y + self.settings.character_speed
		elif self.direction == "down":
			self.y = self.y - self.settings.character_speed


	def blitme(self):
		self.screen.blit(self.image, self.rect)


