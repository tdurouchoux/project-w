import pygame
import time
from threading import Thread
from queue import Queue 

from speedController import SpeedController
from pygameController import PygameController
from irSensors import IrSensors 



pygameController = PygameController()
speedController = SpeedController()
irSensors = IrSensors()

command_queue = Queue()
delta_position_queue = Queue()
detected_object_queue = Queue()

t1 = Thread(target=speedController.run,args=(command_queue,delta_position_queue,))
t2 = Thread(target=pygameController.run,args=(command_queue,delta_position_queue,detected_object_queue,))
t3 = Thread(target=irSensors.run,args=(detected_object_queue,))

t1.start()
t2.start()
t3.start()



    