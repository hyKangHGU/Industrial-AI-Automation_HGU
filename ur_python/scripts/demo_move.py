#! /usr/bin/env python3

import sys
import rospy
import moveit_commander
import moveit_msgs
import geometry_msgs

import tf

from math import pi

from move_group_python_interface import MoveGroupPythonInterface

DEG2RAD = pi/180
RAD2DEG = 180/pi

def main(args):
    try:
        print("grip")
        ur5e = MoveGroupPythonInterface()
        
        # ur5e.move_relative((0.2, 0.0, 0.1), (0.0, 0.0, 90 * DEG2RAD))
        ur5e.move_relative((-0.3, -0.1, 0.0), (0.0, 0.0, 0.0))
        ur5e.gripper_open()
        
        ur5e.move_relative((0.0, 0.0, -0.18), (0.0, 0.0, 0.0))
        ur5e.gripper_close()
        
        ur5e.move_relative((0.0, 0.0, 0.18), (0.0, 0.0, 0.0))
        ur5e.move_relative((0.4, 0.0, 0.0), (0.0, 0.0, 0.0))
        ur5e.move_relative((0.0, 0.0, -0.18), (0.0, 0.0, 0.0))
        ur5e.gripper_open()

        ur5e.move_relative((0.0, 0.0, 0.18), (0.0, 0.0, 0.0))
        ur5e.move_to_standby()

        print("mission 1: complete")
        rospy.sleep(3)

        ur5e.move_relative((0.1, -0.1, 0.0), (0.0, 0.0, 0.0))
        ur5e.gripper_open()
        
        ur5e.move_relative((0.0, 0.0, -0.18), (0.0, 0.0, 0.0))
        ur5e.gripper_close()
        
        ur5e.move_relative((0.0, 0.0, 0.18), (0.0, 0.0, 0.0))
        ur5e.move_relative((-0.4, 0.0, 0.0), (0.0, 0.0, 0.0))
        ur5e.move_relative((0.0, 0.0, -0.18), (0.0, 0.0, 0.0))
        ur5e.gripper_open()

        ur5e.move_relative((0.0, 0.0, 0.18), (0.0, 0.0, 0.0))
        ur5e.move_to_standby()

        print("mission 2: complete")

    except KeyboardInterrupt:
        print("Shut down by Key Interrupt")


if __name__ == '__main__':
    main(sys.argv)