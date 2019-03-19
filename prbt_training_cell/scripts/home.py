#!/usr/bin/env python

from geometry_msgs.msg import Pose, Point
from pilz_robot_programming import *
from pilz_robot_programming.commands import *
import math
import rospy

__REQUIRED_API_VERSION__ = "1"  # API version
__ROBOT_VELOCITY__ = 0.1        # velocity of the robot


# main program
def start_program():


    rospy.loginfo("Program started") # log

    # important positions
    home_pos = [0, 0, 0, 0, 0, 0]   # joint values

    # Move to start point with joint values to avoid random trajectory
    r.move(Ptp(goal = home_pos, vel_scale = __ROBOT_VELOCITY__))


if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')

    # initialisation
    r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot

    # start the main program
    start_program()