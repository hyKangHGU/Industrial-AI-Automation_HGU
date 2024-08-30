# Simulation - UR5e



### Demo 1: Simple Move

```bash
roslaunch ur_gazebo ur5e_bringup.launch
roslaunch ur5e_moveit_config moveit_planning_execution.launch sim:=true
rosrun ur_python demo_move.py
```



### Demo 2: Move with Camera

```bash
roslaunch ur_gazebo ur5e_bringup.launch
roslaunch ur5e_moveit_config moveit_planning_execution.launch sim:=true
rosrun ur_python camera.py
rosrun ur_python demo_move_with_camera.py
rosrun ur_python image_processing.py
```



### Check Initialization in demo file

```python
ur5e = MoveGroupPythonInterface(real="sim")
```



#### **주의사항** 

- 시뮬레이션 모델에는 실제 모델의 end-effector가 반영되어 있지 않음.
- 실제 로봇 모델은 end-effector의 좌표를 기준으로 움직이는 것을 고려해야 함.



### Source Program  Description

`demo_move.py`



`MoveGroupPythonInterface()`



`demo_move_with_camera.py`



`image_processing.py`







