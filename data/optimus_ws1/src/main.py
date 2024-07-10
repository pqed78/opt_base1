from packMasg_client import packMasg_client



def main(arg=None):
    PACK_FMT_STR = '!BBHLH6s'
    IP = '192.168.0.12'
    # Port = 19205 #status 19204v #control 19205
    Port =19204
    reqId = 0
    # msgType=2010 # Control velocity
    msgType=1040 # Check emc_state
    # msg={"vx":0, "vy":1}
    msg={}
    pc=packMasg_client(PACK_FMT_STR, IP, Port, reqId, msgType, msg)
    pc.tcp_socket_connection()
    print(msg,'  ok')

if __name__ == '__main__':
    main()