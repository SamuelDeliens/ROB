import socket
import time

import cv2
from imutils.video import VideoStream
import imagezmq

from FileControler import FileControler

class Camera:
    def __init__(self):
        self.frameWidth = 244
        self.frameHeight = 244
    
    def configCamera(self, frameWidth, frameHeight):
        self.frameWidth = frameWidth
        self.frameHeight = frameHeight
        
    def startCamera(self):
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
        
        
