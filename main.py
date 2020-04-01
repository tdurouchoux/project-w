import pygame
import time
from threading import Thread
from queue import Queue 

from speedController import SpeedController
from pygameController import PygameController




pygameController = PygameController()
speedController = SpeedController()

command_queue = Queue()
delta_position_queue = Queue()

t1 = Thread(target=speedController.run,args=(command_queue,delta_position_queue,))
t2 = Thread(target=pygameController.run,args=(command_queue,delta_position_queue,))

t1.start()
t2.start()



    