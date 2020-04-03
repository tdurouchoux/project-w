

import time
import irSensors
import RPi.GPIO as GPIO

irSensors = irSensors.IrSensors()

for i in range(1000):
	print(irSensors.get_distance_sensor(sensor='left'))
	time.sleep(0.02)

GPIO.cleanup()