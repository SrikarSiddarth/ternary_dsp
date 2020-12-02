#!/usr/bin/env python
#
#
# Receiver for ternary pulse compression code

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Empty
import random
import time
import numpy as np


print('\n....Receiver Started....\n')



N = 8192					# length of array for storing continuous-time values
d = [0]*N 					# initializing the data storage array
# delay = 0					# stores the delay value
# t = []						# trigger array that stores the main data for performing delay
rate = 400					# rate of the main loop
t1 = []						# to extract the time delay from the graph
c = 0

def trig(msg):
	global t1, c
	t1 += [time.time()]
	c = 1


def receive(msg):
	global d
	d = [msg.data] + d[:N-1]

if __name__ == '__main__':
	rospy.init_node('receiver')
	index = rospy.get_param('~length',0)
	data_sub = rospy.Subscriber('/channel', Float64, receive)
	trig_sub = rospy.Subscriber('/trigger', Empty, trig)
	info_pub = rospy.Publisher('/info', Float64, queue_size = 20)
	pw = 100
	f = 20

	tolerance = [1.74,0,0]
	tolerance_b = [1.75]
	
	# ternary code
	y = [[1,1,1,0,0,1,0],
		[1,0,1,0,1,1,0,0,0,0,1,1,0],
		[1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0]
		]

	# # barker code
	# y = [[1,1,1,-1,-1,1,-1],
	# 	[1,1,1,1,1,-1,-1,1,1,-1,1,-1,1]]


	cutoff = [200, 15, 17]
	cutoff_b = [300]
	# l = len(y[index])
	l = len(y[index])*pw
	r = rospy.Rate(rate)
	
	while not rospy.is_shutdown():
		s = 1


		# performing convolution at receiver
		for i in range(l):
			# s += d[l-i-1]*y[index][i]
			s += d[l-i-1]*np.cos(2*np.pi*i/l*f + 0.5*(1-y[index][int(i/pw)])*np.pi)
		
		# s = 20*np.log10(abs(s))			# dB scale
		
		info_pub.publish(s)

		# for ternary code
		# if s>cutoff[index] and c==1:
		# 	print('delay occured in receiving is '+str(time.time()-t1[0]-tolerance[index]))
		# 	# print('delay occured in receiving is '+str(time.time()-t1[0]))
		# 	t1.pop(0)
		# 	c=0

		# for barker code
		# if s>cutoff_b[index] and c==1:
		# 	print('delay occured in receiving is '+str(time.time()-t1[0]-tolerance_b[index]))
		# 	# print('delay occured in receiving is '+str(time.time()-t1[0]))
		# 	t1.pop(0)
		# 	c=0

			# print(s)
		r.sleep()