#include "ros/ros.h"
#include "geometry_msgs/Pose.h"
#include "geometry_msgs/PoseArray.h"

#include <sstream>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "test_posearray");
  ros::NodeHandle n;
  ros::Publisher pub = n.advertise<geometry_msgs::PoseArray>("poses_arrays", 1);
  ros::Rate loop_rate(10);

  while (ros::ok())
  {
    geometry_msgs::PoseArray parray;

    geometry_msgs::Pose pose0;
    pose0.position.x = 2.0;
    pose0.position.y = 2.0;
    pose0.orientation.z = 0.7071;
    pose0.orientation.w = 0.7071;
    parray.poses.push_back(pose0);

    geometry_msgs::Pose pose1;
    pose1.position.x = 1.0;
    pose1.position.y = 1.0;
    pose1.orientation.z = 0;
    pose1.orientation.w = 1;
    parray.poses.push_back(pose1);

    pub.publish(parray);
    ros::spinOnce();
    loop_rate.sleep();
  }

  return 0;
}