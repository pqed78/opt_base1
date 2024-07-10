import rclpy as rp
from rclpy.node import Node

import numpy as np
import time

#Import Library for QOS setup
from rclpy.parameter import Parameter
from rclpy.qos import QoSDurabilityPolicy
from rclpy.qos import QoSHistoryPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy

from .util.packMasg_client import packMasg_client

from ssd_mobilenet_inference_msgs.msg import InferenceResult
from geometry_msgs.msg import Twist


# global temp 
# temp = 0


class StreamingSubscription(Node):
    def __init__(self):
        super().__init__('inference_sub')

        #define QOS offered by DDS
        self.declare_parameter('qos_depth', 10)
        qos_depth=self.get_parameter('qos_depth').value

        # self.msg0={"vx":0.0, "w":0.0, "duration":5000}
        self.temp=0
        self.msg0={}


        QOS_camera_subscribe=QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=qos_depth,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        self.subscription=self.create_subscription(InferenceResult, '/bbox_streaming', self.callback_pose, QOS_camera_subscribe)

        self.subscription
        # self.twist_publisher=self.create_publisher(Twist, '/cmd_vel', 10)


        self.timer_period=0.2
        self.timer=self.create_timer(self.timer_period, self.timer_callback)

        # self.rot=Twist()

     

    def callback_pose(self, msg):

        print(msg.spatial_z)
        if msg.spatial_z>2000:          #사람 발견시
            if msg.spatial_x/msg.spatial_z > 0.1:
                # self.rot.angular.z=0.2
                self.msg0={"vx":-0.3, "w":-0.3, "duration":2000}
                # time.sleep(1.5)
            elif msg.spatial_x/msg.spatial_z < -0.1:
                # self.rot.angular.z=-0.2
                self.msg0={"vx":-0.3, "w":0.3, "duration":2000}
                # time.sleep(1.5)
            else:
                self.msg0={"vx":-0.3, "w":0.0, "duration":2000}
            
            self.temp=msg.spatial_x     

        elif msg.spatial_z>50:          #사람 앞에 있으나 가까울 때
            #print("test ",msg.spatial_z)
            self.msg0={"vx":0.0, "w":0.0, "duration":2000}
            
        #elif msg.spatial_z==50:                           #사람 없을 때
        else:
            #print(msg.spatial_z)
            if self.temp>0:
                self.msg0={"vx":0.0, "w":-0.5, "duration":3000}
                
                # time.sleep(1.5)
            else:
                self.msg0={"vx":0.0, "w":0.5, "duration":3000}
                # time.sleep(1.5)
        


    
    def timer_callback(self):
        #Parameters
        PACK_FMT_STR = '!BBHLH6s'
        IP = '10.0.0.10'
        Port = 19205 #status 19204 #control 19205
        # Port =19204
        reqId = 0
        msgType=2010 # Control velocity
        # msgType=1040 # Check emc_state
        # msg={"vx":0, "vy":1}
        pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, self.msg0)
        pc.tcp_socket_connection()
        # print('1')
        


def main(args=None):
    rp.init(args=args)
    inference_sub=StreamingSubscription()
    rp.spin(inference_sub)
    inference_sub.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()

