#include "ros/ros.h"
#include "std_msgs/String.h"

#include <sstream>

#include <iostream>
#include <cstring>

#include "/home/rainnymig/dl/LeapDeveloperKit_2.3.1+31549_linux/LeapSDK/include/Leap.h"

using namespace Leap;

class SampleListener : public Listener {
  public:
    virtual void onInit(const Controller&);
    virtual void onConnect(const Controller&);
    virtual void onDisconnect(const Controller&);
    virtual void onExit(const Controller&);
    virtual void onFrame(const Controller&);

    SampleListener()
    {
        this->count = 0;
    }

  private:
    int count;
};

void SampleListener::onInit(const Controller& controller) {
  std::cout << "Initialized" << std::endl;
}

void SampleListener::onConnect(const Controller& controller) {
  std::cout << "Connected" << std::endl;
}

void SampleListener::onDisconnect(const Controller& controller) {
  // Note: not dispatched when running in a debugger.
  std::cout << "Disconnected" << std::endl;
}

void SampleListener::onExit(const Controller& controller) {
  std::cout << "Exited" << std::endl;
}


void SampleListener::onFrame(const Controller& controller) {
  // Get the most recent frame and report some basic information
  const Frame frame = controller.frame();

  HandList hands = frame.hands();
  for (HandList::const_iterator hl = hands.begin(); hl != hands.end(); ++hl) {
    // Get the first hand
    const Hand hand = *hl;
    // Get fingers
    const FingerList fingers = hand.fingers();
    int extendedFingers = 0;
    for (int f = 0; f < fingers.count(); f++)
    {
        Leap::Finger finger = fingers[f];
        if(finger.isExtended()) extendedFingers++;
    }
    std::cout << extendedFingers << std::endl;
  }

  if (!frame.hands().isEmpty()) {
    std::cout << std::endl;
  }

}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "rps_recog2");
    ros::NodeHandle n;
    
    ros::Publisher recog_pub = n.advertise<std_msgs::String>("recog_result", 1000);

    ros::Rate loop_rate(1);

    // Create a sample listener and controller
    SampleListener listener;
    Controller controller;
    // Have the sample listener receive events from the controller
    controller.addListener(listener);

    /*
    while(ros::ok())
    {
        std_msgs::String result;
        std::stringstream ss;
        ss << "rock" << count;
        result.data = ss.str();

        ROS_INFO("%s", result.data.c_str());
        recog_pub.publish(result);
        
        ros::spinOnce();
        loop_rate.sleep();

        ++count;
    }
    */

    return 0;
}
