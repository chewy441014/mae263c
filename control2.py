def control2(pos_d):
	try:
		# initialize the encoders
		##################################################
		#This is for motor1 control
		##################################################
		tolerance=0.005
		pos_error1=100
        enter = raw_input(" About to move motor 2")
		print("Controlling Motors 2")
		position_error=100
		duty_cycle_2=100
		while abs(position_error) > tolerance:
			# get current position
			pos_current=countstorad(encoder2_count)
			# get position error
			position_error=pos_d[1]-pos_current
			if position_error<0:
				clockwise(100-duty_cycle_2, p3, p4, m2_en_pin)
			elif position_error>0:
				clockwise(duty_cycle_2, p3, p4, m2_en_pin)

        enter = raw_input(" About to move motor 3")
		print("Controlling Motors 3")
		position_error=100
		duty_cycle_3=100
		while abs(position_error) > tolerance:
			# get current position
			pos_current=countstorad(encoder3_count)
			# get position error
			position_error=pos_d[2]-pos_current
			if position_error<0:
				clockwise(duty_cycle_3, p5, p6, m3_en_pin)
			elif position_error>0:
				clockwise(100-duty_cycle_3, p5, p6, m3_en_pin)
		p5.stop()
		p6.stop()

		print("Controlling motor 1")
		while abs(pos_error1) >=tolerance:
			pos_error1=pos_d[0]-countstorad(encoder1_count)
			duty_cycle_1=100
			if pos_error1>0:
				clockwise(duty_cycle_1, p1, p2, m1_en_pin)
			elif pos_error1<0:
				clockwise(100-duty_cycle_1,p1,p2,m1_en_pin)
		p1.stop()
		p2.stop()
		p3.stop()
		p4.stop()
		p5.stop()
		p6.stop()
	except KeyboardInterrupt:
		p1.stop()
		p2.stop()
		p3.stop()
		p4.stop()
		p5.stop()
		p6.stop()
		io.cleanup()