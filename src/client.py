#!/usr/bin/env python
import sys
import rospy
from example_posearray.srv import *

if __name__ == "__main__":

  rospy.init_node("client_server")
  add_two_ints = rospy.ServiceProxy('add_two_ints', AddTwoInts)
  rospy.wait_for_service('add_two_ints')
  x=4; y=4
  answer = add_two_ints(x, y)
  print(answer)