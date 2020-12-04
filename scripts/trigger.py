#!/usr/bin/env python

import rospy
from std_msgs.msg import Empty
import sys, select, os
if os.name=='nt':
	import msvcrt
else:
	import tty, termios


msg = """
##############################################################################

			Mini-Project EC385
	Department of Electronics and Communication Engineering
	National Institute of Technology Karnataka, Surathkal


	Welcome to the ternary pulse compression code simulation.
	Press the 't' key on the keyboard to Trigger code!


Press ctrl-c to quit
###############################################################################
"""
e = """
Communications failed
"""

def getKey():
	if os.name=='nt':
		return msvcrt.getch()

	tty.setraw(sys.stdin.fileno())
	rlist,_,_ = select.select([sys.stdin],[],[],0.1)
	if rlist:
		key = sys.stdin.read(1)
	else:
		key = ''

	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
	return key


if __name__ == '__main__':
	if os.name!='nt':
		settings = termios.tcgetattr(sys.stdin)

	rospy.init_node('trigger_teleop')
	pub = rospy.Publisher('/trigger', Empty, queue_size=10)

	try:
		print(msg)
		while(1):
			key = getKey()
			if key=='t':
				pub.publish()
				print('A trigger has been made')
			elif key=='\x03':
				break
	except:
		print(e)

	if os.name!='nt':
		termios.tcsetattr(sys.stdin,termios.TCSADRAIN, settings)