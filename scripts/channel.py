#!/usr/bin/env python
#
# The Channel node tries to replicate a real channel by providing sufficient delay to a signal
#
#

import rospy
import random
from std_msgs.msg import Float64
from std_msgs.msg import Empty


msg = """
....Channel Activated!....
"""

rate = 400								# rate at which messages are published
t = []									# trigger array
index = 0								# index determines the length of the ternary code
trig = 0								# trigger indicator
pw = 100								# pulse width
lengths = [7,13,31]						# 
length = 0								# stores the length of signals
delay_time = 2							# standard delay
delay = []								# delay array
delayed_data = 0						# stores the delayed version of the signal that is to be published


def fromTransmitter(msg):
	global trig, length, index, delay, t, delay_time, rate
	if trig:
		t.append([])
		delay.append(delay_time*rate)
		# length = lengths[index]
		length = lengths[index]*pw
		trig = 0
	if length>0:
		if len(t)==0:
			t.append([msg.data])
		else:
			t[-1].append(msg.data)
		length -= 1




def trigger(msg):
	global trig
	trig = 1


if __name__ == '__main__':
	rospy.init_node('channel')
	index = rospy.get_param('~length',0)
	print(msg)
	data_sub = rospy.Subscriber('/data', Float64, fromTransmitter)
	trig_sub = rospy.Subscriber('/trigger', Empty, trigger)
	channel_pub = rospy.Publisher('/channel', Float64, queue_size=10)

	r = rospy.Rate(rate)
	k = []									# indices of triggers whose delay time is finished and ready to enter the receiver
	l = []									# length of the triggers remaining
	while not rospy.is_shutdown():
		delayed_data = 0
		i = 0
		if len(delay)>0:
			while(i<len(delay)):
				# print(delay)
				delay[i] -= 1
				if delay[i]<=0:
					k.append(i)
					# l.append(lengths[index])
					l.append(lengths[index]*pw)
					delay.pop(i)
				i += 1
		i = 0
		if len(k)>0:
			while(i<len(k)):
				# print(i, k, l, t)
				if l[i]>0:
					delayed_data += t[k[i]][0]
					t[k[i]].pop(0)
					l[i] -= 1
				else:
					t.pop(k[i])
					k.pop(i)
					l.pop(i)
				i += 1
		# gaussian white noise of 0.25 volt
		delayed_data += 0.5*(random.random() - 0.5)
		# print(l,delayed_data)
		channel_pub.publish(delayed_data)
		r.sleep()


