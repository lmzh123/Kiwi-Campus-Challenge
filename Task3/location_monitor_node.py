#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'chatter' topic

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
