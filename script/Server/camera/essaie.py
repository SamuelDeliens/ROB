import cv2
from imutils.video import VideoStream
import imagezmq
import socket

sender = imagezmq.ImageSender(connect_to='tcp://192.168.0.10:5555')
print(sender)
rpi_name = socket.gethostname()

frameWidth = 640
frameHeight = 480
while True :
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    sender.send_image(rpi_name, img)
#success, img = cap.read()

#img = cv2.imread('/home/pi/Desktop/image.jpg')
#img = cv2.resize(img, (frameWidth,frameHeight))
#cv2.imshow("RESULT", img)
#cv2.waitKey(0) 
    


