import time
import RPi.GPIO as GPIO
from adafruit_motorkit import MotorKit

kit=MotorKit()

A=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(A, GPIO.IN)

enc = 0

def incr_enc(channel):
	print("detected")
	global enc
	enc+=1

GPIO.add_event_detect(A, GPIO.RISING, callback=incr_enc)

kit.motor3.throttle = 0.2

time.sleep(5)

kit.motor3.throttle=None

print(enc)
