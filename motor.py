import RPi.GPIO as io
import time

io.setmode(io.BOARD)

in1_pin = 16
in2_pin = 18
en_pin = 10

chan_list = [in1_pin, in2_pin, en_pin]

io.setup(chan_list, io.OUT)
hz = 100
dt = 1/hz

p1 = io.PWM(in1_pin, hz)
p2 = io.PWM(in2_pin, hz)

def clockwise(duty):
	p1.start(duty)
	time.sleep(dt)
	p2.start(duty)
	
	
def counter_clockwise(duty):
	p2.start(duty)
	time.sleep(dt)
	p1.start(duty)	
	
clockwise(50)
input('Press return to stop:')
p1.stop
p2.stop
io.cleanup()