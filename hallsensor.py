#!/usr/bin/python

import time
import datetime
import RPi.GPIO as io

def sensorCallback(channel):
	timestamp = time.time()
	stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
	if io.input(channel):
		print("Sensor HIGH" + stamp)
	else:
		print("Sensor LOW" + stamp)
		
def main():
	sensorCallback(17)
	try:
		while True:
			time.sleep(0.1)
	except KeyboardInterrupt:
		io.cleanup()

io.setmode(io.BCM)
print("Setup GPIO pin as input on GPIO17")
io.setup(17, io.IN, pull_up_down=io.PUD_UP)
io.add_event_detect(17, io.BOTH, callback=sensorCallback, bouncetime=200)

if __name__=="__main__":
	main()