# Robot Execution - UR5e

## Required Packages

아래의 패키지 내역이 `catkin_ws/src` 내에 포함되어 있는지 확인하세요.

- `rg2_description`
- `universal_robot`
- `Universal_Robots_ROS_Driver`
- `ur_python`
- `ur5e_rg2_moveit_config`

패키지가 없으면, [Github-Industrial-AI-Automation_HGU](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU)에서 다운받아 주시면 됩니다.



## UR5e Robot Execution

### Robot Setting

1) 티칭 펜던트의 전원을 켠다.
2) 사전에 작업된 `ros.urp` 로봇 프로그램을 불러온다.
3) 로봇의 전원을 켠다.
4) 컨트롤 박스의 랜선을 PC에 연결한다.
5) PC에서 유선 네트워크 연결을 설정한다.

더 자세한 내용은 [Github-Setting UR5e](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU/blob/main/tutorial/setting-ur5e.md)에서 확인한다.



### Execution Flow

- **Hardware Connection (Robot Setting 참고)**

- **Software Connection**

  ```bash
  roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=192.168.0.2
  ```

- **로봇 프로그램 실행 (Teaching Pendant)**

  <img src="https://user-images.githubusercontent.com/91526930/234138529-75eb185e-f308-400f-aebb-d2f79e8b3ffb.png" alt="image" style="zoom:70%;" />

- **Moveit**

  ```bash
  roslaunch ur5e_rg2_moveit_config move_group.launch
  ```

- **Demo Program**

  ```bash
  rosrun ur_python demo_move.py
  ```

  

### Demo 1: Simple Move

```bash
roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=192.168.0.2
roslaunch ur5e_rg2_moveit_config move_group.launch
rosrun ur_python demo_move.py
```



### Demo 2: Gripper Operation

```bash
roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=192.168.0.2
roslaunch ur5e_rg2_moveit_config move_group.launch
rosrun ur_python demo_grip.py
```



### Demo 3: Pick & Place

```bash
roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=192.168.0.2
roslaunch ur5e_rg2_moveit_config move_group.launch
rosrun ur_python demo_pick_and_place.py
```



### Demo 4: Move with Camera

```bash
roslaunch ur_robot_driver ur5e_bringup.launch robot_ip:=192.168.0.2
roslaunch ur5e_rg2_moveit_config move_group.launch
rosrun ur_python camera.py
rosrun ur_python demo_move_with_camera.py
rosrun ur_python image_processing.py
```
