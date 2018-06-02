import RPi.GPIO as io
import time

io.setmode(io.BOARD)

in1_pin = 12
in2_pin = 16
en_pin = 18

chan_list = [in1_pin, in2_pin, en_pin]

io.setup(chan_list, io.OUT)
hz = 50
dt = 1/hz

p1 = io.PWM(in1_pin, hz)
p2 = io.PWM(in2_pin, hz)

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
	
print("duty is 0")
clockwise(0,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 10")
clockwise(10,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 20")
clockwise(20,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 30")
clockwise(30,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 40")
clockwise(40,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 50")
clockwise(50,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 60")
clockwise(60,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 70")
clockwise(70,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 80")
clockwise(80,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 90")
clockwise(90,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
print("duty is 100")
clockwise(100,p1,p2,en_pin)
enter = raw_input("Press return to stop:")
p1.stop
p2.stop
io.cleanup()