import RPi.GPIO as io
import time
import datetime
import math

io.setmode(io.BOARD)

hz = 50
dt = 1/hz
kr = 48

# motor 1
m1_in1_pin = 12
m1_in2_pin = 16
m1_en_pin = 18
chan_list = [m1_en_pin, m1_in1_pin, m1_in2_pin]
io.setup(chan_list, io.OUT)
p1 = io.PWM(in1_pin, hz)
p2 = io.PWM(in2_pin, hz)

# motor 2
m2_in1_pin = 25
m2_in2_pin = 32
m2_en_pin = 36
chan_list = [m2_en_pin, m2_in1_pin, m2_in2_pin]
io.setup(chan_list, io.OUT)
p3 = io.PWM(m2_in1_pin, hz)
p4 = io.PWM(m2_in2_pin, hz)

# motor 3
m3_in1_pin = 38
m3_in2_pin = 40
m3_en_pin = 37
chan_list = [m3_en_pin, m3_in1_pin, m3_in2_pin]
io.setup(chan_list, io.OUT)
p5 = io.PWM(m3_in1_pin, hz)
p6 = io.PWM(m3_in2_pin, hz)

# encoder 1
en1_pin = 35
io.setup(en1_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 2
en2_pin = 33
io.setup(en2_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 3
en3_pin = 31
io.setup(en3_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 4
en4_pin = 29
io.setup(en4_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 5
en5_pin = 15
io.setup(en5_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 6
en6_pin = 13
io.setup(en6_pin, io.IN, pull_up_down=io.PUD_UP)

def clockwise(duty, pwm1, pwm2, en_pin):
	io.output(en_pin, io.HIGH)
	pwm1.start(duty)
	time.sleep(duty/100*dt)
	pwm2.start(100-duty)
	
def counter_clockwise(duty, pwm1, pwm2, en_pin):
	io.output(en_pin, io.HIGH)
	pwm2.start(duty)
	time.sleep(duty/100*dt)
	pwm1.start(100-duty)	

def countstorad(count):
	rad = 2*math.pi*count/8/kr
	return rad	

def sensorCallback(channel):
	if io.input(channel):
		sig = 1
	else:
		sig = 0
	return sig
	
def getpose(key_d):
	pose = [1,1]
	return pose
	
def control1(pos_d):
	# initialize the encoders
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
				else:
					counter-=1
			angle = countstorad(counter)
			print("Position: ")
			print(counter)
			print(angle)
			# the above code gives the joint angle of one joint
			# we need all joint angles, so that we can generate the error
			# in order to do control
	except KeyboardInterrupt:
		io.cleanup()

clockwise(100)
time.sleep(0.1)
p1.stop
p2.stop