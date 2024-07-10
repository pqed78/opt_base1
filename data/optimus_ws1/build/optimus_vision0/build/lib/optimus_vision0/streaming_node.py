#!/env/bin python

import rclpy as rp
from rclpy.node import Node
from sensor_msgs.msg import Image, CompressedImage



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
from ultralytics import YOLO


from ssd_mobilenet_inference_msgs.msg import InferenceResult
# from ssd_mobilenet_inference_msgs.msg import SsdSpatialMobilenet


#  Detection parameters
confidence_value=0.5 # Confidence value of object detection
depth_area_scale=0.5 # The ration of the calculation area for distance to the bounding box area.
fps=30


# To follow only the closest person
# temp_x=0
# temp_y=0
# temp_z=50
# temp_z0=0
# temp_count=[]



# Create pipeline
pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.create(dai.node.ColorCamera)
monoLeft = pipeline.create(dai.node.MonoCamera)
monoRight = pipeline.create(dai.node.MonoCamera)
stereo = pipeline.create(dai.node.StereoDepth)
spatialLocationCalculator = pipeline.create(dai.node.SpatialLocationCalculator)

xoutVideo = pipeline.create(dai.node.XLinkOut)
xoutLeft = pipeline.create(dai.node.XLinkOut)
xoutDepth = pipeline.create(dai.node.XLinkOut)
xoutSpatialData = pipeline.create(dai.node.XLinkOut)
xinSpatialCalcConfig = pipeline.create(dai.node.XLinkIn)

xoutVideo.setStreamName("video")
xoutLeft.setStreamName("left")
xoutDepth.setStreamName("depth")
xoutSpatialData.setStreamName("spatialData")
xinSpatialCalcConfig.setStreamName("spatialCalcConfig")

# Set color properties

camRgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

#Set mono properties
monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)
monoLeft.setCamera("left")
monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_720_P)
monoRight.setCamera("right")

#Set stereo properties
stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_ACCURACY) # Use HIGH_DENSITY, if necessary
stereo.setLeftRightCheck(True) # Check the distance from left to right and vice versa for a better precision of distance measurement.
stereo.setSubpixel(True)

# Config
topLeft = dai.Point2f(0.4, 0.4)
bottomRight = dai.Point2f(0.6, 0.6)

config = dai.SpatialLocationCalculatorConfigData()
config.depthThresholds.lowerThreshold = 300 #minimum distance in mm
config.depthThresholds.upperThreshold = 7000 #maximum distance in mm
calculationAlgorithm = dai.SpatialLocationCalculatorAlgorithm.MEDIAN #MEDIAN, MIN, MODE, MEAN, .... (Calculated these from spatial coordinates within the bounding box)
# config.roi = dai.Rect(topLeft, bottomRight)
spatialLocationCalculator.inputConfig.setWaitForMessage(False)
spatialLocationCalculator.initialConfig.addROI(config)

# Linking
camRgb.video.link(xoutVideo.input)
monoLeft.out.link(xoutLeft.input)
monoLeft.out.link(stereo.left)
monoRight.out.link(stereo.right)

spatialLocationCalculator.passthroughDepth.link(xoutDepth.input)
stereo.depth.link(spatialLocationCalculator.inputDepth)

spatialLocationCalculator.out.link(xoutSpatialData.input)
xinSpatialCalcConfig.out.link(spatialLocationCalculator.inputConfig)

device= dai.Device(pipeline)
video = device.getOutputQueue(name="video", maxSize=4, blocking=False)
left = device.getOutputQueue(name="left", maxSize=4, blocking=False)
depthQueue = device.getOutputQueue(name="depth", maxSize=4, blocking=False)
spatialCalcQueue = device.getOutputQueue(name="spatialData", maxSize=4, blocking=False)
spatialCalcConfigInQueue = device.getInputQueue("spatialCalcConfig")

# Set the model of network. Below is original model, and use *.engine model to use tensorRT,
# #so that increase the speed of inference significantly while minimizing performance degradation
model = YOLO("yolov8n.pt")

# In case of using tensorrt for jetson to reduce the inference time
# Export the model to TensorRT format
model.export(
    format="engine",
    dynamic=True,  
    batch=8,  
    workspace=4,  
    int8=True,
    data="coco.yaml",  
)

# Load the exported TensorRT INT8 model
model = YOLO("yolov8n.engine", task="detect")

# object classes
classNames = ["Person"]

# object details
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
color = (255, 255, 0)
thickness = 3


# Initialized IR Intensity to zero
device.setIrFloodLightIntensity(0)


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
        # To follow only the closest person
        self.temp_x=0
        self.temp_y=0
        self.temp_z=50

        self.bbox_publisher=self.create_publisher(InferenceResult, '/bbox_streaming', QOS_camera_publisher)
        self.nn_image_publisher=self.create_publisher(Image, '/inference_image',QOS_camera_publisher )
        # self.nn_image_publisher=self.create_publisher(CompressedImage, '/inference_image',QOS_camera_publisher ) # To check if the compressed image can be published to reduce the size of data transfer in the network.

        timer_period=1/fps #second        
        self.timer=self.create_timer(timer_period, self.timer_callback)  # timer_callback: location streaming, timer_callback0: location steaming and image display, timer_callback


    def timer_callback(self):



        #Initial brightness of IR led (range is 0 to 1)
        # Control the intensity of IR_LED depending on the brightness of color image
        var=0.01
            
        msg=InferenceResult()
        videoIn = video.get()
        img=videoIn.getCvFrame()   #Convert the video images from color to CV readable arrays.
        brightness_color=np.array(img).sum()
        
        results = model(img, stream=True)

        leftIn = left.get()
        imgl=leftIn.getCvFrame() # Convert the video iamges from the left monochromatic sensor to CV readable arrays.
        brightness_ir=np.array(imgl).sum()
        imgl0=cv2.cvtColor(imgl, cv2.COLOR_GRAY2BGR) # Change one channel color image to three dimensional color images to match the input size required for the model.
        resultsl = model(imgl0, stream=True)
        
        inDepth = depthQueue.get() # Blocking call, will wait until a new data has arrived
        depthFrame = inDepth.getFrame() # depthFrame values are in millimeters
        spatialData = spatialCalcQueue.get().getSpatialLocations() #To obtain the spatial coordiantes (mean, median, mode, min, and so on)


        if brightness_color>1e8:
            imgs=[(img, results)]
            device.setIrLaserDotProjectorBrightness(100)
            stereo.setDepthAlign(dai.CameraBoardSocket.CAM_A)
        else:
            imgs=[(imgl, resultsl)]
            stereo.setDepthAlign(dai.CameraBoardSocket.CAM_B)
            device.setIrLaserDotProjectorBrightness(0)

        # In case of controlling IR_LED, publishing the IR_LED value required. 
        # if brightness_ir<1e8 and ir_led<0.9:
        #     ir_led=ir_led+var
        #     device.setIrFloodLightIntensity(ir_led)
        # elif brightness_ir>5e7 and ir_led>(var-0.001):
        #     ir_led=ir_led-var
        #     device.setIrFloodLightIntensity(ir_led)
        
        if brightness_ir<1e8:
            device.setIrFloodLightIntensity(0.1)
        else:
            device.setIrFloodLightIntensity(0)


        for img, results in imgs:

                for r in results:
                    alpha=(r.boxes.cls==0).nonzero()
                    k=0
                    if len(alpha)>0:
                        for i in range(len(alpha)):
                            sum=r.boxes.xywh[alpha][i][0][2:].sum()
                            if sum>k:
                                k=sum
                                index=i
                            
                        zmin=50

                        # print(alpha[0])
                        for box in r.boxes[alpha[index]]:

                            # bounding box
                            x1, y1, x2, y2 = box.xyxy[0]
                            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values
                                                    
                            
                            x10, y10, x20, y20 = box.xyxyn[0]

                            topLeft = dai.Point2f((x10+x20)/2+(x10-x20)/2*depth_area_scale, (y10+y20)/2+(y10-y20)/2*depth_area_scale)
                            bottomRight = dai.Point2f((x10+x20)/2-(x10-x20)/2*depth_area_scale, (y10+y20)/2-(y10-y20)/2*depth_area_scale)
                            
                            cfg = dai.SpatialLocationCalculatorConfig()
                            config.roi = dai.Rect(topLeft, bottomRight)
                            cfg.addROI(config)
                            spatialCalcConfigInQueue.send(cfg)
                            spatialData = spatialCalcQueue.get().getSpatialLocations()
                            # time.sleep(0.1)
                            
                            # if zmin==50:
                            xmin=x1
                            xmax=x2
                            ymin=y1
                            ymax=y2
                            msg.class_name=str(classNames[0])
                            msg.spatial_x=int(spatialData[0].spatialCoordinates.x)
                            msg.spatial_y=int(spatialData[0].spatialCoordinates.y)
                            msg.spatial_z=int(spatialData[0].spatialCoordinates.z)

                            if img.shape[0]==720:
                                fontScale2=fontScale/2
                                thickness2=thickness
                                # gap2=gap/3
                            elif img.shape[0]==1080:
                                fontScale2=fontScale
                                thickness2=thickness
                                # gap2=gap

                            if zmin==50 or int(spatialData[0].spatialCoordinates.z)>zmin:
                                cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (255, 255, 255), 2)    
                                cv2.putText(img, classNames[0], (xmin, ymin-int(fontScale2*30)), font, int(fontScale2),color, int(thickness2))
                                cv2.putText(img, f"X: {msg.spatial_x} mm", (xmin + 10, ymin + int(fontScale2*30)), font, int(fontScale2), color, int(thickness2))
                                cv2.putText(img, f"Y: {msg.spatial_y} mm", (xmin + 10, ymin + int(2*fontScale2*30)), font, int(fontScale2), color, int(thickness2))
                                cv2.putText(img, f"Z: {msg.spatial_z} mm", (xmin + 10, ymin + int(3*fontScale2*30)), font, int(fontScale2), color, int(thickness2))
                                
                                
                                if img.shape[0]==720:
                                    
                                    img=cv2.resize(img, (640, int(640/1.8)), cv2.INTER_AREA)
                                    img_msg=CvBridge().cv2_to_imgmsg(img)  # Format change from CV image array to msg

                                else:
                                    
                                    img=cv2.resize(img, (640, int(640/1.8)), cv2.INTER_AREA)
                                    img_msg=CvBridge().cv2_to_imgmsg(img, encoding='bgr8') # Format change from CV image array to msg
                                    

                                self.nn_image_publisher.publish(img_msg)    
                                self.bbox_publisher.publish(msg)


                    else:
                        msg.class_name=str('No person')
                        msg.spatial_x=0
                        msg.spatial_y=0
                        msg.spatial_z=50

                        if img.shape[0]==720:
                            
                            img=cv2.resize(img, (640, int(640/1.8)), cv2.INTER_AREA)
                            img_msg=CvBridge().cv2_to_imgmsg(img)
                            
                        else:
                            img=cv2.resize(img, (640, int(640/1.8)), cv2.INTER_AREA)
                            img_msg=CvBridge().cv2_to_imgmsg(img, encoding='bgr8')
                            

                        self.bbox_publisher.publish(msg)
                        self.nn_image_publisher.publish(img_msg)
            


def main(arg=None):
    print('1')
    rp.init()
    camera_publisher=NNCamera_Publisher()
    rp.spin(camera_publisher)
    camera_publisher.destroy_node()
    rp.shutdown()

if __name__ == '__main__':
    main()