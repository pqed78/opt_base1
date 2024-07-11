import rclpy as rp
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist




from pathlib import Path
import sys
import cv2
import depthai as dai
import numpy as np
from cv_bridge import CvBridge
import time


class camera_data:
    def __init__(self, nnBlobPath, confidence_value, depth_area_scale, min_depth, max_depth):
        self.nnBlobPath = nnBlobPath
        self.confidence_value = confidence_value
        self.depth_area_scale = depth_area_scale
        self.min_depth = min_depth
        self.max_depth = max_depth

        # Create pipeline (이미지 파이프라인 만들기)
        pipeline = dai.Pipeline()

        # Define sources and outputs (소스와 아웃풋 정의)
        camRgb = pipeline.create(dai.node.ColorCamera) #중앙 RGB 카메라 소스  
        spatialDetectionNetwork = pipeline.create(dai.node.MobileNetSpatialDetectionNetwork) # 공간 모바일넷 디텍션 소스
        monoLeft = pipeline.create(dai.node.MonoCamera) #왼쪽 모노카메라 소스
        monoRight = pipeline.create(dai.node.MonoCamera) #오른쪽 모노카메라 소스
        stereo = pipeline.create(dai.node.StereoDepth) # 3차원 공간정보 소스

        xoutVideo = pipeline.create(dai.node.XLinkOut) # 중앙 RGB 카메라 소스
        # xoutRgb = pipeline.create(dai.node.XLinkOut) #프리뷰, 아웃풋 사용없음
        xoutNN = pipeline.create(dai.node.XLinkOut)
        xoutDepth = pipeline.create(dai.node.XLinkOut)

        xoutVideo.setStreamName("video") ######## 중앙 RGB 카메라 스트리밍네임(스트리밍에 사용되는 이름 설정)
        # xoutRgb.setStreamName("rgb")  #프리뷰 스트리밍 이름 사용없음
        xoutNN.setStreamName("detections") # 인공지능네트워크 디텍션 스트리밍네임
        xoutDepth.setStreamName("depth") #3차원 깊이 스트리밍에 사용

        # # Properties
        # camRgb.setPreviewSize(300, 300) ## 프리뷰 사용하지 않음
        camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P) #RGB카메라 셋팅 중 해상도가 가장 낮은 것
        camRgb.setInterleaved(False)
        camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)
        camRgb.setPreviewKeepAspectRatio(keep=True)


        monoLeft.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) # 모노카메라 해상도 셋팅, 속도를 위해서 800p대신 400p 사용
        monoLeft.setCamera("left")
        monoRight.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P) # 모노카메라 해상도 셋팅, 속도를 위해서 800p대신 400p 사용
        monoRight.setCamera("right")

        # Setting node configs
        stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY) # 필요시 HIGH_ACCURACY 사용

        # Align depth map to the perspective of RGB camera, on which inference is done
        stereo.setDepthAlign(dai.CameraBoardSocket.CAM_A) #original is CAM_A:rgb_camera, centered Depth카메라와 중앙카메라 Align
        stereo.setSubpixel(True) # 서브픽셀단위로 인터폴레이션 지정
        stereo.setOutputSize(monoLeft.getResolutionWidth(), monoLeft.getResolutionHeight()) # 공간이미지 아웃풋

        spatialDetectionNetwork.setBlobPath(self.nnBlobPath)
        spatialDetectionNetwork.setConfidenceThreshold(self.confidence_value) # default is 0.5
        spatialDetectionNetwork.input.setBlocking(False)
        spatialDetectionNetwork.setBoundingBoxScaleFactor(self.depth_area_scale) #default is 0.5
        spatialDetectionNetwork.setDepthLowerThreshold(self.min_depth)
        spatialDetectionNetwork.setDepthUpperThreshold(self.max_depth) # default is 5000 unit in mm

        # Linking
        monoLeft.out.link(stereo.left)
        monoRight.out.link(stereo.right)
        camRgb.preview.link(spatialDetectionNetwork.input) #프리뷰 사용 없음


        camRgb.video.link(xoutVideo.input) # To increase the field of view for detection
        spatialDetectionNetwork.out.link(xoutNN.input)
        stereo.depth.link(spatialDetectionNetwork.inputDepth)
        spatialDetectionNetwork.passthroughDepth.link(xoutDepth.input)

        device=dai.Device(pipeline)




        return device 