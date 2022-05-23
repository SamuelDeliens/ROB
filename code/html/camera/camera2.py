from flask import Flask, render_template, Response
import cv2
import imagezmq
import shutil


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def gen():
    while True:
        stream_monitor = imagezmq.ImageHub(open_port='tcp://192.168.0.10:5555', REQ_REP = False)
        rpi_name, image = stream_monitor.recv_image()
        ret, buffer = cv2.imencode('.jpg', image)
        frame = buffer.tobytes()
        print(frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    stream_monitor.close()

@app.route('/video')
def video():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug=True)