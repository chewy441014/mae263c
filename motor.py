import RPi.GPIO as io
import time

io.setmode(io.BOARD)

in1_pin = 16
in2_pin = 18
en_pin = 12

chan_list = [in1_pin, in2_pin, en_pin]

io.setup(chan_list, io.OUT)
print("Set pins as outputs")
hz = 50
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
	
clockwise(100)
enter = raw_input("Press return to stop:")
counter_clockwise(100)
enter = raw_input("Press return to stop:")
p1.stop
p2.stop
io.cleanup()