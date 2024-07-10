
import socket
import json
import struct




class packMasg_client:
    
    def __init__(self, PACK_FMT_STR, IP, Port, reqId, msgType, msg={}): # Method Initialization
        self.PACK_FMT_STR = PACK_FMT_STR
        self.IP = IP
        self.Port = Port
        self.reqId = reqId
        self.msgType = msgType
        self.msg = msg

    def packMasg(self): # Packing message to request action for socket communication
        msgLen = 0
        jsonStr = json.dumps(self.msg)
        if (self.msg != {}):
            msgLen = len(jsonStr)

        rawMsg = struct.pack(self.PACK_FMT_STR, 0x5A, 0x01, self.reqId, msgLen,self.msgType, b'\x00\x00\x00\x00\x00\x00')
        # print("{:02X} {:02X} {:04X} {:08X} {:04X}"
            # .format(0x5A, 0x01, reqId, msgLen, msgType))

        if (self.msg != {}):
            rawMsg += bytearray(jsonStr,'ascii')
        # print(msg)

        return rawMsg

    def tcp_socket_connection(self): #socket connection, request action, and receive response
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        so.connect((self.IP, self.Port))
        so.settimeout(5)
        test_msg = self.packMasg()
        # print("\n\nreq:")
        # print(' '.join('{:02X}'.format(x) for x in test_msg))
        so.send(test_msg)

        dataall = b''
        # print('\n\n\n')
        try:
            data = so.recv(16)
        except socket.timeout:
            print('timeout')
            so.close
        jsonDataLen = 0
        backReqNum = 0
        if(len(data) < 16):
            print('pack head error')
            print(data)
            so.close()
        else:
            header = struct.unpack(self.PACK_FMT_STR, data)
            # print("{:02X} {:02X} {:04X} {:08X} {:04X} {:02X} {:02X} {:02X} {:02X} {:02X} {:02X}       length: {}"
            #     .format(header[0], header[1], header[2], header[3], header[4], header[5][0],
            #             header[5][1], header[5][2], header[5][3], header[5][4], header[5][5], header[3]))
            jsonDataLen = header[3]
            backReqNum = header[4]
        dataall += data
        data = b''
        readSize = 1024
        try:
            while (jsonDataLen > 0):
                recv = so.recv(readSize)
                data += recv
                jsonDataLen -= len(recv)
                if jsonDataLen < readSize:
                    readSize = jsonDataLen
            print(json.dumps(json.loads(data), indent=1))
            dataall += data
            # print(' '.join('{:02X}'.format(x) for x in dataall))
        except socket.timeout:
            print('timeout')

        so.close()


