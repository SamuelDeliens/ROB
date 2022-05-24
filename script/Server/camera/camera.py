import socket
import time
#import imutils
import cv2
from imutils.video import VideoStream
import imagezmq
frameWidth = 244
frameHeight = 244
while True :
    sender = imagezmq.ImageSender(connect_to='tcp://*:5555', REQ_REP=False)
    print(sender)
    rpi_name = socket.gethostname()
    print(rpi_name)
    picam = VideoStream(usePiCamera = True).start()
    print(picam)
    time.sleep(2.0)
    continu = True
    while continu :
        image = picam.read()
        print('read')
        image = cv2.resize(image, (frameWidth,frameHeight))
        print('send')
        sender.send_image(rpi_name, image)