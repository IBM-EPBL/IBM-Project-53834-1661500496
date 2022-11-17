from flask import Flask, Response, render_template
from camera import video

app = Flask(_name_)
@app.router('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'content-Type: image/jpeg\r\n\n'+ frame +
              b'\r\n\r\n')

@app.route('video_feed')
def video_feed():
    video = video()
    return Response(gen(video), mimetype='multipart/x-mixed-replace; boundary = frame')


if _name_ == '_main_':

app.run()