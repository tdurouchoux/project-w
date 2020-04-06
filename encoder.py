import RPi.GPIO as GPIO

left_A = 26
left_B = 20 
right_A = 19
right_B = 16

class Encoder:

	def __init__(self) : 
		self.left_enc = 0
		self.right_enc = 0

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(left_A, GPIO.IN)
		GPIO.setup(left_B, GPIO.IN)
		GPIO.setup(right_A, GPIO.IN)
		GPIO.setup(right_B, GPIO.IN)

	def left_both_A(self,channel):
		if (GPIO.input(left_B)==GPIO.input(left_A)) :
			self.left_enc-=1
		else :  
			self.left_enc+=1

	def left_both_B(self,channel):                                                                                                                                                                                                                                                                                                 
		if (GPIO.input(left_B)!=GPIO.input(left_A)) :                                                                                                                   
			self.left_enc-=1                                                                                                                                             
		else :                                                                                                                                                          
			self.left_enc+=1

	def right_both_A(self,channel):
		#print('coucou')
		if (GPIO.input(right_B)!=GPIO.input(right_A)) :
			self.right_enc-=1
		else :
			self.right_enc+=1

	def right_both_B(self,channel):
		#print('connasse')
		if (GPIO.input(right_B)==GPIO.input(right_A)) :
			self.right_enc-=1
		else :
			self.right_enc+=1

	def start(self): 
		GPIO.add_event_detect(left_A, GPIO.BOTH, callback=self.left_both_A)
		GPIO.add_event_detect(left_B, GPIO.BOTH, callback=self.left_both_B) 
		GPIO.add_event_detect(right_A,GPIO.BOTH, callback=self.right_both_A)
		GPIO.add_event_detect(right_B,GPIO.BOTH, callback=self.right_both_B)

	def reset(self): 
		GPIO.remove_event_detect(left_A)
		GPIO.remove_event_detect(left_B) 
		GPIO.remove_event_detect(right_A)
		GPIO.remove_event_detect(right_B)		

		self.left_enc = 0 
		self.right_enc = 0 

	def get_position(self):
		return (self.right_enc + self.left_enc)/2

	def get_angle(self) : 
		return self.left_enc-self.right_enc



