from packMasg_client import packMasg_client

# PACK_FMT_STR = '!BBHLH6s'
# IP = '192.168.0.12'
# Port = 19204
# reqId = 1
# msgType=1007 # battery status
# msg="battery_level"
# msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()



# PACK_FMT_STR = '!BBHLH6s'
# IP = '192.168.0.12'
# Port = 19204
# reqId = 1
# msgType=1000 # robot_status_info_req
# msg={}
# # msg="battery_level"
# # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()



# To stop robot
# PACK_FMT_STR = '!BBHLH6s'
# IP = '192.168.0.12'
# Port = 19205
# reqId = 1
# msgType=2000 # robot_control_stop_req
# msg={}
# # msg="battery_level"
# # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()






# PACK_FMT_STR = '!BBHLH6s'
# IP = '10.0.0.13'
# Port = 19204
# reqId = 1
# msgType=1004 # robot_status_location_req
# msg={}
# # msg="x"
# # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()

# PACK_FMT_STR = '!BBHLH6s'
# IP = '10.0.0.13'
# Port = 19205
# reqId = 1
# msgType=2003 # robot_control_confirmloac_req
# msg={}
# # msg="x"
# # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()

# PACK_FMT_STR = '!BBHLH6s'
# IP = '10.0.0.13'
# Port = 19205
# reqId = 1
# msgType=2003 # robot_control_controlmotion_req
# msg={"vx":0.5, "vy":0.5}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()



# PACK_FMT_STR = '!BBHLH6s'
# IP = '10.0.0.13'
# Port = 19206
# reqId = 1
# msgType=3055 # robot_task_translate_req
# msg={}
# msg={"dist":5.0,"vx":0.5,"vy":0.5}
# # # msg="x"
# # # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()



# PACK_FMT_STR = '!BBHLH6s'
# IP = '10.0.0.13'
# Port = 19206
# reqId = 1
# msgType=3053 # robot_task_translate_req
# msg={}
# msg={"id":"LM5"}
# # # msg="x"
# # # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()

# PACK_FMT_STR = '!BBHLH6s'
# IP = '10.0.0.13'
# Port = 19301
# reqId = 1
# msgType=9300 # robot_pushe
# # msg={}
# msg={"interval":2000,"included_fields":["vx","vy"]}
# # # msg="x"
# # # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()



# PACK_FMT_STR = '!BBHLH6s'
# IP = '10.0.0.13'
# Port = 19301
# reqId = 1
# msgType=19301 # robot_pushe
# # msg={}
# msg={}
# # # msg="x"
# # # msg={msg:-1e9}

# pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
# pc.tcp_socket_connection()
