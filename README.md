# Industrial AI & Automation

This tutorial is ~~~



- install Ubuntu 20.04 : [link]()
- Install utility programs : [link]()



## ROS installation

Reference: [ROS wiki - Installation](http://wiki.ros.org/noetic/Installation/Ubuntu)



### Setup sources & keys

```bash
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
$ sudo apt install curl # if you haven't already installed curl
$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```



### Installation

```bash
$ sudo apt update
$ sudo apt install ros-noetic-desktop-full
```



### Environment setup

```bash
$ source /opt/ros/noetic/setup.bash
$ echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```



### Dependencies for building packages

```bash
$ sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
```



### Initialize rosdep

```bash
$ sudo rosdep init
$ rosdep update
```



### Create a ROS Workspace

```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```



## Packages Installation

###  UR Robots

Reference: [Github - universal robot](https://github.com/ros-industrial/universal_robot)

```bash
$ sudo apt-get install ros-noetic-universal-robots
```



```bash
$ cd ~/catkin_ws/src

# retrieve the sources
$ git clone https://github.com/ros-industrial/universal_robot.git

$ cd ~/catkin_ws

# checking dependencies
$ rosdep update
$ rosdep install --rosdistro noetic --ignore-src --from-paths src

# building
$ catkin_make

# activate this workspace
$ source ~/catkin_ws/devel/setup.bash
```



* demo.launch

```bash
$ roslaunch ur5e_moveit_config demo.launch
```



### UR Robot Driver

Reference: [Github - universal robot ROS driver](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver)

```bash
$ cd ~/catkin_ws/src

# retrieve the sources
$ git clone https://github.com/UniversalRobots/Universal_Robots_ROS_Driver.git

$ cd ~/catkin_ws

# install dependencies
$ sudo apt update -qq
$ rosdep update
$ rosdep install --from-paths src --ignore-src -y

# build the workspace
$ catkin_make

# activate the workspace (ie: source it)
$ source devel/setup.bash
```



### other packages

```bash
$ cd ~/Desktop
$ git clone https://github.com/hyKangHGU/industrial_AI_automation_HGU.git
```

rg2_description is from https://github.com/ekorudiawan/rg2_simulation

copy & paste packages `rg2_description`, `ur5_rg2_moveit_config` and `ur_python` in `~/catkin_ws/src`

```bash
$ cd ~/catkin_ws

# build the workspace
$ catkin_make

# activate the workspace (ie: source it)
$ source devel/setup.bash
```



## UR5e Execution

### Hardware Connection



### Software Connection

```bash
$ roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=192.168.0.2
```



### Teaching Pendant



### Moveit

```bash
$ roslaunch ur5e_rg2_moveit_config move_group.launch
```



### Demo (python file)

```bash
$ rosrun ur_python move_demo.py
```



