import time
from encoder import Encoder

encoder = Encoder()

encoder.start()

time.sleep(6)

print("position :", encoder.get_position())
print("angle :",encoder.get_angle())