#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
import numpy as np

pub = rospy.Publisher('location_monitor_log', String, queue_size=10)

landmarks = [(-2.84301807938 , -0.960722312584, 'Barrier'),
             (-1.432110981, -3.00546955693, 'Cylinder'),
             (0.0402775386124, 0.762637041305, 'Bookshelf'), 
             (-0.0746805300112, -2.91387698629, 'Dumpster'),
             (0.348805138391, -1.06965487885, 'Cube')]

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.pose.pose.position.x)
    x = data.pose.pose.position.x; y = data.pose.pose.position.y
    
    for i in landmarks:
        d = np.sqrt((x-i[0])**2+(y-i[1])**2)
        if d < 0.5:
            log = 'I am near the '+i[2]+' d: '+str(d)+' x: '+str(x)+' y: '+str(y)
            print log
            pub.publish(log)

def listener():
    # Define node
    rospy.init_node('location_monitor_node', anonymous=True)

    rospy.Subscriber('/odom', Odometry, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
