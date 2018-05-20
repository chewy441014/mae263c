#!/usr/bin/python

import time
import datetime
import RPi.GPIO as io
import math

def sensorCallback(channel):
	timestamp = time.time()
	stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S:%f')
	if io.input(channel):
		#print("Sensor HIGH" + stamp)
		sig = 1
	else:
		#print("Sensor LOW" + stamp)
		sig = 0
	return sig
	
def countstorad(count):
	rad = 2*math.pi*count/9/48
	return rad	

def main():
	counter = 0
	A = sensorCallback(22)
	try:
		while True:
			time.sleep(0.1)
			Anew = sensorCallback(22)
			B = sensorCallback(15)
			if A != Anew:
				if B != A:
					counter+=1
				else
					counter-=1
	except KeyboardInterrupt:
		io.cleanup()

io.setmode(io.BOARD)
print("Setup GPIO pin as input on GPIO17")
io.setup(22, io.IN, pull_up_down=io.PUD_UP)
io.add_event_detect(22, io.BOTH, callback=sensorCallback, bouncetime=200)
io.setup(15, io.IN, pull_up_down=io.PUD_UP)
io.add_event_detect(15, io.BOTH, callback=sensorCallback, bouncetime=200)

if __name__=="__main__":
	main()