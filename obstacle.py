import random
import pygame
from pygame.sprite import Sprite

random.seed()

class Obstacle(Sprite):
	def __init__(self, settings, screen, level_map, x, y):
		super(Obstacle, self).__init__()
		self.screen = screen
		self.settings = settings
		self.level_map = level_map
		self.x = x
		self.y = y
		self.image = None
		self.rect = None
		self.rect_interaction = None
		self.interactable = False
		self.side_interactable = False
		self.interaction_side = "up"
		self.pickupable = False
		self.interaction_message = None
		self.interaction_obstacle = None


	def interact_with_player(self):
		pass

	def update(self):
		pass
	
	def blitme(self):
		#self.level_map.image.blit(self.image, self.rect)
		self.rect.x = self.x
		self.rect.y = self.y
		self.screen.display.blit(self.image, self.rect)


# This class may not be a necessary abstaction since it may not be different than the parent Obstacle class
class StaticObstacle(Obstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)

class Item(StaticObstacle):		
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)
		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\desk.png')
		self.image = pygame.transform.scale(self.image, (20, 18))
		self.rect = self.image.get_rect()

		self.rect_interaction = self.rect.inflate(0, 0)
		self.interactable = True
		self.interaction_message = 'item_report_1'
		self.pickupable = True




class Desk(StaticObstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)

		#Load image
		self.image = pygame.image.load('.\\Images\\Objects\\desk.png')
		self.image = pygame.transform.scale(self.image, (55, 40))
		self.rect = self.image.get_rect()

		self.rect_interaction = self.rect.inflate(0, 0)
		self.interactable = True
		self.side_interactable = True
		self.interaction_message = 'desk'


class Wall(StaticObstacle):
	def __init__(self, settings, screen, level_map, x, y):
		super().__init__(settings, screen, level_map, x, y)
		self.image = pygame.image.load('.\\Images\\Maps\\cubicle_wall.png')
		self.rect = self.image.get_rect()

class DynamicObstacle(Obstacle):
	def __init__(self, settings, screen, level_map, x, y, collisions):
		super().__init__(settings, screen, level_map, x, y)
		self.collisions = collisions
		# Character movement states
		self.move_in_progress = False
		self.moving_back = False
		self.direction = "down"
		self.speed_f = 3
		self.speed_b = 1
		self.animation_count_f = 0
		self.animation_count_b = 0

		self.finishing_animation = False

		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

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


	def update(self):
		self.movement()

	def movement(self):
		pass


	#Functions to move the Dynamic Obstacle in different directions with corresponding animation
	def move_right(self):
		self.x = self.x + self.speed_f
		self.image = self.image_right[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "right"

	def move_left(self):
		self.x = self.x - self.speed_f
		self.image = self.image_left[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "left"

	def move_up(self):
		self.y = self.y - self.speed_f
		self.image = self.image_up[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "up"

	def move_down(self):
		self.y = self.y + self.speed_f
		self.image = self.image_down[self.animation_count_f % 12]
		self.animation_count_f += 1
		self.direction = "down"

	def check_collisions(self):
		#If player collides with an object rectangle, stop the player from moving in that direction
		self.collisions.remove(self)
		if  pygame.sprite.spritecollide(self, self.collisions, False):
			self.move_back()
			self.moving_back = True
		self.collisions.add(self)

	def move_back(self):
		self.animation_count_b += 1
		#If colliding but moving forward this move back should cancel the players motion having him not move into the obstacle
		if self.move_in_progress:
			self.speed = self.speed_f
		#If the player finishes colliding and finishes the animation it should slow its speed to 1 so that it can land on the correct pixel
		else:
			self.speed = self.speed_b
		if self.direction =="right":
			self.x = self.x - self.speed
			self.image = self.image_right[self.animation_count_b % 12]

		elif self.direction == "left":
			self.x = self.x + self.speed
			self.image = self.image_left[self.animation_count_b % 12]

		elif self.direction == "up":
			self.y = self.y + self.speed
			self.image = self.image_up[self.animation_count_b % 12]

		elif self.direction == "down":
			self.y = self.y - self.speed
			self.image = self.image_down[self.animation_count_b % 12]
	
	def finish_animation(self):
		#Finish the animation for all movements. Only run after a keyup ends the player movement. Also handles finishing animation after a collision.
		if (self.direction == "right" or self.direction == "left") and self.rect.x % 8 != 0:
			if self.moving_back:
				self.move_back()
			elif self.direction == "right":
				self.move_right()
			elif self.direction == "left":
				self.move_left()
		elif (self.direction == "up" or self.direction == "down") and self.rect.y % 8 != 0:
			if self.moving_back:
				self.move_back()
			elif self.direction == "up":
				self.move_up()
			elif self.direction == "down":
				self.move_down()
		else:
			self.finishing_animation = False
			self.moving_back = False



class NPC(DynamicObstacle):
	def __init__(self, settings, screen, level_map, x, y, collisions, move_width, move_height):
		super().__init__(settings, screen, level_map, x, y, collisions)
		self.move_width = move_width
		self.move_height = move_height


		#Load player image surface and define rectangle
		self.image = pygame.image.load('.\\Images\\Player\\Walk_Left\\left1.png')
		self.rect = self.image.get_rect()
		self.rect_interaction = self.rect.inflate(20, 20)
		self.left_wall = self.x - (self.move_width / 2)
		self.right_wall = self.x + (self.move_width / 2)
		self.top_wall = self.y - (self.move_height / 2)
		self.bottom_wall = self.y + (self.move_height / 2)


		self.interactable = True
		self.move_count = 0
		self.speed_f = 1
		self.speed_b = 1
		self.still_count = 0
		self.staying_still = False
		self.interactable = True
		self.interaction_message = 'NPC_girl'

		#First move direction
		self.moving_right = True


	def change_direction(self):
		x = {"right": 0 ,"up":1, "left":2, "down":3}
		num = random.choice([1,3])
		#print(x.get(self.direction))
		num = (x.get(self.direction) + num) % 4
		key_list = list(x.keys()) 
		val_list = list(x.values()) 
		self.direction = key_list[val_list.index(num)]


	def movement(self):
		rand_num = random.randint(1,100)
		
		#Keep NPC withing given movement rectangle
		#if self.x <= self.left_wall or self.x >= self.right_wall or self.y <= self.top_wall or self.y >= self.bottom_wall:
			#self.change_direction()

		self.still_count += 1
		self.check_collisions()

		if not self.staying_still or self.still_count >15:
			if self.finishing_animation:
				self.finish_animation()
				self.move_in_progress = False

			# % chance to stay still
			elif rand_num < 3:
				self.staying_still = True
				self.change_direction()
				self.still_count = 0

			#% chance to stay still
			#elif rand_num <= 95:
			else:
				self.move_in_progress = True
				#standard player movement to respond to player movement flags set in the event loop
				if self.direction == "right":
					self.move_right()
				elif self.direction == "left":
					self.move_left()		
				elif self.direction == "up":
					self.move_up()		
				elif self.direction == "down":
					self.move_down()
				
				self.finishing_animation = False

			#Chance to change direction
			#else:
			#	self.change_direction()
			#	self.finishing_animation = True







