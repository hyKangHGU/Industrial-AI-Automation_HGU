#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

from move_group_python_interface import MoveGroupPythonInterface
from math import tau
import rospy

def main():
    try:

        indy10_interface = MoveGroupPythonInterface(real=True)

        input("============ Press `Enter` to execute a movement using a joint state goal ...")
        joint_rel = [1/8 * tau, 0, 0, 0, 0, 0]          # tau = 2 * pi
        indy10_interface.go_to_joint_rel(joint_rel)
        
        input("============ Press `Enter` to execute a movement using a joint state goal ...")
        joint_rel = [-1/8 * tau, 0, 0, 0, 0, 0]          # tau = 2 * pi
        indy10_interface.go_to_joint_rel(joint_rel)

        input("============ Press `Enter` to execute a movement using a relative pose ...")
        target_pose_rel_xyz = [0.1, 0.0, 0.0]
        target_pose_rel_rpy = [0, 0, 0]
        indy10_interface.go_to_pose_rel(target_pose_rel_xyz, target_pose_rel_rpy)
        
        input("============ Press `Enter` to execute a movement using a relative pose ...")
        target_pose_rel_xyz = [-0.1, 0.0, 0.0]
        target_pose_rel_rpy = [0, 0, 0]
        indy10_interface.go_to_pose_rel(target_pose_rel_xyz, target_pose_rel_rpy)

        # input("============ Press `Enter` to execute a movement using a absolute pose ...")
        # target_pose_abs_xyz = [0.0, 0.52, 0.54]
        # target_pose_abs_rpy = [0, 0, 0]
        # indy10_interface.go_to_pose_abs(target_pose_abs_xyz, target_pose_abs_rpy)


        print("============ Python tutorial demo complete!")

    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()