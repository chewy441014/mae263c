import RPi.GPIO as io
io.setmode(io.BOARD)

in1_pin = 16
in2_pin = 18
en_pin = 10


GPIO.setup(chan_list, GPIO.OUT)

def set(property, value)
	try:
		f = open("/sys/class/rpi-pwm/pwm0" + property, 'w')
		f.write(value)
		f.close()
	except:
		print("Error writing to: " + property + "value: " + value)

set("delayed", "0")
set("mode", "pwm")
set("frequency", "500")
set("active", "1")

def clockwise():
	io.output(in1_pin, True)
	io.output(in2_pin, False)
	
def counter_clockwise():
	io.output(in1_pin, False)
	io.output(in2_pin, True)
	
while True:
	cmd = raw_input("Command, f/r 0...9, E.g f5 :")
	direction = cmd[0]
	if direction == "f":
		clockwise()
	else:
		counter_clockwise()
	speed = int(cmd[1]) * 11
	set("duty", str(speed))