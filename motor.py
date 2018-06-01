import RPi.GPIO as io
import time

io.setmode(io.BOARD)

in1_pin = 36
in2_pin = 38
en_pin = 40

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
	
clockwise(0)
enter = raw_input("Press return to stop:")
clockwise(10)
enter = raw_input("Press return to stop:")
clockwise(20)
enter = raw_input("Press return to stop:")
clockwise(30)
enter = raw_input("Press return to stop:")
clockwise(40)
enter = raw_input("Press return to stop:")
clockwise(50)
enter = raw_input("Press return to stop:")
clockwise(60)
enter = raw_input("Press return to stop:")
clockwise(70)
enter = raw_input("Press return to stop:")
clockwise(80)
enter = raw_input("Press return to stop:")
clockwise(90)
enter = raw_input("Press return to stop:")
clockwise(100)
enter = raw_input("Press return to stop:")
p1.stop
p2.stop
io.cleanup()