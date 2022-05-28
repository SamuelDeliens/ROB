# ------------------------------------------------------    
# ------------------------ Camera ----------------------
# ------------------------------------------------------

import socket
import time

import cv2
from imutils.video import VideoStream
import imagezmq

from FileControler import FileControler

class Camera:
    """object camera 
    get frame of the ocean
    """
    def __init__(self):
        """Constructor
        define size of the image
        """
        self.frameWidth = 244
        self.frameHeight = 244
    
    def configCamera(self, frameWidth, frameHeight):
        """configure the frame

        Args:
            frameWidth (int): width of the frame
            frameHeight (int): height of the frame
        """
        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        
    def startCamera(self):
        """start the capture and send all the frame
        """
        sender = imagezmq.ImageSender(connect_to='tcp://*:5555', REQ_REP=False)
        rpi_name = socket.gethostname()
        picam = VideoStream(usePiCamera = True).start()
        time.sleep(2.0)
        while FileControler.readFile()["camera"]["status"] == "continu":
            image = picam.read()
            image = cv2.resize(image, (self.frameWidth,self.frameHeight))
            sender.send_image(rpi_name, image)
        picam.stop()
        sender.close()
        
        
