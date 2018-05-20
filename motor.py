import RPi.GPIO as io
import time

io.setmode(io.BOARD)

in1_pin = 8
in2_pin = 10
en_pin = 12

chan_list = [in1_pin, in2_pin, en_pin]

io.setwarnings(False)
io.setup(chan_list, io.OUT)
hz = 100
dt = 1/hz

p1 = io.PWM(in1_pin, hz)
p2 = io.PWM(in2_pin, hz)

def clockwise(duty):
	io.output(en_pin, io.HIGH)
	p1.start(duty)
	time.sleep(dt)
	p2.start(duty)
	
	
def counter_clockwise(duty):
	io.output(en_pin, io.HIGH)
	p2.start(duty)
	time.sleep(dt)
	p1.start(duty)	
	
clockwise(50)
enter = raw_input("Press return to stop:")
counter_clockwise(50)
enter = raw_input("Press return to stop:")
p1.stop
p2.stop
io.setup(chan_list, io.IN)
io.cleanup()