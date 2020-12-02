#!/usr/bin/env python
#
#
# This is the transmitter for simulating the ternary pulse compression code


import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Empty
import random
import numpy as np

print('\n....Tranmission Started....\n')
t = 0
i = 0
def trig(msg):
	global t,i
	t = 1
	i = 0
	# print('triggered!')

if __name__ == '__main__':
	rospy.init_node('transmitter')
	index = rospy.get_param('~length',0)
	code_pub = rospy.Publisher('/data', Float64, queue_size = 20)
	sub = rospy.Subscriber('/trigger', Empty, trig)
	rate = 400
	# 7 - length code
	# x = [1,1,1,-1,-1,1,-1]
	# 13 - length code
	# x = [1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1]
	# 31 - length code
	# x = [1,1,1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1]

	# ternary codes
	x = [[1,1,1,-1,-1,1,-1],
		[1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1],
		[1,1,1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1]]
	
	# barker 7 and 13 bit code 
	# x = [[1,1,1,-1,-1,1,-1],
	# 	[1,1,1,1,1,-1,-1,1,1,-1,1,-1,1]]

	# input pulse width
	pw = 100
	# frequency of signal
	f = 20
	l = len(x[index])*pw
	r = rospy.Rate(rate)
	while not rospy.is_shutdown():
		if t:
			# code_pub.publish(x[index][i])
			code_pub.publish(np.cos(2*np.pi*i/l*f + 0.5*(1-x[index][int(i/pw)])*np.pi))
			i += 1
			if i==l:
				# print('message published')
				t = 0
		else:
			code_pub.publish(0)
		r.sleep()