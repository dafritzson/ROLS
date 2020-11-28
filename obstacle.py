import random
import pygame
import math
import math_functions
from pygame.sprite import Sprite
from map_entity import PhysicalMapEntity
from collision_sprite import CollisionSprite

random.seed()

class Obstacle(PhysicalMapEntity):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)
		#Static Logic Attributes
		#can the obstacle interact with the player
		self.interactable = False
		#can the obstacle interact only from a specific size
		self.side_interactable = False
		self.interaction_side = "up"
		#can the obstacle pe picked up by the player
		self.pickupable = False
		#flag for if the obstacle is an NPC
		self.is_NPC = False 
		#flag for if the obstacle modifies the player's attributes
		self.player_modifier = False
		#variables for the display box associated to that obstacle
		self.interaction_message = ""
		self.message_type = "default"
		self.response_options = ["A","Yes", "No"]
		self.response_messages =["A", "B"]

	def update(self):
		pass
	def modify_player(self, player):
		pass
	def revert_player(self, player):
		pass
	
'''
**************************************************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**************************************************************************************************************************************************************************
'''
# This class may not be a necessary abstaction since it may not be different than the parent Obstacle class
class StaticObstacle(Obstacle):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)

class Item(StaticObstacle):		
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)
		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\item.png')
		#self.image = pygame.transform.scale(self.image, (20, 18))
		self.rect = self.image.get_rect()

		#Logic Attributes
		self.interactable = True
		self.pickupable = True
		self.interaction_message = 'item_report_1'


class Desk(StaticObstacle):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)

		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\desk_test.png')
		self.rect = self.image.get_rect()

		#Logic Attriutes
		self.interactable = True
		self.side_interactable = True
		self.interaction_side = "up"
		self.interaction_message = 'desk'


class CoffeeMachine(StaticObstacle):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)

		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\coffee_machine.png')
		self.rect = self.image.get_rect()

		#Logic Attriutes
		self.interactable = True
		self.side_interactable = True
		self.player_modifier = True
		self.player_modifier_duration = 30
		self.interaction_message = 'coffee_machine'
		self.interaction_side = "up"

	def modify_player(self, player):
		self.player = player
		self.player.speed = 4

	def revert_player(self, player):
		self.player = player
		self.player.speed = self.player.default_speed

class Wall(StaticObstacle):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)
		self.image = pygame.image.load('.\\Images\\Maps\\golden_tile.png')

		self.rect = self.image.get_rect()

'''
**************************************************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**************************************************************************************************************************************************************************
'''
class DynamicObstacle(Obstacle):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)
		
		#Movement Attributes
		#Flaf for when the player is moving with the downkeys
		self.move_in_progress = False
		#the direction the player is facing
		self.direction = "right"
		#forwards and backwards speeds
		self.speed = 2
		#counts for forwards and backwards animation
		self.animation_count = 0
		self.animation_count_b = 0
		#flag for when the player is automatically finishing their animation to land on the correct pixel
		self.finishing_animation = False
		#direction flags to help dictate the player movement
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		#flag for if the player will collide on the next movement
		self.colliding = False

		#Attribute that should only be true for the player, but must be defined for all Dynamic Obstacles
		self.map_moving = False
		
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
		
	def update(self):
		if not self.program_data.game_paused:
			self.movement()

	def movement(self):
		pass

	def update_animation_count(self):
		if self.direction == "right":
			self.image = self.image_right[self.animation_count % 12]
		elif self.direction == "left":
			self.image = self.image_left[self.animation_count % 12]
		elif self.direction == "up":
			self.image = self.image_up[self.animation_count % 12]
		else:
			self.image = self.image_down[self.animation_count % 12]

	def face_right(self):
		self.image = self.image_right[0]
		self.direction = "right"

	def face_left(self):
		self.image = self.image_left[0]
		self.direction = "left"

	def face_up(self):
		self.image = self.image_up[0]
		self.direction = "up"

	def face_down(self):
		self.image = self.image_down[0]
		self.direction = "down"

	#Functions to move the Dynamic Obstacle in different directions with corresponding animation
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

	def check_collisions(self):
		#If player collides with an object rectangle, stop the player from moving in that direction
		self.program_data.collisions.remove(self)
		self.collision_sprite = self.get_collision_rect()
		if  pygame.sprite.spritecollide(self.collision_sprite, self.program_data.collisions, False):
			self.colliding = True
			self.animation_count = 0
		else:
			self.colliding = False
		self.program_data.collisions.add(self)

	def get_collision_rect(self):	
		if self.direction == "right":
			self.collision_sprite = CollisionSprite(self.x + self.speed, self.y)
		elif self.direction == "left":
			self.collision_sprite = CollisionSprite(self.x - self.speed, self.y)
		elif self.direction == "up":
			self.collision_sprite = CollisionSprite(self.x, self.y - self.speed)
		else: 
			self.collision_sprite = CollisionSprite(self.x, self.y + self.speed)
		return self.collision_sprite
	
'''
**************************************************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**************************************************************************************************************************************************************************
'''
class Character(DynamicObstacle):
	def __init__(self, x, y, program_data):
		super().__init__(x, y, program_data)

	def blitme(self):
		self.rect.x = self.x
		self.rect.y = self.y

		self.update_animation_count()

		self.image_x = self.x 
		#offset the y so the image of the player stands closer to the middle of the tile
		self.image_y = self.y - self.program_data.tile_size + 10
		self.screen.display.blit(self.image, (self.image_x, self.image_y))

	def finish_animation(self):
		#Finish the animation for all movements. Only run after a keyup ends the player movement. Also handles finishing animation after a collision.
		self.x_round = self.program_data.tile_size * round(self.x / self.program_data.tile_size)
		self.y_round = self.program_data.tile_size * round(self.y / self.program_data.tile_size)
		if self.direction == "right" or self.direction == "left":
			if abs(self.x - self.x_round) <= self.speed:
				self.x = self.x_round
				self.finishing_animation = False
				self.staying_still = True
			else:
				if self.direction == "right":
					self.move_right()
				elif self.direction == "left":
					self.move_left()
		
		elif self.direction == "up" or self.direction == "down":
			if abs(self.y - self.y_round) <= self.speed:
				self.y = self.y_round
				self.finishing_animation = False
				self.staying_still = True
			else:
				if self.direction == "up":
					self.move_up()
				elif self.direction == "down":
					self.move_down()