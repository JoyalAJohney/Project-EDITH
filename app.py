import cv2
import base64
import numpy as np
from capture_video import process_image
from flask import Flask, render_template, Response, request, jsonify



app = Flask(__name__)


def generate_frames():
    cap = cv2.VideoCapture(0)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.get_json()
    base64_image = data['image']

    response = process_image(base64_image)

    print(response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
