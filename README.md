# ternary_dsp

In this ROS package, a 7, 13 and 31-length Ternary pulse compression code can be simulated.

Type the following command to run both the transmitter and receiver

roslaunch ternary_dsp ternary.launch

Then type in a new terminal the following to trigger the code transmission

rostopic pub /trigger std_msgs/Empty
