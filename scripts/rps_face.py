#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
from roboy_communication_cognition.srv import *

def callback(data):
    # request the corresponding face service according to the message
    mes = data.data
    print mes
    rospy.wait_for_service('/roboy/cognition/face/emotion')
    try:
        fs = rospy.ServiceProxy('/roboy/cognition/face/emotion', ShowEmotion)
        # the following messages are only temporary
        if mes == 'win':
            resp = fs('kiss')
        elif mes == 'lose':
            resp = fs('blink')
        print resp.success
    except rospy.ServiceException, e:
        print "Service call failed: %s" % e

def listener():
    rospy.init_node('mesface', anonymous = True)
    rospy.Subscriber('roboy_message', String, callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
