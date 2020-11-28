# ternary_dsp

In this ROS package, a 7, 13 and 31-length Ternary pulse compression code can be simulated.

Step 1. Type the following command to run both the transmitter and receiver

```sh
$ roslaunch ternary_dsp ternary.launch
```
Step 2. In the plotjuggler application, click the streaming menu and select *Start:ROS Topic Subscriber* and then select the topics */data* and */info* and click ok.
Then create two graph view windows one below the other and add these two topics to each of the window.

Step 3.  To trigger the code transmission type in the same terminal the 't' key from the keyboard,
Or alternatively publish the following message in a new terminal
```sh
$ rostopic pub /trigger std_msgs/Empty
```
