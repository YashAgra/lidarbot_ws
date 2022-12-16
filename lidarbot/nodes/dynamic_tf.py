import roslib
roslib.load_manifest('turtle_tf')

import rospy
import tf
import turtlesim.msg
import tf.msg
import geometry_msgs.msg
import math

class DynamicTFBroadcaster:

    def __init__(self):
        self.pub_tf = rospy.Publisher("/tf", tf.msg.tfMessage)

        change = 0.0
        while not rospy.is_shutdown():
            # Run this loop at about 10Hz
            rospy.sleep(0.1)

            t = geometry_msgs.msg.TransformStamped()
            t.header.frame_id = "map"
            t.header.stamp = rospy.Time.now()
            t.child_frame_id = "odom"
            t.transform.translation.x = 2.0 * math.sin(change)
            t.transform.translation.y = 2.0 * math.cos(change)
            t.transform.translation.z = 0.0

            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = 0.0
            t.transform.rotation.w = 0.0

            tfm = tf.msg.tfMessage([t])
            self.pub_tf.publish(tfm)

            change += 0.1

if __name__ == '__main__':
    rospy.init_node('my_tf_broadcaster')
    tfb = DynamicTFBroadcaster()
    rospy.spin()
