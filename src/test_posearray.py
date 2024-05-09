#!/usr/bin/env python
import rospy
import tf
import numpy as np
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseArray

if __name__ == "__main__":

  rospy.init_node('test_posearray')
  pub = rospy.Publisher('poses_arrays', PoseArray, queue_size=1)
  rate = rospy.Rate(10)

  while not rospy.is_shutdown():

    pose_array = PoseArray()
    pose_array.header.frame_id = "/base_link"
    pose_array.header.stamp = rospy.Time.now()

    pose = Pose()
    pose.position.x = 2
    pose.position.y = 2
    pose.position.z = 0
    pose.orientation.x = 0
    pose.orientation.y = 0
    pose.orientation.z = .7071
    pose.orientation.w = .7071

    pose_array.poses.append(pose)

    pose = Pose()
    pose.position.x = 1
    pose.position.y = 1
    pose.position.z = 0
    pose.orientation.x = 0
    pose.orientation.y = 0
    pose.orientation.z = 0
    pose.orientation.w = 1

    pose_array.poses.append(pose)

    pub.publish(pose_array)

    rate.sleep()