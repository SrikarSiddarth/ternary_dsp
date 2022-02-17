# Ternary pulse compression code simulation

Implemented from the paper:
L. Xu, Q. Liang and T. Jiang, "A ternary pulse compression code: Design and application to radar system," 2010 IEEE International Conference on Acoustics, Speech and Signal Processing, 2010, pp. 4050-4053, doi: 10.1109/ICASSP.2010.5495762.

The updated versions of the system in future can be found at https://github.com/SrikarSiddarth/ternary_dsp

This ROS package can be used to simulate a 7, 13 and 31-length Ternary pulse compression code.

## Prerequisites:
1. Ubuntu 16.04 or higher
2. ROS Kinetic or above. 
For Installation (for example ROS melodic) refer - http://wiki.ros.org/melodic/Installation/Ubuntu
3. Plotjuggler package. 
Installation :
```sh
$ sudo apt install ros-${ROS_DISTRO}-plotjuggler-ros
```

## Running the simulation

Step 0. Copy the *ternary_dsp* folder to the catkin workspace and build the package in the *catkin_ws* folder using the command :
```sh
$ catkin_make
```

Step 1. Type the following command to run both the transmitter and receiver

```sh
$ roslaunch ternary_dsp ternary.launch length:=0
```
setting the *length* parameter to 0, 1, and 2 corresponds to implementing a 7, 13 and 31 bit ternary code respectively.

Step 2. In the plotjuggler application, click the streaming menu and select *Start:ROS Topic Subscriber* and then select the topics */data* and */info* and click ok.
Then create two graph view windows one below the other and add these two topics to each of the window.

Step 3.  Press 't' on the keyboard in the same terminal to trigger the code transmission,
Or alternatively publish the following message in a new terminal
```sh
$ rostopic pub /trigger std_msgs/Empty
```

Note: By default the length of the ternary pulse compression code is set to 7. It can be changed. Set the argument *length* in the /launch/ternary.launch file to 0 or 1 or 2 in order to use the lengths 7 or 13 or 31 respectively.

Please file any issues at https://github.com/SrikarSiddarth/ternary_dsp/issues or send an e-mail to srikarsiddharth@gmail.com
