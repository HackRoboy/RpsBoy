#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from roboy_communication_middleware.msg import FingerCommand

def callback(data):
    gesture=data.data
    pub = rospy.Publisher('/roboy/middleware/FingerCommand',FingerCommand,queue_size=10)
    rate = rospy.Rate(1)

    if gesture=='rock':
        finger0 = FingerCommand()
        finger0.id = 0
        finger0.finger = 0
        finger0.angles = [100, 110, 110, 90]
        rospy.loginfo(finger0)
        pub.publish(finger0)
        rate.sleep()
        pub.publish(finger0)
        
    
        finger1 = FingerCommand()
        finger1.id = 0
        finger1.finger = 1
        finger1.angles = [100, 110, 110, 90]
        rospy.loginfo(finger1)
        pub.publish(finger1)
        rate.sleep()
        pub.publish(finger1)
     
        finger2 = FingerCommand()
        finger2.id = 0
        finger2.finger = 2
        finger2.angles = [100, 110, 110, 90]
        rospy.loginfo(finger2)
        pub.publish(finger2)
        rate.sleep()
        pub.publish(finger2)
     
        finger3 = FingerCommand()
        finger3.id = 0
        finger3.finger = 3
        finger3.angles = [70, 70, 90, 90]
        rospy.loginfo(finger3)
        pub.publish(finger3)
        rate.sleep()
        pub.publish(finger3)

    elif gesture=='paper': 
        finger3 = FingerCommand()
        finger3.id = 0
        finger3.finger = 3
        finger3.angles = [0, 0, 0, 90]
        rospy.loginfo(finger3)
        pub.publish(finger3)
        rate.sleep()
        pub.publish(finger3)
     
        finger2 = FingerCommand()
        finger2.id = 0
        finger2.finger = 2
        finger2.angles = [0, 0, 0, 90]
        rospy.loginfo(finger2)
        pub.publish(finger2)
        rate.sleep()
        pub.publish(finger2)
     
        finger1 = FingerCommand()
        finger1.id = 0
        finger1.finger = 1
        finger1.angles = [0, 0, 0, 90]
        rospy.loginfo(finger1)
        pub.publish(finger1)
        rate.sleep()
        pub.publish(finger1)
     
        finger0 = FingerCommand()
        finger0.id = 0
        finger0.finger = 0
        finger0.angles = [0, 0, 0, 90]
        rospy.loginfo(finger0)
        pub.publish(finger0)
        rate.sleep()
        pub.publish(finger0)

    elif gesture=='scissor': 
        finger0 = FingerCommand()
        finger0.id = 0
        finger0.finger = 0
        finger0.angles = [100, 110, 110, 90]
        rospy.loginfo(finger0)
        pub.publish(finger0)
        rate.sleep()
        pub.publish(finger0)
    
        finger1 = "id:0 finger:1 angles:[0,0,0,90]" 
        finger1 = FingerCommand()
        finger1.id = 0
        finger1.finger = 1
        finger1.angles = [0, 0, 0, 90]
        rospy.loginfo(finger1)
        pub.publish(finger1)
        rate.sleep()
        pub.publish(finger1)
     
        finger2 = FingerCommand()
        finger2.id = 0
        finger2.finger = 2
        finger2.angles = [0, 0, 0, 90]
        rospy.loginfo(finger2)
        pub.publish(finger2)
        rate.sleep()
        pub.publish(finger2)
     
        finger3 = FingerCommand()
        finger3.id = 0
        finger3.finger = 3
        finger3.angles = [70, 70, 90, 90]
        rospy.loginfo(finger3)
        pub.publish(finger3)
        rate.sleep()
        pub.publish(finger3)

    else:
        rospy.loginfo('Please input the right gesture!')

def handgesture():
    rospy.init_node('handgesture',anonymous=True)
    rospy.Subscriber('hahaha',String,callback)

    rospy.spin()

if __name__ == "__main__":
    handgesture()
