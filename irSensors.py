
import time
import ADS1256
import json
import numpy as np

class IrSensors : 

	sensors = ['center','left','right']
	sensors_channel = {'center':2,'left':3,'right':4}
	sensors_limits = {'center':120,'left':120,'right':110}

	def __init__(self): 
		
		with open('sensors_regression_weights.json') as f : 
			self.regression_weights = json.loads(f.read())

		self.ADS = ADS1256.ADS1256()
		self.ADS.ADS1256_init()


	def voltage_to_distance(self,y,sensor='center'):
    
		b0 = self.regression_weights[sensor]['constant']
		a = self.regression_weights[sensor]['linear']
		c = self.regression_weights[sensor]['inverse']
		d = self.regression_weights[sensor]['inverse_2'] 
		b = b0-y
		delta_0 = b**2-3*a*c

		delta_1 = 2*(b**3)-9*a*b*c+27*(a**2)*d
		C = ((delta_1+(delta_1**2-4*(delta_0**3))**(1/2))/2)**(1/3)


		return np.real(-(b+C+delta_0/C)/(3*a))


	def get_distance_sensor(self,sensor='center'):

		ir1 = self.ADS.ADS1256_GetChannalValue(self.sensors_channel[sensor])*5.0/0x7fffff
		time.sleep(0.001)
		ir2 = self.ADS.ADS1256_GetChannalValue(self.sensors_channel[sensor])*5.0/0x7fffff
		time.sleep(0.001)
		ir3 = self.ADS.ADS1256_GetChannalValue(self.sensors_channel[sensor])*5.0/0x7fffff

		distance = self.voltage_to_distance(np.mean([ir1,ir2,ir3]),sensor=sensor)
		if distance> self.sensors_limits[sensor] : 
			return -1
		else : 
			print(ir1,ir2,ir3)
			return distance

	def get_distance_all(self): 

		return [self.get_distance_sensor(sensor=current_sensor) for current_sensor in self.sensors]