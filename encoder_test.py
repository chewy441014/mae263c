import RPi.GPIO as io
import time
import datetime
import math

io.setmode(io.BOARD)

# sensor 1
en1_pin = 35
io.setup(en1_pin, io.IN, pull_up_down=io.PUD_UP)

# sensor 2
en2_pin = 33
io.setup(en2_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 1
encoder1_sensors = [en1_pin, en2_pin]
A1_old = 0
encoder1_count = 0

def encoder1Callback(channel):
	# this function is called when an encoder reading is detected
	global A1_old, encoder1_count
	if io.input(channel):
		A = 1
	else:
		A = 0
	if io.input(encoder1_sensors[1]):
		B = 1
	else:
		B = 0
	if A != A1_old:
		if A != B:
			encoder1_count += 1
		else:
			encoder1_count -= 1
	A1_old = A
	
def initializeEncoders():
	global encoder1_count
	encoder1_count = 0;
	
def countstorad(count):
	# returns the joints space angle in radians
	rad = 2*math.pi*count/8/48
	return rad	

io.add_event_detect(en1_pin, io.BOTH, callback=encoder1Callback)
while True:
	print(countstorad(encoder1_count))
	enter = raw_input("Press to continue: ")