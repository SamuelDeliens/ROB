import cv2
import imagezmq
import shutil
import os

if(os.path.exists("Data/Video")):
    shutil.rmtree("Data/Video")
os.makedirs("Data/Video") 
while True:
    print("newStart")
    i=0
    while i<10000:
        print(i)
        stream_monitor = imagezmq.ImageHub(open_port='tcp://192.168.0.10:5555', REQ_REP = False)
        rpi_name, image = stream_monitor.recv_image()
        cv2.imwrite('Data/Video/videoStream'+str(i)+'.jpg', image)
        i=i+1
        #cv2.imshow(rpi_name, image)
        #cv2.waitKey(1) & 0xFF == ord('q')
        #jpg = cv2.imencode('.jpg', image)[1]
stream_monitor.close()
