#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import time

velocity_publisher = rospy.Publisher(
    '/robotont/cmd_vel', Twist, queue_size=10)
vel_msg = Twist()


def closing():
    # After the loop, stops the robot
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    # Force the robot to stop
    velocity_publisher.publish(vel_msg)

#######################
# YOUR FUNCTIONS HERE #
#######################
def otse(kestus, kiirus):
    for i in range(kestus):
        vel_msg.linear.x = kiirus
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def paremvasak(kestus, kiirus):
    for i in range(kestus):
        vel_msg.linear.x = 0
        vel_msg.linear.y = kiirus
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)

def keera(kestus, kiirus):
    for i in range(kestus):
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.angular.z = kiirus
        velocity_publisher.publish(vel_msg)
        rospy.sleep(0.1)
###########################
# YOUR FUNCTIONS HERE END #
###########################


def move():
    # Starts a new node
    rospy.init_node('robotont_velocity_publisher', anonymous=True)

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():
        ########################
        # YOUR CODE HERE START #
        ########################
        otse(30, 0.3)
        keera(45, 0.5)
        paremvasak(30, 0.3)
        ######################
        # YOUR CODE HERE END #
        ######################


if __name__ == '__main__':
    try:
        rospy.on_shutdown(closing)
        move()
    except rospy.ROSInterruptException:
        pass
