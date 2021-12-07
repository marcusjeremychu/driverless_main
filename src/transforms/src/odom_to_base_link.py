#!/usr/bin/env python
import rospy

import tf_conversions

import tf2_ros
import geometry_msgs.geometry_msgs

def handle_odom_transform(msg):
    br = tf2_ros.TransformerBroadcaster()
    tf2Stamp = geometry_msgs.msg.TransformStamped()

    tf2Stamp.header.stamp = rospy.Time.now()
    tf2Stamp.header.frame_id = 'odom'
    tf2Stamp.child_frame_id = 'base_link'

    tf2Stamp.transform.translation = (msg.x, msg.y, msg.z)
    q = tf_conversions.transformations.quaternion_from_euler(0, 0, msg.theta)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]
    br.sendTransform(tf2Stamp)


if __name__=="__main__":
    rospy.init_node('odom_to_base_link_broadcaster')

    rospy.spin()
