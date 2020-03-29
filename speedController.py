import time
import matplotlib.pyplot as plt

import encoder as enc
from adafruit_motorkit import MotorKit


class SpeedController : 
   
	p_pos = 0.02
	pi_pos = 0.01
	pd_pos = 0.01

	p_angle = 0.02
	pi_angle = 0.01
	pd_angle = 0.01

	def __init__(self,position_speed_goal=0,angle_speed_goal=0): 
		
		self.position_speed_goal = position_speed_goal
		self.angle_speed_goal = angle_speed_goal

		self.position = 0 
		self.angle = 0 
		self.position_speed = 0 
		self.angle_speed = 0 
		self.position_acce = 0 
		self.angle_acce = 0 

		self.actual_position_goal = 0 
		self.actual_angle_goal = 0

		self.iteration = 0 

		self.encoder = enc.Encoder()
		self.encoder.start()

	def set_speed(self,position_speed_goal,angle_speed_goal): 
		
		self.position_speed_goal = position_speed_goal
		self.angle_speed_goal = angle_speed_goal		

	def update_status(self): 
		new_position = self.encoder.get_position()
		new_angle = self. encoder.get_angle()

		self.position_acce = (new_position-self.position) - self.position_speed
		self.angle_acce = (new_angle-self.angle) - self.angle_speed	
	
		self.position_speed = new_position-self.position
		self.angle_speed = new_angle-self.angle

		self.position = new_position
		self.angle = new_angle

		self.actual_position_goal+=self.position_speed_goal
		self.actual_angle_goal+=self.angle_speed_goal

	def compute_controls(self):

		self.update_status()

		v1 = self.p_pos * (self.position_speed_goal-self.position_speed) + self.pi_pos*(self.actual_position_goal-self.position)-self.pd_pos*self.position_acce
		v2 = self.p_angle*(self.angle_speed_goal-self.angle_speed) + self.pi_angle*(self.actual_angle_goal-self.angle)- self.pd_angle*self.angle_acce
		
		#print(self.p_pos * (self.position_speed_goal-self.position_speed),self.pi_pos*(self.actual_position_goal-self.position),self.pd_pos*self. position_acce)

		v_left=v1+v2
		v_right=v1-v2
		
		if (v_left>1):
			v_left=1
		elif (v_left<-1):
			v_left=-1
		if (v_right>1):
			v_right=1
		elif (v_right<-1):
			v_right=-1

		return v_left,v_right#,self.position_speed,self.angle_speed


