import time
from adafruit_motorkit import MotorKit
kit=MotorKit()
kit.motor1.throttle=-0.4
kit.motor3.throttle=-0.4
time.sleep(3)
kit.motor1.throttle=None
kit.motor3.throttle=None

