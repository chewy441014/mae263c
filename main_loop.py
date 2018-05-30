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
p1 = io.PWM(m1_in1_pin, hz)
p2 = io.PWM(m1_in2_pin, hz)

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
	# returns the joints space angle in radians
	rad = 2*math.pi*count/8/kr
	return rad	

def sensorCallback(channel):
	# this function is called when an encoder reading is detected
	if io.input(channel):
		sig = 1
	else:
		sig = 0
	return sig
	
def getpose(key_d):
	# calculate the inverse kinematics
	# return the joint space position of desired key
	# return pose_desired
	
def control1(pos_d):
	# initialize the encoders
	# set parameters of robot
	a1,a2=
	len_link1=
	len_link2=
	m_link1=
	m_link2=
	m_motor=
	k_t=k_e=k=0.44
	R=5.5#resistance
	V=
	# while error < tolerance
		# get current position
		# estimate g(q)
		g_q=(m_link1*len_link1+m_motor*a1+m_link2*a1)*math.cos(JOINT_ANGLE_1)+m_link2*len_link2*math.cos(JOINT_ANGLE_1+JOINT_ANGLE_2)
		# calculate position error
		# u = PD control with gravity compensation
		u=g_q+K_p*POSITION_ERROR-K_d*ANGULAR_VELOCITY
		# duty = function(u)
		V_d=R*u/k+k*ANGULAR_VELOCITY
		duty=V_d/V*100
		# move the motors according to duty

def taskcontrol(string_d):
	# for each key in string_desired
		# getpose(key_desired)
		# control(pose_desired)
		# control(intermediate home position)
	# end for loop
	# return to global home position

def setparameter():
