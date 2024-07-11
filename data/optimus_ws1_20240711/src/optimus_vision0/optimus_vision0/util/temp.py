from packMasg_client2 import packMasg_client2

IP = '192.168.0.25'
# IP = '10.0.0.13'

# # robot_control_comfirmloc_req
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19205
# reqId = 1
# msgType=2003 # robot_control_comfirmloc_req
# msg={}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()

# #robot_status_reloc_req
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19204
# reqId = 1
# msgType=1021 #robot_status_reloc_req

# msg={}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port,reqId, msgType, msg)
# val=pc.tcp_socket_connection()
# print(val["reloc_status"])
# alpha={}
# alpha=pc.tcp_socket_connection()
# print(alpha["reloc_status"])




# #To monitor batter level
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19204
# reqId = 1
# msgType=1007 # Battery level
# msg="battery_level"
# msg={msg:-1e9}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()


# #to extract position (x,y)
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19204
# reqId = 1
# msgType=1004 # robot_status_location_req
# msg={}
# # msg={"x":-1e9, "y":-1e9}
# msg={"x":-1e9, "y":-1e9}
# # msg={msg:-1e9}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()
# print(pc.tcp_socket_connection())

# # To go to target point (task)
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19206
# reqId = 1
# msgType=3051 # robot_task_gotarget_req
# msg={"source_id":"LM3","id":"LM6", "task_id":"1234"}
# # msg={"source_id":"LM3","id":"LM6"}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()


# To translate (task)
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19206
# reqId = 1
# msgType=3055 # robot_task_translate_req
# msg={"dist":0.1,"vx":0.5, "vy":0.5} # only absolute number

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()


""" Not working at all
# # To go to target list (task)
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19206
# reqId = 1
# msgType=3066 # robot_task_gotarget_req
# msg={"move_task_list": [{"id":"LM7","source_id":"LM3"}, {"id":"LM6","source_id":"LM7"}]}


# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)

# pc.tcp_socket_connection()
"""

# # To pause[go to target point (task)]
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19206
# reqId = 1
# msgType=3001 # robot_task_pause_req
# msg={}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()

# # To resume [go to target point (task), paused]
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19206
# reqId = 1
# msgType=3002 # robot_task_resume_req
# msg={}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()

# # To cancel [go to target point (task), paused]
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19206
# reqId = 1
# msgType=3003 # robot_task_resume_req
# msg={}

# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()



# # To move position
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19205
# reqId = 1
# msgType=2002 # robot_control_reloc_req
# msg={"x":0,"y":-1.0,"angle":0}


# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()

# # To calcel [move position]
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19205
# reqId = 1
# msgType=2004 # robot_control_canclreloc_req
# msg={}


# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()



# # # # To stop robot
# PACK_FMT_STR = '!BBHLH6s'
# Port = 19205
# reqId = 1
# msgType=2000 # robot_control_stop_req
# msg={}


# pc=packMasg_client2(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()