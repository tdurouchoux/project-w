import sys
import time
import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit

kit=MotorKit()

left_A = 26
left_B = 20 
right_A = 19
right_B = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(left_A, GPIO.IN)
GPIO.setup(left_B, GPIO.IN)
GPIO.setup(right_A, GPIO.IN)
GPIO.setup(right_B, GPIO.IN)

left_enc = 0
right_enc = 0
forward_enc_int=0
angle_enc_int=0
p = float(sys.argv[1])
#0.005
pi = float(sys.argv[2])
goal = 200
goal_angle = 0
p_angle =float(sys.argv[3])
#0.004
pi_angle = float(sys.argv[4])
def left_both_A(channel):
	global left_enc
	if (GPIO.input(left_B)==GPIO.input(left_A)) :
		left_enc-=1
	else :  
		left_enc+=1

def left_both_B(channel):                                                                                                                                               
        global left_enc                                                                                                                                                 
        if (GPIO.input(left_B)!=GPIO.input(left_A)) :                                                                                                                   
                left_enc-=1                                                                                                                                             
        else :                                                                                                                                                          
                left_enc+=1

def right_both_A(channel):
	global right_enc
	if (GPIO.input(right_B)!=GPIO.input(right_A)) :
		right_enc-=1
	else :
		right_enc+=1

def right_both_B(channel):
	global right_enc
	if (GPIO.input(right_B)==GPIO.input(right_A)) :
		right_enc-=1
	else :
		right_enc+=1

GPIO.add_event_detect(left_A, GPIO.BOTH, callback=left_both_A)
GPIO.add_event_detect(left_B, GPIO.BOTH, callback=left_both_B) 
GPIO.add_event_detect(right_A,GPIO.BOTH, callback=right_both_A)
GPIO.add_event_detect(right_B,GPIO.BOTH, callback=right_both_B)

def compute_pid(p,pi,goal,p_angle,pi_angle,goal_angle,right_enc, left_enc):
	global forward_enc_int
	global angle_enc_int
	
	forward_enc = (right_enc + left_enc)/2
	forward_enc_int+= forward_enc
	angle_enc = (left_enc-right_enc)
	angle_enc_int+=angle_enc
	
	v1 = p *(goal-forward_enc) + (pi*forward_enc_int) 
	v2 = p_angle*(goal_angle-angle_enc) + pi*angle_enc_int
	
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
	
	kit.motor3.throttle = v_left
	kit.motor1.throttle = v_right

for i in range(150):
	time.sleep(0.05)
	compute_pid(p,pi,goal,p_angle,pi_angle,goal_angle,right_enc,left_enc)

kit.motor3.throttle=None
kit.motor1.throttle=None

GPIO.remove_event_detect(left_A)
GPIO.remove_event_detect(left_B)
GPIO.remove_event_detect(right_A)
GPIO.remove_event_detect(right_B)
GPIO.cleanup()

print("left")
print(left_enc)
print("right")
print(right_enc)
