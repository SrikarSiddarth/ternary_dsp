#!/usr/bin/env python
#
#
# This is the transmitter for simulating the ternary pulse compression code


import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Empty
import random

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
	index = rospy.get_param('~length',2)
	code_pub = rospy.Publisher('/data', Float64, queue_size = 20)
	sub = rospy.Subscriber('/trigger', Empty, trig)

	# 7 - length code
	# x = [1,1,1,-1,-1,1,-1]
	# 13 - length code
	# x = [1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1]
	# 31 - length code
	# x = [1,1,1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1]

	
	x = [[1,1,1,-1,-1,1,-1],
		[1,1,1,-1,1,1,-1,-1,-1,-1,1,1,-1],
		[1,1,1,1,-1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1,1,-1,-1,1,-1,-1,1,1,1,-1,1,1,-1]]
	r = rospy.Rate(100)
	while not rospy.is_shutdown():
		if t:
			code_pub.publish(x[index][i])
			i += 1
			if i==len(x[index]):
				# print('message published')
				t = 0
		else:
			code_pub.publish(0)		# generates random number between -0.5 and 0.5
		r.sleep()