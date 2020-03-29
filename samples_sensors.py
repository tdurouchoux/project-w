
import time
import ADS1256
import RPi.GPIO as GPIO
import json


try:
	ADC = ADS1256.ADS1256()
	ADC.ADS1256_init()
	
	dict_dist = dict()
	current_dist = float(input('current mesured distance ? '))


	while current_dist >= 0 : 

		for i in range(4): 
			print('remaining time (s):',3-i)
			time.sleep(1)

		ir1 = ADC.ADS1256_GetChannalValue(2)*5.0/0x7fffff
		#ir2 = ADC.ADS1256_GetChannalValue(3)
		#ir3 = ADC.ADS1256_GetChannalValue(4)
		
		dict_dist[current_dist] = ir1 
		print(ir1)
		current_dist = float(input('current mesured distance ? '))

	print('measure section completed')


	with open('result.json', 'w') as f:
		json.dump(dict_dist, f)



except :
	GPIO.cleanup()