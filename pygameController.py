
import pygame 
from pygame.locals import *
import numpy as np

class Environment():  
	
	background_size = (1600,1600)

	def __init__(self,screen): 
		self.background = pygame.Surface(self.background_size)
		self.background = self.background.convert()
		self.background.fill((250, 250, 250))

		self.background_rect = self.background.get_rect()
		self.area = screen.get_rect()
		self.background_rect.center = self.area.center

		screen.blit(self.background,self.background_rect)

		self.detect_image = pygame.image.load('detected_point.png')

		pygame.draw.line(self.background,(250,0,0),(15,15),(15,self.background_size[1]-15),2)
		pygame.draw.line(self.background,(250,0,0),(15,self.background_size[1]-15),(self.background_size[0]-15,self.background_size[1]-15),2)
		pygame.draw.line(self.background,(250,0,0),(self.background_size[0]-15,self.background_size[1]-15),(self.background_size[0]-15,15),2)
		pygame.draw.line(self.background,(250,0,0),(self.background_size[0]-15,15),(15,15),2)

		for i in range(40,self.background_size[0],40):
			pygame.draw.line(self.background,(166, 166, 166),(i,0),(i,self.background_size[1]),1)
		
		for i in range(40,self.background_size[1],40):
			pygame.draw.line(self.background,(166, 166, 166),(0,i),(self.background_size[0],i),1)
				
	def add_obstacle(self,dx,dy):

		obstacle_position_x = dx +343 - self.background_rect.left
		obstacle_position_y = dy + 343 - self.background_rect.top	
		self.background.blit(self.detect_image,(obstacle_position_x,obstacle_position_y))  

	def move(self,dx,dy):

		self.background_rect = self.background_rect.move((-dx,dy))

	def update(self,screen): 
		screen.blit(self.background,self.background_rect)

class Robot(pygame.sprite.Sprite):
	"""docstring for Robot"""
	
	movement_speed = 10 
	rotation_speed = 7

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.original_image = pygame.image.load('robot_image.png')
		self.original_image = pygame.transform.scale(self.original_image, (48, 48))
		self.image = self.original_image
		self.rect = self.image.get_rect()
		self.area = screen.get_rect()
		self.rect.centerx = self.area.centerx
		self.rect.centery = self.area.centery

		self.current_move = 0  
		self.current_rotation = 0 
		self.current_angle = -90# <<<<<<<<<<<<<<<<<<<

	def compute_movement(delta_position,delta_angle):
		#
		#
		return dx,dy,delta_theta 

	def update(self,env,delta_position,delta_angle): 

		dx,dy,delta_theta = self.compute_movement(delta_position,delta_angle)

		self.current_angle += delta_theta
		current_pos = self.rect.center
		self.image = pygame.transform.rotate(self.original_image,self.current_angle)
		self.rect = self.image.get_rect()
		self.rect.center = current_pos 

		env.move(dx,dy)


class PygameController : 

	position_speed = 10 
	angle_speed = 7 

	def __init__(self):

		self.position_command = 0 
		self.angle_command = 0 

		pygame.init()
		screen = pygame.display.set_mode((700, 700))

		env = Environment(screen)
		robot = Robot()

		env.update(screen)

		allsprites = pygame.sprite.RenderPlain((robot))

	def get_inputs(): 

		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_UP: 
					self.position_command = self.position_speed
				elif event.key == K_DOWN :
					self.position_command = - self.position_speed 
				elif event.key == K_RIGHT : 
					self.angle_command = -self.rotation_speed
				elif event.key == K_LEFT :
					self.angle_command = self.rotation_speed
			
			if event.type == KEYUP : 
				if event.key in (K_UP,K_DOWN):
					self.position_command = 0 
				elif event.key in (K_LEFT,K_RIGHT) : 
					self.angle_command = 0 

	def run(self,position_command,angle_command,delta_position,delta_angle): 
		# DELTA POSITION MUST BE QUEUE 

		while 1:
			get_inputs()
			
			position_command,angle_command = self.position_command,self.angle_command

			allsprites.update(env,delta_position,delta_angle)
		# update environment 
			env.update(screen)
			allsprites.draw(screen)
			pygame.display.flip()




