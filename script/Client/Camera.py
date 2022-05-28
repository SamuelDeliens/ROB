# ------------------------------------------------------    
# ------------------------ Camera ----------------------
# ------------------------------------------------------

import base64

from flask import Flask, render_template, Response
from flask_sock import Sock
import cv2
import imagezmq

app = Flask(__name__)
sock = Sock(app)
stream_monitor = imagezmq.ImageHub(open_port='tcp://192.168.0.10:5555', REQ_REP = False)

@app.route('/')
def index():
    return render_template("index.html")

def gen():
    while True:
        stream_monitor = imagezmq.ImageHub(open_port='tcp://192.168.0.10:5555', REQ_REP = False)
        rpi_name, image = stream_monitor.recv_image()
        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        frame = base64.b64encode(frame).decode("UTF-8")
        print(frame)
        sock.send(frame)
    stream_monitor.close()

def video_():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@sock.route('/video')
def video(sock):
    while True:
        rpi_name, image = stream_monitor.recv_image()
        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        frame = base64.b64encode(frame).decode("UTF-8")
        sock.send(frame)
    
if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")
