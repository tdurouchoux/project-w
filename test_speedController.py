from speedController import SpeedController
import time

from speedController import SpeedController
from adafruit_motorkit import MotorKit

controller = SpeedController()
kit = MotorKit()

controller.set_speed(7,0)

for i in range(100):
	v_left, v_right = controller.compute_controls()

	kit.motor3.throttle = v_left
	kit.motor1.throttle = v_right
	time.sleep(0.05)

kit.motor3.throttle=None
kit.motor1.throttle=None