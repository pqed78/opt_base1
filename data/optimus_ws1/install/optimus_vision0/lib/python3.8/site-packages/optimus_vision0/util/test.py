from packMasg_client3 import packMasg_client3
from packMasg_client import packMasg_client
import numpy as np
import time


#Common parameters
IP = '192.168.0.25'    
# IP = '10.0.0.13'
PACK_FMT_STR = '!BBHLH6s'

alpha=packMasg_client3(PACK_FMT_STR, IP, 19204, 0, 1025,{}).tcp_socket_connection()

print(alpha)