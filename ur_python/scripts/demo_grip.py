#! /usr/bin/env python3

import sys
import rospy
import moveit_commander
import moveit_msgs
import geometry_msgs
import tf

from math import pi
from move_group_python_interface import MoveGroupPythonInterface

def main(args):
    try:
        print("grip")
        ur5e = MoveGroupPythonInterface()
        ur5e.gripper_close()
        ur5e.gripper_open()
        print("complete")


    except KeyboardInterrupt:
        print("Shut down by Key Interrupt")


if __name__ == '__main__':
    main(sys.argv)