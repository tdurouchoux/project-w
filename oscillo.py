import time
import ADS1256


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


ADS = ADS1256.ADS1256()
ADS.ADS1256_init()

global data

data = list(np.zeros(100))
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_ylim(-6,6)

def update(data):
	line.set_ydata(data)
	return line,

def get_data() : 	
	input_ADS = ADS.ADS1256_GetChannalValue(7)
	return input_ADS*5.0/0x7fffff

def oscillo():
	data.pop(0)
	data.append(get_data())   

	yield data 

ani = animation.FuncAnimation(fig, update, oscillo, interval=1)
plt.show()