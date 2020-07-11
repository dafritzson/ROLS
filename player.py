import pygame
from pygame.sprite import Sprite
from obstacle import DynamicObstacle


class Player(DynamicObstacle):
	def __init__(self, settings, screen, level_map, x, y, collisions, display_box, obstacles, report):
		super(Player, self).__init__(settings, screen, level_map, x, y, collisions,)
		self.display_box = display_box
		self.obstacles = obstacles

		#Default Image
		self.image = pygame.image.load('.\\Images\\Player\\player_test.png')
		self.rect = self.image.get_rect()
		self.image = pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png')
		self.rect.center = self.screen.rect.center
		self.speed_f = 3
		self.speed_b = 1

		#Logic Attributes
		#flag for when the player is ready to interact with an obstacle when 'a' is pressed
		self.ready_for_interaction = False
		#flag for if the player can interact with the coliding obstacle
		self.interaction_obstacle = None
		#flag for if the player can pickup the interacting obstacle
		self.can_pickup = False
		#flag
		self.face_me = False
		#flag for if the map is animating and not the player
		self.map_moving = False

		
		#Player items and game attributes
		self.report_count = 0

		#Load player images
		'''
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
		'''

		self.image_right = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		self.image_left = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		self.image_up = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		self.image_down = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		

#Functions for animating the player without changing their position
	def animate_right(self):
		self.image = self.image_right[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "right"

	def animate_left(self):
		self.image = self.image_left[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "left"

	def animate_up(self):
		self.image = self.image_up[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "up"

	def animate_down(self):
		self.image = self.image_down[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "down"

#Functions to move the level_map and obstacles as defined by the players position
	def move_map_right(self):
		self.level_map.rect.x -= self.speed_f
		for obst in self.obstacles:
			obst.x -= self.speed_f

	def move_map_left(self):
		self.level_map.rect.x += self.speed_f
		for obst in self.obstacles:
			obst.x += self.speed_f

	def move_map_up(self):
		self.level_map.rect.y += self.speed_f
		for obst in self.obstacles:
			obst.y += self.speed_f

	def move_map_down(self):
		self.level_map.rect.y -= self.speed_f
		self.count=1
		for obst in self.obstacles:
			obst.y -= self.speed_f

	def interaction(self):
		self.collisions.remove(self)
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			pass
		self.collisions.add(self)

