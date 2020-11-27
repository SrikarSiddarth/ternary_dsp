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



N = 1024					# length of array for storing continuous-time values
d = [0]*N 					# initializing the data storage array
delay = 0					# stores the delay value
t = []						# trigger array that stores the main data for performing delay
rate = 100					# rate of the main loop
t1 = 0						# to extract the time delay from the graph

def trig(msg):
	global t, delay, t1
	t1 = time.time()
	t = []
	x = random.random()*4 + 1
	delay = x*rate 				# giving a delay of 1-5 seconds
	print('triggered! at a delay of '+str(x)+' seconds.')

def receive(msg):
	global d,t,delay
	if delay>0:
		t += [msg.data]
		delay -= 1
		d = [random.random()-0.5] + d[:N-1]
	else:
		if len(t)>0:
			d = [t[0]]+d[:N-1]
			t.pop(0)
		else:
			d = [msg.data] + d[:N-1]


if __name__ == '__main__':
	rospy.init_node('receiver')
	data_sub = rospy.Subscriber('/data', Float64, receive)
	trig_sub = rospy.Subscriber('/trigger', Empty, trig)
	info_pub = rospy.Publisher('/info', Float64, queue_size = 20)


	# select length index as 0, 1 or 2 for a 7, 13, or 31 length ternary code
	index = 2
	y = [[1,1,1,0,0,1,0],
		[1,1,1,0,1,1,0,0,0,0,1,1,0],
		[1,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0]
		]

	cutoff = [11.5, 15, 17]
	l = len(y[index])
	r = rospy.Rate(rate)
	Smax = 0
	while not rospy.is_shutdown():
		s = 1
		# performing convolution at receiver
		for i in range(l):
			s += d[l-i-1]*y[index][i]
		s = 20*np.log10(abs(s))			# dB scale
		info_pub.publish(s)
		if s>cutoff[index]:
			t1 = time.time()-t1
			print('delay occured in receiving is '+str(t1))
		r.sleep()
	