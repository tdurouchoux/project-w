import pygame
import time
from threading import Thread
from queue import Queue 

from speedController import SpeedController

speedController = SpeedController()


command_queue = Queue()
delta_position_queue = Queue()

command_queue.put([10,0])


t1 = Thread(target=speedController.run,args=(command_queue,delta_position_queue,))


t1.start()




    