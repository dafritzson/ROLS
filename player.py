import pygame
import math_functions
from pygame.sprite import Sprite
from obstacle import Character


class Player(Character):
	def __init__(self, x, y, settings, screen, level_map, collisions, map_entities, golden_map_tile):
		super(Player, self).__init__(x, y, settings, screen, level_map, collisions)
		self.map_entities = map_entities
		self.golden_map_tile = golden_map_tile

		#Default Image
		self.image = pygame.image.load('.\\Images\\Player\\player_test.png')
		self.rect = self.image.get_rect()
		self.image = pygame.image.load('.\\Images\\Player\\Walk_Right\\right1.png')
		self.default_speed = 2
		self.speed = self.default_speed

		#Logic Attributes
		#flag for when the player is ready to interact with an obstacle when 'a' is pressed
		self.ready_for_interaction = False
		#flag for if the map is animating and not the player
		self.map_moving = False
		
		#Player items and game attributes
		self.report_count = 0

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
		'''

		self.image_right = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		self.image_left = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		self.image_up = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		self.image_down = [pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png'),pygame.image.load('.\\Images\\Player\\player_test.png')]
		'''

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

#Functions to move the level_map and obstacles as defined by the players position
	def move_map_right(self):
		for ent in self.map_entities:
			ent.x -= self.speed
		self.level_map.rect_overlay.x -= self.speed

	def move_map_left(self):
		for ent in self.map_entities:
			ent.x += self.speed
		self.level_map.rect_overlay.x += self.speed

	def move_map_up(self):
		for ent in self.map_entities:
			ent.y += self.speed
		self.level_map.rect_overlay.y += self.speed

	def move_map_down(self):
		for ent in self.map_entities:
			ent.y -= self.speed
		self.level_map.rect_overlay.y -= self.speed


	def interaction(self):
		self.collisions.remove(self)
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			pass
		self.collisions.add(self)

	
	def finish_animation(self):
		#Finish the animation for all movements. Only run after a keyup ends the player movement. Also handles finishing animation after a collision.
		if self.finishing_animation:
			self.player_x_round = math_functions.round_to_tileset(self.x, self.settings)
			self.player_y_round = math_functions.round_to_tileset(self.y, self.settings)
			self.golden_x_round = math_functions.round_to_tileset(self.golden_map_tile.x, self.settings)
			self.golden_y_round = math_functions.round_to_tileset(self.golden_map_tile.y, self.settings)

			if self.map_moving == False:
				if self.direction == "right" or self.direction == "left":
					if abs(self.x - self.player_x_round) <= self.speed:
						self.finishing_animation = False
						self.x = self.player_x_round
						self.animation_count = 0
					else:
						if self.direction == "right":
							self.move_right()
						elif self.direction == "left":
							self.move_left()
				
				elif self.direction == "up" or self.direction == "down":
					if abs(self.y - self.player_y_round) <= self.speed:
						self.y = self.player_y_round
						self.finishing_animation = False
						self.animation_count = 0
					else:
						if self.direction == "up":
							self.move_up()
						elif self.direction == "down":
							self.move_down()

			#finishing the level_map animation and player animates in place
			else:
				if self.direction == "right" or self.direction == "left":
					if abs(self.golden_map_tile.x - self.golden_x_round) <= self.speed:
						for ent in self.map_entities:
							ent.x = math_functions.round_to_tileset(ent.x, self.settings)
						self.level_map.rect_overlay.x = math_functions.round_to_tileset(self.level_map.rect_overlay.x, self.settings)
						self.finishing_animation = False
						self.animation_count = 0
					else:
						if self.direction == "right":
							self.animate_right()
							self.move_map_right()
							
						elif self.direction == "left":
							self.animate_left()
							self.move_map_left()
					
				elif self.direction == "up" or self.direction == "down":
					if abs(self.golden_map_tile.y - self.golden_y_round) <= self.speed:
						for ent in self.map_entities:
							ent.y = math_functions.round_to_tileset(ent.y, self.settings)
						self.level_map.rect_overlay.y = math_functions.round_to_tileset(self.level_map.rect_overlay.y, self.settings)
						#self.y = self.player_y_round
						self.finishing_animation = False
						self.animation_count = 0
					else:
						if self.direction == "up":
							self.animate_up()
							self.move_map_up()
						elif self.direction == "down":
							self.animate_down()
							self.move_map_down()


