#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response

import pibrella
from flask import Flask, render_template

import io
import time
#import picamera
#from base_camera import BaseCamera

# import camera driver
#if os.environ.get('CAMERA'):
#    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
#else:
#    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
#from camera_pi import Camera
#class Camera(BaseCamera):
#    @staticmethod
#    def frames():
#        with picamera.PiCamera() as camera:
#            # let camera warm up
#            time.sleep(2)
#
#            stream = io.BytesIO()
#            for foo in camera.capture_continuous(stream, 'jpeg',
#                                                 use_video_port=True):
#                # return current frame
#                stream.seek(0)
#                yield stream.read()
#
#                # reset stream for next frame
#                stream.seek(0)
#                stream.truncate()
				
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO Pins Direction & Moteur
dirIn1=17
dirIn2=18
dirPWM=27
dirD1=22
dirEn=23
motIn1=6
motIn2=12
motPWM=13

#Tous les GPIO pololu sont OUTPUT
GPIO.setup(dirIn1, GPIO.OUT)
GPIO.setup(dirIn2, GPIO.OUT)
GPIO.setup(dirPWM, GPIO.OUT)
GPIO.setup(dirD1, GPIO.OUT)
GPIO.setup(dirEn, GPIO.OUT)
GPIO.setup(motIn1, GPIO.OUT)
GPIO.setup(motIn2, GPIO.OUT)
GPIO.setup(motPWM, GPIO.OUT)

@app.route('/')
@app.route("/<state>")
def update_robot(state=None):
    if state == 'forward':
        GPIO.output(motIn1, GPIO.HIGH)
        GPIO.output(motIn2, GPIO.LOW)
        GPIO.output(motPWM, GPIO.HIGH)
    if state == 'back':
        GPIO.output(motIn1, GPIO.LOW)
        GPIO.output(motIn2, GPIO.HIGH)
        GPIO.output(motPWM, GPIO.HIGH)
    if state == 'left':
        GPIO.output(dirIn1, GPIO.HIGH)
        GPIO.output(dirIn2, GPIO.LOW)
        GPIO.output(dirD1, GPIO.LOW)
        GPIO.output(dirPWM, GPIO.HIGH)
        GPIO.output(dirEn, GPIO.HIGH)
    if state == 'right':
        GPIO.output(dirIn1, GPIO.LOW)
        GPIO.output(dirIn2, GPIO.HIGH)
        GPIO.output(dirD1, GPIO.LOW)
        GPIO.output(dirPWM, GPIO.HIGH)
        GPIO.output(dirEn, GPIO.HIGH)
    if state == 'stop':
        GPIO.output(dirEn, GPIO.LOW) #Direction
        GPIO.output(motIn1, GPIO.LOW) #Moteur
        GPIO.output(motIn2, GPIO.LOW)
        GPIO.output(motPWM, GPIO.LOW)
    template_data = {
        'title' : state,
    }
    return render_template('main.html', **template_data)


#def gen(camera):
#    """Video streaming generator function."""
#    while True:
#        frame = camera.get_frame()
#        yield (b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#@app.route('/video_feed')
#def video_feed():
#    """Video streaming route. Put this in the src attribute of an img tag."""
#    return Response(gen(Camera()),
#                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, threaded=True)
