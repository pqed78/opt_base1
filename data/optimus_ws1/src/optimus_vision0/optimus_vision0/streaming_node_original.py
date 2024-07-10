import rclpy as rp
from rclpy.node import Node
from sensor_msgs.msg import Image


#Import Library for QOS setup
from rclpy.parameter import Parameter
from rclpy.qos import QoSDurabilityPolicy
from rclpy.qos import QoSHistoryPolicy
from rclpy.qos import QoSProfile
from rclpy.qos import QoSReliabilityPolicy





from pathlib import Path
import sys
import cv2
import depthai as dai
import numpy as np
from cv_bridge import CvBridge
import time



from ssd_mobilenet_inference_msgs.msg import InferenceResult
# from ssd_mobilenet_inference_msgs.msg import SsdSpatialMobilenet

'''
Spatial detection network
    Performs inference on RGB camera and retrieves spatial location coordinates: x,y,z relative to the center of depth map.
'''
model=1

# To change the number of consecutive images to draw the bounding box and send the message of the location of the closest person
n=2

# To change the orientation of camera (normal=0, upsidedown=1)
flipmode=0

# To detect person only. The number of person label is not independent of the model.
    
if model==0: #MobileNet-SSD
    temp_model=15
    image_size1=300
    image_size2=300
elif model==1:#Yolov8n
    temp_model=0
    image_size1=640
    image_size2=352
    

if model==0:
    # Default-SSD mobilenet
    nnBlobPath = '/home/ubuntu/optimus_ws/src/optimus_vision0/optimus_vision0/models/mobilenet-ssd_openvino_2021.4_6shave.blob'


    # MobilenetSSD label texts: Only use Person (아래 표기된 것들 중 사람만 확인 index=15)
    labelMap = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
                "diningtable", "dog", "horse", "motorbike", "Person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
elif model==1:
    # Get argument first
    nnBlobPath = '/home/optimus/virtual/optimus/optimus_ws1_20240624/src/optimus_vision0/optimus_vision0/models/yolov8n_coco_640x352.blob'


    # Yolov8n
    labelMap = [
        "person",         "bicycle",    "car",           "motorbike",     "aeroplane",   "bus",           "train",
        "truck",          "boat",       "traffic light", "fire hydrant",  "stop sign",   "parking meter", "bench",
        "bird",           "cat",        "dog",           "horse",         "sheep",       "cow",           "elephant",
        "bear",           "zebra",      "giraffe",       "backpack",      "umbrella",    "handbag",       "tie",
        "suitcase",       "frisbee",    "skis",          "snowboard",     "sports ball", "kite",          "baseball bat",
        "baseball glove", "skateboard", "surfboard",     "tennis racket", "bottle",      "wine glass",    "cup",
        "fork",           "knife",      "spoon",         "bowl",          "banana",      "apple",         "sandwich",
        "orange",         "broccoli",   "carrot",        "hot dog",       "pizza",       "donut",         "cake",
        "chair",          "sofa",       "pottedplant",   "bed",           "diningtable", "toilet",        "tvmonitor",
        "laptop",         "mouse",      "remote",        "keyboard",      "cell phone",  "microwave",     "oven",
        "toaster",        "sink",       "refrigerator",  "book",          "clock",       "vase",          "scissors",
        "teddy bear",     "hair drier", "toothbrush"
    ]






syncNN = True

# Spatial depth range
min_depth=100
max_depth=10000

#  Detection parameters
confidence_value=0.5
depth_area_scale=0.5
fps=30

#Initialization of IR power for brightness control
ir=0
ir2=0
var=1

# To follow only the closest person
temp_x=0
temp_y=0
temp_z=50
temp_z0=0
temp_count=[]

# Create pipeline (이미지 파이프라인 만들기)
pipeline = dai.Pipeline()

# Define sources and outputs (소스와 아웃풋 정의)
camRgb = pipeline.create(dai.node.ColorCamera) #중앙 RGB 카메라 소스

if model==0: 
    spatialDetectionNetwork = pipeline.create(dai.node.MobileNetSpatialDetectionNetwork) # 공간 모바일넷 디텍션 소스
elif model==1:
    spatialDetectionNetwork = pipeline.create(dai.node.YoloSpatialDetectionNetwork)

monoLeft = pipeline.create(dai.node.MonoCamera) #왼쪽 모노카메라 소스
monoRight = pipeline.create(dai.node.MonoCamera) #오른쪽 모노카메라 소스
stereo = pipeline.create(dai.node.StereoDepth) # 3차원 공간정보 소스


xoutRgb = pipeline.create(dai.node.XLinkOut) # 중앙 RGB 카메라 소스
xoutNN = pipeline.create(dai.node.XLinkOut)
xoutDepth = pipeline.create(dai.node.XLinkOut)


# xoutVideo.setStreamName("video") ######## 중앙 RGB 카메라 스트리밍네임(스트리밍에 사용되는 이름 설정)
xoutRgb.setStreamName("rgb")  #프리뷰 스트리밍 이름 사용없음
xoutNN.setStreamName("detections") # 인공지능네트워크 디텍션 스트리밍네임
xoutDepth.setStreamName("depth") #3차원 깊이 스트리밍에 사용

# # Properties
camRgb.setPreviewSize(image_size1, image_size2) ## 프리뷰 사용하지 않음
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P) #RGB카메라 셋팅 중 해상도가 가장 낮은 것
camRgb.setInterleaved(False)
camRgb.setPreviewKeepAspectRatio(False) # 최대 FOV를 활용하기 위하여 사용- detection accuracy may decrease.
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

if flipmode==1:
    camRgb.setImageOrientation(dai.CameraImageOrientation.ROTATE_180_DEG)


monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) # 모노카메라 해상도 셋팅, 속도를 위해서 800p대신 400p 사용
monoLeft.setCamera("left")
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) # 모노카메라 해상도 셋팅, 속도를 위해서 800p대신 400p 사용
monoRight.setCamera("right")




# Setting node configs
stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY) # 필요시 HIGH_ACCURACY 사용

# Align depth map to the perspective of RGB camera, on which inference is done
stereo.setDepthAlign(dai.CameraBoardSocket.CAM_A) #original is CAM_A:rgb_camera, centered Depth카메라와 중앙카depth메라 Align
stereo.setSubpixel(True) # 서브픽셀단위로 인터폴레이션 지정
stereo.setOutputSize(monoLeft.getResolutionWidth(), monoLeft.getResolutionHeight()) # 공간이미지 아웃풋

rotate_stereo_manip = pipeline.createImageManip()
if flipmode==1:
    rotate_stereo_manip.initialConfig.setVerticalFlip(True)
    rotate_stereo_manip.initialConfig.setHorizontalFlip(True)
    rotate_stereo_manip.setFrameType(dai.ImgFrame.Type.RAW16)
stereo.depth.link(rotate_stereo_manip.inputImage)

spatialDetectionNetwork.setBlobPath(nnBlobPath)
spatialDetectionNetwork.setConfidenceThreshold(confidence_value) # default is 0.5
spatialDetectionNetwork.input.setBlocking(False)
spatialDetectionNetwork.setBoundingBoxScaleFactor(depth_area_scale) #default is 0.5
spatialDetectionNetwork.setDepthLowerThreshold(min_depth)
spatialDetectionNetwork.setDepthUpperThreshold(max_depth) # default is 5000 unit in mm

if model==1:
    # Yolo specific parameters
    spatialDetectionNetwork.setNumClasses(80)
    spatialDetectionNetwork.setCoordinateSize(4)
    # spatialDetectionNetwork.setAnchors([10,14, 23,27, 37,58, 81,82, 135,169, 344,319])
    # spatialDetectionNetwork.setAnchorMasks({ "side26": [1,2,3], "side13": [3,4,5] })

    spatialDetectionNetwork.setAnchors([10,13, 16,30, 33,23, 30,61, 62,45, 59,119, 116,90, 156,198, 373,326])
    spatialDetectionNetwork.setAnchorMasks({ "side52" : [0,1,2],
                                                "side26" : [3,4,5],
                                                "side13" : [6,7,8]})
    spatialDetectionNetwork.setIouThreshold(0.5)




# Linking
monoLeft.out.link(stereo.left)
monoRight.out.link(stereo.right)

camRgb.preview.link(spatialDetectionNetwork.input)

if syncNN:
    spatialDetectionNetwork.passthrough.link(xoutRgb.input)
else:
    camRgb.preview.link(xoutRgb.input)

spatialDetectionNetwork.out.link(xoutNN.input)
rotate_stereo_manip.out.link(spatialDetectionNetwork.inputDepth)
spatialDetectionNetwork.passthroughDepth.link(xoutDepth.input)


device=dai.Device(pipeline)

# Output queues will be used to get the rgb frames and nn data from the outputs defined above
# qVideo = device.getOutputQueue(name="video", maxSize=4, blocking=False)
previewQueue = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
detectionNNQueue =  device.getOutputQueue(name="detections", maxSize=4, blocking=False)
depthQueue =  device.getOutputQueue(name="depth", maxSize=4, blocking=False)


class NNCamera_Publisher(Node):
    
    def __init__(self):
        super().__init__('camera_publisher')

        #define QOS offered by DDS
        self.declare_parameter('qos_depth', 10)
        qos_depth=self.get_parameter('qos_depth').value

        QOS_camera_publisher=QoSProfile(
            reliability=QoSReliabilityPolicy.RELIABLE,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=qos_depth,
            durability=QoSDurabilityPolicy.VOLATILE
        )

        # self.subscription = self.create_subscription(
        #     Image,
        #     'rgb_cam/image_raw'
        # )
        self.temp_x = temp_x

        self.temp_y = temp_y
        self.temp_z = temp_z
        self.temp_z0 = temp_z0
        self.temp_count = temp_count
        # self.n=n


        self.bbox_publisher=self.create_publisher(InferenceResult, '/bbox_streaming', QOS_camera_publisher)
        self.nn_image_publisher=self.create_publisher(Image, '/inference_image',QOS_camera_publisher )

        timer_period=1/fps #second        
        self.timer=self.create_timer(timer_period, self.timer_callback)  # timer_callback: location streaming, timer_callback0: location steaming and image display, timer_callback


    def timer_callback(self):
            
        # To follow only the closest person
        self.temp_x=0
        self.temp_y=0
        self.temp_z=50
        # self.n=2
         
        for i in range(n):
            self.temp_count.append(0)    # append로 요소 추가 

        for ii in np.arange(n): 

            msg=InferenceResult()
            inVideo=previewQueue.get() #original video
            inDet = detectionNNQueue.get()
            depth = depthQueue.get()


            color = (255, 255, 255) # 박스 및 텍스트 색상 [3D depth image]
            color1 = (255, 255, 255) # 박스 및 텍스트 색상 [RGB color image]


            if inVideo is not None:
                frame = inVideo.getCvFrame()
                # frame = cv2.rotate(frame,cv2.ROTATE_180)

            # # 컬러에 깊이정보까지 획득: 4차원 포맷
            depthFrame = depth.getFrame() # depthFrame values are in millimeters
    
            # No need to scale the colormap for 3d stereo image
            # depth_downscaled = depthFrame[::4]
            # min_depth = np.percentile(depth_downscaled[depth_downscaled != 0], 1) #가까운 곳 1% 위치 확인
            # max_depth = np.percentile(depth_downscaled, 99) #먼곳 99% 거리 확인



            depthFrameColor = np.interp(depthFrame, (min_depth, max_depth), (0, 255)).astype(np.uint8)
            depthFrameColor = cv2.applyColorMap(depthFrameColor, cv2.COLORMAP_HOT) #계산된 거리를 바탕으로 색상 자동 형성

            detections = inDet.detections  #인공지능 측정 결과 정보

            # For Full FOV
            if model==0:
                frame=cv2.resize(frame, (int(4/3*image_size1), image_size2))

            # If the frame is available, draw bounding boxes on it and show the frame
            height = frame.shape[0]  #RGB 높이
            width  = frame.shape[1]  #RGB 폭
              
            

             #To detect only Person
            if len(detections) !=0:
                for detection in detections:
                    if detection.label ==temp_model: # Detect person only
                        try:
                            label = labelMap[detection.label]
                        except:
                            label = detection.label
                    


                        if self.temp_z==50 or detection.spatialCoordinates.z<self.temp_z:
                            a=detection.confidence*100
                            self.temp_x=int(detection.spatialCoordinates.x)
                            self.temp_y=int(detection.spatialCoordinates.y)
                            self.temp_z=int(detection.spatialCoordinates.z)

                            roiData = detection.boundingBoxMapping
                            roi = roiData.roi
                            roi = roi.denormalize(depthFrameColor.shape[1], depthFrameColor.shape[0])
                            topLeft = roi.topLeft()
                            bottomRight = roi.bottomRight()
                            xmin = int(topLeft.x)
                            ymin = int(topLeft.y)
                            xmax = int(bottomRight.x)
                            ymax = int(bottomRight.y)
                            
                            x1 = int(detection.xmin * width)
                            x2 = int(detection.xmax * width)
                            y1 = int(detection.ymin * height)
                            y2 = int(detection.ymax * height)

                    
                            self.temp_x=int(detection.spatialCoordinates.x)
                            self.temp_y=int(detection.spatialCoordinates.y)
                            self.temp_z=int(detection.spatialCoordinates.z)

                            self.temp_count[ii]=1



                        # # To draw BBOX for the closest person

                        # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2, cv2.FONT_HERSHEY_SIMPLEX)
                        # cv2.putText(frame, str(label), (x1 + 10, y1 + 15), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)
                        # cv2.putText(frame, "{:.2f}".format(detection.confidence*100), (x1 + 10, y1 + 30), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)
                        # cv2.putText(frame, f"X: {int(detection.spatialCoordinates.x)} mm", (x1 + 10, y1 + 45), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255),1)
                        # cv2.putText(frame, f"Y: {int(detection.spatialCoordinates.y)} mm", (x1 + 10, y1 + 60), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)
                        # cv2.putText(frame, f"Z: {int(detection.spatialCoordinates.z*0.85)} mm", (x1 + 10, y1 + 75), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)

                        # img_msg=CvBridge().cv2_to_imgmsg(frame, encoding='bgr8')
                        

                        # print(np.sum(self.temp_count),n)
                        # if np.sum(self.temp_count)>1.5 and np.sum(self.temp_count)<10: # 2 out of n 인식될 경우에만 위치 전달
                        #     self.bbox_publisher.publish(msg)

                        # self.nn_image_publisher.publish(img_msg)    
                        



                    if detection.label !=temp_model: # Detect person only
                        msg.class_name=str('No person')
                        msg.spatial_x=0
                        msg.spatial_y=0
                        msg.spatial_z=50


                        # img_msg=CvBridge().cv2_to_imgmsg(frame)
                        img_msg=CvBridge().cv2_to_imgmsg(frame, encoding='bgr8')

                        self.temp_count[ii]=10
                        if np.sum(self.temp_count)>10*n/2: # 연속으로 인식될 경우에만 위치 전달
                            self.bbox_publisher.publish(msg)
                        self.nn_image_publisher.publish(img_msg)

         

            else:
                # print(np.sum(self.temp_count))    
                msg.class_name=str('No person')
                msg.spatial_x=0
                msg.spatial_y=0
                msg.spatial_z=50

                # img_msg=CvBridge().cv2_to_imgmsg(frame)
                img_msg=CvBridge().cv2_to_imgmsg(frame, encoding='bgr8')
                self.temp_count[ii]=10

                if np.sum(self.temp_count)>10*n/2: # 연속으로 인식될 경우에만 위치 전달
                    self.bbox_publisher.publish(msg)
                self.nn_image_publisher.publish(img_msg)

            if len(detections) !=0:
                for detection in detections:
                    if detection.label ==temp_model: # Detect person only
                        msg.class_name=str(label)
                        msg.spatial_x=self.temp_x
                        msg.spatial_y=self.temp_y
                        msg.spatial_z=int(self.temp_z*0.85) 

                        # print(np.sum(self.temp_count),n)
                        if np.sum(self.temp_count)>n/2 and np.sum(self.temp_count)<10*n/2: # 2 out of n 인식될 경우에만 위치 전달
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2, cv2.FONT_HERSHEY_SIMPLEX)
                            cv2.putText(frame, str(label), (x1 + 10, y1 + 15), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)
                            cv2.putText(frame, "{:.2f}".format(a), (x1 + 10, y1 + 30), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)
                            cv2.putText(frame, f"X: {int(self.temp_x)} mm", (x1 + 10, y1 + 45), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255),1)
                            cv2.putText(frame, f"Y: {int(self.temp_y)} mm", (x1 + 10, y1 + 60), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)
                            cv2.putText(frame, f"Z: {int(self.temp_z*0.85)} mm", (x1 + 10, y1 + 75), cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255), 1)
                            self.bbox_publisher.publish(msg)


                        img_msg=CvBridge().cv2_to_imgmsg(frame, encoding='bgr8')
                        self.nn_image_publisher.publish(img_msg)    

def main(arg=None):
    print('1')
    rp.init()
    camera_publisher=NNCamera_Publisher()
    rp.spin(camera_publisher)
    camera_publisher.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()##### 중앙 RGB 카메라 스트리밍네임(스트리밍에 사용되는 이름 설정)