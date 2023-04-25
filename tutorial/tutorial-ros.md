# ROS Tutorial



Node, Topic, msgs (type) -> 검색

publish/subscribe



## Talker & Listener

- Tutorial 폴더 접근하기

  ```bash
  $ roscd rospy_tutorials
  $ code .
  ```



- 실행하기

  ```bash
  $ roslaunch rospy_tutorials talker_listener.py
  ```

  

- node & Topic 관찰하기

  ```bash
  $ rqt_graph
  ```

  



## Turtlesim

- Ros master 

  ```bash
  $ roscore
  ```

  

- Turtlesim node

  ```bash
  $ rosrun turtlesim turtlesim_node
  ```

  

- teleop key

  ```bash
  $ rosrun turtlesim turtle_teleop_key
  ```

  방향키를 눌러보자.



- node & Topic 관찰하기

  ```bash
  $ rqt_graph
  ```

  

