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

# sensor 3
en3_pin = 31
io.setup(en3_pin, io.IN, pull_up_down=io.PUD_UP)

# sensor 4
en4_pin = 29
io.setup(en4_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 2
encoder2_sensors = [en3_pin, en4_pin]
A2_old = 0
encoder2_count = 0

# sensor 5
en5_pin = 15
io.setup(en5_pin, io.IN, pull_up_down=io.PUD_UP)

# sensor 6
en6_pin = 13
io.setup(en6_pin, io.IN, pull_up_down=io.PUD_UP)

# encoder 3
encoder3_sensors = [en5_pin, en6_pin]
A3_old = 0
encoder3_count = 0

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
	
def initializeEncoders():
	global encoder2_count, encoder3_count
	encoder2_count = 0
	encoder3_count = -math.pi/2
	
def resetEncoders():
	global encoder1_count, encoder2_count, encoder3_count
	encoder1_count = 0
	encoder2_count = 0
	encoder3_count = -math.pi/2

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
io.add_event_detect(en1_pin, io.BOTH, callback=encoder1Callback)
	
def encoder2Callback(channel):
	# this function is called when an encoder reading is detected
	global A2_old, encoder2_count
	if io.input(channel):
		A = 1
	else:
		A = 0
	if io.input(encoder2_sensors[1]):
		B = 1
	else:
		B = 0
	if A != A2_old:
		if A != B:
			encoder2_count += 1
		else:
			encoder2_count -= 1
	A2_old = A
io.add_event_detect(en3_pin, io.BOTH, callback=encoder2Callback)

def encoder3Callback(channel):
	# this function is called when an encoder reading is detected
	global A3_old, encoder3_count
	if io.input(channel):
		A = 1
	else:
		A = 0
	if io.input(encoder3_sensors[1]):
		B = 1
	else:
		B = 0
	if A != A3_old:
		if A != B:
			encoder3_count += 1
		else:
			encoder3_count -= 1
	A3_old = A
io.add_event_detect(en5_pin, io.BOTH, callback=encoder3Callback)

def getpose(key_d):
	# calculate the inverse kinematics
	# return the joint space position of desired key
	# return pose_desired
	
def control1(pos_d):
	# initialize the encoders
	# set parameters of robot
	a1,a2=0.115,0.064
	len_link1=0.07
	len_link2=0.04
	m_link1=0.005
	m_link2=0.003
	m_motor=0.06
	k=0.048
	R=3.6
	V=5
	K_p,K_d=2.5,1
	tolerance=0.1
	while error < tolerance
		# get current position
		# estimate g(q)
		g_q=[(m_link1*len_link1+m_motor*a1+m_link2*a1)*math.cos(JOINT_ANGLE_1)+m_link2*len_link2*math.cos(JOINT_ANGLE_1+JOINT_ANGLE_2),\
		m_link2*len_link2*math.cos(JOINT_ANGLE_1+JOINT_ANGLE_2)]
		# calculate position error
		POSITION_ERROR=pos_d-pos_current
		# u = PD control with gravity compensation
		u=[g_q[0]+K_p*POSITION_ERROR-K_d*ANGULAR_VELOCITY,\
		g_q[1]+K_p*POSITION_ERROR-K_d*ANGULAR_VELOCITY]
		for i in range(2):
			if u[i]>=0.08:
				u[i]=0.08
			elif u[i]<=-0.08:
				u[i]=-0.08
		
		# duty = function(u)
		V_d=[R*u[0]/k+k*ANGULAR_VELOCITY,R*u[1]/k+k*ANGULAR_VELOCITY]
		duty=[V_d[0]/V*100,V_d[1]/V*100]

		# move the motors according to duty
		#motor1 duty cycle ##############################
		if duty[0]>0:
			if duty[0]>=100:
				duty[0]=100
			elif duty[0]<=60:
				duty[0]=
			clockwise(duty, p1, p2, m1_en_pin)
		else:
			if duty[0]<=-100:
				duty[0]=100
			elif duty[0]>=-60:
				duty[0]=
			else:
				duty[0]=-duty[0]
			counter_clockwise(duty,p1,p2,m1_en_pin)
		###################################################
		#motor2 duty cycle ################################
		if duty[1]>0:
			if duty[1]>=100:
				duty[1]=100
			elif duty[1]<=60:
				duty[1]=
			clockwise(duty, p3, p4, m2_en_pin)
		else:
			if duty[1]<=-100:
				duty[1]=100
			elif duty[1]>=-60:
				duty[1]=
			else:
				duty[1]=-duty[1]
			counter_clockwise(duty,p3,p4,m2_en_pin)
		####################################################
		


def taskcontrol(string_d):
	# for each key in string_desired
		# getpose(key_desired)
		# control(pose_desired)
		# control(intermediate home position)
	# end for loop
	# return to global home position;
def setparameter():
