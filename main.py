import pygame
import time
from threading import Thread
from queue import Queue 

from speedController import SpeedController
from pygameController import PygameController
from adafruit_motorkit import MotorKit


def run_motor(motor_command_queue):

    while 1 : 
        v_left,v_right = motor_command_queue.get()

        kit.motor3.throttle = v_left
        kit.motor1.throttle = v_right

pygameController = PygameController()
speedController = SpeedController()
kit = MotorKit()

position_command = 0 
angle_command = 0 
delta_position_queue = Queue()
motor_command_queue = Queue()

t1 = Thread(target=run_motor,args=(motor_command_queue,))
t2 = Thread(target=speedController.run,args=(position_command,angle_command,delta_position_queue,motor_command_queue,))
t3 = Thread(target=pygameController.run,args=(position_command,angle_command,delta_position_queue,))

t1.start()
t2.start()
t3.start()

kit.motor3.throttle=None
kit.motor1.throttle=None

pygame.quit()
    