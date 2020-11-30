# Ternary pulse compression code simulation

This ROS package can be used to simulate a 7, 13 and 31-length Ternary pulse compression code.

## Prerequisites:
1. ROS Kinetic or above
For Installation (for example ROS melodic) refer - http://wiki.ros.org/melodic/Installation/Ubuntu
2. Plotjuggler package
Installation :
```sh
$ sudo apt install ros-${ROS_DISTRO}-plotjuggler-ros
```
3. clone this package to the workspace and build it

## Running the simulation
Step 1. Type the following command to run both the transmitter and receiver

```sh
$ roslaunch ternary_dsp ternary.launch
```
Step 2. In the plotjuggler application, click the streaming menu and select *Start:ROS Topic Subscriber* and then select the topics */data* and */info* and click ok.
Then create two graph view windows one below the other and add these two topics to each of the window.

Step 3.  Press 't' on the keyboard in the same terminal to trigger the code transmission,
Or alternatively publish the following message in a new terminal
```sh
$ rostopic pub /trigger std_msgs/Empty
```

Note: By default the length of the ternary pulse compression code is set to 31. It can be changed. Set the argument *length* in the /launch/ternary.launch file to 0 or 1 or 2 in order to use the lengths 7 or 13 or 31 respectively.

Please file any issues at https://github.com/SrikarSiddarth/ternary_dsp/issues or send an e-mail to srikarsiddharth@gmail.com
