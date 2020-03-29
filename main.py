import pygame
import time

from speedController import SpeedController
from adafruit_motorkit import MotorKit

controller = SpeedController()
kit = MotorKit()

pygame.init()
pygame.display.set_mode()

position_speed_goal = 0 
angle_speed_goal = 0 

step = 0.25



def update_speed(position_speed_goal,angle_speed_goal) :

    status_keyboard = pygame.key.get_pressed()
    is_pressed_up = status_keyboard[pygame.K_UP]
    is_pressed_down = status_keyboard[pygame.K_DOWN]
    is_pressed_left = status_keyboard[pygame.K_LEFT]
    is_pressed_right = status_keyboard[pygame.K_RIGHT] 

    if is_pressed_right: 
        if angle_speed_goal<24:
            angle_speed_goal+=step/2 
    elif is_pressed_left: 
        if angle_speed_goal>-24:
            angle_speed_goal-=step/2

    if angle_speed_goal>0 and not is_pressed_right:
        angle_speed_goal-=step/2 
    elif angle_speed_goal<0 and not is_pressed_left: 
        angle_speed_goal+=step/2 
    
    if is_pressed_up:
        if position_speed_goal<12:
            position_speed_goal+=step
    elif is_pressed_down:
        if position_speed_goal>-12:
            position_speed_goal-=step
    
    if position_speed_goal>0 and not is_pressed_up:
        position_speed_goal-=step
    elif position_speed_goal<0 and not is_pressed_down:
        position_speed_goal+=step

    pygame.event.pump()

    return position_speed_goal,angle_speed_goal, status_keyboard[pygame.K_q]

stop = False

while not stop:
    
    position_speed_goal,angle_speed_goal,stop = update_speed(position_speed_goal,angle_speed_goal)

    controller.set_speed(position_speed_goal,angle_speed_goal)
    v_left, v_right = controller.compute_controls()

    kit.motor3.throttle = v_left
    kit.motor1.throttle = v_right

    time.sleep(0.05)

kit.motor3.throttle=None
kit.motor1.throttle=None

pygame.quit()
    