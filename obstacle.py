import random
import pygame
from pygame.sprite import Sprite
from map_entity import MapEntity
from collision_sprite import CollisionSprite

random.seed()

class Obstacle(MapEntity):
	def __init__(self, x, y, settings, screen, level_map):
		super().__init__(x, y, settings, screen)
		self.settings = settings
		self.screen = screen
		self.level_map = level_map

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
		self.response_options = ["Yes", "No"]

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
	def __init__(self, x, y, settings, screen, level_map):
		super().__init__(x, y, settings, screen, level_map)

class Item(StaticObstacle):		
	def __init__(self, x, y, settings, screen, level_map):
		super().__init__(x, y, settings, screen, level_map)
		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\item.png')
		#self.image = pygame.transform.scale(self.image, (20, 18))
		self.rect = self.image.get_rect()
		#self.rect_interaction = self.rect.inflate(0, 0)

		#Logic Attributes
		self.interactable = True
		self.pickupable = True
		self.interaction_message = 'item_report_1'


class Desk(StaticObstacle):
	def __init__(self, x, y, settings, screen, level_map):
		super().__init__(x, y, settings, screen, level_map)

		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\desk_test.png')
		self.rect = self.image.get_rect()

		#Logic Attriutes
		self.interactable = True
		self.side_interactable = True
		self.interaction_side = "up"
		self.interaction_message = 'desk'


class CoffeeMachine(StaticObstacle):
	def __init__(self, x, y, settings, screen, level_map):
		super().__init__(x, y, settings, screen, level_map)

		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\coffee_machine.png')
		self.rect = self.image.get_rect()

		#Logic Attriutes
		self.interactable = True
		self.side_interactable = True
		self.player_modifier = True
		self.player_modifier_duration = 8.0
		self.interaction_message = 'coffee_machine'
		self.interaction_side = "up"

	def modify_player(self, player):
		self.player = player
		self.player.speed = 4

	def revert_player(self, player):
		self.player = player
		self.player.speed = self.player.default_speed

class Wall(StaticObstacle):
	def __init__(self, x, y, settings, screen, level_map):
		super().__init__(x, y, settings, screen, level_map)
		self.image = pygame.image.load('.\\Images\\Maps\\cubicle1.png')
		self.rect = self.image.get_rect()

'''
**************************************************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**************************************************************************************************************************************************************************
'''
class DynamicObstacle(Obstacle):
	def __init__(self, x, y, settings, screen, level_map, collisions):
		super().__init__(x, y, settings, screen, level_map)
		self.collisions = collisions
		
		#Movement Attributes
		#Flaf for when the player is moving with the downkeys
		self.move_in_progress = False
		#the direction the player is facing
		self.direction = "down"
		#forwards and backwards speeds
		self.speed = 2
		#counts for forwards and backwards animation
		self.animation_count_f = 0
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
		self.movement()

	def movement(self):
		pass

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
		self.image = self.image_right[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "right"

	def move_left(self):
		self.x = self.x - self.speed
		self.image = self.image_left[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "left"

	def move_up(self):
		self.y = self.y - self.speed
		self.image = self.image_up[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "up"

	def move_down(self):
		self.y = self.y + self.speed
		self.image = self.image_down[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "down"

	def check_collisions(self):
		#If player collides with an object rectangle, stop the player from moving in that direction
		self.collisions.remove(self)
		self.collision_sprite = self.get_collision_rect()
		
		if  pygame.sprite.spritecollide(self.collision_sprite, self.collisions, False):
			self.colliding = True
		else:
			self.colliding = False
		self.collisions.add(self)

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
	
	def finish_animation(self):
		#Finish the animation for all movements. Only run after a keyup ends the player movement. Also handles finishing animation after a collision.
		self.x_round = self.settings.tile_size * round(self.x / self.settings.tile_size)
		self.y_round = self.settings.tile_size * round(self.y / self.settings.tile_size)
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
'''
**************************************************************************************************************************************************************************
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**************************************************************************************************************************************************************************
'''
class Character(DynamicObstacle):
	def __init__(self, x, y, settings, screen, level_map, collisions):
		super().__init__(x, y, settings, screen, level_map, collisions)

	def blitme(self):
		self.rect.x = self.x
		self.rect.y = self.y

		self.image_x = self.x 
		self.image_y = self.y - self.settings.tile_size + 10
		self.screen.display.blit(self.image, (self.image_x, self.image_y))
		#self.screen.display.blit(self.image, (self.rect.x, self.rect.y))

	def round_to_tileset(self, value_to_round):
		self.value_to_round = value_to_round
		return self.settings.tile_size * round(self.value_to_round / self.settings.tile_size)


class NPC(Character):
	def __init__(self, x, y, settings, screen, level_map, collisions, move_width, move_height):
		super().__init__(x, y, settings, screen, level_map, collisions)
		self.move_width = move_width
		self.move_height = move_height

		#Load player image surface and define rectangle
		self.image = pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png')
		self.rect = self.image.get_rect()
		self.rect_interaction = self.rect.inflate(20, 20)
		#self.left_wall = self.x - (self.move_width / 2)
		#self.right_wall = self.x + (self.move_width / 2)
		#self.top_wall = self.y - (self.move_height / 2)
		#self.bottom_wall = self.y + (self.move_height / 2)

		#Movement Attributes
		self.speed = 1
		#attributes to help the NPC stay still for a certain count
		self.still_count = 0
		self.staying_still = False
		#Default movement
		self.moving_right = True


		#Logic Attributes
		self.interactable = True
		self.interactable = True
		self.is_NPC = True
		self.needs_response = True
		self.interaction_message = 'NPC_girl'
		self.message_type = "responsive"

	def face_player(self, player_direction):
		self.player_direction = player_direction
		x = {"right": 0 ,"up":1, "left":2, "down":3}
		num = 2
		num = (x.get(self.player_direction) + num) % 4
		key_list = list(x.keys()) 
		val_list = list(x.values()) 
		self.direction = key_list[val_list.index(num)]

		if self.direction == "right":
			self.face_right()
		elif self.direction == "left":
			self.face_left()		
		elif self.direction == "up":
			self.face_up()		
		elif self.direction == "down":
			self.face_down()

		self.still_count = 0

	def change_direction(self):
		x = {"right": 0 ,"up":1, "left":2, "down":3}
		num = random.choice([1,3])
		num = (x.get(self.direction) + num) % 4
		key_list = list(x.keys()) 
		val_list = list(x.values()) 
		self.direction = key_list[val_list.index(num)]

	def movement(self):
		rand_num = random.randint(1,100)
		
		#Keep NPC withing given movement rectangle
		#if self.x <= self.left_wall or self.x >= self.right_wall or self.y <= self.top_wall or self.y >= self.bottom_wall:
			#self.change_direction()

		self.check_collisions()
		
		if self.colliding:
			self.x = self.round_to_tileset(self.x)
			self.y = self.round_to_tileset(self.y)
			self.change_direction()

		elif self.finishing_animation and not self.staying_still:
			self.finish_animation()
		
		elif rand_num <3 and not self.staying_still:
			self.finishing_animation = True

		elif self.staying_still and self.still_count <15:
			self.still_count +=1

		elif self.staying_still and self.still_count >=15:
			self.staying_still = False
			self.still_count = 0
			self.change_direction()

		else:
			#standard player movement to respond to player movement flags set in the event loop
			if self.direction == "right":
				self.move_right()
			elif self.direction == "left":
				self.move_left()		
			elif self.direction == "up":
				self.move_up()		
			elif self.direction == "down":
				self.move_down()


class NPC_Still(NPC):
	def __init__(self,  x, y, settings, screen, level_map, collisions, move_width, move_height):
		super().__init__(x, y, settings, screen, level_map, collisions, move_width, move_height)

		self.image = pygame.image.load('.\\Images\\Player\\player_test.png')
		self.rect = self.image.get_rect()

	def movement(self):
		rand_num = random.randint(1,100)
		self.still_count += 1

		if not self.staying_still or self.still_count >30:

			# % chance to stay still
			if rand_num < 2:
				self.staying_still = True
				self.change_direction()
				self.still_count = 0

			else:
				self.staying_still = False
				if self.direction == "right":
					self.face_right()
				elif self.direction == "left":
					self.face_left()		
				elif self.direction == "up":
					self.face_up()		
				elif self.direction == "down":
					self.face_down()




