"""
# robot_navigation_sequence.py (20240627)
This code is the procedure of continuous navigation with TCP API for iamRobotics AMR.
1. Start AMR
2. Wait until ROBOT is sucessfully connected (no API for this)
3. relocation code(robot_control_reloc_req, 19205, 2002)
4. Wait until relocation is done(robot_status_reloc_req, 19204, 1021)
5. Confirm the location of robot (robot_control_comfirmloc_req, 19205, 2003)
6. Go target point (robot_task_gotarget_req, 19206, 3051)
7. Wait until the navigation is finished(robot_status_task_req, 19204, 1020)
8. repeat step 6 and 7 for continuous navigation.

Additional API to monitor the staus of AMR
1. Check Battery Level(robot_status_battery_req, 19204, 1007, {}["battery_level"])
2. Control the motion of AMR (robot_control_motion_req, 19205, 2010, {"vx":0.5,"vy":0.5, "W":rad/s, "duration":ms})
3. Check the position of AMR (robot_status_loc_req, 19204, 1004, {}["x","y","current_station", "last_station",...])
4. Translate AMR to fixed distance (robot_status_loc_req, 19206, {"dist":0.1,"vx":0.5, "vy":0.5} # only absolute number)
5. Pause, Resume, cancel the navigation(19206, 3001, 3002, 3003, {})

"""
from packMasg_client3 import packMasg_client3
from packMasg_client import packMasg_client
import numpy as np
import time


#Common parameters
IP = '192.168.0.25'    
# IP = '10.0.0.13'
PACK_FMT_STR = '!BBHLH6s'


# #To move a certain distance
# Port = 19206
# reqId = 1
# msgType=3055# Control velocity
# # msg="battery_level"
# msg={"dist":3, "vx":1, "vy":-1}
# # msg={}


# msg={}
while True:
    #To check block
    Port = 19204
    reqId = 1
    msgType=1006# Control velocity
    # msg="battery_level"
    # msg={"duration":5000, "vx":1, "vy":-1}
    msg={}

    block_coord=packMasg_client3(PACK_FMT_STR, IP, Port, reqId, msgType, msg).tcp_socket_connection()
    # val={}
    block_coord_np=np.array([block_coord['block_x'],block_coord['block_y']])

    #Check th coordinate of current position
    cur_position=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1004, {}).tcp_socket_connection()
    cur_position_np=np.array([cur_position['x'],cur_position['y']]) 
    distance=np.linalg.norm(block_coord_np-cur_position_np)
    print(distance)

    if distance>=1.3:
        move=packMasg_client3(PACK_FMT_STR, IP, 19205, 1, 2010,{"duration":1000, "vx":1, "vy":1}).tcp_socket_connection()


    time.sleep(0.1)



# #To monitor batter level
# Port = 19204
# reqId = 1
# msgType=1007 # Control velocity
# # msg="battery_level"
# # msg={msg:-1e9}
# msg={}

# pc_b_level=packMasg_client3(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# # val={}
# battery_level=pc_b_level.tcp_socket_connection()["battery_level"]

# #to extract position (x,y)
# Port = 19204
# reqId = 1
# msgType=1004 # robot_status_location_req
# msg={}

# pc=packMasg_client3(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# # val={}
# val=pc.tcp_socket_connection()
# print(val)

# #to extract position (x,y)
# Port = 19204
# reqId = 1
# msgType=1301 # robot_status_location_req
# msg={}

# pc=packMasg_client3(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# # val={}
# val=pc.tcp_socket_connection()
# lm_position=[[val['stations'][lm]['x'], val['stations'][lm]['y']] for lm in range(len(val["stations"]))]
# lm_position=np.array(lm_position)
# print(lm_position[0],lm_position[1],np.linalg.norm(lm_position[0]-lm_position[1],2) )
# # print(val['stations'][lm]['x'] for lm in range(len(val['stations'])))
