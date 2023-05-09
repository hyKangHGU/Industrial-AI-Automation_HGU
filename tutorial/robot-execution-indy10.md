# Robot Execution - Indy10

## Required Packages

아래의 패키지 내역이 `catkin_ws/src` 내에 포함되어 있는지 확인하세요.

- `indy_driver`
- `indy_utils`
- `indy10_control`
- `indy10_description`
- `indy10_gazebo`
- `indy10_moveit_config`

패키지가 없으면, [Github-Industrial-AI-Automation_HGU](https://github.com/hyKangHGU/Industrial-AI-Automation_HGU)에서 다운받아 주시면 됩니다.



## Indy10 Robot Execution

### Robot Setting

1) 로봇의 전원을 켠다.
2) PC의 WiFi를 sslab으로 연결한다.
   - pw: `********`
3) 로봇의 IP 주소를 확인한다.
   - No.1 : 192.168.0.6
   - No.2: 192.168.0.9



### Demo 1: Simple Move

```bash
roslaunch indy10_moveit_config moveit_planning_execution.launch robot_ip:=192.168.0.6
rosrun indy_driver demo_move.py
```



### Demo 2: Gripper Operation

```bash
roslaunch indy10_moveit_config moveit_planning_execution.launch robot_ip:=192.168.0.6
rosrun indy_driver demo_grip.py
```



### Demo 3: Move with Camera

```bash
roslaunch indy10_moveit_config moveit_planning_execution.launch robot_ip:=192.168.0.6
rosrun indy_driver camera.py
rosrun indy_driver demo_move_with_camera.py
rosrun indy_driver image_processing.py
```





`demo_grip.py`

```python
indy10_interface = MoveGroupPythonInterface(real=True, gripper="Vaccum")
```

- gripper 사용시, `MoveGroupPythonInterface()` class 초기화시 다음과 같이 설정해야한다.
  - real = True
  - gripper = "Gripper" or "Vaccum" 
