import pygame
from pygame.sprite import Sprite
from obstacle import Character


class Player(DynamicObstacle):
	def __init__(self, x, y, settings, screen, level_map, collisions, display_box, obstacles, map_entities, golden_map_tile, tile_list):
		super(Player, self).__init__(x, y, settings, screen, level_map, collisions)
		self.display_box = display_box
		self.obstacles = obstacles
		self.map_entities = map_entities
		self.golden_map_tile = golden_map_tile

		#Default Image
		self.image = pygame.image.load('.\\Images\\Player\\player_test.png')
		self.rect = self.image.get_rect()
		self.image = pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png')
		self.default_speed = 2
		self.speed = self.default_speed

		#Logic Attributes
		#flag for when the player is ready to interact with an obstacle when 'a' is pressed
		self.ready_for_interaction = False
		#flag for if the map is animating and not the player
		self.map_moving = False
		
		#Player items and game attributes
		self.report_count = 0
		
		# Initialize player location by selecting a tile. In this example, we'll try starting on the third walkable tile.
		tile_counter = 0
		for tile in tile_list:
			if tile.walkable:
				tile_counter += 1
				if tile_counter == 50:
					self.current_tile = tile
		print(tile_counter)
		self.x = self.current_tile.centerX
		self.y = self.current_tile.centerY
				

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
		for ent in self.map_entities:
			ent.x -= self.speed

	def move_map_left(self):
		for ent in self.map_entities:
			ent.x += self.speed

	def move_map_up(self):
		for ent in self.map_entities:
			ent.y += self.speed

	def move_map_down(self):
		for ent in self.map_entities:
			ent.y -= self.speed

	def interaction(self):
		self.collisions.remove(self)
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			pass
		self.collisions.add(self)

	def move_right(self, target_tile):
		self.targetX = target_tile.centerX
		if self.x < self.targetX:
			self.x = self.x + self.speed
		else:
			self.finishing_animation = False
			self.move_in_progress = False
			self.current_tile = target_tile

		self.image = self.image_right[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "right"

	def move_left(self, target_tile):
		self.targetX = target_tile.centerX
		if self.x > self.targetX:
			self.x = self.x - self.speed
		else:
			self.finishing_animation = False
			self.move_in_progress = False
			self.current_tile = target_tile

		self.image = self.image_left[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "left"

	def move_up(self, target_tile):
		self.targetY = target_tile.centerY
		if self.y > self.targetY:
			self.y = self.y - self.speed
		else:
			self.finishing_animation = False
			self.move_in_progress = False
			self.current_tile = target_tile

		self.image = self.image_up[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "up"

	def move_down(self, target_tile):
		self.targetY = target_tile.centerY
		if self.y < self.targetY:
			self.y = self.y + self.speed
		else:
			self.finishing_animation = False
			self.move_in_progress = False
			self.current_tile = target_tile

		self.image = self.image_down[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "down"


	def finish_animation(self, tile_list):
		#Finish the animation for all movements. Also handles finishing animation after a collision.
		if self.map_moving == False:
			if self.direction == "right" or self.direction == "left":
				# if (((self.x + self.speed) % self.settings.tile_size) < (self.x  % self.settings.tile_size) or ((self.x - self.speed) % self.settings.tile_size) > (self.x  % self.settings.tile_size)) or self.x % self.settings.tile_size == 0:
				# 	self.x = self.settings.tile_size * round(self.x / self.settings.tile_size)
				# 	self.finishing_animation = False
				# else:
				if self.direction == "right":
					for tile in tile_list:
						if tile.tileY == self.current_tile.tileY and tile.tileX == self.current_tile.tileX + 1:
							self.move_right(tile)
				elif self.direction == "left":
					for tile in tile_list:
						if tile.tileY == self.current_tile.tileY and tile.tileX == self.current_tile.tileX - 1:
							self.move_left(tile)
			
			elif self.direction == "up" or self.direction == "down":
				# if (((self.y + self.speed) % self.settings.tile_size) < (self.y % self.settings.tile_size) or ((self.y - self.speed) % self.settings.tile_size) > (self.y  % self.settings.tile_size)) or self.y % self.settings.tile_size == 0:
				# 	self.y = self.settings.tile_size * round(self.y / self.settings.tile_size)
				# 	self.finishing_animation = False
				# else:
				if self.direction == "up":
					for tile in tile_list:
						if tile.tileX == self.current_tile.tileX and tile.tileY == self.current_tile.tileY - 1:
							self.move_up(tile)
				elif self.direction == "down":
					for tile in tile_list:
						if tile.tileX == self.current_tile.tileX and tile.tileY == self.current_tile.tileY + 1:
							self.move_down(tile)

			else:
				self.finishing_animation = False
		
		#finishing the level_map animation and player animates in place
		else:
			if self.direction == "right" or self.direction == "left":
				if (((self.golden_map_tile.rect.x + self.speed) % self.settings.tile_size) < (self.golden_map_tile.rect.x  % self.settings.tile_size) or ((self.golden_map_tile.rect.x - self.speed) % self.settings.tile_size) > (self.golden_map_tile.rect.x  % self.settings.tile_size)) or self.golden_map_tile.rect.x % self.settings.tile_size == 0:
					self.golden_map_tile.rect.x = self.settings.tile_size * round(self.golden_map_tile.rect.x / self.settings.tile_size)
					self.finishing_animation = False
					
				else:
					if self.direction == "right":
						self.animate_right()
						self.move_map_right()
					elif self.direction == "left":
						self.animate_left()
						self.move_map_left()
				
				elif self.direction == "up" or self.direction == "down":
					if abs(self.y - self.player_y_round) <= self.speed:
						self.y = self.player_y_round
						self.finishing_animation = False

					else:
						if self.direction == "up":
							self.move_up()
						elif self.direction == "down":
							self.move_down()

			#finishing the level_map animation and player animates in place
			else:
				if self.direction == "right" or self.direction == "left":
					if abs(self.golden_map_tile.x - self.golden_x_round) <= self.speed:
						#self.golden_map_tile.x = self.golden_x_round
						for ent in self.map_entities:
							ent.x = self.round_to_tileset(ent.x)
							ent.blitme()
						self.finishing_animation = False

					else:
						if self.direction == "right":
							self.animate_right()
							self.move_map_right()
							
						elif self.direction == "left":
							self.animate_left()
							self.move_map_left()
					
				elif self.direction == "up" or self.direction == "down":
					if abs(self.golden_map_tile.y - self.golden_y_round) <= self.speed:
						#self.golden_map_tile.y = self.golden_y_round
						for ent in self.map_entities:
							ent.y = self.round_to_tileset(ent.y)
							ent.blitme()
						self.finishing_animation = False

					else:
						if self.direction == "up":
							self.animate_up()
							self.move_map_up()
						elif self.direction == "down":
							self.animate_down()
							self.move_map_down()

	def round_to_tileset(self, value_to_round):
		self.value_to_round = value_to_round
		return self.settings.tile_size * round(self.value_to_round / self.settings.tile_size)

