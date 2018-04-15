#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback1(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    #publish the msg to the topic controlling the leap motion recognition

def callback2(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # publish the msg to the topic controlling the hand gesture

def listener():
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber('roboy_command', String, callback1)
    rospy.Subscriber('rps_decision', String, callback2)
    rospy.spin()

if __name__ == '__main__':
    listener()
