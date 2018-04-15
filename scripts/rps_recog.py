#!/usr/bin/env python

import Leap, sys, thread, time
import rospy
from std_msgs.msg import String

class MotionListener(Leap.Listener):

    frame_count = 0
    pub = rospy.Publisher('rps_recog', String, queue_size=10)
    
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        self.frame_count = self.frame_count+1
        if self.frame_count < 100: 
            return
        else:
            self.frame_count = 0
        for hand in frame.hands:
            realfinger = len(hand.fingers.extended())
            recog_result = "unknown"
            if realfinger == 0:
                recog_result = "rock"
            elif realfinger == 2:
                recog_result = "scissor"
            elif realfinger == 5:
                recog_result = "paper"
            else:
                recog_result = "unknown"
            rospy.loginfo(recog_result)

            if not rospy.is_shutdown():
                self.pub.publish(recog_result)

        if not (frame.hands.is_empty and frame.gestures().is_empty):
            print ""

        #if len(frame.hands):
        #    hand = frame.hands[0]
        #    realfinger = len(hand.fingers.extended())
        #    recog_result = "unknown"
        #    if realfinger == 0:
        #        recog_result = "rock"
        #    elif realfinger == 2:
        #        recog_result = "scissor"
        #    elif realfinger == 5:
        #        recog_result = "paper"
        #    else:
        #        recog_result = "unknown"
        #    rospy.loginfo(recog_result)

        #    #if not rospy.is_shutdown():
        #    #    pub.publish(recog_result)
        #    #    rospy.loginfo(recog_result)


def recognize():
    rospy.init_node('rps_recognize', anonymous=True)
    listener = MotionListener()
    controller = Leap.Controller()
    controller.add_listener(listener)

    rospy.spin()

    # Remove the sample listener when done
    controller.remove_listener(listener)

if __name__ == '__main__':
    recognize()
