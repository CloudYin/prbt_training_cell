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

    # transport position (unit: degree)
    # A1: 0
    # A2: -115
    # A3: -135
    # A4: 90
    # A5: 90
    # A6: 0 
    transport_pos = [0, math.radians(-115), math.radians(-134), math.radians(90), math.radians(90), 0]

    # Move to start point with joint values to avoid random trajectory
    r.move(Ptp(goal = transport_pos, vel_scale = __ROBOT_VELOCITY__))    # 1st move joint A5


if __name__ == "__main__":
    # init a rosnode
    rospy.init_node('robot_program_node')

    # initialisation
    r = Robot(__REQUIRED_API_VERSION__)  # instance of the robot

    # start the main program
    start_program()