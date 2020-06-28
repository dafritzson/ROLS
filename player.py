import pygame
from pygame.sprite import Sprite
from obstacle import DynamicObstacle


class Player(DynamicObstacle):
	def __init__(self, settings, screen, level_map, x, y, collisions, display_box, obstacles):
		super(Player, self).__init__(settings, screen, level_map, x, y, collisions,)
		self.display_box = display_box
		self.obstacles = obstacles

		#Default Image
		self.image = pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.screen.rect.center

		#Player specific states
		self.finishing_animation = False
		self.ready_for_interaction = False

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

#Functions to move the level_map and objects as defined by the players position
	def move_map_right(self):
		self.level_map.rect.centerx -= self.speed
		for obst in self.obstacles:
			obst.x -= self.speed

	def move_map_left(self):
		self.level_map.rect.centerx += self.speed
		for obst in self.obstacles:
			obst.x += self.speed
			print(obst)

	def move_map_up(self):
		self.level_map.rect.centery += self.speed
		for obst in self.obstacles:
			obst.y += self.speed

	def move_map_down(self):
		self.level_map.rect.centery -= self.speed
		self.count=1
		for obst in self.obstacles:
			obst.y -= self.speed

	def interaction(self):
		self.collisions.remove(self)
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			pass
		self.collisions.add(self)

