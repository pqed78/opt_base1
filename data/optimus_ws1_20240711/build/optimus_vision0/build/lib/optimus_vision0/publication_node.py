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


from ssd_mobilenet_inference_msgs.msg import InferenceResult
from geometry_msgs.msg import Twist

from .util.packMasg_client3 import packMasg_client3


# global temp 
# temp = 0


class StreamingSubscription(Node):
    def __init__(self):
        super().__init__('inference_sub')

        self.PACK_FMT_STR = '!BBHLH6s'
        self.IP = '192.168.0.25'

        #define QOS offered by DDS
        self.declare_parameter('qos_depth', 5)
        qos_depth=self.get_parameter('qos_depth').value

        # self.msg0={"vx":0.0, "w":0.0, "duration":5000}
        self.temp=0 # 사람의 추적여부 판단
        self.temp1=0 # 사람 추적 시작 여부 판단
        self.temp2=0 #  네비게이션 중지 여부 판단
        self.msg0={}


        QOS_camera_subscribe=QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=qos_depth,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        self.subscription=self.create_subscription(InferenceResult, '/bbox_streaming', self.callback_pose, QOS_camera_subscribe)


        self.timer_period=0.2
        self.timer_period=0.1
        self.timer=self.create_timer(self.timer_period, self.timer_callback)
        self.timer2=self.create_timer(self.timer_period, self.timer_callback2)

        # self.rot=Twist()

     

    def callback_pose(self, msg):

        if msg.spatial_z>2000:          #사람 발견시
            #To check block
            block_coord=packMasg_client3(self.PACK_FMT_STR, self.IP, 19204, 1, 1006, {}).tcp_socket_connection()
            block_coord_np=np.array([block_coord['block_x'],block_coord['block_y']])

            #Check th coordinate of current position
            cur_position=packMasg_client3(self.PACK_FMT_STR, self.IP,  19204, 1, 1004, {}).tcp_socket_connection()
            cur_position_np=np.array([cur_position['x'],cur_position['y']]) 
            distance=np.linalg.norm(block_coord_np-cur_position_np)
            if distance>2:
            
                if msg.spatial_x/msg.spatial_z > 0.2:
                    # self.rot.angular.z=0.2
                    self.msg0={"vx":0.5, "w":-0.2, "duration":2000}

                    # time.sleep(1.5)
                elif msg.spatial_x/msg.spatial_z < -0.2:
                    # self.rot.angular.z=-0.2
                    self.msg0={"vx":0.5, "w":0.2, "duration":2000}
                    # time.sleep(1.5)

                else:
                    self.msg0={"vx":0.5, "w":0.0, "duration":2000}

                self.temp=1
                self.temp1=0

        elif msg.spatial_z>50 and msg.spatial_z<=2000:          #사람 앞에 있으나 가까울 때
            #print("test ",msg.spatial_z)
            self.msg0={"vx":0.0, "w":0.0, "duration":2000}

            self.temp=1
            self.temp1=0

        else:
            if self.temp==1 and self.temp1==0:
                # Find the coordinate of location_mark
                lm_position=packMasg_client3(self.PACK_FMT_STR, self.IP, 19204, 1, 1301, {}).tcp_socket_connection()
                num_station=len(lm_position["stations"])
                lm_id=[lm_position['stations'][count]['id'] for count in range(num_station)]
                # print(lm_id)
                lm_position=[[lm_position['stations'][lm]['x'], lm_position['stations'][lm]['y']] for lm in range(num_station)]
                lm_position=np.array(lm_position)

                #Check th coordinate of current position
                cur_position=packMasg_client3(self.PACK_FMT_STR, self.IP, 19204, 1, 1004, {}).tcp_socket_connection()
                cur_position_coord=[cur_position['x'],cur_position['y']] 
                # print(position)

                #Find closest location mark (LM)
                distance=[np.linalg.norm(cur_position_coord-lm_position[i]) for i in range(num_station)]
                print(lm_id[distance.index(min(distance))]+" is the closest LM, and goes to "+lm_id[distance.index(min(distance))])

                position_close=lm_id[distance.index(min(distance))]
                go_target_init=packMasg_client3(self.PACK_FMT_STR, self.IP, 19206, 1, 3051, {'id':position_close}).tcp_socket_connection()
                
                print(position_close)

            self.temp=0
            self.temp1=1




        # else:                            #사람이 없을 때

            self.temp2=msg.spatial_z
            print(self.temp2)

    def timer_callback(self):


        if self.temp==1:
            pc=packMasg_client3(self.PACK_FMT_STR, self.IP, 19205, 0, 2010, self.msg0)
            pc.tcp_socket_connection()

    
    def timer_callback2(self):
    
        if self.temp==0:
            point1='LM7'
            point2='LM8'

        #go to the target point
            pc_go_target=packMasg_client3(self.PACK_FMT_STR, self.IP, 19206, 1, 3051, {'source_id':point1, 'id':point2})
            pc_go_target2=packMasg_client3(self.PACK_FMT_STR, self.IP, 19206, 1, 3051, {'source_id':point2, 'id':point1})


            pc_go_status_task=packMasg_client3(self.PACK_FMT_STR, self.IP, 19204, 1, 1020, {}) # to wait until navagation is done
            go_target_status=pc_go_status_task.tcp_socket_connection()

            if go_target_status['target_id']==point2:
                if go_target_status['task_status']<4:
                    pc_go_target.tcp_socket_connection()
                elif go_target_status['task_status']==4:
                    pc_go_target2.tcp_socket_connection()

            
            elif go_target_status['target_id']==point1:
                if go_target_status['task_status']<4:
                    pc_go_target2.tcp_socket_connection()
                elif go_target_status['task_status']==4:
                    pc_go_target.tcp_socket_connection()
            
            else:
                pc_go_target.tcp_socket_connection()

    



def main(args=None):
    rp.init(args=args)
    inference_sub=StreamingSubscription()
    rp.spin(inference_sub)
    inference_sub.destroy_node()
    rp.shutdown()


if __name__ == '__main__':
    main()

