# ROS Tutorial



## Talker & Listener

- 실행하기

  ```bash
  roslaunch rospy_tutorials talker_listener.py
  ```

  

  - talker가 생성한 내용을 listener가 메시지로 받아서 화면에 출력한다.

  ![image](https://user-images.githubusercontent.com/91526930/234394784-a24bfbb2-8f10-443e-b23d-f5dafda2532e.png)





- node & Topic 관찰하기

  ```bash
  rqt_graph
  ```

  

  - talker와 listener라는 노드가 있으며, chatter라는 정보를 전달하고 있다.

  ![image](https://user-images.githubusercontent.com/91526930/234394161-ca099b10-639c-466d-9162-7fe709a4a39a.png)







- Tutorial 폴더 접근하기

  ```bash
  roscd rospy_tutorials
  code .
  ```

  

  - 폴더에는 `.launch` `.py`의 구성

    ![image](https://user-images.githubusercontent.com/91526930/234396103-730b952f-d540-4871-b962-3101a73b3778.png)

  

  - `talker_listener.launch`파일 내에는 두 개의 node를 실행하는 것으로 구성되며, 각각 python 파일로부터 불러와지는 것을 확인할 수 있다.

    ![image](https://user-images.githubusercontent.com/91526930/234396233-154876be-05dc-4bba-b92e-f6e1e1acc233.png)

  

  - `listener.py`

    ![image](https://user-images.githubusercontent.com/91526930/234396748-210f85b3-f6da-42a1-8e1e-434460f27045.png)

    - 'listener'라는 노드를 `init_node`를 통해 초기화한다.

    - 'chatter'라는 String 형태의 msg 정보를 subscribing하고, callback함수를 실행한다. 

    - callback 함수는 data를 받아서, terminal 창에 출력한다.

      

  - `talker.py`

    ![image](https://user-images.githubusercontent.com/91526930/234398302-2ef57b3a-b3d7-4d62-966b-13475a1e5971.png)

    - 'chatter'라는 String 형태의 msg 정보를 publishing하는 변수 pub을 선언한다.
    - 'talker'라는 노드를 초기화한다.
    - hello_str에는 String 형태의 정보를 생산 및 할당한다.
    - publish 함수를 통해 hello_str 변수를 publishing 한다.

    

  - std_msgs

    - [ROS Wiki - std_msgs](http://wiki.ros.org/std_msgs)
    - std_msgs는 기본적으로 정의된 msgs들의 기본 형식을 제공한다. 
    - `Bool`, `Byte`, `Int16`, `Float32`, `Int8MultiArray`, `String`, `Time` 등의 변수 type들이 존재한다.

    ![image](https://user-images.githubusercontent.com/91526930/234399565-051b3c6f-2160-4341-a715-0a4e2f4b68e4.png)



- 노드와 메세지의 활용법을 더 자세히 알고자 한다면, 002~009의 tutorial을 통해서 연습하도록 합시다.



## Turtlesim

talker & listener를 통해 배운 노드와 메세지 개념을 turtlesim 예제를 통해 적용해보자.

- Ros master 실행

  ```bash
  roscore
  ```

  

- Turtlesim node

  ```bash
  rosrun turtlesim turtlesim_node
  ```

  거북이가 새로운 창에 출력된다.

  

- teleop key

  ```bash
  rosrun turtlesim turtle_teleop_key
  ```

  방향키를 누르면, 거북이가 움직인다.



- node & Topic 관찰하기

  ```bash
  rqt_graph
  ```






## ROS Package 설치

- ROS에서 공식적으로 제공하는 pacakge는 보통 다음과 같은 명령어를 통해 설치됨.

  ```bash
  sudo apt-get install ros-noetic-[pacakge name]
  ```

- 위 방식으로 설치된 package는 `roscd` 명령어를 통해 폴더에 접근할 수 있음. 

  ```bash
  roscd [package name]
  ```

- 경로에서 확인할 수 있듯이 package를 설치하면 `/opt/ros/noetic/share` 내부에는 알게 모르게 설치된 수많은 package들이 존재함.
  `vs code`를 통해 프로그램 코드를 모두 확인할 수는 있지만, 수정할 수 있는 권한이 없음.

![image](https://user-images.githubusercontent.com/91526930/235362934-a74b67f4-0026-4bf7-96af-aaeec117a5f3.png)





## ROS Package 복사

- ROS에서 공식적으로 만들어서 제공하는 package는 아니지만, 특정 회사나 개인이 만들어 package를 github를 통해 배포하는 경우가 있음.

- ROS 인증(?) 받은 package의 경우, 아래와 같이 설치할 수 있음.

  ```bash
  sudo apt-get install ros-noetic-[pacakge name]
  ```

- 그러나, 해당 package를 직접 수정하여 build하고자 한다면 다음과 같이 `~/catkin_ws/src` 내부에 패키지를 복사하면 가능함.
  (ROS 인증이 되지 않은 package이더라도, 유용한 pacakge로 판단된다면, 복사하여 필요한 작업을 진행하면 됨.)

  ```bash
  [위치] ~/catkin/src
  git clone https://github.com/[USERNAME]/[REPOSITORY_NAME].git
  git clone -b [branch name] https://github.com/[USERNAME]/[REPOSITORY_NAME].git # 특정 branch를 복사해야 하는 경우
  ```

- 패키지 빌드

  ```bash
  [위치] ~/catkin
  catkin_make
  ```

