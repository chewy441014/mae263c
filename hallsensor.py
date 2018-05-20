#!/usr/bin/python

import time
import datetime
import RPi.GPIO as io

def sensorCallback(channel):
	timestamp = time.time()
	stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
	if io.input(channel):
		print("Sensor HIGH" + stamp)
		sig = 1
	else:
		print("Sensor LOW" + stamp)
		sig = 0
	return sig
	
def main():
	A = sensorCallback(22)
	B = sensorCallback(15)
	try:
		while True:
			time.sleep(0.1)
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