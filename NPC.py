import random
import pygame
import math_functions
from pygame.sprite import Sprite
from obstacle import Character

class NPC(Character):
	def __init__(self, x, y, program_data, screen, level_map, collisions):
		super().__init__(x, y, program_data, screen, level_map, collisions)

		#Load player image surface and define rectangle
		self.image = pygame.image.load('.\\Images\\Player\\player_test.png')
		self.rect = self.image.get_rect()
	
		#Movement Attributes
		self.speed = 1
		#attributes to help the NPC stay still for a certain count
		self.still_count = 0
		self.staying_still = False
		#Default movement
		self.moving_right = True


		#Logic Attributes
		self.interactable = True
		self.is_NPC = True
		self.is_battler = False
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
		

		self.check_collisions()
		
		if self.colliding:
			self.x = math_functions.round_to_tileset(self.x, self.program_data)
			self.y = math_functions.round_to_tileset(self.y, self.program_data)
			self.change_direction()

		elif self.finishing_animation and not self.staying_still:
			self.finish_animation()
		
		elif rand_num < 3 and not self.staying_still:
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
	def __init__(self,  x, y, program_data, screen, level_map, collisions):
		super().__init__(x, y, program_data, screen, level_map, collisions)

		self.response_messages =["I can't believe you picked the third option!", "Wow, you know so much about your colleagues! ; Let's be friends on BitLinked.", "Wow, you are so out of touch with your coworkers. ; Come back and talk to me later when you start caring."]


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

class NPC_Battler(NPC_Still):
	def __init__(self,  x, y, program_data, screen, level_map, collisions):
		super().__init__(x, y, program_data, screen, level_map, collisions)

		self.is_battler = True
		self.interaction_message = 'battle_kid'
		self.message_type = "battle"



