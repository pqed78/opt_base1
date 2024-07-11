"""
# robot_navigation_sequence.py (20240627)
This code is the procedure of continuous navigation with TCP API for iamRobotics AMR.
1. Start AMR
2. Wait until ROBOT is sucessfully connected (no API for this)
--------------------------------------------------------------------------
3. relocation code(robot_control_reloc_req, 19205, 2002)
4. Wait until relocation is done(robot_status_reloc_req, 19204, 1021)
5. Confirm the location of robot (robot_control_comfirmloc_req, 19205, 2003)
3-5 is useless in our application
-----------------------------------------------------------------------------
6. Go target point (robot_task_gotarget_req, 19206, 3051)
7. Wait until the navigation is finished(robot_status_task_req, 19204, 1020)
8. repeat step 6 and 7 for continuous navigation.

Additional API to monitor the staus of AMR
1. Check Battery Level(robot_status_battery_req, 19204, 1007, {}["battery_level"])
2. Control the motion of AMR (robot_control_motion_req, 19205, 2010, {"vx":0.5,"vy":0.5, "W":rad/s, "duration":ms})
3. Check the position of AMR (robot_status_loc_req, 19204, 1004, {}["x","y","current_station", "last_station",...])
4. Translate AMR to fixed distance (robot_status_loc_req, 19206, {"dist":0.1,"vx":0.5, "vy":0.5} # only absolute number)
5. Pause, Resume, cancel the navigation(19206, 3001, 3002, 3003, {})
6. To find location_mark(LM1, LM2, LM3....)(robot_status_station_req, 19204, 1301, {})

"""
from packMasg_client3 import packMasg_client3
from packMasg_client import packMasg_client
import numpy as np
import time


#Common parameters
IP = '192.168.0.25'    
# IP = '10.0.0.13'
PACK_FMT_STR = '!BBHLH6s'

"""
# # relocation (reset the current position to [0,0] if posiiton is really bad, unless do not use this)
# pc_reloc=packMasg_client3(PACK_FMT_STR, IP, 19205, 1, 2002,{"x":0,"y":0.0,"angle":0})
# reloc=pc_reloc.tcp_soc
# ket_connection()
# print(reloc)
"""

# Find the coordinate of location_mark
lm_position=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1301, {}).tcp_socket_connection()

num_station=len(lm_position["stations"])
lm_id=[lm_position['stations'][count]['id'] for count in range(num_station)]
# print(lm_id)
lm_position=[[lm_position['stations'][lm]['x'], lm_position['stations'][lm]['y']] for lm in range(num_station)]
lm_position=np.array(lm_position)

#Check th coordinate of current position
cur_position=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1004, {}).tcp_socket_connection()
cur_position_coord=[cur_position['x'],cur_position['y']] 
# print(position)

#Find closest location mark (LM)
distance=[np.linalg.norm(cur_position_coord-lm_position[i]) for i in range(num_station)]
print(lm_id[distance.index(min(distance))]+" is the closest LM, and goes to "+lm_id[distance.index(min(distance))])

position_close=lm_id[distance.index(min(distance))]
point1='LM3'
point2='LM5'
battery_level=50 # dummy value to start

go_target_init=packMasg_client3(PACK_FMT_STR, IP, 19206, 1, 3051, {'source_id':point1, 'id':position_close}).tcp_socket_connection()
print(position_close)
while True:

    if battery_level>0.5:

        #go to the target point
        pc_go_target=packMasg_client3(PACK_FMT_STR, IP, 19206, 1, 3051, {'source_id':point1, 'id':point2})
        pc_go_target2=packMasg_client3(PACK_FMT_STR, IP, 19206, 1, 3051, {'source_id':point2, 'id':point1})


        pc_go_status_task=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1020, {}) # to wait until navagation is done
        go_target_status=pc_go_status_task.tcp_socket_connection()
        while go_target_status['task_status']<4:
            time.sleep(0.5)
            pc_go_status_task=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1020, {})
            go_target_status=pc_go_status_task.tcp_socket_connection()
            # print(go_target_status)


        pc_go_target.tcp_socket_connection()

        pc_go_status_task=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1020, {})
        go_target_status=pc_go_status_task.tcp_socket_connection()
        while go_target_status['task_status']<4:
            time.sleep(0.5)
            pc_go_status_task=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1020, {})
            go_target_status=pc_go_status_task.tcp_socket_connection()
            # print(go_target_status)

        pc_go_target2.tcp_socket_connection()

        #Check batterylevel
        pc_b_level=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1007, {})
        battery_level=pc_b_level.tcp_socket_connection()["battery_level"]
        print(battery_level)

    # else:





#     #Check batterylevel
#     pc_b_level=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1007, {})
#     battery_level=pc_b_level.tcp_socket_connection()["battery_level"]
#     print(battery_level)


    
#     #Check batterylevel
#     pc_b_level=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1007, {})
#     battery_level=pc_b_level.tcp_socket_connection()["battery_level"]
#     print(battery_level)

#     #Check currentposition
#     pc_cur_position=packMasg_client3(PACK_FMT_STR, IP, 19204, 1, 1004, {})
#     position=[pc_cur_position.tcp_socket_connection()['x'],pc_cur_position.tcp_socket_connection()['y']] 
#     print(position)
#     time.sleep(1)




# #Find closest location mark (LM)

# distance=[np.linalg.norm(position-lm_position[i]) for i in range(num_station)]
# print(lm_id[distance.index(min(distance))]+" is the closest LM, and goes to "+lm_id[distance.index(min(distance))])










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
# msgType=1301 # robot_status_station_req
# msg={}

# pc=packMasg_client3(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# # val={}
# val=pc.tcp_socket_connection()
# lm_position=[[val['stations'][lm]['x'], val['stations'][lm]['y']] for lm in range(len(val["stations"]))]
# lm_position=np.array(lm_position)
# print(lm_position[0],lm_position[1],np.linalg.norm(lm_position[0]-lm_position[1],2) )
# # print(val['stations'][lm]['x'] for lm in range(len(val['stations'])))