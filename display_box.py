import pygame
import time
from pygame.sprite import Sprite
import audio_mixer as am

class DummyBox(Sprite):
	'''class to always populate the display_box group, to allow it to update properly'''
	def __init__(self):
		super(DummyBox, self).__init__()
		self.visible = False
		self.is_active = False

	def update(self):
		pass

class DisplayBox(Sprite):
	'''class to define the display box at the bottom of the screen'''
	def __init__(self, program_data, screen, audio_mixer):
		super(DisplayBox, self).__init__()
		self.program_data = program_data
		self.screen = screen
		self.audio_mixer = audio_mixer
		
		#font_main program_data
		self.text_color = (4,65,33)
		self.font_main = pygame.font.SysFont('Calibri', 20)
		self.font_sub = pygame.font.SysFont('Calibri', 18)

		self.color = (240, 240, 240)
		self.color_scrollbar = (200, 10, 10)
		self.color_scrollbar_inside = (100, 100, 100)

		#Default display box locations
		self.width = self.screen.rect.width
		self.height = self.program_data.tile_size*3
		self.left = self.screen.rect.left
		self.top = self.screen.rect.bottom - self.height
		self.rect = pygame.Rect(self.left, self.top, self.width, self.height)

		self.response_width = self.screen.rect.width/2
		self.response_height = self.program_data.tile_size*2
		self.response_left = self.screen.rect.right - self.response_width
		self.response_top = self.screen.rect.bottom - self.program_data.tile_size*5

		self.rect_response = pygame.Rect(self.response_left , self.response_top, self.response_width, self.response_height)
		self.rect_scrollbar = pygame.Rect(self.screen.rect.width - 14, self.response_top + 6, round(self.program_data.tile_size/3) + 4 , self.response_height - 12)
		
		self.arrow_value_x = 0
		self.arrow_value_y = 0


		#Use the ";" character to indicate a break in the sentence. 
		#All breaks will clear the display box and start displaying after the break
		self.messages = {
		'intro' : "hello the_Guy", 
		'NPC_girl' : "Did you hear Bob and Karren went fishing last weekend?",
		'desk' : "This is my desk",
		'item_report_1' : "You found a level 1 BitCorp Report!",
		'coffee_machine' : "Enjoy your brew! ; The Guy drank his coffee and is feeling ready to work.",
		'battle_kid' : "Hey you! ; There is no way you are a more effective employee than me! ; Let's battle and find out"
		}
		self.message_to_write = "Hello the_Guy"

		#Dynamic Attributes
		self.is_active = True
		self.visible = False
		self.noise_on = False
		self.character_line_limit = 42
		self.message_key = 'intro'
		self.message_type = "default"
		self.response_options = ["Yes", "No"]
		self.response_messages = ["A", "B"]
		self.response_lines_to_show = 2

	def prep_message(self):
		#Reset display box, and counters and prep it for displaying the message
		self.message_to_write = self.messages.get(self.message_key)
		self.word_list = self.message_to_write.split()
		self.responses_number = len(self.response_options)
		self.response_line = 1
		self.reset_display_box_variables()
		
	def reset_display_box_variables(self):
		self.clear_lines()
		self.word_count = 0
		self.char_count = 0
		self.blit_count = 0
		self.blit_count_counter = 0

		#States of the message being written
		self.main_message_done = False
		self.message_sequence_done = False
		self.typing = False
		self.switching_lines = False
		self.switching_lines_count = 0



	def clear_lines(self):
		self.line1 = ""
		self.line1_words_only = ""
		self.line2 = ""	
		self.line2_words_only = ""
		self.line1_temp = ""
		self.line2_temp = ""
		self.current_active_line = 1
		self.clear_on_click = False

	def update(self):
		pygame.draw.rect(self.screen.display, self.color, self.rect)
		self.noise_on = False

		#Updating through the main message
		if not self.main_message_done:
			if self.switching_lines:
				self.switching_lines_count +=1
				self.switch_lines()

			else:
				#itterate through all words in the message
				if self.word_count < (len(self.word_list)):
					self.current_word = self.word_list[self.word_count]
				else:
					self.main_message_done = True
					self.blit_lines()
					return
				
				#Handle message break character
				if self.current_word == ";":
					self.clear_on_click = True
					self.word_count += 1
					self.typing = False
					self.blit_lines()
					self.blit_next_arrow()
					return

				elif not self.clear_on_click:
					if self.current_active_line == 1:
						self.fill_line1()
						
					else:
						self.current_active_line = 2
						self.fill_line2()
		#Main message is done
		else:
			self.typing = False
			#Trigger a response if it is a reponsive type message
			if not self.message_sequence_done:
				if self.message_type == "responsive":
					self.blit_response_options()
					self.blit_select_arrow()
					self.noise_on = True
					self.audio_mixer.audio_key = ('sound_display_box')
					self.audio_mixer.load_sound()
					
					if self.arrow_value_y <= 1:
						self.response_line = self.arrow_value_y = 1
					elif self.arrow_value_y >= self.responses_number:
						self.response_line = self.arrow_value_y = self.responses_number
					else:
						self.response_line = self.arrow_value_y
					print(self.response_line)

				else:
					self.message_sequence_done = True

			#Trigger battle sequence for battlers
			if self.message_type == "battle":
				self.program_data.game_state = "battle"
		self.blit_lines()

	def fill_line1(self):
		if len(self.line1_words_only + self.current_word) <= self.character_line_limit:
			#Check if there are more characters in the given word
			if self.char_count < len(self.current_word):
				self.line1 += (self.current_word[self.char_count])
				self.char_count += 1
				self.typing = True
			else:
				self.line1_words_only = self.line1
				self.line1 += " "
				self.char_count = 0
				self.word_count += 1
		else:
			self.current_active_line = 2
			self.char_count = 0

	def fill_line2(self):
		if len(self.line2_words_only + self.current_word) <= self.character_line_limit:
			#Check if there are more characters in the given word
			if self.char_count < len(self.current_word):
				self.line2 += (self.current_word[self.char_count])
				self.char_count += 1
				self.typing = True
			else:
				self.line2_words_only = self.line2
				self.line2 += " "
				self.char_count = 0
				self.word_count += 1
		else:
			self.char_count = 0
			self.typing = False

	def switch_lines(self):
		self.switching_lines = True	
		if self.switching_lines_count == 0:
			self.line1_temp = self.line1
			self.line1 = ""
			self.line1_words_only = ""
			self.line2_temp = self.line2
			self.line2 = ""
			self.line2_words_only = ""
		elif self.switching_lines_count > 3:
			self.line1_temp = ""
			self.line1 = self.line2_temp
			self.line2_temp = ""
			self.switching_lines_count = 0
			self.switching_lines = False
		self.blit_lines()

	def blit_lines(self):
		#blit line1 and line2 to the screen on the screen
		self.line1_image = self.font_main.render(self.line1, True, self.text_color, self.color)
		self.line1_rect = self.line1_image.get_rect()
		self.line1_rect.left = self.rect.left + 5
		self.line1_rect.centery = self.rect.centery - self.rect.height/5
		self.screen.display.blit(self.line1_image, self.line1_rect)

		self.line2_image = self.font_main.render(self.line2, True, self.text_color, self.color)
		self.line2_rect = self.line2_image.get_rect()
		self.line2_rect.left = self.rect.left + 5
		self.line2_rect.centery = self.rect.centery + self.rect.height/5
		self.screen.display.blit(self.line2_image, self.line2_rect)

		self.line1_temp_image = self.font_main.render(self.line1_temp, True, self.text_color, self.color)
		self.line1_temp_rect = self.line1_temp_image.get_rect()
		self.line1_temp_rect.left = self.rect.left + 5
		self.line1_temp_rect.centery = self.rect.centery - self.rect.height/3
		self.screen.display.blit(self.line1_temp_image, self.line1_temp_rect)

		self.line2_temp_image = self.font_main.render(self.line2_temp, True, self.text_color, self.color)
		self.line2_temp_rect = self.line2_temp_image.get_rect()
		self.line2_temp_rect.left = self.rect.left + 5
		self.line2_temp_rect.centery = self.rect.centery
		self.screen.display.blit(self.line2_temp_image, self.line2_temp_rect)	

		if not self.typing and self.main_message_done == False:
			self.blit_next_arrow()	
			self.noise_on = True
			self.audio_mixer.audio_key = 'sound_display_box'
			self.audio_mixer.load_sound()

	def blit_next_arrow(self):
		self.arrow_images = [pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png')]
		#self.arrow_images = [pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png'), pygame.image.load('.\\Images\\Misc\\down_arrow2.png')]
		self.blit_count_counter +=1 
		if self.blit_count_counter % 12 ==0:
			self.blit_count += 1
		self.arrow_image = self.arrow_images[self.blit_count%3]

		self.arrow_rect = self.arrow_image.get_rect()
		self.arrow_rect.left = self.rect_response.right - 30
		self.arrow_rect.centery = self.rect.bottom - 15
		self.screen.display.blit(self.arrow_image, self.arrow_rect)

	def blit_response_options(self):
		pygame.draw.rect(self.screen.display, self.color, self.rect_response)

		self.blit_response_scrollbar()
		self.option_count = 0
		for option in self.response_options:
			self.option_count += 1
			self.line_image = self.font_sub.render(option, True, self.text_color, self.color)
			self.line_image_size = self.font_sub.size(option)
			self.line_rect = self.line_image.get_rect()
			self.line_rect.left = self.rect_response.left + 20
			self.line_rect.centery = self.rect_response.top + self.line_image_size[1] * self.option_count - self.response_line*10
			if self.rect_response.contains(self.line_rect):
				self.screen.display.blit(self.line_image, self.line_rect)

	def blit_select_arrow(self):
		self.arrow_image = pygame.image.load('.\\Images\\Misc\\right_arrow.png')
		self.arrow_rect = self.arrow_image.get_rect()
		self.arrow_rect.left = self.rect_response.left + 5
		#self.arrow_rect.centery = self.rect_response.top + self.rect_response.height/3 * self.response_line - self.response_line*10
		self.arrow_rect.centery = self.rect_response.top + self.line_image_size[1] * self.response_line - self.response_line*10
		self.screen.display.blit(self.arrow_image, self.arrow_rect)
		pygame.draw.rect(self.screen.display, self.color, self.rect)

	def blit_response_scrollbar(self):
		self.rect_scrollbar_inside = pygame.Rect(self.screen.rect.width - 11, self.response_top + 10, self.program_data.tile_size/4 + 1, self.response_height - 50)
		pygame.draw.rect(self.screen.display, self.color_scrollbar, self.rect_scrollbar)
		pygame.draw.rect(self.screen.display, self.color_scrollbar_inside, self.rect_scrollbar_inside)

	def run_responsive_message(self):
		self.reset_display_box_variables()
		self.message_type = "default"
		self.message_to_write = self.response_messages[self.response_line - 1]
		self.word_list = self.message_to_write.split()

	def deactivate(self):
		self.is_active = False

	def activate(self):
		self.is_active = True


class Scrollbox(DisplayBox):
	'''class to define the display box at the bottom of the screen'''
	def __init__(self, program_data, screen, audio_mixer):
		super().__init__(program_data, screen, audio_mixer)

