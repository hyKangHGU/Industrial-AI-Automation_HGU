#! /usr/bin/env python3

import sys
import rospy
import moveit_commander
import moveit_msgs
import geometry_msgs

import tf

from tf.transformations import *
from geometry_msgs.msg import Quaternion

from ur_msgs.srv import SetIO, SetIORequest

class MoveGroupPythonInterface():
    def __init__(self):
        rospy.init_node("ur_python", anonymous=True)

        self.robot = moveit_commander.RobotCommander()
        self.manipulator = moveit_commander.move_group.MoveGroupCommander("manipulator")

        self.io_handler = rospy.ServiceProxy('/ur_hardware_interface/set_io', SetIO)

        self.gripper = SetIORequest()
        self.gripper_init()

        self.move_to_standby()

        rospy.sleep(1)

    def move_to_standby(self):
        self.manipulator.set_named_target("stand_by")
        self.manipulator.go(wait=True)
        self.manipulator.stop()
        
    def gripper_init(self):
        self.gripper.fun=1
        self.gripper.pin=1
        self.gripper_open()
    
    def gripper_close(self):
        self.gripper.state=1
        self.io_handler.call(self.gripper)
        rospy.sleep(1.5)
        
    def gripper_open(self):
        self.gripper.state=0
        self.io_handler.call(self.gripper)
        rospy.sleep(1.5)

    def get_pose(self):
        return self.manipulator.get_current_pose().pose

    def move_relative(self, relative_xyz, relative_rpy):
        # xyz unit: [m], rpy unit: [rad]

        # get current pose
        current_pose = self.get_pose()
        print(f"<current_pose>\n{current_pose}")

        # calculate the target position with current position and relative coordinates
        target_pose = current_pose
        target_pose.position.x += relative_xyz[0]
        target_pose.position.y += relative_xyz[1]
        target_pose.position.z += relative_xyz[2]

        # Get the target orientation with current orientation(quaternion) and relative orientation(euler)
        current_quat = [current_pose.orientation.x, current_pose.orientation.y, current_pose.orientation.z, current_pose.orientation.w]
        current_rpy = euler_from_quaternion(current_quat)   # current orientation: Quat -> Euler
        target_rpy = [0., 0., 0.]                           # calculate the target orientation in Euler Coordinate
        target_rpy[0] = current_rpy[0] + relative_rpy[0]
        target_rpy[1] = current_rpy[1] + relative_rpy[1]
        target_rpy[2] = current_rpy[2] + relative_rpy[2]
        
        # Transform target_rpy to target_quat
        target_quat = quaternion_from_euler(target_rpy[0], target_rpy[1], target_rpy[2])
        
        # Apply target_quat to the orientation of target_pose
        target_pose.orientation = Quaternion(target_quat[0], target_quat[1], target_quat[2], target_quat[3])

        print(f"<target_pose>\n{target_pose}")
        print(f"current xyz: ({current_pose.position.x:.2f}, {current_pose.position.y:.2f}, {current_pose.position.z:.2f}), rpy: {current_rpy}")
        print(f"target  xyz: ({target_pose.position.x:.2f}, {target_pose.position.y:.2f}, {target_pose.position.z:.2f}), rpy: {target_rpy}")

        # Plan & Move
        self.manipulator.set_pose_target(target_pose)
        self.manipulator.go(wait=True)
        self.manipulator.stop()
        self.manipulator.clear_pose_targets()