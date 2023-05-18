# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data

from std_msgs.msg import String
from sensor_msgs.msg import Image

from cv_bridge import CvBridge

import cv2
import numpy as np





class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Image,
            'camera_01',
            self.listener_callback,
            qos_profile_sensor_data)
        self.subscription  # prevent unused variable warning
        #self.show_image()
        self.bridge = CvBridge()

    def show_image(self, img):
        cv2.imshow('cam image', img)
        cv2.waitKey(1)

    def listener_callback(self, msg):
        #self.get_logger().info('I heard: "%s"' % msg.data)
        #self.get_logger().info('Received image')
        self.get_logger().info('Image size [w, h] = [{}, {}]'.format(msg.width, msg.height))
        #cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding = 'passthrough')
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding = 'bgr8')
        #cv_image = cv2.resize(cv_image, [msg.width/2, msg.height/2])
        cv_image = cv2.resize(cv_image, None, fx=0.5, fy=0.5)
        self.show_image(cv_image)
        

        
        
        
        
        
        
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    cv2.namedWindow("cam image", 1)

    rclpy.spin(minimal_subscriber)


    cv2.destroyAllWindows()

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
