#! /usr/bin/env python

import rospy
from std_msgs.msg import String

def messager():
    pub = rospy.Publisher('sentence_to_say', String, queue_size=10)
    rospy.init_node('rps_messager', anonymous=True)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        message_str = "test message!"
        rospy.loginfo(message_str)
        pub.publish(message_str)
        rate.sleep()

if __name__ == '__main__':
    messager()
