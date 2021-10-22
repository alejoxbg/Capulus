# Capulus

This project is the design, construction and software development of a ground mobile robot focused to perform activities within coffee farms, in this repository you can find the CAD models that were used to model and build the robot, the dynamic simulations in webots and the different ROS packages that were used to perform the teleoperation and for its perception system.

You can see videos of the robot in the following links:

Tilt tests:
https://www.youtube.com/watch?v=4jDVVaN-1A8

Spin test:
https://www.youtube.com/watch?v=EYGEjlZiWx4

Real field tests:
https://www.youtube.com/watch?v=VNCkxsc_Qe4

Kalman filter localization:
https://www.youtube.com/watch?v=74ZAOpA_L4A

## Circuit

![](https://github.com/alejoxbg/Capulus/blob/main/Circuit.jpg)

## Run
>cd #your workspace#/src
https://github.com/alejoxbg/Capulus.git && cd ..
catkin_make
roslaunch capulus driver.launch
