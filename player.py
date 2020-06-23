import pygame
from pygame.sprite import Sprite


class Player(Sprite):
	def __init__(self, settings, screen, level_map, display_box, collisions, static_objects):
		super(Player, self).__init__()
		self.screen = screen
		self.settings = settings
		self.level_map = level_map
		self.display_box = display_box
		self.collisions = collisions
		self.static_objects = static_objects

		#Default Image
		self.image = pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png')
		self.rect = self.image.get_rect()
		#self.rect = self.image.get_rect(center = (16,-16))
		#self.rect = self.rect.inflate(0,-30)

		self.rect.center = self.screen.rect.center

		#Player movement data
		self.move_in_progress = False
		self.finishing_animation = False
		self.move_count = 0
		self.direction = "none"
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.speed = 3
		self.animation_count = 0

		#Load player images
		self.image_left = [pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left2.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left2.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left3.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left3.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left4.png'),pygame.image.load('.\\Images\\Player\\Walk_Left\\left4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Left\\left4.png')]

		self.image_right = [pygame.image.load('.\\Images\\Player\\Walk_Right\\right1.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right1.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right2.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right2.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right3.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right3.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right4.png'),pygame.image.load('.\\Images\\Player\\Walk_Right\\right4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Right\\right4.png')]

		self.image_up = [pygame.image.load('.\\Images\\Player\\Walk_Up\\up1.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up1.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up2.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up2.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up3.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up3.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up4.png'),pygame.image.load('.\\Images\\Player\\Walk_Up\\up4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Up\\up4.png')]

		self.image_down = [pygame.image.load('.\\Images\\Player\\Walk_Down\\down1.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down1.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down1.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down2.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down2.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down2.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down3.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down3.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down3.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down4.png'),pygame.image.load('.\\Images\\Player\\Walk_Down\\down4.png'),
		pygame.image.load('.\\Images\\Player\\Walk_Down\\down4.png')]


		#Player exact positions
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

#Functions to move the player in different directions with corresponding animation
	def move_right(self):
		self.x = self.x + self.speed
		self.image = self.image_right[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "right"

	def move_left(self):
		self.x = self.x - self.speed
		self.image = self.image_left[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "left"

	def move_up(self):
		self.y = self.y - self.speed
		self.image = self.image_up[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "up"

	def move_down(self):
		self.y = self.y + self.speed
		self.image = self.image_down[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "down"

#Functions for animating the player without changing their position
	def animate_right(self):
		self.image = self.image_right[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "right"

	def animate_left(self):
		self.image = self.image_left[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "left"

	def animate_up(self):
		self.image = self.image_up[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "up"

	def animate_down(self):
		self.image = self.image_down[self.animation_count % 12]
		self.animation_count += 1
		self.direction = "down"

	def check_collision(self):
		#If player collides with an object rectangle, stop the player from moving in that direction
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			self.move_back()

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
		self.rect.x = int(self.x)
		self.rect.y = int(self.y)
		self.screen.display.blit(self.image, self.rect)


#Functions to move the level_map and objects as defined by the players position
	def move_map_right(self):
		self.level_map.rect.centerx -= self.speed
		for obj in self.static_objects:
			obj.rect.centerx -=self.speed

	def move_map_left(self):
		self.level_map.rect.centerx += self.speed
		for obj in self.static_objects:
			obj.rect.centerx +=self.speed

	def move_map_up(self):
		self.level_map.rect.centery += self.speed
		for obj in self.static_objects:
			obj.rect.centery += self.speed

	def move_map_down(self):
		self.level_map.rect.centery -= self.speed
		for obj in self.static_objects:
			obj.rect.centery -=self.speed