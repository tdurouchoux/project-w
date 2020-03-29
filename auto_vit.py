import sys
import time
import matplotlib.pyplot as plt

import encoder as enc
from adafruit_motorkit import MotorKit


encoder = enc.Encoder()
kit = MotorKit()

p_pos = float(sys.argv[1])
pi_pos = float(sys.argv[2])
pd_pos = float(sys.argv[3])

p_angle = float(sys.argv[4])
pi_angle = float(sys.argv[5])
pd_angle = float(sys.argv[6])

position_speed_goal = float(sys.argv[7])
angle_speed_goal = float(sys.argv[8])

encoder.start()

position = encoder.get_position()
angle = encoder.get_angle()

position_speed,angle_speed = 0,0

position_speed_array = [0]
angle_speed_array = [0]

v_left_array = [0]
v_right_array =[0]

def compute_pi(position_speed_goal,angle_speed_goal,position,angle,position_speed,angle_speed,i):
	
	new_position = encoder.get_position()
	position_acce = (new_position-position) - position_speed
	position_speed = new_position-position
	position = new_position

	new_angle = encoder.get_angle()
	angle_acce = (new_angle-angle) - angle_speed
	angle_speed = new_angle-angle
	angle = new_angle


	print('position_speed :', position_speed)
	print('angle speed :',angle_speed)
	print('---------------------------')

	v1 = p_pos * (position_speed_goal-position_speed) + pi_pos*(i*position_speed_goal-position)-pd_pos*position_acce
	v2 = p_angle*(angle_speed_goal-angle_speed) + pi_angle*(i*angle_speed_goal-angle)- pd_angle*angle_acce
	
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
	
	position_speed_array.append(position_speed)
	angle_speed_array.append(angle_speed)

	v_left_array.append(v_left)
	v_right_array.append(v_right)

	return position,angle,position_speed,angle_speed

for i in range(150):
	time.sleep(0.05)
	position,angle,position_speed,angle_speed = compute_pi(position_speed_goal,angle_speed_goal,position,angle,position_speed,angle_speed,i)

kit.motor3.throttle=None
kit.motor1.throttle=None

encoder.reset()

print('printing speed and angle speed evolution')

plt.figure()
plt.plot(position_speed_array,'b',label='actual speed') 
plt.plot([position_speed_goal]*len(position_speed_array),'r',label='speed command')
plt.title('position speed evolution')
plt.savefig('position.png')

plt.figure()
plt.plot(angle_speed_array,'b',label='actual speed') 
plt.plot([angle_speed_goal]*len(angle_speed_array),'r',label='speed command')
plt.title('angle speed evolution')
plt.savefig('angle.png')

plt.figure()
plt.plot(v_left_array,label='left motor control')
plt.plot(v_right_array,label='right motor control')
plt.title('motors controls evolution')
plt.savefig('motors.png')








