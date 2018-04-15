#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from roboy_communication_middleware.msg import FingerCommand

rospy.init_node('handgesture',anonymous=True)
rate = rospy.Rate(1)

pub = rospy.Publisher('/roboy/middleware/FingerCommand',FingerCommand,queue_size=10)

finger1 = FingerCommand()
finger1.id = 0
finger1.finger = 1
finger1.angles = [100, 110, 110, 90]
rospy.loginfo(finger1)
pub.publish(finger1)
rate.sleep()
pub.publish(finger1)

rospy.spin()

