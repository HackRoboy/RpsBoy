#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
from roboy_communication_cognition.srv import Talk

#rospy.ServiceProxy('Talk', Talk)

def callback(data):
    mes = data.data
    print mes
    rospy.wait_for_service('/roboy/cognition/speech/synthesis/talk')
    try:
        stt = rospy.ServiceProxy('/roboy/cognition/speech/synthesis/talk', Talk)
        resp = stt(sentence)
        print resp.success
        if(resp.success == True):
            print 'hell yah'
        else:
            print 'oh no'
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def listener():
    rospy.init_node('mestalk', anonymous = True)
    rospy.Subscriber('roboy_message', String, callback)

    rospy.spin()

if __name__ == "__main__":
    listener()
