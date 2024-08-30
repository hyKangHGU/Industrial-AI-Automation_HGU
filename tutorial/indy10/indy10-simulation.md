# Simulation - Indy10



### Demo 1: Simple Move

```bash
roslaunch indy10_gazebo indy10_moveit_gazebo.launch
rosrun indy_driver demo_move.py
```



### Demo 2: Move with Camera

```bash
roslaunch indy10_gazebo indy10_moveit_gazebo.launch
rosrun indy_driver camera.py
rosrun indy_driver demo_move_with_camera.py
rosrun indy_driver image_processing.py
```



### Source Program  Description

`demo_move.py`



`MoveGroupPythonInterface()`



`demo_move_with_camera.py`



`image_processing.py`







