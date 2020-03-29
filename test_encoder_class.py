import encoder 
import time 

encoder = encoder.Encoder()

encoder.start()

print('angle :', encoder.get_angle())
print('position :',encoder.get_position())

print('---------------------')

time.sleep(2)

print('angle :', encoder.get_angle())
print('position :',encoder.get_position())

print('---------------------')

time.sleep(2)

print('angle :', encoder.get_angle())
print('position :',encoder.get_position())

print('---------------------')

time.sleep(2)
encoder.reset()

print('angle :', encoder.get_angle())
print('position :',encoder.get_position())
