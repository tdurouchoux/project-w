import time
import ADS1256


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


ADS = ADS1256.ADS1256()

global data

data = list(np.zeros(1000))
fig, ax = plt.subplots()
line, = ax.plot(data)
ax.set_ylim(-6,6)

def update(data):
	line.set_ydata(data)
	return line,

def get_data() : 	
	input = ADS.ADS1256_GetChannalValue(7)*5.0/0x7fffff
	return input*5.0/0x7fffff

def oscillo():
	while 1 :
		data.pop(0)
		data.append(get_data())   

		yield data 

ani = animation.FuncAnimation(fig, update, oscillo, interval=10)
plt.show()