# Task 2: Stage Mobile Robot Simulator

## Task 2.1

The configuration file and map are defined and the simulator is launched using the command as follows:

```
rosrun stage_ros stageros ra1.cfg
```

A bag file called Task2_1.bag is created storing all topics.


```
rosbag record -a
```

![](Task2_1_rostopic_list.png)

## Task 2.2
The simulated robot can be controlled using the script teleop_twist_keyboard.py from the teleop_twist_keyboard package.

![](Task2_2_stage.png)

```
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

![](Task2_2_teleop.png)

A bag file is created while controlling the robot of name Task2_2.bag